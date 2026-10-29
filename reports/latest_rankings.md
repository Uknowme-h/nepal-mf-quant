# Nepal MF Quant — Full Analysis Report

*Generated: 2026-10-29 16:56*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-10-29 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 17 |
| Median Discount | -7.16% |
| CONSIDER | 9 |
| IGNORE | 30 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 23.1% |
| -10% to -6% | 18 | 46.2% |
| -6% to -4% | 9 | 23.1% |
| -4% to 0% | 3 | 7.7% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.23 | -11.84% | 2.6y | high | 2d | 0.48% | 74.9 | ↑ narrowing | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.52 | -15.75% | 3.0y | high | 3d | -2.04% | 70.0 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 9.94 | 9.26 | -6.84% | 2.6y | medium | 4d | -1.29% | 57.7 | ↑ narrowing | — |
| 4 | LUK | Laxmi Unnati Kosh | 11.66 | 9.84 | -15.61% | 3.8y | medium | 2d | -1.17% | 56.7 | → stable | — |
| 5 | PSF | Prabhu Select Fund | 12.00 | 11.22 | -6.50% | 1.6y | medium | 10d | -8.33% | 54.5 | ↑ narrowing | — |
| 6 | SLCF | Sanima Large Cap Fund | 10.04 | 9.45 | -5.88% | 1.3y | medium | 1d | -0.99% | 54.2 | ↑ narrowing | — |
| 7 | SEF | Siddhartha Equity Fund | 10.49 | 9.94 | -5.24% | 1.0y | high | 11d | 1.06% | 54.1 | ↑ narrowing | — |
| 8 | RMF1 | RBB Mutual Fund 1 | 10.22 | 9.31 | -8.90% | 1.7y | medium | 18d | -0.87% | 53.2 | → stable | high_vol |
| 9 | NICSF | NIC Asia Select-30 | 9.28 | 8.80 | -5.17% | 1.7y | high | 20d | -2.11% | 49.7 | ↑ narrowing | high_vol |

## IGNORE Summary

*30 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -19.25% | liquidity:low; maturity:5.3y |
| SBCF | -17.99% | liquidity:low; maturity:4.4y |
| LVF2 | -17.62% | liquidity:low; maturity:6.8y |
| GIBF1 | -12.27% | maturity:5.8y |
| RMF2 | -11.19% | liquidity:low; maturity:6.6y |
| NBF3 | -10.85% | maturity:4.9y |
| H8020 | -9.82% | liquidity:low; maturity:6.9y |
| NIBSF2 | -9.05% | maturity:4.6y |
| NICGF2 | -8.31% | maturity:4.1y |
| RBBF40 | -8.31% | maturity:11.1y |
| C30MF | -8.04% | maturity:6.5y |
| MNMF1 | -8.01% | maturity:8.2y |
| GBIMESY2 | -8.00% | liquidity:low; maturity:8.7y |
| NIBLGF | -7.93% | maturity:6.2y |
| NICBF | -7.69% | liquidity:low |
| KSY | -7.16% | maturity:7.4y |
| GSY | -7.00% | maturity:8.2y |
| RSY | -6.73% | maturity:8.5y |
| NIBLSTF | -6.46% | maturity:9.3y |
| SAGF | -6.40% | liquidity:low; maturity:7.1y |
| KEF | -6.17% | maturity:4.4y |
| KDBY | -5.79% | maturity:5.7y |
| MMF1 | -5.79% | maturity:4.9y |
| MBLEF | -5.33% | maturity:10.4y |
| PRSF | -5.15% | maturity:5.4y |
| NMBHF2 | -5.14% | maturity:8.3y |
| SIGS2 | -4.07% | liquidity:low |
| NSIF2 | -3.89% | valuation:small_discount; maturity:5.8y |
| HLICF | -2.45% | valuation:small_discount; liquidity:low; maturity:8.9y |
| SIGS3 | -1.12% | valuation:small_discount; maturity:6.5y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 27
- NAV data age: median 44 days, max 518 days

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
