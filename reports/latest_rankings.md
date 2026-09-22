# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-22 14:51*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-22 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 32 |
| Median Discount | -12.28% |
| CONSIDER | 9 |
| IGNORE | 30 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 28 | 71.8% |
| -10% to -6% | 7 | 17.9% |
| -6% to -4% | 3 | 7.7% |
| -4% to 0% | 1 | 2.6% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | LUK | Laxmi Unnati Kosh | 11.66 | 9.77 | -16.21% | 3.9y | medium | 3d | -1.17% | 76.7 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 13.09 | 10.92 | -16.58% | 1.8y | high | 74d | 0.38% | 75.0 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.93 | -13.30% | 2.7y | medium | 2d | 0.88% | 71.9 | ↑ narrowing | — |
| 4 | SEF | Siddhartha Equity Fund | 10.36 | 9.74 | -5.98% | 1.1y | high | 22d | -2.72% | 51.5 | ↑ narrowing | — |
| 5 | SIGS2 | Siddhartha Investment Gro | 10.95 | 9.46 | -13.61% | 2.9y | medium | 1d | -3.30% | 49.6 | ↓ widening | — |
| 6 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.60 | -8.31% | 2.7y | medium | 1d | 0.48% | 46.1 | → stable | — |
| 7 | NICSF | NIC Asia Select-30 | 9.48 | 8.40 | -11.39% | 1.8y | medium | 1d | -3.27% | 40.4 | ↓ widening | — |
| 8 | SLCF | Sanima Large Cap Fund | 10.14 | 9.20 | -9.27% | 1.4y | medium | 2d | -2.12% | 40.3 | → stable | — |
| 9 | RMF1 | RBB Mutual Fund 1 | 10.31 | 9.30 | -9.80% | 1.8y | medium | 16d | -1.63% | 39.6 | ↓ widening | high_vol |

## IGNORE Summary

*30 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 1 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -21.26% | maturity:5.4y |
| LVF2 | -20.25% | liquidity:low; maturity:7.0y |
| SFMF | -18.41% | liquidity:low |
| RSY | -17.92% | maturity:8.6y |
| SBCF | -17.11% | liquidity:low; maturity:4.5y |
| NICGF2 | -15.87% | liquidity:low; maturity:4.2y |
| KDBY | -15.22% | maturity:5.8y |
| MBLEF | -15.19% | liquidity:low; maturity:10.5y |
| PRSF | -14.57% | maturity:5.5y |
| KEF | -14.51% | maturity:4.5y |
| NICBF | -13.76% | liquidity:low |
| NIBSF2 | -13.50% | maturity:4.7y |
| NMBHF2 | -13.15% | maturity:8.4y |
| NSIF2 | -13.09% | maturity:6.0y |
| NIBLSTF | -12.59% | maturity:9.4y |
| H8020 | -12.28% | maturity:7.0y |
| KSY | -11.82% | liquidity:low; maturity:7.5y |
| NIBLGF | -11.66% | maturity:6.3y |
| MNMF1 | -11.60% | maturity:8.2y |
| SIGS3 | -11.17% | liquidity:low; maturity:6.6y |
| SAGF | -11.15% | maturity:7.2y |
| RBBF40 | -11.02% | liquidity:low; maturity:11.2y |
| GBIMESY2 | -10.07% | liquidity:low; maturity:8.8y |
| GSY | -9.94% | maturity:8.3y |
| NBF3 | -7.85% | maturity:5.0y |
| RMF2 | -6.69% | maturity:6.7y |
| MMF1 | -6.59% | maturity:5.0y |
| C30MF | -5.47% | maturity:6.7y |
| HLICF | -5.18% | maturity:9.0y |
| GIBF1 | -1.53% | valuation:small_discount; maturity:5.8y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 22
- NAV data age: median 38 days, max 481 days

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
