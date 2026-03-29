# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-29 10:54*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-29 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 35 |
| At Premium (price ≥ NAV) | 6 |
| Deep Discount (≤ -8%) | 6 |
| Median Discount | -2.99% |
| CONSIDER | 2 |
| IGNORE | 39 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 3 | 7.3% |
| -10% to -6% | 8 | 19.5% |
| -6% to -4% | 4 | 9.8% |
| -4% to 0% | 20 | 48.8% |
| ≥ 0% (premium) | 6 | 14.6% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.09 | 9.66 | -4.26% | 3.2y | medium | 1d | 0.70% | 63.2 | → stable | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.53 | -6.81% | 3.6y | medium | 2d | -2.04% | 50.4 | ↓ widening | — |

## IGNORE Summary

*39 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 26 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -13.38% | maturity:4.4y |
| LVF2 | -13.23% | liquidity:low; maturity:7.4y |
| SBCF | -13.14% | liquidity:low; maturity:5.0y |
| NSIF2 | -9.75% | maturity:6.4y |
| NMBHF2 | -9.30% | maturity:8.9y |
| KSY | -8.37% | maturity:8.0y |
| SFEF | -7.26% | maturity:5.9y |
| PRSF | -7.24% | liquidity:low; maturity:6.0y |
| SAGF | -6.93% | liquidity:low; maturity:7.7y |
| PSF | -6.59% | liquidity:low |
| MBLEF | -5.76% | liquidity:low; maturity:11.0y |
| GIBF1 | -4.07% | maturity:6.3y |
| SIGS2 | -4.02% | liquidity:low |
| NBF2 | -3.92% | valuation:small_discount |
| NICGF2 | -3.65% | valuation:small_discount; liquidity:low; maturity:4.7y |
| NBF3 | -3.20% | valuation:small_discount; maturity:5.5y |
| GSY | -3.09% | valuation:small_discount; maturity:8.8y |
| KDBY | -3.02% | valuation:small_discount; maturity:6.3y |
| RMF2 | -2.99% | valuation:small_discount; maturity:7.2y |
| C30MF | -2.83% | valuation:small_discount; maturity:7.1y |
| NIBSF2 | -2.75% | valuation:small_discount; maturity:5.2y |
| MNMF1 | -2.70% | valuation:small_discount; maturity:8.7y |
| RSY | -2.51% | valuation:small_discount; maturity:9.1y |
| RBBF40 | -2.22% | valuation:small_discount; liquidity:low; maturity:11.6y |
| GBIMESY2 | -2.12% | valuation:small_discount; maturity:9.3y |
| H8020 | -1.82% | valuation:small_discount; maturity:7.5y |
| SIGS3 | -1.76% | valuation:small_discount; maturity:7.1y |
| NIBLSTF | -1.74% | valuation:small_discount; maturity:9.9y |
| RMF1 | -1.60% | valuation:small_discount |
| SLCF | -1.48% | valuation:small_discount |
| NMB50 | -1.47% | valuation:small_discount |
| KEF | -0.79% | valuation:small_discount; maturity:5.0y |
| NICSF | -0.31% | valuation:small_discount |
| SEF | 0.50% | valuation:premium |
| HLICF | 0.52% | valuation:premium; liquidity:low; maturity:9.5y |
| CMF2 | 0.88% | valuation:premium |
| NICBF | 1.60% | valuation:premium |
| MMF1 | 2.30% | valuation:premium; maturity:5.5y |
| NIBLGF | 5.41% | valuation:premium; maturity:6.8y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 14
- NAV data age: median 42 days, max 304 days

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
