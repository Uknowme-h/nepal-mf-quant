"""
README Auto-Updater for Mutual Fund Decision System

Generates a rich quantitative dashboard in README.md with:
- Market snapshot (total funds, discount stats, data freshness)
- Enhanced CONSIDER table (name, NAV, LTP, score, trend, risk, streak)
- Discount distribution summary
- Data status footer with pipeline freshness
- Links to full reports

Preserves all static README content outside the auto-generated markers.
This is for research dashboard purposes only — NO investment advice.
"""

import numpy as np
import pandas as pd
import logging
from pathlib import Path
from datetime import datetime
import re

logger = logging.getLogger(__name__)


class ReadmeUpdater:
    """
    Updates README.md with a comprehensive decision analysis dashboard.

    Only modifies the auto-generated section, preserves all other content.
    """

    SECTION_HEADER = "## 📊 Daily Mutual Fund Decision Summary"
    SECTION_START_MARKER = "<!-- AUTO-GENERATED-START -->"
    SECTION_END_MARKER = "<!-- AUTO-GENERATED-END -->"

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.history_path = project_root / "data" / "history" / "mf_decision_history.csv"
        self.decision_path = project_root / "data" / "processed" / "mf_decision_table.csv"
        self.scored_path = project_root / "data" / "processed" / "mf_scored.csv"
        self.quality_path = project_root / "data" / "processed" / "mf_data_quality.csv"
        self.snapshot_path = project_root / "data" / "processed" / "mf_daily_snapshot.csv"
        self.universe_path = project_root / "data" / "raw" / "fund_universe.csv"
        self.readme_path = project_root / "README.md"

    # ------------------------------------------------------------------
    # Data loading
    # ------------------------------------------------------------------

    def _load_csv(self, path: Path, date_cols: list | None = None) -> pd.DataFrame:
        if not path.exists():
            return pd.DataFrame()
        df = pd.read_csv(path)
        for col in (date_cols or []):
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors="coerce")
        return df

    def load_all_data(self) -> dict:
        """Load all data sources for the dashboard."""
        return {
            "history": self._load_csv(self.history_path, ["date"]),
            "decisions": self._load_csv(self.decision_path, ["date"]),
            "scored": self._load_csv(self.scored_path, ["date"]),
            "quality": self._load_csv(self.quality_path),
            "snapshot": self._load_csv(self.snapshot_path, ["date"]),
            "universe": self._load_csv(self.universe_path),
        }

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def calculate_consider_streaks(self, history: pd.DataFrame) -> pd.DataFrame:
        """Calculate consecutive CONSIDER days for each symbol."""
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

    @staticmethod
    def _fmt(val, fmt_str=".2f", suffix="", na="—"):
        if pd.isna(val):
            return na
        return f"{val:{fmt_str}}{suffix}"

    @staticmethod
    def _trend_arrow(trend: str) -> str:
        return {"narrowing": "↑", "widening": "↓", "stable": "→"}.get(str(trend), "·")

    # ------------------------------------------------------------------
    # Markdown generation
    # ------------------------------------------------------------------

    def generate_markdown_content(self, data: dict) -> str:
        """Generate the full auto-generated README section."""
        lines = []
        decisions = data["decisions"]
        scored = data["scored"]
        history = data["history"]
        universe = data["universe"]
        quality = data["quality"]

        lines.append(self.SECTION_HEADER)
        lines.append("")
        lines.append(self.SECTION_START_MARKER)
        lines.append("")

        if decisions.empty:
            lines.append("**Status**: No analysis data available yet.")
            lines.append("")
            lines.append("Run the pipeline to generate decision data:")
            lines.append("```bash")
            lines.append("python src/pipeline.py --skip-scrape")
            lines.append("```")
            lines.append("")
            lines.append(self.SECTION_END_MARKER)
            return "\n".join(lines)

        latest_date = decisions["date"].max()
        date_str = latest_date.strftime("%Y-%m-%d") if hasattr(latest_date, "strftime") else str(latest_date)

        # ====== MARKET SNAPSHOT ======
        lines.append("### Market Snapshot")
        lines.append("")

        total = len(decisions)
        at_discount = (decisions["discount_pct"] < 0).sum()
        at_premium = (decisions["discount_pct"] >= 0).sum()
        deep_discount = (decisions["discount_pct"] <= -8).sum()
        median_disc = decisions["discount_pct"].median()
        consider_n = (decisions["decision_flag"] == "CONSIDER").sum()

        lines.append(f"| | |")
        lines.append(f"|---|---|")
        lines.append(f"| **Date** | {date_str} |")
        lines.append(f"| **Funds Tracked** | {total} |")
        lines.append(f"| **Median Discount** | {median_disc:.2f}% |")
        lines.append(f"| **At Discount** | {at_discount} ({at_discount/total*100:.0f}%) |")
        lines.append(f"| **Deep Discount (≤-8%)** | {deep_discount} |")
        lines.append(f"| **CONSIDER** | {consider_n} |")
        lines.append(f"| **IGNORE** | {total - consider_n} |")
        lines.append("")

        # NAV freshness warning
        if not quality.empty and "nav_stale" in quality.columns:
            stale_count = quality["nav_stale"].sum()
            if stale_count > 0:
                lines.append(f"> ⚠️ {stale_count} fund(s) have NAV data older than 45 days.")
                lines.append("")

        # ====== DISCOUNT DISTRIBUTION ======
        lines.append("### Discount Distribution")
        lines.append("")
        bins_labels = [
            ((-np.inf, -10), "< -10%"),
            ((-10, -6), "-10% to -6%"),
            ((-6, -4), "-6% to -4%"),
            ((-4, 0), "-4% to 0%"),
            ((0, np.inf), "≥ 0%"),
        ]
        parts = []
        for (lo, hi), label in bins_labels:
            if lo == -np.inf:
                c = (decisions["discount_pct"] <= hi).sum()
            elif hi == np.inf:
                c = (decisions["discount_pct"] > lo).sum()
            else:
                c = ((decisions["discount_pct"] > lo) & (decisions["discount_pct"] <= hi)).sum()
            bar = "█" * c
            parts.append(f"| {label:>14} | {bar} {c} |")

        lines.append("| Range | Distribution |")
        lines.append("|-------|-------------|")
        lines.extend(parts)
        lines.append("")

        # ====== CONSIDER TABLE ======
        lines.append("### Active CONSIDER Candidates")
        lines.append("")

        consider = decisions[decisions["decision_flag"] == "CONSIDER"].copy()

        # Merge names
        if not universe.empty and "name" in universe.columns:
            consider = consider.merge(universe[["symbol", "name"]], on="symbol", how="left")
        else:
            consider["name"] = consider["symbol"]

        # Merge streaks
        streaks = self.calculate_consider_streaks(history)
        if not streaks.empty:
            consider = consider.merge(streaks, on="symbol", how="left")
            consider["consider_streak"] = consider["consider_streak"].fillna(0).astype(int)
        else:
            consider["consider_streak"] = 0

        # Sort by priority_rank or discount
        sort_col = "priority_rank" if "priority_rank" in consider.columns and consider["priority_rank"].notna().any() else "discount_pct"
        consider = consider.sort_values(sort_col, ascending=True, na_position="last")

        if len(consider) == 0:
            lines.append("*No funds currently meet CONSIDER criteria.*")
            lines.append("")
        else:
            has_score = "composite_score" in consider.columns and consider["composite_score"].notna().any()
            has_trend = "discount_trend" in consider.columns

            header = "| # | Symbol | Name | Discount | NAV | LTP | Maturity | Liquidity | Streak |"
            sep = "|---|--------|------|----------|-----|-----|----------|-----------|--------|"
            if has_score:
                header += " Score |"
                sep += "-------|"
            if has_trend:
                header += " Trend |"
                sep += "-------|"

            lines.append(header)
            lines.append(sep)

            for idx, (_, row) in enumerate(consider.iterrows(), 1):
                name = str(row.get("name", row["symbol"]))[:20]
                streak = int(row.get("consider_streak", 0))
                streak_str = f"{streak}d"
                r = f"| {idx} | **{row['symbol']}** | {name} "
                r += f"| {self._fmt(row.get('discount_pct'), '.2f', '%')} "
                r += f"| {self._fmt(row.get('nav'), '.2f')} "
                r += f"| {self._fmt(row.get('ltp'), '.2f')} "
                maturity = row.get("years_to_maturity", np.nan)
                r += f"| {self._fmt(maturity, '.1f', 'y')} "
                r += f"| {row.get('liquidity_bucket', '—')} "
                r += f"| {streak_str} "
                if has_score:
                    r += f"| {self._fmt(row.get('composite_score'), '.1f')} "
                if has_trend:
                    trend = str(row.get("discount_trend", "unknown"))
                    r += f"| {self._trend_arrow(trend)} "
                r += "|"
                lines.append(r)

            lines.append("")

        # ====== KEY METRICS ======
        if not consider.empty and "composite_score" in consider.columns:
            top3 = consider.head(3)
            if top3["composite_score"].notna().any():
                lines.append("### Top Picks by Composite Score")
                lines.append("")
                for _, row in top3.iterrows():
                    name = str(row.get("name", row["symbol"]))
                    lines.append(f"- **{row['symbol']}** ({name}): {self._fmt(row.get('discount_pct'), '.2f', '%')} discount, score {self._fmt(row.get('composite_score'), '.1f')}")
                lines.append("")

        # ====== INTERPRETATION ======
        lines.append("### Interpretation")
        lines.append("")
        lines.append("CONSIDER = discount ≤ -4% AND liquidity ≠ low AND maturity ≤ 4 years. "
                      "Funds are ranked by a composite score (discount 35%, liquidity 20%, maturity 15%, "
                      "momentum 10%, volatility 10%, trend 10%). This is rule-based screening for "
                      "research purposes only.")
        lines.append("")

        # ====== DATA STATUS ======
        lines.append("### Data Status")
        lines.append("")
        lines.append(f"- Latest price data: {date_str}")
        if not quality.empty and "nav_age_days" in quality.columns:
            median_age = quality["nav_age_days"].median()
            lines.append(f"- NAV data age: median {self._fmt(median_age, '.0f')} days")
        history_days = history["date"].nunique() if not history.empty else 0
        lines.append(f"- History depth: {history_days} trading day(s)")
        lines.append(f"- Full report: [reports/latest_rankings.md](reports/latest_rankings.md)")
        lines.append(f"- Metrics CSV: [reports/metrics_table.csv](reports/metrics_table.csv)")
        lines.append("")

        lines.append(self.SECTION_END_MARKER)

        return "\n".join(lines)

    # ------------------------------------------------------------------
    # README update
    # ------------------------------------------------------------------

    def update_readme(self, new_content: str) -> None:
        """Replace auto-generated section in README.md."""
        if self.readme_path.exists():
            with open(self.readme_path, "r", encoding="utf-8") as f:
                existing_content = f.read()
        else:
            existing_content = ""

        if self.SECTION_HEADER in existing_content:
            pattern = re.escape(self.SECTION_HEADER) + r".*?" + re.escape(self.SECTION_END_MARKER)
            updated_content = re.sub(pattern, new_content, existing_content, flags=re.DOTALL)
            operation = "Updated"
        else:
            if existing_content and not existing_content.endswith("\n\n"):
                existing_content = existing_content.rstrip("\n") + "\n\n"
            updated_content = existing_content + new_content + "\n"
            operation = "Appended"

        with open(self.readme_path, "w", encoding="utf-8") as f:
            f.write(updated_content)

        logger.info("%s README: %s (%d chars)", operation, self.readme_path, len(updated_content))

    # ------------------------------------------------------------------
    # Pipeline entry point
    # ------------------------------------------------------------------

    def run(self) -> None:
        """Execute README update pipeline."""
        logger.info("=" * 80)
        logger.info("README AUTO-UPDATER")
        logger.info("=" * 80)

        try:
            data = self.load_all_data()
            markdown_content = self.generate_markdown_content(data)
            self.update_readme(markdown_content)

            logger.info("=" * 80)
            logger.info("README UPDATE COMPLETE")
            logger.info("=" * 80)

        except Exception as e:
            logger.error("README UPDATE FAILED: %s", e)
            raise


def main():
    """Entry point."""
    project_root = Path(__file__).parent.parent.parent
    updater = ReadmeUpdater(project_root)
    updater.run()


if __name__ == "__main__":
    main()
