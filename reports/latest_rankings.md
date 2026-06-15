# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-15 16:08*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-15 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 19 |
| Median Discount | -7.40% |
| CONSIDER | 4 |
| IGNORE | 37 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 22.0% |
| -10% to -6% | 16 | 39.0% |
| -6% to -4% | 7 | 17.1% |
| -4% to 0% | 6 | 14.6% |
| ≥ 0% (premium) | 3 | 7.3% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.40 | -9.53% | 3.0y | medium | 5d | -1.24% | 68.9 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 13.69 | 12.30 | -10.15% | 2.0y | high | 9d | -4.60% | 66.2 | → stable | — |
| 3 | SEF | Siddhartha Equity Fund | 10.65 | 10.19 | -4.32% | 1.4y | high | 24d | -2.74% | 60.4 | ↑ narrowing | — |
| 4 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.72 | -7.16% | 3.0y | medium | 3d | 0.48% | 48.7 | ↓ widening | — |

## IGNORE Summary

*37 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 9 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -14.46% | liquidity:low; maturity:7.2y |
| SBCF | -13.93% | maturity:4.8y |
| LUK | -13.89% | maturity:4.2y |
| PRSF | -12.74% | maturity:5.8y |
| KDBY | -12.35% | maturity:6.1y |
| NICBF | -11.85% | liquidity:low |
| NICGF2 | -11.56% | maturity:4.4y |
| SFEF | -11.55% | maturity:5.7y |
| GIBF1 | -9.92% | maturity:6.1y |
| RMF2 | -9.43% | liquidity:low; maturity:6.9y |
| RSY | -9.36% | maturity:8.9y |
| KEF | -9.24% | maturity:4.8y |
| MBLEF | -9.17% | maturity:10.8y |
| NSIF2 | -8.95% | maturity:6.2y |
| RBBF40 | -8.60% | liquidity:low; maturity:11.4y |
| NMBHF2 | -8.23% | maturity:8.7y |
| GBIMESY2 | -8.02% | liquidity:low; maturity:9.1y |
| NIBSF2 | -7.60% | maturity:5.0y |
| KSY | -7.40% | maturity:7.8y |
| H8020 | -7.36% | maturity:7.3y |
| NIBLGF | -7.14% | liquidity:low; maturity:6.6y |
| C30MF | -6.97% | maturity:6.9y |
| SAGF | -5.29% | liquidity:low; maturity:7.5y |
| RMF1 | -5.28% | liquidity:low |
| MNMF1 | -5.21% | maturity:8.5y |
| GSY | -4.97% | maturity:8.6y |
| SFMF | -4.34% | liquidity:low |
| NIBLSTF | -4.00% | maturity:9.7y |
| SLCF | -3.77% | valuation:small_discount |
| CMF2 | -3.23% | valuation:small_discount |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.3y |
| NICSF | -2.69% | valuation:small_discount |
| SIGS3 | -2.69% | valuation:small_discount; maturity:6.9y |
| MMF1 | -1.55% | valuation:small_discount; maturity:5.2y |
| SIGS2 | 1.51% | valuation:premium; liquidity:low |
| NMB50 | 1.52% | valuation:premium |
| HLICF | 1.58% | valuation:premium; maturity:9.3y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 23
- NAV data age: median 31 days, max 382 days

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
