# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-06 14:03*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-06 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 23 |
| Median Discount | -8.68% |
| CONSIDER | 6 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 13 | 31.7% |
| -10% to -6% | 15 | 36.6% |
| -6% to -4% | 6 | 14.6% |
| -4% to 0% | 7 | 17.1% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.39 | -9.62% | 3.0y | high | 6d | -1.24% | 69.3 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 13.69 | 11.76 | -14.10% | 2.0y | high | 24d | -4.60% | 68.9 | → stable | — |
| 3 | NICBF | NIC ASIA Balanced Fund | 10.38 | 9.09 | -12.43% | 3.1y | medium | 2d | -0.86% | 60.5 | → stable | high_vol |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.94 | -4.88% | 2.0y | medium | 2d | 0.38% | 53.9 | ↑ narrowing | high_vol |
| 5 | NICSF | NIC Asia Select-30 | 9.80 | 9.35 | -4.59% | 2.0y | high | 2d | 1.45% | 53.8 | → stable | — |
| 6 | SEF | Siddhartha Equity Fund | 10.65 | 10.00 | -6.10% | 1.3y | high | 3d | 0.00% | 44.3 | ↓ widening | — |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 7 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -15.50% | maturity:5.7y |
| KDBY | -15.17% | maturity:6.1y |
| SBCF | -14.81% | maturity:4.7y |
| LVF2 | -14.55% | liquidity:low; maturity:7.2y |
| SFEF | -12.51% | liquidity:low; maturity:5.6y |
| NIBLSTF | -12.24% | maturity:9.6y |
| NICGF2 | -12.13% | maturity:4.4y |
| RSY | -11.89% | maturity:8.8y |
| SIGS3 | -10.92% | maturity:6.8y |
| KEF | -10.88% | maturity:4.7y |
| RBBF40 | -10.34% | maturity:11.4y |
| GBIMESY2 | -9.98% | liquidity:low; maturity:9.0y |
| LUK | -9.95% | maturity:4.1y |
| NSIF2 | -9.56% | maturity:6.2y |
| MBLEF | -9.26% | maturity:10.7y |
| NIBSF2 | -9.16% | maturity:4.9y |
| MNMF1 | -8.95% | maturity:8.5y |
| RMF2 | -8.68% | maturity:6.9y |
| KSY | -8.51% | liquidity:low; maturity:7.7y |
| C30MF | -8.23% | liquidity:low; maturity:6.9y |
| GIBF1 | -7.94% | liquidity:low; maturity:6.1y |
| H8020 | -7.92% | liquidity:low; maturity:7.2y |
| NMBHF2 | -7.20% | maturity:8.7y |
| SIGS2 | -6.42% | liquidity:low |
| GSY | -5.62% | maturity:8.5y |
| SAGF | -4.90% | maturity:7.4y |
| NIBLGF | -4.81% | maturity:6.5y |
| SFMF | -4.51% | liquidity:low |
| NMB50 | -3.87% | valuation:small_discount |
| SLCF | -3.38% | valuation:small_discount |
| MMF1 | -3.17% | valuation:small_discount; maturity:5.2y |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.2y |
| CMF2 | -2.65% | valuation:small_discount; liquidity:low |
| NBF2 | -1.62% | valuation:small_discount |
| HLICF | -0.67% | valuation:small_discount; maturity:9.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 23
- NAV data age: median 21 days, max 403 days

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
