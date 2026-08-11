# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-11 11:05*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-11 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 21 |
| Median Discount | -8.29% |
| CONSIDER | 5 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 6 | 15.0% |
| -10% to -6% | 23 | 57.5% |
| -6% to -4% | 7 | 17.5% |
| -4% to 0% | 4 | 10.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.30 | -8.85% | 3.2y | medium | 1d | -2.04% | 70.2 | → stable | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.20 | -10.68% | 2.9y | medium | 4d | 0.88% | 65.5 | ↓ widening | — |
| 3 | PSF | Prabhu Select Fund | 13.04 | 11.84 | -9.20% | 1.9y | medium | 48d | -4.26% | 58.8 | ↓ widening | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.28 | 9.82 | -4.47% | 1.9y | high | 17d | -1.63% | 54.2 | ↑ narrowing | high_vol |
| 5 | SLCF | Sanima Large Cap Fund | 10.08 | 9.33 | -7.44% | 1.5y | medium | 1d | -2.70% | 45.9 | ↓ widening | — |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -19.72% | liquidity:low; maturity:7.1y |
| SBCF | -15.34% | maturity:4.6y |
| SFEF | -14.26% | liquidity:low; maturity:5.5y |
| NICGF2 | -13.37% | maturity:4.3y |
| KDBY | -11.26% | maturity:6.0y |
| NICBF | -9.88% | liquidity:low |
| RMF2 | -9.58% | liquidity:low; maturity:6.8y |
| RBBF40 | -9.45% | maturity:11.3y |
| KSY | -9.33% | maturity:7.6y |
| NICSF | -9.32% | liquidity:low |
| LUK | -9.18% | maturity:4.0y |
| NIBLSTF | -9.10% | maturity:9.5y |
| NIBSF2 | -9.03% | maturity:4.8y |
| NIBLGF | -9.02% | maturity:6.4y |
| NMBHF2 | -8.68% | maturity:8.6y |
| PRSF | -8.55% | maturity:5.6y |
| GBIMESY2 | -8.36% | maturity:8.9y |
| NSIF2 | -8.23% | liquidity:low; maturity:6.1y |
| RSY | -7.97% | maturity:8.7y |
| GIBF1 | -7.47% | maturity:6.0y |
| NBF3 | -6.98% | maturity:5.1y |
| MNMF1 | -6.95% | maturity:8.4y |
| MMF1 | -6.12% | maturity:5.1y |
| KEF | -6.12% | maturity:4.6y |
| NBF2 | -6.11% | liquidity:low |
| H8020 | -5.66% | liquidity:low; maturity:7.2y |
| C30MF | -5.32% | maturity:6.8y |
| SIGS3 | -5.16% | maturity:6.7y |
| SAGF | -5.12% | liquidity:low; maturity:7.3y |
| MBLEF | -4.88% | maturity:10.6y |
| GSY | -4.62% | maturity:8.4y |
| HLICF | -2.63% | valuation:small_discount; maturity:9.1y |
| SIGS2 | -1.38% | valuation:small_discount |
| SEF | -1.06% | valuation:small_discount |
| NMB50 | -0.38% | valuation:small_discount; liquidity:low |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 29
- NAV data age: median 8 days, max 439 days

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
