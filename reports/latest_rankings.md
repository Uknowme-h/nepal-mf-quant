# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-22 15:34*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-22 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 19 |
| Median Discount | -7.71% |
| CONSIDER | 4 |
| IGNORE | 37 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 13 | 31.7% |
| -10% to -6% | 11 | 26.8% |
| -6% to -4% | 7 | 17.1% |
| -4% to 0% | 10 | 24.4% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICBF | NIC ASIA Balanced Fund | 10.38 | 9.18 | -11.56% | 3.2y | medium | 1d | -0.86% | 64.9 | → stable | high_vol |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.33 | -10.20% | 3.0y | medium | 10d | -1.24% | 61.2 | ↓ widening | — |
| 3 | PSF | Prabhu Select Fund | 13.69 | 11.99 | -12.42% | 2.0y | medium | 14d | -4.60% | 55.7 | ↓ widening | — |
| 4 | SIGS2 | Siddhartha Investment Gro | 11.23 | 10.50 | -6.50% | 3.2y | medium | 1d | -2.60% | 43.9 | ↓ widening | — |

## IGNORE Summary

*37 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -15.34% | maturity:4.8y |
| PRSF | -15.03% | maturity:5.7y |
| KDBY | -14.53% | maturity:6.1y |
| LVF2 | -14.02% | maturity:7.2y |
| LUK | -12.52% | maturity:4.2y |
| KEF | -12.49% | maturity:4.7y |
| GIBF1 | -12.01% | maturity:6.1y |
| SFEF | -11.81% | liquidity:low; maturity:5.7y |
| SIGS3 | -11.44% | liquidity:low; maturity:6.9y |
| NSIF2 | -10.97% | maturity:6.2y |
| RSY | -9.89% | maturity:8.9y |
| MBLEF | -9.63% | maturity:10.8y |
| RMF2 | -9.34% | liquidity:low; maturity:6.9y |
| NICGF2 | -9.26% | maturity:4.4y |
| NMBHF2 | -9.08% | maturity:8.7y |
| NIBLSTF | -8.11% | liquidity:low; maturity:9.6y |
| GBIMESY2 | -7.92% | maturity:9.1y |
| RBBF40 | -7.71% | liquidity:low; maturity:11.4y |
| MNMF1 | -6.54% | maturity:8.5y |
| C30MF | -6.13% | liquidity:low; maturity:6.9y |
| KSY | -5.98% | liquidity:low; maturity:7.8y |
| NIBLGF | -5.94% | liquidity:low; maturity:6.6y |
| NBF2 | -5.35% | liquidity:low |
| SFMF | -5.31% | liquidity:low |
| SAGF | -5.29% | maturity:7.4y |
| GSY | -4.49% | maturity:8.5y |
| NBF3 | -4.07% | maturity:5.3y |
| NICSF | -3.93% | valuation:small_discount |
| CMF2 | -3.71% | valuation:small_discount |
| SLCF | -3.58% | valuation:small_discount |
| NIBSF2 | -3.55% | valuation:small_discount; maturity:4.9y |
| RMF1 | -3.46% | valuation:small_discount |
| SEF | -3.29% | valuation:small_discount |
| H8020 | -2.53% | valuation:small_discount; maturity:7.3y |
| HLICF | -1.47% | valuation:small_discount; maturity:9.2y |
| MMF1 | -1.24% | valuation:small_discount; maturity:5.2y |
| NMB50 | -0.85% | valuation:small_discount |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 21
- NAV data age: median 38 days, max 389 days

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
