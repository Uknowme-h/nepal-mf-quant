# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-06 12:18*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-06 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 19 |
| Median Discount | -7.78% |
| CONSIDER | 7 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 13 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 22.5% |
| -10% to -6% | 18 | 45.0% |
| -6% to -4% | 8 | 20.0% |
| -4% to 0% | 3 | 7.5% |
| ≥ 0% (premium) | 2 | 5.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.20 | -9.73% | 3.2y | medium | 4d | -2.04% | 70.0 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.13 | -11.36% | 2.9y | medium | 1d | 0.88% | 68.4 | → stable | — |
| 3 | PSF | Prabhu Select Fund | 13.69 | 11.80 | -13.81% | 1.9y | medium | 45d | -4.60% | 59.9 | → stable | — |
| 4 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.90 | -5.44% | 2.8y | medium | 2d | 0.48% | 55.5 | → stable | — |
| 5 | SEF | Siddhartha Equity Fund | 10.36 | 9.81 | -5.31% | 1.3y | medium | 7d | -2.72% | 53.4 | ↑ narrowing | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.28 | 9.68 | -5.84% | 2.0y | medium | 14d | -1.63% | 44.1 | → stable | high_vol |
| 7 | SLCF | Sanima Large Cap Fund | 10.08 | 9.49 | -5.85% | 1.6y | medium | 3d | -2.70% | 37.5 | ↓ widening | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 5 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -18.49% | liquidity:low; maturity:7.1y |
| SBCF | -16.23% | maturity:4.6y |
| SFEF | -13.82% | liquidity:low; maturity:5.5y |
| PRSF | -13.14% | maturity:5.6y |
| NICBF | -11.82% | liquidity:low |
| NICGF2 | -11.73% | maturity:4.3y |
| NICSF | -10.37% | liquidity:low |
| KDBY | -9.38% | maturity:6.0y |
| RMF2 | -9.30% | liquidity:low; maturity:6.8y |
| RBBF40 | -9.15% | maturity:11.3y |
| NSIF2 | -8.40% | maturity:6.1y |
| NMBHF2 | -8.40% | maturity:8.6y |
| LUK | -8.23% | liquidity:low; maturity:4.0y |
| SIGS3 | -8.22% | liquidity:low; maturity:6.7y |
| KEF | -8.22% | maturity:4.6y |
| RSY | -8.15% | maturity:8.7y |
| NBF3 | -7.85% | maturity:5.1y |
| MMF1 | -7.70% | maturity:5.1y |
| NIBSF2 | -7.69% | maturity:4.8y |
| KSY | -7.68% | maturity:7.6y |
| GBIMESY2 | -7.35% | maturity:8.9y |
| NIBLSTF | -6.98% | maturity:9.5y |
| GIBF1 | -6.79% | maturity:6.0y |
| MNMF1 | -6.07% | maturity:8.4y |
| C30MF | -5.98% | liquidity:low; maturity:6.8y |
| MBLEF | -5.25% | maturity:10.7y |
| NIBLGF | -5.23% | maturity:6.5y |
| GSY | -4.52% | maturity:8.4y |
| HLICF | -2.63% | valuation:small_discount; maturity:9.1y |
| H8020 | -1.37% | valuation:small_discount; maturity:7.2y |
| SIGS2 | -0.46% | valuation:small_discount; liquidity:low |
| SAGF | 0.28% | valuation:premium; liquidity:low; maturity:7.3y |
| NMB50 | 1.44% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 45
- Symbols with issues: 32
- NAV data age: median 3 days, max 434 days

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
