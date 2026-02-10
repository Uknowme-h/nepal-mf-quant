# Nepal Mutual Fund Quantitative Analysis

A quantitative analysis platform for Nepal's closed-end mutual funds. Scrapes market data from NEPSE and NAV data from ShareSansar, computes risk-adjusted metrics, ranks funds by composite factor scoring, and applies rule-based screening to surface investment candidates trading at a discount to NAV.

## Key Capabilities

- **Automated Data Collection** — Daily OHLC prices from NEPSE (Playwright), monthly NAV from ShareSansar API, weekly fund metadata refresh
- **Multi-Factor Scoring** — Composite ranking across 6 factors: discount depth, liquidity, maturity, momentum, volatility, discount trend
- **Risk Analytics** — Parkinson volatility (OHLC-based), return volatility, intraday range, maximum drawdown, Sharpe ratio
- **Returns Analysis** — 1-day / 1-week / 1-month price returns, discount change tracking, NAV growth
- **Data Quality Validation** — NAV staleness detection, price outlier flags, volume anomaly checks, OHLC consistency
- **Rule-Based Screening** — CONSIDER/IGNORE decision engine with transparent gate-failure reasons
- **Automated Reporting** — Rich Markdown rankings, CSV metrics export, auto-updated README dashboard

## Project Structure

```
nepal-mf-quant/
├── src/
│   ├── pipeline.py                 # 12-step orchestrator with retry, cadence, logging
│   ├── scrape/
│   │   ├── fund_universe.py        # ShareSansar fund metadata scraper
│   │   ├── fund_metadata.py        # Fund detail enrichment
│   │   └── nav_scraper.py          # Monthly NAV data from ShareSansar API
│   └── analytics/
│       ├── valuation.py            # NAV-to-price discount calculation
│       ├── returns.py              # Price returns, discount change, NAV growth
│       ├── risk.py                 # Parkinson vol, drawdown, Sharpe ratio
│       ├── scoring.py              # 6-factor composite scoring engine
│       ├── data_quality.py         # Data freshness and consistency checks
│       ├── decision_layer.py       # CONSIDER/IGNORE rule-based screening
│       ├── decision_history.py     # Temporal decision tracking
│       ├── report_generator.py     # Markdown + CSV report generation
│       └── update_readme.py        # README dashboard auto-updater
├── scrapers/
│   ├── market/
│   │   └── daily_price_scraper.py  # NEPSE OHLC via Playwright
│   └── mappings/
│       └── build_symbol_nepse_map.py
├── data/
│   ├── raw/                        # Scraped: fund_universe, market_prices, nav/*.csv
│   ├── processed/                  # Analytics output: snapshots, decisions, scores
│   ├── history/                    # Temporal decision log
│   ├── metrics/                    # Computed metrics archive
│   └── reference/                  # Symbol mappings, security IDs
└── reports/
    ├── latest_rankings.md          # Detailed fund rankings report
    └── metrics_table.csv           # Comprehensive metrics for all funds
```

## Pipeline Steps

The orchestrator (`src/pipeline.py`) runs 12 steps in dependency order:

| Step | Name          | Cadence | Critical | Description                                |
| ---- | ------------- | ------- | -------- | ------------------------------------------ |
| 1    | Fund Universe | Weekly  | No       | Scrape fund metadata from ShareSansar      |
| 2    | NAV Data      | Monthly | No       | Fetch latest NAV from ShareSansar API      |
| 3    | Market Prices | Daily   | Yes      | Scrape OHLC prices from NEPSE (Playwright) |
| 4    | Data Quality  | Daily   | No       | Validate freshness, outliers, coverage     |
| 5    | Valuation     | Daily   | Yes      | Join NAV + prices, calculate discounts     |
| 6    | Returns       | Daily   | Yes      | Price returns, discount change, NAV growth |
| 7    | Risk Metrics  | Daily   | Yes      | Parkinson vol, drawdown, Sharpe ratio      |
| 8    | Scoring       | Daily   | Yes      | Composite factor ranking                   |
| 9    | Decisions     | Daily   | Yes      | CONSIDER/IGNORE screening                  |
| 10   | History       | Daily   | Yes      | Append to temporal decision log            |
| 11   | Reports       | Daily   | No       | Generate Markdown + CSV reports            |
| 12   | README        | Daily   | No       | Update dashboard in README.md              |

## Scoring Methodology

Funds are ranked by a weighted composite of percentile scores:

| Factor               | Weight | Source        | Direction                    |
| -------------------- | ------ | ------------- | ---------------------------- |
| Discount to NAV      | 35%    | Valuation     | Deeper discount = better     |
| Liquidity            | 20%    | Market volume | Higher = better              |
| Maturity Proximity   | 15%    | Fund metadata | Closer maturity = better     |
| Momentum (1m return) | 10%    | Returns       | Higher = better              |
| Low Volatility       | 10%    | Risk metrics  | Lower Parkinson vol = better |
| Discount Trend       | 10%    | Returns       | Narrowing discount = better  |

Funds with missing factors have weights re-normalized across available factors.

## Installation

```bash
git clone https://github.com/your-repo/nepal-mf-quant.git
cd nepal-mf-quant
pip install -r requirements.txt
playwright install chromium
```

## Usage

```bash
# Full daily run (respects cadence rules)
python src/pipeline.py

# Force all steps regardless of cadence
python src/pipeline.py --force

# Preview what would run without executing
python src/pipeline.py --dry-run

# Skip scraping, run analytics only (steps 4-12)
python src/pipeline.py --skip-scrape

# Run specific steps
python src/pipeline.py --steps 5,6,7,8,9

# Build symbol-NEPSE mapping (first-time setup)
python scrapers/mappings/build_symbol_nepse_map.py
```

## Reports

- [Latest Rankings](reports/latest_rankings.md) — Detailed fund analysis with scores, trends, and risk flags
- [Metrics Table](reports/metrics_table.csv) — Comprehensive per-fund metrics for custom analysis

## Data Sources

| Source                                                | Data                            | Method                        |
| ----------------------------------------------------- | ------------------------------- | ----------------------------- |
| [NEPSE](https://nepalstock.com.np)                    | Daily OHLC, volume, trade count | Playwright browser automation |
| [ShareSansar](https://merolagani.com/mutualfund.aspx) | Fund universe, NAV, metadata    | HTTP API / HTML scraping      |

## License

MIT

## 📊 Daily Mutual Fund Decision Summary

<!-- AUTO-GENERATED-START -->

### Market Snapshot

| | |
|---|---|
| **Date** | 2026-02-10 |
| **Funds Tracked** | 41 |
| **Median Discount** | -6.60% |
| **At Discount** | 39 (95%) |
| **Deep Discount (≤-8%)** | 9 |
| **CONSIDER** | 6 |
| **IGNORE** | 35 |

> ⚠️ 41 fund(s) have NAV data older than 45 days.

### Discount Distribution

| Range | Distribution |
|-------|-------------|
|         < -10% |  0 |
|    -10% to -6% | ███████████████████████ 23 |
|     -6% to -4% | ███████ 7 |
|      -4% to 0% | █████████ 9 |
|           ≥ 0% | ██ 2 |

### Active CONSIDER Candidates

| # | Symbol | Name | Discount | NAV | LTP | Maturity | Liquidity | Streak | Score | Trend |
|---|--------|------|----------|-----|-----|----------|-----------|--------|-------|-------|
| 1 | **NICFC** | NIC Asia Flexi Cap F | -8.68% | 10.02 | 9.15 | 3.4y | medium | 2d | 66.5 | → |
| 2 | **PSF** | Prabhu Select Fund | -7.07% | 12.03 | 11.18 | 2.4y | medium | 1d | 64.6 | ↑ |
| 3 | **NBF2** | Nabil Balanced Fund  | -8.06% | 10.42 | 9.58 | 3.3y | high | 2d | 63.8 | ↓ |
| 4 | **NICBF** | NIC ASIA Balanced Fu | -7.37% | 10.04 | 9.30 | 3.5y | medium | 2d | 61.7 | → |
| 5 | **NICSF** | NIC Asia Select-30 | -6.60% | 9.54 | 8.91 | 2.4y | high | 1d | 60.2 | → |
| 6 | **RMF1** | RBB Mutual Fund 1 | -6.69% | 10.02 | 9.35 | 2.5y | medium | 2d | 48.7 | ↓ |

### Top Picks by Composite Score

- **NICFC** (NIC Asia Flexi Cap Fund): -8.68% discount, score 66.5
- **PSF** (Prabhu Select Fund): -7.07% discount, score 64.6
- **NBF2** (Nabil Balanced Fund - 2): -8.06% discount, score 63.8

### Interpretation

CONSIDER = discount ≤ -4% AND liquidity ≠ low AND maturity ≤ 4 years. Funds are ranked by a composite score (discount 35%, liquidity 20%, maturity 15%, momentum 10%, volatility 10%, trend 10%). This is rule-based screening for research purposes only.

### Data Status

- Latest price data: 2026-02-10
- NAV data age: median 57 days
- History depth: 2 trading day(s)
- Full report: [reports/latest_rankings.md](reports/latest_rankings.md)
- Metrics CSV: [reports/metrics_table.csv](reports/metrics_table.csv)

<!-- AUTO-GENERATED-END -->
