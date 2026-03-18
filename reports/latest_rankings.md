# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-18 11:09*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-17 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 5 |
| Median Discount | -4.76% |
| CONSIDER | 1 |
| IGNORE | 40 |

> ⚠️ **NAV Staleness Warning**: 5 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 3 | 7.3% |
| -10% to -6% | 9 | 22.0% |
| -6% to -4% | 16 | 39.0% |
| -4% to 0% | 11 | 26.8% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SIGS2 | Siddhartha Investment Gro | 10.44 | 9.80 | -6.13% | 3.5y | medium | 3d | 0.29% | 69.6 | ↑ narrowing | — |

## IGNORE Summary

*40 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 13 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -14.99% | maturity:5.0y |
| LUK | -14.75% | maturity:4.4y |
| LVF2 | -12.80% | maturity:7.5y |
| NICGF2 | -8.97% | liquidity:low; maturity:4.7y |
| SFEF | -8.84% | maturity:5.9y |
| SFMF | -7.96% | liquidity:low |
| NICFC | -6.84% | liquidity:low |
| MNMF1 | -6.55% | maturity:8.8y |
| NSIF2 | -6.45% | maturity:6.5y |
| PRSF | -6.25% | liquidity:low; maturity:6.0y |
| KDBY | -6.22% | maturity:6.4y |
| NBF3 | -5.91% | maturity:5.5y |
| MBLEF | -5.85% | maturity:11.0y |
| GIBF1 | -5.77% | maturity:6.4y |
| GBIMESY2 | -5.65% | liquidity:low; maturity:9.3y |
| KSY | -5.57% | maturity:8.0y |
| NMBHF2 | -5.50% | maturity:9.0y |
| SAGF | -4.84% | liquidity:low; maturity:7.7y |
| NBF2 | -4.78% | liquidity:low |
| KEF | -4.76% | maturity:5.0y |
| H8020 | -4.70% | maturity:7.5y |
| NIBSF2 | -4.58% | maturity:5.2y |
| GSY | -4.53% | maturity:8.8y |
| C30MF | -4.43% | maturity:7.2y |
| RMF2 | -4.38% | liquidity:low; maturity:7.2y |
| SIGS3 | -4.36% | maturity:7.1y |
| NIBLSTF | -4.30% | maturity:9.9y |
| PSF | -3.73% | valuation:small_discount |
| NIBLGF | -3.37% | valuation:small_discount; maturity:6.8y |
| RSY | -2.97% | valuation:small_discount; maturity:9.1y |
| SLCF | -2.46% | valuation:small_discount |
| RBBF40 | -2.42% | valuation:small_discount; liquidity:low; maturity:11.7y |
| RMF1 | -2.29% | valuation:small_discount |
| NICSF | -2.20% | valuation:small_discount |
| MMF1 | -1.36% | valuation:small_discount; maturity:5.5y |
| HLICF | -0.84% | valuation:small_discount; liquidity:low; maturity:9.5y |
| CMF2 | -0.58% | valuation:small_discount |
| NICBF | -0.50% | valuation:small_discount |
| NMB50 | 0.10% | valuation:premium |
| SEF | 0.90% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 9
- NAV data age: median 31 days, max 293 days

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
