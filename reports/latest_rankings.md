# Nepal MF Quant — Full Analysis Report

*Generated: 2026-02-24 11:07*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-02-24 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 11 |
| Median Discount | -6.83% |
| CONSIDER | 7 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 4 | 9.8% |
| -10% to -6% | 21 | 51.2% |
| -6% to -4% | 9 | 22.0% |
| -4% to 0% | 5 | 12.2% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.27 | -9.12% | 3.7y | high | 2d | -2.04% | 73.1 | → stable | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.02 | 9.20 | -8.18% | 3.3y | medium | 9d | 3.51% | 70.3 | → stable | — |
| 3 | PSF | Prabhu Select Fund | 12.03 | 11.01 | -8.48% | 2.3y | medium | 4d | 3.35% | 62.9 | ↓ widening | — |
| 4 | NBF2 | Nabil Balanced Fund - 2 | 10.42 | 9.61 | -7.77% | 3.3y | medium | 1d | 2.26% | 56.9 | ↓ widening | — |
| 5 | NICSF | NIC Asia Select-30 | 9.54 | 9.10 | -4.61% | 2.4y | high | 2d | — | 56.5 | ↑ narrowing | — |
| 6 | SLCF | Sanima Large Cap Fund | 10.12 | 9.51 | -6.03% | 2.0y | medium | 1d | — | 45.4 | ↓ widening | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.02 | 9.45 | -5.69% | 2.4y | medium | 1d | — | 42.0 | ↓ widening | high_vol |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 7 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -16.74% | maturity:7.5y |
| SFEF | -16.54% | liquidity:low; maturity:6.0y |
| LUK | -16.38% | maturity:4.5y |
| SBCF | -14.02% | maturity:5.1y |
| RMF2 | -9.80% | liquidity:low; maturity:7.2y |
| NSIF2 | -9.29% | maturity:6.5y |
| GIBF1 | -8.73% | liquidity:low; maturity:6.4y |
| NICGF2 | -8.68% | maturity:4.7y |
| NBF3 | -7.84% | maturity:5.6y |
| KEF | -7.74% | maturity:5.1y |
| NIBSF2 | -7.67% | maturity:5.3y |
| KDBY | -7.67% | maturity:6.4y |
| PRSF | -7.57% | maturity:6.0y |
| C30MF | -7.35% | liquidity:low; maturity:7.2y |
| RSY | -7.04% | maturity:9.2y |
| SIGS2 | -6.92% | liquidity:low |
| GSY | -6.83% | maturity:8.9y |
| MBLEF | -6.74% | maturity:11.1y |
| GBIMESY2 | -6.62% | maturity:9.4y |
| NMBHF2 | -6.17% | maturity:9.0y |
| SIGS3 | -5.57% | maturity:7.2y |
| SAGF | -5.53% | maturity:7.8y |
| KSY | -5.46% | maturity:8.1y |
| MNMF1 | -5.18% | maturity:8.8y |
| NIBLSTF | -5.13% | maturity:10.0y |
| HLICF | -5.08% | maturity:9.6y |
| NICBF | -4.38% | liquidity:low |
| SEF | -3.99% | valuation:small_discount |
| RBBF40 | -3.71% | valuation:small_discount; liquidity:low; maturity:11.7y |
| H8020 | -3.36% | valuation:small_discount; liquidity:low; maturity:7.6y |
| NIBLGF | -3.17% | valuation:small_discount; liquidity:low; maturity:6.9y |
| CMF2 | -1.79% | valuation:small_discount; liquidity:low |
| MMF1 | 0.73% | valuation:premium; maturity:5.5y |
| NMB50 | 4.55% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 41
- Symbols with issues: 23
- NAV data age: median 40 days, max 271 days

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
