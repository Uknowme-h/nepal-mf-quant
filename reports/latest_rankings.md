# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-05 11:42*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-05 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 29 |
| Median Discount | -11.39% |
| CONSIDER | 9 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 24 | 58.5% |
| -10% to -6% | 12 | 29.3% |
| -6% to -4% | 3 | 7.3% |
| -4% to 0% | 2 | 4.9% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 14.35 | 11.93 | -16.86% | 2.1y | high | 2d | 12.55% | 72.9 | ↓ widening | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.25 | -12.07% | 3.1y | medium | 3d | 4.26% | 62.0 | → stable | — |
| 3 | SEF | Siddhartha Equity Fund | 10.95 | 9.90 | -9.59% | 1.5y | high | 1d | 3.79% | 60.9 | → stable | high_vol |
| 4 | SLCF | Sanima Large Cap Fund | 10.65 | 9.75 | -8.45% | 1.8y | medium | 18d | 0.47% | 60.5 | → stable | — |
| 5 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.00 | -4.49% | 3.1y | high | 1d | 0.48% | 55.0 | → stable | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.64 | 9.73 | -8.55% | 2.2y | medium | 10d | 0.76% | 52.4 | ↑ narrowing | high_vol |
| 7 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.74 | -6.97% | 3.3y | medium | 5d | 4.39% | 51.2 | ↑ narrowing | high_vol |
| 8 | NICSF | NIC Asia Select-30 | 9.89 | 9.28 | -6.17% | 2.2y | medium | 3d | -1.49% | 47.1 | → stable | — |
| 9 | NMB50 | NMB 50 | 10.76 | 10.30 | -4.28% | 0.3y | medium | 1d | -0.92% | 40.4 | ↓ widening | — |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 2 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -18.17% | liquidity:low; maturity:5.9y |
| KEF | -17.60% | maturity:4.9y |
| KDBY | -16.67% | maturity:6.2y |
| SIGS3 | -15.15% | maturity:7.0y |
| GIBF1 | -14.98% | maturity:6.2y |
| LUK | -14.67% | maturity:4.3y |
| SBCF | -14.02% | maturity:4.9y |
| KSY | -13.40% | liquidity:low; maturity:7.9y |
| NSIF2 | -13.22% | maturity:6.3y |
| NICGF2 | -12.84% | liquidity:low; maturity:4.5y |
| LVF2 | -12.80% | liquidity:low; maturity:7.3y |
| SFEF | -12.51% | maturity:5.8y |
| RSY | -12.40% | maturity:9.0y |
| MBLEF | -12.08% | maturity:10.9y |
| NMBHF2 | -11.99% | maturity:8.8y |
| MNMF1 | -11.58% | maturity:8.6y |
| SIGS2 | -11.54% | liquidity:low |
| H8020 | -11.48% | maturity:7.4y |
| GSY | -11.39% | maturity:8.7y |
| RMF2 | -10.30% | maturity:7.0y |
| C30MF | -10.19% | liquidity:low; maturity:7.0y |
| GBIMESY2 | -10.04% | liquidity:low; maturity:9.2y |
| NIBLSTF | -9.66% | maturity:9.8y |
| NIBSF2 | -9.41% | maturity:5.1y |
| SFMF | -7.96% | liquidity:low |
| SAGF | -7.64% | maturity:7.6y |
| RBBF40 | -7.50% | maturity:11.5y |
| CMF2 | -6.84% | liquidity:low |
| NIBLGF | -6.22% | maturity:6.7y |
| MMF1 | -5.81% | maturity:5.3y |
| NBF3 | -3.78% | valuation:small_discount; maturity:5.4y |
| HLICF | -2.36% | valuation:small_discount; liquidity:low; maturity:9.4y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 27
- NAV data age: median 20 days, max 341 days

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
