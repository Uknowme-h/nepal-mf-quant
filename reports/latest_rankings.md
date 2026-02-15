# Nepal MF Quant — Full Analysis Report

*Generated: 2026-02-15 10:48*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-02-12 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 12 |
| Median Discount | -6.07% |
| CONSIDER | 6 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 4 | 9.8% |
| -10% to -6% | 17 | 41.5% |
| -6% to -4% | 13 | 31.7% |
| -4% to 0% | 7 | 17.1% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.02 | 9.16 | -8.58% | 3.3y | medium | 4d | 3.51% | 67.2 | → stable | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.23 | -9.47% | 3.7y | medium | 1d | -2.04% | 66.8 | → stable | — |
| 3 | NBF2 | Nabil Balanced Fund - 2 | 10.42 | 9.85 | -5.47% | 3.3y | high | 4d | 2.26% | 64.4 | ↑ narrowing | — |
| 4 | PSF | Prabhu Select Fund | 12.03 | 11.30 | -6.07% | 2.4y | medium | 3d | 3.35% | 63.6 | ↑ narrowing | — |
| 5 | NICSF | NIC Asia Select-30 | 9.54 | 8.92 | -6.50% | 2.4y | medium | 3d | — | 60.6 | ↑ narrowing | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.02 | 9.60 | -4.19% | 2.4y | high | 1d | — | 41.3 | → stable | high_vol |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 7 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -17.11% | liquidity:low; maturity:5.1y |
| LVF2 | -15.51% | liquidity:low; maturity:7.6y |
| LUK | -15.09% | liquidity:low; maturity:4.5y |
| SFEF | -14.26% | liquidity:low; maturity:6.0y |
| NICGF2 | -9.37% | maturity:4.8y |
| NMBHF2 | -8.78% | maturity:9.1y |
| NICBF | -8.37% | liquidity:low |
| NSIF2 | -8.34% | maturity:6.6y |
| PRSF | -8.30% | maturity:6.1y |
| RSY | -8.17% | maturity:9.2y |
| GIBF1 | -7.45% | maturity:6.5y |
| C30MF | -7.26% | liquidity:low; maturity:7.2y |
| KEF | -6.94% | maturity:5.1y |
| MBLEF | -6.83% | maturity:11.1y |
| SIGS2 | -6.82% | liquidity:low |
| KSY | -6.63% | liquidity:low; maturity:8.1y |
| NIBSF2 | -6.44% | maturity:5.3y |
| KDBY | -5.94% | maturity:6.5y |
| RBBF40 | -5.92% | maturity:11.8y |
| SAGF | -5.82% | liquidity:low; maturity:7.8y |
| NBF3 | -5.39% | maturity:5.6y |
| MNMF1 | -5.18% | maturity:8.8y |
| NIBLSTF | -5.03% | maturity:10.0y |
| RMF2 | -4.95% | maturity:7.3y |
| MMF1 | -4.92% | maturity:5.6y |
| GSY | -4.46% | maturity:8.9y |
| HLICF | -4.05% | maturity:9.6y |
| H8020 | -4.03% | maturity:7.6y |
| SIGS3 | -3.90% | valuation:small_discount; maturity:7.2y |
| GBIMESY2 | -2.95% | valuation:small_discount; liquidity:low; maturity:9.4y |
| NIBLGF | -2.56% | valuation:small_discount; maturity:6.9y |
| SEF | -2.30% | valuation:small_discount |
| SLCF | -2.27% | valuation:small_discount |
| CMF2 | -2.09% | valuation:small_discount |
| NMB50 | -0.58% | valuation:small_discount |

</details>

## Data Quality

- Symbols checked: 41
- Symbols with issues: 12
- NAV data age: median 31 days, max 262 days

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
