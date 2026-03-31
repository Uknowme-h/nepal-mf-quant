# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-31 11:12*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-31 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 37 |
| At Premium (price ≥ NAV) | 4 |
| Deep Discount (≤ -8%) | 8 |
| Median Discount | -4.39% |
| CONSIDER | 4 |
| IGNORE | 37 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 4 | 9.8% |
| -10% to -6% | 7 | 17.1% |
| -6% to -4% | 14 | 34.1% |
| -4% to 0% | 12 | 29.3% |
| ≥ 0% (premium) | 4 | 9.8% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 12.75 | 12.20 | -4.31% | 2.2y | medium | 2d | 5.81% | 68.0 | ↑ narrowing | — |
| 2 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.00 | -4.49% | 3.2y | high | 1d | 0.48% | 64.9 | → stable | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.09 | 9.60 | -4.86% | 3.2y | medium | 1d | 0.70% | 57.3 | ↓ widening | — |
| 4 | SIGS2 | Siddhartha Investment Gro | 10.44 | 9.96 | -4.60% | 3.4y | medium | 1d | 0.29% | 53.2 | ↓ widening | — |

## IGNORE Summary

*37 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 16 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -15.44% | liquidity:low; maturity:4.4y |
| SBCF | -15.17% | maturity:5.0y |
| LVF2 | -13.58% | liquidity:low; maturity:7.4y |
| SFEF | -10.50% | maturity:5.9y |
| SFMF | -9.73% | liquidity:low |
| KSY | -9.30% | liquidity:low; maturity:8.0y |
| NSIF2 | -9.02% | maturity:6.4y |
| PRSF | -8.09% | maturity:6.0y |
| NMBHF2 | -7.81% | maturity:8.9y |
| SAGF | -6.93% | maturity:7.7y |
| MBLEF | -6.22% | maturity:11.0y |
| GIBF1 | -5.35% | maturity:6.3y |
| RMF2 | -5.32% | maturity:7.2y |
| RSY | -5.29% | maturity:9.1y |
| NIBSF2 | -4.79% | liquidity:low; maturity:5.2y |
| NIBLSTF | -4.71% | maturity:9.9y |
| NICBF | -4.49% | liquidity:low |
| NIBLGF | -4.39% | maturity:6.8y |
| NICGF2 | -4.33% | maturity:4.6y |
| C30MF | -4.06% | maturity:7.1y |
| H8020 | -4.04% | maturity:7.5y |
| GBIMESY2 | -3.63% | valuation:small_discount; maturity:9.3y |
| RBBF40 | -3.54% | valuation:small_discount; liquidity:low; maturity:11.6y |
| GSY | -3.47% | valuation:small_discount; maturity:8.8y |
| NMB50 | -3.31% | valuation:small_discount; liquidity:low |
| NBF3 | -3.20% | valuation:small_discount; maturity:5.5y |
| MNMF1 | -2.70% | valuation:small_discount; maturity:8.7y |
| SIGS3 | -2.69% | valuation:small_discount; liquidity:low; maturity:7.1y |
| RMF1 | -2.09% | valuation:small_discount |
| KDBY | -1.56% | valuation:small_discount; maturity:6.3y |
| SLCF | -1.48% | valuation:small_discount |
| NICSF | -1.26% | valuation:small_discount |
| KEF | -0.89% | valuation:small_discount; maturity:5.0y |
| HLICF | 1.15% | valuation:premium; liquidity:low; maturity:9.5y |
| SEF | 1.49% | valuation:premium |
| CMF2 | 1.85% | valuation:premium |
| MMF1 | 3.76% | valuation:premium; maturity:5.4y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 14
- NAV data age: median 44 days, max 306 days

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
