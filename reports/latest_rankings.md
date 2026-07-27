# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-27 13:21*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-27 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 24 |
| Median Discount | -8.48% |
| CONSIDER | 6 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 16 | 40.0% |
| -10% to -6% | 17 | 42.5% |
| -6% to -4% | 3 | 7.5% |
| -4% to 0% | 4 | 10.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.46 | -8.16% | 2.9y | high | 7d | 0.88% | 68.5 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 13.69 | 12.10 | -11.61% | 1.9y | high | 38d | -4.60% | 68.1 | ↑ narrowing | — |
| 3 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.05 | -11.06% | 3.3y | medium | 1d | -2.04% | 55.2 | ↓ widening | — |
| 4 | NICSF | NIC Asia Select-30 | 9.80 | 9.00 | -8.16% | 1.9y | medium | 2d | 1.45% | 46.1 | ↓ widening | — |
| 5 | SIGS2 | Siddhartha Investment Gro | 11.22 | 10.50 | -6.42% | 3.1y | medium | 2d | -0.09% | 45.6 | → stable | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.68 | -7.37% | 2.0y | medium | 7d | 0.38% | 43.5 | ↓ widening | high_vol |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -15.86% | liquidity:low; maturity:7.1y |
| LUK | -14.24% | maturity:4.0y |
| KDBY | -13.76% | maturity:6.0y |
| PRSF | -13.07% | maturity:5.6y |
| SBCF | -12.26% | maturity:4.7y |
| SIGS3 | -11.76% | liquidity:low; maturity:6.8y |
| SFEF | -11.11% | maturity:5.5y |
| NICGF2 | -10.87% | maturity:4.3y |
| NIBSF2 | -10.67% | maturity:4.8y |
| KEF | -10.63% | maturity:4.6y |
| GIBF1 | -10.61% | maturity:6.0y |
| C30MF | -10.27% | liquidity:low; maturity:6.8y |
| NIBLSTF | -10.20% | maturity:9.5y |
| RSY | -10.13% | maturity:8.8y |
| NICBF | -9.50% | liquidity:low |
| NSIF2 | -9.47% | maturity:6.1y |
| GBIMESY2 | -9.00% | maturity:9.0y |
| RMF2 | -8.50% | maturity:6.8y |
| RBBF40 | -8.47% | maturity:11.3y |
| MBLEF | -8.35% | maturity:10.7y |
| MNMF1 | -7.72% | maturity:8.4y |
| NIBLGF | -7.62% | maturity:6.5y |
| NMBHF2 | -7.48% | maturity:8.6y |
| SAGF | -7.02% | liquidity:low; maturity:7.3y |
| KSY | -7.00% | liquidity:low; maturity:7.7y |
| H8020 | -6.42% | liquidity:low; maturity:7.2y |
| SLCF | -6.37% | liquidity:low |
| GSY | -5.91% | maturity:8.4y |
| NBF3 | -4.07% | maturity:5.2y |
| HLICF | -4.02% | maturity:9.1y |
| MMF1 | -2.86% | valuation:small_discount; maturity:5.1y |
| NBF2 | -2.58% | valuation:small_discount |
| SEF | -2.35% | valuation:small_discount; liquidity:low |
| NMB50 | -1.70% | valuation:small_discount; liquidity:low |

</details>

## Data Quality

- Symbols checked: 44
- Symbols with issues: 30
- NAV data age: median 42 days, max 424 days

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
