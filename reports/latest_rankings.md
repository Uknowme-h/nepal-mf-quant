# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-30 14:53*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-27 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 30 |
| Median Discount | -11.01% |
| CONSIDER | 6 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 23 | 59.0% |
| -10% to -6% | 12 | 30.8% |
| -6% to -4% | 3 | 7.7% |
| -4% to 0% | 1 | 2.6% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SEF | Siddhartha Equity Fund | 10.36 | 9.20 | -11.20% | 1.2y | high | 8d | -2.72% | 67.0 | ↓ widening | — |
| 2 | PSF | Prabhu Select Fund | 13.04 | 12.17 | -6.67% | 1.8y | high | 60d | -4.26% | 59.1 | ↑ narrowing | — |
| 3 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.72 | -7.16% | 2.8y | medium | 2d | 0.48% | 55.4 | ↓ widening | — |
| 4 | NICSF | NIC Asia Select-30 | 9.55 | 8.48 | -11.20% | 1.9y | medium | 12d | -2.55% | 50.3 | ↓ widening | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.28 | 9.30 | -9.53% | 1.9y | medium | 2d | -1.63% | 45.0 | ↓ widening | high_vol |
| 6 | SIGS2 | Siddhartha Investment Gro | 10.85 | 10.27 | -5.35% | 3.0y | medium | 1d | -3.30% | 44.1 | ↓ widening | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 9 |
| valuation | 1 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -21.12% | liquidity:low; maturity:7.0y |
| KDBY | -20.47% | maturity:5.9y |
| SBCF | -18.25% | maturity:4.6y |
| NMBHF2 | -17.94% | maturity:8.5y |
| LUK | -17.92% | liquidity:low |
| NICGF2 | -16.44% | maturity:4.2y |
| SFEF | -15.57% | maturity:5.5y |
| RSY | -15.41% | maturity:8.7y |
| KEF | -15.38% | maturity:4.6y |
| SFMF | -15.04% | liquidity:low |
| NSIF2 | -14.75% | maturity:6.0y |
| NICFC | -13.79% | liquidity:low |
| KSY | -13.57% | maturity:7.6y |
| NIBSF2 | -12.82% | liquidity:low; maturity:4.8y |
| NIBLGF | -12.50% | maturity:6.4y |
| NICBF | -12.40% | liquidity:low |
| MBLEF | -12.35% | maturity:10.6y |
| NIBLSTF | -11.01% | maturity:9.4y |
| GBIMESY2 | -10.47% | maturity:8.9y |
| GSY | -10.14% | maturity:8.4y |
| RMF2 | -10.13% | liquidity:low; maturity:6.7y |
| GIBF1 | -9.85% | maturity:5.9y |
| SLCF | -9.72% | liquidity:low |
| NBF3 | -9.50% | maturity:5.1y |
| PRSF | -9.12% | maturity:5.5y |
| MNMF1 | -9.00% | maturity:8.3y |
| MMF1 | -8.23% | maturity:5.0y |
| C30MF | -7.31% | liquidity:low; maturity:6.7y |
| RBBF40 | -7.04% | maturity:11.2y |
| SAGF | -6.55% | maturity:7.3y |
| HLICF | -5.15% | maturity:9.1y |
| H8020 | -5.09% | maturity:7.1y |
| SIGS3 | -3.93% | valuation:small_discount; maturity:6.7y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 26
- NAV data age: median 27 days, max 458 days

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
