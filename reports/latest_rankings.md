# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-21 12:00*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-21 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 23 |
| Median Discount | -8.82% |
| CONSIDER | 7 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 15 | 37.5% |
| -10% to -6% | 13 | 32.5% |
| -6% to -4% | 5 | 12.5% |
| -4% to 0% | 6 | 15.0% |
| ≥ 0% (premium) | 1 | 2.5% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 12.00 | -12.34% | 1.9y | high | 34d | -4.60% | 71.2 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.03 | -12.33% | 2.9y | high | 3d | 0.88% | 65.4 | ↓ widening | — |
| 3 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.30 | -8.85% | 3.3y | high | 1d | -2.04% | 58.3 | → stable | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.90 | -5.26% | 2.0y | high | 3d | 0.38% | 55.9 | ↑ narrowing | high_vol |
| 5 | SEF | Siddhartha Equity Fund | 10.65 | 10.10 | -5.16% | 1.3y | medium | 13d | 0.00% | 47.8 | ↑ narrowing | — |
| 6 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.81 | -6.30% | 2.9y | medium | 1d | 0.48% | 45.7 | ↓ widening | — |
| 7 | NICSF | NIC Asia Select-30 | 9.80 | 9.00 | -8.16% | 2.0y | medium | 12d | 1.45% | 45.4 | ↓ widening | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 7 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -14.32% | maturity:4.1y |
| LVF2 | -13.41% | maturity:7.1y |
| KDBY | -13.14% | maturity:6.0y |
| PRSF | -13.14% | maturity:5.7y |
| KEF | -12.97% | maturity:4.7y |
| NICGF2 | -12.50% | liquidity:low; maturity:4.3y |
| GIBF1 | -12.11% | maturity:6.0y |
| NICBF | -11.82% | liquidity:low |
| SBCF | -11.82% | liquidity:low; maturity:4.7y |
| SIGS3 | -11.76% | maturity:6.8y |
| SFEF | -11.64% | liquidity:low; maturity:5.6y |
| NIBLSTF | -11.53% | liquidity:low; maturity:9.6y |
| RSY | -11.01% | maturity:8.8y |
| RBBF40 | -9.56% | maturity:11.3y |
| NIBSF2 | -9.37% | maturity:4.9y |
| MBLEF | -9.26% | liquidity:low; maturity:10.7y |
| GBIMESY2 | -9.00% | liquidity:low; maturity:9.0y |
| NSIF2 | -8.80% | maturity:6.1y |
| NMBHF2 | -8.14% | maturity:8.6y |
| SIGS2 | -7.75% | liquidity:low |
| C30MF | -7.40% | maturity:6.8y |
| MNMF1 | -7.25% | maturity:8.4y |
| RMF2 | -6.87% | maturity:6.8y |
| KSY | -5.39% | maturity:7.7y |
| H8020 | -5.15% | maturity:7.2y |
| GSY | -4.67% | maturity:8.5y |
| SLCF | -3.96% | valuation:small_discount |
| MMF1 | -3.27% | valuation:small_discount; maturity:5.1y |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.2y |
| SAGF | -3.05% | valuation:small_discount; liquidity:low; maturity:7.4y |
| HLICF | -2.57% | valuation:small_discount; liquidity:low; maturity:9.2y |
| NIBLGF | -2.00% | valuation:small_discount; maturity:6.5y |
| NMB50 | 0.57% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 44
- Symbols with issues: 23
- NAV data age: median 36 days, max 418 days

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
