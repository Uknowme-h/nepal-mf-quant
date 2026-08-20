# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-20 10:47*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-20 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 19 |
| Median Discount | -7.40% |
| CONSIDER | 10 |
| IGNORE | 30 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 14 | 35.0% |
| -10% to -6% | 13 | 32.5% |
| -6% to -4% | 10 | 25.0% |
| -4% to 0% | 3 | 7.5% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | LUK | Laxmi Unnati Kosh | 11.66 | 9.74 | -16.47% | 4.0y | medium | 1d | -1.17% | 75.9 | → stable | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.25 | -10.19% | 2.8y | medium | 2d | 0.88% | 70.5 | ↑ narrowing | — |
| 3 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.20 | -9.73% | 3.2y | high | 4d | -2.04% | 68.6 | → stable | — |
| 4 | NICBF | NIC ASIA Balanced Fund | 10.32 | 9.64 | -6.59% | 3.0y | medium | 1d | 0.88% | 58.4 | ↑ narrowing | high_vol |
| 5 | SEF | Siddhartha Equity Fund | 10.36 | 9.30 | -10.23% | 1.2y | high | 3d | -2.72% | 57.2 | ↓ widening | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.28 | 9.57 | -6.91% | 1.9y | medium | 1d | -1.63% | 55.6 | → stable | high_vol |
| 7 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.85 | -5.92% | 2.8y | medium | 1d | 0.48% | 55.4 | → stable | — |
| 8 | PSF | Prabhu Select Fund | 13.04 | 11.87 | -8.97% | 1.8y | medium | 55d | -4.26% | 54.1 | ↓ widening | — |
| 9 | NMB50 | NMB 50 | 10.45 | 10.02 | -4.11% | 0.0y | high | 4d | -1.42% | 50.0 | ↓ widening | — |
| 10 | NICSF | NIC Asia Select-30 | 9.55 | 8.85 | -7.33% | 1.9y | medium | 7d | -2.55% | 48.2 | → stable | — |

## IGNORE Summary

*30 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| KDBY | -18.68% | maturity:5.9y |
| LVF2 | -16.04% | liquidity:low; maturity:7.0y |
| SBCF | -15.34% | maturity:4.6y |
| SFEF | -14.26% | liquidity:low; maturity:5.5y |
| NICGF2 | -13.46% | liquidity:low; maturity:4.2y |
| NIBLGF | -13.11% | maturity:6.4y |
| KEF | -12.50% | maturity:4.6y |
| NIBSF2 | -12.00% | maturity:4.8y |
| MBLEF | -11.80% | liquidity:low; maturity:10.6y |
| NIBLSTF | -11.32% | maturity:9.5y |
| KSY | -10.98% | maturity:7.6y |
| RBBF40 | -9.55% | maturity:11.2y |
| GBIMESY2 | -8.36% | liquidity:low; maturity:8.9y |
| PRSF | -8.05% | maturity:5.6y |
| GIBF1 | -7.47% | liquidity:low; maturity:5.9y |
| MNMF1 | -7.05% | maturity:8.3y |
| RMF2 | -7.00% | liquidity:low; maturity:6.8y |
| GSY | -6.43% | maturity:8.4y |
| NBF3 | -6.30% | maturity:5.1y |
| NSIF2 | -5.66% | maturity:6.0y |
| NMBHF2 | -5.53% | maturity:8.5y |
| MMF1 | -5.49% | maturity:5.0y |
| RSY | -5.47% | maturity:8.7y |
| SAGF | -5.22% | liquidity:low; maturity:7.3y |
| C30MF | -5.03% | maturity:6.7y |
| H8020 | -4.61% | maturity:7.1y |
| HLICF | -4.12% | liquidity:low; maturity:9.1y |
| SIGS3 | -3.85% | valuation:small_discount; maturity:6.7y |
| SLCF | -3.77% | valuation:small_discount; liquidity:low |
| SIGS2 | -3.13% | valuation:small_discount |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 27
- NAV data age: median 17 days, max 448 days

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
