# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-08 11:58*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-08 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 22 |
| Median Discount | -8.11% |
| CONSIDER | 7 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 12 | 29.3% |
| -10% to -6% | 18 | 43.9% |
| -6% to -4% | 3 | 7.3% |
| -4% to 0% | 6 | 14.6% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 11.95 | -12.71% | 2.0y | high | 26d | -4.60% | 71.2 | → stable | — |
| 2 | NICSF | NIC Asia Select-30 | 9.80 | 9.40 | -4.08% | 2.0y | high | 4d | 1.45% | 61.8 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.36 | -9.91% | 2.9y | medium | 8d | -1.24% | 60.5 | → stable | — |
| 4 | NICBF | NIC ASIA Balanced Fund | 10.38 | 9.60 | -7.51% | 3.1y | medium | 1d | -0.86% | 56.6 | ↑ narrowing | high_vol |
| 5 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.81 | -6.30% | 2.9y | high | 2d | 0.48% | 51.5 | ↓ widening | — |
| 6 | SEF | Siddhartha Equity Fund | 10.65 | 9.91 | -6.95% | 1.3y | medium | 5d | 0.00% | 42.8 | ↓ widening | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.78 | -6.41% | 2.0y | medium | 4d | 0.38% | 41.7 | ↓ widening | high_vol |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 8 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| KDBY | -17.90% | maturity:6.0y |
| SBCF | -15.34% | maturity:4.7y |
| PRSF | -15.16% | maturity:5.7y |
| KEF | -13.56% | maturity:4.7y |
| SFEF | -12.95% | liquidity:low; maturity:5.6y |
| LVF2 | -12.36% | maturity:7.2y |
| NICGF2 | -12.13% | liquidity:low; maturity:4.4y |
| SIGS3 | -12.02% | maturity:6.8y |
| LUK | -11.66% | maturity:4.1y |
| NSIF2 | -11.15% | liquidity:low; maturity:6.2y |
| RSY | -11.01% | maturity:8.8y |
| GBIMESY2 | -9.98% | maturity:9.0y |
| GIBF1 | -9.69% | maturity:6.1y |
| NIBSF2 | -9.57% | liquidity:low; maturity:4.9y |
| KSY | -9.46% | maturity:7.7y |
| MBLEF | -9.26% | liquidity:low; maturity:10.7y |
| NIBLSTF | -9.08% | maturity:9.6y |
| RMF2 | -8.68% | liquidity:low; maturity:6.9y |
| SIGS2 | -8.11% | liquidity:low |
| SAGF | -8.04% | liquidity:low; maturity:7.4y |
| SFMF | -7.35% | liquidity:low |
| NMBHF2 | -7.29% | maturity:8.7y |
| MNMF1 | -7.25% | maturity:8.4y |
| NIBLGF | -6.91% | maturity:6.5y |
| C30MF | -5.27% | maturity:6.8y |
| GSY | -5.15% | maturity:8.5y |
| H8020 | -3.96% | valuation:small_discount; maturity:7.2y |
| SLCF | -3.38% | valuation:small_discount |
| RBBF40 | -3.15% | valuation:small_discount; maturity:11.4y |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.2y |
| CMF2 | -2.65% | valuation:small_discount; liquidity:low |
| NMB50 | -1.98% | valuation:small_discount |
| MMF1 | 0.10% | valuation:premium; maturity:5.2y |
| HLICF | 2.23% | valuation:premium; maturity:9.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 27
- NAV data age: median 23 days, max 405 days

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
