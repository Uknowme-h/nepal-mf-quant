# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-19 13:50*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-19 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 17 |
| Median Discount | -6.62% |
| CONSIDER | 3 |
| IGNORE | 38 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 12 | 29.3% |
| -10% to -6% | 14 | 34.1% |
| -6% to -4% | 5 | 12.2% |
| -4% to 0% | 9 | 22.0% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.32 | -10.30% | 3.0y | medium | 9d | -1.24% | 70.5 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 13.69 | 12.20 | -10.88% | 2.0y | high | 13d | -4.60% | 65.8 | → stable | — |
| 3 | NICSF | NIC Asia Select-30 | 9.66 | 9.23 | -4.45% | 2.0y | medium | 1d | -2.33% | 38.7 | ↓ widening | — |

## IGNORE Summary

*38 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -15.03% | maturity:5.7y |
| LUK | -14.24% | maturity:4.2y |
| SBCF | -13.84% | maturity:4.8y |
| LVF2 | -13.50% | liquidity:low; maturity:7.2y |
| KDBY | -12.67% | maturity:6.1y |
| GIBF1 | -11.68% | maturity:6.1y |
| SFEF | -11.64% | liquidity:low; maturity:5.7y |
| SIGS3 | -11.61% | maturity:6.9y |
| NSIF2 | -10.55% | maturity:6.2y |
| KEF | -10.49% | maturity:4.8y |
| RSY | -9.45% | maturity:8.9y |
| NICBF | -9.34% | liquidity:low |
| NICGF2 | -8.79% | maturity:4.4y |
| MBLEF | -8.27% | maturity:10.8y |
| NMBHF2 | -8.14% | maturity:8.7y |
| RMF2 | -7.52% | liquidity:low; maturity:6.9y |
| SAGF | -7.15% | maturity:7.5y |
| GBIMESY2 | -7.04% | maturity:9.1y |
| RBBF40 | -6.62% | liquidity:low; maturity:11.4y |
| C30MF | -6.60% | maturity:6.9y |
| MNMF1 | -6.54% | maturity:8.5y |
| NIBLSTF | -6.37% | maturity:9.6y |
| NIBSF2 | -6.08% | maturity:5.0y |
| KSY | -6.07% | maturity:7.8y |
| NIBLGF | -5.94% | maturity:6.6y |
| RMF1 | -5.76% | liquidity:low |
| H8020 | -5.30% | maturity:7.3y |
| GSY | -4.49% | maturity:8.6y |
| SIGS2 | -3.83% | valuation:small_discount; liquidity:low |
| NBF3 | -3.59% | valuation:small_discount; maturity:5.3y |
| NBF2 | -3.53% | valuation:small_discount |
| SEF | -3.29% | valuation:small_discount; liquidity:low |
| MMF1 | -2.58% | valuation:small_discount; maturity:5.2y |
| SFMF | -2.57% | valuation:small_discount |
| SLCF | -2.32% | valuation:small_discount |
| CMF2 | -1.37% | valuation:small_discount; liquidity:low |
| HLICF | -0.34% | valuation:small_discount; maturity:9.2y |
| NMB50 | 1.52% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 25
- NAV data age: median 35 days, max 386 days

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
