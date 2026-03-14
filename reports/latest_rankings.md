# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-14 10:48*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-12 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 4 |
| Median Discount | -4.76% |
| CONSIDER | 4 |
| IGNORE | 37 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 3 | 7.3% |
| -10% to -6% | 10 | 24.4% |
| -6% to -4% | 10 | 24.4% |
| -4% to 0% | 15 | 36.6% |
| ≥ 0% (premium) | 3 | 7.3% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.50 | -7.08% | 3.6y | medium | 4d | -2.04% | 69.8 | ↑ narrowing | — |
| 2 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.87 | -5.73% | 3.2y | high | 1d | 0.48% | 68.3 | ↑ narrowing | — |
| 3 | SLCF | Sanima Large Cap Fund | 10.15 | 9.64 | -5.02% | 1.9y | high | 2d | 0.30% | 59.8 | ↑ narrowing | — |
| 4 | NICFC | NIC Asia Flexi Cap Fund | 10.02 | 9.50 | -5.19% | 3.3y | medium | 1d | 3.51% | 50.2 | ↑ narrowing | — |

## IGNORE Summary

*37 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 18 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -14.24% | liquidity:low; maturity:4.4y |
| SBCF | -12.79% | maturity:5.0y |
| LVF2 | -12.53% | liquidity:low; maturity:7.5y |
| SFEF | -9.89% | maturity:5.9y |
| NMBHF2 | -7.33% | maturity:9.0y |
| NICGF2 | -6.90% | liquidity:low; maturity:4.7y |
| NSIF2 | -6.79% | maturity:6.5y |
| KDBY | -6.77% | maturity:6.4y |
| GIBF1 | -6.62% | maturity:6.4y |
| RMF2 | -6.62% | liquidity:low; maturity:7.2y |
| PRSF | -6.57% | maturity:6.0y |
| KSY | -6.45% | liquidity:low; maturity:8.0y |
| GBIMESY2 | -5.55% | liquidity:low; maturity:9.4y |
| RSY | -5.39% | maturity:9.2y |
| NBF3 | -5.04% | maturity:5.5y |
| GSY | -5.01% | maturity:8.8y |
| KEF | -4.76% | maturity:5.0y |
| NIBSF2 | -4.68% | maturity:5.2y |
| SIGS3 | -4.26% | liquidity:low; maturity:7.1y |
| RBBF40 | -3.84% | valuation:small_discount; maturity:11.7y |
| C30MF | -3.77% | valuation:small_discount; maturity:7.2y |
| PSF | -3.73% | valuation:small_discount |
| MNMF1 | -3.66% | valuation:small_discount; maturity:8.8y |
| NICBF | -3.29% | valuation:small_discount |
| RMF1 | -2.89% | valuation:small_discount |
| SAGF | -2.67% | valuation:small_discount; liquidity:low; maturity:7.7y |
| H8020 | -2.56% | valuation:small_discount; liquidity:low; maturity:7.6y |
| NIBLGF | -2.45% | valuation:small_discount; maturity:6.9y |
| MBLEF | -2.29% | valuation:small_discount; maturity:11.1y |
| NIBLSTF | -1.74% | valuation:small_discount; maturity:9.9y |
| MMF1 | -0.84% | valuation:small_discount; maturity:5.5y |
| SIGS2 | -0.57% | valuation:small_discount |
| CMF2 | -0.29% | valuation:small_discount |
| HLICF | -0.21% | valuation:small_discount; liquidity:low; maturity:9.5y |
| NICSF | 0.10% | valuation:premium |
| NMB50 | 0.19% | valuation:premium |
| SEF | 0.40% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 13
- NAV data age: median 27 days, max 289 days

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
