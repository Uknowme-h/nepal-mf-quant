# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-10 11:01*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-10 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 9 |
| Median Discount | -5.48% |
| CONSIDER | 4 |
| IGNORE | 37 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 4 | 9.8% |
| -10% to -6% | 13 | 31.7% |
| -6% to -4% | 15 | 36.6% |
| -4% to 0% | 6 | 14.6% |
| ≥ 0% (premium) | 3 | 7.3% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 12.05 | 11.39 | -5.48% | 2.3y | high | 10d | 0.17% | 64.3 | ↑ narrowing | — |
| 2 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.00 | -4.49% | 3.2y | high | 7d | 0.48% | 57.0 | ↑ narrowing | — |
| 3 | SIGS2 | Siddhartha Investment Gro | 10.44 | 9.70 | -7.09% | 3.5y | medium | 2d | 0.29% | 56.8 | ↓ widening | — |
| 4 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.26 | -9.20% | 3.7y | medium | 2d | -2.04% | 55.1 | → stable | — |

## IGNORE Summary

*37 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 9 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -15.95% | liquidity:low; maturity:4.4y |
| LVF2 | -13.94% | maturity:7.5y |
| SBCF | -12.70% | maturity:5.0y |
| SFEF | -11.64% | maturity:5.9y |
| NICBF | -9.76% | liquidity:low |
| GIBF1 | -9.08% | maturity:6.4y |
| NICGF2 | -8.28% | liquidity:low; maturity:4.7y |
| PRSF | -8.12% | maturity:6.0y |
| KSY | -7.62% | liquidity:low; maturity:8.0y |
| KDBY | -7.14% | maturity:6.4y |
| NIBSF2 | -7.13% | maturity:5.2y |
| NICFC | -6.69% | liquidity:low |
| RMF2 | -6.44% | maturity:7.2y |
| C30MF | -6.32% | liquidity:low; maturity:7.2y |
| RBBF40 | -6.26% | maturity:11.7y |
| GSY | -5.59% | maturity:8.8y |
| MNMF1 | -5.59% | maturity:8.8y |
| NBF3 | -5.52% | maturity:5.5y |
| SIGS3 | -5.47% | liquidity:low; maturity:7.2y |
| KEF | -5.46% | maturity:5.0y |
| GBIMESY2 | -5.45% | maturity:9.4y |
| SLCF | -5.42% | liquidity:low |
| NMBHF2 | -5.30% | maturity:9.0y |
| RSY | -5.29% | maturity:9.2y |
| NSIF2 | -5.16% | maturity:6.5y |
| MBLEF | -4.66% | maturity:11.1y |
| NIBLSTF | -4.20% | maturity:9.9y |
| SAGF | -4.10% | maturity:7.7y |
| RMF1 | -3.79% | valuation:small_discount |
| H8020 | -2.64% | valuation:small_discount; liquidity:low; maturity:7.6y |
| SEF | -1.49% | valuation:small_discount |
| HLICF | -1.15% | valuation:small_discount; liquidity:low; maturity:9.5y |
| NICSF | -0.42% | valuation:small_discount |
| MMF1 | -0.31% | valuation:small_discount; maturity:5.5y |
| CMF2 | 0.39% | valuation:premium |
| NMB50 | 4.17% | valuation:premium |
| NIBLGF | 5.21% | valuation:premium; maturity:6.9y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 9
- NAV data age: median 23 days, max 285 days

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
