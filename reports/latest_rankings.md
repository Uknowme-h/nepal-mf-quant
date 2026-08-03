# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-03 13:21*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-03 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 14 |
| Median Discount | -7.40% |
| CONSIDER | 7 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 13 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 6 | 15.0% |
| -10% to -6% | 18 | 45.0% |
| -6% to -4% | 7 | 17.5% |
| -4% to 0% | 8 | 20.0% |
| ≥ 0% (premium) | 1 | 2.5% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.25 | -9.29% | 3.3y | medium | 2d | -2.04% | 68.0 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 13.69 | 12.00 | -12.34% | 1.9y | medium | 43d | -4.60% | 62.6 | ↓ widening | — |
| 3 | NICSF | NIC Asia Select-30 | 9.55 | 9.00 | -5.76% | 1.9y | high | 7d | -2.55% | 59.2 | ↑ narrowing | — |
| 4 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.34 | -9.32% | 2.9y | medium | 12d | 0.88% | 58.9 | ↓ widening | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.28 | 9.62 | -6.42% | 2.0y | medium | 12d | -1.63% | 51.8 | ↑ narrowing | high_vol |
| 6 | SLCF | Sanima Large Cap Fund | 10.08 | 9.61 | -4.66% | 1.6y | medium | 1d | -2.70% | 51.2 | ↑ narrowing | — |
| 7 | SEF | Siddhartha Equity Fund | 10.36 | 9.79 | -5.50% | 1.3y | high | 5d | -2.72% | 43.9 | ↓ widening | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 9 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -16.23% | maturity:4.7y |
| PRSF | -13.21% | liquidity:low; maturity:5.6y |
| SFEF | -11.64% | maturity:5.5y |
| LVF2 | -11.13% | liquidity:low; maturity:7.1y |
| NICGF2 | -11.06% | maturity:4.3y |
| LUK | -9.95% | maturity:4.0y |
| RMF2 | -9.76% | liquidity:low; maturity:6.8y |
| NIBSF2 | -9.64% | maturity:4.8y |
| KEF | -9.09% | maturity:4.6y |
| NICBF | -8.91% | liquidity:low |
| NSIF2 | -8.49% | liquidity:low; maturity:6.1y |
| NIBLSTF | -7.94% | maturity:9.5y |
| KDBY | -7.91% | maturity:6.0y |
| SIGS3 | -7.78% | liquidity:low; maturity:6.8y |
| MBLEF | -7.74% | liquidity:low; maturity:10.7y |
| RSY | -7.62% | liquidity:low; maturity:8.8y |
| GIBF1 | -7.47% | maturity:6.0y |
| RBBF40 | -7.34% | maturity:11.3y |
| NMBHF2 | -6.77% | maturity:8.6y |
| GBIMESY2 | -6.34% | maturity:9.0y |
| H8020 | -5.42% | liquidity:low; maturity:7.2y |
| MNMF1 | -4.99% | maturity:8.4y |
| KSY | -4.28% | maturity:7.6y |
| C30MF | -4.08% | maturity:6.8y |
| NBF3 | -3.78% | valuation:small_discount; maturity:5.1y |
| MMF1 | -3.27% | valuation:small_discount; maturity:5.1y |
| NBF2 | -3.15% | valuation:small_discount; liquidity:low |
| HLICF | -2.52% | valuation:small_discount; maturity:9.1y |
| SAGF | -1.33% | valuation:small_discount; maturity:7.3y |
| GSY | -0.40% | valuation:small_discount; maturity:8.4y |
| SIGS2 | -0.37% | valuation:small_discount |
| NIBLGF | -0.10% | valuation:small_discount; maturity:6.5y |
| NMB50 | 0.48% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 45
- Symbols with issues: 24
- NAV data age: median 0 days, max 431 days

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
