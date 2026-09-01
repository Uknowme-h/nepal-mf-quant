# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-01 14:52*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-01 |
| Funds Tracked | 38 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 31 |
| Median Discount | -12.39% |
| CONSIDER | 7 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 17 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 28 | 73.7% |
| -10% to -6% | 8 | 21.1% |
| -6% to -4% | 1 | 2.6% |
| -4% to 0% | 1 | 2.6% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.50 | -15.93% | 3.2y | medium | 1d | -2.04% | 71.2 | ↓ widening | — |
| 2 | SEF | Siddhartha Equity Fund | 10.36 | 9.45 | -8.78% | 1.2y | medium | 10d | 0.00% | 61.2 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.81 | -14.47% | 2.8y | medium | 1d | 0.88% | 57.8 | ↓ widening | — |
| 4 | NICBF | NIC ASIA Balanced Fund | 10.32 | 8.89 | -13.86% | 3.0y | high | 1d | 0.88% | 56.7 | ↓ widening | — |
| 5 | PSF | Prabhu Select Fund | 13.04 | 12.00 | -7.98% | 1.8y | high | 62d | -4.26% | 56.0 | → stable | — |
| 6 | SIGS2 | Siddhartha Investment Gro | 10.95 | 9.42 | -13.97% | 3.0y | high | 3d | -3.30% | 55.9 | ↓ widening | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.31 | 9.26 | -10.18% | 1.9y | medium | 4d | -1.63% | 47.4 | ↓ widening | high_vol |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 27 |
| liquidity | 10 |
| valuation | 1 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -21.12% | liquidity:low; maturity:7.0y |
| LUK | -19.21% | liquidity:low |
| KDBY | -18.39% | maturity:5.9y |
| MBLEF | -17.66% | maturity:10.6y |
| NMBHF2 | -16.98% | liquidity:low; maturity:8.5y |
| RSY | -16.86% | maturity:8.7y |
| NIBLGF | -16.33% | maturity:6.4y |
| KEF | -15.41% | liquidity:low; maturity:4.5y |
| NICGF2 | -15.19% | maturity:4.2y |
| NSIF2 | -14.67% | liquidity:low; maturity:6.0y |
| NIBLSTF | -14.27% | maturity:9.4y |
| SFEF | -14.00% | maturity:5.5y |
| NIBSF2 | -13.81% | maturity:4.7y |
| MNMF1 | -12.66% | maturity:8.3y |
| NICSF | -12.66% | liquidity:low |
| SIGS3 | -12.12% | maturity:6.7y |
| KSY | -11.82% | liquidity:low; maturity:7.5y |
| NBF3 | -11.63% | maturity:5.1y |
| GIBF1 | -11.12% | maturity:5.9y |
| RMF2 | -11.09% | maturity:6.7y |
| GSY | -10.34% | maturity:8.3y |
| SLCF | -10.26% | liquidity:low |
| RBBF40 | -10.23% | maturity:11.2y |
| PRSF | -9.48% | maturity:5.5y |
| GBIMESY2 | -9.26% | maturity:8.9y |
| SAGF | -7.31% | maturity:7.2y |
| NBF2 | -7.16% | liquidity:low |
| H8020 | -7.10% | maturity:7.1y |
| C30MF | -6.13% | maturity:6.7y |
| MMF1 | -5.96% | maturity:5.0y |
| HLICF | -1.61% | valuation:small_discount; liquidity:low; maturity:9.0y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 34
- NAV data age: median 17 days, max 460 days

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
