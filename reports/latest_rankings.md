# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-09 14:33*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-09 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 30 |
| Median Discount | -12.33% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 26 | 66.7% |
| -10% to -6% | 8 | 20.5% |
| -6% to -4% | 5 | 12.8% |
| -4% to 0% | 0 | 0.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | LUK | Laxmi Unnati Kosh | 11.66 | 9.78 | -16.12% | 3.9y | medium | 2d | -1.17% | 74.5 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.03 | -12.33% | 2.8y | medium | 5d | 0.88% | 68.1 | ↑ narrowing | — |
| 3 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.20 | -18.58% | 3.2y | medium | 5d | -2.04% | 63.1 | ↓ widening | — |
| 4 | PSF | Prabhu Select Fund | 13.09 | 12.13 | -7.33% | 1.8y | high | 66d | 0.38% | 61.7 | ↑ narrowing | — |
| 5 | NICBF | NIC ASIA Balanced Fund | 10.32 | 8.66 | -16.09% | 3.0y | medium | 1d | 0.88% | 59.7 | ↓ widening | — |
| 6 | SEF | Siddhartha Equity Fund | 10.36 | 9.60 | -7.34% | 1.2y | high | 14d | -2.72% | 58.0 | ↑ narrowing | — |
| 7 | SLCF | Sanima Large Cap Fund | 10.14 | 8.92 | -12.03% | 1.5y | medium | 1d | -2.12% | 50.6 | ↓ widening | — |
| 8 | RMF1 | RBB Mutual Fund 1 | 10.31 | 9.79 | -5.04% | 1.9y | medium | 8d | -1.63% | 48.7 | ↑ narrowing | high_vol |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -20.68% | maturity:7.0y |
| SBCF | -18.08% | liquidity:low; maturity:4.5y |
| KDBY | -16.97% | maturity:5.9y |
| MBLEF | -16.74% | maturity:10.6y |
| RSY | -16.50% | maturity:8.7y |
| NICGF2 | -16.35% | liquidity:low; maturity:4.2y |
| SFEF | -16.10% | liquidity:low; maturity:5.4y |
| NIBSF2 | -15.84% | maturity:4.7y |
| NSIF2 | -15.74% | maturity:6.0y |
| KEF | -15.32% | maturity:4.5y |
| KSY | -15.02% | maturity:7.5y |
| NIBLSTF | -13.43% | maturity:9.4y |
| MNMF1 | -13.23% | maturity:8.3y |
| NICSF | -12.97% | liquidity:low |
| NIBLGF | -12.88% | maturity:6.4y |
| SIGS3 | -12.47% | maturity:6.6y |
| NMBHF2 | -11.42% | maturity:8.5y |
| SAGF | -11.29% | liquidity:low; maturity:7.2y |
| GBIMESY2 | -11.28% | maturity:8.9y |
| RMF2 | -10.63% | maturity:6.7y |
| GSY | -10.34% | maturity:8.3y |
| RBBF40 | -9.63% | liquidity:low; maturity:11.2y |
| SIGS2 | -9.22% | liquidity:low |
| NBF3 | -9.21% | maturity:5.0y |
| C30MF | -8.02% | liquidity:low; maturity:6.7y |
| PRSF | -7.39% | maturity:5.5y |
| GIBF1 | -6.62% | maturity:5.9y |
| MMF1 | -5.96% | maturity:5.0y |
| HLICF | -5.52% | liquidity:low; maturity:9.0y |
| NBF2 | -4.49% | liquidity:low |
| H8020 | -4.15% | maturity:7.1y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 27
- NAV data age: median 25 days, max 468 days

## Methodology

### Decision Gates
A fund receives **CONSIDER** only if ALL three gates pass:
1. **Valuation**: Discount to NAV ≤ -4% (deep or moderate discount)
2. **Liquidity**: Volume not in the bottom 25th percentile
3. **Maturity**: ≤ 4 years to maturity (discount convergence horizon)

### Composite Score
Within CONSIDER funds, a weighted composite score ranks relative attractiveness:
- Discount depth: 30% — deeper discount = higher score
- Liquidity: 15% — higher volume = higher score
- Maturity proximity: 15% — closer maturity = higher score
- NAV growth: 10% — positive month-over-month NAV return = higher score (fund manager quality)
- Price momentum: 10% — positive return = higher score
- Volatility (inverse): 10% — lower Parkinson vol = higher score
- Discount trend: 10% — narrowing discount = higher score

### Risk Metrics
- **Parkinson Volatility**: Estimated from OHLC (high/low) range — more efficient than close-to-close for small samples
- **Intraday Range**: `(high - low) / LTP` — measures trading friction
- **Volume CV**: Coefficient of variation of daily volume — flags erratic liquidity

---
*This report is auto-generated for research purposes only. Not investment advice.*
