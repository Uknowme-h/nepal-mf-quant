# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-11 10:56*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-10 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 21 |
| Median Discount | -8.05% |
| CONSIDER | 9 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 11 | 26.8% |
| -10% to -6% | 18 | 43.9% |
| -6% to -4% | 7 | 17.1% |
| -4% to 0% | 4 | 9.8% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.45 | -10.17% | 3.2y | medium | 8d | 4.26% | 62.0 | ↑ narrowing | — |
| 2 | SLCF | Sanima Large Cap Fund | 10.60 | 9.96 | -6.04% | 1.9y | medium | 3d | 4.43% | 58.2 | ↑ narrowing | — |
| 3 | PSF | Prabhu Select Fund | 12.75 | 12.20 | -4.31% | 2.2y | high | 10d | 5.81% | 55.1 | ↑ narrowing | — |
| 4 | NICSF | NIC Asia Select-30 | 10.04 | 9.30 | -7.37% | 2.2y | medium | 3d | 5.35% | 54.8 | ↑ narrowing | — |
| 5 | SEF | Siddhartha Equity Fund | 10.55 | 9.90 | -6.16% | 1.6y | medium | 8d | 4.98% | 52.4 | ↑ narrowing | high_vol |
| 6 | SIGS2 | Siddhartha Investment Gro | 10.98 | 10.06 | -8.38% | 3.4y | medium | 3d | 5.17% | 52.3 | ↓ widening | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.71 | -8.05% | 2.3y | medium | 8d | 5.28% | 51.6 | ↑ narrowing | high_vol |
| 8 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.42 | -10.03% | 3.4y | high | 2d | 4.39% | 49.5 | ↓ widening | high_vol |
| 9 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.00 | -4.49% | 3.1y | medium | 1d | 0.48% | 39.0 | → stable | — |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 5 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -15.52% | liquidity:low; maturity:4.3y |
| SBCF | -14.11% | maturity:5.0y |
| LVF2 | -13.23% | maturity:7.4y |
| SFEF | -12.07% | maturity:5.8y |
| NICGF2 | -11.15% | maturity:4.6y |
| MBLEF | -10.91% | maturity:11.0y |
| NSIF2 | -10.90% | maturity:6.4y |
| KSY | -10.33% | liquidity:low; maturity:8.0y |
| GIBF1 | -10.10% | maturity:6.3y |
| GBIMESY2 | -9.90% | liquidity:low; maturity:9.3y |
| NIBLSTF | -9.55% | maturity:9.8y |
| RMF2 | -9.32% | maturity:7.1y |
| C30MF | -9.00% | liquidity:low; maturity:7.1y |
| MNMF1 | -8.84% | maturity:8.7y |
| RSY | -8.77% | maturity:9.1y |
| SIGS3 | -8.55% | liquidity:low; maturity:7.1y |
| GSY | -8.11% | maturity:8.7y |
| NIBLGF | -7.89% | maturity:6.8y |
| NIBSF2 | -7.61% | maturity:5.1y |
| RBBF40 | -7.43% | liquidity:low; maturity:11.6y |
| NMBHF2 | -7.07% | maturity:8.9y |
| SAGF | -6.02% | maturity:7.6y |
| H8020 | -5.41% | liquidity:low; maturity:7.5y |
| SFMF | -5.22% | liquidity:low |
| MMF1 | -4.63% | maturity:5.4y |
| NMB50 | -4.60% | liquidity:low |
| HLICF | -4.25% | maturity:9.4y |
| CMF2 | -3.86% | valuation:small_discount; liquidity:low |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.5y |
| PRSF | -1.46% | valuation:small_discount; maturity:5.9y |
| KEF | -0.66% | valuation:small_discount; maturity:4.9y |
| KDBY | 1.58% | valuation:premium; maturity:6.3y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 17
- NAV data age: median 27 days, max 317 days

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
