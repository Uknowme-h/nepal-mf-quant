# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-08 14:33*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-07 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 30 |
| Median Discount | -11.69% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 26 | 66.7% |
| -10% to -6% | 8 | 20.5% |
| -6% to -4% | 3 | 7.7% |
| -4% to 0% | 2 | 5.1% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | LUK | Laxmi Unnati Kosh | 11.66 | 9.50 | -18.52% | 3.9y | medium | 1d | -1.17% | 68.0 | ↓ widening | — |
| 2 | PSF | Prabhu Select Fund | 13.09 | 12.28 | -6.19% | 1.8y | high | 65d | 0.38% | 61.1 | ↑ narrowing | — |
| 3 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.02 | -20.18% | 3.2y | medium | 4d | -2.04% | 60.6 | ↓ widening | — |
| 4 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.77 | -14.85% | 2.8y | medium | 4d | 0.88% | 59.0 | ↓ widening | — |
| 5 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.82 | -6.21% | 2.7y | medium | 3d | 0.48% | 57.0 | ↑ narrowing | — |
| 6 | SEF | Siddhartha Equity Fund | 10.36 | 9.41 | -9.17% | 1.2y | high | 13d | -2.72% | 56.9 | ↑ narrowing | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.31 | 9.70 | -5.92% | 1.9y | medium | 7d | -1.63% | 45.9 | ↑ narrowing | high_vol |
| 8 | NICSF | NIC Asia Select-30 | 9.48 | 8.35 | -11.92% | 1.8y | medium | 3d | -3.27% | 44.2 | ↓ widening | — |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 9 |
| valuation | 2 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -20.28% | maturity:4.5y |
| LVF2 | -18.49% | maturity:7.0y |
| KDBY | -17.30% | maturity:5.9y |
| RSY | -16.42% | maturity:8.7y |
| MBLEF | -16.29% | liquidity:low; maturity:10.6y |
| SFEF | -16.10% | liquidity:low; maturity:5.4y |
| NIBSF2 | -15.74% | maturity:4.7y |
| NSIF2 | -15.57% | maturity:6.0y |
| NICBF | -15.50% | liquidity:low |
| KSY | -15.21% | maturity:7.5y |
| NICGF2 | -14.52% | liquidity:low; maturity:4.2y |
| NIBLGF | -13.79% | maturity:6.4y |
| KEF | -13.18% | maturity:4.5y |
| NIBLSTF | -12.49% | maturity:9.4y |
| MNMF1 | -12.46% | maturity:8.3y |
| SIGS3 | -11.69% | maturity:6.7y |
| SAGF | -11.48% | liquidity:low; maturity:7.2y |
| NMBHF2 | -11.32% | maturity:8.5y |
| RMF2 | -11.09% | liquidity:low; maturity:6.7y |
| SLCF | -10.95% | liquidity:low |
| RBBF40 | -10.63% | maturity:11.2y |
| GBIMESY2 | -10.37% | liquidity:low; maturity:8.9y |
| GSY | -9.64% | maturity:8.3y |
| SIGS2 | -9.22% | liquidity:low |
| PRSF | -8.83% | maturity:5.5y |
| NBF3 | -6.59% | maturity:5.0y |
| C30MF | -6.13% | maturity:6.7y |
| GIBF1 | -5.94% | maturity:5.9y |
| MMF1 | -5.86% | maturity:5.0y |
| HLICF | -2.07% | valuation:small_discount; maturity:9.0y |
| H8020 | -0.48% | valuation:small_discount; maturity:7.1y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 28
- NAV data age: median 24 days, max 467 days

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
