"""
Data Quality Validation Layer

Runs pre-analytics checks on scraped data to surface staleness,
outliers, anomalies, and coverage gaps before they silently corrupt
downstream metrics.

Checks:
- NAV staleness: warns if latest NAV is >45 days old
- Price outliers: flags >15% daily LTP moves
- Volume anomalies: flags >80% drop from rolling average
- Coverage: symbols in universe but missing price/NAV data
- OHLC consistency: high >= low, high >= open, etc.

Output: data/processed/mf_data_quality.csv
"""

import numpy as np
import pandas as pd
import logging
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)


class DataQualityChecker:
    """
    Validates data quality across all raw inputs.
    Produces a per-symbol quality report and logs warnings.
    """

    # Thresholds
    NAV_STALENESS_DAYS = 45
    PRICE_OUTLIER_PCT = 15.0
    VOLUME_DROP_PCT = 80.0

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.price_path = project_root / "data" / "raw" / "market_prices.csv"
        self.nav_dir = project_root / "data" / "raw" / "nav"
        self.universe_path = project_root / "data" / "raw" / "fund_universe.csv"
        self.output_path = project_root / "data" / "processed" / "mf_data_quality.csv"

    # ------------------------------------------------------------------
    # Individual checks
    # ------------------------------------------------------------------

    def check_nav_staleness(self, today: datetime) -> pd.DataFrame:
        """
        Check how old each fund's latest NAV data is.

        Returns DataFrame with symbol, latest_nav_date, nav_age_days, nav_stale flag.
        """
        logger.info("Checking NAV staleness...")

        if not self.nav_dir.exists():
            logger.warning("  NAV directory missing")
            return pd.DataFrame(columns=["symbol", "latest_nav_date", "nav_age_days", "nav_stale"])

        records = []
        for nav_file in self.nav_dir.glob("*.csv"):
            symbol = nav_file.stem
            try:
                df = pd.read_csv(nav_file)
                df["date"] = pd.to_datetime(df["date"])
                latest = df["date"].max()
                age_days = (today - latest).days
                records.append({
                    "symbol": symbol,
                    "latest_nav_date": latest.strftime("%Y-%m-%d"),
                    "nav_age_days": age_days,
                    "nav_stale": age_days > self.NAV_STALENESS_DAYS,
                })
            except Exception as exc:
                logger.warning("  Failed to check %s: %s", nav_file.name, exc)
                records.append({
                    "symbol": symbol,
                    "latest_nav_date": None,
                    "nav_age_days": None,
                    "nav_stale": True,
                })

        result = pd.DataFrame(records)
        stale_count = result["nav_stale"].sum()
        if stale_count > 0:
            logger.warning("  %d/%d funds have stale NAV (>%d days old)",
                           stale_count, len(result), self.NAV_STALENESS_DAYS)
        else:
            logger.info("  All NAV data is fresh (<=%d days)", self.NAV_STALENESS_DAYS)

        return result

    def check_price_outliers(self, prices: pd.DataFrame) -> pd.DataFrame:
        """
        Flag symbols with >15% daily price moves (possible data errors).
        """
        logger.info("Checking price outliers...")

        if prices.empty:
            return pd.DataFrame(columns=["symbol", "price_outlier", "max_daily_move_pct"])

        results = []
        for symbol, grp in prices.groupby("symbol"):
            grp = grp.sort_values("date")
            if len(grp) < 2:
                results.append({
                    "symbol": symbol,
                    "price_outlier": False,
                    "max_daily_move_pct": np.nan,
                })
                continue

            pct_change = grp["ltp"].pct_change().abs() * 100
            max_move = pct_change.max()
            outlier = max_move > self.PRICE_OUTLIER_PCT if pd.notna(max_move) else False

            if outlier:
                logger.warning("  %s: %.1f%% daily price move detected", symbol, max_move)

            results.append({
                "symbol": symbol,
                "price_outlier": outlier,
                "max_daily_move_pct": round(max_move, 2) if pd.notna(max_move) else np.nan,
            })

        return pd.DataFrame(results)

    def check_volume_anomalies(self, prices: pd.DataFrame) -> pd.DataFrame:
        """
        Flag symbols where latest volume dropped >80% from mean.
        """
        logger.info("Checking volume anomalies...")

        if prices.empty:
            return pd.DataFrame(columns=["symbol", "volume_anomaly", "volume_drop_pct"])

        results = []
        for symbol, grp in prices.groupby("symbol"):
            grp = grp.sort_values("date")
            if len(grp) < 2:
                results.append({
                    "symbol": symbol,
                    "volume_anomaly": False,
                    "volume_drop_pct": np.nan,
                })
                continue

            mean_vol = grp["volume"].mean()
            latest_vol = grp["volume"].iloc[-1]

            if mean_vol > 0:
                drop_pct = ((mean_vol - latest_vol) / mean_vol) * 100
            else:
                drop_pct = 0

            anomaly = drop_pct > self.VOLUME_DROP_PCT

            if anomaly:
                logger.warning("  %s: volume dropped %.0f%% from mean", symbol, drop_pct)

            results.append({
                "symbol": symbol,
                "volume_anomaly": anomaly,
                "volume_drop_pct": round(drop_pct, 1),
            })

        return pd.DataFrame(results)

    def check_ohlc_consistency(self, prices: pd.DataFrame) -> pd.DataFrame:
        """
        Validate OHLC relationships: high >= low, high >= open, etc.
        """
        logger.info("Checking OHLC consistency...")

        if prices.empty:
            return pd.DataFrame(columns=["symbol", "ohlc_errors"])

        # Check per row
        issues = prices[
            (prices["high"] < prices["low"])
            | (prices["high"] < prices["open"])
            | (prices["low"] > prices["open"])
        ]

        error_counts = issues.groupby("symbol").size().reset_index(name="ohlc_errors")

        # Ensure all symbols are represented
        all_symbols = prices[["symbol"]].drop_duplicates()
        result = all_symbols.merge(error_counts, on="symbol", how="left")
        result["ohlc_errors"] = result["ohlc_errors"].fillna(0).astype(int)

        bad = result[result["ohlc_errors"] > 0]
        if len(bad) > 0:
            logger.warning("  %d symbols have OHLC consistency issues", len(bad))
        else:
            logger.info("  All OHLC data consistent")

        return result

    def check_coverage(self, prices: pd.DataFrame) -> pd.DataFrame:
        """
        Check which universe symbols have price and NAV data.
        """
        logger.info("Checking data coverage...")

        if not self.universe_path.exists():
            logger.warning("  Fund universe not found")
            return pd.DataFrame(columns=["symbol", "has_price_data", "has_nav_data"])

        universe = pd.read_csv(self.universe_path)
        symbols = set(universe["symbol"].unique())
        price_symbols = set(prices["symbol"].unique()) if not prices.empty else set()

        nav_symbols = set()
        if self.nav_dir.exists():
            nav_symbols = {f.stem for f in self.nav_dir.glob("*.csv")}

        records = []
        for sym in sorted(symbols):
            has_price = sym in price_symbols
            has_nav = sym in nav_symbols
            if not has_price:
                logger.warning("  %s: missing price data", sym)
            if not has_nav:
                logger.warning("  %s: missing NAV data", sym)
            records.append({
                "symbol": sym,
                "has_price_data": has_price,
                "has_nav_data": has_nav,
            })

        result = pd.DataFrame(records)
        missing_price = (~result["has_price_data"]).sum()
        missing_nav = (~result["has_nav_data"]).sum()
        logger.info("  Coverage: %d/%d with prices, %d/%d with NAV",
                     len(result) - missing_price, len(result),
                     len(result) - missing_nav, len(result))

        return result

    # ------------------------------------------------------------------
    # Output
    # ------------------------------------------------------------------

    def run(self) -> pd.DataFrame:
        """Execute all data quality checks and save report."""
        logger.info("=" * 80)
        logger.info("DATA QUALITY VALIDATION")
        logger.info("=" * 80)

        today = datetime.now()

        # Load prices once
        prices = pd.DataFrame()
        if self.price_path.exists():
            prices = pd.read_csv(self.price_path)
            prices["date"] = pd.to_datetime(prices["date"])
            prices = prices.sort_values(["symbol", "date"])

        # Run all checks
        nav_staleness = self.check_nav_staleness(today)
        price_outliers = self.check_price_outliers(prices)
        volume_anomalies = self.check_volume_anomalies(prices)
        ohlc_checks = self.check_ohlc_consistency(prices)
        coverage = self.check_coverage(prices)

        # Merge all on symbol
        result = coverage.copy()
        for check_df in [nav_staleness, price_outliers, volume_anomalies, ohlc_checks]:
            if not check_df.empty:
                result = result.merge(check_df, on="symbol", how="outer")

        # Add overall quality flag
        issue_cols = ["nav_stale", "price_outlier", "volume_anomaly"]
        existing_issue_cols = [c for c in issue_cols if c in result.columns]

        if existing_issue_cols:
            result["has_issues"] = result[existing_issue_cols].any(axis=1)
        else:
            result["has_issues"] = False

        # Add check timestamp
        result.insert(0, "checked_at", today.strftime("%Y-%m-%d %H:%M"))

        # Save
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        result.to_csv(self.output_path, index=False)

        # Summary
        issues = result["has_issues"].sum() if "has_issues" in result.columns else 0
        logger.info("")
        logger.info("=" * 80)
        logger.info("DATA QUALITY SUMMARY")
        logger.info("  Symbols checked: %d", len(result))
        logger.info("  Symbols with issues: %d", issues)
        logger.info("  Report saved: %s", self.output_path)
        logger.info("=" * 80)

        return result


def main():
    """Entry point."""
    project_root = Path(__file__).parent.parent.parent
    checker = DataQualityChecker(project_root)
    checker.run()


if __name__ == "__main__":
    main()
