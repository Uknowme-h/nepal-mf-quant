# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-21 13:33*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-21 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 24 |
| Median Discount | -8.70% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 16 | 39.0% |
| -10% to -6% | 16 | 39.0% |
| -6% to -4% | 6 | 14.6% |
| -4% to 0% | 3 | 7.3% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 14.35 | 12.35 | -13.94% | 2.1y | high | 5d | 12.55% | 82.1 | ↑ narrowing | — |
| 2 | SIGS2 | Siddhartha Investment Gro | 11.53 | 10.51 | -8.85% | 3.3y | medium | 4d | 5.01% | 67.6 | ↑ narrowing | — |
| 3 | SEF | Siddhartha Equity Fund | 10.95 | 10.00 | -8.68% | 1.5y | high | 9d | 3.79% | 65.4 | ↑ narrowing | — |
| 4 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.40 | -10.65% | 3.1y | medium | 4d | 4.26% | 64.5 | ↑ narrowing | — |
| 5 | SLCF | Sanima Large Cap Fund | 10.65 | 10.13 | -4.88% | 1.8y | high | 1d | 0.47% | 58.5 | ↑ narrowing | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.64 | 9.99 | -6.11% | 2.2y | medium | 22d | 0.76% | 40.6 | → stable | high_vol |
| 7 | CMF2 | Citizens Mutual Fund - 2 | 10.52 | 9.89 | -5.99% | 0.1y | medium | 1d | -0.94% | 38.8 | ↓ widening | — |
| 8 | NICSF | NIC Asia Select-30 | 9.89 | 9.13 | -7.68% | 2.1y | medium | 7d | -1.49% | 36.5 | ↓ widening | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -18.61% | maturity:5.8y |
| KEF | -16.82% | maturity:4.8y |
| KDBY | -14.92% | maturity:6.2y |
| LUK | -14.84% | maturity:4.2y |
| LVF2 | -14.11% | liquidity:low; maturity:7.3y |
| SIGS3 | -12.38% | liquidity:low; maturity:7.0y |
| RSY | -11.88% | maturity:8.9y |
| SBCF | -11.82% | maturity:4.8y |
| MBLEF | -11.38% | maturity:10.9y |
| NSIF2 | -11.16% | maturity:6.3y |
| GIBF1 | -10.93% | maturity:6.2y |
| SFMF | -10.62% | liquidity:low |
| C30MF | -10.56% | liquidity:low; maturity:7.0y |
| SFEF | -10.15% | maturity:5.7y |
| KSY | -9.69% | liquidity:low; maturity:7.8y |
| MNMF1 | -8.84% | maturity:8.6y |
| NICGF2 | -8.81% | maturity:4.5y |
| GBIMESY2 | -8.70% | maturity:9.2y |
| GSY | -8.17% | maturity:8.6y |
| NIBSF2 | -8.02% | maturity:5.0y |
| NMBHF2 | -7.87% | maturity:8.8y |
| NICBF | -7.83% | liquidity:low |
| RBBF40 | -7.30% | maturity:11.5y |
| NIBLSTF | -7.27% | liquidity:low; maturity:9.7y |
| SAGF | -7.19% | maturity:7.5y |
| RMF2 | -6.75% | liquidity:low; maturity:7.0y |
| H8020 | -5.23% | maturity:7.4y |
| MMF1 | -5.01% | maturity:5.3y |
| NIBLGF | -4.94% | maturity:6.7y |
| NBF2 | -4.49% | liquidity:low |
| HLICF | -3.54% | valuation:small_discount; maturity:9.3y |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.3y |
| NMB50 | -0.09% | valuation:small_discount; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 24
- NAV data age: median 36 days, max 357 days

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
