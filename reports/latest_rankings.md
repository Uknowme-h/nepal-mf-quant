# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-06 12:06*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-06 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 27 |
| Median Discount | -9.92% |
| CONSIDER | 9 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 20 | 48.8% |
| -10% to -6% | 14 | 34.1% |
| -6% to -4% | 6 | 14.6% |
| -4% to 0% | 1 | 2.4% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 14.35 | 12.28 | -14.43% | 2.1y | medium | 3d | 12.55% | 74.4 | ↑ narrowing | — |
| 2 | SIGS2 | Siddhartha Investment Gro | 11.53 | 10.35 | -10.23% | 3.3y | medium | 1d | 5.01% | 60.1 | ↓ widening | — |
| 3 | SEF | Siddhartha Equity Fund | 10.95 | 10.00 | -8.68% | 1.5y | medium | 2d | 3.79% | 60.1 | ↑ narrowing | high_vol |
| 4 | SLCF | Sanima Large Cap Fund | 10.65 | 9.88 | -7.23% | 1.8y | medium | 19d | 0.47% | 54.8 | ↑ narrowing | — |
| 5 | NICSF | NIC Asia Select-30 | 9.89 | 9.45 | -4.45% | 2.2y | high | 4d | -1.49% | 51.3 | ↑ narrowing | — |
| 6 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.88 | -5.64% | 3.1y | medium | 2d | 0.48% | 49.0 | ↓ widening | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.64 | 9.88 | -7.14% | 2.2y | medium | 11d | 0.76% | 47.2 | → stable | high_vol |
| 8 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.40 | -7.96% | 3.5y | high | 1d | -2.04% | 44.6 | ↓ widening | — |
| 9 | CMF2 | Citizens Mutual Fund - 2 | 10.52 | 9.80 | -6.84% | 0.2y | medium | 1d | -0.94% | 42.9 | ↓ widening | — |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 1 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -18.61% | maturity:5.9y |
| KEF | -17.45% | maturity:4.9y |
| KDBY | -16.96% | maturity:6.2y |
| LVF2 | -14.90% | liquidity:low; maturity:7.3y |
| GIBF1 | -14.49% | maturity:6.2y |
| LUK | -14.24% | maturity:4.3y |
| SBCF | -14.02% | liquidity:low; maturity:4.9y |
| SFEF | -13.82% | maturity:5.8y |
| NMBHF2 | -12.36% | maturity:8.8y |
| H8020 | -12.10% | maturity:7.4y |
| KSY | -11.63% | liquidity:low; maturity:7.9y |
| RSY | -11.62% | maturity:9.0y |
| SIGS3 | -11.24% | maturity:7.0y |
| GSY | -10.93% | maturity:8.7y |
| MBLEF | -10.93% | liquidity:low; maturity:10.9y |
| NICBF | -10.89% | liquidity:low |
| NICFC | -10.65% | liquidity:low |
| MNMF1 | -10.57% | maturity:8.6y |
| C30MF | -9.92% | liquidity:low; maturity:7.0y |
| RMF2 | -9.41% | liquidity:low; maturity:7.0y |
| GBIMESY2 | -9.18% | liquidity:low; maturity:9.2y |
| NSIF2 | -9.17% | maturity:6.3y |
| SAGF | -9.01% | maturity:7.6y |
| NICGF2 | -8.34% | maturity:4.5y |
| NIBSF2 | -7.92% | maturity:5.1y |
| NIBLSTF | -6.67% | maturity:9.8y |
| NIBLGF | -6.22% | maturity:6.7y |
| RBBF40 | -4.87% | maturity:11.5y |
| NBF3 | -4.84% | maturity:5.4y |
| MMF1 | -4.71% | maturity:5.3y |
| NMB50 | -4.18% | liquidity:low |
| HLICF | -1.29% | valuation:small_discount; maturity:9.4y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 24
- NAV data age: median 21 days, max 342 days

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
