# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-26 12:50*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-26 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 24 |
| Median Discount | -9.19% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 14 | 34.1% |
| -10% to -6% | 18 | 43.9% |
| -6% to -4% | 6 | 14.6% |
| -4% to 0% | 2 | 4.9% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 14.35 | 12.30 | -14.29% | 2.1y | medium | 8d | 12.55% | 72.6 | ↑ narrowing | — |
| 2 | SIGS2 | Siddhartha Investment Gro | 11.53 | 10.82 | -6.16% | 3.2y | high | 1d | 5.01% | 67.8 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.55 | -9.22% | 3.1y | medium | 1d | 4.26% | 63.3 | ↑ narrowing | — |
| 4 | SEF | Siddhartha Equity Fund | 10.95 | 10.19 | -6.94% | 1.4y | high | 12d | 3.79% | 62.3 | ↑ narrowing | — |
| 5 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.75 | -6.88% | 3.3y | medium | 1d | 4.39% | 50.5 | ↑ narrowing | high_vol |
| 6 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.00 | -4.49% | 3.0y | medium | 3d | 0.48% | 45.7 | ↑ narrowing | — |
| 7 | SLCF | Sanima Large Cap Fund | 10.65 | 10.05 | -5.63% | 1.8y | medium | 4d | 0.47% | 44.4 | ↑ narrowing | — |
| 8 | RMF1 | RBB Mutual Fund 1 | 10.64 | 10.05 | -5.55% | 2.2y | medium | 25d | 0.76% | 40.0 | ↑ narrowing | high_vol |

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
| PRSF | -18.49% | maturity:5.8y |
| KDBY | -16.52% | maturity:6.2y |
| KEF | -14.41% | maturity:4.8y |
| LVF2 | -13.06% | maturity:7.3y |
| LUK | -12.52% | liquidity:low; maturity:4.2y |
| SBCF | -11.99% | maturity:4.8y |
| MBLEF | -11.55% | maturity:10.8y |
| NSIF2 | -11.40% | maturity:6.3y |
| GIBF1 | -10.93% | liquidity:low; maturity:6.2y |
| MNMF1 | -10.67% | maturity:8.6y |
| GBIMESY2 | -10.61% | maturity:9.2y |
| RMF2 | -10.30% | liquidity:low; maturity:7.0y |
| KSY | -10.15% | liquidity:low; maturity:7.8y |
| RSY | -9.80% | maturity:8.9y |
| NMBHF2 | -9.74% | maturity:8.8y |
| SFMF | -9.73% | liquidity:low |
| SIGS3 | -9.53% | maturity:6.9y |
| RBBF40 | -9.35% | maturity:11.5y |
| SFEF | -9.19% | maturity:5.7y |
| NICGF2 | -9.18% | liquidity:low; maturity:4.5y |
| C30MF | -9.01% | maturity:7.0y |
| GSY | -8.26% | maturity:8.6y |
| SAGF | -7.19% | liquidity:low; maturity:7.5y |
| NIBLSTF | -6.97% | liquidity:low; maturity:9.7y |
| NIBSF2 | -6.34% | maturity:5.0y |
| H8020 | -6.32% | maturity:7.4y |
| NIBLGF | -6.22% | maturity:6.7y |
| NICSF | -5.97% | liquidity:low |
| HLICF | -4.51% | maturity:9.3y |
| MMF1 | -4.31% | maturity:5.3y |
| NBF3 | -3.29% | valuation:small_discount; maturity:5.3y |
| CMF2 | -2.66% | valuation:small_discount |
| NMB50 | 0.74% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 23
- NAV data age: median 41 days, max 362 days

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
