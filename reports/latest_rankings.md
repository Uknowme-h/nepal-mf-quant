# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-13 11:12*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-13 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 16 |
| Median Discount | -7.01% |
| CONSIDER | 5 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 8 | 20.0% |
| -10% to -6% | 19 | 47.5% |
| -6% to -4% | 7 | 17.5% |
| -4% to 0% | 6 | 15.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.07 | -11.94% | 2.8y | medium | 6d | 0.88% | 71.6 | ↓ widening | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.20 | -9.73% | 3.2y | medium | 3d | -2.04% | 71.1 | → stable | — |
| 3 | PSF | Prabhu Select Fund | 13.04 | 12.00 | -7.98% | 1.9y | medium | 50d | -4.26% | 61.6 | ↑ narrowing | — |
| 4 | NICSF | NIC Asia Select-30 | 9.55 | 8.89 | -6.91% | 1.9y | medium | 2d | -2.55% | 57.9 | ↑ narrowing | — |
| 5 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.88 | -5.64% | 2.8y | medium | 1d | 0.48% | 55.7 | → stable | — |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 9 |
| valuation | 6 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -20.16% | liquidity:low; maturity:7.1y |
| SBCF | -17.20% | maturity:4.6y |
| LUK | -16.55% | maturity:4.0y |
| SFEF | -14.17% | maturity:5.5y |
| NICGF2 | -13.56% | maturity:4.3y |
| NICBF | -10.85% | liquidity:low |
| KDBY | -10.28% | maturity:6.0y |
| NIBLGF | -9.73% | maturity:6.4y |
| KSY | -9.62% | liquidity:low; maturity:7.6y |
| NIBLSTF | -9.42% | liquidity:low; maturity:9.5y |
| GBIMESY2 | -9.37% | maturity:8.9y |
| NIBSF2 | -9.23% | maturity:4.8y |
| PRSF | -8.62% | maturity:5.6y |
| GIBF1 | -8.32% | maturity:6.0y |
| RBBF40 | -7.64% | maturity:11.3y |
| MNMF1 | -7.05% | maturity:8.4y |
| SAGF | -7.02% | maturity:7.3y |
| RMF2 | -7.00% | maturity:6.8y |
| NMBHF2 | -6.97% | maturity:8.6y |
| SIGS3 | -6.91% | maturity:6.7y |
| RMF1 | -6.91% | liquidity:low |
| NSIF2 | -6.60% | maturity:6.1y |
| GSY | -6.12% | maturity:8.4y |
| RSY | -5.91% | maturity:8.7y |
| NBF3 | -5.81% | maturity:5.1y |
| MMF1 | -5.06% | maturity:5.1y |
| C30MF | -5.03% | liquidity:low; maturity:6.8y |
| H8020 | -4.61% | maturity:7.1y |
| KEF | -4.11% | maturity:4.6y |
| HLICF | -3.67% | valuation:small_discount; maturity:9.1y |
| MBLEF | -3.13% | valuation:small_discount; maturity:10.6y |
| SEF | -2.99% | valuation:small_discount; liquidity:low |
| SIGS2 | -1.38% | valuation:small_discount; liquidity:low |
| SLCF | -0.79% | valuation:small_discount |
| NMB50 | -0.38% | valuation:small_discount; liquidity:low |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 31
- NAV data age: median 10 days, max 441 days

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
