# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-28 12:00*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-26 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 23 |
| Median Discount | -8.81% |
| CONSIDER | 3 |
| IGNORE | 38 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 14 | 34.1% |
| -10% to -6% | 12 | 29.3% |
| -6% to -4% | 4 | 9.8% |
| -4% to 0% | 10 | 24.4% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 11.75 | -14.17% | 2.0y | medium | 18d | -4.60% | 60.0 | ↓ widening | — |
| 2 | SIGS2 | Siddhartha Investment Gro | 11.23 | 10.25 | -8.73% | 3.2y | medium | 5d | -2.60% | 48.7 | ↓ widening | — |
| 3 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.67 | -5.58% | 3.4y | medium | 1d | -2.04% | 47.4 | ↓ widening | — |

## IGNORE Summary

*38 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 11 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -15.77% | maturity:5.7y |
| KDBY | -14.92% | maturity:6.1y |
| LVF2 | -14.11% | liquidity:low; maturity:7.2y |
| SBCF | -12.70% | maturity:4.8y |
| SFEF | -12.51% | maturity:5.6y |
| NICGF2 | -12.42% | maturity:4.4y |
| GIBF1 | -12.18% | liquidity:low; maturity:6.1y |
| LUK | -12.09% | maturity:4.1y |
| NICFC | -10.88% | liquidity:low |
| KEF | -10.82% | maturity:4.7y |
| NSIF2 | -10.56% | maturity:6.2y |
| RSY | -10.51% | maturity:8.8y |
| NICBF | -10.40% | liquidity:low |
| GBIMESY2 | -9.58% | liquidity:low; maturity:9.1y |
| MBLEF | -9.36% | maturity:10.8y |
| RBBF40 | -9.29% | maturity:11.4y |
| H8020 | -8.95% | maturity:7.3y |
| NMBHF2 | -8.90% | maturity:8.7y |
| SIGS3 | -8.83% | maturity:6.8y |
| NIBSF2 | -8.81% | maturity:4.9y |
| KSY | -8.70% | maturity:7.7y |
| C30MF | -7.06% | liquidity:low; maturity:6.9y |
| SAGF | -7.06% | liquidity:low; maturity:7.4y |
| MNMF1 | -6.64% | maturity:8.5y |
| RMF2 | -5.62% | liquidity:low; maturity:6.9y |
| NIBLSTF | -4.52% | maturity:9.6y |
| GSY | -4.49% | maturity:8.5y |
| NMB50 | -3.77% | valuation:small_discount; liquidity:low |
| CMF2 | -3.62% | valuation:small_discount |
| RMF1 | -3.46% | valuation:small_discount |
| NBF2 | -3.06% | valuation:small_discount |
| SEF | -2.82% | valuation:small_discount |
| NBF3 | -2.81% | valuation:small_discount; maturity:5.2y |
| SLCF | -2.32% | valuation:small_discount |
| NICSF | -2.28% | valuation:small_discount |
| NIBLGF | -1.21% | valuation:small_discount; maturity:6.6y |
| MMF1 | -1.03% | valuation:small_discount; maturity:5.2y |
| HLICF | 0.68% | valuation:premium; liquidity:low; maturity:9.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 23
- NAV data age: median 44 days, max 395 days

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
