# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-03 11:04*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-02 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 18 |
| Median Discount | -7.86% |
| CONSIDER | 9 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 22.0% |
| -10% to -6% | 24 | 58.5% |
| -6% to -4% | 6 | 14.6% |
| -4% to 0% | 2 | 4.9% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SIGS2 | Siddhartha Investment Gro | 10.98 | 10.17 | -7.38% | 3.4y | medium | 3d | 5.17% | 65.1 | → stable | — |
| 2 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.75 | -7.67% | 2.3y | high | 2d | 5.28% | 61.6 | ↓ widening | high_vol |
| 3 | SLCF | Sanima Large Cap Fund | 10.60 | 9.80 | -7.55% | 1.9y | medium | 1d | 4.43% | 57.3 | ↓ widening | — |
| 4 | PSF | Prabhu Select Fund | 12.75 | 11.80 | -7.45% | 2.2y | medium | 4d | 5.81% | 57.2 | ↓ widening | — |
| 5 | NICSF | NIC Asia Select-30 | 10.04 | 9.40 | -6.37% | 2.3y | medium | 2d | 5.35% | 54.0 | ↓ widening | — |
| 6 | CMF2 | Citizens Mutual Fund - 2 | 10.62 | 10.13 | -4.61% | 0.3y | medium | 2d | 3.31% | 45.9 | ↓ widening | — |
| 7 | SEF | Siddhartha Equity Fund | 10.55 | 10.01 | -5.12% | 1.6y | high | 2d | 4.98% | 44.6 | ↓ widening | high_vol |
| 8 | NICFC | NIC Asia Flexi Cap Fund | 10.09 | 9.30 | -7.83% | 3.2y | medium | 3d | 0.70% | 39.5 | ↓ widening | — |
| 9 | NICBF | NIC ASIA Balanced Fund | 10.03 | 9.38 | -6.48% | 3.4y | medium | 2d | -0.10% | 24.7 | ↓ widening | high_vol |

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
| LUK | -16.04% | liquidity:low; maturity:4.4y |
| SBCF | -15.87% | maturity:5.0y |
| LVF2 | -13.85% | maturity:7.4y |
| GIBF1 | -12.76% | liquidity:low; maturity:6.3y |
| KSY | -10.88% | maturity:8.0y |
| SFEF | -10.76% | liquidity:low; maturity:5.9y |
| MBLEF | -10.56% | maturity:11.0y |
| NMBHF2 | -10.42% | maturity:8.9y |
| RSY | -10.10% | maturity:9.1y |
| H8020 | -9.38% | maturity:7.5y |
| MNMF1 | -9.30% | maturity:8.7y |
| C30MF | -9.09% | maturity:7.1y |
| NIBLSTF | -9.06% | maturity:9.9y |
| NSIF2 | -9.02% | maturity:6.4y |
| SIGS3 | -8.81% | liquidity:low; maturity:7.1y |
| GSY | -8.66% | maturity:8.8y |
| RMF2 | -8.61% | liquidity:low; maturity:7.1y |
| RBBF40 | -8.29% | liquidity:low; maturity:11.6y |
| KDBY | -7.98% | maturity:6.3y |
| NICGF2 | -7.88% | maturity:4.6y |
| PRSF | -7.86% | maturity:6.0y |
| SAGF | -7.39% | liquidity:low; maturity:7.7y |
| KEF | -7.30% | maturity:5.0y |
| GBIMESY2 | -7.21% | maturity:9.3y |
| SFMF | -7.08% | liquidity:low |
| NIBSF2 | -6.54% | maturity:5.2y |
| MMF1 | -5.71% | maturity:5.4y |
| NIBLGF | -5.56% | maturity:6.8y |
| NBF2 | -5.35% | liquidity:low |
| NBF3 | -4.46% | maturity:5.5y |
| NMB50 | -3.87% | valuation:small_discount; liquidity:low |
| HLICF | -1.56% | valuation:small_discount; maturity:9.5y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 26
- NAV data age: median 19 days, max 309 days

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
