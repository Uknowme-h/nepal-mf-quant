# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-03 15:02*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-03 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 18 |
| Median Discount | -7.36% |
| CONSIDER | 4 |
| IGNORE | 37 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 7 | 17.1% |
| -10% to -6% | 18 | 43.9% |
| -6% to -4% | 7 | 17.1% |
| -4% to 0% | 7 | 17.1% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.50 | -8.57% | 3.0y | medium | 5d | -1.24% | 64.2 | → stable | — |
| 2 | PSF | Prabhu Select Fund | 13.69 | 12.20 | -10.88% | 2.0y | medium | 1d | -4.60% | 63.3 | ↓ widening | — |
| 3 | SEF | Siddhartha Equity Fund | 10.65 | 9.96 | -6.48% | 1.4y | medium | 16d | -2.74% | 47.0 | ↓ widening | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.41 | 9.80 | -5.86% | 2.1y | medium | 2d | -2.16% | 36.0 | ↓ widening | high_vol |

## IGNORE Summary

*37 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 9 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -14.24% | maturity:4.2y |
| SBCF | -13.58% | maturity:4.8y |
| SFEF | -12.07% | maturity:5.7y |
| PRSF | -11.79% | maturity:5.8y |
| KDBY | -10.72% | maturity:6.2y |
| NICGF2 | -10.22% | liquidity:low; maturity:4.5y |
| RSY | -9.81% | maturity:8.9y |
| LVF2 | -9.73% | maturity:7.3y |
| SFMF | -9.65% | liquidity:low |
| GIBF1 | -9.51% | maturity:6.2y |
| NSIF2 | -9.45% | liquidity:low; maturity:6.2y |
| NICBF | -9.15% | liquidity:low |
| KEF | -8.41% | maturity:4.8y |
| RBBF40 | -8.20% | maturity:11.4y |
| RMF2 | -8.07% | liquidity:low; maturity:7.0y |
| NMBHF2 | -8.04% | maturity:8.7y |
| KSY | -7.78% | liquidity:low; maturity:7.8y |
| NIBLGF | -7.44% | maturity:6.6y |
| MBLEF | -7.36% | maturity:10.8y |
| GBIMESY2 | -7.14% | maturity:9.1y |
| NIBLSTF | -6.57% | maturity:9.7y |
| H8020 | -6.02% | maturity:7.3y |
| NIBSF2 | -5.78% | maturity:5.0y |
| C30MF | -5.67% | maturity:7.0y |
| SAGF | -5.29% | liquidity:low; maturity:7.5y |
| MNMF1 | -5.21% | maturity:8.6y |
| SIGS3 | -5.13% | maturity:6.9y |
| GSY | -4.30% | maturity:8.6y |
| SIGS2 | -3.74% | valuation:small_discount; liquidity:low |
| NICSF | -3.52% | valuation:small_discount |
| SLCF | -3.29% | valuation:small_discount |
| CMF2 | -2.83% | valuation:small_discount; liquidity:low |
| NBF3 | -2.71% | valuation:small_discount; maturity:5.3y |
| MMF1 | -2.16% | valuation:small_discount; maturity:5.3y |
| NBF2 | -0.76% | valuation:small_discount |
| HLICF | 2.14% | valuation:premium; maturity:9.3y |
| NMB50 | 2.47% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 24
- NAV data age: median 19 days, max 370 days

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
