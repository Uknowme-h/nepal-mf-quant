# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-04 14:21*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-03 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 33 |
| Median Discount | -12.91% |
| CONSIDER | 9 |
| IGNORE | 30 |

> ⚠️ **NAV Staleness Warning**: 17 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 28 | 71.8% |
| -10% to -6% | 9 | 23.1% |
| -6% to -4% | 2 | 5.1% |
| -4% to 0% | 0 | 0.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.27 | -17.96% | 3.2y | medium | 3d | -2.04% | 64.9 | ↓ widening | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.72 | -15.34% | 2.8y | medium | 3d | 0.88% | 63.7 | ↓ widening | — |
| 3 | NICBF | NIC ASIA Balanced Fund | 10.32 | 8.72 | -15.50% | 3.0y | high | 1d | 0.88% | 59.5 | ↓ widening | high_vol |
| 4 | SEF | Siddhartha Equity Fund | 10.36 | 9.40 | -9.27% | 1.2y | high | 12d | -2.72% | 55.4 | ↓ widening | — |
| 5 | SLCF | Sanima Large Cap Fund | 10.14 | 9.06 | -10.65% | 1.5y | medium | 1d | -2.12% | 53.5 | → stable | — |
| 6 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.80 | -6.40% | 2.7y | medium | 2d | 0.48% | 53.5 | ↑ narrowing | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.31 | 9.50 | -7.86% | 1.9y | high | 6d | -1.63% | 52.6 | → stable | high_vol |
| 8 | PSF | Prabhu Select Fund | 13.04 | 11.99 | -8.05% | 1.8y | high | 64d | -4.26% | 50.8 | ↓ widening | — |
| 9 | NICSF | NIC Asia Select-30 | 9.48 | 8.31 | -12.34% | 1.8y | medium | 2d | -3.27% | 50.5 | ↓ widening | — |

## IGNORE Summary

*30 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -20.46% | maturity:4.6y |
| LUK | -19.38% | liquidity:low |
| LVF2 | -18.76% | maturity:7.0y |
| KDBY | -18.30% | maturity:5.9y |
| NICGF2 | -16.92% | maturity:4.2y |
| MBLEF | -16.47% | maturity:10.6y |
| RSY | -16.42% | maturity:8.7y |
| NIBSF2 | -15.23% | liquidity:low; maturity:4.7y |
| NIBLGF | -15.21% | liquidity:low; maturity:6.4y |
| NSIF2 | -15.09% | maturity:6.0y |
| RMF2 | -14.94% | liquidity:low; maturity:6.7y |
| KSY | -14.34% | liquidity:low; maturity:7.5y |
| NMBHF2 | -14.31% | maturity:8.5y |
| SFEF | -13.74% | maturity:5.5y |
| MNMF1 | -13.71% | maturity:8.3y |
| KEF | -13.62% | maturity:4.5y |
| NIBLSTF | -12.91% | liquidity:low; maturity:9.4y |
| SIGS3 | -12.55% | maturity:6.7y |
| SIGS2 | -11.05% | liquidity:low |
| GIBF1 | -10.78% | maturity:5.9y |
| RBBF40 | -10.63% | liquidity:low; maturity:11.2y |
| GSY | -10.14% | maturity:8.3y |
| GBIMESY2 | -10.07% | liquidity:low; maturity:8.9y |
| SAGF | -8.63% | maturity:7.2y |
| MMF1 | -8.26% | maturity:5.0y |
| PRSF | -8.13% | maturity:5.5y |
| NBF3 | -7.56% | maturity:5.1y |
| C30MF | -6.13% | liquidity:low; maturity:6.7y |
| HLICF | -4.37% | maturity:9.0y |
| H8020 | -4.31% | maturity:7.1y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 33
- NAV data age: median 20 days, max 463 days

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
