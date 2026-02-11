# Nepal MF Quant — Full Analysis Report

*Generated: 2026-02-11 15:58*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-02-11 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 13 |
| Median Discount | -7.10% |
| CONSIDER | 6 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 5 | 12.2% |
| -10% to -6% | 22 | 53.7% |
| -6% to -4% | 5 | 12.2% |
| -4% to 0% | 8 | 19.5% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.02 | 9.16 | -8.58% | 3.3y | medium | 3d | 3.51% | 69.3 | → stable | — |
| 2 | NICBF | NIC ASIA Balanced Fund | 10.04 | 9.19 | -8.47% | 3.5y | medium | 3d | 3.83% | 66.6 | ↓ widening | — |
| 3 | PSF | Prabhu Select Fund | 12.03 | 11.10 | -7.73% | 2.4y | medium | 2d | 3.35% | 65.2 | ↓ widening | — |
| 4 | NBF2 | Nabil Balanced Fund - 2 | 10.42 | 9.68 | -7.10% | 3.3y | medium | 3d | 2.26% | 58.9 | ↑ narrowing | — |
| 5 | SIGS2 | Siddhartha Investment Gro | 10.41 | 9.80 | -5.86% | 3.5y | medium | 1d | — | 56.8 | ↑ narrowing | — |
| 6 | NICSF | NIC Asia Select-30 | 9.54 | 8.82 | -7.55% | 2.4y | medium | 2d | — | 51.5 | ↓ widening | — |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 9 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -16.74% | maturity:7.6y |
| SBCF | -16.23% | maturity:5.1y |
| LUK | -15.18% | liquidity:low; maturity:4.5y |
| SFEF | -13.04% | maturity:6.0y |
| NICGF2 | -10.26% | maturity:4.8y |
| SFMF | -9.65% | liquidity:low |
| NMBHF2 | -9.27% | maturity:9.1y |
| SIGS3 | -8.91% | maturity:7.2y |
| KDBY | -8.68% | maturity:6.5y |
| PRSF | -8.38% | liquidity:low; maturity:6.1y |
| NSIF2 | -8.00% | maturity:6.6y |
| RSY | -7.98% | maturity:9.2y |
| KEF | -7.74% | liquidity:low; maturity:5.1y |
| GIBF1 | -7.62% | maturity:6.5y |
| MNMF1 | -7.62% | maturity:8.9y |
| RMF2 | -7.56% | maturity:7.3y |
| NIBLSTF | -6.77% | liquidity:low; maturity:10.0y |
| MBLEF | -6.74% | maturity:11.1y |
| KSY | -6.63% | liquidity:low; maturity:8.1y |
| MMF1 | -6.60% | maturity:5.6y |
| NIBSF2 | -6.44% | maturity:5.3y |
| C30MF | -6.21% | maturity:7.3y |
| GSY | -5.94% | maturity:8.9y |
| SAGF | -5.82% | maturity:7.8y |
| NBF3 | -4.22% | maturity:5.6y |
| SLCF | -4.05% | liquidity:low |
| RMF1 | -3.69% | valuation:small_discount |
| RBBF40 | -3.61% | valuation:small_discount; liquidity:low; maturity:11.8y |
| GBIMESY2 | -3.46% | valuation:small_discount; maturity:9.4y |
| HLICF | -2.49% | valuation:small_discount; liquidity:low; maturity:9.6y |
| SEF | -2.30% | valuation:small_discount |
| H8020 | -2.10% | valuation:small_discount; maturity:7.6y |
| CMF2 | -2.09% | valuation:small_discount; liquidity:low |
| NMB50 | -0.48% | valuation:small_discount |
| NIBLGF | 0.31% | valuation:premium; maturity:6.9y |

</details>

## Data Quality

- Symbols checked: 41
- Symbols with issues: 10
- NAV data age: median 27 days, max 258 days

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
