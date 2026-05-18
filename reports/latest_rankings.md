# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-18 14:01*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-18 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 27 |
| Median Discount | -9.37% |
| CONSIDER | 9 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 19 | 46.3% |
| -10% to -6% | 15 | 36.6% |
| -6% to -4% | 5 | 12.2% |
| -4% to 0% | 2 | 4.9% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 14.35 | 12.07 | -15.89% | 2.1y | high | 2d | 12.55% | 72.7 | ↓ widening | — |
| 2 | SIGS2 | Siddhartha Investment Gro | 11.53 | 10.45 | -9.37% | 3.3y | medium | 1d | 5.01% | 68.2 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.40 | -10.65% | 3.1y | medium | 1d | 4.26% | 54.9 | ↓ widening | — |
| 4 | SLCF | Sanima Large Cap Fund | 10.65 | 9.95 | -6.57% | 1.8y | medium | 2d | 0.47% | 54.9 | → stable | — |
| 5 | SEF | Siddhartha Equity Fund | 10.95 | 9.95 | -9.13% | 1.5y | medium | 6d | 3.79% | 53.8 | ↓ widening | — |
| 6 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.35 | -8.41% | 3.5y | medium | 1d | -2.04% | 50.5 | → stable | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.64 | 9.80 | -7.89% | 2.2y | high | 19d | 0.76% | 47.0 | ↓ widening | high_vol |
| 8 | CMF2 | Citizens Mutual Fund - 2 | 10.52 | 9.96 | -5.32% | 0.1y | medium | 1d | -0.94% | 46.3 | → stable | — |
| 9 | NICSF | NIC Asia Select-30 | 9.89 | 9.25 | -6.47% | 2.1y | high | 4d | -1.49% | 37.9 | ↓ widening | — |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 2 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -18.11% | maturity:5.8y |
| KDBY | -17.69% | maturity:6.2y |
| KEF | -15.65% | maturity:4.8y |
| LVF2 | -15.51% | liquidity:low; maturity:7.3y |
| LUK | -14.58% | liquidity:low; maturity:4.2y |
| SBCF | -14.37% | maturity:4.9y |
| GIBF1 | -13.52% | liquidity:low; maturity:6.2y |
| KSY | -12.73% | maturity:7.8y |
| RSY | -12.23% | maturity:9.0y |
| SIGS3 | -12.13% | maturity:7.0y |
| NICGF2 | -11.90% | maturity:4.5y |
| NSIF2 | -11.90% | maturity:6.3y |
| NMBHF2 | -11.61% | maturity:8.8y |
| SFEF | -11.29% | maturity:5.7y |
| MBLEF | -10.85% | liquidity:low; maturity:10.9y |
| RMF2 | -10.30% | maturity:7.0y |
| GBIMESY2 | -10.04% | maturity:9.2y |
| C30MF | -9.92% | liquidity:low; maturity:7.0y |
| NIBLSTF | -8.86% | liquidity:low; maturity:9.7y |
| RBBF40 | -8.86% | maturity:11.5y |
| MNMF1 | -8.84% | maturity:8.6y |
| GSY | -8.63% | maturity:8.6y |
| NIBLGF | -7.40% | maturity:6.7y |
| H8020 | -7.10% | maturity:7.4y |
| NICBF | -6.40% | liquidity:low |
| SAGF | -6.28% | maturity:7.5y |
| NIBSF2 | -5.94% | maturity:5.0y |
| MMF1 | -4.81% | maturity:5.3y |
| NBF2 | -4.49% | liquidity:low |
| NBF3 | -4.07% | maturity:5.3y |
| HLICF | -3.33% | valuation:small_discount; liquidity:low; maturity:9.3y |
| NMB50 | -2.23% | valuation:small_discount; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 20
- NAV data age: median 33 days, max 354 days

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
