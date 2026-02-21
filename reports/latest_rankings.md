# Nepal MF Quant — Full Analysis Report

*Generated: 2026-02-21 10:46*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-02-17 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 11 |
| Median Discount | -6.46% |
| CONSIDER | 5 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 4 | 9.8% |
| -10% to -6% | 17 | 41.5% |
| -6% to -4% | 12 | 29.3% |
| -4% to 0% | 7 | 17.1% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.02 | 9.20 | -8.18% | 3.3y | medium | 6d | 3.51% | 66.3 | → stable | — |
| 2 | PSF | Prabhu Select Fund | 12.03 | 11.20 | -6.90% | 2.3y | medium | 1d | 3.35% | 64.3 | ↑ narrowing | — |
| 3 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.26 | -9.20% | 3.7y | medium | 3d | -2.04% | 60.8 | ↓ widening | — |
| 4 | NBF2 | Nabil Balanced Fund - 2 | 10.42 | 9.62 | -7.68% | 3.3y | medium | 6d | 2.26% | 55.5 | ↓ widening | — |
| 5 | NICSF | NIC Asia Select-30 | 9.54 | 9.12 | -4.40% | 2.4y | medium | 5d | — | 52.3 | ↑ narrowing | — |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 8 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -17.11% | maturity:5.1y |
| LUK | -16.81% | maturity:4.5y |
| LVF2 | -16.39% | maturity:7.5y |
| SFEF | -15.49% | maturity:6.0y |
| PRSF | -8.95% | maturity:6.1y |
| NSIF2 | -8.86% | liquidity:low; maturity:6.5y |
| C30MF | -8.60% | liquidity:low; maturity:7.2y |
| GIBF1 | -8.39% | liquidity:low; maturity:6.5y |
| NMBHF2 | -8.30% | maturity:9.0y |
| MBLEF | -7.57% | maturity:11.1y |
| MNMF1 | -7.53% | maturity:8.8y |
| NBF3 | -7.35% | maturity:5.6y |
| KDBY | -7.21% | maturity:6.4y |
| RMF2 | -7.10% | liquidity:low; maturity:7.3y |
| SIGS2 | -6.92% | liquidity:low |
| NICGF2 | -6.61% | maturity:4.8y |
| NIBLSTF | -6.46% | maturity:10.0y |
| SAGF | -5.82% | liquidity:low; maturity:7.8y |
| MMF1 | -5.76% | maturity:5.6y |
| KSY | -5.65% | maturity:8.1y |
| SLCF | -5.34% | liquidity:low |
| NIBSF2 | -5.32% | maturity:5.3y |
| GBIMESY2 | -5.30% | liquidity:low; maturity:9.4y |
| RSY | -5.26% | maturity:9.2y |
| SIGS3 | -5.20% | maturity:7.2y |
| KEF | -5.16% | maturity:5.1y |
| RBBF40 | -4.51% | maturity:11.7y |
| H8020 | -4.12% | maturity:7.6y |
| GSY | -3.96% | valuation:small_discount; maturity:8.9y |
| NICBF | -3.88% | valuation:small_discount |
| SEF | -2.89% | valuation:small_discount |
| NIBLGF | -2.76% | valuation:small_discount; maturity:6.9y |
| RMF1 | -2.50% | valuation:small_discount |
| NMB50 | -1.36% | valuation:small_discount; liquidity:low |
| HLICF | -0.31% | valuation:small_discount; maturity:9.6y |
| CMF2 | 1.59% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 41
- Symbols with issues: 14
- NAV data age: median 37 days, max 268 days

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
