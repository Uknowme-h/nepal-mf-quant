# Nepal MF Quant — Full Analysis Report

*Generated: 2026-11-05 18:01*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-11-05 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 25 |
| Median Discount | -9.14% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 15 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 10 | 25.6% |
| -10% to -6% | 22 | 56.4% |
| -6% to -4% | 2 | 5.1% |
| -4% to 0% | 4 | 10.3% |
| ≥ 0% (premium) | 1 | 2.6% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | LUK | Laxmi Unnati Kosh | 11.66 | 9.60 | -17.67% | 3.8y | medium | 2d | -1.17% | 69.0 | → stable | — |
| 2 | SEF | Siddhartha Equity Fund | 10.78 | 10.00 | -7.24% | 1.0y | high | 15d | 2.76% | 68.3 | ↑ narrowing | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.21 | 9.15 | -10.38% | 1.7y | medium | 22d | -0.10% | 64.1 | ↑ narrowing | high_vol |
| 4 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.16 | -12.51% | 2.6y | medium | 6d | 0.48% | 63.3 | ↓ widening | — |
| 5 | SLCF | Sanima Large Cap Fund | 10.10 | 9.15 | -9.41% | 1.3y | medium | 1d | 0.60% | 62.6 | → stable | — |
| 6 | NICSF | NIC Asia Select-30 | 9.50 | 8.69 | -8.53% | 1.7y | medium | 24d | 2.37% | 61.1 | ↑ narrowing | high_vol |
| 7 | SIGS2 | Siddhartha Investment Gro | 10.65 | 9.66 | -9.30% | 2.8y | medium | 1d | 3.30% | 55.1 | ↓ widening | — |
| 8 | NICFC | NIC Asia Flexi Cap Fund | 9.94 | 9.27 | -6.74% | 2.6y | medium | 2d | -1.29% | 53.2 | ↑ narrowing | — |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 5 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -20.38% | liquidity:low; maturity:5.3y |
| SBCF | -18.17% | maturity:4.4y |
| LVF2 | -17.62% | liquidity:low; maturity:6.8y |
| SFMF | -12.39% | liquidity:low |
| NBF3 | -12.11% | maturity:4.9y |
| MBLEF | -10.28% | maturity:10.4y |
| RMF2 | -10.18% | liquidity:low; maturity:6.5y |
| MMF1 | -9.86% | maturity:4.8y |
| NIBLGF | -9.75% | maturity:6.2y |
| MNMF1 | -9.70% | maturity:8.1y |
| RBBF40 | -9.54% | maturity:11.0y |
| NMBHF2 | -9.51% | liquidity:low; maturity:8.3y |
| NIBLSTF | -9.39% | maturity:9.3y |
| NICGF2 | -9.32% | liquidity:low; maturity:4.0y |
| NIBSF2 | -9.14% | maturity:4.6y |
| C30MF | -9.09% | maturity:6.5y |
| GBIMESY2 | -9.05% | maturity:8.7y |
| GSY | -9.04% | maturity:8.2y |
| RSY | -8.65% | maturity:8.5y |
| NICBF | -7.99% | liquidity:low |
| SAGF | -7.40% | liquidity:low; maturity:7.1y |
| KSY | -7.04% | maturity:7.4y |
| KDBY | -6.17% | maturity:5.7y |
| NSIF2 | -6.05% | maturity:5.8y |
| KEF | -5.77% | maturity:4.4y |
| GIBF1 | -4.96% | liquidity:low; maturity:5.7y |
| PSF | -3.50% | valuation:small_discount |
| SIGS3 | -2.82% | valuation:small_discount; maturity:6.5y |
| PRSF | -2.61% | valuation:small_discount; maturity:5.4y |
| HLICF | -1.51% | valuation:small_discount; liquidity:low; maturity:8.9y |
| H8020 | 1.53% | valuation:premium; maturity:6.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 29
- NAV data age: median 21 days, max 525 days

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
