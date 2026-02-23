# Nepal MF Quant — Full Analysis Report

*Generated: 2026-02-23 11:07*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-02-23 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 13 |
| Median Discount | -6.92% |
| CONSIDER | 6 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 5 | 12.2% |
| -10% to -6% | 22 | 53.7% |
| -6% to -4% | 7 | 17.1% |
| -4% to 0% | 5 | 12.2% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.02 | 9.16 | -8.58% | 3.3y | medium | 8d | 3.51% | 72.0 | → stable | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.07 | -10.88% | 3.7y | high | 1d | -2.04% | 65.7 | ↓ widening | — |
| 3 | NICBF | NIC ASIA Balanced Fund | 10.04 | 9.60 | -4.38% | 3.5y | high | 1d | 3.83% | 63.1 | ↑ narrowing | — |
| 4 | PSF | Prabhu Select Fund | 12.03 | 11.10 | -7.73% | 2.3y | medium | 3d | 3.35% | 61.9 | → stable | — |
| 5 | NICSF | NIC Asia Select-30 | 9.54 | 8.89 | -6.81% | 2.4y | medium | 1d | — | 58.1 | ↑ narrowing | — |
| 6 | SEF | Siddhartha Equity Fund | 10.02 | 9.61 | -4.09% | 1.7y | high | 2d | — | 45.7 | ↓ widening | — |

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
| SFEF | -16.01% | maturity:6.0y |
| LVF2 | -15.69% | maturity:7.5y |
| SBCF | -14.81% | maturity:5.1y |
| LUK | -14.75% | maturity:4.5y |
| NSIF2 | -9.72% | liquidity:low; maturity:6.5y |
| PRSF | -9.28% | maturity:6.1y |
| KSY | -9.06% | maturity:8.1y |
| GIBF1 | -8.82% | maturity:6.4y |
| NICGF2 | -8.78% | liquidity:low; maturity:4.7y |
| KDBY | -8.68% | maturity:6.4y |
| KEF | -8.63% | liquidity:low; maturity:5.1y |
| RSY | -7.98% | maturity:9.2y |
| NBF3 | -7.84% | maturity:5.6y |
| NBF2 | -7.77% | liquidity:low |
| MNMF1 | -7.14% | maturity:8.8y |
| NMBHF2 | -6.94% | maturity:9.0y |
| GSY | -6.93% | maturity:8.9y |
| SIGS2 | -6.92% | liquidity:low |
| NIBSF2 | -6.85% | maturity:5.3y |
| MBLEF | -6.74% | maturity:11.1y |
| RMF2 | -6.63% | liquidity:low; maturity:7.2y |
| C30MF | -6.40% | maturity:7.2y |
| SIGS3 | -6.13% | liquidity:low; maturity:7.2y |
| SLCF | -5.93% | liquidity:low |
| SAGF | -5.53% | liquidity:low; maturity:7.8y |
| NIBLSTF | -5.13% | maturity:10.0y |
| GBIMESY2 | -4.99% | maturity:9.4y |
| HLICF | -4.88% | liquidity:low; maturity:9.6y |
| RBBF40 | -3.71% | valuation:small_discount; maturity:11.7y |
| RMF1 | -3.69% | valuation:small_discount |
| H8020 | -3.36% | valuation:small_discount; maturity:7.6y |
| CMF2 | -1.69% | valuation:small_discount |
| NIBLGF | -1.23% | valuation:small_discount; maturity:6.9y |
| MMF1 | 0.63% | valuation:premium; maturity:5.5y |
| NMB50 | 1.65% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 41
- Symbols with issues: 17
- NAV data age: median 39 days, max 270 days

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
