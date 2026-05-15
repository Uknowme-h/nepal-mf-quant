# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-15 12:08*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-15 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 26 |
| Median Discount | -9.09% |
| CONSIDER | 6 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 17 | 41.5% |
| -10% to -6% | 17 | 41.5% |
| -6% to -4% | 5 | 12.2% |
| -4% to 0% | 2 | 4.9% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 14.35 | 11.93 | -16.86% | 2.1y | high | 1d | 12.55% | 70.1 | ↓ widening | — |
| 2 | SEF | Siddhartha Equity Fund | 10.95 | 9.95 | -9.13% | 1.5y | medium | 5d | 3.79% | 60.4 | → stable | — |
| 3 | SLCF | Sanima Large Cap Fund | 10.65 | 10.09 | -5.26% | 1.8y | medium | 1d | 0.47% | 54.9 | ↑ narrowing | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.64 | 9.82 | -7.71% | 2.2y | high | 18d | 0.76% | 43.7 | ↓ widening | high_vol |
| 5 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.00 | -4.49% | 3.0y | medium | 1d | 0.48% | 40.5 | ↓ widening | — |
| 6 | NICSF | NIC Asia Select-30 | 9.89 | 9.15 | -7.48% | 2.1y | high | 3d | -1.49% | 39.8 | ↓ widening | — |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 2 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -18.04% | maturity:5.8y |
| KEF | -17.29% | maturity:4.8y |
| KDBY | -17.03% | maturity:6.2y |
| GIBF1 | -13.68% | maturity:6.2y |
| SIGS3 | -13.68% | maturity:7.0y |
| LUK | -13.38% | maturity:4.2y |
| LVF2 | -13.32% | maturity:7.3y |
| KSY | -13.28% | liquidity:low; maturity:7.8y |
| NICGF2 | -13.21% | liquidity:low; maturity:4.5y |
| SBCF | -13.14% | maturity:4.9y |
| NSIF2 | -11.57% | liquidity:low; maturity:6.3y |
| NICFC | -11.41% | liquidity:low |
| SFEF | -11.11% | maturity:5.8y |
| RSY | -11.10% | maturity:9.0y |
| MBLEF | -10.58% | maturity:10.9y |
| NMBHF2 | -10.58% | liquidity:low; maturity:8.8y |
| SIGS2 | -9.97% | liquidity:low |
| RMF2 | -9.41% | maturity:7.0y |
| GSY | -9.09% | maturity:8.6y |
| H8020 | -8.98% | maturity:7.4y |
| NIBSF2 | -8.91% | maturity:5.0y |
| MNMF1 | -8.84% | maturity:8.6y |
| C30MF | -8.55% | maturity:7.0y |
| SFMF | -8.32% | liquidity:low |
| GBIMESY2 | -7.93% | maturity:9.2y |
| RBBF40 | -7.50% | maturity:11.5y |
| NICBF | -6.40% | liquidity:low |
| CMF2 | -6.37% | liquidity:low |
| NIBLGF | -6.22% | maturity:6.7y |
| NIBLSTF | -6.18% | maturity:9.7y |
| SAGF | -5.37% | maturity:7.5y |
| MMF1 | -4.81% | maturity:5.3y |
| NBF3 | -4.07% | maturity:5.4y |
| HLICF | -3.43% | valuation:small_discount; maturity:9.3y |
| NMB50 | -2.42% | valuation:small_discount; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 24
- NAV data age: median 30 days, max 351 days

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
