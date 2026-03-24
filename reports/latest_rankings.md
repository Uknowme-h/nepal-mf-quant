# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-24 11:10*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-24 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 32 |
| At Premium (price ≥ NAV) | 9 |
| Deep Discount (≤ -8%) | 4 |
| Median Discount | -2.66% |
| CONSIDER | 2 |
| IGNORE | 39 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 3 | 7.3% |
| -10% to -6% | 2 | 4.9% |
| -6% to -4% | 4 | 9.8% |
| -4% to 0% | 23 | 56.1% |
| ≥ 0% (premium) | 9 | 22.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.05 | -4.01% | 3.2y | medium | 1d | 0.48% | 60.1 | ↑ narrowing | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.60 | -6.19% | 3.6y | medium | 2d | -2.04% | 53.5 | ↓ widening | — |

## IGNORE Summary

*39 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| valuation | 32 |
| maturity | 29 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -14.24% | liquidity:low; maturity:4.4y |
| LVF2 | -12.45% | liquidity:low; maturity:7.5y |
| SBCF | -10.41% | maturity:5.0y |
| SFEF | -8.14% | maturity:5.9y |
| NICGF2 | -4.83% | liquidity:low; maturity:4.7y |
| KSY | -4.30% | liquidity:low; maturity:8.0y |
| NSIF2 | -4.30% | maturity:6.5y |
| NICFC | -3.96% | valuation:small_discount; liquidity:low |
| GSY | -3.95% | valuation:small_discount; maturity:8.8y |
| KDBY | -3.84% | valuation:small_discount; maturity:6.3y |
| MNMF1 | -3.66% | valuation:small_discount; maturity:8.8y |
| NMBHF2 | -3.57% | valuation:small_discount; maturity:8.9y |
| RMF2 | -3.54% | valuation:small_discount; maturity:7.2y |
| C30MF | -3.40% | valuation:small_discount; maturity:7.2y |
| PRSF | -3.25% | valuation:small_discount; maturity:6.0y |
| GIBF1 | -3.23% | valuation:small_discount; maturity:6.3y |
| H8020 | -3.05% | valuation:small_discount; maturity:7.5y |
| RSY | -2.97% | valuation:small_discount; maturity:9.1y |
| SAGF | -2.66% | valuation:small_discount; liquidity:low; maturity:7.7y |
| MBLEF | -2.65% | valuation:small_discount; maturity:11.0y |
| SIGS3 | -1.76% | valuation:small_discount; liquidity:low; maturity:7.1y |
| NBF3 | -1.74% | valuation:small_discount; maturity:5.5y |
| SLCF | -1.38% | valuation:small_discount; liquidity:low |
| SIGS2 | -1.34% | valuation:small_discount |
| GBIMESY2 | -1.31% | valuation:small_discount; liquidity:low; maturity:9.3y |
| NIBLSTF | -0.72% | valuation:small_discount; maturity:9.9y |
| PSF | -0.66% | valuation:small_discount |
| KEF | -0.60% | valuation:small_discount; maturity:5.0y |
| RMF1 | -0.50% | valuation:small_discount |
| NIBSF2 | -0.20% | valuation:small_discount; maturity:5.2y |
| CMF2 | 0.29% | valuation:premium |
| RBBF40 | 1.01% | valuation:premium; maturity:11.7y |
| NIBLGF | 1.02% | valuation:premium; maturity:6.8y |
| HLICF | 1.67% | valuation:premium; maturity:9.5y |
| NMB50 | 1.74% | valuation:premium |
| SEF | 2.39% | valuation:premium |
| NICSF | 2.62% | valuation:premium |
| MMF1 | 3.13% | valuation:premium; maturity:5.5y |
| NICBF | 4.49% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 9
- NAV data age: median 37 days, max 299 days

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
