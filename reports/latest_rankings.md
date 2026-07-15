# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-15 11:48*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-15 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 24 |
| Median Discount | -9.34% |
| CONSIDER | 6 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 16 | 40.0% |
| -10% to -6% | 13 | 32.5% |
| -6% to -4% | 6 | 15.0% |
| -4% to 0% | 5 | 12.5% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 11.70 | -14.54% | 1.9y | medium | 30d | -4.60% | 64.8 | → stable | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.49 | -8.66% | 2.9y | medium | 2d | -1.24% | 60.2 | ↑ narrowing | — |
| 3 | SEF | Siddhartha Equity Fund | 10.65 | 9.96 | -6.48% | 1.3y | high | 9d | 0.00% | 54.9 | → stable | — |
| 4 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.91 | -5.35% | 2.9y | medium | 6d | 0.48% | 53.1 | ↓ widening | — |
| 5 | NICSF | NIC Asia Select-30 | 9.80 | 9.00 | -8.16% | 2.0y | medium | 8d | 1.45% | 48.0 | ↓ widening | — |
| 6 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.18 | -9.91% | 3.3y | medium | 3d | -2.04% | 44.8 | ↓ widening | — |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 5 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -16.64% | maturity:5.7y |
| KDBY | -15.79% | maturity:6.0y |
| LUK | -15.09% | liquidity:low; maturity:4.1y |
| SBCF | -14.90% | maturity:4.7y |
| KEF | -13.64% | maturity:4.7y |
| NIBLSTF | -13.27% | maturity:9.6y |
| NSIF2 | -12.82% | maturity:6.1y |
| LVF2 | -12.80% | maturity:7.1y |
| SFEF | -12.51% | liquidity:low; maturity:5.6y |
| GIBF1 | -12.28% | maturity:6.0y |
| RSY | -11.81% | maturity:8.8y |
| SIGS3 | -11.76% | liquidity:low; maturity:6.8y |
| NICBF | -10.98% | liquidity:low |
| NMBHF2 | -10.98% | maturity:8.6y |
| RMF2 | -10.22% | maturity:6.8y |
| SIGS2 | -9.98% | liquidity:low |
| NICGF2 | -9.93% | liquidity:low; maturity:4.3y |
| C30MF | -9.81% | maturity:6.8y |
| RBBF40 | -8.87% | maturity:11.3y |
| NIBSF2 | -8.36% | maturity:4.9y |
| MBLEF | -7.99% | maturity:10.7y |
| KSY | -7.76% | maturity:7.7y |
| GBIMESY2 | -7.05% | maturity:9.0y |
| MNMF1 | -6.78% | maturity:8.4y |
| RMF1 | -5.26% | liquidity:low |
| H8020 | -4.91% | maturity:7.2y |
| NIBLGF | -4.91% | liquidity:low; maturity:6.5y |
| SAGF | -4.81% | maturity:7.4y |
| GSY | -4.67% | maturity:8.5y |
| SLCF | -3.47% | valuation:small_discount |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.2y |
| HLICF | -2.90% | valuation:small_discount; liquidity:low; maturity:9.2y |
| NMB50 | -1.04% | valuation:small_discount; liquidity:low |
| MMF1 | -0.31% | valuation:small_discount; maturity:5.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 26
- NAV data age: median 30 days, max 412 days

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
