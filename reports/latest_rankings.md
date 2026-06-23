# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-23 12:48*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-23 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 15 |
| Median Discount | -7.21% |
| CONSIDER | 2 |
| IGNORE | 39 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 12 | 29.3% |
| -10% to -6% | 13 | 31.7% |
| -6% to -4% | 6 | 14.6% |
| -4% to 0% | 9 | 22.0% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 12.15 | -11.25% | 2.0y | medium | 15d | -4.60% | 60.4 | ↓ widening | — |
| 2 | SIGS2 | Siddhartha Investment Gro | 11.23 | 10.40 | -7.39% | 3.2y | medium | 2d | -2.60% | 49.6 | ↓ widening | — |

## IGNORE Summary

*39 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| KDBY | -15.46% | maturity:6.1y |
| LVF2 | -14.11% | maturity:7.2y |
| PRSF | -13.88% | maturity:5.7y |
| KEF | -13.57% | maturity:4.7y |
| SFEF | -12.51% | maturity:5.6y |
| NICBF | -11.75% | liquidity:low |
| NICFC | -11.16% | liquidity:low |
| NICGF2 | -11.08% | maturity:4.4y |
| SBCF | -11.02% | maturity:4.8y |
| NSIF2 | -10.89% | liquidity:low; maturity:6.2y |
| RSY | -10.34% | maturity:8.9y |
| GIBF1 | -9.51% | maturity:6.1y |
| RMF2 | -9.34% | liquidity:low; maturity:6.9y |
| RBBF40 | -8.99% | maturity:11.4y |
| GBIMESY2 | -7.92% | maturity:9.1y |
| MBLEF | -7.90% | maturity:10.8y |
| NMBHF2 | -7.76% | maturity:8.7y |
| LUK | -7.29% | maturity:4.2y |
| KSY | -7.21% | maturity:7.7y |
| MNMF1 | -6.82% | maturity:8.5y |
| SIGS3 | -6.64% | liquidity:low; maturity:6.9y |
| C30MF | -6.13% | maturity:6.9y |
| SAGF | -6.13% | maturity:7.4y |
| NIBLGF | -5.94% | liquidity:low; maturity:6.6y |
| GSY | -5.44% | maturity:8.5y |
| NBF2 | -5.44% | liquidity:low |
| NIBSF2 | -5.27% | maturity:4.9y |
| H8020 | -4.99% | liquidity:low; maturity:7.3y |
| NIBLSTF | -4.62% | maturity:9.6y |
| RMF1 | -3.75% | valuation:small_discount |
| CMF2 | -3.71% | valuation:small_discount; liquidity:low |
| SLCF | -3.19% | valuation:small_discount |
| NMB50 | -3.13% | valuation:small_discount |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.2y |
| NICSF | -2.90% | valuation:small_discount |
| SFMF | -2.65% | valuation:small_discount; liquidity:low |
| SEF | -2.44% | valuation:small_discount |
| MMF1 | -1.03% | valuation:small_discount; maturity:5.2y |
| HLICF | 0.23% | valuation:premium; maturity:9.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 21
- NAV data age: median 39 days, max 390 days

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
