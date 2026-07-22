# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-22 12:03*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-22 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 23 |
| Median Discount | -8.68% |
| CONSIDER | 5 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 17 | 42.5% |
| -10% to -6% | 13 | 32.5% |
| -6% to -4% | 3 | 7.5% |
| -4% to 0% | 7 | 17.5% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 12.00 | -12.34% | 1.9y | medium | 35d | -4.60% | 70.8 | ↑ narrowing | — |
| 2 | NICSF | NIC Asia Select-30 | 9.80 | 9.00 | -8.16% | 2.0y | medium | 13d | 1.45% | 56.0 | → stable | — |
| 3 | SEF | Siddhartha Equity Fund | 10.65 | 10.18 | -4.41% | 1.3y | medium | 14d | 0.00% | 54.6 | ↑ narrowing | — |
| 4 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.27 | -10.00% | 2.9y | medium | 4d | 0.88% | 48.8 | ↓ widening | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.67 | -7.46% | 2.0y | high | 4d | 0.38% | 47.6 | ↓ widening | high_vol |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 7 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -16.30% | liquidity:low; maturity:4.1y |
| SBCF | -14.90% | maturity:4.7y |
| PRSF | -14.56% | liquidity:low; maturity:5.7y |
| LVF2 | -14.55% | maturity:7.1y |
| KDBY | -13.37% | maturity:6.0y |
| SFEF | -12.51% | maturity:5.6y |
| NICGF2 | -12.40% | liquidity:low; maturity:4.3y |
| NIBLSTF | -12.24% | maturity:9.6y |
| GIBF1 | -11.86% | maturity:6.0y |
| NICBF | -11.82% | liquidity:low |
| SIGS3 | -11.76% | maturity:6.8y |
| NIBSF2 | -11.18% | maturity:4.8y |
| KEF | -11.05% | maturity:4.7y |
| NSIF2 | -10.73% | maturity:6.1y |
| SIGS2 | -10.52% | liquidity:low |
| RSY | -9.34% | maturity:8.8y |
| NMBHF2 | -9.09% | maturity:8.6y |
| SFMF | -8.85% | liquidity:low |
| RMF2 | -8.50% | liquidity:low; maturity:6.8y |
| GBIMESY2 | -8.02% | maturity:9.0y |
| RBBF40 | -7.98% | maturity:11.3y |
| KSY | -7.66% | maturity:7.7y |
| MBLEF | -7.44% | liquidity:low; maturity:10.7y |
| MNMF1 | -7.25% | maturity:8.4y |
| C30MF | -6.66% | maturity:6.8y |
| SAGF | -6.47% | maturity:7.4y |
| GSY | -5.62% | maturity:8.4y |
| NIBLGF | -4.81% | maturity:6.5y |
| NBF2 | -3.63% | valuation:small_discount |
| NBF3 | -3.00% | valuation:small_discount; maturity:5.2y |
| H8020 | -2.54% | valuation:small_discount; liquidity:low; maturity:7.2y |
| SLCF | -2.51% | valuation:small_discount |
| NMB50 | -1.60% | valuation:small_discount |
| MMF1 | -0.92% | valuation:small_discount; maturity:5.1y |
| HLICF | -0.11% | valuation:small_discount; liquidity:low; maturity:9.2y |

</details>

## Data Quality

- Symbols checked: 44
- Symbols with issues: 23
- NAV data age: median 37 days, max 419 days

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
