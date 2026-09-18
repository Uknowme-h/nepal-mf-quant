# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-18 14:30*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-18 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 30 |
| Median Discount | -12.28% |
| CONSIDER | 6 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 26 | 66.7% |
| -10% to -6% | 9 | 23.1% |
| -6% to -4% | 1 | 2.6% |
| -4% to 0% | 3 | 7.7% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.09 | 11.00 | -15.97% | 1.8y | high | 73d | 0.38% | 78.5 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.90 | -13.59% | 2.7y | medium | 1d | 0.88% | 66.3 | ↑ narrowing | — |
| 3 | LUK | Laxmi Unnati Kosh | 11.66 | 9.50 | -18.52% | 3.9y | medium | 2d | -1.17% | 66.3 | → stable | — |
| 4 | SLCF | Sanima Large Cap Fund | 10.14 | 9.25 | -8.78% | 1.4y | medium | 1d | -2.12% | 54.4 | ↑ narrowing | — |
| 5 | SEF | Siddhartha Equity Fund | 10.36 | 9.61 | -7.24% | 1.1y | high | 21d | -2.72% | 45.0 | → stable | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.31 | 9.42 | -8.63% | 1.9y | high | 15d | -1.63% | 43.9 | ↓ widening | high_vol |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -21.17% | liquidity:low; maturity:5.4y |
| SFMF | -20.71% | liquidity:low |
| LVF2 | -19.81% | liquidity:low; maturity:7.0y |
| SBCF | -17.99% | maturity:4.5y |
| NICGF2 | -16.35% | maturity:4.2y |
| KDBY | -15.97% | maturity:5.8y |
| RSY | -15.53% | liquidity:low; maturity:8.6y |
| KEF | -15.23% | maturity:4.5y |
| MBLEF | -15.19% | maturity:10.5y |
| NMBHF2 | -14.97% | maturity:8.4y |
| PRSF | -14.93% | maturity:5.5y |
| NSIF2 | -14.46% | maturity:6.0y |
| NIBSF2 | -13.30% | maturity:4.7y |
| SIGS2 | -13.24% | liquidity:low |
| KSY | -12.79% | liquidity:low; maturity:7.5y |
| MNMF1 | -12.46% | maturity:8.3y |
| NIBLSTF | -12.28% | maturity:9.4y |
| NICBF | -11.24% | liquidity:low |
| NBF2 | -11.08% | liquidity:low |
| RBBF40 | -10.63% | maturity:11.2y |
| SIGS3 | -10.56% | maturity:6.6y |
| NICSF | -10.23% | liquidity:low |
| SAGF | -10.21% | liquidity:low; maturity:7.2y |
| NIBLGF | -9.74% | maturity:6.3y |
| MMF1 | -8.16% | maturity:5.0y |
| GBIMESY2 | -7.75% | maturity:8.8y |
| GSY | -7.63% | maturity:8.3y |
| RMF2 | -6.78% | maturity:6.7y |
| NBF3 | -6.20% | maturity:5.0y |
| C30MF | -5.66% | maturity:6.7y |
| HLICF | -3.34% | valuation:small_discount; maturity:9.0y |
| H8020 | -0.16% | valuation:small_discount; maturity:7.0y |
| GIBF1 | 0.00% | valuation:premium; maturity:5.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 26
- NAV data age: median 34 days, max 477 days

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
