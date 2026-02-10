"""
Returns Calculator for Closed-End Mutual Funds

Computes price returns, discount change, and NAV growth from available data.
All calculations use graceful degradation — returns NaN when insufficient
data is available, with logged warnings.

Metrics:
- Price returns: 1-day, 1-week (5 trading days), 1-month (22 trading days)
- Discount change: 1-day, 1-week change in discount_pct
- NAV return: Month-over-month NAV growth (requires NAV history)

Output: data/processed/mf_returns.csv
"""

import numpy as np
import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class ReturnsCalculator:
    """
    Calculates rolling returns from market prices, NAV history,
    and discount snapshots.

    Designed for graceful degradation: each return window checks
    whether sufficient data points exist before computing.
    """

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.price_path = project_root / "data" / "raw" / "market_prices.csv"
        self.snapshot_path = project_root / "data" / "processed" / "mf_daily_snapshot.csv"
        self.nav_dir = project_root / "data" / "raw" / "nav"
        self.output_path = project_root / "data" / "processed" / "mf_returns.csv"

    # ------------------------------------------------------------------
    # Data loading
    # ------------------------------------------------------------------

    def load_prices(self) -> pd.DataFrame:
        """Load market_prices.csv with date parsing."""
        if not self.price_path.exists():
            raise FileNotFoundError(f"Market prices not found: {self.price_path}")

        df = pd.read_csv(self.price_path)
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values(["symbol", "date"]).reset_index(drop=True)
        logger.info("Loaded %d price records for %d symbols", len(df), df["symbol"].nunique())
        return df

    def load_snapshot(self) -> pd.DataFrame:
        """Load mf_daily_snapshot.csv for discount history."""
        if not self.snapshot_path.exists():
            raise FileNotFoundError(f"Snapshot not found: {self.snapshot_path}")

        df = pd.read_csv(self.snapshot_path)
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values(["symbol", "date"]).reset_index(drop=True)
        return df

    def load_all_nav(self) -> pd.DataFrame:
        """Load all NAV CSV files into a single DataFrame."""
        if not self.nav_dir.exists():
            logger.warning("NAV directory not found: %s", self.nav_dir)
            return pd.DataFrame(columns=["date", "symbol", "nav"])

        frames = []
        for nav_file in self.nav_dir.glob("*.csv"):
            try:
                tmp = pd.read_csv(nav_file)
                tmp["date"] = pd.to_datetime(tmp["date"])
                tmp["symbol"] = nav_file.stem
                frames.append(tmp[["date", "symbol", "nav"]])
            except Exception as exc:
                logger.warning("Failed to load %s: %s", nav_file.name, exc)

        if not frames:
            return pd.DataFrame(columns=["date", "symbol", "nav"])

        df = pd.concat(frames, ignore_index=True).sort_values(["symbol", "date"])
        logger.info("Loaded NAV data for %d symbols (%d records)", df["symbol"].nunique(), len(df))
        return df

    # ------------------------------------------------------------------
    # Return calculations
    # ------------------------------------------------------------------

    def _pct_change_safe(self, series: pd.Series, periods: int) -> pd.Series:
        """Percentage change with NaN for insufficient history."""
        if len(series) < periods + 1:
            return pd.Series(np.nan, index=series.index)
        return series.pct_change(periods=periods) * 100

    def calculate_price_returns(self, prices: pd.DataFrame) -> pd.DataFrame:
        """
        Compute rolling price returns per symbol.

        Returns DataFrame with columns:
            symbol, date, ltp, price_return_1d, price_return_1w, price_return_1m
        """
        logger.info("Calculating price returns...")

        results = []
        for symbol, grp in prices.groupby("symbol"):
            grp = grp.sort_values("date").copy()
            n = len(grp)

            grp["price_return_1d"] = self._pct_change_safe(grp["ltp"], 1)
            grp["price_return_1w"] = (
                self._pct_change_safe(grp["ltp"], 5) if n >= 6 else np.nan
            )
            grp["price_return_1m"] = (
                self._pct_change_safe(grp["ltp"], 22) if n >= 23 else np.nan
            )
            results.append(grp)

        df = pd.concat(results, ignore_index=True)

        for col in ["price_return_1d", "price_return_1w", "price_return_1m"]:
            valid = df[col].notna().sum()
            total = len(df)
            logger.info("  %s: %d/%d valid (%.0f%%)", col, valid, total,
                         valid / total * 100 if total else 0)

        return df

    def calculate_discount_change(self, snapshot: pd.DataFrame) -> pd.DataFrame:
        """
        Compute change in discount_pct over 1-day and 1-week windows.

        A narrowing discount (positive change toward 0) is a bullish signal.
        A widening discount (negative change away from 0) is bearish.
        """
        logger.info("Calculating discount change...")

        results = []
        for symbol, grp in snapshot.groupby("symbol"):
            grp = grp.sort_values("date").copy()
            n = len(grp)

            grp["discount_change_1d"] = grp["discount_pct"].diff(1) if n >= 2 else np.nan
            grp["discount_change_1w"] = grp["discount_pct"].diff(5) if n >= 6 else np.nan

            results.append(grp[["date", "symbol", "discount_pct", "discount_change_1d", "discount_change_1w"]])

        if not results:
            return pd.DataFrame()

        return pd.concat(results, ignore_index=True)

    def calculate_nav_returns(self, nav_df: pd.DataFrame) -> pd.DataFrame:
        """
        Compute month-over-month NAV growth per symbol.

        With a single data point per fund, this returns NaN.
        Becomes useful as monthly scrapes accumulate.
        """
        logger.info("Calculating NAV returns...")

        if nav_df.empty:
            logger.warning("  No NAV data available — skipping NAV returns")
            return pd.DataFrame(columns=["date", "symbol", "nav_return_1m"])

        results = []
        for symbol, grp in nav_df.groupby("symbol"):
            grp = grp.sort_values("date").copy()
            if len(grp) >= 2:
                grp["nav_return_1m"] = grp["nav"].pct_change() * 100
            else:
                grp["nav_return_1m"] = np.nan
            results.append(grp[["date", "symbol", "nav_return_1m"]])

        df = pd.concat(results, ignore_index=True)
        valid = df["nav_return_1m"].notna().sum()
        logger.info("  NAV returns: %d/%d valid (need >=2 monthly NAV points per fund)",
                     valid, len(df))
        return df

    # ------------------------------------------------------------------
    # Output
    # ------------------------------------------------------------------

    def merge_and_save(
        self,
        price_returns: pd.DataFrame,
        discount_changes: pd.DataFrame,
        nav_returns: pd.DataFrame,
    ) -> pd.DataFrame:
        """Merge all return metrics and save to CSV."""
        out = price_returns[
            ["date", "symbol", "ltp", "price_return_1d", "price_return_1w", "price_return_1m"]
        ].copy()

        # Merge discount changes
        if not discount_changes.empty:
            out = out.merge(
                discount_changes[["date", "symbol", "discount_change_1d", "discount_change_1w"]],
                on=["date", "symbol"],
                how="left",
            )
        else:
            out["discount_change_1d"] = np.nan
            out["discount_change_1w"] = np.nan

        # Merge NAV returns (monthly, so broadcast latest per symbol)
        if not nav_returns.empty:
            nav_latest = (
                nav_returns.sort_values("date")
                .groupby("symbol")
                .last()
                .reset_index()[["symbol", "nav_return_1m"]]
            )
            out = out.merge(nav_latest, on="symbol", how="left")
        else:
            out["nav_return_1m"] = np.nan

        # Round
        numeric_cols = [
            "price_return_1d", "price_return_1w", "price_return_1m",
            "discount_change_1d", "discount_change_1w", "nav_return_1m",
        ]
        for col in numeric_cols:
            if col in out.columns:
                out[col] = out[col].round(2)

        # Save
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        out_csv = out.copy()
        out_csv["date"] = out_csv["date"].dt.strftime("%Y-%m-%d")
        out_csv.to_csv(self.output_path, index=False)
        logger.info("Saved returns to %s (%d records)", self.output_path, len(out_csv))

        return out

    # ------------------------------------------------------------------
    # Pipeline entry point
    # ------------------------------------------------------------------

    def run(self) -> pd.DataFrame:
        """Execute the full returns calculation pipeline."""
        logger.info("=" * 80)
        logger.info("RETURNS CALCULATOR")
        logger.info("=" * 80)

        prices = self.load_prices()
        snapshot = self.load_snapshot()
        nav_df = self.load_all_nav()

        price_returns = self.calculate_price_returns(prices)
        discount_changes = self.calculate_discount_change(snapshot)
        nav_returns = self.calculate_nav_returns(nav_df)

        result = self.merge_and_save(price_returns, discount_changes, nav_returns)

        logger.info("=" * 80)
        logger.info("RETURNS COMPLETE — %d records", len(result))
        logger.info("=" * 80)

        return result


def main():
    """Entry point."""
    project_root = Path(__file__).parent.parent.parent
    calc = ReturnsCalculator(project_root)
    calc.run()


if __name__ == "__main__":
    main()
