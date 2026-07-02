# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-02 12:22*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-02 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 23 |
| Median Discount | -8.14% |
| CONSIDER | 3 |
| IGNORE | 38 |

> ⚠️ **NAV Staleness Warning**: 13 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 12 | 29.3% |
| -10% to -6% | 15 | 36.6% |
| -6% to -4% | 4 | 9.8% |
| -4% to 0% | 10 | 24.4% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 11.88 | -13.22% | 2.0y | high | 22d | -4.60% | 71.8 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.45 | -9.05% | 3.0y | medium | 4d | -1.24% | 53.7 | → stable | — |
| 3 | SEF | Siddhartha Equity Fund | 10.65 | 9.95 | -6.57% | 1.4y | high | 1d | 0.00% | 46.6 | ↓ widening | — |

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
| LUK | -14.24% | maturity:4.1y |
| LVF2 | -13.50% | liquidity:low; maturity:7.2y |
| KDBY | -13.37% | maturity:6.1y |
| PRSF | -13.07% | maturity:5.7y |
| SBCF | -12.70% | maturity:4.7y |
| SFEF | -12.34% | liquidity:low; maturity:5.6y |
| GIBF1 | -11.45% | maturity:6.1y |
| KEF | -11.21% | maturity:4.7y |
| NICGF2 | -11.17% | maturity:4.4y |
| SIGS3 | -10.92% | maturity:6.8y |
| NICBF | -10.40% | liquidity:low |
| NSIF2 | -9.97% | maturity:6.2y |
| RMF2 | -9.58% | maturity:6.9y |
| RBBF40 | -9.36% | maturity:11.4y |
| MBLEF | -9.26% | maturity:10.7y |
| RSY | -9.25% | maturity:8.8y |
| GBIMESY2 | -8.51% | liquidity:low; maturity:9.1y |
| NIBSF2 | -8.36% | liquidity:low; maturity:4.9y |
| NMBHF2 | -8.14% | maturity:8.7y |
| NIBLSTF | -8.06% | liquidity:low; maturity:9.6y |
| KSY | -8.04% | liquidity:low; maturity:7.7y |
| NIBLGF | -7.31% | maturity:6.5y |
| MNMF1 | -7.25% | maturity:8.5y |
| GSY | -6.01% | maturity:8.5y |
| C30MF | -5.83% | maturity:6.9y |
| RMF1 | -5.65% | liquidity:low |
| H8020 | -5.31% | maturity:7.2y |
| SFMF | -4.42% | liquidity:low |
| NBF2 | -3.92% | valuation:small_discount |
| SIGS2 | -3.74% | valuation:small_discount |
| NICSF | -3.27% | valuation:small_discount |
| SLCF | -3.19% | valuation:small_discount |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.2y |
| CMF2 | -2.65% | valuation:small_discount |
| SAGF | -2.60% | valuation:small_discount; maturity:7.4y |
| NMB50 | -0.94% | valuation:small_discount |
| MMF1 | -0.82% | valuation:small_discount; maturity:5.2y |
| HLICF | -0.45% | valuation:small_discount; liquidity:low; maturity:9.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 25
- NAV data age: median 17 days, max 399 days

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
