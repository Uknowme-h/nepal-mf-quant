# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-11 11:01*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-11 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 37 |
| At Premium (price ≥ NAV) | 4 |
| Deep Discount (≤ -8%) | 5 |
| Median Discount | -5.11% |
| CONSIDER | 5 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 4 | 9.8% |
| -10% to -6% | 12 | 29.3% |
| -6% to -4% | 10 | 24.4% |
| -4% to 0% | 11 | 26.8% |
| ≥ 0% (premium) | 4 | 9.8% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.50 | -7.08% | 3.6y | medium | 3d | -2.04% | 64.8 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 12.05 | 11.51 | -4.48% | 2.3y | high | 11d | 0.17% | 64.5 | ↑ narrowing | — |
| 3 | NICBF | NIC ASIA Balanced Fund | 10.04 | 9.34 | -6.97% | 3.5y | medium | 1d | 3.83% | 56.2 | ↓ widening | — |
| 4 | SEF | Siddhartha Equity Fund | 10.05 | 9.56 | -4.88% | 1.7y | high | 1d | 0.30% | 52.9 | → stable | — |
| 5 | SLCF | Sanima Large Cap Fund | 10.15 | 9.60 | -5.42% | 2.0y | medium | 1d | 0.30% | 47.4 | ↓ widening | — |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 15 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -15.26% | maturity:5.0y |
| LUK | -14.32% | liquidity:low; maturity:4.4y |
| LVF2 | -12.97% | liquidity:low; maturity:7.5y |
| SFEF | -11.64% | maturity:5.9y |
| GIBF1 | -8.57% | maturity:6.4y |
| NMBHF2 | -7.81% | liquidity:low; maturity:9.0y |
| NICGF2 | -7.40% | maturity:4.7y |
| GSY | -6.94% | maturity:8.8y |
| NSIF2 | -6.71% | maturity:6.5y |
| KDBY | -6.68% | maturity:6.4y |
| PRSF | -6.57% | maturity:6.0y |
| RMF2 | -6.53% | liquidity:low; maturity:7.2y |
| RSY | -6.41% | maturity:9.2y |
| NBF3 | -6.01% | maturity:5.5y |
| NICFC | -5.99% | liquidity:low |
| NBF2 | -5.44% | liquidity:low |
| KEF | -5.26% | maturity:5.0y |
| MNMF1 | -5.11% | maturity:8.8y |
| C30MF | -4.15% | maturity:7.2y |
| MBLEF | -4.02% | maturity:11.1y |
| SAGF | -4.01% | liquidity:low; maturity:7.7y |
| GBIMESY2 | -3.94% | valuation:small_discount; liquidity:low; maturity:9.4y |
| SIGS3 | -3.61% | valuation:small_discount; maturity:7.1y |
| RBBF40 | -3.54% | valuation:small_discount; liquidity:low; maturity:11.7y |
| NIBSF2 | -3.26% | valuation:small_discount; maturity:5.2y |
| NIBLSTF | -3.07% | valuation:small_discount; maturity:9.9y |
| KSY | -2.83% | valuation:small_discount; maturity:8.0y |
| H8020 | -2.56% | valuation:small_discount; maturity:7.6y |
| SIGS2 | -2.49% | valuation:small_discount; liquidity:low |
| RMF1 | -2.29% | valuation:small_discount |
| HLICF | -0.63% | valuation:small_discount; maturity:9.5y |
| NICSF | -0.31% | valuation:small_discount |
| MMF1 | 0.21% | valuation:premium; maturity:5.5y |
| NMB50 | 0.39% | valuation:premium |
| NIBLGF | 1.12% | valuation:premium; maturity:6.9y |
| CMF2 | 1.65% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 11
- NAV data age: median 24 days, max 286 days

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
