# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-11 12:52*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-11 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 24 |
| Median Discount | -9.03% |
| CONSIDER | 7 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 16 | 39.0% |
| -10% to -6% | 16 | 39.0% |
| -6% to -4% | 5 | 12.2% |
| -4% to 0% | 4 | 9.8% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 14.35 | 12.51 | -12.82% | 2.1y | medium | 6d | 12.55% | 77.3 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.57 | -9.03% | 3.1y | medium | 1d | 4.26% | 65.8 | ↑ narrowing | — |
| 3 | SEF | Siddhartha Equity Fund | 10.95 | 10.14 | -7.40% | 1.5y | high | 1d | 3.79% | 64.2 | ↑ narrowing | — |
| 4 | SLCF | Sanima Large Cap Fund | 10.65 | 9.95 | -6.57% | 1.8y | medium | 22d | 0.47% | 57.2 | ↑ narrowing | — |
| 5 | CMF2 | Citizens Mutual Fund - 2 | 10.52 | 10.00 | -4.94% | 0.2y | medium | 1d | -0.94% | 50.4 | ↑ narrowing | — |
| 6 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.40 | -7.96% | 3.5y | medium | 4d | -2.04% | 44.4 | ↓ widening | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.64 | 10.00 | -6.02% | 2.2y | medium | 14d | 0.76% | 38.4 | → stable | high_vol |

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
| LVF2 | -17.62% | maturity:7.3y |
| PRSF | -17.10% | maturity:5.8y |
| KEF | -16.82% | maturity:4.8y |
| LUK | -14.67% | maturity:4.3y |
| SBCF | -14.37% | maturity:4.9y |
| SIGS3 | -14.25% | liquidity:low; maturity:7.0y |
| GIBF1 | -12.55% | liquidity:low; maturity:6.2y |
| RSY | -12.14% | maturity:9.0y |
| NICGF2 | -11.90% | maturity:4.5y |
| MBLEF | -11.64% | maturity:10.9y |
| GSY | -10.93% | maturity:8.7y |
| SFEF | -10.76% | maturity:5.8y |
| SIGS2 | -10.23% | liquidity:low |
| KSY | -10.15% | maturity:7.9y |
| GBIMESY2 | -10.13% | liquidity:low; maturity:9.2y |
| NSIF2 | -9.92% | liquidity:low; maturity:6.3y |
| MNMF1 | -9.75% | maturity:8.6y |
| RMF2 | -9.41% | liquidity:low; maturity:7.0y |
| NIBSF2 | -9.31% | maturity:5.0y |
| C30MF | -9.01% | liquidity:low; maturity:7.0y |
| KDBY | -8.73% | maturity:6.2y |
| H8020 | -8.59% | maturity:7.4y |
| NMBHF2 | -7.49% | maturity:8.8y |
| SAGF | -7.19% | maturity:7.5y |
| RBBF40 | -6.52% | maturity:11.5y |
| NIBLGF | -6.22% | liquidity:low; maturity:6.7y |
| NICBF | -4.97% | liquidity:low |
| MMF1 | -4.71% | maturity:5.3y |
| NBF2 | -4.49% | liquidity:low |
| NIBLSTF | -4.38% | maturity:9.8y |
| NBF3 | -3.78% | valuation:small_discount; maturity:5.4y |
| NICSF | -2.93% | valuation:small_discount |
| NMB50 | -2.42% | valuation:small_discount |
| HLICF | -2.36% | valuation:small_discount; maturity:9.3y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 19
- NAV data age: median 26 days, max 347 days

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
