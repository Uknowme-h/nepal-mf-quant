# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-27 13:49*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-27 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 22 |
| Median Discount | -8.26% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 12 | 29.3% |
| -10% to -6% | 19 | 46.3% |
| -6% to -4% | 5 | 12.2% |
| -4% to 0% | 4 | 9.8% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 14.35 | 12.54 | -12.61% | 2.1y | medium | 9d | 12.55% | 81.3 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.59 | -8.84% | 3.0y | medium | 2d | 4.26% | 65.6 | ↑ narrowing | — |
| 3 | SIGS2 | Siddhartha Investment Gro | 11.53 | 10.71 | -7.11% | 3.2y | medium | 2d | 5.01% | 62.3 | ↑ narrowing | — |
| 4 | SEF | Siddhartha Equity Fund | 10.95 | 10.20 | -6.85% | 1.4y | high | 13d | 3.79% | 60.2 | ↑ narrowing | — |
| 5 | SLCF | Sanima Large Cap Fund | 10.65 | 10.17 | -4.51% | 1.8y | medium | 5d | 0.47% | 57.0 | ↑ narrowing | — |
| 6 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.70 | -7.35% | 3.2y | medium | 2d | 4.39% | 46.6 | → stable | high_vol |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.64 | 9.85 | -7.42% | 2.2y | medium | 26d | 0.76% | 44.6 | ↓ widening | high_vol |
| 8 | NICSF | NIC Asia Select-30 | 9.89 | 9.32 | -5.76% | 2.1y | medium | 1d | -1.49% | 33.8 | → stable | — |

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
| PRSF | -17.67% | maturity:5.8y |
| KDBY | -16.23% | maturity:6.2y |
| KEF | -14.33% | maturity:4.8y |
| SBCF | -13.32% | maturity:4.8y |
| LUK | -12.95% | maturity:4.2y |
| LVF2 | -12.36% | maturity:7.3y |
| GIBF1 | -11.98% | maturity:6.2y |
| SFEF | -11.64% | liquidity:low; maturity:5.7y |
| RSY | -11.36% | maturity:8.9y |
| GBIMESY2 | -10.61% | maturity:9.2y |
| NSIF2 | -10.50% | maturity:6.3y |
| MBLEF | -9.79% | maturity:10.8y |
| NMBHF2 | -9.74% | maturity:8.8y |
| SFMF | -9.73% | liquidity:low |
| KSY | -9.32% | maturity:7.8y |
| NICGF2 | -8.90% | liquidity:low; maturity:4.5y |
| SIGS3 | -8.79% | maturity:6.9y |
| MNMF1 | -8.75% | maturity:8.6y |
| GSY | -8.26% | liquidity:low; maturity:8.6y |
| NIBLGF | -8.00% | liquidity:low; maturity:6.7y |
| RMF2 | -7.64% | liquidity:low; maturity:7.0y |
| C30MF | -7.28% | liquidity:low; maturity:7.0y |
| SAGF | -7.19% | liquidity:low; maturity:7.5y |
| NIBLSTF | -7.07% | liquidity:low; maturity:9.7y |
| RBBF40 | -6.43% | maturity:11.5y |
| NIBSF2 | -5.15% | maturity:5.0y |
| MMF1 | -5.01% | maturity:5.3y |
| H8020 | -4.37% | maturity:7.3y |
| HLICF | -3.43% | valuation:small_discount; maturity:9.3y |
| NBF3 | -3.29% | valuation:small_discount; maturity:5.3y |
| CMF2 | -3.04% | valuation:small_discount |
| NBF2 | -2.67% | valuation:small_discount |
| NMB50 | 0.74% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 16
- NAV data age: median 42 days, max 363 days

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
