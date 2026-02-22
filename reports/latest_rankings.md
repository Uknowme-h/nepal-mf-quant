# Nepal MF Quant — Full Analysis Report

*Generated: 2026-02-22 10:45*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-02-22 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 13 |
| Median Discount | -6.75% |
| CONSIDER | 5 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 6 | 14.6% |
| -10% to -6% | 17 | 41.5% |
| -6% to -4% | 11 | 26.8% |
| -4% to 0% | 5 | 12.2% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.02 | 9.16 | -8.58% | 3.3y | high | 7d | 3.51% | 76.0 | → stable | — |
| 2 | NBF2 | Nabil Balanced Fund - 2 | 10.42 | 9.60 | -7.87% | 3.3y | medium | 7d | 2.26% | 64.0 | → stable | — |
| 3 | PSF | Prabhu Select Fund | 12.03 | 11.08 | -7.90% | 2.3y | medium | 2d | 3.35% | 62.1 | ↓ widening | — |
| 4 | SEF | Siddhartha Equity Fund | 10.02 | 9.43 | -5.89% | 1.7y | high | 1d | — | 52.9 | ↓ widening | — |
| 5 | SLCF | Sanima Large Cap Fund | 10.12 | 9.70 | -4.15% | 2.0y | medium | 1d | — | 37.5 | ↓ widening | — |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 7 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -16.91% | maturity:7.5y |
| LUK | -16.81% | liquidity:low; maturity:4.5y |
| SFEF | -15.75% | maturity:6.0y |
| SBCF | -15.52% | maturity:5.1y |
| KDBY | -10.23% | maturity:6.4y |
| NSIF2 | -10.15% | maturity:6.5y |
| SFMF | -9.20% | liquidity:low |
| PRSF | -9.03% | maturity:6.1y |
| GIBF1 | -8.82% | maturity:6.4y |
| NMBHF2 | -8.78% | maturity:9.0y |
| C30MF | -8.21% | liquidity:low; maturity:7.2y |
| KSY | -8.09% | liquidity:low; maturity:8.1y |
| RMF2 | -7.84% | maturity:7.2y |
| NICGF2 | -7.30% | maturity:4.8y |
| MBLEF | -6.83% | maturity:11.1y |
| GBIMESY2 | -6.82% | liquidity:low; maturity:9.4y |
| NBF3 | -6.76% | maturity:5.6y |
| KEF | -6.75% | maturity:5.1y |
| GSY | -6.63% | maturity:8.9y |
| RSY | -6.10% | maturity:9.2y |
| NIBLSTF | -5.64% | maturity:10.0y |
| MMF1 | -5.24% | maturity:5.5y |
| SIGS3 | -5.20% | maturity:7.2y |
| SIGS2 | -5.09% | liquidity:low |
| NICSF | -4.61% | liquidity:low |
| MNMF1 | -4.50% | maturity:8.8y |
| NICBF | -4.28% | liquidity:low |
| H8020 | -4.03% | maturity:7.6y |
| SAGF | -4.01% | maturity:7.8y |
| RMF1 | -3.69% | valuation:small_discount |
| HLICF | -3.53% | valuation:small_discount; liquidity:low; maturity:9.6y |
| NIBSF2 | -2.15% | valuation:small_discount; maturity:5.3y |
| RBBF40 | -2.01% | valuation:small_discount; maturity:11.7y |
| NMB50 | -0.19% | valuation:small_discount |
| NIBLGF | 1.13% | valuation:premium; maturity:6.9y |
| CMF2 | 1.59% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 41
- Symbols with issues: 12
- NAV data age: median 38 days, max 269 days

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
