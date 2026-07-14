# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-14 11:45*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-14 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 24 |
| Median Discount | -8.97% |
| CONSIDER | 7 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 17 | 42.5% |
| -10% to -6% | 14 | 35.0% |
| -6% to -4% | 3 | 7.5% |
| -4% to 0% | 5 | 12.5% |
| ≥ 0% (premium) | 1 | 2.5% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 11.80 | -13.81% | 1.9y | medium | 29d | -4.60% | 65.2 | → stable | — |
| 2 | NICSF | NIC Asia Select-30 | 9.80 | 9.35 | -4.59% | 2.0y | high | 7d | 1.45% | 56.9 | → stable | — |
| 3 | SEF | Siddhartha Equity Fund | 10.65 | 10.00 | -6.10% | 1.3y | medium | 8d | 0.00% | 52.7 | → stable | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.69 | -7.27% | 2.0y | high | 7d | 0.38% | 49.3 | ↓ widening | high_vol |
| 5 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.17 | -11.74% | 2.9y | medium | 1d | -1.24% | 48.3 | ↓ widening | — |
| 6 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.30 | -8.85% | 3.3y | medium | 2d | -2.04% | 44.0 | ↓ widening | — |
| 7 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.00 | -4.49% | 2.9y | medium | 5d | 0.48% | 44.0 | ↓ widening | — |

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
| KDBY | -15.32% | maturity:6.0y |
| LUK | -15.09% | liquidity:low; maturity:4.1y |
| PRSF | -15.09% | liquidity:low; maturity:5.7y |
| SBCF | -14.90% | maturity:4.7y |
| GIBF1 | -13.95% | maturity:6.0y |
| NICBF | -13.49% | liquidity:low |
| NSIF2 | -12.82% | maturity:6.1y |
| SFEF | -12.51% | maturity:5.6y |
| NIBSF2 | -12.39% | maturity:4.9y |
| LVF2 | -12.36% | liquidity:low; maturity:7.2y |
| RMF2 | -12.30% | maturity:6.9y |
| KEF | -12.13% | maturity:4.7y |
| RSY | -11.89% | liquidity:low; maturity:8.8y |
| SIGS3 | -11.85% | maturity:6.8y |
| NICGF2 | -10.41% | maturity:4.4y |
| MNMF1 | -9.60% | maturity:8.4y |
| NMBHF2 | -9.56% | maturity:8.6y |
| SIGS2 | -9.09% | liquidity:low |
| MBLEF | -8.62% | maturity:10.7y |
| H8020 | -8.48% | maturity:7.2y |
| RBBF40 | -8.37% | maturity:11.3y |
| NIBLSTF | -7.45% | maturity:9.6y |
| C30MF | -7.31% | maturity:6.8y |
| KSY | -7.28% | maturity:7.7y |
| SAGF | -7.12% | liquidity:low; maturity:7.4y |
| GBIMESY2 | -7.05% | liquidity:low; maturity:9.0y |
| NIBLGF | -4.81% | maturity:6.5y |
| GSY | -3.72% | valuation:small_discount; maturity:8.5y |
| NBF3 | -3.59% | valuation:small_discount; maturity:5.2y |
| SLCF | -3.47% | valuation:small_discount |
| HLICF | -2.34% | valuation:small_discount; liquidity:low; maturity:9.2y |
| NMB50 | -1.04% | valuation:small_discount; liquidity:low |
| MMF1 | 0.20% | valuation:premium; maturity:5.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 24
- NAV data age: median 29 days, max 411 days

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
