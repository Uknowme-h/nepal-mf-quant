"""
Risk Metrics for Closed-End Mutual Funds

Uses OHLC data (open/high/low/close) — previously unused — to compute
volatility estimates without requiring long return histories.

Metrics:
- Parkinson volatility: Uses high/low range, more efficient than close-to-close
- Intraday range ratio: (high - low) / ltp as a spread/friction metric
- Close-to-close volatility: Standard deviation of daily log returns (rolling)
- Volume stability: Coefficient of variation of daily volume
- Max drawdown: Peak-to-trough decline from price series

Output: data/processed/mf_risk_metrics.csv
"""

import numpy as np
import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class RiskMetrics:
    """
    Computes risk metrics from OHLC market data and price history.

    Key design: leverages the open/high/low columns from market_prices.csv
    that are currently unused by the rest of the pipeline.
    """

    # Configurable risk-free rate (annualized, Nepal T-bill proxy ~5%)
    RISK_FREE_RATE = 5.0

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.price_path = project_root / "data" / "raw" / "market_prices.csv"
        self.returns_path = project_root / "data" / "processed" / "mf_returns.csv"
        self.output_path = project_root / "data" / "processed" / "mf_risk_metrics.csv"

    # ------------------------------------------------------------------
    # Data loading
    # ------------------------------------------------------------------

    def load_prices(self) -> pd.DataFrame:
        """Load market_prices.csv with OHLC columns."""
        if not self.price_path.exists():
            raise FileNotFoundError(f"Market prices not found: {self.price_path}")

        df = pd.read_csv(self.price_path)
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values(["symbol", "date"]).reset_index(drop=True)

        # Validate OHLC columns exist
        required = ["date", "symbol", "ltp", "open", "high", "low", "volume"]
        missing = [c for c in required if c not in df.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

        logger.info("Loaded %d OHLC records for %d symbols", len(df), df["symbol"].nunique())
        return df

    def load_returns(self) -> pd.DataFrame:
        """Load pre-computed returns if available."""
        if not self.returns_path.exists():
            logger.warning("Returns file not found — Sharpe ratio will be NaN")
            return pd.DataFrame()

        df = pd.read_csv(self.returns_path)
        df["date"] = pd.to_datetime(df["date"])
        return df

    # ------------------------------------------------------------------
    # Volatility metrics
    # ------------------------------------------------------------------

    def calculate_parkinson_volatility(self, prices: pd.DataFrame) -> pd.DataFrame:
        """
        Parkinson volatility estimator using high/low range.

        Formula: sigma_P = sqrt( 1/(4*n*ln2) * sum( (ln(H/L))^2 ) )

        More efficient than close-to-close for small samples because it
        uses intraday range information — exactly what our OHLC data provides.
        Annualized by multiplying by sqrt(252).
        """
        logger.info("Calculating Parkinson volatility...")

        results = []
        for symbol, grp in prices.groupby("symbol"):
            grp = grp.sort_values("date").copy()

            # Avoid division by zero
            valid = grp[(grp["high"] > 0) & (grp["low"] > 0) & (grp["high"] >= grp["low"])].copy()

            if len(valid) < 1:
                results.append({"symbol": symbol, "parkinson_vol": np.nan, "parkinson_vol_ann": np.nan})
                continue

            log_hl = np.log(valid["high"] / valid["low"])
            n = len(valid)

            # Daily Parkinson variance
            parkinson_var = (1.0 / (4.0 * n * np.log(2))) * (log_hl ** 2).sum()
            parkinson_daily = np.sqrt(parkinson_var)

            # Annualized
            parkinson_ann = parkinson_daily * np.sqrt(252)

            results.append({
                "symbol": symbol,
                "parkinson_vol": round(parkinson_daily * 100, 4),      # daily, as %
                "parkinson_vol_ann": round(parkinson_ann * 100, 2),    # annualized, as %
            })

        df = pd.DataFrame(results)
        valid_count = df["parkinson_vol"].notna().sum()
        logger.info("  Parkinson vol: %d/%d symbols computed", valid_count, len(df))
        return df

    def calculate_intraday_range(self, prices: pd.DataFrame) -> pd.DataFrame:
        """
        Intraday range ratio: (high - low) / ltp per record.

        A simple friction/spread metric computable from day 1.
        High values = wide intraday swings = higher execution risk.
        """
        logger.info("Calculating intraday range...")

        prices = prices.copy()
        prices["intraday_range"] = np.where(
            prices["ltp"] > 0,
            ((prices["high"] - prices["low"]) / prices["ltp"] * 100).round(4),
            np.nan,
        )

        # Per-symbol average (latest date and rolling mean)
        latest_date = prices["date"].max()
        latest = prices[prices["date"] == latest_date][["symbol", "intraday_range"]].copy()

        # Also compute mean across all available days
        mean_range = (
            prices.groupby("symbol")["intraday_range"]
            .mean()
            .reset_index()
            .rename(columns={"intraday_range": "avg_intraday_range"})
        )
        latest = latest.merge(mean_range, on="symbol", how="left")
        latest["avg_intraday_range"] = latest["avg_intraday_range"].round(4)

        return latest

    def calculate_return_volatility(self, prices: pd.DataFrame) -> pd.DataFrame:
        """
        Close-to-close return volatility (rolling 5-day and 22-day windows).

        Uses log returns: r_t = ln(P_t / P_{t-1})
        """
        logger.info("Calculating return volatility...")

        results = []
        for symbol, grp in prices.groupby("symbol"):
            grp = grp.sort_values("date").copy()
            n = len(grp)

            grp["log_return"] = np.log(grp["ltp"] / grp["ltp"].shift(1))

            vol_5d = grp["log_return"].rolling(5).std() * 100 if n >= 5 else pd.Series(np.nan, index=grp.index)
            vol_22d = grp["log_return"].rolling(22).std() * 100 if n >= 22 else pd.Series(np.nan, index=grp.index)

            # Take latest values
            results.append({
                "symbol": symbol,
                "return_vol_5d": round(vol_5d.iloc[-1], 4) if pd.notna(vol_5d.iloc[-1]) else np.nan,
                "return_vol_22d": round(vol_22d.iloc[-1], 4) if n >= 22 and pd.notna(vol_22d.iloc[-1]) else np.nan,
            })

        return pd.DataFrame(results)

    def calculate_volume_stability(self, prices: pd.DataFrame) -> pd.DataFrame:
        """
        Volume coefficient of variation per symbol.

        CV = std(volume) / mean(volume)
        High CV = erratic volume = liquidity risk.
        """
        logger.info("Calculating volume stability...")

        results = []
        for symbol, grp in prices.groupby("symbol"):
            vol_mean = grp["volume"].mean()
            vol_std = grp["volume"].std()

            if vol_mean > 0 and pd.notna(vol_std):
                cv = round(vol_std / vol_mean, 4)
            else:
                cv = np.nan

            results.append({"symbol": symbol, "volume_cv": cv})

        df = pd.DataFrame(results)
        logger.info("  Volume CV: %d/%d symbols computed", df["volume_cv"].notna().sum(), len(df))
        return df

    def calculate_max_drawdown(self, prices: pd.DataFrame) -> pd.DataFrame:
        """
        Maximum drawdown from peak for each symbol.

        MDD = (trough - peak) / peak
        Requires at least 2 data points.
        """
        logger.info("Calculating max drawdown...")

        results = []
        for symbol, grp in prices.groupby("symbol"):
            grp = grp.sort_values("date")
            if len(grp) < 2:
                results.append({"symbol": symbol, "max_drawdown": np.nan})
                continue

            cummax = grp["ltp"].cummax()
            drawdown = (grp["ltp"] - cummax) / cummax
            mdd = drawdown.min() * 100  # as percentage

            results.append({"symbol": symbol, "max_drawdown": round(mdd, 2)})

        return pd.DataFrame(results)

    def calculate_sharpe_ratio(self, returns_df: pd.DataFrame) -> pd.DataFrame:
        """
        Sharpe ratio = (mean_return - risk_free) / volatility

        Uses daily price_return_1d from the returns module.
        Annualized: multiply mean by 252, vol by sqrt(252).
        Requires at least 22 data points for meaningful result.
        """
        logger.info("Calculating Sharpe ratio...")

        if returns_df.empty or "price_return_1d" not in returns_df.columns:
            logger.warning("  No return data — Sharpe ratio will be NaN")
            return pd.DataFrame(columns=["symbol", "sharpe_1m"])

        daily_rf = self.RISK_FREE_RATE / 252  # daily risk-free rate in %

        results = []
        for symbol, grp in returns_df.groupby("symbol"):
            valid = grp["price_return_1d"].dropna()
            if len(valid) < 22:
                results.append({"symbol": symbol, "sharpe_1m": np.nan})
                continue

            mean_ret = valid.mean()
            std_ret = valid.std()

            if std_ret > 0:
                # Daily Sharpe, annualized
                daily_sharpe = (mean_ret - daily_rf) / std_ret
                ann_sharpe = daily_sharpe * np.sqrt(252)
                results.append({"symbol": symbol, "sharpe_1m": round(ann_sharpe, 2)})
            else:
                results.append({"symbol": symbol, "sharpe_1m": np.nan})

        df = pd.DataFrame(results)
        valid_count = df["sharpe_1m"].notna().sum()
        logger.info("  Sharpe ratio: %d/%d symbols (need >=22 daily returns)", valid_count, len(df))
        return df

    # ------------------------------------------------------------------
    # Output
    # ------------------------------------------------------------------

    def merge_and_save(self, *metric_dfs: pd.DataFrame) -> pd.DataFrame:
        """Merge all risk metric DataFrames on symbol and save."""
        # Start with first non-empty DataFrame
        out = None
        for df in metric_dfs:
            if df.empty:
                continue
            if out is None:
                out = df.copy()
            else:
                out = out.merge(df, on="symbol", how="outer")

        if out is None or out.empty:
            logger.warning("No risk metrics computed")
            out = pd.DataFrame(columns=["symbol"])

        # Add date column (latest date from prices)
        prices = pd.read_csv(self.price_path)
        prices["date"] = pd.to_datetime(prices["date"])
        latest_date = prices["date"].max()
        out.insert(0, "date", latest_date.strftime("%Y-%m-%d"))

        # Save
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        out.to_csv(self.output_path, index=False)
        logger.info("Saved risk metrics to %s (%d symbols)", self.output_path, len(out))

        return out

    # ------------------------------------------------------------------
    # Pipeline entry point
    # ------------------------------------------------------------------

    def run(self) -> pd.DataFrame:
        """Execute the full risk metrics pipeline."""
        logger.info("=" * 80)
        logger.info("RISK METRICS")
        logger.info("=" * 80)

        prices = self.load_prices()
        returns_df = self.load_returns()

        parkinson = self.calculate_parkinson_volatility(prices)
        intraday = self.calculate_intraday_range(prices)
        ret_vol = self.calculate_return_volatility(prices)
        vol_stability = self.calculate_volume_stability(prices)
        drawdown = self.calculate_max_drawdown(prices)
        sharpe = self.calculate_sharpe_ratio(returns_df)

        result = self.merge_and_save(
            parkinson, intraday, ret_vol, vol_stability, drawdown, sharpe,
        )

        logger.info("=" * 80)
        logger.info("RISK METRICS COMPLETE — %d symbols", len(result))
        logger.info("=" * 80)

        return result


def main():
    """Entry point."""
    project_root = Path(__file__).parent.parent.parent
    risk = RiskMetrics(project_root)
    risk.run()


if __name__ == "__main__":
    main()
