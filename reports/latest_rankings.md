# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-23 11:10*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-23 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 32 |
| At Premium (price ≥ NAV) | 9 |
| Deep Discount (≤ -8%) | 5 |
| Median Discount | -2.76% |
| CONSIDER | 1 |
| IGNORE | 40 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 3 | 7.3% |
| -10% to -6% | 3 | 7.3% |
| -6% to -4% | 8 | 19.5% |
| -4% to 0% | 19 | 46.3% |
| ≥ 0% (premium) | 8 | 19.5% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.39 | -8.05% | 3.6y | medium | 1d | -2.04% | 53.2 | ↓ widening | — |

## IGNORE Summary

*40 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 27 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -14.24% | liquidity:low; maturity:4.4y |
| LVF2 | -12.36% | maturity:7.5y |
| SBCF | -11.82% | maturity:5.0y |
| SFEF | -9.80% | maturity:5.9y |
| NSIF2 | -6.10% | liquidity:low; maturity:6.5y |
| MBLEF | -5.85% | maturity:11.0y |
| KDBY | -5.76% | maturity:6.3y |
| MNMF1 | -5.11% | maturity:8.8y |
| KSY | -4.79% | liquidity:low; maturity:8.0y |
| GIBF1 | -4.58% | maturity:6.3y |
| RMF2 | -4.57% | liquidity:low; maturity:7.2y |
| NICFC | -4.56% | liquidity:low |
| NICGF2 | -4.33% | liquidity:low; maturity:4.7y |
| NBF2 | -3.92% | valuation:small_discount |
| C30MF | -3.77% | valuation:small_discount; maturity:7.2y |
| GSY | -3.57% | valuation:small_discount; maturity:8.8y |
| H8020 | -3.55% | valuation:small_discount; maturity:7.5y |
| GBIMESY2 | -3.23% | valuation:small_discount; liquidity:low; maturity:9.3y |
| RSY | -2.97% | valuation:small_discount; maturity:9.1y |
| PRSF | -2.76% | valuation:small_discount; maturity:6.0y |
| NBF3 | -2.62% | valuation:small_discount; maturity:5.5y |
| NMBHF2 | -2.60% | valuation:small_discount; maturity:8.9y |
| NIBLGF | -2.35% | valuation:small_discount; maturity:6.8y |
| NIBLSTF | -2.25% | valuation:small_discount; maturity:9.9y |
| RMF1 | -1.89% | valuation:small_discount |
| NIBSF2 | -1.73% | valuation:small_discount; maturity:5.2y |
| SAGF | -1.71% | valuation:small_discount; maturity:7.7y |
| SIGS3 | -1.02% | valuation:small_discount; maturity:7.1y |
| KEF | -0.79% | valuation:small_discount; maturity:5.0y |
| NICBF | -0.60% | valuation:small_discount |
| PSF | -0.33% | valuation:small_discount |
| SLCF | 0.00% | valuation:premium |
| RBBF40 | 0.51% | valuation:premium; maturity:11.7y |
| SEF | 1.59% | valuation:premium |
| SIGS2 | 1.63% | valuation:premium |
| CMF2 | 1.75% | valuation:premium; liquidity:low |
| NICSF | 1.78% | valuation:premium |
| HLICF | 3.66% | valuation:premium; liquidity:low; maturity:9.5y |
| NMB50 | 3.68% | valuation:premium; liquidity:low |
| MMF1 | 4.07% | valuation:premium; maturity:5.5y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 8
- NAV data age: median 36 days, max 298 days

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
