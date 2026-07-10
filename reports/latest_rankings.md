# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-10 12:38*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-10 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 22 |
| Median Discount | -8.77% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 17 | 41.5% |
| -10% to -6% | 12 | 29.3% |
| -6% to -4% | 6 | 14.6% |
| -4% to 0% | 6 | 14.6% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 11.85 | -13.44% | 1.9y | medium | 27d | -4.60% | 64.8 | → stable | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.60 | -7.60% | 2.9y | medium | 9d | -1.24% | 56.6 | ↑ narrowing | — |
| 3 | SEF | Siddhartha Equity Fund | 10.65 | 10.22 | -4.04% | 1.3y | medium | 6d | 0.00% | 54.3 | ↑ narrowing | — |
| 4 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.90 | -5.44% | 2.9y | medium | 3d | 0.48% | 53.7 | ↓ widening | — |
| 5 | NICSF | NIC Asia Select-30 | 9.80 | 9.35 | -4.59% | 2.0y | high | 5d | 1.45% | 52.8 | ↓ widening | — |
| 6 | SIGS2 | Siddhartha Investment Gro | 11.22 | 10.20 | -9.09% | 3.1y | medium | 1d | -0.09% | 51.3 | ↓ widening | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.80 | -6.22% | 2.0y | medium | 5d | 0.38% | 50.1 | ↓ widening | high_vol |
| 8 | NICBF | NIC ASIA Balanced Fund | 10.38 | 9.10 | -12.33% | 3.1y | medium | 2d | -0.86% | 49.8 | ↓ widening | high_vol |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 6 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| KDBY | -16.50% | maturity:6.0y |
| SBCF | -14.81% | maturity:4.7y |
| LVF2 | -14.55% | liquidity:low; maturity:7.2y |
| PRSF | -14.42% | maturity:5.7y |
| LUK | -14.24% | maturity:4.1y |
| NIBLSTF | -13.57% | maturity:9.6y |
| NICGF2 | -13.09% | maturity:4.4y |
| SFEF | -12.51% | liquidity:low; maturity:5.6y |
| GIBF1 | -12.28% | liquidity:low; maturity:6.0y |
| GBIMESY2 | -11.06% | maturity:9.0y |
| RSY | -11.01% | maturity:8.8y |
| SIGS3 | -10.92% | maturity:6.8y |
| NIBSF2 | -10.78% | maturity:4.9y |
| NSIF2 | -10.73% | liquidity:low; maturity:6.2y |
| RMF2 | -10.04% | liquidity:low; maturity:6.9y |
| SFMF | -9.73% | liquidity:low |
| MBLEF | -9.26% | liquidity:low; maturity:10.7y |
| RBBF40 | -8.77% | maturity:11.3y |
| KSY | -8.23% | maturity:7.7y |
| C30MF | -7.40% | liquidity:low; maturity:6.8y |
| NMBHF2 | -7.39% | maturity:8.6y |
| MNMF1 | -7.25% | maturity:8.4y |
| KEF | -6.61% | maturity:4.7y |
| H8020 | -6.50% | maturity:7.2y |
| SAGF | -5.27% | maturity:7.4y |
| NIBLGF | -4.81% | liquidity:low; maturity:6.5y |
| GSY | -4.67% | maturity:8.5y |
| SLCF | -3.47% | valuation:small_discount |
| NMB50 | -3.30% | valuation:small_discount |
| CMF2 | -2.65% | valuation:small_discount; liquidity:low |
| HLICF | -2.57% | valuation:small_discount; maturity:9.2y |
| NBF3 | -2.13% | valuation:small_discount; maturity:5.2y |
| MMF1 | -1.84% | valuation:small_discount; maturity:5.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 25
- NAV data age: median 25 days, max 407 days

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
