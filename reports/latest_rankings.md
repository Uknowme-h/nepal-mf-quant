# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-25 11:07*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-25 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 33 |
| At Premium (price ≥ NAV) | 8 |
| Deep Discount (≤ -8%) | 4 |
| Median Discount | -2.99% |
| CONSIDER | 1 |
| IGNORE | 40 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 3 | 7.3% |
| -10% to -6% | 2 | 4.9% |
| -6% to -4% | 7 | 17.1% |
| -4% to 0% | 21 | 51.2% |
| ≥ 0% (premium) | 8 | 19.5% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.05 | -4.01% | 3.2y | medium | 2d | 0.48% | 59.9 | ↑ narrowing | — |

## IGNORE Summary

*40 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 29 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -14.24% | liquidity:low; maturity:4.4y |
| LVF2 | -12.80% | maturity:7.5y |
| SBCF | -10.49% | maturity:5.0y |
| SFEF | -9.36% | liquidity:low; maturity:5.9y |
| SFMF | -7.96% | liquidity:low |
| NSIF2 | -5.59% | maturity:6.4y |
| MBLEF | -4.94% | liquidity:low; maturity:11.0y |
| C30MF | -4.53% | liquidity:low; maturity:7.1y |
| NMBHF2 | -4.34% | maturity:8.9y |
| GIBF1 | -4.24% | maturity:6.3y |
| RSY | -4.09% | maturity:9.1y |
| NICFC | -3.87% | valuation:small_discount; liquidity:low |
| GSY | -3.76% | valuation:small_discount; maturity:8.8y |
| KDBY | -3.75% | valuation:small_discount; maturity:6.3y |
| MNMF1 | -3.66% | valuation:small_discount; maturity:8.7y |
| SAGF | -3.51% | valuation:small_discount; liquidity:low; maturity:7.7y |
| NICGF2 | -3.45% | valuation:small_discount; maturity:4.7y |
| KSY | -3.32% | valuation:small_discount; liquidity:low; maturity:8.0y |
| SIGS2 | -3.26% | valuation:small_discount |
| RMF2 | -2.99% | valuation:small_discount; maturity:7.2y |
| NBF3 | -2.62% | valuation:small_discount; maturity:5.5y |
| RBBF40 | -2.53% | valuation:small_discount; liquidity:low; maturity:11.6y |
| SLCF | -2.46% | valuation:small_discount |
| PRSF | -2.11% | valuation:small_discount; maturity:6.0y |
| PSF | -1.58% | valuation:small_discount |
| KEF | -1.29% | valuation:small_discount; maturity:5.0y |
| H8020 | -0.99% | valuation:small_discount; maturity:7.5y |
| SIGS3 | -0.83% | valuation:small_discount; maturity:7.1y |
| GBIMESY2 | -0.81% | valuation:small_discount; maturity:9.3y |
| RMF1 | -0.30% | valuation:small_discount |
| NIBSF2 | -0.20% | valuation:small_discount; maturity:5.2y |
| NICSF | -0.10% | valuation:small_discount |
| CMF2 | 0.68% | valuation:premium |
| SEF | 0.70% | valuation:premium |
| NIBLSTF | 1.02% | valuation:premium; maturity:9.9y |
| NIBLGF | 2.15% | valuation:premium; maturity:6.8y |
| HLICF | 2.41% | valuation:premium; maturity:9.5y |
| MMF1 | 2.61% | valuation:premium; maturity:5.5y |
| NMB50 | 3.20% | valuation:premium |
| NICBF | 4.19% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 8
- NAV data age: median 38 days, max 300 days

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
