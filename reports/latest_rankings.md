# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-09 11:03*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-09 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 11 |
| Median Discount | -7.05% |
| CONSIDER | 6 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 5 | 12.2% |
| -10% to -6% | 20 | 48.8% |
| -6% to -4% | 5 | 12.2% |
| -4% to 0% | 9 | 22.0% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.89 | -5.54% | 3.2y | high | 6d | 0.48% | 64.5 | ↑ narrowing | — |
| 2 | SIGS2 | Siddhartha Investment Gro | 10.44 | 9.50 | -9.00% | 3.5y | high | 1d | 0.29% | 61.3 | ↓ widening | — |
| 3 | PSF | Prabhu Select Fund | 12.05 | 11.20 | -7.05% | 2.3y | high | 9d | 0.17% | 58.0 | ↑ narrowing | — |
| 4 | SLCF | Sanima Large Cap Fund | 10.15 | 9.68 | -4.63% | 2.0y | high | 2d | 0.30% | 55.5 | ↑ narrowing | — |
| 5 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.06 | -10.97% | 3.7y | high | 1d | -2.04% | 55.4 | ↓ widening | — |
| 6 | NICBF | NIC ASIA Balanced Fund | 10.04 | 9.61 | -4.28% | 3.5y | high | 1d | 3.83% | 50.3 | → stable | — |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 11 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -16.81% | maturity:4.4y |
| SBCF | -15.17% | maturity:5.0y |
| LVF2 | -14.20% | maturity:7.5y |
| SFEF | -11.46% | maturity:5.9y |
| NMBHF2 | -8.97% | maturity:9.0y |
| KDBY | -8.87% | maturity:6.4y |
| NSIF2 | -8.68% | maturity:6.5y |
| NICGF2 | -8.58% | maturity:4.7y |
| GIBF1 | -8.15% | maturity:6.4y |
| PRSF | -7.63% | maturity:6.0y |
| MBLEF | -7.50% | maturity:11.1y |
| GSY | -7.43% | maturity:8.8y |
| C30MF | -7.36% | maturity:7.2y |
| MNMF1 | -7.32% | maturity:8.8y |
| NIBSF2 | -7.23% | maturity:5.2y |
| GBIMESY2 | -7.16% | maturity:9.4y |
| RSY | -7.15% | maturity:9.2y |
| KEF | -7.14% | maturity:5.0y |
| NBF3 | -6.98% | maturity:5.5y |
| RMF2 | -6.72% | maturity:7.2y |
| KSY | -6.45% | maturity:8.0y |
| SIGS3 | -6.21% | maturity:7.2y |
| SAGF | -5.53% | maturity:7.7y |
| RBBF40 | -4.55% | maturity:11.7y |
| NIBLSTF | -3.99% | valuation:small_discount; maturity:9.9y |
| HLICF | -3.97% | valuation:small_discount; maturity:9.5y |
| SEF | -3.48% | valuation:small_discount |
| RMF1 | -2.59% | valuation:small_discount |
| NICFC | -2.10% | valuation:small_discount |
| CMF2 | -1.75% | valuation:small_discount |
| MMF1 | -1.57% | valuation:small_discount; maturity:5.5y |
| H8020 | -1.40% | valuation:small_discount; maturity:7.6y |
| NICSF | -0.52% | valuation:small_discount |
| NIBLGF | 1.12% | valuation:premium; maturity:6.9y |
| NMB50 | 2.03% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 41
- NAV data age: median 22 days, max 284 days

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
