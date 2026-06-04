# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-04 12:55*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-04 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 17 |
| Median Discount | -7.51% |
| CONSIDER | 4 |
| IGNORE | 37 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 8 | 19.5% |
| -10% to -6% | 17 | 41.5% |
| -6% to -4% | 8 | 19.5% |
| -4% to 0% | 5 | 12.2% |
| ≥ 0% (premium) | 3 | 7.3% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 12.30 | -10.15% | 2.0y | high | 2d | -4.60% | 67.6 | → stable | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.50 | -8.57% | 3.0y | medium | 6d | -1.24% | 61.2 | → stable | — |
| 3 | SEF | Siddhartha Equity Fund | 10.65 | 10.10 | -5.16% | 1.4y | medium | 17d | -2.74% | 42.9 | ↓ widening | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.41 | 9.80 | -5.86% | 2.1y | medium | 3d | -2.16% | 40.5 | ↓ widening | high_vol |

## IGNORE Summary

*37 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 8 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -13.14% | maturity:4.8y |
| LUK | -12.95% | liquidity:low; maturity:4.2y |
| PRSF | -12.40% | maturity:5.8y |
| LVF2 | -12.27% | liquidity:low; maturity:7.2y |
| KDBY | -11.42% | maturity:6.2y |
| SFEF | -10.85% | maturity:5.7y |
| NICGF2 | -10.51% | maturity:4.5y |
| SFMF | -9.65% | liquidity:low |
| GIBF1 | -9.59% | maturity:6.2y |
| RSY | -9.45% | maturity:8.9y |
| NSIF2 | -9.28% | maturity:6.2y |
| KEF | -9.16% | maturity:4.8y |
| NICBF | -8.48% | liquidity:low |
| NMBHF2 | -8.14% | maturity:8.7y |
| RMF2 | -8.07% | liquidity:low; maturity:7.0y |
| KSY | -7.97% | liquidity:low; maturity:7.8y |
| MBLEF | -7.81% | maturity:10.8y |
| GBIMESY2 | -7.62% | maturity:9.1y |
| RBBF40 | -7.51% | maturity:11.4y |
| SIGS3 | -7.40% | liquidity:low; maturity:6.9y |
| C30MF | -6.13% | liquidity:low; maturity:7.0y |
| SAGF | -6.13% | maturity:7.5y |
| SIGS2 | -6.06% | liquidity:low |
| NIBLSTF | -5.75% | maturity:9.7y |
| NIBSF2 | -5.57% | maturity:5.0y |
| NIBLGF | -5.43% | maturity:6.6y |
| MNMF1 | -5.31% | maturity:8.6y |
| H8020 | -4.20% | maturity:7.3y |
| GSY | -4.20% | maturity:8.6y |
| NICSF | -3.83% | valuation:small_discount |
| NBF3 | -2.91% | valuation:small_discount; maturity:5.3y |
| MMF1 | -2.89% | valuation:small_discount; maturity:5.3y |
| CMF2 | -2.25% | valuation:small_discount |
| SLCF | -1.84% | valuation:small_discount |
| NBF2 | 2.10% | valuation:premium; liquidity:low |
| HLICF | 3.61% | valuation:premium; maturity:9.3y |
| NMB50 | 4.93% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 21
- NAV data age: median 20 days, max 371 days

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
