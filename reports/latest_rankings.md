# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-09 12:52*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-09 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 18 |
| Median Discount | -6.97% |
| CONSIDER | 5 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 22.0% |
| -10% to -6% | 16 | 39.0% |
| -6% to -4% | 8 | 19.5% |
| -4% to 0% | 6 | 14.6% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.50 | -8.57% | 3.0y | medium | 1d | -1.24% | 71.1 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 13.69 | 12.25 | -10.52% | 2.0y | medium | 5d | -4.60% | 58.8 | → stable | — |
| 3 | SIGS2 | Siddhartha Investment Gro | 11.23 | 10.78 | -4.01% | 3.2y | high | 1d | -2.60% | 54.4 | → stable | — |
| 4 | SEF | Siddhartha Equity Fund | 10.65 | 10.00 | -6.10% | 1.4y | medium | 20d | -2.74% | 50.1 | → stable | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.41 | 9.90 | -4.90% | 2.1y | medium | 6d | -2.16% | 49.9 | ↑ narrowing | high_vol |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 8 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -14.73% | maturity:4.8y |
| LVF2 | -13.58% | maturity:7.2y |
| PRSF | -12.94% | maturity:5.8y |
| KDBY | -12.59% | maturity:6.1y |
| SFEF | -12.07% | liquidity:low; maturity:5.7y |
| LUK | -11.66% | liquidity:low; maturity:4.2y |
| NICBF | -11.56% | liquidity:low |
| KEF | -10.49% | maturity:4.8y |
| GIBF1 | -9.92% | maturity:6.1y |
| RSY | -9.89% | maturity:8.9y |
| GBIMESY2 | -9.19% | maturity:9.1y |
| MBLEF | -9.17% | maturity:10.8y |
| NSIF2 | -8.44% | maturity:6.2y |
| NICGF2 | -8.12% | maturity:4.5y |
| RBBF40 | -8.10% | liquidity:low; maturity:11.4y |
| RMF2 | -8.07% | liquidity:low; maturity:7.0y |
| SIGS3 | -7.49% | maturity:6.9y |
| SFMF | -6.99% | liquidity:low |
| C30MF | -6.97% | liquidity:low; maturity:6.9y |
| KSY | -6.83% | maturity:7.8y |
| NMBHF2 | -6.81% | maturity:8.7y |
| NIBSF2 | -6.79% | maturity:5.0y |
| H8020 | -5.94% | maturity:7.3y |
| NIBLGF | -5.53% | maturity:6.6y |
| MNMF1 | -5.50% | maturity:8.5y |
| SAGF | -5.29% | maturity:7.5y |
| NIBLSTF | -4.72% | maturity:9.7y |
| GSY | -4.49% | maturity:8.6y |
| NBF2 | -3.63% | valuation:small_discount; liquidity:low |
| NBF3 | -3.39% | valuation:small_discount; maturity:5.3y |
| MMF1 | -2.99% | valuation:small_discount; maturity:5.2y |
| SLCF | -2.32% | valuation:small_discount |
| NICSF | -2.28% | valuation:small_discount |
| CMF2 | -2.15% | valuation:small_discount; liquidity:low |
| HLICF | 1.58% | valuation:premium; liquidity:low; maturity:9.3y |
| NMB50 | 3.23% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 29
- NAV data age: median 25 days, max 376 days

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
