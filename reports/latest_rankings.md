# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-24 12:31*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-24 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 20 |
| Median Discount | -7.92% |
| CONSIDER | 3 |
| IGNORE | 38 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 14 | 34.1% |
| -10% to -6% | 13 | 31.7% |
| -6% to -4% | 4 | 9.8% |
| -4% to 0% | 9 | 22.0% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 11.81 | -13.73% | 2.0y | high | 16d | -4.60% | 62.6 | ↓ widening | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.27 | -10.78% | 3.0y | medium | 1d | -1.24% | 57.1 | ↓ widening | — |
| 3 | SIGS2 | Siddhartha Investment Gro | 11.23 | 10.22 | -8.99% | 3.2y | medium | 3d | -2.60% | 47.4 | ↓ widening | — |

## IGNORE Summary

*38 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -15.09% | maturity:5.7y |
| KDBY | -14.92% | maturity:6.1y |
| LVF2 | -14.55% | liquidity:low; maturity:7.2y |
| KEF | -12.24% | maturity:4.7y |
| GIBF1 | -12.01% | liquidity:low; maturity:6.1y |
| SBCF | -11.82% | maturity:4.8y |
| NICGF2 | -11.65% | maturity:4.4y |
| SFEF | -11.64% | maturity:5.6y |
| NICBF | -11.18% | liquidity:low |
| NSIF2 | -11.14% | maturity:6.2y |
| RMF2 | -10.97% | liquidity:low; maturity:6.9y |
| RSY | -10.25% | maturity:8.9y |
| MBLEF | -9.17% | maturity:10.8y |
| RBBF40 | -9.09% | maturity:11.4y |
| H8020 | -8.71% | maturity:7.3y |
| NMBHF2 | -8.23% | maturity:8.7y |
| NIBSF2 | -8.00% | liquidity:low; maturity:4.9y |
| GBIMESY2 | -7.92% | maturity:9.1y |
| KSY | -7.50% | maturity:7.7y |
| LUK | -7.46% | maturity:4.1y |
| C30MF | -7.06% | liquidity:low; maturity:6.9y |
| SAGF | -7.06% | maturity:7.4y |
| SIGS3 | -6.64% | liquidity:low; maturity:6.8y |
| MNMF1 | -6.35% | maturity:8.5y |
| NBF2 | -5.35% | liquidity:low |
| NIBLSTF | -5.03% | maturity:9.6y |
| GSY | -4.49% | maturity:8.5y |
| NIBLGF | -4.43% | maturity:6.6y |
| RMF1 | -3.94% | valuation:small_discount |
| NICSF | -3.73% | valuation:small_discount |
| CMF2 | -3.32% | valuation:small_discount |
| NMB50 | -3.32% | valuation:small_discount; liquidity:low |
| SEF | -3.29% | valuation:small_discount |
| NBF3 | -3.20% | valuation:small_discount; maturity:5.2y |
| SFMF | -2.65% | valuation:small_discount; liquidity:low |
| SLCF | -2.42% | valuation:small_discount |
| MMF1 | -0.72% | valuation:small_discount; maturity:5.2y |
| HLICF | 0.23% | valuation:premium; maturity:9.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 26
- NAV data age: median 40 days, max 391 days

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
