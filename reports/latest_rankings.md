# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-04 12:19*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-04 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 18 |
| Median Discount | -7.68% |
| CONSIDER | 7 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 13 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 10 | 25.0% |
| -10% to -6% | 15 | 37.5% |
| -6% to -4% | 8 | 20.0% |
| -4% to 0% | 5 | 12.5% |
| ≥ 0% (premium) | 2 | 5.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.25 | -9.29% | 3.2y | medium | 3d | -2.04% | 64.1 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 13.69 | 11.74 | -14.24% | 1.9y | medium | 44d | -4.60% | 60.1 | ↓ widening | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.28 | 9.61 | -6.52% | 2.0y | high | 13d | -1.63% | 55.6 | ↑ narrowing | high_vol |
| 4 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.99 | -4.58% | 2.8y | medium | 1d | 0.48% | 48.9 | ↓ widening | — |
| 5 | NICSF | NIC Asia Select-30 | 9.55 | 8.80 | -7.85% | 1.9y | medium | 8d | -2.55% | 48.1 | ↑ narrowing | — |
| 6 | SEF | Siddhartha Equity Fund | 10.36 | 9.90 | -4.44% | 1.3y | medium | 6d | -2.72% | 45.4 | ↑ narrowing | — |
| 7 | SLCF | Sanima Large Cap Fund | 10.08 | 9.60 | -4.76% | 1.6y | medium | 2d | -2.70% | 39.8 | ↓ widening | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 7 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -14.64% | maturity:4.6y |
| SFEF | -13.82% | maturity:5.5y |
| PRSF | -12.94% | maturity:5.6y |
| NICBF | -12.60% | liquidity:low |
| LVF2 | -12.36% | maturity:7.1y |
| NICGF2 | -12.31% | maturity:4.3y |
| NICFC | -11.46% | liquidity:low |
| NIBSF2 | -11.08% | maturity:4.8y |
| RMF2 | -10.50% | liquidity:low; maturity:6.8y |
| LUK | -9.95% | maturity:4.0y |
| RBBF40 | -9.85% | maturity:11.3y |
| KDBY | -9.30% | maturity:6.0y |
| GIBF1 | -8.57% | liquidity:low; maturity:6.0y |
| KEF | -8.57% | maturity:4.6y |
| GBIMESY2 | -8.16% | liquidity:low; maturity:9.0y |
| NSIF2 | -8.15% | maturity:6.1y |
| NMBHF2 | -7.92% | liquidity:low; maturity:8.6y |
| SIGS3 | -7.52% | liquidity:low; maturity:6.7y |
| MNMF1 | -7.05% | maturity:8.4y |
| NIBLSTF | -6.77% | maturity:9.5y |
| RSY | -6.00% | maturity:8.8y |
| MBLEF | -5.53% | maturity:10.7y |
| NBF3 | -5.52% | maturity:5.1y |
| KSY | -5.25% | liquidity:low; maturity:7.6y |
| MMF1 | -5.06% | maturity:5.1y |
| C30MF | -4.18% | maturity:6.8y |
| GSY | -3.71% | valuation:small_discount; maturity:8.4y |
| H8020 | -1.05% | valuation:small_discount; maturity:7.2y |
| HLICF | -0.80% | valuation:small_discount; maturity:9.1y |
| NIBLGF | -0.41% | valuation:small_discount; liquidity:low; maturity:6.5y |
| SIGS2 | -0.37% | valuation:small_discount; liquidity:low |
| SAGF | 0.28% | valuation:premium; maturity:7.3y |
| NMB50 | 1.44% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 45
- Symbols with issues: 27
- NAV data age: median 1 days, max 432 days

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
