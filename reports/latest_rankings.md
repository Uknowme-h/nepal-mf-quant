# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-26 11:37*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-24 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 25 |
| Median Discount | -8.95% |
| CONSIDER | 6 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 17 | 42.5% |
| -10% to -6% | 15 | 37.5% |
| -6% to -4% | 3 | 7.5% |
| -4% to 0% | 5 | 12.5% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 12.10 | -11.61% | 1.9y | high | 37d | -4.60% | 71.4 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.20 | -10.68% | 2.9y | medium | 6d | 0.88% | 71.0 | ↑ narrowing | — |
| 3 | NICSF | NIC Asia Select-30 | 9.80 | 9.20 | -6.12% | 1.9y | high | 1d | 1.45% | 52.6 | ↓ widening | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.70 | -7.18% | 2.0y | high | 6d | 0.38% | 52.0 | ↓ widening | high_vol |
| 5 | SEF | Siddhartha Equity Fund | 10.65 | 10.11 | -5.07% | 1.3y | medium | 1d | 0.00% | 51.2 | ↑ narrowing | — |
| 6 | SIGS2 | Siddhartha Investment Gro | 11.22 | 10.20 | -9.09% | 3.1y | medium | 1d | -0.09% | 49.4 | ↓ widening | — |

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
| LUK | -16.30% | liquidity:low; maturity:4.1y |
| LVF2 | -15.34% | liquidity:low; maturity:7.1y |
| SBCF | -15.26% | maturity:4.7y |
| KDBY | -14.00% | maturity:6.0y |
| PRSF | -13.95% | maturity:5.6y |
| SFEF | -12.95% | liquidity:low; maturity:5.6y |
| GIBF1 | -11.86% | maturity:6.0y |
| SIGS3 | -11.76% | maturity:6.8y |
| NICBF | -11.63% | liquidity:low |
| SFMF | -11.24% | liquidity:low |
| NIBSF2 | -10.88% | maturity:4.8y |
| KEF | -10.54% | maturity:4.7y |
| NSIF2 | -10.48% | liquidity:low; maturity:6.1y |
| GSY | -10.20% | maturity:8.4y |
| NIBLSTF | -10.20% | maturity:9.6y |
| NICGF2 | -9.81% | maturity:4.3y |
| KSY | -9.65% | maturity:7.7y |
| RSY | -8.81% | maturity:8.8y |
| GBIMESY2 | -8.71% | maturity:9.0y |
| MNMF1 | -8.66% | maturity:8.4y |
| RMF2 | -8.50% | liquidity:low; maturity:6.8y |
| RBBF40 | -8.18% | maturity:11.3y |
| C30MF | -7.86% | liquidity:low; maturity:6.8y |
| NIBLGF | -7.62% | liquidity:low; maturity:6.5y |
| NMBHF2 | -7.48% | maturity:8.6y |
| MBLEF | -7.44% | maturity:10.7y |
| SAGF | -6.65% | maturity:7.3y |
| H8020 | -4.91% | maturity:7.2y |
| NBF2 | -4.30% | liquidity:low |
| NBF3 | -3.39% | valuation:small_discount; maturity:5.2y |
| MMF1 | -3.17% | valuation:small_discount; maturity:5.1y |
| HLICF | -2.34% | valuation:small_discount; maturity:9.2y |
| SLCF | -1.54% | valuation:small_discount |
| NMB50 | 0.00% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 44
- Symbols with issues: 27
- NAV data age: median 41 days, max 423 days

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
