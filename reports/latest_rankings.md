# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-16 14:57*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-16 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 32 |
| Median Discount | -12.49% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 28 | 71.8% |
| -10% to -6% | 8 | 20.5% |
| -6% to -4% | 1 | 2.6% |
| -4% to 0% | 2 | 5.1% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.09 | 10.91 | -16.65% | 1.8y | medium | 71d | 0.38% | 62.2 | ↓ widening | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.96 | -13.01% | 2.8y | medium | 1d | 0.88% | 57.4 | ↓ widening | — |
| 3 | NICSF | NIC Asia Select-30 | 9.48 | 8.50 | -10.34% | 1.8y | medium | 1d | -3.27% | 54.0 | ↑ narrowing | — |
| 4 | SLCF | Sanima Large Cap Fund | 10.14 | 9.48 | -6.51% | 1.4y | medium | 3d | -2.12% | 53.3 | ↑ narrowing | — |
| 5 | SIGS2 | Siddhartha Investment Gro | 10.95 | 9.60 | -12.33% | 3.0y | medium | 3d | -3.30% | 50.4 | ↓ widening | — |
| 6 | SEF | Siddhartha Equity Fund | 10.36 | 9.57 | -7.63% | 1.1y | high | 19d | -2.72% | 46.1 | → stable | — |
| 7 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.55 | -8.79% | 2.7y | medium | 4d | 0.48% | 43.8 | ↓ widening | — |
| 8 | RMF1 | RBB Mutual Fund 1 | 10.31 | 9.46 | -8.24% | 1.9y | medium | 13d | -1.63% | 41.1 | ↓ widening | high_vol |

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
| SBCF | -20.37% | maturity:4.5y |
| LUK | -19.90% | liquidity:low |
| SFEF | -19.51% | maturity:5.4y |
| NMBHF2 | -18.71% | maturity:8.4y |
| SFMF | -18.58% | liquidity:low |
| LVF2 | -18.23% | maturity:7.0y |
| NICGF2 | -17.88% | maturity:4.2y |
| RSY | -17.12% | maturity:8.6y |
| KDBY | -15.56% | maturity:5.9y |
| KEF | -15.41% | maturity:4.5y |
| MBLEF | -15.37% | maturity:10.5y |
| PRSF | -15.15% | maturity:5.5y |
| NSIF2 | -14.46% | liquidity:low; maturity:6.0y |
| KSY | -14.34% | liquidity:low; maturity:7.5y |
| NIBLGF | -14.00% | maturity:6.3y |
| NICBF | -13.66% | liquidity:low |
| NIBLSTF | -12.91% | maturity:9.4y |
| NIBSF2 | -12.49% | maturity:4.7y |
| MNMF1 | -11.98% | maturity:8.3y |
| SAGF | -11.15% | maturity:7.2y |
| GBIMESY2 | -10.78% | liquidity:low; maturity:8.8y |
| RMF2 | -10.54% | liquidity:low; maturity:6.7y |
| RBBF40 | -10.43% | maturity:11.2y |
| SIGS3 | -10.30% | liquidity:low; maturity:6.6y |
| NBF3 | -8.82% | maturity:5.0y |
| GSY | -8.13% | maturity:8.3y |
| MMF1 | -6.17% | maturity:5.0y |
| C30MF | -6.04% | liquidity:low; maturity:6.7y |
| HLICF | -4.95% | liquidity:low; maturity:9.0y |
| GIBF1 | -2.38% | valuation:small_discount; maturity:5.9y |
| H8020 | -1.12% | valuation:small_discount; maturity:7.0y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 27
- NAV data age: median 32 days, max 475 days

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
