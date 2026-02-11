"""
End-to-end pipeline orchestrator for Nepal Mutual Fund Quantitative Analysis.

Runs all scraping, analytics, and reporting steps in dependency order
with retry logic, cadence checks, and structured logging.

Usage:
    python src/pipeline.py                  # Full daily run (respects cadence)
    python src/pipeline.py --force          # Force all steps regardless of cadence
    python src/pipeline.py --dry-run        # Show what would run without executing
    python src/pipeline.py --steps 3,4,5    # Run only specific steps
    python src/pipeline.py --skip-scrape    # Skip all scraping, only run analytics

Steps:
     1. Scrape fund universe         (weekly)
     2. Scrape NAV (ShareSansar)      (monthly)
     3. Scrape NAV (direct providers)  (weekly)
     4. Scrape market prices          (daily)   [critical]
     5. Data quality validation       (daily)
     6. Calculate valuations          (daily)   [critical]
     7. Calculate returns             (daily)   [critical]
     8. Calculate risk metrics        (daily)   [critical]
     9. Score & rank funds            (daily)   [critical]
    10. Apply decision rules          (daily)   [critical]
    11. Update decision history       (daily)   [critical]
    12. Generate reports              (daily)
    13. Update README dashboard       (daily)
"""

import argparse
import asyncio
import logging
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable, List, Optional

# ---------------------------------------------------------------------------
# Resolve project root (works from repo root OR from src/)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Ensure the project root is on sys.path so we can import sibling packages
# (scrapers/, src/scrape/, src/analytics/) without PYTHONPATH hacks.
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(PROJECT_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT / "src"))

# ---------------------------------------------------------------------------
# Logging — single config; all downstream modules inherit this.
# ---------------------------------------------------------------------------
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger("pipeline")


# ---------------------------------------------------------------------------
# Pipeline step definition
# ---------------------------------------------------------------------------
@dataclass
class PipelineStep:
    """A single step in the pipeline."""

    number: int
    name: str
    cadence: str  # "daily" | "weekly" | "monthly"
    critical: bool  # If True, downstream steps abort on failure
    run_fn: Callable  # () -> None  (raised exceptions = failure)
    description: str = ""
    skipped: bool = False
    status: str = "pending"  # pending | skipped | success | failed
    duration_s: float = 0.0
    error: Optional[str] = None


# ---------------------------------------------------------------------------
# Retry wrapper
# ---------------------------------------------------------------------------
def run_with_retry(
    fn: Callable,
    step_name: str,
    max_retries: int = 3,
    backoff_base: float = 5.0,
) -> None:
    """
    Execute *fn* with exponential-backoff retries.

    Raises the last exception after all retries are exhausted.
    """
    last_exc: Optional[Exception] = None

    for attempt in range(1, max_retries + 1):
        try:
            fn()
            return  # success
        except Exception as exc:
            last_exc = exc
            if attempt < max_retries:
                wait = backoff_base * (2 ** (attempt - 1))
                logger.warning(
                    "[%s] Attempt %d/%d failed: %s — retrying in %.0fs",
                    step_name,
                    attempt,
                    max_retries,
                    exc,
                    wait,
                )
                time.sleep(wait)
            else:
                logger.error(
                    "[%s] Attempt %d/%d failed: %s — no retries left",
                    step_name,
                    attempt,
                    max_retries,
                    exc,
                )

    raise last_exc  # type: ignore[misc]


# ===================================================================
# Step implementations — thin wrappers around existing module classes
# ===================================================================

def step_scrape_fund_universe():
    """Step 1: Scrape fund universe from ShareSansar."""
    from src.scrape.fund_universe import FundUniverseScraper

    scraper = FundUniverseScraper(project_root=PROJECT_ROOT)
    funds_df = scraper.scrape_all()
    if funds_df.empty:
        raise RuntimeError("Fund universe scrape returned 0 funds")
    scraper.save_to_csv(funds_df)
    logger.info("Fund universe: %d funds saved", len(funds_df))


def step_scrape_nav():
    """Step 2: Scrape monthly NAV data from ShareSansar."""
    from src.scrape.nav_scraper import (
        fetch_current_monthly_nav,
        load_fund_universe,
        update_fund_nav_csv,
        PROVIDER_SYMBOLS,
    )

    universe_path = PROJECT_ROOT / "data" / "raw" / "fund_universe.csv"
    data_dir = PROJECT_ROOT / "data" / "raw"

    if not universe_path.exists():
        raise FileNotFoundError(
            f"Fund universe not found at {universe_path} — run step 1 first"
        )

    symbols = load_fund_universe(universe_path)
    if not symbols:
        raise RuntimeError("No fund symbols found in universe")

    nav_data = fetch_current_monthly_nav()
    if not nav_data:
        raise RuntimeError("NAV scrape returned no data from API")

    updated = 0
    skipped_provider = 0
    for symbol in symbols:
        if symbol in PROVIDER_SYMBOLS:
            skipped_provider += 1
            continue
        if symbol in nav_data:
            date, nav = nav_data[symbol]
            update_fund_nav_csv(symbol, date, nav, data_dir)
            updated += 1

    logger.info(
        "NAV update (ShareSansar): %d/%d funds updated (%d skipped — have provider)",
        updated, len(symbols), skipped_provider,
    )


def step_scrape_monthly_nav_providers():
    """Step 3: Scrape monthly NAV data from direct provider APIs."""
    from src.scrape.monthly_nav_scraper import run as run_monthly_scraper

    stats = run_monthly_scraper(PROJECT_ROOT)
    total_new = sum(stats.values())
    symbols_updated = sum(1 for v in stats.values() if v > 0)
    logger.info(
        "Direct-provider NAV update: %d new records across %d symbols",
        total_new,
        symbols_updated,
    )


def step_scrape_market_prices():
    """Step 4: Scrape daily market prices from NEPSE via Playwright."""
    from scrapers.market.daily_price_scraper import MarketDataExtractor

    async def _run():
        extractor = MarketDataExtractor(PROJECT_ROOT)
        new_records, failed, scraped_count = await extractor.scrape_all()
        extractor.validate_success_rate(scraped_count, failed, len(new_records))
        extractor.save_results(new_records)
        return len(new_records), len(failed), scraped_count

    new_count, fail_count, total = asyncio.run(_run())
    logger.info(
        "Market prices: %d new records, %d failed, %d total scraped",
        new_count,
        fail_count,
        total,
    )


def step_data_quality():
    """Step 5: Run data quality validation checks."""
    from src.analytics.data_quality import DataQualityChecker

    checker = DataQualityChecker(PROJECT_ROOT)
    result = checker.run()
    issues = result["has_issues"].sum() if "has_issues" in result.columns else 0
    if issues > 0:
        logger.warning("Data quality: %d/%d symbols have issues", issues, len(result))
    else:
        logger.info("Data quality: all %d symbols clean", len(result))


def step_valuation():
    """Step 6: Calculate NAV-to-price valuations."""
    from src.analytics.valuation import MutualFundValuation

    pipeline = MutualFundValuation(PROJECT_ROOT)
    pipeline.run(top_n=10)


def step_returns():
    """Step 7: Calculate price returns and discount change."""
    from src.analytics.returns import ReturnsCalculator

    calc = ReturnsCalculator(PROJECT_ROOT)
    calc.run()


def step_risk():
    """Step 8: Calculate risk metrics from OHLC data."""
    from src.analytics.risk import RiskMetrics

    risk = RiskMetrics(PROJECT_ROOT)
    risk.run()


def step_scoring():
    """Step 9: Score and rank funds by composite factors."""
    from src.analytics.scoring import FundScorer

    scorer = FundScorer(PROJECT_ROOT)
    scorer.run()


def step_decision_layer():
    """Step 10: Apply rule-based screening decisions."""
    from src.analytics.decision_layer import InvestmentDecisionLayer

    pipeline = InvestmentDecisionLayer(PROJECT_ROOT)
    pipeline.run()


def step_decision_history():
    """Step 11: Append today's decisions to history log."""
    from src.analytics.decision_history import DecisionHistoryTracker

    tracker = DecisionHistoryTracker(PROJECT_ROOT)
    tracker.run()


def step_generate_reports():
    """Step 12: Generate detailed markdown and CSV reports."""
    from src.analytics.report_generator import ReportGenerator

    gen = ReportGenerator(PROJECT_ROOT)
    gen.run()


def step_update_readme():
    """Step 13: Update README dashboard section."""
    from src.analytics.update_readme import ReadmeUpdater

    updater = ReadmeUpdater(PROJECT_ROOT)
    updater.run()


# ===================================================================
# Cadence checks
# ===================================================================

def should_run_weekly() -> bool:
    """Run on Sundays (start of Nepali work week) or if fund_universe.csv is missing."""
    universe = PROJECT_ROOT / "data" / "raw" / "fund_universe.csv"
    if not universe.exists():
        logger.info("  Fund universe file missing — forcing weekly step")
        return True
    today = datetime.now()
    # Sunday = 6 in Python's weekday()
    return today.weekday() == 6


def should_run_monthly() -> bool:
    """Run on days 1-3 of the month or if nav/ directory is empty."""
    nav_dir = PROJECT_ROOT / "data" / "raw" / "nav"
    if not nav_dir.exists() or not list(nav_dir.glob("*.csv")):
        logger.info("  NAV directory empty or missing — forcing monthly step")
        return True
    return datetime.now().day <= 3


# ===================================================================
# Pre-flight validation
# ===================================================================

def validate_prerequisites():
    """
    Check that critical files and directories exist before running.
    Creates output directories if missing.
    """
    errors = []

    # Required input files
    mapping_file = PROJECT_ROOT / "data" / "reference" / "symbol_nepse_map.csv"
    if not mapping_file.exists():
        errors.append(
            f"Symbol-NEPSE mapping missing: {mapping_file}\n"
            "  -> Run:  python scrapers/mappings/build_symbol_nepse_map.py"
        )

    # Create output dirs if needed
    for subdir in [
        "data/processed",
        "data/history",
        "data/raw/nav",
        "data/metrics",
        "reports",
    ]:
        (PROJECT_ROOT / subdir).mkdir(parents=True, exist_ok=True)

    if errors:
        logger.error("Pre-flight check failed:")
        for err in errors:
            logger.error("  %s", err)
        raise RuntimeError(
            f"Pre-flight validation failed with {len(errors)} error(s)"
        )

    logger.info("Pre-flight checks passed")


# ===================================================================
# Pipeline runner
# ===================================================================

class PipelineRunner:
    """Orchestrates pipeline steps with retry, cadence, and logging."""

    def __init__(
        self,
        force: bool = False,
        dry_run: bool = False,
        selected_steps: Optional[List[int]] = None,
        skip_scrape: bool = False,
        max_retries: int = 3,
        backoff_base: float = 5.0,
    ):
        self.force = force
        self.dry_run = dry_run
        self.selected_steps = selected_steps
        self.skip_scrape = skip_scrape
        self.max_retries = max_retries
        self.backoff_base = backoff_base
        self.steps = self._build_steps()

    def _build_steps(self) -> List[PipelineStep]:
        """Define the ordered pipeline steps."""
        return [
            PipelineStep(
                number=1,
                name="scrape_fund_universe",
                cadence="weekly",
                critical=False,
                run_fn=step_scrape_fund_universe,
                description="Scrape fund metadata from ShareSansar",
            ),
            PipelineStep(
                number=2,
                name="scrape_nav_sharesansar",
                cadence="monthly",
                critical=False,
                run_fn=step_scrape_nav,
                description="Scrape monthly NAV data from ShareSansar",
            ),
            PipelineStep(
                number=3,
                name="scrape_nav_providers",
                cadence="weekly",
                critical=False,
                run_fn=step_scrape_monthly_nav_providers,
                description="Scrape monthly NAVs from 7 direct provider APIs",
            ),
            PipelineStep(
                number=4,
                name="scrape_market_prices",
                cadence="daily",
                critical=True,
                run_fn=step_scrape_market_prices,
                description="Scrape daily OHLC prices from NEPSE (Playwright)",
            ),
            PipelineStep(
                number=5,
                name="data_quality",
                cadence="daily",
                critical=False,
                run_fn=step_data_quality,
                description="Validate data freshness, outliers, and coverage",
            ),
            PipelineStep(
                number=6,
                name="valuation",
                cadence="daily",
                critical=True,
                run_fn=step_valuation,
                description="Join NAV + prices, calculate discounts, rank",
            ),
            PipelineStep(
                number=7,
                name="returns",
                cadence="daily",
                critical=True,
                run_fn=step_returns,
                description="Calculate price returns, discount change, NAV growth",
            ),
            PipelineStep(
                number=8,
                name="risk_metrics",
                cadence="daily",
                critical=True,
                run_fn=step_risk,
                description="Calculate Parkinson vol, intraday range, drawdown",
            ),
            PipelineStep(
                number=9,
                name="scoring",
                cadence="daily",
                critical=True,
                run_fn=step_scoring,
                description="Composite factor scoring and fund ranking",
            ),
            PipelineStep(
                number=10,
                name="decision_layer",
                cadence="daily",
                critical=True,
                run_fn=step_decision_layer,
                description="Apply rule-based CONSIDER/IGNORE screening",
            ),
            PipelineStep(
                number=11,
                name="decision_history",
                cadence="daily",
                critical=True,
                run_fn=step_decision_history,
                description="Append decisions to temporal history log",
            ),
            PipelineStep(
                number=12,
                name="generate_reports",
                cadence="daily",
                critical=False,
                run_fn=step_generate_reports,
                description="Generate detailed markdown + CSV reports",
            ),
            PipelineStep(
                number=13,
                name="update_readme",
                cadence="daily",
                critical=False,
                run_fn=step_update_readme,
                description="Update README.md dashboard section",
            ),
        ]

    def _should_run(self, step: PipelineStep) -> bool:
        """Determine if a step should execute based on cadence and filters."""
        # Explicit step selection overrides everything
        if self.selected_steps is not None:
            return step.number in self.selected_steps

        # --skip-scrape skips steps 1-4 (all scraping)
        if self.skip_scrape and step.number <= 4:
            return False

        # --force ignores cadence
        if self.force:
            return True

        # Cadence check
        if step.cadence == "weekly":
            return should_run_weekly()
        elif step.cadence == "monthly":
            return should_run_monthly()

        return True  # daily always runs

    def run(self) -> int:
        """
        Execute the pipeline. Returns exit code (0 = success, 1 = critical failure).
        """
        logger.info("=" * 80)
        logger.info("NEPAL MF QUANT — PIPELINE START")
        logger.info("=" * 80)
        logger.info("Project root : %s", PROJECT_ROOT)
        logger.info("Timestamp    : %s", datetime.now().isoformat())
        logger.info("Mode         : %s",
                     "DRY RUN" if self.dry_run else
                     "FORCED" if self.force else
                     "NORMAL")
        if self.selected_steps:
            logger.info("Steps filter : %s", self.selected_steps)
        if self.skip_scrape:
            logger.info("Skip scrape  : True (steps 1-3)")
        logger.info("Max retries  : %d (backoff base: %.0fs)", self.max_retries, self.backoff_base)
        logger.info("=" * 80)

        # Pre-flight (skip in dry-run)
        if not self.dry_run:
            try:
                validate_prerequisites()
            except RuntimeError:
                return 1

        pipeline_start = time.time()
        critical_failed = False

        for step in self.steps:
            if not self._should_run(step):
                step.status = "skipped"
                step.skipped = True
                logger.info(
                    "[Step %d/%d] %-25s — SKIPPED (cadence: %s)",
                    step.number,
                    len(self.steps),
                    step.name,
                    step.cadence,
                )
                continue

            # Abort downstream steps if a critical step already failed
            if critical_failed:
                step.status = "skipped"
                step.skipped = True
                logger.warning(
                    "[Step %d/%d] %-25s — SKIPPED (upstream critical failure)",
                    step.number,
                    len(self.steps),
                    step.name,
                )
                continue

            logger.info("")
            logger.info("-" * 80)
            logger.info(
                "[Step %d/%d] %s",
                step.number,
                len(self.steps),
                step.name,
            )
            logger.info("  %s", step.description)
            logger.info("  Cadence: %s | Critical: %s", step.cadence, step.critical)
            logger.info("-" * 80)

            if self.dry_run:
                step.status = "skipped"
                logger.info("  -> Would execute (dry-run mode)")
                continue

            step_start = time.time()
            try:
                run_with_retry(
                    step.run_fn,
                    step.name,
                    max_retries=self.max_retries,
                    backoff_base=self.backoff_base,
                )
                step.duration_s = time.time() - step_start
                step.status = "success"
                logger.info(
                    "[Step %d] %s — SUCCESS (%.1fs)",
                    step.number,
                    step.name,
                    step.duration_s,
                )
            except Exception as exc:
                step.duration_s = time.time() - step_start
                step.status = "failed"
                step.error = str(exc)
                logger.error(
                    "[Step %d] %s — FAILED after %d retries (%.1fs): %s",
                    step.number,
                    step.name,
                    self.max_retries,
                    step.duration_s,
                    exc,
                )
                if step.critical:
                    critical_failed = True
                    logger.error(
                        "  Critical step failed — aborting downstream steps"
                    )

        # ---------------------------------------------------------------
        # Summary
        # ---------------------------------------------------------------
        total_time = time.time() - pipeline_start
        logger.info("")
        logger.info("=" * 80)
        logger.info("PIPELINE SUMMARY")
        logger.info("=" * 80)

        for step in self.steps:
            icon = {
                "success": "+",
                "failed": "X",
                "skipped": "o",
                "pending": ".",
            }.get(step.status, "?")
            duration = f"{step.duration_s:.1f}s" if step.duration_s > 0 else "-"
            extra = f" [{step.error}]" if step.error else ""
            logger.info(
                "  %s Step %d: %-25s %8s  %s%s",
                icon,
                step.number,
                step.name,
                duration,
                step.status.upper(),
                extra,
            )

        succeeded = sum(1 for s in self.steps if s.status == "success")
        failed = sum(1 for s in self.steps if s.status == "failed")
        skipped = sum(1 for s in self.steps if s.status == "skipped")

        logger.info("-" * 80)
        logger.info(
            "  Total: %d succeeded, %d failed, %d skipped (%.1fs)",
            succeeded,
            failed,
            skipped,
            total_time,
        )
        logger.info("=" * 80)

        if critical_failed:
            logger.error("PIPELINE FAILED — critical step(s) did not succeed")
            return 1

        if failed > 0:
            logger.warning(
                "PIPELINE COMPLETED WITH WARNINGS — %d non-critical step(s) failed",
                failed,
            )

        logger.info("PIPELINE COMPLETED SUCCESSFULLY")
        return 0


# ===================================================================
# CLI
# ===================================================================

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Nepal MF Quant — Pipeline Orchestrator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Steps:
   1  Scrape fund universe         (weekly)
   2  Scrape NAV (ShareSansar)      (monthly)
   3  Scrape NAV (direct providers)  (weekly)
   4  Scrape market prices          (daily)   [critical]
   5  Data quality validation       (daily)
   6  Calculate valuations          (daily)   [critical]
   7  Calculate returns             (daily)   [critical]
   8  Calculate risk metrics        (daily)   [critical]
   9  Score & rank funds            (daily)   [critical]
  10  Apply decision rules          (daily)   [critical]
  11  Update decision history       (daily)   [critical]
  12  Generate reports              (daily)
  13  Update README dashboard       (daily)

Examples:
  python src/pipeline.py                      # Normal daily run
  python src/pipeline.py --force              # Force all steps
  python src/pipeline.py --dry-run            # Preview what would run
  python src/pipeline.py --steps 6,7,8,9,10   # Run analytics only
  python src/pipeline.py --skip-scrape        # Same as above
  python src/pipeline.py --retries 5          # More retries for flaky networks
        """,
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Ignore cadence checks; force-run all steps",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show which steps would run without executing them",
    )
    parser.add_argument(
        "--steps",
        type=str,
        default=None,
        help="Comma-separated step numbers to run (e.g. 3,4,5)",
    )
    parser.add_argument(
        "--skip-scrape",
        action="store_true",
        help="Skip scraping steps (1-4), only run analytics (5-13)",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="Max retries per step on failure (default: 3)",
    )
    parser.add_argument(
        "--backoff",
        type=float,
        default=5.0,
        help="Base backoff delay in seconds (default: 5.0)",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    selected_steps = None
    if args.steps:
        try:
            selected_steps = [int(s.strip()) for s in args.steps.split(",")]
            invalid = [s for s in selected_steps if s < 1 or s > 13]
            if invalid:
                logger.error("Invalid step numbers: %s (must be 1-13)", invalid)
                return 1
        except ValueError:
            logger.error("--steps must be comma-separated integers (e.g. 3,4,5)")
            return 1

    runner = PipelineRunner(
        force=args.force,
        dry_run=args.dry_run,
        selected_steps=selected_steps,
        skip_scrape=args.skip_scrape,
        max_retries=args.retries,
        backoff_base=args.backoff,
    )

    return runner.run()


if __name__ == "__main__":
    sys.exit(main())
