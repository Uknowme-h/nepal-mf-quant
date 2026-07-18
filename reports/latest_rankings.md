# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-18 11:19*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-17 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 37 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 21 |
| Median Discount | -9.03% |
| CONSIDER | 6 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 16 | 40.0% |
| -10% to -6% | 12 | 30.0% |
| -6% to -4% | 4 | 10.0% |
| -4% to 0% | 6 | 15.0% |
| ≥ 0% (premium) | 2 | 5.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 11.92 | -12.93% | 1.9y | high | 32d | -4.60% | 67.5 | ↑ narrowing | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.20 | -9.73% | 3.3y | medium | 5d | -2.04% | 56.7 | → stable | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.76 | -6.60% | 2.0y | high | 1d | 0.38% | 51.5 | → stable | high_vol |
| 4 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.10 | -12.42% | 2.9y | medium | 1d | -1.24% | 50.4 | ↓ widening | — |
| 5 | NICSF | NIC Asia Select-30 | 9.80 | 9.26 | -5.51% | 2.0y | medium | 10d | 1.45% | 46.5 | ↓ widening | — |
| 6 | SEF | Siddhartha Equity Fund | 10.65 | 9.98 | -6.29% | 1.3y | medium | 11d | 0.00% | 45.0 | ↓ widening | — |

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
| KDBY | -15.01% | maturity:6.0y |
| PRSF | -13.81% | maturity:5.7y |
| KEF | -13.47% | maturity:4.7y |
| SFEF | -12.95% | liquidity:low; maturity:5.6y |
| GIBF1 | -12.70% | maturity:6.0y |
| LVF2 | -12.36% | maturity:7.1y |
| RSY | -11.89% | maturity:8.8y |
| NSIF2 | -11.74% | maturity:6.1y |
| NICBF | -10.98% | liquidity:low |
| NIBSF2 | -10.88% | maturity:4.9y |
| RMF2 | -10.31% | liquidity:low; maturity:6.8y |
| SBCF | -10.14% | maturity:4.7y |
| SIGS3 | -10.08% | liquidity:low; maturity:6.8y |
| LUK | -10.03% | maturity:4.1y |
| MNMF1 | -9.51% | maturity:8.4y |
| NMBHF2 | -9.47% | maturity:8.6y |
| NICGF2 | -9.26% | maturity:4.3y |
| MBLEF | -8.80% | maturity:10.7y |
| KSY | -7.76% | maturity:7.7y |
| RBBF40 | -7.59% | maturity:11.3y |
| H8020 | -7.13% | liquidity:low; maturity:7.2y |
| NBF2 | -6.40% | liquidity:low |
| NIBLSTF | -6.33% | maturity:9.6y |
| C30MF | -5.64% | maturity:6.8y |
| GBIMESY2 | -5.19% | maturity:9.0y |
| SIGS2 | -4.90% | liquidity:low |
| HLICF | -3.57% | valuation:small_discount; maturity:9.2y |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.2y |
| SAGF | -3.05% | valuation:small_discount; liquidity:low; maturity:7.4y |
| GSY | -1.81% | valuation:small_discount; liquidity:low; maturity:8.5y |
| SLCF | -1.16% | valuation:small_discount |
| NMB50 | 0.00% | valuation:premium |
| MMF1 | 0.92% | valuation:premium; maturity:5.2y |
| NIBLGF | 9.32% | valuation:premium; liquidity:low; maturity:6.5y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 32
- NAV data age: median 33 days, max 415 days

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
