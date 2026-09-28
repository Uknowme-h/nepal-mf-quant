# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-28 18:11*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-28 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 35 |
| Median Discount | -12.28% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 31 | 79.5% |
| -10% to -6% | 6 | 15.4% |
| -6% to -4% | 0 | 0.0% |
| -4% to 0% | 2 | 5.1% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.09 | 10.89 | -16.81% | 1.7y | high | 77d | 0.38% | 74.5 | ↓ widening | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.92 | -13.40% | 2.7y | medium | 5d | 0.88% | 69.6 | ↑ narrowing | — |
| 3 | LUK | Laxmi Unnati Kosh | 11.66 | 9.30 | -20.24% | 3.9y | medium | 1d | -1.17% | 69.0 | → stable | — |
| 4 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.10 | -19.47% | 3.1y | medium | 1d | -2.04% | 67.8 | ↓ widening | — |
| 5 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.25 | -11.65% | 2.7y | medium | 4d | 0.48% | 56.0 | → stable | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.31 | 9.10 | -11.74% | 1.8y | high | 2d | -1.63% | 49.9 | ↓ widening | high_vol |
| 7 | SEF | Siddhartha Equity Fund | 10.36 | 9.60 | -7.34% | 1.1y | high | 25d | -2.72% | 45.1 | ↓ widening | — |
| 8 | NICSF | NIC Asia Select-30 | 9.48 | 8.30 | -12.45% | 1.8y | medium | 4d | -3.27% | 44.1 | ↓ widening | high_vol |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 2 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -22.05% | liquidity:low; maturity:4.5y |
| SFEF | -22.05% | maturity:5.4y |
| LVF2 | -20.25% | liquidity:low; maturity:6.9y |
| RSY | -17.83% | maturity:8.6y |
| KDBY | -15.81% | maturity:5.8y |
| GIBF1 | -15.11% | maturity:5.8y |
| KEF | -14.78% | maturity:4.5y |
| PRSF | -14.57% | maturity:5.5y |
| MBLEF | -14.46% | maturity:10.5y |
| NICGF2 | -14.33% | liquidity:low; maturity:4.2y |
| NMBHF2 | -13.82% | maturity:8.4y |
| NSIF2 | -13.60% | maturity:5.9y |
| NICBF | -12.40% | liquidity:low |
| SIGS2 | -12.33% | liquidity:low |
| H8020 | -12.28% | maturity:7.0y |
| NIBLSTF | -11.75% | maturity:9.4y |
| NIBSF2 | -11.27% | maturity:4.7y |
| NBF3 | -11.24% | maturity:5.0y |
| SIGS3 | -11.17% | maturity:6.6y |
| MNMF1 | -11.12% | maturity:8.2y |
| RBBF40 | -11.02% | maturity:11.1y |
| SAGF | -10.96% | maturity:7.2y |
| SLCF | -10.95% | liquidity:low |
| NIBLGF | -10.45% | maturity:6.3y |
| RMF2 | -9.72% | maturity:6.7y |
| GSY | -9.64% | maturity:8.3y |
| GBIMESY2 | -9.16% | liquidity:low; maturity:8.8y |
| C30MF | -8.02% | liquidity:low; maturity:6.6y |
| MMF1 | -7.01% | maturity:5.0y |
| KSY | -3.93% | valuation:small_discount; liquidity:low; maturity:7.5y |
| HLICF | -3.11% | valuation:small_discount; liquidity:low; maturity:9.0y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 24
- NAV data age: median 44 days, max 487 days

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
