# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-20 12:40*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-20 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 24 |
| Median Discount | -8.85% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 16 | 39.0% |
| -10% to -6% | 16 | 39.0% |
| -6% to -4% | 6 | 14.6% |
| -4% to 0% | 3 | 7.3% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 14.35 | 12.10 | -15.68% | 2.1y | high | 4d | 12.55% | 82.4 | ↑ narrowing | — |
| 2 | SIGS2 | Siddhartha Investment Gro | 11.53 | 10.51 | -8.85% | 3.3y | medium | 3d | 5.01% | 69.3 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.35 | -11.12% | 3.1y | medium | 3d | 4.26% | 60.0 | → stable | — |
| 4 | SEF | Siddhartha Equity Fund | 10.95 | 10.00 | -8.68% | 1.5y | high | 8d | 3.79% | 58.5 | → stable | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.64 | 9.94 | -6.58% | 2.2y | medium | 21d | 0.76% | 54.5 | ↑ narrowing | high_vol |
| 6 | NICSF | NIC Asia Select-30 | 9.89 | 9.36 | -5.36% | 2.1y | medium | 6d | -1.49% | 47.7 | ↑ narrowing | — |
| 7 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.20 | -9.73% | 3.5y | medium | 3d | -2.04% | 46.2 | ↓ widening | — |
| 8 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.00 | -4.49% | 3.0y | medium | 2d | 0.48% | 40.5 | → stable | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -17.35% | maturity:5.8y |
| KEF | -16.36% | maturity:4.8y |
| KDBY | -15.72% | maturity:6.2y |
| LVF2 | -14.72% | liquidity:low; maturity:7.3y |
| LUK | -14.24% | maturity:4.2y |
| SBCF | -13.93% | maturity:4.8y |
| GIBF1 | -12.79% | maturity:6.2y |
| RSY | -12.23% | maturity:9.0y |
| SIGS3 | -11.64% | maturity:7.0y |
| NICGF2 | -11.43% | maturity:4.5y |
| SFEF | -11.20% | maturity:5.7y |
| NSIF2 | -10.74% | maturity:6.3y |
| C30MF | -10.56% | liquidity:low; maturity:7.0y |
| MBLEF | -10.05% | liquidity:low; maturity:10.9y |
| MNMF1 | -9.75% | maturity:8.6y |
| KSY | -9.69% | maturity:7.8y |
| GSY | -9.09% | maturity:8.6y |
| NMBHF2 | -8.61% | maturity:8.8y |
| GBIMESY2 | -8.22% | liquidity:low; maturity:9.2y |
| NICBF | -7.83% | liquidity:low |
| H8020 | -7.49% | maturity:7.4y |
| NIBLGF | -7.40% | liquidity:low; maturity:6.7y |
| NIBLSTF | -7.07% | liquidity:low; maturity:9.7y |
| RMF2 | -6.75% | maturity:7.0y |
| MMF1 | -6.61% | maturity:5.3y |
| SLCF | -6.57% | liquidity:low |
| RBBF40 | -5.55% | liquidity:low; maturity:11.5y |
| NIBSF2 | -5.45% | maturity:5.0y |
| SAGF | -5.37% | maturity:7.5y |
| CMF2 | -5.32% | liquidity:low |
| NBF3 | -3.59% | valuation:small_discount; maturity:5.3y |
| HLICF | -3.00% | valuation:small_discount; maturity:9.3y |
| NMB50 | -2.04% | valuation:small_discount |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 20
- NAV data age: median 35 days, max 356 days

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
