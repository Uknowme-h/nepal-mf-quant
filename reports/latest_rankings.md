# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-23 12:03*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-23 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 21 |
| Median Discount | -8.32% |
| CONSIDER | 4 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 16 | 40.0% |
| -10% to -6% | 12 | 30.0% |
| -6% to -4% | 5 | 12.5% |
| -4% to 0% | 7 | 17.5% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 12.00 | -12.34% | 1.9y | high | 36d | -4.60% | 71.1 | ↑ narrowing | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.50 | -7.08% | 3.3y | high | 1d | -2.04% | 66.0 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.10 | -11.65% | 2.9y | medium | 5d | 0.88% | 63.4 | → stable | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.90 | -5.26% | 2.0y | high | 5d | 0.38% | 48.9 | ↓ widening | high_vol |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 9 |
| valuation | 7 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -14.02% | maturity:7.1y |
| LUK | -13.72% | maturity:4.1y |
| KDBY | -13.37% | maturity:6.0y |
| GIBF1 | -13.03% | liquidity:low; maturity:6.0y |
| PRSF | -12.53% | maturity:5.7y |
| SFEF | -12.51% | maturity:5.6y |
| KEF | -12.13% | maturity:4.7y |
| NICBF | -11.82% | liquidity:low |
| SIGS3 | -10.92% | maturity:6.8y |
| NICGF2 | -10.77% | maturity:4.3y |
| NSIF2 | -10.56% | maturity:6.1y |
| SIGS2 | -10.52% | liquidity:low |
| NIBSF2 | -10.47% | maturity:4.8y |
| SBCF | -10.23% | maturity:4.7y |
| NIBLSTF | -9.69% | maturity:9.6y |
| RBBF40 | -9.46% | maturity:11.3y |
| RSY | -8.81% | maturity:8.8y |
| RMF2 | -8.50% | liquidity:low; maturity:6.8y |
| NMBHF2 | -8.14% | maturity:8.6y |
| KSY | -7.76% | maturity:7.7y |
| MBLEF | -7.44% | maturity:10.7y |
| NIBLGF | -7.31% | maturity:6.5y |
| MNMF1 | -7.06% | maturity:8.4y |
| GBIMESY2 | -7.05% | liquidity:low; maturity:9.0y |
| NICSF | -6.12% | liquidity:low |
| SAGF | -5.73% | maturity:7.3y |
| GSY | -5.62% | maturity:8.4y |
| C30MF | -5.46% | liquidity:low; maturity:6.8y |
| H8020 | -4.91% | maturity:7.2y |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.2y |
| MMF1 | -2.86% | valuation:small_discount; maturity:5.1y |
| SEF | -2.54% | valuation:small_discount |
| NMB50 | -1.60% | valuation:small_discount; liquidity:low |
| NBF2 | -1.53% | valuation:small_discount |
| SLCF | -1.16% | valuation:small_discount; liquidity:low |
| HLICF | -0.45% | valuation:small_discount; maturity:9.2y |

</details>

## Data Quality

- Symbols checked: 44
- Symbols with issues: 33
- NAV data age: median 38 days, max 420 days

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
