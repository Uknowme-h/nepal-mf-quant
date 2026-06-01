# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-01 16:20*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-01 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 21 |
| Median Discount | -8.11% |
| CONSIDER | 5 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 22.0% |
| -10% to -6% | 16 | 39.0% |
| -6% to -4% | 9 | 22.0% |
| -4% to 0% | 5 | 12.2% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SIGS2 | Siddhartha Investment Gro | 11.23 | 10.50 | -6.50% | 3.2y | high | 3d | -2.60% | 62.0 | → stable | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.34 | -10.11% | 3.0y | medium | 3d | -1.24% | 61.7 | ↓ widening | — |
| 3 | PSF | Prabhu Select Fund | 13.69 | 12.01 | -12.27% | 2.1y | high | 10d | -4.60% | 61.2 | ↓ widening | — |
| 4 | SEF | Siddhartha Equity Fund | 10.65 | 10.20 | -4.23% | 1.4y | medium | 14d | -2.74% | 52.0 | ↑ narrowing | — |
| 5 | NICSF | NIC Asia Select-30 | 9.66 | 9.10 | -5.80% | 2.1y | high | 2d | -2.33% | 51.3 | → stable | — |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 7 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -13.58% | maturity:4.8y |
| LUK | -12.95% | liquidity:low; maturity:4.2y |
| PRSF | -12.60% | maturity:5.8y |
| LVF2 | -12.36% | maturity:7.3y |
| SFEF | -11.46% | liquidity:low; maturity:5.7y |
| KDBY | -10.64% | maturity:6.2y |
| RSY | -10.16% | maturity:8.9y |
| SFMF | -9.73% | liquidity:low |
| KEF | -9.24% | maturity:4.8y |
| NSIF2 | -8.86% | maturity:6.3y |
| MBLEF | -8.81% | maturity:10.8y |
| NMBHF2 | -8.80% | maturity:8.8y |
| NICGF2 | -8.50% | maturity:4.5y |
| NIBSF2 | -8.41% | maturity:5.0y |
| RMF2 | -8.34% | liquidity:low; maturity:7.0y |
| GIBF1 | -8.26% | maturity:6.2y |
| NIBLGF | -8.25% | liquidity:low; maturity:6.6y |
| KSY | -8.25% | maturity:7.8y |
| GBIMESY2 | -8.11% | maturity:9.1y |
| RBBF40 | -7.61% | maturity:11.5y |
| NICBF | -6.55% | liquidity:low |
| C30MF | -6.13% | maturity:7.0y |
| SIGS3 | -5.80% | liquidity:low; maturity:6.9y |
| SAGF | -5.76% | maturity:7.5y |
| RMF1 | -5.38% | liquidity:low |
| MNMF1 | -5.31% | maturity:8.6y |
| H8020 | -5.07% | maturity:7.3y |
| GSY | -4.30% | maturity:8.6y |
| NIBLSTF | -4.11% | maturity:9.7y |
| NBF2 | -3.53% | valuation:small_discount |
| SLCF | -3.29% | valuation:small_discount |
| NBF3 | -3.20% | valuation:small_discount; maturity:5.3y |
| CMF2 | -3.13% | valuation:small_discount; liquidity:low |
| MMF1 | -2.27% | valuation:small_discount; maturity:5.3y |
| HLICF | 0.45% | valuation:premium; maturity:9.3y |
| NMB50 | 3.04% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 22
- NAV data age: median 17 days, max 368 days

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
