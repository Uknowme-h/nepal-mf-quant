# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-20 10:58*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-19 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 37 |
| At Premium (price ≥ NAV) | 4 |
| Deep Discount (≤ -8%) | 4 |
| Median Discount | -4.53% |
| CONSIDER | 4 |
| IGNORE | 37 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 3 | 7.3% |
| -10% to -6% | 7 | 17.1% |
| -6% to -4% | 15 | 36.6% |
| -4% to 0% | 12 | 29.3% |
| ≥ 0% (premium) | 4 | 9.8% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.02 | -4.30% | 3.2y | high | 1d | 0.48% | 67.9 | ↑ narrowing | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.60 | -6.19% | 3.6y | medium | 1d | -2.04% | 64.9 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.09 | 9.43 | -6.54% | 3.2y | medium | 1d | 0.70% | 62.2 | → stable | — |
| 4 | SIGS2 | Siddhartha Investment Gro | 10.44 | 10.01 | -4.12% | 3.4y | medium | 4d | 0.29% | 51.6 | ↓ widening | — |

## IGNORE Summary

*37 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 16 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -14.81% | maturity:5.0y |
| LUK | -14.24% | liquidity:low; maturity:4.4y |
| LVF2 | -12.27% | maturity:7.5y |
| SFEF | -8.31% | maturity:5.9y |
| GIBF1 | -6.45% | liquidity:low; maturity:6.4y |
| MNMF1 | -6.17% | maturity:8.8y |
| PRSF | -6.09% | maturity:6.0y |
| NMBHF2 | -6.08% | maturity:8.9y |
| MBLEF | -5.67% | liquidity:low; maturity:11.0y |
| RMF2 | -5.50% | maturity:7.2y |
| NSIF2 | -5.42% | maturity:6.5y |
| KDBY | -5.22% | maturity:6.4y |
| GBIMESY2 | -5.15% | liquidity:low; maturity:9.3y |
| NICGF2 | -5.12% | maturity:4.7y |
| SAGF | -4.84% | liquidity:low; maturity:7.7y |
| SIGS3 | -4.63% | liquidity:low; maturity:7.1y |
| NBF3 | -4.55% | maturity:5.5y |
| GSY | -4.53% | maturity:8.8y |
| C30MF | -4.53% | maturity:7.2y |
| NIBLGF | -4.39% | maturity:6.8y |
| KSY | -4.20% | maturity:8.0y |
| PSF | -3.98% | valuation:small_discount |
| H8020 | -3.63% | valuation:small_discount; maturity:7.5y |
| NIBSF2 | -3.46% | valuation:small_discount; maturity:5.2y |
| RBBF40 | -3.03% | valuation:small_discount; liquidity:low; maturity:11.7y |
| RSY | -2.97% | valuation:small_discount; maturity:9.1y |
| NIBLSTF | -2.87% | valuation:small_discount; maturity:9.9y |
| SLCF | -2.56% | valuation:small_discount |
| HLICF | -2.30% | valuation:small_discount; liquidity:low; maturity:9.5y |
| RMF1 | -2.09% | valuation:small_discount |
| KEF | -1.88% | valuation:small_discount; maturity:5.0y |
| MMF1 | -1.57% | valuation:small_discount; maturity:5.5y |
| CMF2 | -0.58% | valuation:small_discount |
| SEF | 0.50% | valuation:premium |
| NMB50 | 0.58% | valuation:premium; liquidity:low |
| NICSF | 0.73% | valuation:premium |
| NICBF | 1.30% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 8
- NAV data age: median 33 days, max 295 days

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
