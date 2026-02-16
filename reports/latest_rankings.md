# Nepal MF Quant — Full Analysis Report

*Generated: 2026-02-16 11:07*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-02-16 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 10 |
| Median Discount | -7.02% |
| CONSIDER | 6 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 4 | 9.8% |
| -10% to -6% | 21 | 51.2% |
| -6% to -4% | 9 | 22.0% |
| -4% to 0% | 6 | 14.6% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.27 | -9.12% | 3.7y | high | 2d | -2.04% | 72.6 | → stable | — |
| 2 | NICBF | NIC ASIA Balanced Fund | 10.04 | 9.32 | -7.17% | 3.5y | medium | 1d | 3.83% | 70.5 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.02 | 9.20 | -8.18% | 3.3y | medium | 5d | 3.51% | 69.9 | → stable | — |
| 4 | SIGS2 | Siddhartha Investment Gro | 10.41 | 9.88 | -5.09% | 3.5y | medium | 1d | — | 64.9 | ↑ narrowing | — |
| 5 | NBF2 | Nabil Balanced Fund - 2 | 10.42 | 9.61 | -7.77% | 3.3y | high | 5d | 2.26% | 55.7 | ↓ widening | — |
| 6 | NICSF | NIC Asia Select-30 | 9.54 | 8.90 | -6.71% | 2.4y | medium | 4d | — | 52.2 | → stable | — |

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
| SBCF | -15.52% | maturity:5.1y |
| LUK | -15.09% | maturity:4.5y |
| SFEF | -15.05% | liquidity:low; maturity:6.0y |
| LVF2 | -14.90% | maturity:7.5y |
| NICGF2 | -9.66% | liquidity:low; maturity:4.8y |
| KSY | -8.48% | liquidity:low; maturity:8.1y |
| RMF2 | -8.40% | liquidity:low; maturity:7.3y |
| RBBF40 | -8.12% | maturity:11.8y |
| PSF | -7.90% | liquidity:low |
| PRSF | -7.89% | maturity:6.1y |
| NMBHF2 | -7.82% | maturity:9.0y |
| GIBF1 | -7.79% | liquidity:low; maturity:6.5y |
| NSIF2 | -7.57% | maturity:6.5y |
| C30MF | -7.55% | maturity:7.2y |
| NBF3 | -7.16% | maturity:5.6y |
| NIBSF2 | -7.16% | maturity:5.3y |
| MBLEF | -7.02% | maturity:11.1y |
| MMF1 | -6.60% | maturity:5.6y |
| MNMF1 | -6.16% | maturity:8.8y |
| RSY | -6.10% | maturity:9.2y |
| KDBY | -5.94% | maturity:6.4y |
| NIBLSTF | -5.33% | maturity:10.0y |
| KEF | -5.16% | maturity:5.1y |
| GSY | -4.95% | maturity:8.9y |
| GBIMESY2 | -4.89% | maturity:9.4y |
| SAGF | -4.68% | maturity:7.8y |
| NIBLGF | -4.50% | liquidity:low; maturity:6.9y |
| SIGS3 | -4.36% | maturity:7.2y |
| HLICF | -3.94% | valuation:small_discount; liquidity:low; maturity:9.6y |
| H8020 | -3.78% | valuation:small_discount; maturity:7.6y |
| SEF | -3.69% | valuation:small_discount |
| SLCF | -3.66% | valuation:small_discount |
| RMF1 | -2.40% | valuation:small_discount; liquidity:low |
| CMF2 | -1.79% | valuation:small_discount; liquidity:low |
| NMB50 | 1.36% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 41
- Symbols with issues: 11
- NAV data age: median 32 days, max 263 days

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
