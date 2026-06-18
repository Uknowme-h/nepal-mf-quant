# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-18 13:42*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-18 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 15 |
| Median Discount | -6.62% |
| CONSIDER | 2 |
| IGNORE | 39 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 8 | 19.5% |
| -10% to -6% | 13 | 31.7% |
| -6% to -4% | 8 | 19.5% |
| -4% to 0% | 11 | 26.8% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.39 | -9.62% | 3.0y | medium | 8d | -1.24% | 65.5 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 13.69 | 12.14 | -11.32% | 2.0y | medium | 12d | -4.60% | 59.9 | → stable | — |

## IGNORE Summary

*39 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 12 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -14.24% | liquidity:low; maturity:4.2y |
| PRSF | -13.75% | maturity:5.7y |
| KDBY | -12.74% | maturity:6.1y |
| SBCF | -12.26% | maturity:4.8y |
| SFEF | -11.64% | liquidity:low; maturity:5.7y |
| GIBF1 | -11.51% | liquidity:low; maturity:6.1y |
| LVF2 | -11.13% | maturity:7.2y |
| RSY | -9.72% | maturity:8.9y |
| NICBF | -9.34% | liquidity:low |
| NICGF2 | -9.26% | maturity:4.4y |
| GBIMESY2 | -8.80% | maturity:9.1y |
| NSIF2 | -8.78% | maturity:6.2y |
| KEF | -8.41% | maturity:4.8y |
| NMBHF2 | -7.95% | maturity:8.7y |
| MBLEF | -7.81% | maturity:10.8y |
| NIBSF2 | -7.80% | maturity:5.0y |
| SIGS3 | -7.40% | maturity:6.9y |
| KSY | -6.74% | liquidity:low; maturity:7.8y |
| RMF2 | -6.62% | maturity:6.9y |
| RBBF40 | -5.93% | maturity:11.4y |
| GSY | -5.44% | maturity:8.6y |
| MNMF1 | -5.40% | maturity:8.5y |
| SFMF | -5.31% | liquidity:low |
| SAGF | -5.29% | liquidity:low; maturity:7.5y |
| C30MF | -4.83% | maturity:6.9y |
| NIBLGF | -4.43% | maturity:6.6y |
| NIBLSTF | -4.21% | maturity:9.7y |
| NICSF | -3.73% | valuation:small_discount |
| NBF3 | -3.59% | valuation:small_discount; maturity:5.3y |
| RMF1 | -3.46% | valuation:small_discount |
| NBF2 | -2.58% | valuation:small_discount; liquidity:low |
| H8020 | -2.45% | valuation:small_discount; liquidity:low; maturity:7.3y |
| SEF | -2.25% | valuation:small_discount |
| SIGS2 | -1.51% | valuation:small_discount; liquidity:low |
| CMF2 | -1.37% | valuation:small_discount |
| SLCF | -1.35% | valuation:small_discount |
| MMF1 | -1.24% | valuation:small_discount; maturity:5.2y |
| HLICF | -0.45% | valuation:small_discount; maturity:9.2y |
| NMB50 | 1.52% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 22
- NAV data age: median 34 days, max 385 days

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
