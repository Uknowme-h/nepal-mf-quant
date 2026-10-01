# Nepal MF Quant — Full Analysis Report

*Generated: 2026-10-01 17:06*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-10-01 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 36 |
| Median Discount | -11.24% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 24 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 30 | 76.9% |
| -10% to -6% | 8 | 20.5% |
| -6% to -4% | 0 | 0.0% |
| -4% to 0% | 1 | 2.6% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.09 | 10.90 | -16.73% | 1.7y | medium | 80d | 0.38% | 74.6 | → stable | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.98 | -12.82% | 2.7y | medium | 1d | 0.88% | 71.7 | ↑ narrowing | — |
| 3 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.11 | -19.38% | 3.1y | medium | 4d | -2.04% | 62.8 | ↓ widening | — |
| 4 | LUK | Laxmi Unnati Kosh | 11.66 | 9.30 | -20.24% | 3.9y | medium | 2d | -1.17% | 60.6 | ↓ widening | — |
| 5 | SLCF | Sanima Large Cap Fund | 10.14 | 9.12 | -10.06% | 1.4y | high | 2d | -2.12% | 57.8 | ↑ narrowing | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.22 | 9.01 | -11.84% | 1.8y | medium | 5d | -0.87% | 50.2 | ↓ widening | high_vol |
| 7 | NICSF | NIC Asia Select-30 | 9.28 | 8.50 | -8.41% | 1.8y | medium | 7d | -2.11% | 37.6 | ↓ widening | high_vol |
| 8 | SEF | Siddhartha Equity Fund | 10.36 | 9.60 | -7.34% | 1.1y | medium | 28d | -2.72% | 36.9 | ↓ widening | — |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 1 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -21.26% | maturity:5.4y |
| LVF2 | -19.81% | liquidity:low; maturity:6.9y |
| SBCF | -18.96% | maturity:4.5y |
| GIBF1 | -14.82% | maturity:5.8y |
| RMF2 | -14.71% | maturity:6.6y |
| NICGF2 | -14.62% | maturity:4.1y |
| NMBHF2 | -14.30% | liquidity:low; maturity:8.4y |
| NSIF2 | -13.69% | maturity:5.9y |
| PRSF | -13.64% | maturity:5.5y |
| NICBF | -12.79% | liquidity:low |
| H8020 | -11.89% | maturity:7.0y |
| SIGS2 | -11.87% | liquidity:low |
| NBF2 | -11.84% | liquidity:low |
| MNMF1 | -11.47% | maturity:8.2y |
| NBF3 | -11.24% | maturity:5.0y |
| NIBSF2 | -11.21% | liquidity:low; maturity:4.7y |
| SAGF | -11.15% | liquidity:low; maturity:7.2y |
| RSY | -10.77% | liquidity:low; maturity:8.6y |
| SIGS3 | -10.48% | maturity:6.6y |
| C30MF | -10.47% | maturity:6.6y |
| NIBLGF | -10.47% | maturity:6.3y |
| NIBLSTF | -10.38% | maturity:9.4y |
| MBLEF | -10.36% | liquidity:low; maturity:10.5y |
| GBIMESY2 | -10.00% | maturity:8.8y |
| RBBF40 | -9.91% | maturity:11.1y |
| KSY | -9.27% | maturity:7.5y |
| KDBY | -8.69% | maturity:5.8y |
| GSY | -8.53% | maturity:8.3y |
| KEF | -8.42% | maturity:4.5y |
| MMF1 | -7.89% | maturity:4.9y |
| HLICF | -2.80% | valuation:small_discount; liquidity:low; maturity:9.0y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 39
- NAV data age: median 46 days, max 490 days

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
