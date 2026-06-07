# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-07 12:03*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-05 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 16 |
| Median Discount | -6.92% |
| CONSIDER | 5 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 7 | 17.1% |
| -10% to -6% | 20 | 48.8% |
| -6% to -4% | 4 | 9.8% |
| -4% to 0% | 8 | 19.5% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 12.50 | -8.69% | 2.0y | high | 3d | -4.60% | 67.4 | → stable | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.54 | -8.18% | 3.0y | medium | 7d | -1.24% | 61.5 | → stable | — |
| 3 | NICBF | NIC ASIA Balanced Fund | 10.38 | 9.75 | -6.07% | 3.2y | medium | 1d | -0.86% | 54.1 | → stable | high_vol |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.41 | 9.66 | -7.20% | 2.1y | high | 4d | -2.16% | 51.0 | ↓ widening | high_vol |
| 5 | SEF | Siddhartha Equity Fund | 10.65 | 9.97 | -6.38% | 1.4y | medium | 18d | -2.74% | 44.8 | ↓ widening | — |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -15.43% | maturity:4.8y |
| LUK | -14.75% | liquidity:low; maturity:4.2y |
| LVF2 | -12.71% | maturity:7.2y |
| PRSF | -12.47% | maturity:5.8y |
| KDBY | -11.42% | maturity:6.1y |
| SFEF | -11.29% | maturity:5.7y |
| NICGF2 | -10.60% | maturity:4.5y |
| SFMF | -9.65% | liquidity:low |
| KEF | -9.24% | maturity:4.8y |
| RSY | -8.75% | maturity:8.9y |
| NSIF2 | -8.44% | maturity:6.2y |
| GIBF1 | -8.26% | maturity:6.2y |
| NMBHF2 | -8.14% | maturity:8.7y |
| GBIMESY2 | -8.11% | liquidity:low; maturity:9.1y |
| KSY | -7.50% | maturity:7.8y |
| MBLEF | -7.36% | maturity:10.8y |
| C30MF | -6.97% | liquidity:low; maturity:7.0y |
| RBBF40 | -6.92% | maturity:11.4y |
| MNMF1 | -6.64% | maturity:8.6y |
| NIBSF2 | -6.59% | maturity:5.0y |
| SAGF | -6.22% | liquidity:low; maturity:7.5y |
| RMF2 | -6.17% | liquidity:low; maturity:7.0y |
| NIBLSTF | -5.54% | maturity:9.7y |
| NIBLGF | -5.43% | maturity:6.6y |
| SIGS3 | -5.38% | maturity:6.9y |
| GSY | -4.30% | maturity:8.6y |
| SIGS2 | -3.83% | valuation:small_discount |
| H8020 | -3.72% | valuation:small_discount; liquidity:low; maturity:7.3y |
| SLCF | -3.29% | valuation:small_discount; liquidity:low |
| NICSF | -3.21% | valuation:small_discount |
| NBF3 | -2.81% | valuation:small_discount; maturity:5.3y |
| MMF1 | -2.58% | valuation:small_discount; maturity:5.3y |
| CMF2 | -2.25% | valuation:small_discount; liquidity:low |
| NBF2 | -0.96% | valuation:small_discount; liquidity:low |
| NMB50 | 4.27% | valuation:premium |
| HLICF | 5.53% | valuation:premium; maturity:9.3y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 23
- NAV data age: median 23 days, max 374 days

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
