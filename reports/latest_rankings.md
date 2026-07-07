# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-07 12:39*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-07 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 21 |
| Median Discount | -8.68% |
| CONSIDER | 7 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 16 | 39.0% |
| -10% to -6% | 11 | 26.8% |
| -6% to -4% | 6 | 14.6% |
| -4% to 0% | 6 | 14.6% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.35 | -10.01% | 2.9y | medium | 7d | -1.24% | 64.4 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 13.69 | 11.76 | -14.10% | 2.0y | medium | 25d | -4.60% | 63.9 | → stable | — |
| 3 | SIGS2 | Siddhartha Investment Gro | 11.22 | 10.60 | -5.53% | 3.1y | medium | 1d | -0.09% | 52.9 | ↑ narrowing | — |
| 4 | NICSF | NIC Asia Select-30 | 9.80 | 9.16 | -6.53% | 2.0y | medium | 3d | 1.45% | 47.8 | ↓ widening | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.81 | -6.12% | 2.0y | medium | 3d | 0.38% | 46.5 | → stable | high_vol |
| 6 | SEF | Siddhartha Equity Fund | 10.65 | 10.00 | -6.10% | 1.3y | medium | 4d | 0.00% | 46.3 | ↓ widening | — |
| 7 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.00 | -4.49% | 2.9y | medium | 1d | 0.48% | 46.0 | → stable | — |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 8 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| KDBY | -18.06% | maturity:6.0y |
| PRSF | -15.23% | maturity:5.7y |
| SBCF | -14.02% | maturity:4.7y |
| KEF | -13.81% | maturity:4.7y |
| KSY | -12.96% | maturity:7.7y |
| SFEF | -12.95% | liquidity:low; maturity:5.6y |
| NICGF2 | -12.61% | liquidity:low; maturity:4.4y |
| LVF2 | -12.36% | maturity:7.2y |
| NSIF2 | -11.65% | liquidity:low; maturity:6.2y |
| GBIMESY2 | -11.55% | maturity:9.0y |
| SIGS3 | -10.92% | liquidity:low; maturity:6.8y |
| LUK | -10.81% | maturity:4.1y |
| GIBF1 | -10.69% | liquidity:low; maturity:6.1y |
| RSY | -10.22% | maturity:8.8y |
| NICBF | -9.83% | liquidity:low |
| MBLEF | -9.71% | maturity:10.7y |
| NIBSF2 | -9.57% | maturity:4.9y |
| NMBHF2 | -9.38% | maturity:8.7y |
| RMF2 | -8.68% | liquidity:low; maturity:6.9y |
| NIBLSTF | -7.45% | maturity:9.6y |
| MNMF1 | -7.25% | maturity:8.5y |
| NIBLGF | -6.81% | maturity:6.5y |
| SAGF | -5.73% | maturity:7.4y |
| H8020 | -5.71% | maturity:7.2y |
| C30MF | -5.64% | maturity:6.9y |
| SFMF | -4.51% | liquidity:low |
| GSY | -3.72% | valuation:small_discount; maturity:8.5y |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.2y |
| CMF2 | -2.65% | valuation:small_discount; liquidity:low |
| SLCF | -2.51% | valuation:small_discount |
| MMF1 | -1.02% | valuation:small_discount; maturity:5.2y |
| HLICF | -0.67% | valuation:small_discount; liquidity:low; maturity:9.2y |
| NMB50 | 0.85% | valuation:premium |
| RBBF40 | 2.07% | valuation:premium; maturity:11.4y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 26
- NAV data age: median 22 days, max 404 days

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
