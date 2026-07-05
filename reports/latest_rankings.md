# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-05 11:49*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-03 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 20 |
| Median Discount | -7.76% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 12 | 29.3% |
| -10% to -6% | 15 | 36.6% |
| -6% to -4% | 6 | 14.6% |
| -4% to 0% | 8 | 19.5% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 11.82 | -13.66% | 2.0y | medium | 23d | -4.60% | 65.5 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.40 | -9.53% | 3.0y | medium | 5d | -1.24% | 58.3 | ↑ narrowing | — |
| 3 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.79 | -4.51% | 3.3y | high | 1d | -2.04% | 54.1 | ↑ narrowing | — |
| 4 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.87 | -5.73% | 2.9y | high | 1d | 0.48% | 52.7 | ↓ widening | — |
| 5 | NICBF | NIC ASIA Balanced Fund | 10.38 | 9.30 | -10.40% | 3.1y | medium | 1d | -0.86% | 49.4 | → stable | high_vol |
| 6 | NICSF | NIC Asia Select-30 | 9.80 | 9.24 | -5.71% | 2.0y | medium | 1d | 1.45% | 47.4 | ↓ widening | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.80 | -6.22% | 2.1y | medium | 1d | 0.38% | 39.4 | ↓ widening | high_vol |
| 8 | SEF | Siddhartha Equity Fund | 10.65 | 9.95 | -6.57% | 1.4y | medium | 2d | 0.00% | 38.7 | ↓ widening | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 8 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -15.03% | maturity:5.7y |
| LUK | -14.15% | maturity:4.1y |
| SBCF | -13.58% | maturity:4.7y |
| KDBY | -13.45% | maturity:6.1y |
| LVF2 | -12.36% | maturity:7.2y |
| SFEF | -12.34% | liquidity:low; maturity:5.6y |
| NICGF2 | -12.03% | maturity:4.4y |
| RSY | -11.81% | liquidity:low; maturity:8.8y |
| GIBF1 | -11.28% | liquidity:low; maturity:6.1y |
| SIGS3 | -10.92% | maturity:6.8y |
| GBIMESY2 | -9.78% | maturity:9.1y |
| KEF | -9.71% | maturity:4.7y |
| RMF2 | -9.58% | liquidity:low; maturity:6.9y |
| NSIF2 | -9.56% | maturity:6.2y |
| MBLEF | -9.26% | liquidity:low; maturity:10.7y |
| RBBF40 | -8.87% | maturity:11.4y |
| NIBSF2 | -8.36% | maturity:4.9y |
| KSY | -7.76% | maturity:7.7y |
| NMBHF2 | -7.39% | maturity:8.7y |
| NIBLGF | -7.31% | liquidity:low; maturity:6.5y |
| MNMF1 | -7.25% | maturity:8.5y |
| GSY | -6.77% | maturity:8.5y |
| C30MF | -5.83% | maturity:6.9y |
| H8020 | -5.31% | liquidity:low; maturity:7.2y |
| NIBLSTF | -5.10% | maturity:9.6y |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.2y |
| SAGF | -3.05% | valuation:small_discount; liquidity:low; maturity:7.4y |
| SLCF | -2.99% | valuation:small_discount |
| CMF2 | -2.65% | valuation:small_discount; liquidity:low |
| SIGS2 | -2.41% | valuation:small_discount |
| HLICF | -1.79% | valuation:small_discount; maturity:9.2y |
| NMB50 | -0.94% | valuation:small_discount; liquidity:low |
| MMF1 | -0.31% | valuation:small_discount; maturity:5.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 28
- NAV data age: median 20 days, max 402 days

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
