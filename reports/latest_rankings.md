# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-26 14:29*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-24 |
| Funds Tracked | 38 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 31 |
| Median Discount | -11.68% |
| CONSIDER | 7 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 26 | 68.4% |
| -10% to -6% | 9 | 23.7% |
| -6% to -4% | 1 | 2.6% |
| -4% to 0% | 2 | 5.3% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.09 | 10.86 | -17.04% | 1.7y | high | 76d | 0.38% | 74.9 | → stable | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.87 | -13.88% | 2.7y | medium | 4d | 0.88% | 55.4 | ↓ widening | — |
| 3 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.21 | -12.03% | 2.7y | medium | 3d | 0.48% | 55.0 | ↓ widening | — |
| 4 | SIGS2 | Siddhartha Investment Gro | 10.95 | 9.46 | -13.61% | 2.9y | medium | 1d | -3.30% | 50.7 | ↓ widening | — |
| 5 | SEF | Siddhartha Equity Fund | 10.36 | 9.70 | -6.37% | 1.1y | high | 24d | -2.72% | 49.0 | ↑ narrowing | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.31 | 9.39 | -8.92% | 1.8y | high | 1d | -1.63% | 45.8 | ↓ widening | high_vol |
| 7 | NICSF | NIC Asia Select-30 | 9.48 | 8.60 | -9.28% | 1.8y | medium | 3d | -3.27% | 45.1 | ↑ narrowing | — |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 27 |
| liquidity | 10 |
| valuation | 2 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -21.34% | maturity:4.5y |
| SFEF | -20.30% | maturity:5.4y |
| LVF2 | -20.25% | liquidity:low; maturity:7.0y |
| LUK | -18.70% | liquidity:low |
| SFMF | -18.14% | liquidity:low |
| RSY | -17.30% | liquidity:low; maturity:8.6y |
| KEF | -16.92% | maturity:4.5y |
| PRSF | -15.08% | maturity:5.5y |
| MBLEF | -15.00% | maturity:10.5y |
| NICBF | -14.73% | liquidity:low |
| NICGF2 | -14.42% | maturity:4.2y |
| NSIF2 | -14.03% | maturity:5.9y |
| NMBHF2 | -14.01% | maturity:8.4y |
| NBF3 | -12.79% | maturity:5.0y |
| NIBLGF | -11.87% | maturity:6.3y |
| H8020 | -11.48% | maturity:7.0y |
| NIBLSTF | -11.33% | maturity:9.4y |
| MNMF1 | -11.31% | maturity:8.2y |
| NIBSF2 | -11.27% | maturity:4.7y |
| RBBF40 | -11.12% | maturity:11.1y |
| SAGF | -11.06% | liquidity:low; maturity:7.2y |
| SIGS3 | -10.39% | maturity:6.6y |
| GBIMESY2 | -9.37% | liquidity:low; maturity:8.8y |
| SLCF | -9.27% | liquidity:low |
| C30MF | -8.02% | maturity:6.6y |
| KSY | -7.66% | liquidity:low; maturity:7.5y |
| GSY | -7.13% | liquidity:low; maturity:8.3y |
| MMF1 | -6.59% | maturity:5.0y |
| RMF2 | -5.68% | maturity:6.7y |
| GIBF1 | -0.68% | valuation:small_discount; maturity:5.8y |
| HLICF | -0.35% | valuation:small_discount; maturity:9.0y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 23
- NAV data age: median 42 days, max 485 days

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
