# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-13 12:25*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-13 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 26 |
| Median Discount | -9.60% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 18 | 43.9% |
| -10% to -6% | 14 | 34.1% |
| -6% to -4% | 6 | 14.6% |
| -4% to 0% | 3 | 7.3% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 14.35 | 11.98 | -16.52% | 2.1y | medium | 8d | 12.55% | 67.4 | ↓ widening | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.38 | -10.84% | 3.1y | medium | 3d | 4.26% | 57.6 | → stable | — |
| 3 | SEF | Siddhartha Equity Fund | 10.95 | 10.00 | -8.68% | 1.5y | high | 3d | 3.79% | 57.1 | → stable | — |
| 4 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.85 | -5.92% | 3.3y | medium | 1d | 4.39% | 55.5 | ↑ narrowing | high_vol |
| 5 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.00 | -4.49% | 3.0y | high | 1d | 0.48% | 54.1 | ↑ narrowing | — |
| 6 | SLCF | Sanima Large Cap Fund | 10.65 | 9.99 | -6.20% | 1.8y | medium | 24d | 0.47% | 49.5 | ↑ narrowing | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.64 | 9.81 | -7.80% | 2.2y | medium | 16d | 0.76% | 41.3 | ↓ widening | high_vol |
| 8 | NICSF | NIC Asia Select-30 | 9.89 | 9.24 | -6.57% | 2.1y | medium | 1d | -1.49% | 38.9 | ↓ widening | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -18.61% | maturity:5.8y |
| KDBY | -16.30% | maturity:6.2y |
| LVF2 | -15.69% | liquidity:low; maturity:7.3y |
| KEF | -15.58% | maturity:4.8y |
| GIBF1 | -13.60% | liquidity:low; maturity:6.2y |
| SIGS3 | -13.52% | liquidity:low; maturity:7.0y |
| SFEF | -13.30% | liquidity:low; maturity:5.8y |
| LUK | -12.61% | liquidity:low; maturity:4.3y |
| RSY | -12.06% | maturity:9.0y |
| NSIF2 | -11.57% | maturity:6.3y |
| SBCF | -11.46% | maturity:4.9y |
| NMBHF2 | -10.96% | maturity:8.8y |
| MNMF1 | -10.48% | maturity:8.6y |
| RMF2 | -10.21% | liquidity:low; maturity:7.0y |
| MBLEF | -10.14% | maturity:10.9y |
| KSY | -10.06% | maturity:7.8y |
| SIGS2 | -9.89% | liquidity:low |
| GSY | -9.73% | maturity:8.7y |
| H8020 | -9.60% | maturity:7.4y |
| NIBLSTF | -9.36% | maturity:9.8y |
| NICGF2 | -9.28% | maturity:4.5y |
| GBIMESY2 | -9.18% | maturity:9.2y |
| C30MF | -8.10% | maturity:7.0y |
| RBBF40 | -7.40% | maturity:11.5y |
| SFMF | -7.08% | liquidity:low |
| NIBSF2 | -6.24% | maturity:5.0y |
| NIBLGF | -5.23% | liquidity:low; maturity:6.7y |
| MMF1 | -4.81% | maturity:5.3y |
| SAGF | -4.37% | maturity:7.5y |
| NBF3 | -4.17% | maturity:5.4y |
| CMF2 | -3.99% | valuation:small_discount |
| HLICF | -2.15% | valuation:small_discount; maturity:9.3y |
| NMB50 | -2.14% | valuation:small_discount; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 31
- NAV data age: median 28 days, max 349 days

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
