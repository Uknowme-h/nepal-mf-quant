# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-19 12:55*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-19 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 27 |
| Median Discount | -10.23% |
| CONSIDER | 9 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 22 | 53.7% |
| -10% to -6% | 13 | 31.7% |
| -6% to -4% | 3 | 7.3% |
| -4% to 0% | 3 | 7.3% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 14.35 | 12.01 | -16.31% | 2.1y | medium | 3d | 12.55% | 79.6 | → stable | — |
| 2 | SIGS2 | Siddhartha Investment Gro | 11.53 | 10.35 | -10.23% | 3.3y | medium | 2d | 5.01% | 66.3 | → stable | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.26 | -11.98% | 3.1y | medium | 2d | 4.26% | 59.5 | ↓ widening | — |
| 4 | SLCF | Sanima Large Cap Fund | 10.65 | 9.96 | -6.48% | 1.8y | high | 3d | 0.47% | 58.4 | → stable | — |
| 5 | SEF | Siddhartha Equity Fund | 10.95 | 9.95 | -9.13% | 1.5y | high | 7d | 3.79% | 57.0 | ↓ widening | — |
| 6 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.90 | -5.44% | 3.0y | high | 1d | 0.48% | 48.7 | ↓ widening | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.64 | 9.92 | -6.77% | 2.2y | high | 20d | 0.76% | 46.2 | ↓ widening | high_vol |
| 8 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.40 | -7.96% | 3.5y | medium | 2d | -2.04% | 43.9 | ↓ widening | — |
| 9 | NICSF | NIC Asia Select-30 | 9.89 | 9.25 | -6.47% | 2.1y | high | 5d | -1.49% | 36.6 | ↓ widening | — |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -18.11% | maturity:5.8y |
| KEF | -16.98% | maturity:4.8y |
| KDBY | -16.30% | maturity:6.2y |
| LVF2 | -16.21% | liquidity:low; maturity:7.3y |
| SBCF | -14.46% | maturity:4.8y |
| LUK | -14.24% | liquidity:low; maturity:4.2y |
| SIGS3 | -13.27% | liquidity:low; maturity:7.0y |
| MBLEF | -12.35% | maturity:10.9y |
| RSY | -11.97% | maturity:9.0y |
| KSY | -11.72% | maturity:7.8y |
| SFEF | -11.55% | liquidity:low; maturity:5.7y |
| NMBHF2 | -11.52% | maturity:8.8y |
| NSIF2 | -11.49% | liquidity:low; maturity:6.3y |
| NICGF2 | -11.43% | maturity:4.5y |
| C30MF | -11.28% | liquidity:low; maturity:7.0y |
| MNMF1 | -11.03% | maturity:8.6y |
| GIBF1 | -10.85% | maturity:6.2y |
| RMF2 | -10.30% | liquidity:low; maturity:7.0y |
| GBIMESY2 | -10.04% | maturity:9.2y |
| NIBLGF | -9.58% | liquidity:low; maturity:6.7y |
| GSY | -8.82% | maturity:8.6y |
| NIBSF2 | -8.42% | maturity:5.0y |
| NICBF | -8.31% | liquidity:low |
| SAGF | -7.64% | maturity:7.5y |
| RBBF40 | -7.01% | maturity:11.5y |
| NIBLSTF | -6.97% | maturity:9.7y |
| H8020 | -6.32% | maturity:7.4y |
| CMF2 | -5.32% | liquidity:low |
| MMF1 | -4.31% | maturity:5.3y |
| HLICF | -3.43% | valuation:small_discount; maturity:9.3y |
| NBF3 | -3.29% | valuation:small_discount; maturity:5.3y |
| NMB50 | -2.14% | valuation:small_discount |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 27
- NAV data age: median 34 days, max 355 days

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
