# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-02 14:28*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-02 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 31 |
| Median Discount | -12.78% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 17 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 30 | 76.9% |
| -10% to -6% | 7 | 17.9% |
| -6% to -4% | 2 | 5.1% |
| -4% to 0% | 0 | 0.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.75 | -15.05% | 2.8y | medium | 2d | 0.88% | 68.2 | ↓ widening | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.35 | -17.26% | 3.2y | medium | 2d | -2.04% | 67.2 | ↓ widening | — |
| 3 | SEF | Siddhartha Equity Fund | 10.36 | 9.27 | -10.52% | 1.2y | high | 11d | -2.72% | 63.0 | → stable | — |
| 4 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.80 | -6.40% | 2.8y | high | 1d | 0.48% | 60.5 | → stable | — |
| 5 | SIGS2 | Siddhartha Investment Gro | 10.95 | 9.74 | -11.05% | 3.0y | high | 4d | -3.30% | 52.6 | ↓ widening | — |
| 6 | PSF | Prabhu Select Fund | 13.04 | 12.01 | -7.90% | 1.8y | medium | 63d | -4.26% | 49.7 | ↓ widening | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.31 | 9.02 | -12.51% | 1.9y | medium | 5d | -1.63% | 49.1 | ↓ widening | high_vol |
| 8 | NICSF | NIC Asia Select-30 | 9.48 | 8.52 | -10.13% | 1.8y | medium | 1d | -3.27% | 46.8 | ↓ widening | — |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -20.46% | maturity:4.6y |
| LVF2 | -18.76% | maturity:7.0y |
| KDBY | -18.39% | maturity:5.9y |
| NMBHF2 | -18.13% | maturity:8.5y |
| MBLEF | -17.29% | maturity:10.6y |
| RSY | -16.86% | liquidity:low; maturity:8.7y |
| LUK | -16.81% | liquidity:low |
| NICGF2 | -16.35% | liquidity:low; maturity:4.2y |
| NICBF | -15.79% | liquidity:low |
| NIBSF2 | -15.43% | maturity:4.7y |
| RMF2 | -14.94% | liquidity:low; maturity:6.7y |
| KSY | -14.34% | liquidity:low; maturity:7.5y |
| NSIF2 | -14.24% | maturity:6.0y |
| SFEF | -13.82% | maturity:5.5y |
| NIBLSTF | -13.75% | maturity:9.4y |
| KEF | -13.62% | maturity:4.5y |
| SIGS3 | -13.42% | liquidity:low; maturity:6.7y |
| NIBLGF | -12.78% | maturity:6.4y |
| MNMF1 | -12.56% | maturity:8.3y |
| NBF3 | -11.72% | maturity:5.1y |
| GIBF1 | -11.04% | maturity:5.9y |
| GBIMESY2 | -10.47% | maturity:8.9y |
| SLCF | -10.26% | liquidity:low |
| GSY | -10.24% | maturity:8.3y |
| PRSF | -9.48% | maturity:5.5y |
| RBBF40 | -7.94% | liquidity:low; maturity:11.2y |
| H8020 | -7.34% | liquidity:low; maturity:7.1y |
| MMF1 | -6.90% | maturity:5.0y |
| C30MF | -6.13% | maturity:6.7y |
| SAGF | -5.12% | maturity:7.2y |
| HLICF | -4.49% | maturity:9.0y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 35
- NAV data age: median 18 days, max 461 days

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
