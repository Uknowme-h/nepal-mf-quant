# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-11 14:13*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-11 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 18 |
| Median Discount | -7.08% |
| CONSIDER | 6 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 11 | 26.8% |
| -10% to -6% | 17 | 41.5% |
| -6% to -4% | 5 | 12.2% |
| -4% to 0% | 6 | 14.6% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 12.20 | -10.88% | 2.0y | high | 7d | -4.60% | 68.4 | ↓ widening | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.50 | -7.08% | 3.4y | medium | 2d | -2.04% | 65.7 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.25 | -10.97% | 3.0y | medium | 3d | -1.24% | 56.8 | ↓ widening | — |
| 4 | SEF | Siddhartha Equity Fund | 10.65 | 10.00 | -6.10% | 1.4y | high | 22d | -2.74% | 53.3 | ↓ widening | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.41 | 9.77 | -6.15% | 2.1y | medium | 8d | -2.16% | 50.0 | → stable | high_vol |
| 6 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.88 | -5.64% | 3.0y | medium | 1d | 0.48% | 44.9 | ↓ widening | — |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 8 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -15.09% | maturity:4.2y |
| LVF2 | -14.55% | liquidity:low; maturity:7.2y |
| SBCF | -14.46% | maturity:4.8y |
| PRSF | -13.07% | maturity:5.8y |
| KDBY | -12.51% | maturity:6.1y |
| SFEF | -11.81% | maturity:5.7y |
| NICBF | -11.37% | liquidity:low |
| KEF | -10.74% | maturity:4.8y |
| GIBF1 | -10.51% | maturity:6.1y |
| RSY | -9.45% | maturity:8.9y |
| RMF2 | -9.43% | liquidity:low; maturity:7.0y |
| SIGS3 | -9.17% | liquidity:low; maturity:6.9y |
| MBLEF | -9.08% | maturity:10.8y |
| RBBF40 | -8.60% | liquidity:low; maturity:11.4y |
| NSIF2 | -8.52% | maturity:6.2y |
| NMBHF2 | -8.42% | maturity:8.7y |
| NICGF2 | -7.83% | maturity:4.5y |
| KSY | -7.31% | liquidity:low; maturity:7.8y |
| C30MF | -7.06% | maturity:6.9y |
| H8020 | -6.97% | maturity:7.3y |
| NIBLSTF | -6.47% | maturity:9.7y |
| GBIMESY2 | -6.35% | maturity:9.1y |
| NIBSF2 | -6.28% | maturity:5.0y |
| NIBLGF | -5.43% | liquidity:low; maturity:6.6y |
| SAGF | -5.29% | liquidity:low; maturity:7.5y |
| MNMF1 | -5.21% | maturity:8.5y |
| GSY | -4.87% | maturity:8.6y |
| SLCF | -3.29% | valuation:small_discount |
| CMF2 | -3.23% | valuation:small_discount; liquidity:low |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.3y |
| NICSF | -2.17% | valuation:small_discount |
| SIGS2 | -2.05% | valuation:small_discount |
| MMF1 | -1.86% | valuation:small_discount; maturity:5.2y |
| HLICF | 1.58% | valuation:premium; maturity:9.3y |
| NMB50 | 4.55% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 24
- NAV data age: median 27 days, max 378 days

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
