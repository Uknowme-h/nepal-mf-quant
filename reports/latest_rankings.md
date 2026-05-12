# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-12 12:13*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-12 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 25 |
| Median Discount | -9.73% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 17 | 41.5% |
| -10% to -6% | 15 | 36.6% |
| -6% to -4% | 3 | 7.3% |
| -4% to 0% | 6 | 14.6% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 14.35 | 12.03 | -16.17% | 2.1y | high | 7d | 12.55% | 74.6 | ↑ narrowing | — |
| 2 | SIGS2 | Siddhartha Investment Gro | 11.53 | 10.39 | -9.89% | 3.3y | medium | 1d | 5.01% | 65.2 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.40 | -10.65% | 3.1y | medium | 2d | 4.26% | 59.9 | ↑ narrowing | — |
| 4 | SLCF | Sanima Large Cap Fund | 10.65 | 10.00 | -6.10% | 1.8y | medium | 23d | 0.47% | 59.6 | ↑ narrowing | — |
| 5 | SEF | Siddhartha Equity Fund | 10.95 | 10.05 | -8.22% | 1.5y | high | 2d | 3.79% | 58.5 | ↑ narrowing | — |
| 6 | CMF2 | Citizens Mutual Fund - 2 | 10.52 | 10.01 | -4.85% | 0.2y | medium | 2d | -0.94% | 54.6 | ↑ narrowing | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.64 | 10.09 | -5.17% | 2.2y | medium | 15d | 0.76% | 52.2 | ↑ narrowing | high_vol |
| 8 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.55 | -6.64% | 3.5y | medium | 5d | -2.04% | 49.0 | ↑ narrowing | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 9 |
| valuation | 6 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -17.35% | maturity:5.8y |
| KEF | -16.67% | maturity:4.8y |
| KDBY | -16.30% | maturity:6.2y |
| LVF2 | -15.78% | maturity:7.3y |
| GIBF1 | -13.44% | liquidity:low; maturity:6.2y |
| SIGS3 | -13.27% | maturity:7.0y |
| NICGF2 | -12.84% | maturity:4.5y |
| LUK | -12.61% | maturity:4.3y |
| RSY | -11.97% | maturity:9.0y |
| SBCF | -11.90% | maturity:4.9y |
| SFEF | -11.90% | maturity:5.8y |
| NSIF2 | -11.57% | liquidity:low; maturity:6.3y |
| MBLEF | -10.93% | maturity:10.9y |
| MNMF1 | -10.30% | maturity:8.6y |
| KSY | -10.15% | maturity:7.9y |
| RMF2 | -9.86% | liquidity:low; maturity:7.0y |
| NMBHF2 | -9.83% | maturity:8.8y |
| GSY | -9.73% | maturity:8.7y |
| H8020 | -9.68% | liquidity:low; maturity:7.4y |
| GBIMESY2 | -9.27% | maturity:9.2y |
| C30MF | -8.83% | maturity:7.0y |
| NICBF | -7.74% | liquidity:low |
| NIBLSTF | -7.47% | maturity:9.8y |
| SAGF | -7.10% | liquidity:low; maturity:7.5y |
| NIBLGF | -6.22% | liquidity:low; maturity:6.7y |
| NIBSF2 | -6.14% | maturity:5.0y |
| NBF2 | -4.49% | liquidity:low |
| MMF1 | -3.91% | valuation:small_discount; maturity:5.3y |
| NBF3 | -3.88% | valuation:small_discount; maturity:5.4y |
| RBBF40 | -3.80% | valuation:small_discount; maturity:11.5y |
| NICSF | -3.13% | valuation:small_discount; liquidity:low |
| NMB50 | -2.14% | valuation:small_discount |
| HLICF | -0.21% | valuation:small_discount; maturity:9.3y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 24
- NAV data age: median 27 days, max 348 days

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
