# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-20 11:43*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-20 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 20 |
| Median Discount | -7.91% |
| CONSIDER | 6 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 10 | 24.4% |
| -10% to -6% | 16 | 39.0% |
| -6% to -4% | 6 | 14.6% |
| -4% to 0% | 6 | 14.6% |
| ≥ 0% (premium) | 3 | 7.3% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SIGS2 | Siddhartha Investment Gro | 10.98 | 10.15 | -7.56% | 3.4y | high | 2d | 5.17% | 67.9 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.40 | -10.65% | 3.2y | medium | 2d | 4.26% | 60.9 | → stable | — |
| 3 | NICSF | NIC Asia Select-30 | 10.04 | 9.16 | -8.76% | 2.2y | medium | 3d | 5.35% | 53.2 | ↓ widening | — |
| 4 | SLCF | Sanima Large Cap Fund | 10.60 | 9.95 | -6.13% | 1.9y | medium | 8d | 4.43% | 52.4 | → stable | — |
| 5 | SEF | Siddhartha Equity Fund | 10.55 | 10.12 | -4.08% | 1.6y | medium | 1d | 4.98% | 52.4 | ↑ narrowing | high_vol |
| 6 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.66 | -5.66% | 3.5y | high | 1d | -2.04% | 50.0 | → stable | — |

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
| LVF2 | -13.85% | liquidity:low; maturity:7.4y |
| LUK | -13.38% | maturity:4.3y |
| SBCF | -11.90% | maturity:4.9y |
| MBLEF | -11.61% | maturity:10.9y |
| NICGF2 | -11.53% | liquidity:low; maturity:4.6y |
| SFEF | -11.46% | maturity:5.8y |
| NSIF2 | -10.41% | liquidity:low; maturity:6.4y |
| GIBF1 | -10.18% | maturity:6.3y |
| NIBLSTF | -10.14% | maturity:9.8y |
| KSY | -9.77% | maturity:7.9y |
| RSY | -9.65% | maturity:9.0y |
| MNMF1 | -9.58% | maturity:8.7y |
| RMF2 | -9.49% | liquidity:low; maturity:7.1y |
| RMF1 | -9.09% | liquidity:low |
| NICBF | -9.07% | liquidity:low |
| NIBSF2 | -8.78% | maturity:5.1y |
| NMBHF2 | -8.65% | maturity:8.9y |
| RBBF40 | -8.39% | maturity:11.6y |
| C30MF | -7.91% | liquidity:low; maturity:7.1y |
| NIBLGF | -7.41% | maturity:6.8y |
| SAGF | -6.93% | liquidity:low; maturity:7.6y |
| GSY | -6.91% | maturity:8.7y |
| GBIMESY2 | -5.96% | maturity:9.2y |
| H8020 | -4.61% | maturity:7.5y |
| NBF2 | -4.49% | liquidity:low |
| MMF1 | -4.43% | maturity:5.4y |
| CMF2 | -3.95% | valuation:small_discount; liquidity:low |
| NBF3 | -3.59% | valuation:small_discount; maturity:5.4y |
| SIGS3 | -3.35% | valuation:small_discount; maturity:7.0y |
| NMB50 | -3.31% | valuation:small_discount |
| HLICF | -3.22% | valuation:small_discount; maturity:9.4y |
| PSF | -2.04% | valuation:small_discount |
| PRSF | 1.85% | valuation:premium; maturity:5.9y |
| KDBY | 2.80% | valuation:premium; maturity:6.3y |
| KEF | 4.08% | valuation:premium; maturity:4.9y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 19
- NAV data age: median 36 days, max 326 days

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
