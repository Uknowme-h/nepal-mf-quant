# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-29 14:20*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-29 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 22 |
| Median Discount | -8.43% |
| CONSIDER | 5 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 13 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 16 | 39.0% |
| -10% to -6% | 13 | 31.7% |
| -6% to -4% | 4 | 9.8% |
| -4% to 0% | 7 | 17.1% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 11.76 | -14.10% | 2.0y | high | 19d | -4.60% | 64.8 | ↓ widening | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.07 | -12.70% | 3.0y | medium | 1d | -1.24% | 58.0 | ↓ widening | — |
| 3 | SIGS2 | Siddhartha Investment Gro | 11.23 | 10.50 | -6.50% | 3.2y | medium | 6d | -2.60% | 51.0 | → stable | — |
| 4 | NMB50 | NMB 50 | 10.60 | 10.08 | -4.91% | 0.2y | medium | 1d | 0.57% | 50.2 | ↓ widening | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.41 | 9.75 | -6.34% | 2.1y | high | 1d | -2.16% | 42.9 | ↓ widening | high_vol |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 8 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| KDBY | -16.08% | maturity:6.1y |
| PRSF | -15.63% | maturity:5.7y |
| LUK | -13.81% | maturity:4.1y |
| NICBF | -12.91% | liquidity:low |
| SFEF | -12.51% | maturity:5.6y |
| LVF2 | -12.36% | maturity:7.2y |
| NICGF2 | -12.13% | maturity:4.4y |
| SBCF | -11.82% | maturity:4.7y |
| GIBF1 | -11.59% | maturity:6.1y |
| RSY | -11.57% | maturity:8.8y |
| NSIF2 | -11.40% | liquidity:low; maturity:6.2y |
| SIGS3 | -10.85% | maturity:6.8y |
| KEF | -10.16% | maturity:4.7y |
| H8020 | -10.13% | maturity:7.3y |
| MBLEF | -9.63% | maturity:10.8y |
| GBIMESY2 | -9.38% | liquidity:low; maturity:9.1y |
| NMBHF2 | -8.62% | maturity:8.7y |
| RBBF40 | -8.60% | liquidity:low; maturity:11.4y |
| RMF2 | -8.43% | maturity:6.9y |
| NIBSF2 | -8.21% | maturity:4.9y |
| C30MF | -7.62% | maturity:6.9y |
| KSY | -7.28% | maturity:7.7y |
| SAGF | -7.15% | maturity:7.4y |
| SFMF | -7.08% | liquidity:low |
| MNMF1 | -7.01% | liquidity:low; maturity:8.5y |
| NIBLSTF | -4.52% | maturity:9.6y |
| GSY | -4.49% | maturity:8.5y |
| NIBLGF | -4.43% | liquidity:low; maturity:6.6y |
| NICSF | -3.21% | valuation:small_discount |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.2y |
| NBF2 | -2.96% | valuation:small_discount; liquidity:low |
| SEF | -1.69% | valuation:small_discount; liquidity:low |
| CMF2 | -1.27% | valuation:small_discount |
| MMF1 | -1.03% | valuation:small_discount; maturity:5.2y |
| SLCF | -0.39% | valuation:small_discount |
| HLICF | 0.45% | valuation:premium; liquidity:low; maturity:9.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 23
- NAV data age: median 45 days, max 396 days

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
