# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-15 11:17*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-15 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 37 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 16 |
| Median Discount | -7.48% |
| CONSIDER | 6 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 6 | 15.0% |
| -10% to -6% | 20 | 50.0% |
| -6% to -4% | 4 | 10.0% |
| -4% to 0% | 7 | 17.5% |
| ≥ 0% (premium) | 3 | 7.5% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.52 | -9.51% | 3.2y | medium | 10d | 4.26% | 65.0 | ↑ narrowing | — |
| 2 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.80 | -7.20% | 2.3y | medium | 10d | 5.28% | 58.8 | ↑ narrowing | high_vol |
| 3 | SLCF | Sanima Large Cap Fund | 10.60 | 10.01 | -5.57% | 1.9y | medium | 5d | 4.43% | 52.5 | ↑ narrowing | — |
| 4 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.52 | -6.90% | 3.6y | medium | 1d | -2.04% | 44.1 | → stable | — |
| 5 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.01 | -4.39% | 3.1y | high | 3d | 0.48% | 42.6 | ↓ widening | — |
| 6 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.52 | -9.07% | 3.4y | medium | 1d | 4.39% | 40.9 | ↓ widening | high_vol |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -14.24% | liquidity:low; maturity:4.3y |
| SBCF | -13.40% | liquidity:low; maturity:5.0y |
| LVF2 | -12.36% | maturity:7.4y |
| MBLEF | -11.78% | maturity:11.0y |
| SFEF | -11.37% | liquidity:low; maturity:5.8y |
| NSIF2 | -10.98% | maturity:6.4y |
| NIBLSTF | -9.45% | maturity:9.8y |
| GIBF1 | -9.37% | maturity:6.3y |
| NICGF2 | -9.18% | maturity:4.6y |
| RSY | -9.12% | maturity:9.1y |
| GBIMESY2 | -9.04% | liquidity:low; maturity:9.3y |
| NMBHF2 | -8.37% | liquidity:low; maturity:8.9y |
| RBBF40 | -8.29% | maturity:11.6y |
| GSY | -8.11% | maturity:8.7y |
| MNMF1 | -7.92% | liquidity:low; maturity:8.7y |
| NIBSF2 | -7.80% | maturity:5.1y |
| RMF2 | -7.72% | maturity:7.1y |
| C30MF | -7.55% | maturity:7.1y |
| NIBLGF | -7.41% | maturity:6.8y |
| SAGF | -6.57% | maturity:7.6y |
| SIGS2 | -6.38% | liquidity:low |
| NICSF | -6.37% | liquidity:low |
| SIGS3 | -5.81% | maturity:7.0y |
| H8020 | -4.61% | liquidity:low; maturity:7.5y |
| SEF | -3.79% | valuation:small_discount |
| CMF2 | -3.39% | valuation:small_discount; liquidity:low |
| NMB50 | -3.31% | valuation:small_discount |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.4y |
| PSF | -3.06% | valuation:small_discount |
| MMF1 | -2.96% | valuation:small_discount; maturity:5.4y |
| HLICF | -1.56% | valuation:small_discount; maturity:9.4y |
| PRSF | 1.23% | valuation:premium; maturity:5.9y |
| KEF | 3.32% | valuation:premium; maturity:4.9y |
| KDBY | 4.73% | valuation:premium; maturity:6.3y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 11
- NAV data age: median 31 days, max 321 days

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
