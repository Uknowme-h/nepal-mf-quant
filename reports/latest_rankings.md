# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-08 14:24*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-08 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 18 |
| Median Discount | -7.36% |
| CONSIDER | 3 |
| IGNORE | 38 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 8 | 19.5% |
| -10% to -6% | 19 | 46.3% |
| -6% to -4% | 4 | 9.8% |
| -4% to 0% | 8 | 19.5% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 12.30 | -10.15% | 2.0y | high | 4d | -4.60% | 75.2 | ↑ narrowing | — |
| 2 | RMF1 | RBB Mutual Fund 1 | 10.41 | 9.71 | -6.72% | 2.1y | high | 5d | -2.16% | 49.0 | ↓ widening | high_vol |
| 3 | SEF | Siddhartha Equity Fund | 10.65 | 9.93 | -6.76% | 1.4y | high | 19d | -2.74% | 47.6 | ↓ widening | — |

## IGNORE Summary

*38 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -15.17% | maturity:4.8y |
| LVF2 | -13.23% | maturity:7.2y |
| KDBY | -12.90% | maturity:6.1y |
| PRSF | -12.40% | liquidity:low; maturity:5.8y |
| SFEF | -12.25% | maturity:5.7y |
| LUK | -11.66% | maturity:4.2y |
| NICFC | -10.49% | liquidity:low |
| GIBF1 | -9.84% | maturity:6.1y |
| RSY | -9.81% | maturity:8.9y |
| SFMF | -9.65% | liquidity:low |
| KEF | -9.58% | maturity:4.8y |
| NSIF2 | -9.45% | maturity:6.2y |
| NICBF | -8.86% | liquidity:low |
| NMBHF2 | -8.70% | maturity:8.7y |
| NICGF2 | -8.31% | maturity:4.5y |
| GBIMESY2 | -8.11% | maturity:9.1y |
| RMF2 | -8.07% | liquidity:low; maturity:7.0y |
| SIGS3 | -7.49% | maturity:6.9y |
| KSY | -7.40% | liquidity:low; maturity:7.8y |
| MBLEF | -7.36% | maturity:10.8y |
| MNMF1 | -7.11% | maturity:8.5y |
| C30MF | -7.06% | maturity:6.9y |
| RBBF40 | -6.13% | maturity:11.4y |
| SAGF | -6.04% | liquidity:low; maturity:7.5y |
| NIBSF2 | -5.98% | maturity:5.0y |
| H8020 | -5.94% | liquidity:low; maturity:7.3y |
| NIBLGF | -5.53% | maturity:6.6y |
| GSY | -4.39% | maturity:8.6y |
| SIGS2 | -3.83% | valuation:small_discount; liquidity:low |
| NICSF | -3.62% | valuation:small_discount |
| NIBLSTF | -3.29% | valuation:small_discount; maturity:9.7y |
| SLCF | -3.09% | valuation:small_discount |
| NBF3 | -2.81% | valuation:small_discount; maturity:5.3y |
| CMF2 | -2.15% | valuation:small_discount |
| MMF1 | -2.06% | valuation:small_discount; maturity:5.2y |
| NBF2 | -0.67% | valuation:small_discount |
| HLICF | 2.03% | valuation:premium; maturity:9.3y |
| NMB50 | 4.27% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 23
- NAV data age: median 24 days, max 375 days

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
