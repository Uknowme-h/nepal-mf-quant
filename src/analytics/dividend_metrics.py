"""
Dividend Metrics Calculator for Nepal Closed-End Mutual Funds

Computes per-fund dividend metrics from raw dividend history stored in
data/raw/dividends/{SYMBOL}.csv files.

Frequency metrics:
    dividend_count           — total number of dividend payments ever
    dividend_years           — distinct fiscal years with dividends
    dividend_consistency_pct — % of years active that paid dividends
    recent_dividend_years    — dividend count in the last 3 fiscal years

Yield metrics:
    avg_dividend_rate_pct    — arithmetic average of all cash dividend rates
    ttm_dividend_rate_pct    — trailing twelve months dividend yield
    max_dividend_rate_pct    — highest single payout (cash dividends)
    cumulative_dividend_pct  — sum of all cash dividend rates ever paid

Output: data/processed/mf_dividend_metrics.csv
"""

import csv
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


class DividendMetricsCalculator:
    """
    Calculates per-fund dividend metrics from per-fund CSV files.

    Designed for graceful degradation: funds with no dividend history
    receive NaN values so the NaN-aware scoring engine handles them
    correctly without penalising them.
    """

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.div_dir = project_root / "data" / "raw" / "dividends"
        self.universe_path = project_root / "data" / "raw" / "fund_universe.csv"
        self.output_path = project_root / "data" / "processed" / "mf_dividend_metrics.csv"

    # ------------------------------------------------------------------
    # Data loading
    # ------------------------------------------------------------------

    def _load_fund_dividends(self, symbol: str) -> pd.DataFrame:
        """Load raw dividend CSV for a single fund. Returns empty DF if missing."""
        path = self.div_dir / f"{symbol}.csv"
        if not path.exists():
            return pd.DataFrame()
        try:
            df = pd.read_csv(path, dtype=str)
            df["dividend_rate_pct"] = pd.to_numeric(
                df["dividend_rate_pct"], errors="coerce"
            )
            return df
        except Exception as exc:
            logger.warning("%s: could not load dividend CSV: %s", symbol, exc)
            return pd.DataFrame()

    def _load_universe(self) -> pd.DataFrame:
        """Load fund universe to get inception/listing dates and fund names."""
        if not self.universe_path.exists():
            logger.warning("Fund universe not found — consistency % will be NaN")
            return pd.DataFrame()
        try:
            df = pd.read_csv(self.universe_path)
            # Use maturity_date and fund_size as proxies; we don't have
            # inception dates but we can estimate years active from history.
            return df
        except Exception as exc:
            logger.warning("Could not load fund universe: %s", exc)
            return pd.DataFrame()

    # ------------------------------------------------------------------
    # Per-fund metric computation
    # ------------------------------------------------------------------

    def compute_fund_metrics(self, symbol: str, div_df: pd.DataFrame) -> Dict:
        """
        Compute all dividend metrics for a single fund.

        Returns a dict with all metric keys.  NaN values where
        insufficient data is available.
        """
        base: Dict = {
            "symbol": symbol,
            "dividend_count": 0,
            "dividend_years": 0,
            "dividend_consistency_pct": np.nan,
            "recent_dividend_years": 0,
            "avg_dividend_rate_pct": np.nan,
            "ttm_dividend_rate_pct": np.nan,
            "max_dividend_rate_pct": np.nan,
            "cumulative_dividend_pct": np.nan,
        }

        if div_df.empty:
            return base

        # Work only with cash dividends for yield metrics; count all types for
        # frequency metrics (bonus and right shares also signal shareholder
        # returns even if they're not direct cash).
        all_rows = div_df.dropna(subset=["dividend_rate_pct"])
        cash_rows = all_rows[all_rows["dividend_type"].str.lower().str.strip() == "cash"]

        if all_rows.empty:
            return base

        # --- Frequency metrics ---
        base["dividend_count"] = len(all_rows)
        unique_years = all_rows["fiscal_year"].dropna().unique()
        base["dividend_years"] = len(unique_years)

        # Estimate years active from fiscal_year range
        year_numbers = []
        for fy in unique_years:
            m = __import__("re").search(r"(\d{4})", str(fy))
            if m:
                year_numbers.append(int(m.group(1)))

        if year_numbers:
            min_year = min(year_numbers)
            max_year = max(year_numbers)
            # Years in the range from first dividend year to most recent
            years_span = max(max_year - min_year + 1, 1)
            base["dividend_consistency_pct"] = round(
                len(unique_years) / years_span * 100, 2
            )

        # Recent dividend years (last 3 fiscal years based on year numbers)
        if year_numbers:
            recent_cutoff = max(year_numbers) - 2  # most recent 3 years
            recent_years = [y for y in year_numbers if y >= recent_cutoff]
            base["recent_dividend_years"] = len(
                all_rows[
                    all_rows["fiscal_year"].apply(
                        lambda fy: _extract_year(str(fy)) is not None
                        and _extract_year(str(fy)) >= recent_cutoff
                    )
                ]
            )

        # --- Cash yield metrics ---
        if not cash_rows.empty:
            rates = cash_rows["dividend_rate_pct"].dropna()
            if not rates.empty:
                base["avg_dividend_rate_pct"] = round(float(rates.mean()), 4)
                base["max_dividend_rate_pct"] = round(float(rates.max()), 4)
                base["cumulative_dividend_pct"] = round(float(rates.sum()), 4)

        # TTM: cash dividends with record_date within last 365 days
        ttm_cutoff = datetime.utcnow() - timedelta(days=365)
        if not cash_rows.empty and "record_date" in cash_rows.columns:
            ttm_mask = cash_rows["record_date"].apply(
                lambda d: _parse_date_safe(d) is not None
                and _parse_date_safe(d) >= ttm_cutoff
            )
            ttm_rows = cash_rows[ttm_mask]
            if not ttm_rows.empty:
                base["ttm_dividend_rate_pct"] = round(
                    float(ttm_rows["dividend_rate_pct"].sum()), 4
                )

        return base

    # ------------------------------------------------------------------
    # Full universe run
    # ------------------------------------------------------------------

    def run(self) -> pd.DataFrame:
        """
        Compute dividend metrics for all funds in the universe.

        Returns a DataFrame with one row per fund.
        """
        logger.info("=" * 80)
        logger.info("DIVIDEND METRICS CALCULATOR")
        logger.info("=" * 80)

        universe = self._load_universe()
        if not universe.empty and "symbol" in universe.columns:
            symbols = universe["symbol"].dropna().unique().tolist()
        else:
            # Fall back to scanning dividend files directly
            symbols = [p.stem for p in sorted(self.div_dir.glob("*.csv"))]

        if not symbols:
            logger.warning("No symbols found — returning empty metrics")
            empty = pd.DataFrame(columns=["symbol"] + _METRIC_COLS)
            self._save(empty)
            return empty

        logger.info("Computing dividend metrics for %d funds...", len(symbols))
        rows = []
        funds_with_data = 0
        for symbol in symbols:
            div_df = self._load_fund_dividends(symbol)
            if not div_df.empty:
                funds_with_data += 1
            metrics = self.compute_fund_metrics(symbol, div_df)
            rows.append(metrics)

        df = pd.DataFrame(rows)

        logger.info(
            "Metrics computed: %d/%d funds have dividend history",
            funds_with_data,
            len(symbols),
        )

        if funds_with_data > 0:
            logger.info(
                "  Avg dividend rate (across paying funds): %.2f%%",
                df["avg_dividend_rate_pct"].dropna().mean(),
            )
            logger.info(
                "  Max dividend count: %d (%s)",
                int(df["dividend_count"].max()),
                df.loc[df["dividend_count"].idxmax(), "symbol"],
            )

        self._save(df)

        logger.info("=" * 80)
        logger.info("DIVIDEND METRICS COMPLETE — %d funds", len(df))
        logger.info("=" * 80)

        return df

    # ------------------------------------------------------------------
    # Output
    # ------------------------------------------------------------------

    def _save(self, df: pd.DataFrame) -> None:
        """Save metrics to output CSV."""
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(self.output_path, index=False)
        logger.info("Saved dividend metrics: %s (%d rows)", self.output_path, len(df))


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------

_METRIC_COLS = [
    "dividend_count",
    "dividend_years",
    "dividend_consistency_pct",
    "recent_dividend_years",
    "avg_dividend_rate_pct",
    "ttm_dividend_rate_pct",
    "max_dividend_rate_pct",
    "cumulative_dividend_pct",
]


def _extract_year(raw: str) -> Optional[int]:
    """Extract a 4-digit year from a fiscal year string like '2079/80' or '2022'."""
    import re
    m = re.search(r"(\d{4})", raw)
    if m:
        return int(m.group(1))
    return None


def _parse_date_safe(raw) -> Optional[datetime]:
    """Parse a date string to datetime; return None on failure."""
    if not raw or str(raw).strip() in ("", "nan", "NaT", "-", "—"):
        return None
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"):
        try:
            return datetime.strptime(str(raw).strip(), fmt)
        except ValueError:
            continue
    return None


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    """Standalone entry point."""
    import sys
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    project_root = Path(__file__).parent.parent.parent
    calc = DividendMetricsCalculator(project_root)
    calc.run()


if __name__ == "__main__":
    main()
