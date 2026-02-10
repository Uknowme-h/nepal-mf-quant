"""
Report Generator for Nepal MF Quant

Produces detailed markdown and CSV reports from all processed analytics data.
Generates:
    - reports/latest_rankings.md   — Full quant analysis report
    - reports/metrics_table.csv    — Complete metrics for all funds

Reads from: data/processed/mf_scored.csv, mf_decision_table.csv,
            mf_risk_metrics.csv, mf_returns.csv, mf_data_quality.csv,
            data/history/mf_decision_history.csv, data/raw/fund_universe.csv
"""

import numpy as np
import pandas as pd
import logging
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)


class ReportGenerator:
    """
    Generates comprehensive markdown and CSV reports from all
    processed analytics outputs.
    """

    def __init__(self, project_root: Path):
        self.project_root = project_root

        # Inputs
        self.scored_path = project_root / "data" / "processed" / "mf_scored.csv"
        self.decision_path = project_root / "data" / "processed" / "mf_decision_table.csv"
        self.risk_path = project_root / "data" / "processed" / "mf_risk_metrics.csv"
        self.returns_path = project_root / "data" / "processed" / "mf_returns.csv"
        self.quality_path = project_root / "data" / "processed" / "mf_data_quality.csv"
        self.history_path = project_root / "data" / "history" / "mf_decision_history.csv"
        self.universe_path = project_root / "data" / "raw" / "fund_universe.csv"
        self.snapshot_path = project_root / "data" / "processed" / "mf_daily_snapshot.csv"

        # Outputs
        self.md_path = project_root / "reports" / "latest_rankings.md"
        self.csv_path = project_root / "reports" / "metrics_table.csv"

    # ------------------------------------------------------------------
    # Data loading helpers
    # ------------------------------------------------------------------

    def _load_csv(self, path: Path, date_cols: list | None = None) -> pd.DataFrame:
        if not path.exists():
            logger.warning("Report input missing: %s", path)
            return pd.DataFrame()
        df = pd.read_csv(path)
        for col in (date_cols or []):
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors="coerce")
        return df

    def load_all(self) -> dict:
        """Load all available input DataFrames."""
        data = {
            "scored": self._load_csv(self.scored_path, ["date"]),
            "decisions": self._load_csv(self.decision_path, ["date"]),
            "risk": self._load_csv(self.risk_path),
            "returns": self._load_csv(self.returns_path, ["date"]),
            "quality": self._load_csv(self.quality_path),
            "history": self._load_csv(self.history_path, ["date"]),
            "universe": self._load_csv(self.universe_path),
            "snapshot": self._load_csv(self.snapshot_path, ["date"]),
        }
        loaded = sum(1 for v in data.values() if not v.empty)
        logger.info("Loaded %d/%d report data sources", loaded, len(data))
        return data

    # ------------------------------------------------------------------
    # Streak calculation
    # ------------------------------------------------------------------

    def _calculate_streaks(self, history: pd.DataFrame) -> pd.DataFrame:
        """Calculate current CONSIDER streak per symbol from history."""
        if history.empty:
            return pd.DataFrame(columns=["symbol", "consider_streak"])

        df = history.sort_values(["symbol", "date"]).copy()
        df["is_consider"] = (df["decision_flag"] == "CONSIDER").astype(int)
        df["streak_reset"] = (df.groupby("symbol")["is_consider"].diff().fillna(0) != 0).astype(int)
        df["streak_group"] = df.groupby("symbol")["streak_reset"].cumsum()
        df["streak_length"] = df.groupby(["symbol", "streak_group"]).cumcount() + 1
        df["consider_streak"] = df["is_consider"] * df["streak_length"]

        latest_date = df["date"].max()
        return df[df["date"] == latest_date][["symbol", "consider_streak"]].copy()

    # ------------------------------------------------------------------
    # Helper formatting
    # ------------------------------------------------------------------

    @staticmethod
    def _fmt(val, fmt_str=".2f", suffix="", na="—"):
        """Format a value with NaN handling."""
        if pd.isna(val):
            return na
        return f"{val:{fmt_str}}{suffix}"

    @staticmethod
    def _trend_arrow(trend: str) -> str:
        arrows = {"narrowing": "↑", "widening": "↓", "stable": "→"}
        return arrows.get(trend, "?")

    # ------------------------------------------------------------------
    # Markdown report generation
    # ------------------------------------------------------------------

    def generate_markdown(self, data: dict) -> str:
        """Generate the full latest_rankings.md content."""
        lines = []
        decisions = data["decisions"]
        scored = data["scored"]
        history = data["history"]
        universe = data["universe"]
        quality = data["quality"]
        snapshot = data["snapshot"]

        now = datetime.now()
        lines.append("# Nepal MF Quant — Full Analysis Report")
        lines.append("")
        lines.append(f"*Generated: {now.strftime('%Y-%m-%d %H:%M')}*")
        lines.append("")

        # ==== MARKET OVERVIEW ====
        lines.append("## Market Overview")
        lines.append("")

        if not decisions.empty:
            latest_date = decisions["date"].max()
            total = len(decisions)
            at_discount = (decisions["discount_pct"] < 0).sum()
            at_premium = (decisions["discount_pct"] >= 0).sum()
            deep_discount = (decisions["discount_pct"] <= -8).sum()
            median_disc = decisions["discount_pct"].median()
            consider_n = (decisions["decision_flag"] == "CONSIDER").sum()
            ignore_n = (decisions["decision_flag"] == "IGNORE").sum()

            lines.append(f"| Metric | Value |")
            lines.append(f"|--------|-------|")
            lines.append(f"| Analysis Date | {latest_date.strftime('%Y-%m-%d') if hasattr(latest_date, 'strftime') else latest_date} |")
            lines.append(f"| Funds Tracked | {total} |")
            lines.append(f"| At Discount (price < NAV) | {at_discount} |")
            lines.append(f"| At Premium (price ≥ NAV) | {at_premium} |")
            lines.append(f"| Deep Discount (≤ -8%) | {deep_discount} |")
            lines.append(f"| Median Discount | {median_disc:.2f}% |")
            lines.append(f"| CONSIDER | {consider_n} |")
            lines.append(f"| IGNORE | {ignore_n} |")
            lines.append("")

        # NAV freshness warning
        if not quality.empty and "nav_stale" in quality.columns:
            stale = quality[quality["nav_stale"] == True]
            if len(stale) > 0:
                lines.append(f"> ⚠️ **NAV Staleness Warning**: {len(stale)} fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.")
                lines.append("")

        # ==== DISCOUNT DISTRIBUTION ====
        lines.append("## Discount Distribution")
        lines.append("")

        if not decisions.empty:
            bins = [(-np.inf, -10), (-10, -6), (-6, -4), (-4, 0), (0, np.inf)]
            labels = ["< -10%", "-10% to -6%", "-6% to -4%", "-4% to 0%", "≥ 0% (premium)"]
            lines.append("| Discount Range | Count | % of Universe |")
            lines.append("|---------------|-------|---------------|")
            for (lo, hi), label in zip(bins, labels):
                count = ((decisions["discount_pct"] > lo) & (decisions["discount_pct"] <= hi)).sum()
                if lo == -np.inf:
                    count = (decisions["discount_pct"] <= hi).sum()
                if hi == np.inf:
                    count = (decisions["discount_pct"] > lo).sum()
                pct = count / len(decisions) * 100
                lines.append(f"| {label} | {count} | {pct:.1f}% |")
            lines.append("")

        # ==== TOP CONSIDER FUNDS ====
        lines.append("## CONSIDER Candidates")
        lines.append("")

        if not decisions.empty:
            consider = decisions[decisions["decision_flag"] == "CONSIDER"].copy()

            # Merge names from universe
            if not universe.empty and "name" in universe.columns:
                consider = consider.merge(universe[["symbol", "name"]], on="symbol", how="left")
            else:
                consider["name"] = consider["symbol"]

            # Merge streaks
            streaks = self._calculate_streaks(history)
            if not streaks.empty:
                consider = consider.merge(streaks, on="symbol", how="left")
                consider["consider_streak"] = consider["consider_streak"].fillna(0).astype(int)
            else:
                consider["consider_streak"] = 0

            # Sort by priority_rank if available, else by discount
            sort_col = "priority_rank" if "priority_rank" in consider.columns else "discount_pct"
            ascending = True if sort_col == "priority_rank" else True
            consider = consider.sort_values(sort_col, ascending=ascending, na_position="last")

            if len(consider) == 0:
                lines.append("*No funds currently meet all CONSIDER criteria (discount ≤-4%, liquidity not low, maturity ≤4y).*")
                lines.append("")
            else:
                has_score = "composite_score" in consider.columns and consider["composite_score"].notna().any()
                has_trend = "discount_trend" in consider.columns
                has_risk = "risk_flag" in consider.columns
                has_nav_growth = "nav_return_1m" in consider.columns and consider["nav_return_1m"].notna().any()

                # Build header
                header = "| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak |"
                sep = "|---|--------|------|-----|-----|----------|----------|-----------|--------|"
                if has_nav_growth:
                    header += " NAV Δ |"
                    sep += "-------|"
                if has_score:
                    header += " Score |"
                    sep += "-------|"
                if has_trend:
                    header += " Trend |"
                    sep += "-------|"
                if has_risk:
                    header += " Risk |"
                    sep += "------|"

                lines.append(header)
                lines.append(sep)

                for idx, (_, row) in enumerate(consider.iterrows(), 1):
                    name = str(row.get("name", row["symbol"]))[:25]
                    r = f"| {idx} | {row['symbol']} | {name} "
                    r += f"| {self._fmt(row.get('nav'), '.2f')} "
                    r += f"| {self._fmt(row.get('ltp'), '.2f')} "
                    r += f"| {self._fmt(row.get('discount_pct'), '.2f', '%')} "
                    maturity = row.get("years_to_maturity", np.nan)
                    r += f"| {self._fmt(maturity, '.1f', 'y')} "
                    r += f"| {row.get('liquidity_bucket', '—')} "
                    r += f"| {int(row.get('consider_streak', 0))}d "
                    if has_nav_growth:
                        r += f"| {self._fmt(row.get('nav_return_1m'), '.2f', '%')} "
                    if has_score:
                        r += f"| {self._fmt(row.get('composite_score'), '.1f')} "
                    if has_trend:
                        trend = row.get("discount_trend", "unknown")
                        r += f"| {self._trend_arrow(trend)} {trend} "
                    if has_risk:
                        flag = row.get("risk_flag", "")
                        r += f"| {flag if pd.notna(flag) and flag else '—'} "
                    r += "|"
                    lines.append(r)

                lines.append("")

        # ==== IGNORE SUMMARY ====
        lines.append("## IGNORE Summary")
        lines.append("")

        if not decisions.empty:
            ignore = decisions[decisions["decision_flag"] == "IGNORE"].copy()
            if len(ignore) > 0 and "ignore_reasons" in ignore.columns:
                lines.append(f"*{len(ignore)} funds are flagged IGNORE. Top reasons:*")
                lines.append("")

                # Count reasons
                all_reasons = []
                for reasons_str in ignore["ignore_reasons"].dropna():
                    for reason in str(reasons_str).split("; "):
                        if reason.strip():
                            all_reasons.append(reason.strip().split(":")[0])
                if all_reasons:
                    reason_counts = pd.Series(all_reasons).value_counts()
                    lines.append("| Gate Failed | Count |")
                    lines.append("|-------------|-------|")
                    for reason, count in reason_counts.items():
                        lines.append(f"| {reason} | {count} |")
                    lines.append("")

                # Compact table of ignore funds
                lines.append("<details>")
                lines.append("<summary>Full IGNORE list (click to expand)</summary>")
                lines.append("")
                lines.append("| Symbol | Discount | Reason |")
                lines.append("|--------|----------|--------|")
                for _, row in ignore.sort_values("discount_pct").iterrows():
                    lines.append(f"| {row['symbol']} | {self._fmt(row.get('discount_pct'), '.2f', '%')} | {row.get('ignore_reasons', '—')} |")
                lines.append("")
                lines.append("</details>")
                lines.append("")
            else:
                lines.append(f"*{len(ignore)} funds flagged IGNORE.*")
                lines.append("")

        # ==== DATA QUALITY ====
        if not quality.empty:
            lines.append("## Data Quality")
            lines.append("")
            issues = quality["has_issues"].sum() if "has_issues" in quality.columns else 0
            total_checked = len(quality)
            lines.append(f"- Symbols checked: {total_checked}")
            lines.append(f"- Symbols with issues: {issues}")

            if "nav_age_days" in quality.columns:
                max_age = quality["nav_age_days"].max()
                median_age = quality["nav_age_days"].median()
                lines.append(f"- NAV data age: median {self._fmt(median_age, '.0f')} days, max {self._fmt(max_age, '.0f')} days")
            lines.append("")

        # ==== METHODOLOGY ====
        lines.append("## Methodology")
        lines.append("")
        lines.append("### Decision Gates")
        lines.append("A fund receives **CONSIDER** only if ALL three gates pass:")
        lines.append("1. **Valuation**: Discount to NAV ≤ -4% (deep or moderate discount)")
        lines.append("2. **Liquidity**: Volume not in the bottom 25th percentile")
        lines.append("3. **Maturity**: ≤ 4 years to maturity (discount convergence horizon)")
        lines.append("")
        lines.append("### Composite Score")
        lines.append("Within CONSIDER funds, a weighted composite score ranks relative attractiveness:")
        lines.append("- Discount depth: 30% — deeper discount = higher score")
        lines.append("- Liquidity: 15% — higher volume = higher score")
        lines.append("- Maturity proximity: 15% — closer maturity = higher score")
        lines.append("- NAV growth: 10% — positive month-over-month NAV return = higher score (fund manager quality)")
        lines.append("- Price momentum: 10% — positive return = higher score")
        lines.append("- Volatility (inverse): 10% — lower Parkinson vol = higher score")
        lines.append("- Discount trend: 10% — narrowing discount = higher score")
        lines.append("")
        lines.append("### Risk Metrics")
        lines.append("- **Parkinson Volatility**: Estimated from OHLC (high/low) range — more efficient than close-to-close for small samples")
        lines.append("- **Intraday Range**: `(high - low) / LTP` — measures trading friction")
        lines.append("- **Volume CV**: Coefficient of variation of daily volume — flags erratic liquidity")
        lines.append("")
        lines.append("---")
        lines.append(f"*This report is auto-generated for research purposes only. Not investment advice.*")
        lines.append("")

        return "\n".join(lines)

    # ------------------------------------------------------------------
    # CSV metrics table
    # ------------------------------------------------------------------

    def generate_metrics_csv(self, data: dict) -> pd.DataFrame:
        """
        Generate a comprehensive metrics CSV for all funds.
        Replaces the empty placeholder reports/metrics_table.csv.
        """
        decisions = data["decisions"]
        universe = data["universe"]
        risk = data["risk"]
        scored = data["scored"]
        streaks = self._calculate_streaks(data["history"])

        if decisions.empty:
            logger.warning("No decision data — metrics table will be empty")
            return pd.DataFrame()

        df = decisions.copy()

        # Merge fund name
        if not universe.empty and "name" in universe.columns:
            df = df.merge(universe[["symbol", "name"]], on="symbol", how="left")
        else:
            df["name"] = df["symbol"]

        # Merge risk metrics
        if not risk.empty:
            risk_cols = [c for c in risk.columns if c not in ("date",)]
            df = df.merge(risk[risk_cols].drop_duplicates("symbol"), on="symbol", how="left")

        # Merge scored metrics
        if not scored.empty:
            score_cols = ["symbol", "price_return_1d", "price_return_1w",
                          "discount_change_1d", "discount_change_1w",
                          "nav_return_1m",
                          "composite_score", "rank"]
            score_cols = [c for c in score_cols if c in scored.columns]
            df = df.merge(scored[score_cols].drop_duplicates("symbol"), on="symbol", how="left")

        # Merge streaks
        if not streaks.empty:
            df = df.merge(streaks, on="symbol", how="left")
            df["consider_streak"] = df["consider_streak"].fillna(0).astype(int)
        else:
            df["consider_streak"] = 0

        # Select and order final columns
        desired_cols = [
            "date", "symbol", "name", "nav", "ltp", "discount_pct",
            "volume", "days_to_maturity", "years_to_maturity",
            "valuation_bucket", "liquidity_bucket", "decision_flag",
            "ignore_reasons", "composite_score", "rank", "priority_rank",
            "discount_trend", "risk_flag", "consider_streak",
            "nav_return_1m",
            "price_return_1d", "price_return_1w",
            "discount_change_1d", "discount_change_1w",
            "parkinson_vol", "parkinson_vol_ann",
            "intraday_range", "avg_intraday_range",
            "return_vol_5d", "volume_cv", "max_drawdown", "sharpe_1m",
        ]
        final_cols = [c for c in desired_cols if c in df.columns]
        df = df[final_cols].copy()

        # Format date
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

        return df

    # ------------------------------------------------------------------
    # Pipeline entry point
    # ------------------------------------------------------------------

    def run(self) -> None:
        """Generate all reports."""
        logger.info("=" * 80)
        logger.info("REPORT GENERATOR")
        logger.info("=" * 80)

        data = self.load_all()

        # Generate markdown
        logger.info("Generating markdown report...")
        md_content = self.generate_markdown(data)
        self.md_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        logger.info("Saved: %s (%d chars)", self.md_path, len(md_content))

        # Generate CSV
        logger.info("Generating metrics CSV...")
        csv_df = self.generate_metrics_csv(data)
        csv_df.to_csv(self.csv_path, index=False)
        logger.info("Saved: %s (%d rows)", self.csv_path, len(csv_df))

        logger.info("=" * 80)
        logger.info("REPORTS COMPLETE")
        logger.info("=" * 80)


def main():
    """Entry point."""
    project_root = Path(__file__).parent.parent.parent
    gen = ReportGenerator(project_root)
    gen.run()


if __name__ == "__main__":
    main()
