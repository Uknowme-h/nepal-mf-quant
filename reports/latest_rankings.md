# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-22 10:49*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-22 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 35 |
| At Premium (price ≥ NAV) | 6 |
| Deep Discount (≤ -8%) | 4 |
| Median Discount | -3.37% |
| CONSIDER | 2 |
| IGNORE | 39 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 3 | 7.3% |
| -10% to -6% | 1 | 2.4% |
| -6% to -4% | 12 | 29.3% |
| -4% to 0% | 19 | 46.3% |
| ≥ 0% (premium) | 6 | 14.6% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.09 | 9.63 | -4.56% | 3.2y | medium | 2d | 0.70% | 62.1 | ↑ narrowing | — |
| 2 | NICBF | NIC ASIA Balanced Fund | 10.03 | 9.58 | -4.49% | 3.4y | medium | 1d | -0.10% | 41.7 | ↓ widening | high_vol |

## IGNORE Summary

*39 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 25 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -14.29% | maturity:5.0y |
| LUK | -14.24% | liquidity:low; maturity:4.4y |
| LVF2 | -13.23% | maturity:7.5y |
| SFEF | -9.80% | liquidity:low; maturity:5.9y |
| NSIF2 | -5.85% | liquidity:low; maturity:6.5y |
| MNMF1 | -5.20% | maturity:8.8y |
| NICGF2 | -5.02% | maturity:4.7y |
| PRSF | -4.87% | maturity:6.0y |
| MBLEF | -4.84% | maturity:11.0y |
| SIGS3 | -4.54% | liquidity:low; maturity:7.1y |
| GSY | -4.53% | maturity:8.8y |
| SFMF | -4.51% | liquidity:low |
| NMBHF2 | -4.44% | maturity:8.9y |
| NBF3 | -4.36% | maturity:5.5y |
| NBF2 | -3.72% | valuation:small_discount |
| C30MF | -3.68% | valuation:small_discount; maturity:7.2y |
| GIBF1 | -3.65% | valuation:small_discount; maturity:6.4y |
| RMF2 | -3.45% | valuation:small_discount; liquidity:low; maturity:7.2y |
| NIBLGF | -3.37% | valuation:small_discount; maturity:6.8y |
| KSY | -3.32% | valuation:small_discount; maturity:8.0y |
| GBIMESY2 | -3.13% | valuation:small_discount; liquidity:low; maturity:9.3y |
| SAGF | -2.94% | valuation:small_discount; maturity:7.7y |
| KDBY | -2.29% | valuation:small_discount; maturity:6.3y |
| SLCF | -2.17% | valuation:small_discount |
| RSY | -2.04% | valuation:small_discount; maturity:9.1y |
| KEF | -1.88% | valuation:small_discount; maturity:5.0y |
| H8020 | -1.82% | valuation:small_discount; maturity:7.5y |
| NIBLSTF | -1.74% | valuation:small_discount; maturity:9.9y |
| HLICF | -1.15% | valuation:small_discount; liquidity:low; maturity:9.5y |
| NIBSF2 | -0.81% | valuation:small_discount; maturity:5.2y |
| RBBF40 | -0.81% | valuation:small_discount; liquidity:low; maturity:11.7y |
| PSF | -0.41% | valuation:small_discount |
| RMF1 | -0.20% | valuation:small_discount |
| CMF2 | 0.29% | valuation:premium; liquidity:low |
| NICSF | 0.73% | valuation:premium |
| SEF | 1.09% | valuation:premium |
| SIGS2 | 1.34% | valuation:premium |
| NMB50 | 2.62% | valuation:premium |
| MMF1 | 3.13% | valuation:premium; maturity:5.5y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 6
- NAV data age: median 35 days, max 297 days

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
