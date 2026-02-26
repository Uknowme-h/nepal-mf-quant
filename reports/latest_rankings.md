# Nepal MF Quant — Full Analysis Report

*Generated: 2026-02-26 11:07*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-02-26 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 15 |
| Median Discount | -6.92% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 4 | 9.8% |
| -10% to -6% | 20 | 48.8% |
| -6% to -4% | 12 | 29.3% |
| -4% to 0% | 4 | 9.8% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.02 | 9.46 | -5.59% | 3.3y | high | 11d | 3.51% | 70.9 | ↑ narrowing | — |
| 2 | SIGS2 | Siddhartha Investment Gro | 10.41 | 9.69 | -6.92% | 3.5y | high | 2d | — | 64.4 | → stable | — |
| 3 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.26 | -9.20% | 3.7y | medium | 1d | -2.04% | 63.1 | → stable | — |
| 4 | NBF2 | Nabil Balanced Fund - 2 | 10.42 | 9.65 | -7.39% | 3.3y | high | 3d | 2.26% | 63.1 | → stable | — |
| 5 | PSF | Prabhu Select Fund | 12.03 | 11.02 | -8.40% | 2.3y | medium | 6d | 3.35% | 58.2 | ↓ widening | — |
| 6 | SLCF | Sanima Large Cap Fund | 10.12 | 9.66 | -4.55% | 2.0y | medium | 3d | — | 54.4 | ↑ narrowing | — |
| 7 | NICSF | NIC Asia Select-30 | 9.54 | 9.02 | -5.45% | 2.4y | medium | 4d | — | 44.3 | ↓ widening | — |
| 8 | SEF | Siddhartha Equity Fund | 10.02 | 9.57 | -4.49% | 1.7y | medium | 2d | — | 42.1 | ↓ widening | — |

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
| SBCF | -17.55% | liquidity:low; maturity:5.1y |
| LUK | -15.95% | maturity:4.5y |
| LVF2 | -14.99% | maturity:7.5y |
| SFEF | -14.35% | maturity:6.0y |
| NMBHF2 | -9.26% | maturity:9.0y |
| KSY | -9.16% | liquidity:low; maturity:8.1y |
| GIBF1 | -9.08% | liquidity:low; maturity:6.4y |
| NICGF2 | -9.07% | maturity:4.7y |
| KDBY | -8.77% | maturity:6.4y |
| NSIF2 | -8.68% | maturity:6.5y |
| RMF2 | -8.40% | maturity:7.2y |
| PRSF | -8.06% | liquidity:low; maturity:6.0y |
| C30MF | -8.02% | maturity:7.2y |
| KEF | -7.74% | maturity:5.1y |
| NIBSF2 | -7.57% | maturity:5.2y |
| MBLEF | -7.29% | maturity:11.1y |
| NIBLSTF | -7.18% | maturity:9.9y |
| NBF3 | -6.76% | maturity:5.6y |
| NIBLGF | -6.24% | liquidity:low; maturity:6.9y |
| RSY | -6.10% | maturity:9.2y |
| GSY | -5.84% | maturity:8.8y |
| HLICF | -5.81% | liquidity:low; maturity:9.6y |
| MNMF1 | -5.67% | maturity:8.8y |
| SAGF | -5.53% | maturity:7.8y |
| RBBF40 | -5.12% | maturity:11.7y |
| GBIMESY2 | -5.09% | maturity:9.4y |
| SIGS3 | -4.36% | maturity:7.2y |
| NICBF | -4.28% | liquidity:low |
| RMF1 | -3.99% | valuation:small_discount |
| H8020 | -3.19% | valuation:small_discount; liquidity:low; maturity:7.6y |
| MMF1 | -0.21% | valuation:small_discount; maturity:5.5y |
| NMB50 | -0.19% | valuation:small_discount; liquidity:low |
| CMF2 | 1.99% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 41
- Symbols with issues: 17
- NAV data age: median 42 days, max 273 days

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
