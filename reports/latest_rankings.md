# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-12 13:42*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-12 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 19 |
| Median Discount | -7.81% |
| CONSIDER | 6 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 10 | 24.4% |
| -10% to -6% | 15 | 36.6% |
| -6% to -4% | 7 | 17.1% |
| -4% to 0% | 6 | 14.6% |
| ≥ 0% (premium) | 3 | 7.3% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | RMF1 | RBB Mutual Fund 1 | 10.41 | 9.80 | -5.86% | 2.1y | high | 9d | -2.16% | 61.1 | ↑ narrowing | high_vol |
| 2 | SEF | Siddhartha Equity Fund | 10.65 | 10.18 | -4.41% | 1.4y | high | 23d | -2.74% | 60.9 | ↑ narrowing | — |
| 3 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.81 | -4.34% | 3.4y | medium | 3d | -2.04% | 60.4 | ↑ narrowing | — |
| 4 | PSF | Prabhu Select Fund | 13.69 | 12.25 | -10.52% | 2.0y | high | 8d | -4.60% | 58.4 | ↓ widening | — |
| 5 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.26 | -10.88% | 3.0y | medium | 4d | -1.24% | 57.9 | ↓ widening | — |
| 6 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.94 | -5.06% | 3.0y | medium | 2d | 0.48% | 44.0 | ↓ widening | — |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 9 |
| valuation | 9 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -14.24% | maturity:4.2y |
| LVF2 | -13.94% | liquidity:low; maturity:7.2y |
| PRSF | -13.54% | maturity:5.8y |
| SBCF | -12.79% | maturity:4.8y |
| KDBY | -12.28% | maturity:6.1y |
| SFEF | -11.81% | maturity:5.7y |
| NICBF | -11.37% | liquidity:low |
| NICGF2 | -10.60% | maturity:4.4y |
| NSIF2 | -9.70% | maturity:6.2y |
| KEF | -9.66% | maturity:4.8y |
| RMF2 | -9.43% | liquidity:low; maturity:7.0y |
| RSY | -8.75% | maturity:8.9y |
| NIBSF2 | -8.51% | maturity:5.0y |
| NMBHF2 | -8.23% | maturity:8.7y |
| H8020 | -8.16% | maturity:7.3y |
| GIBF1 | -8.09% | maturity:6.1y |
| KSY | -8.06% | liquidity:low; maturity:7.8y |
| GBIMESY2 | -7.92% | maturity:9.1y |
| C30MF | -7.81% | maturity:6.9y |
| MBLEF | -7.36% | maturity:10.8y |
| NIBLGF | -7.24% | liquidity:low; maturity:6.6y |
| RBBF40 | -6.42% | liquidity:low; maturity:11.4y |
| SAGF | -6.22% | maturity:7.5y |
| SIGS3 | -5.38% | maturity:6.9y |
| MNMF1 | -5.21% | maturity:8.5y |
| GSY | -4.87% | maturity:8.6y |
| NIBLSTF | -3.49% | valuation:small_discount; maturity:9.7y |
| CMF2 | -3.23% | valuation:small_discount; liquidity:low |
| SLCF | -3.19% | valuation:small_discount |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.3y |
| NICSF | -2.69% | valuation:small_discount |
| MMF1 | -1.55% | valuation:small_discount; maturity:5.2y |
| SIGS2 | 1.51% | valuation:premium |
| HLICF | 1.69% | valuation:premium; liquidity:low; maturity:9.3y |
| NMB50 | 4.55% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 23
- NAV data age: median 28 days, max 379 days

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
