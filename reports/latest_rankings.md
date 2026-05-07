# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-07 12:06*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-07 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 30 |
| Median Discount | -10.32% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 22 | 53.7% |
| -10% to -6% | 13 | 31.7% |
| -6% to -4% | 3 | 7.3% |
| -4% to 0% | 3 | 7.3% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SIGS2 | Siddhartha Investment Gro | 11.53 | 10.34 | -10.32% | 3.3y | high | 2d | 5.01% | 73.2 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 14.35 | 12.01 | -16.31% | 2.1y | medium | 4d | 12.55% | 69.6 | ↓ widening | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.27 | -11.88% | 3.1y | medium | 1d | 4.26% | 68.8 | → stable | — |
| 4 | SEF | Siddhartha Equity Fund | 10.95 | 9.90 | -9.59% | 1.5y | medium | 3d | 3.79% | 52.3 | ↓ widening | high_vol |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.64 | 9.80 | -7.89% | 2.2y | medium | 12d | 0.76% | 48.8 | ↑ narrowing | high_vol |
| 6 | SLCF | Sanima Large Cap Fund | 10.65 | 9.62 | -9.67% | 1.8y | medium | 20d | 0.47% | 47.9 | ↓ widening | — |
| 7 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.00 | -4.49% | 3.1y | high | 3d | 0.48% | 45.0 | ↓ widening | — |
| 8 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.31 | -8.76% | 3.5y | medium | 2d | -2.04% | 39.0 | ↓ widening | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -18.36% | maturity:5.9y |
| KDBY | -18.05% | maturity:6.2y |
| KEF | -17.13% | maturity:4.9y |
| LVF2 | -16.39% | liquidity:low; maturity:7.3y |
| GIBF1 | -14.57% | maturity:6.2y |
| SBCF | -13.58% | maturity:4.9y |
| SIGS3 | -13.52% | liquidity:low; maturity:7.0y |
| LUK | -13.38% | maturity:4.3y |
| SFEF | -12.60% | maturity:5.8y |
| RSY | -12.14% | maturity:9.0y |
| KSY | -11.63% | liquidity:low; maturity:7.9y |
| MBLEF | -11.55% | maturity:10.9y |
| NSIF2 | -11.49% | maturity:6.3y |
| MNMF1 | -11.39% | maturity:8.6y |
| C30MF | -11.10% | liquidity:low; maturity:7.0y |
| GSY | -10.93% | maturity:8.7y |
| NMBHF2 | -10.86% | maturity:8.8y |
| NICGF2 | -10.68% | maturity:4.5y |
| NICBF | -10.12% | liquidity:low |
| NIBSF2 | -9.41% | maturity:5.1y |
| RMF2 | -9.41% | maturity:7.0y |
| H8020 | -9.13% | liquidity:low; maturity:7.4y |
| GBIMESY2 | -8.70% | maturity:9.2y |
| SAGF | -8.10% | maturity:7.6y |
| RBBF40 | -7.01% | liquidity:low; maturity:11.5y |
| CMF2 | -6.84% | liquidity:low |
| NIBLSTF | -6.47% | maturity:9.8y |
| NIBLGF | -6.02% | maturity:6.7y |
| NBF3 | -4.94% | maturity:5.4y |
| NMB50 | -4.09% | liquidity:low |
| MMF1 | -3.51% | valuation:small_discount; maturity:5.3y |
| NICSF | -2.93% | valuation:small_discount; liquidity:low |
| HLICF | -1.29% | valuation:small_discount; maturity:9.4y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 33
- NAV data age: median 22 days, max 343 days

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
