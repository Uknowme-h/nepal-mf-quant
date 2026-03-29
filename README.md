# Nepal Mutual Fund Quantitative Analysis

A quantitative analysis platform for Nepal's closed-end mutual funds. Scrapes market data from NEPSE and NAV data from ShareSansar, computes risk-adjusted metrics, ranks funds by composite factor scoring, and applies rule-based screening to surface investment candidates trading at a discount to NAV.

## Key Capabilities

- **Automated Data Collection** — Daily OHLC prices from NEPSE (Playwright), monthly NAV from ShareSansar API + 7 direct fund management company APIs, weekly fund metadata refresh
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
│   ├── pipeline.py                 # 13-step orchestrator with retry, cadence, logging
│   ├── scrape/
│   │   ├── fund_universe.py        # ShareSansar fund metadata scraper
│   │   ├── fund_metadata.py        # Fund detail enrichment
│   │   ├── nav_scraper.py          # Monthly NAV data from ShareSansar API
│   │   └── monthly_nav_scraper.py  # Direct provider APIs (7 fund companies)
│   └── analytics/
│       ├── valuation.py            # NAV-to-price discount calculation
│       ├── returns.py              # Price returns, discount change, NAV growth
│       ├── risk.py                 # Parkinson vol, drawdown, Sharpe ratio
│       ├── scoring.py              # 7-factor composite scoring engine
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

The orchestrator (`src/pipeline.py`) runs 13 steps in dependency order:

| Step | Name              | Cadence | Critical | Description                                               |
| ---- | ----------------- | ------- | -------- | --------------------------------------------------------- |
| 1    | Fund Universe     | Weekly  | No       | Scrape fund metadata from ShareSansar                     |
| 2    | NAV (ShareSansar) | Monthly | No       | Fetch latest NAV from ShareSansar API                     |
| 3    | NAV (Providers)   | Weekly  | No       | Fetch historical monthly NAVs from 7 direct provider APIs |
| 4    | Market Prices     | Daily   | Yes      | Scrape OHLC prices from NEPSE (Playwright)                |
| 5    | Data Quality      | Daily   | No       | Validate freshness, outliers, coverage                    |
| 6    | Valuation         | Daily   | Yes      | Join NAV + prices, calculate discounts                    |
| 7    | Returns           | Daily   | Yes      | Price returns, discount change, NAV growth                |
| 8    | Risk Metrics      | Daily   | Yes      | Parkinson vol, drawdown, Sharpe ratio                     |
| 9    | Scoring           | Daily   | Yes      | Composite factor ranking                                  |
| 10   | Decisions         | Daily   | Yes      | CONSIDER/IGNORE screening                                 |
| 11   | History           | Daily   | Yes      | Append to temporal decision log                           |
| 12   | Reports           | Daily   | No       | Generate Markdown + CSV reports                           |
| 13   | README            | Daily   | No       | Update dashboard in README.md                             |

## Scoring Methodology

Funds are ranked by a weighted composite of percentile scores:

| Factor               | Weight | Source        | Direction                      |
| -------------------- | ------ | ------------- | ------------------------------ |
| Discount to NAV      | 30%    | Valuation     | Deeper discount = better       |
| Liquidity            | 15%    | Market volume | Higher = better                |
| Maturity Proximity   | 15%    | Fund metadata | Closer maturity = better       |
| NAV Growth           | 10%    | NAV history   | Higher MoM NAV return = better |
| Momentum (1w return) | 10%    | Returns       | Higher = better                |
| Low Volatility       | 10%    | Risk metrics  | Lower Parkinson vol = better   |
| Discount Trend       | 10%    | Returns       | Narrowing discount = better    |

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

# Skip scraping, run analytics only (steps 5-13)
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

| Source                                 | Data                                    | Method                        |
| -------------------------------------- | --------------------------------------- | ----------------------------- |
| [NEPSE](https://nepalstock.com.np)     | Daily OHLC, volume, trade count         | Playwright browser automation |
| [ShareSansar](https://sharesansar.com) | Fund universe, NAV, metadata            | HTTP API / HTML scraping      |
| Laxmi Capital                          | LUK, LVF2, SFEF, SFMF, SBCF monthly NAV | Vue SPA REST API              |
| NMB Capital                            | NMB50, NSIF2, NMBHF2 monthly NAV        | Vue SPA REST API              |
| NIC Asia Capital                       | NICBF, NICFC, NICGF2 monthly NAV        | HTML table scrape             |
| Nabil Investment                       | NBF2, NBF3 monthly NAV                  | WordPress AJAX                |
| Kumari Capital                         | KSY monthly NAV                         | Directus REST API             |
| Prabhu Capital                         | PRSF, PSF monthly NAV                   | REST API                      |
| Sanima Capital                         | SAGF monthly NAV                        | Vue SPA REST API              |

## License

MIT

## 📊 Daily Mutual Fund Decision Summary

<!-- AUTO-GENERATED-START -->

### Market Snapshot

| | |
|---|---|
| **Date** | 2026-03-29 |
| **Funds Tracked** | 41 |
| **Median Discount** | -2.99% |
| **At Discount** | 35 (85%) |
| **Deep Discount (≤-8%)** | 6 |
| **CONSIDER** | 2 |
| **IGNORE** | 39 |

> ⚠️ 5 fund(s) have NAV data older than 45 days.

### Discount Distribution

| Range | Distribution |
|-------|-------------|
|         < -10% | ███ 3 |
|    -10% to -6% | ████████ 8 |
|     -6% to -4% | ████ 4 |
|      -4% to 0% | ████████████████████ 20 |
|           ≥ 0% | ██████ 6 |

### Active CONSIDER Candidates

| # | Symbol | Name | Discount | NAV | LTP | Maturity | Liquidity | Streak | NAV Δ | Score | Trend |
|---|--------|------|----------|-----|-----|----------|-----------|--------|-------|-------|-------|
| 1 | **NICFC** | NIC Asia Flexi Cap F | -4.26% | 10.09 | 9.66 | 3.2y | medium | 1d | 0.70% | 63.2 | → |
| 2 | **SFMF** | Sunrise First Mutual | -6.81% | 11.30 | 10.53 | 3.6y | medium | 2d | -2.04% | 50.4 | ↓ |

### Top Picks by Composite Score

- **NICFC** (NIC Asia Flexi Cap Fund): -4.26% discount, score 63.2
- **SFMF** (Sunrise First Mutual Fund): -6.81% discount, score 50.4

### Interpretation

CONSIDER = discount ≤ -4% AND liquidity ≠ low AND maturity ≤ 4 years. Funds are ranked by a 7-factor composite score (discount 30%, liquidity 15%, maturity 15%, NAV growth 10%, momentum 10%, volatility 10%, trend 10%). NAV growth reflects fund manager performance via month-over-month NAV returns. This is rule-based screening for research purposes only.

### Data Status

- Latest price data: 2026-03-29
- NAV data age: median 42 days
- History depth: 27 trading day(s)
- Full report: [reports/latest_rankings.md](reports/latest_rankings.md)
- Metrics CSV: [reports/metrics_table.csv](reports/metrics_table.csv)

<!-- AUTO-GENERATED-END -->
