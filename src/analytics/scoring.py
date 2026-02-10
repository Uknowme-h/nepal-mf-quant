"""
Composite Fund Scoring & Ranking System

Combines multiple quantitative factors into a single composite score
for each fund, enabling relative ranking within the universe.

Factor weights (configurable):
    discount    35%   — deeper discount = higher score
    liquidity   20%   — higher volume = higher score
    maturity    15%   — closer to maturity = higher score
    momentum    10%   — positive price return = higher score
    volatility  10%   — lower volatility = higher score (inverse)
    disc_trend  10%   — narrowing discount = higher score

NaN handling: if a factor is NaN (insufficient data), it is excluded
from the weighted sum and remaining weights are re-normalized.

Output: data/processed/mf_scored.csv
"""

import numpy as np
import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


# Default factor weights — can be overridden in constructor
DEFAULT_WEIGHTS = {
    "discount_score": 0.30,
    "liquidity_score": 0.15,
    "maturity_score": 0.15,
    "nav_growth_score": 0.10,
    "momentum_score": 0.10,
    "volatility_score": 0.10,
    "disc_trend_score": 0.10,
}


class FundScorer:
    """
    Scores and ranks funds using percentile-based factor scoring
    with configurable weighted aggregation.
    """

    def __init__(self, project_root: Path, weights: dict | None = None):
        self.project_root = project_root
        self.weights = weights or DEFAULT_WEIGHTS.copy()

        # Input paths
        self.snapshot_path = project_root / "data" / "processed" / "mf_daily_snapshot.csv"
        self.returns_path = project_root / "data" / "processed" / "mf_returns.csv"
        self.risk_path = project_root / "data" / "processed" / "mf_risk_metrics.csv"
        self.universe_path = project_root / "data" / "raw" / "fund_universe.csv"

        # Output
        self.output_path = project_root / "data" / "processed" / "mf_scored.csv"

    # ------------------------------------------------------------------
    # Data loading
    # ------------------------------------------------------------------

    def load_data(self) -> pd.DataFrame:
        """
        Load and merge all input data into a single DataFrame.

        Filters to the latest date in the snapshot.
        """
        logger.info("Loading scoring inputs...")

        # Snapshot (required)
        if not self.snapshot_path.exists():
            raise FileNotFoundError(f"Snapshot not found: {self.snapshot_path}")
        snapshot = pd.read_csv(self.snapshot_path)
        snapshot["date"] = pd.to_datetime(snapshot["date"])

        # Filter to latest date only
        latest_date = snapshot["date"].max()
        snapshot = snapshot[snapshot["date"] == latest_date].copy()
        logger.info("  Snapshot: %d records (date: %s)", len(snapshot), latest_date.date())

        # Universe (for maturity)
        if self.universe_path.exists():
            universe = pd.read_csv(self.universe_path)
            universe["maturity_date"] = pd.to_datetime(universe["maturity_date"], errors="coerce")
            universe["days_to_maturity"] = (universe["maturity_date"] - latest_date).dt.days
            universe["years_to_maturity"] = (universe["days_to_maturity"] / 365.0).round(2)
            snapshot = snapshot.merge(
                universe[["symbol", "name", "fund_size", "days_to_maturity", "years_to_maturity"]],
                on="symbol", how="left",
            )
        else:
            logger.warning("  Fund universe not found — maturity & fund_size unavailable")
            snapshot["name"] = snapshot["symbol"]
            snapshot["fund_size"] = np.nan
            snapshot["days_to_maturity"] = np.nan
            snapshot["years_to_maturity"] = np.nan

        # Returns (optional)
        if self.returns_path.exists():
            returns_df = pd.read_csv(self.returns_path)
            returns_df["date"] = pd.to_datetime(returns_df["date"])
            returns_latest = returns_df[returns_df["date"] == latest_date].copy()
            ret_cols = ["symbol", "price_return_1d", "price_return_1w",
                        "discount_change_1d", "discount_change_1w", "nav_return_1m"]
            ret_cols = [c for c in ret_cols if c in returns_latest.columns]
            snapshot = snapshot.merge(
                returns_latest[ret_cols],
                on="symbol", how="left",
            )
            logger.info("  Returns: merged")
        else:
            logger.warning("  Returns file not found — momentum & trend scores will be NaN")
            for col in ["price_return_1d", "price_return_1w", "discount_change_1d", "discount_change_1w", "nav_return_1m"]:
                snapshot[col] = np.nan

        # Risk (optional)
        if self.risk_path.exists():
            risk_df = pd.read_csv(self.risk_path)
            snapshot = snapshot.merge(
                risk_df[["symbol", "parkinson_vol", "parkinson_vol_ann"]].drop_duplicates("symbol"),
                on="symbol", how="left",
            )
            logger.info("  Risk: merged")
        else:
            logger.warning("  Risk file not found — volatility score will be NaN")
            snapshot["parkinson_vol"] = np.nan
            snapshot["parkinson_vol_ann"] = np.nan

        return snapshot

    # ------------------------------------------------------------------
    # Factor scoring
    # ------------------------------------------------------------------

    @staticmethod
    def _percentile_rank(series: pd.Series, ascending: bool = True) -> pd.Series:
        """
        Compute percentile rank (0-100) for a series.

        ascending=True: higher raw value = higher score
        ascending=False: lower raw value = higher score (inverted)
        """
        if series.isna().all():
            return pd.Series(np.nan, index=series.index)

        if ascending:
            return series.rank(pct=True, na_option="keep") * 100
        else:
            return (1 - series.rank(pct=True, na_option="keep")) * 100

    def score_factors(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Compute individual factor scores (0-100 percentile) for each fund.
        """
        logger.info("Computing factor scores...")

        # 1. Discount score — deeper discount (more negative) = HIGHER score
        #    Invert: lower discount_pct = higher score
        df["discount_score"] = self._percentile_rank(df["discount_pct"], ascending=False)

        # 2. Liquidity score — higher volume = higher score
        df["liquidity_score"] = self._percentile_rank(df["volume"], ascending=True)

        # 3. Maturity score — closer to maturity (fewer days) = higher score
        df["maturity_score"] = self._percentile_rank(df["days_to_maturity"], ascending=False)

        # 4. NAV growth score — positive NAV return = higher score (fund manager performance)
        if "nav_return_1m" in df.columns and df["nav_return_1m"].notna().any():
            df["nav_growth_score"] = self._percentile_rank(df["nav_return_1m"], ascending=True)
        else:
            df["nav_growth_score"] = np.nan

        # 5. Momentum score — positive price return = higher score
        #    Use 1-week return if available, fallback to 1-day
        momentum_col = "price_return_1w"
        if momentum_col not in df.columns or df[momentum_col].isna().all():
            momentum_col = "price_return_1d"
        if momentum_col in df.columns:
            df["momentum_score"] = self._percentile_rank(df[momentum_col], ascending=True)
        else:
            df["momentum_score"] = np.nan

        # 6. Volatility score — lower Parkinson vol = higher score (inverse)
        if "parkinson_vol" in df.columns:
            df["volatility_score"] = self._percentile_rank(df["parkinson_vol"], ascending=False)
        else:
            df["volatility_score"] = np.nan

        # 7. Discount trend score — narrowing discount (positive change) = higher score
        trend_col = "discount_change_1w"
        if trend_col not in df.columns or df[trend_col].isna().all():
            trend_col = "discount_change_1d"
        if trend_col in df.columns:
            df["disc_trend_score"] = self._percentile_rank(df[trend_col], ascending=True)
        else:
            df["disc_trend_score"] = np.nan

        # Log coverage
        score_cols = ["discount_score", "liquidity_score", "maturity_score",
                      "nav_growth_score", "momentum_score", "volatility_score",
                      "disc_trend_score"]
        for col in score_cols:
            valid = df[col].notna().sum()
            logger.info("  %s: %d/%d valid", col, valid, len(df))

        return df

    def compute_composite_score(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Compute weighted composite score with NaN-aware re-normalization.

        If a factor is NaN for a fund, exclude it from the weighted sum
        and re-normalize the remaining weights so they still sum to 1.
        """
        logger.info("Computing composite scores...")

        score_cols = list(self.weights.keys())
        weight_vals = np.array([self.weights[c] for c in score_cols])

        composite_scores = []
        for _, row in df.iterrows():
            values = np.array([row.get(c, np.nan) for c in score_cols], dtype=float)
            mask = ~np.isnan(values)

            if mask.sum() == 0:
                composite_scores.append(np.nan)
                continue

            # Re-normalize weights for available factors
            available_weights = weight_vals[mask]
            available_weights = available_weights / available_weights.sum()
            available_values = values[mask]

            composite = np.dot(available_weights, available_values)
            composite_scores.append(round(composite, 2))

        df["composite_score"] = composite_scores

        # Rank by composite score (higher = better)
        # Use na_option="bottom" so NaN scores get the worst (highest) rank numbers
        df["rank"] = df["composite_score"].rank(ascending=False, method="min", na_option="bottom").astype(int)

        # Sort by rank
        df = df.sort_values("rank").reset_index(drop=True)

        # Log top 5
        logger.info("  Top 5 by composite score:")
        for _, row in df.head(5).iterrows():
            logger.info("    #%d  %-10s  score=%.1f  discount=%.2f%%",
                         row["rank"], row["symbol"], row["composite_score"],
                         row.get("discount_pct", np.nan))

        return df

    # ------------------------------------------------------------------
    # Output
    # ------------------------------------------------------------------

    def save(self, df: pd.DataFrame) -> None:
        """Save scored output to CSV."""
        output_cols = [
            "date", "symbol", "name", "nav", "ltp", "discount_pct",
            "volume", "fund_size", "days_to_maturity", "years_to_maturity",
            "price_return_1d", "price_return_1w",
            "discount_change_1d", "discount_change_1w",
            "parkinson_vol", "parkinson_vol_ann",
            "nav_return_1m",
            "discount_score", "liquidity_score", "maturity_score",
            "nav_growth_score", "momentum_score", "volatility_score",
            "disc_trend_score",
            "composite_score", "rank",
        ]

        # Keep only columns that exist
        output_cols = [c for c in output_cols if c in df.columns]
        out = df[output_cols].copy()

        # Format date
        if "date" in out.columns:
            out["date"] = pd.to_datetime(out["date"]).dt.strftime("%Y-%m-%d")

        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        out.to_csv(self.output_path, index=False)
        logger.info("Saved scored output to %s (%d funds)", self.output_path, len(out))

    # ------------------------------------------------------------------
    # Pipeline entry point
    # ------------------------------------------------------------------

    def run(self) -> pd.DataFrame:
        """Execute the full scoring pipeline."""
        logger.info("=" * 80)
        logger.info("FUND SCORING & RANKING")
        logger.info("=" * 80)

        df = self.load_data()
        df = self.score_factors(df)
        df = self.compute_composite_score(df)
        self.save(df)

        logger.info("=" * 80)
        logger.info("SCORING COMPLETE — %d funds ranked", len(df))
        logger.info("=" * 80)

        return df


def main():
    """Entry point."""
    project_root = Path(__file__).parent.parent.parent
    scorer = FundScorer(project_root)
    scorer.run()


if __name__ == "__main__":
    main()
