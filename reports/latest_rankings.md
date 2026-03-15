# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-15 10:51*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-15 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 4 |
| Median Discount | -4.61% |
| CONSIDER | 4 |
| IGNORE | 37 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 4 | 9.8% |
| -10% to -6% | 6 | 14.6% |
| -6% to -4% | 20 | 48.8% |
| -4% to 0% | 8 | 19.5% |
| ≥ 0% (premium) | 3 | 7.3% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.90 | -5.44% | 3.2y | high | 2d | 0.48% | 68.4 | ↑ narrowing | — |
| 2 | SIGS2 | Siddhartha Investment Gro | 10.44 | 10.00 | -4.21% | 3.5y | medium | 1d | 0.29% | 62.9 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.09 | 9.50 | -5.85% | 3.2y | high | 2d | 0.70% | 58.0 | ↓ widening | — |
| 4 | SLCF | Sanima Large Cap Fund | 10.15 | 9.72 | -4.24% | 1.9y | medium | 3d | 0.30% | 49.1 | → stable | — |

## IGNORE Summary

*37 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 11 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -15.01% | liquidity:low; maturity:4.4y |
| SBCF | -14.46% | maturity:5.0y |
| LVF2 | -13.76% | liquidity:low; maturity:7.5y |
| SFEF | -11.64% | maturity:5.9y |
| GIBF1 | -7.47% | liquidity:low; maturity:6.4y |
| NSIF2 | -6.45% | maturity:6.5y |
| NICGF2 | -6.40% | maturity:4.7y |
| MNMF1 | -6.36% | maturity:8.8y |
| NBF3 | -6.20% | maturity:5.5y |
| RMF2 | -6.16% | liquidity:low; maturity:7.2y |
| SFMF | -5.22% | liquidity:low |
| NMBHF2 | -5.11% | liquidity:low; maturity:9.0y |
| NIBSF2 | -5.09% | maturity:5.2y |
| KEF | -5.06% | maturity:5.0y |
| SAGF | -5.03% | maturity:7.7y |
| MBLEF | -4.94% | maturity:11.0y |
| RSY | -4.83% | maturity:9.1y |
| PRSF | -4.71% | maturity:6.0y |
| NIBLSTF | -4.61% | maturity:9.9y |
| KDBY | -4.39% | maturity:6.4y |
| SIGS3 | -4.36% | liquidity:low; maturity:7.1y |
| KSY | -4.30% | maturity:8.0y |
| C30MF | -4.25% | maturity:7.2y |
| NIBLGF | -4.09% | maturity:6.8y |
| GSY | -4.05% | maturity:8.8y |
| GBIMESY2 | -4.04% | liquidity:low; maturity:9.3y |
| RMF1 | -3.49% | valuation:small_discount |
| NICBF | -3.19% | valuation:small_discount |
| PSF | -2.57% | valuation:small_discount |
| H8020 | -2.56% | valuation:small_discount; liquidity:low; maturity:7.5y |
| MMF1 | -2.30% | valuation:small_discount; maturity:5.5y |
| HLICF | -1.88% | valuation:small_discount; liquidity:low; maturity:9.5y |
| RBBF40 | -0.71% | valuation:small_discount; maturity:11.7y |
| NICSF | -0.10% | valuation:small_discount |
| NMB50 | 0.19% | valuation:premium |
| CMF2 | 1.17% | valuation:premium |
| SEF | 4.38% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 5
- NAV data age: median 28 days, max 290 days

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
