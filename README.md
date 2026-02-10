# Nepal Mutual Fund Quantitative Analysis

Automated data scraping, analysis, and ranking system for mutual funds in Nepal.

## Features

- 📊 Automated NAV data scraping
- 📈 Returns and risk metrics calculation
- 🏆 Fund scoring and ranking
- ⏰ Scheduled daily updates via GitHub Actions
- 📋 Automated report generation

## Project Structure

```
nepal-mf-quant/
│
├── data/
│   ├── raw/                 # scraped NAVs
│   ├── processed/           # cleaned time series
│   └── metrics/             # computed metrics
│
├── src/
│   ├── scrape/
│   │   ├── nav_scraper.py
│   │   └── fund_metadata.py
│   │
│   ├── analytics/
│   │   ├── returns.py
│   │   ├── risk.py
│   │   └── scoring.py
│   │
│   └── pipeline.py          # end-to-end runner
│
├── reports/
│   ├── latest_rankings.md
│   └── metrics_table.csv
│
└── .github/workflows/
    └── scheduled.yml
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the complete pipeline:

```bash
python src/pipeline.py
```

## Reports

Check the `reports/` directory for:

- [Latest Rankings](reports/latest_rankings.md) - Markdown formatted rankings
- [Metrics Table](reports/metrics_table.csv) - CSV data for further analysis

## Automated Updates

The pipeline runs automatically every day via GitHub Actions. Check the [workflow file](.github/workflows/scheduled.yml) for scheduling details.

## License

MIT

## 📊 Daily Mutual Fund Decision Summary

<!-- AUTO-GENERATED-START -->

**Last updated**: 2026-02-10
**Funds analyzed**: 41
**CONSIDER**: 6
**IGNORE**: 35

### Current CONSIDER Candidates

| Symbol | Discount % | Days to Maturity | Liquidity | CONSIDER Streak |
|--------|------------|------------------|-----------|-----------------|
| NICFC | -8.68% | 1,221 | medium | 2 days |
| NBF2 | -8.06% | 1,206 | high | 2 days |
| NICBF | -7.37% | 1,294 | medium | 2 days |
| RMF1 | -6.69% | 894 | high | 2 days |
| PSF | -7.07% | 862 | medium | 1 day |
| NICSF | -6.60% | 876 | high | 1 day |

### Interpretation

This table highlights closed-end mutual funds that are trading at a discount to NAV, have sufficient liquidity, and are approaching maturity.
The system is rule-based and intended for research and monitoring purposes only.

<!-- AUTO-GENERATED-END -->
