# Nepal MF Quant — Full Analysis Report

*Generated: 2026-10-26 16:48*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-10-26 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 22 |
| Median Discount | -8.64% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 13 | 33.3% |
| -10% to -6% | 20 | 51.3% |
| -6% to -4% | 4 | 10.3% |
| -4% to 0% | 2 | 5.1% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.08 | -13.28% | 2.6y | medium | 7d | 0.48% | 68.5 | → stable | — |
| 2 | RMF1 | RBB Mutual Fund 1 | 10.22 | 9.10 | -10.96% | 1.7y | high | 15d | -0.87% | 63.9 | → stable | high_vol |
| 3 | SEF | Siddhartha Equity Fund | 10.49 | 9.76 | -6.96% | 1.0y | high | 8d | 1.06% | 58.7 | → stable | — |
| 4 | NICFC | NIC Asia Flexi Cap Fund | 9.94 | 9.03 | -9.15% | 2.6y | high | 1d | -1.29% | 55.6 | ↓ widening | — |
| 5 | SLCF | Sanima Large Cap Fund | 10.04 | 9.30 | -7.37% | 1.3y | medium | 2d | -0.99% | 54.2 | ↑ narrowing | — |
| 6 | SIGS2 | Siddhartha Investment Gro | 10.31 | 9.80 | -4.95% | 2.8y | medium | 1d | -5.84% | 49.0 | ↑ narrowing | — |
| 7 | NICSF | NIC Asia Select-30 | 9.28 | 8.49 | -8.51% | 1.7y | medium | 17d | -2.11% | 46.3 | → stable | high_vol |
| 8 | PSF | Prabhu Select Fund | 12.00 | 11.00 | -8.33% | 1.6y | medium | 7d | -8.33% | 46.3 | → stable | — |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 2 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -19.34% | maturity:5.3y |
| LVF2 | -19.11% | liquidity:low; maturity:6.9y |
| SBCF | -18.78% | maturity:4.4y |
| LUK | -15.52% | liquidity:low |
| SFMF | -13.72% | liquidity:low |
| GIBF1 | -12.95% | liquidity:low; maturity:5.8y |
| NBF3 | -11.82% | maturity:4.9y |
| RMF2 | -11.47% | maturity:6.6y |
| KSY | -10.38% | liquidity:low; maturity:7.4y |
| MNMF1 | -10.29% | maturity:8.2y |
| NICGF2 | -10.03% | maturity:4.1y |
| NIBLGF | -9.96% | maturity:6.2y |
| NICBF | -9.49% | liquidity:low |
| H8020 | -9.42% | maturity:6.9y |
| C30MF | -9.09% | maturity:6.5y |
| SAGF | -8.80% | liquidity:low; maturity:7.1y |
| NIBSF2 | -8.64% | liquidity:low; maturity:4.6y |
| RSY | -7.88% | maturity:8.5y |
| NIBLSTF | -7.52% | maturity:9.3y |
| GBIMESY2 | -7.50% | liquidity:low; maturity:8.7y |
| MMF1 | -7.37% | maturity:4.9y |
| KDBY | -7.15% | maturity:5.8y |
| KEF | -6.95% | maturity:4.4y |
| PRSF | -6.84% | liquidity:low; maturity:5.4y |
| GSY | -6.61% | maturity:8.2y |
| MBLEF | -6.31% | maturity:10.4y |
| RBBF40 | -5.81% | maturity:11.1y |
| NMBHF2 | -5.75% | maturity:8.3y |
| NSIF2 | -5.03% | maturity:5.8y |
| SIGS3 | -3.82% | valuation:small_discount; maturity:6.5y |
| HLICF | -1.40% | valuation:small_discount; maturity:8.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 31
- NAV data age: median 41 days, max 515 days

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
