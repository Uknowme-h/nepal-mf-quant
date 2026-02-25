# Nepal MF Quant — Full Analysis Report

*Generated: 2026-02-25 11:09*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-02-25 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 13 |
| Median Discount | -6.91% |
| CONSIDER | 7 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 5 | 12.2% |
| -10% to -6% | 22 | 53.7% |
| -6% to -4% | 8 | 19.5% |
| -4% to 0% | 3 | 7.3% |
| ≥ 0% (premium) | 3 | 7.3% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.02 | 9.20 | -8.18% | 3.3y | high | 10d | 3.51% | 75.2 | → stable | — |
| 2 | PSF | Prabhu Select Fund | 12.03 | 11.05 | -8.15% | 2.3y | medium | 5d | 3.35% | 71.3 | → stable | — |
| 3 | NBF2 | Nabil Balanced Fund - 2 | 10.42 | 9.70 | -6.91% | 3.3y | high | 2d | 2.26% | 65.0 | ↑ narrowing | — |
| 4 | SEF | Siddhartha Equity Fund | 10.02 | 9.55 | -4.69% | 1.7y | high | 1d | — | 54.6 | ↓ widening | — |
| 5 | NICSF | NIC Asia Select-30 | 9.54 | 9.10 | -4.61% | 2.4y | medium | 3d | — | 53.1 | ↑ narrowing | — |
| 6 | SIGS2 | Siddhartha Investment Gro | 10.41 | 9.88 | -5.09% | 3.5y | medium | 1d | — | 52.2 | → stable | — |
| 7 | SLCF | Sanima Large Cap Fund | 10.12 | 9.46 | -6.52% | 2.0y | medium | 2d | — | 43.6 | ↓ widening | — |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 6 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -16.65% | maturity:7.5y |
| LUK | -16.21% | maturity:4.5y |
| SBCF | -16.14% | liquidity:low; maturity:5.1y |
| SFEF | -15.92% | maturity:6.0y |
| NSIF2 | -10.40% | liquidity:low; maturity:6.5y |
| SFMF | -9.20% | liquidity:low |
| KSY | -9.06% | liquidity:low; maturity:8.1y |
| C30MF | -8.98% | liquidity:low; maturity:7.2y |
| GIBF1 | -8.82% | maturity:6.4y |
| KEF | -8.13% | maturity:5.1y |
| RMF2 | -8.12% | maturity:7.2y |
| NIBSF2 | -7.67% | maturity:5.3y |
| KDBY | -7.67% | maturity:6.4y |
| SIGS3 | -7.43% | liquidity:low; maturity:7.2y |
| PRSF | -7.40% | maturity:6.0y |
| NICGF2 | -7.30% | liquidity:low; maturity:4.7y |
| MBLEF | -7.29% | maturity:11.1y |
| RBBF40 | -7.12% | maturity:11.7y |
| NBF3 | -6.86% | maturity:5.6y |
| NIBLSTF | -6.36% | maturity:10.0y |
| GSY | -6.24% | maturity:8.9y |
| NMBHF2 | -6.17% | liquidity:low; maturity:9.0y |
| RSY | -6.01% | maturity:9.2y |
| HLICF | -5.08% | maturity:9.6y |
| NIBLGF | -5.02% | liquidity:low; maturity:6.9y |
| GBIMESY2 | -4.79% | maturity:9.4y |
| NICBF | -4.38% | liquidity:low |
| MNMF1 | -4.30% | maturity:8.8y |
| RMF1 | -3.99% | valuation:small_discount |
| SAGF | -3.72% | valuation:small_discount; maturity:7.8y |
| H8020 | -1.43% | valuation:small_discount; maturity:7.6y |
| NMB50 | 0.78% | valuation:premium |
| CMF2 | 1.39% | valuation:premium |
| MMF1 | 2.09% | valuation:premium; maturity:5.5y |

</details>

## Data Quality

- Symbols checked: 41
- Symbols with issues: 18
- NAV data age: median 41 days, max 272 days

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
