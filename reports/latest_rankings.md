# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-26 11:13*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-26 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 32 |
| At Premium (price ≥ NAV) | 9 |
| Deep Discount (≤ -8%) | 5 |
| Median Discount | -2.22% |
| CONSIDER | 2 |
| IGNORE | 39 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 3 | 7.3% |
| -10% to -6% | 2 | 4.9% |
| -6% to -4% | 5 | 12.2% |
| -4% to 0% | 23 | 56.1% |
| ≥ 0% (premium) | 8 | 19.5% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.30 | -8.85% | 3.6y | medium | 1d | -2.04% | 59.0 | ↓ widening | — |
| 2 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.05 | -4.01% | 3.2y | medium | 3d | 0.48% | 55.7 | → stable | — |

## IGNORE Summary

*39 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| valuation | 31 |
| maturity | 29 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -13.46% | liquidity:low; maturity:4.4y |
| LVF2 | -12.36% | liquidity:low; maturity:7.5y |
| SBCF | -10.67% | maturity:5.0y |
| SFEF | -8.40% | maturity:5.9y |
| RSY | -4.83% | maturity:9.1y |
| KSY | -4.59% | liquidity:low; maturity:8.0y |
| NMBHF2 | -4.24% | maturity:8.9y |
| RMF2 | -4.01% | liquidity:low; maturity:7.2y |
| GIBF1 | -3.90% | valuation:small_discount; maturity:6.3y |
| NSIF2 | -3.70% | valuation:small_discount; maturity:6.4y |
| GSY | -3.47% | valuation:small_discount; maturity:8.8y |
| NICGF2 | -3.45% | valuation:small_discount; maturity:4.7y |
| C30MF | -3.30% | valuation:small_discount; maturity:7.1y |
| MBLEF | -3.11% | valuation:small_discount; maturity:11.0y |
| NICFC | -2.87% | valuation:small_discount |
| MNMF1 | -2.79% | valuation:small_discount; maturity:8.7y |
| NIBSF2 | -2.75% | valuation:small_discount; maturity:5.2y |
| SIGS2 | -2.49% | valuation:small_discount |
| SIGS3 | -2.22% | valuation:small_discount; liquidity:low; maturity:7.1y |
| NBF3 | -2.13% | valuation:small_discount; maturity:5.5y |
| GBIMESY2 | -2.12% | valuation:small_discount; liquidity:low; maturity:9.3y |
| SLCF | -2.07% | valuation:small_discount |
| PRSF | -1.79% | valuation:small_discount; maturity:6.0y |
| KDBY | -1.56% | valuation:small_discount; maturity:6.3y |
| RMF1 | -1.30% | valuation:small_discount |
| SAGF | -1.23% | valuation:small_discount; maturity:7.7y |
| H8020 | -0.99% | valuation:small_discount; liquidity:low; maturity:7.5y |
| NIBLSTF | -0.72% | valuation:small_discount; maturity:9.9y |
| NIBLGF | -0.51% | valuation:small_discount; maturity:6.8y |
| RBBF40 | -0.51% | valuation:small_discount; liquidity:low; maturity:11.6y |
| PSF | 0.00% | valuation:premium |
| NICSF | 0.21% | valuation:premium |
| HLICF | 0.42% | valuation:premium; liquidity:low; maturity:9.5y |
| KEF | 0.69% | valuation:premium; maturity:5.0y |
| CMF2 | 0.78% | valuation:premium |
| MMF1 | 2.30% | valuation:premium; maturity:5.5y |
| SEF | 2.69% | valuation:premium; liquidity:low |
| NMB50 | 3.68% | valuation:premium |
| NICBF | 5.18% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 9
- NAV data age: median 39 days, max 301 days

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
