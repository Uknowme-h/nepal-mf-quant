# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-30 11:20*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-30 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 7 |
| Median Discount | -3.81% |
| CONSIDER | 2 |
| IGNORE | 38 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 3 | 7.5% |
| -10% to -6% | 8 | 20.0% |
| -6% to -4% | 8 | 20.0% |
| -4% to 0% | 19 | 47.5% |
| ≥ 0% (premium) | 2 | 5.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 12.75 | 11.85 | -7.06% | 2.2y | medium | 1d | 5.81% | 67.5 | ↓ widening | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.35 | -8.41% | 3.6y | medium | 3d | -2.04% | 65.5 | → stable | — |

## IGNORE Summary

*38 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 21 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -15.61% | maturity:5.0y |
| LUK | -14.24% | maturity:4.4y |
| LVF2 | -13.67% | liquidity:low; maturity:7.4y |
| SFEF | -9.62% | maturity:5.9y |
| KSY | -9.30% | liquidity:low; maturity:8.0y |
| NSIF2 | -9.18% | maturity:6.4y |
| PRSF | -7.78% | liquidity:low; maturity:6.0y |
| NMBHF2 | -7.72% | maturity:8.9y |
| SAGF | -6.48% | maturity:7.7y |
| NICFC | -5.65% | liquidity:low |
| MBLEF | -5.58% | maturity:11.0y |
| GIBF1 | -5.35% | maturity:6.3y |
| RMF2 | -4.76% | maturity:7.2y |
| C30MF | -4.72% | maturity:7.1y |
| RSY | -4.64% | liquidity:low; maturity:9.1y |
| MNMF1 | -4.05% | maturity:8.7y |
| NBF2 | -4.01% | liquidity:low |
| KDBY | -3.93% | valuation:small_discount; maturity:6.3y |
| NIBLSTF | -3.68% | valuation:small_discount; maturity:9.9y |
| NBF3 | -3.59% | valuation:small_discount; maturity:5.5y |
| GSY | -3.57% | valuation:small_discount; maturity:8.8y |
| RMF1 | -3.49% | valuation:small_discount |
| NICGF2 | -3.45% | valuation:small_discount; maturity:4.7y |
| SIGS2 | -3.26% | valuation:small_discount |
| NIBSF2 | -3.16% | valuation:small_discount; maturity:5.2y |
| H8020 | -2.64% | valuation:small_discount; maturity:7.5y |
| RBBF40 | -2.53% | valuation:small_discount; liquidity:low; maturity:11.6y |
| SIGS3 | -2.22% | valuation:small_discount; liquidity:low; maturity:7.1y |
| NMB50 | -2.12% | valuation:small_discount; liquidity:low |
| SLCF | -1.97% | valuation:small_discount |
| NICSF | -1.57% | valuation:small_discount |
| KEF | -1.29% | valuation:small_discount; maturity:5.0y |
| HLICF | -1.26% | valuation:small_discount; liquidity:low; maturity:9.5y |
| GBIMESY2 | -1.11% | valuation:small_discount; maturity:9.3y |
| SEF | -0.70% | valuation:small_discount |
| NIBLGF | -0.41% | valuation:small_discount; maturity:6.8y |
| CMF2 | 0.19% | valuation:premium |
| MMF1 | 2.30% | valuation:premium; maturity:5.5y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 16
- NAV data age: median 43 days, max 305 days

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
