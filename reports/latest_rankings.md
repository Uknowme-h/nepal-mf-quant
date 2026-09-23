# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-23 15:01*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-23 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 32 |
| Median Discount | -12.91% |
| CONSIDER | 5 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 29 | 74.4% |
| -10% to -6% | 7 | 17.9% |
| -6% to -4% | 1 | 2.6% |
| -4% to 0% | 2 | 5.1% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.09 | 10.93 | -16.50% | 1.8y | high | 75d | 0.38% | 69.0 | ↓ widening | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.91 | -13.50% | 2.7y | medium | 3d | 0.88% | 66.2 | ↑ narrowing | — |
| 3 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.25 | -11.65% | 2.7y | high | 2d | 0.48% | 54.0 | ↓ widening | — |
| 4 | NICSF | NIC Asia Select-30 | 9.48 | 8.60 | -9.28% | 1.8y | medium | 2d | -3.27% | 48.1 | ↑ narrowing | — |
| 5 | SEF | Siddhartha Equity Fund | 10.36 | 9.70 | -6.37% | 1.1y | medium | 23d | -2.72% | 37.3 | ↓ widening | — |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 2 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -21.96% | maturity:5.4y |
| SBCF | -20.63% | maturity:4.5y |
| LVF2 | -19.81% | maturity:7.0y |
| SFMF | -18.41% | liquidity:low |
| NICGF2 | -16.35% | maturity:4.2y |
| LUK | -16.21% | liquidity:low |
| KEF | -16.03% | maturity:4.5y |
| RSY | -15.53% | maturity:8.6y |
| PRSF | -15.51% | maturity:5.5y |
| KDBY | -15.31% | maturity:5.8y |
| MBLEF | -14.91% | maturity:10.5y |
| NICBF | -14.73% | liquidity:low |
| KSY | -14.15% | liquidity:low; maturity:7.5y |
| NSIF2 | -13.77% | maturity:6.0y |
| SIGS2 | -13.61% | liquidity:low |
| NIBSF2 | -13.50% | maturity:4.7y |
| H8020 | -13.08% | maturity:7.0y |
| NIBLSTF | -12.91% | maturity:9.4y |
| NIBLGF | -12.68% | maturity:6.3y |
| NMBHF2 | -12.67% | maturity:8.4y |
| MNMF1 | -12.27% | maturity:8.2y |
| SLCF | -11.24% | liquidity:low |
| SIGS3 | -11.08% | liquidity:low; maturity:6.6y |
| SAGF | -11.06% | liquidity:low; maturity:7.2y |
| RBBF40 | -11.02% | maturity:11.2y |
| NBF3 | -10.56% | liquidity:low; maturity:5.0y |
| RMF1 | -9.89% | liquidity:low |
| RMF2 | -8.07% | maturity:6.7y |
| MMF1 | -7.95% | maturity:5.0y |
| GSY | -7.53% | maturity:8.3y |
| GBIMESY2 | -6.75% | maturity:8.8y |
| C30MF | -4.72% | maturity:6.6y |
| HLICF | -3.22% | valuation:small_discount; maturity:9.0y |
| GIBF1 | -2.38% | valuation:small_discount; maturity:5.8y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 28
- NAV data age: median 39 days, max 482 days

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
