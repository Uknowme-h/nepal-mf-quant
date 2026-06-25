# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-25 12:35*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-25 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 22 |
| Median Discount | -8.34% |
| CONSIDER | 5 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 13 | 31.7% |
| -10% to -6% | 15 | 36.6% |
| -6% to -4% | 3 | 7.3% |
| -4% to 0% | 9 | 22.0% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.40 | -9.53% | 3.0y | high | 2d | -1.24% | 70.1 | → stable | — |
| 2 | PSF | Prabhu Select Fund | 13.69 | 11.75 | -14.17% | 2.0y | high | 17d | -4.60% | 63.2 | ↓ widening | — |
| 3 | SIGS2 | Siddhartha Investment Gro | 11.23 | 10.30 | -8.28% | 3.2y | medium | 4d | -2.60% | 50.4 | ↓ widening | — |
| 4 | SEF | Siddhartha Equity Fund | 10.65 | 10.16 | -4.60% | 1.4y | medium | 1d | -2.74% | 43.8 | ↓ widening | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.41 | 9.78 | -6.05% | 2.1y | medium | 1d | -2.16% | 37.4 | ↓ widening | high_vol |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| KDBY | -15.54% | maturity:6.1y |
| PRSF | -14.76% | maturity:5.7y |
| SBCF | -14.46% | liquidity:low; maturity:4.8y |
| LVF2 | -14.11% | maturity:7.2y |
| KEF | -13.41% | maturity:4.7y |
| SFEF | -12.42% | maturity:5.6y |
| NICGF2 | -11.46% | maturity:4.4y |
| GIBF1 | -11.18% | maturity:6.1y |
| NICBF | -11.18% | liquidity:low |
| NSIF2 | -10.38% | liquidity:low; maturity:6.2y |
| SIGS3 | -10.26% | maturity:6.8y |
| RSY | -10.25% | maturity:8.9y |
| GBIMESY2 | -9.78% | maturity:9.1y |
| MBLEF | -9.63% | maturity:10.8y |
| LUK | -9.61% | maturity:4.1y |
| NMBHF2 | -9.08% | maturity:8.7y |
| H8020 | -8.71% | maturity:7.3y |
| RBBF40 | -8.60% | maturity:11.4y |
| RMF2 | -8.34% | liquidity:low; maturity:6.9y |
| KSY | -7.50% | maturity:7.7y |
| MNMF1 | -7.30% | maturity:8.5y |
| C30MF | -7.06% | liquidity:low; maturity:6.9y |
| NIBSF2 | -6.59% | liquidity:low; maturity:4.9y |
| SAGF | -6.41% | liquidity:low; maturity:7.4y |
| GSY | -4.49% | maturity:8.5y |
| NIBLSTF | -4.41% | liquidity:low; maturity:9.6y |
| SLCF | -3.87% | valuation:small_discount |
| NICSF | -3.73% | valuation:small_discount |
| NBF2 | -3.53% | valuation:small_discount |
| NIBLGF | -3.42% | valuation:small_discount; maturity:6.6y |
| NMB50 | -3.32% | valuation:small_discount; liquidity:low |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.2y |
| CMF2 | -2.74% | valuation:small_discount; liquidity:low |
| SFMF | -2.65% | valuation:small_discount |
| MMF1 | -2.47% | valuation:small_discount; maturity:5.2y |
| HLICF | 1.58% | valuation:premium; maturity:9.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 28
- NAV data age: median 41 days, max 392 days

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
