# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-10 14:25*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-10 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 32 |
| Median Discount | -13.52% |
| CONSIDER | 7 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 29 | 74.4% |
| -10% to -6% | 4 | 10.3% |
| -6% to -4% | 4 | 10.3% |
| -4% to 0% | 2 | 5.1% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.09 | 10.89 | -16.81% | 1.8y | high | 67d | 0.38% | 67.7 | ↓ widening | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.79 | -14.66% | 2.8y | medium | 6d | 0.88% | 59.5 | → stable | — |
| 3 | SIGS2 | Siddhartha Investment Gro | 10.95 | 9.66 | -11.78% | 3.0y | medium | 1d | -3.30% | 57.4 | ↑ narrowing | — |
| 4 | SEF | Siddhartha Equity Fund | 10.36 | 9.58 | -7.53% | 1.2y | high | 15d | -2.72% | 51.0 | ↑ narrowing | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.31 | 9.41 | -8.73% | 1.9y | medium | 9d | -1.63% | 47.7 | ↑ narrowing | high_vol |
| 6 | NICSF | NIC Asia Select-30 | 9.48 | 8.25 | -12.97% | 1.8y | medium | 1d | -3.27% | 47.4 | → stable | — |
| 7 | SLCF | Sanima Large Cap Fund | 10.14 | 9.00 | -11.24% | 1.4y | medium | 2d | -2.12% | 43.0 | ↓ widening | — |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 2 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -20.25% | maturity:7.0y |
| SBCF | -20.19% | liquidity:low; maturity:4.5y |
| SFMF | -18.58% | liquidity:low |
| KDBY | -17.30% | maturity:5.9y |
| KEF | -17.19% | maturity:4.5y |
| RSY | -17.03% | maturity:8.7y |
| NICBF | -16.38% | liquidity:low |
| MBLEF | -16.19% | maturity:10.6y |
| LUK | -16.12% | liquidity:low |
| SFEF | -16.10% | liquidity:low; maturity:5.4y |
| PRSF | -16.01% | maturity:5.5y |
| NSIF2 | -15.31% | maturity:6.0y |
| KSY | -14.34% | liquidity:low; maturity:7.5y |
| NIBLSTF | -14.27% | maturity:9.4y |
| NIBSF2 | -14.11% | maturity:4.7y |
| NICGF2 | -13.85% | maturity:4.2y |
| NIBLGF | -13.69% | maturity:6.4y |
| MNMF1 | -13.52% | maturity:8.3y |
| NMBHF2 | -13.15% | maturity:8.5y |
| SIGS3 | -12.73% | maturity:6.6y |
| GBIMESY2 | -11.38% | liquidity:low; maturity:8.9y |
| SAGF | -10.82% | liquidity:low; maturity:7.2y |
| RMF2 | -10.63% | liquidity:low; maturity:6.7y |
| GSY | -10.44% | maturity:8.3y |
| NBF3 | -8.91% | maturity:5.0y |
| RBBF40 | -8.64% | maturity:11.2y |
| MMF1 | -5.23% | maturity:5.0y |
| C30MF | -5.19% | maturity:6.7y |
| GIBF1 | -4.50% | maturity:5.9y |
| NBF2 | -4.49% | liquidity:low |
| HLICF | -2.88% | valuation:small_discount; maturity:9.0y |
| H8020 | -2.71% | valuation:small_discount; maturity:7.1y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 25
- NAV data age: median 26 days, max 469 days

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
