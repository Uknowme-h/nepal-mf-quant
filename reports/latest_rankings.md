# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-29 12:18*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-29 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 25 |
| Median Discount | -8.67% |
| CONSIDER | 7 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 12 | 30.0% |
| -10% to -6% | 20 | 50.0% |
| -6% to -4% | 4 | 10.0% |
| -4% to 0% | 4 | 10.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.12 | -11.46% | 2.9y | medium | 9d | 0.88% | 60.6 | ↓ widening | — |
| 2 | PSF | Prabhu Select Fund | 13.69 | 11.85 | -13.44% | 1.9y | medium | 40d | -4.60% | 60.5 | ↓ widening | — |
| 3 | NICSF | NIC Asia Select-30 | 9.80 | 8.95 | -8.67% | 1.9y | medium | 4d | 1.45% | 58.8 | ↓ widening | — |
| 4 | SIGS2 | Siddhartha Investment Gro | 11.22 | 10.50 | -6.42% | 3.1y | medium | 4d | -0.09% | 55.2 | ↑ narrowing | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.88 | -5.45% | 2.0y | high | 9d | 0.38% | 54.8 | ↑ narrowing | high_vol |
| 6 | SEF | Siddhartha Equity Fund | 10.65 | 9.75 | -8.45% | 1.3y | high | 2d | 0.00% | 49.8 | ↓ widening | — |
| 7 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.90 | -5.44% | 2.8y | medium | 1d | 0.48% | 44.9 | ↓ widening | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -18.49% | maturity:7.1y |
| SBCF | -14.81% | maturity:4.7y |
| KEF | -13.39% | maturity:4.6y |
| KDBY | -12.74% | maturity:6.0y |
| PRSF | -12.74% | liquidity:low; maturity:5.6y |
| SFEF | -12.34% | maturity:5.5y |
| NICGF2 | -12.12% | liquidity:low; maturity:4.3y |
| NIBSF2 | -11.88% | maturity:4.8y |
| GIBF1 | -11.03% | maturity:6.0y |
| SFMF | -10.53% | liquidity:low |
| RSY | -9.96% | maturity:8.8y |
| NSIF2 | -9.89% | maturity:6.1y |
| RMF2 | -9.86% | liquidity:low; maturity:6.8y |
| SIGS3 | -9.50% | maturity:6.8y |
| NICBF | -9.50% | liquidity:low |
| NMBHF2 | -9.28% | maturity:8.6y |
| NIBLGF | -8.72% | liquidity:low; maturity:6.5y |
| RBBF40 | -8.67% | maturity:11.3y |
| NIBLSTF | -8.27% | maturity:9.5y |
| MNMF1 | -8.19% | maturity:8.4y |
| GBIMESY2 | -8.12% | maturity:9.0y |
| LUK | -7.46% | maturity:4.0y |
| MBLEF | -7.44% | maturity:10.7y |
| H8020 | -7.29% | maturity:7.2y |
| GSY | -6.86% | maturity:8.4y |
| C30MF | -6.85% | liquidity:low; maturity:6.8y |
| KSY | -6.34% | liquidity:low; maturity:7.6y |
| MMF1 | -5.93% | maturity:5.1y |
| SAGF | -4.34% | liquidity:low; maturity:7.3y |
| HLICF | -3.01% | valuation:small_discount; maturity:9.1y |
| SLCF | -2.99% | valuation:small_discount |
| NBF3 | -2.23% | valuation:small_discount; maturity:5.2y |
| NMB50 | -0.09% | valuation:small_discount; liquidity:low |

</details>

## Data Quality

- Symbols checked: 44
- Symbols with issues: 26
- NAV data age: median 44 days, max 426 days

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
