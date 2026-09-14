# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-14 16:23*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-14 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 33 |
| Median Discount | -12.79% |
| CONSIDER | 9 |
| IGNORE | 30 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 27 | 69.2% |
| -10% to -6% | 8 | 20.5% |
| -6% to -4% | 2 | 5.1% |
| -4% to 0% | 2 | 5.1% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | LUK | Laxmi Unnati Kosh | 11.66 | 9.28 | -20.41% | 3.9y | medium | 2d | -1.17% | 72.6 | ↓ widening | — |
| 2 | PSF | Prabhu Select Fund | 13.09 | 10.84 | -17.19% | 1.8y | high | 69d | 0.38% | 65.6 | ↓ widening | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.60 | -16.50% | 2.8y | medium | 1d | 0.88% | 63.3 | ↓ widening | — |
| 4 | NICSF | NIC Asia Select-30 | 9.48 | 8.60 | -9.28% | 1.8y | medium | 3d | -3.27% | 52.6 | ↑ narrowing | — |
| 5 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.60 | -8.31% | 2.7y | high | 2d | 0.48% | 52.3 | ↓ widening | — |
| 6 | SEF | Siddhartha Equity Fund | 10.36 | 9.56 | -7.72% | 1.1y | high | 17d | -2.72% | 52.0 | ↑ narrowing | — |
| 7 | SIGS2 | Siddhartha Investment Gro | 10.95 | 9.55 | -12.79% | 3.0y | medium | 1d | -3.30% | 50.9 | ↓ widening | — |
| 8 | SLCF | Sanima Large Cap Fund | 10.14 | 9.20 | -9.27% | 1.4y | medium | 1d | -2.12% | 50.0 | ↑ narrowing | — |
| 9 | RMF1 | RBB Mutual Fund 1 | 10.31 | 9.40 | -8.83% | 1.9y | medium | 11d | -1.63% | 38.1 | ↓ widening | high_vol |

## IGNORE Summary

*30 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 8 |
| valuation | 2 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -20.38% | maturity:5.4y |
| LVF2 | -20.25% | liquidity:low; maturity:7.0y |
| RSY | -18.80% | maturity:8.6y |
| SFMF | -18.58% | liquidity:low |
| NICGF2 | -18.56% | maturity:4.2y |
| NICBF | -17.93% | liquidity:low |
| SBCF | -17.72% | maturity:4.5y |
| KEF | -17.19% | maturity:4.5y |
| KDBY | -16.39% | maturity:5.9y |
| MBLEF | -15.65% | maturity:10.5y |
| PRSF | -15.58% | maturity:5.5y |
| NMBHF2 | -14.40% | maturity:8.5y |
| KSY | -14.34% | liquidity:low; maturity:7.5y |
| NIBLGF | -13.79% | maturity:6.3y |
| NSIF2 | -13.77% | maturity:6.0y |
| NIBSF2 | -13.71% | maturity:4.7y |
| MNMF1 | -12.27% | maturity:8.3y |
| RBBF40 | -12.12% | liquidity:low; maturity:11.2y |
| SIGS3 | -11.95% | liquidity:low; maturity:6.6y |
| GBIMESY2 | -11.88% | maturity:8.8y |
| SAGF | -11.15% | maturity:7.2y |
| NIBLSTF | -10.81% | maturity:9.4y |
| RMF2 | -10.63% | liquidity:low; maturity:6.7y |
| GSY | -9.54% | maturity:8.3y |
| NBF3 | -9.30% | maturity:5.0y |
| MMF1 | -7.11% | maturity:5.0y |
| C30MF | -5.38% | maturity:6.7y |
| HLICF | -5.18% | liquidity:low; maturity:9.0y |
| GIBF1 | -1.61% | valuation:small_discount; maturity:5.9y |
| H8020 | -0.48% | valuation:small_discount; maturity:7.0y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 30
- NAV data age: median 30 days, max 473 days

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
