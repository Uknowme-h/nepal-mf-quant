# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-25 13:42*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-25 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 26 |
| Median Discount | -9.01% |
| CONSIDER | 7 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 15 | 36.6% |
| -10% to -6% | 19 | 46.3% |
| -6% to -4% | 4 | 9.8% |
| -4% to 0% | 3 | 7.3% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 14.35 | 12.30 | -14.29% | 2.1y | high | 7d | 12.55% | 84.4 | ↑ narrowing | — |
| 2 | SEF | Siddhartha Equity Fund | 10.95 | 10.09 | -7.85% | 1.5y | high | 11d | 3.79% | 61.8 | ↑ narrowing | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.64 | 10.05 | -5.55% | 2.2y | medium | 24d | 0.76% | 52.0 | ↑ narrowing | high_vol |
| 4 | SLCF | Sanima Large Cap Fund | 10.65 | 10.01 | -6.01% | 1.8y | medium | 3d | 0.47% | 48.2 | ↑ narrowing | — |
| 5 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.96 | -4.87% | 3.0y | medium | 2d | 0.48% | 43.3 | → stable | — |
| 6 | CMF2 | Citizens Mutual Fund - 2 | 10.52 | 10.01 | -4.85% | 0.1y | medium | 1d | -0.94% | 42.6 | → stable | — |
| 7 | NICSF | NIC Asia Select-30 | 9.89 | 9.20 | -6.98% | 2.1y | medium | 9d | -1.49% | 31.5 | ↓ widening | — |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -18.30% | maturity:5.8y |
| KDBY | -15.07% | maturity:6.2y |
| KEF | -14.33% | maturity:4.8y |
| LUK | -14.24% | maturity:4.2y |
| LVF2 | -12.80% | maturity:7.3y |
| SIGS3 | -12.05% | liquidity:low; maturity:6.9y |
| SBCF | -11.99% | maturity:4.8y |
| SFMF | -11.42% | liquidity:low |
| NSIF2 | -11.40% | maturity:6.3y |
| MBLEF | -11.11% | maturity:10.8y |
| NICGF2 | -10.97% | liquidity:low; maturity:4.5y |
| GIBF1 | -10.93% | maturity:6.2y |
| RSY | -10.67% | maturity:8.9y |
| GBIMESY2 | -10.04% | maturity:9.2y |
| SFEF | -9.89% | maturity:5.7y |
| NICFC | -9.70% | liquidity:low |
| RMF2 | -9.41% | maturity:7.0y |
| MNMF1 | -9.21% | maturity:8.6y |
| NMBHF2 | -9.18% | maturity:8.8y |
| C30MF | -9.01% | maturity:7.0y |
| SIGS2 | -8.93% | liquidity:low |
| KSY | -8.67% | maturity:7.8y |
| NIBSF2 | -8.42% | maturity:5.0y |
| RBBF40 | -8.37% | liquidity:low; maturity:11.5y |
| GSY | -8.17% | maturity:8.6y |
| H8020 | -7.65% | maturity:7.4y |
| NICBF | -7.55% | liquidity:low |
| SAGF | -7.19% | liquidity:low; maturity:7.5y |
| NIBLSTF | -7.17% | maturity:9.7y |
| NIBLGF | -6.91% | liquidity:low; maturity:6.7y |
| MMF1 | -4.11% | maturity:5.3y |
| HLICF | -3.86% | valuation:small_discount; maturity:9.3y |
| NBF3 | -3.49% | valuation:small_discount; maturity:5.3y |
| NMB50 | -0.56% | valuation:small_discount; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 21
- NAV data age: median 40 days, max 361 days

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
