# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-01 12:48*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-01 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 19 |
| Median Discount | -7.39% |
| CONSIDER | 6 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 13 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 16 | 39.0% |
| -10% to -6% | 10 | 24.4% |
| -6% to -4% | 8 | 19.5% |
| -4% to 0% | 7 | 17.1% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 11.90 | -13.08% | 2.0y | high | 21d | -4.60% | 72.1 | ↑ narrowing | — |
| 2 | SIGS2 | Siddhartha Investment Gro | 11.22 | 10.50 | -6.42% | 3.2y | medium | 1d | -0.09% | 64.9 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.35 | -10.01% | 3.0y | medium | 3d | -1.24% | 57.8 | ↑ narrowing | — |
| 4 | NICSF | NIC Asia Select-30 | 9.80 | 9.30 | -5.10% | 2.0y | medium | 1d | 1.45% | 53.8 | → stable | — |
| 5 | CMF2 | Citizens Mutual Fund - 2 | 10.17 | 9.69 | -4.72% | 0.0y | medium | 1d | -0.59% | 44.3 | ↓ widening | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.45 | 10.00 | -4.31% | 2.1y | medium | 3d | 0.38% | 39.6 | → stable | high_vol |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 7 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -14.08% | maturity:5.7y |
| KDBY | -14.07% | maturity:6.1y |
| SBCF | -13.58% | maturity:4.7y |
| NICBF | -13.01% | liquidity:low |
| LUK | -12.52% | maturity:4.1y |
| LVF2 | -12.36% | liquidity:low; maturity:7.2y |
| KEF | -11.63% | maturity:4.7y |
| GIBF1 | -11.53% | maturity:6.1y |
| SIGS3 | -11.34% | maturity:6.8y |
| SFEF | -10.85% | maturity:5.6y |
| RSY | -10.66% | liquidity:low; maturity:8.8y |
| H8020 | -10.06% | liquidity:low; maturity:7.3y |
| RBBF40 | -10.05% | liquidity:low; maturity:11.4y |
| NICGF2 | -10.03% | maturity:4.4y |
| NSIF2 | -9.56% | maturity:6.2y |
| MBLEF | -9.26% | maturity:10.8y |
| NIBSF2 | -9.16% | liquidity:low; maturity:4.9y |
| MNMF1 | -7.63% | maturity:8.5y |
| NMBHF2 | -7.39% | maturity:8.7y |
| NIBLSTF | -7.35% | maturity:9.6y |
| RMF2 | -7.32% | liquidity:low; maturity:6.9y |
| NIBLGF | -7.31% | liquidity:low; maturity:6.5y |
| GBIMESY2 | -7.05% | maturity:9.1y |
| KSY | -5.49% | maturity:7.7y |
| SAGF | -5.29% | maturity:7.4y |
| C30MF | -5.18% | maturity:6.9y |
| GSY | -4.67% | maturity:8.5y |
| SFMF | -4.42% | liquidity:low |
| NBF2 | -3.92% | valuation:small_discount |
| SEF | -3.76% | valuation:small_discount |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.2y |
| SLCF | -2.99% | valuation:small_discount |
| NMB50 | -2.36% | valuation:small_discount; liquidity:low |
| HLICF | -2.23% | valuation:small_discount; maturity:9.2y |
| MMF1 | -1.33% | valuation:small_discount; maturity:5.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 26
- NAV data age: median 16 days, max 398 days

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
