# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-16 11:12*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-16 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 4 |
| Median Discount | -4.84% |
| CONSIDER | 4 |
| IGNORE | 37 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 4 | 9.8% |
| -10% to -6% | 8 | 19.5% |
| -6% to -4% | 18 | 43.9% |
| -4% to 0% | 11 | 26.8% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 12.05 | 11.54 | -4.23% | 2.3y | high | 1d | 0.17% | 62.7 | ↑ narrowing | — |
| 2 | SIGS2 | Siddhartha Investment Gro | 10.44 | 9.98 | -4.41% | 3.5y | medium | 2d | 0.29% | 60.7 | ↑ narrowing | — |
| 3 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.91 | -5.35% | 3.2y | high | 3d | 0.48% | 59.3 | → stable | — |
| 4 | NICFC | NIC Asia Flexi Cap Fund | 10.09 | 9.51 | -5.75% | 3.2y | medium | 3d | 0.70% | 47.7 | ↓ widening | — |

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
| LUK | -16.38% | liquidity:low; maturity:4.4y |
| SBCF | -15.34% | maturity:5.0y |
| LVF2 | -13.50% | liquidity:low; maturity:7.5y |
| SFEF | -12.34% | liquidity:low; maturity:5.9y |
| GIBF1 | -7.47% | maturity:6.4y |
| KSY | -7.32% | liquidity:low; maturity:8.0y |
| MNMF1 | -6.94% | maturity:8.8y |
| NSIF2 | -6.71% | maturity:6.5y |
| NMBHF2 | -6.46% | maturity:9.0y |
| NBF3 | -6.30% | maturity:5.5y |
| RMF2 | -6.16% | maturity:7.2y |
| RSY | -6.13% | maturity:9.1y |
| MBLEF | -5.85% | maturity:11.0y |
| KDBY | -5.76% | maturity:6.4y |
| NIBLSTF | -5.63% | maturity:9.9y |
| GSY | -5.50% | maturity:8.8y |
| SFMF | -5.22% | liquidity:low |
| C30MF | -5.19% | maturity:7.2y |
| SAGF | -4.84% | maturity:7.7y |
| KEF | -4.76% | maturity:5.0y |
| NIBSF2 | -4.48% | maturity:5.2y |
| SIGS3 | -4.45% | liquidity:low; maturity:7.1y |
| NICGF2 | -4.43% | maturity:4.7y |
| PRSF | -4.38% | maturity:6.0y |
| NICBF | -4.29% | liquidity:low |
| H8020 | -4.13% | maturity:7.5y |
| NIBLGF | -3.68% | valuation:small_discount; maturity:6.8y |
| SLCF | -3.45% | valuation:small_discount |
| HLICF | -3.24% | valuation:small_discount; liquidity:low; maturity:9.5y |
| CMF2 | -2.53% | valuation:small_discount |
| RMF1 | -2.29% | valuation:small_discount |
| GBIMESY2 | -2.12% | valuation:small_discount; maturity:9.3y |
| MMF1 | -0.52% | valuation:small_discount; maturity:5.5y |
| NICSF | -0.31% | valuation:small_discount |
| SEF | -0.20% | valuation:small_discount |
| NMB50 | -0.10% | valuation:small_discount; liquidity:low |
| RBBF40 | -0.10% | valuation:small_discount; liquidity:low; maturity:11.7y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 9
- NAV data age: median 29 days, max 291 days

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
