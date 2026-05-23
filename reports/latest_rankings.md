# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-23 11:36*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-22 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 23 |
| Median Discount | -9.46% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 18 | 43.9% |
| -10% to -6% | 15 | 36.6% |
| -6% to -4% | 3 | 7.3% |
| -4% to 0% | 5 | 12.2% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 14.35 | 12.21 | -14.91% | 2.1y | high | 6d | 12.55% | 83.8 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.40 | -10.65% | 3.1y | high | 5d | 4.26% | 65.4 | ↑ narrowing | — |
| 3 | SEF | Siddhartha Equity Fund | 10.95 | 10.40 | -5.02% | 1.5y | high | 10d | 3.79% | 64.5 | ↑ narrowing | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.64 | 10.00 | -6.02% | 2.2y | medium | 23d | 0.76% | 51.2 | ↑ narrowing | high_vol |
| 5 | NICSF | NIC Asia Select-30 | 9.89 | 9.29 | -6.07% | 2.1y | high | 8d | -1.49% | 49.3 | ↑ narrowing | — |
| 6 | SLCF | Sanima Large Cap Fund | 10.65 | 10.00 | -6.10% | 1.8y | medium | 2d | 0.47% | 44.9 | ↓ widening | — |
| 7 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.40 | -10.22% | 3.3y | medium | 1d | 4.39% | 43.2 | ↓ widening | high_vol |
| 8 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.95 | -4.97% | 3.0y | medium | 1d | 0.48% | 40.6 | → stable | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 5 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -18.30% | maturity:5.8y |
| KDBY | -16.67% | maturity:6.2y |
| KEF | -16.28% | maturity:4.8y |
| LUK | -14.67% | liquidity:low; maturity:4.2y |
| SBCF | -12.70% | maturity:4.8y |
| LVF2 | -12.36% | maturity:7.3y |
| SIGS3 | -11.56% | liquidity:low; maturity:7.0y |
| SFMF | -11.42% | liquidity:low |
| MBLEF | -11.38% | maturity:10.8y |
| SFEF | -11.37% | liquidity:low; maturity:5.7y |
| NSIF2 | -11.16% | maturity:6.3y |
| GBIMESY2 | -10.99% | liquidity:low; maturity:9.2y |
| GIBF1 | -10.93% | maturity:6.2y |
| C30MF | -10.56% | liquidity:low; maturity:7.0y |
| RSY | -10.23% | maturity:8.9y |
| NICGF2 | -9.65% | liquidity:low; maturity:4.5y |
| KSY | -9.59% | maturity:7.8y |
| NMBHF2 | -9.46% | maturity:8.8y |
| MNMF1 | -8.84% | maturity:8.6y |
| GSY | -8.17% | maturity:8.6y |
| RBBF40 | -7.98% | maturity:11.5y |
| NIBLSTF | -7.47% | maturity:9.7y |
| NIBSF2 | -7.43% | maturity:5.0y |
| SAGF | -7.19% | maturity:7.5y |
| RMF2 | -6.75% | liquidity:low; maturity:7.0y |
| H8020 | -6.48% | maturity:7.4y |
| SIGS2 | -6.16% | liquidity:low |
| HLICF | -4.83% | maturity:9.3y |
| MMF1 | -3.91% | valuation:small_discount; maturity:5.3y |
| CMF2 | -3.61% | valuation:small_discount; liquidity:low |
| NBF3 | -3.59% | valuation:small_discount; maturity:5.3y |
| NIBLGF | -2.17% | valuation:small_discount; maturity:6.7y |
| NMB50 | -0.56% | valuation:small_discount |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 23
- NAV data age: median 38 days, max 359 days

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
