# Nepal MF Quant — Full Analysis Report

*Generated: 2026-10-03 14:45*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-10-02 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 33 |
| Median Discount | -11.70% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 17 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 27 | 69.2% |
| -10% to -6% | 10 | 25.6% |
| -6% to -4% | 1 | 2.6% |
| -4% to 0% | 1 | 2.6% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.09 | 10.92 | -16.58% | 1.7y | medium | 81d | 0.38% | 80.6 | → stable | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.25 | -18.14% | 3.1y | medium | 5d | -2.04% | 75.4 | → stable | — |
| 3 | LUK | Laxmi Unnati Kosh | 11.66 | 9.73 | -16.55% | 3.9y | medium | 3d | -1.17% | 72.2 | ↑ narrowing | — |
| 4 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.00 | -14.04% | 2.7y | high | 1d | 0.48% | 68.8 | ↓ widening | — |
| 5 | SEF | Siddhartha Equity Fund | 10.49 | 9.60 | -8.48% | 1.1y | medium | 29d | 1.06% | 50.3 | ↓ widening | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.22 | 9.00 | -11.94% | 1.8y | medium | 6d | -0.87% | 49.7 | ↓ widening | high_vol |
| 7 | SLCF | Sanima Large Cap Fund | 10.04 | 9.12 | -9.16% | 1.4y | medium | 3d | -0.99% | 45.1 | ↓ widening | — |
| 8 | NICSF | NIC Asia Select-30 | 9.28 | 8.32 | -10.34% | 1.8y | medium | 8d | -2.11% | 39.9 | ↓ widening | high_vol |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 1 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -20.82% | maturity:5.4y |
| LVF2 | -19.81% | liquidity:low; maturity:6.9y |
| SBCF | -18.87% | maturity:4.5y |
| NSIF2 | -15.31% | maturity:5.9y |
| NMBHF2 | -14.59% | liquidity:low; maturity:8.4y |
| NICGF2 | -14.04% | maturity:4.1y |
| GIBF1 | -13.63% | maturity:5.8y |
| NICFC | -13.50% | liquidity:low |
| NICBF | -12.79% | liquidity:low |
| PRSF | -12.71% | maturity:5.5y |
| RMF2 | -12.21% | liquidity:low; maturity:6.6y |
| NBF3 | -11.82% | maturity:5.0y |
| NIBLSTF | -11.76% | maturity:9.4y |
| RSY | -11.73% | maturity:8.6y |
| GBIMESY2 | -11.70% | maturity:8.8y |
| H8020 | -11.41% | maturity:7.0y |
| NIBSF2 | -11.32% | maturity:4.7y |
| RBBF40 | -10.91% | maturity:11.1y |
| SAGF | -10.78% | maturity:7.2y |
| GSY | -10.55% | maturity:8.3y |
| MBLEF | -10.26% | maturity:10.5y |
| MNMF1 | -9.99% | maturity:8.2y |
| KDBY | -9.41% | liquidity:low; maturity:5.8y |
| KEF | -9.40% | liquidity:low; maturity:4.5y |
| C30MF | -9.28% | maturity:6.6y |
| KSY | -7.76% | liquidity:low; maturity:7.5y |
| SIGS2 | -7.76% | liquidity:low |
| MMF1 | -7.05% | maturity:4.9y |
| NIBLGF | -6.91% | maturity:6.3y |
| SIGS3 | -4.76% | liquidity:low; maturity:6.6y |
| HLICF | -0.82% | valuation:small_discount; maturity:9.0y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 31
- NAV data age: median 18 days, max 492 days

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
