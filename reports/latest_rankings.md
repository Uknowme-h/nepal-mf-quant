# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-07 10:41*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-03 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 11 |
| Median Discount | -6.90% |
| CONSIDER | 4 |
| IGNORE | 37 |

> ⚠️ **NAV Staleness Warning**: 14 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 5 | 12.2% |
| -10% to -6% | 20 | 48.8% |
| -6% to -4% | 7 | 17.1% |
| -4% to 0% | 7 | 17.1% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 12.03 | 11.20 | -6.90% | 2.3y | high | 8d | 3.35% | 65.8 | ↑ narrowing | — |
| 2 | SLCF | Sanima Large Cap Fund | 10.15 | 9.68 | -4.63% | 2.0y | medium | 1d | 0.30% | 58.2 | ↑ narrowing | — |
| 3 | NBF2 | Nabil Balanced Fund - 2 | 10.42 | 9.72 | -6.72% | 3.2y | medium | 5d | 2.26% | 55.6 | ↑ narrowing | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.03 | 9.58 | -4.49% | 2.4y | medium | 1d | 0.10% | 36.2 | ↓ widening | high_vol |

## IGNORE Summary

*37 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 9 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -16.81% | liquidity:low; maturity:4.5y |
| SBCF | -15.17% | liquidity:low; maturity:5.1y |
| LVF2 | -14.20% | maturity:7.5y |
| SFEF | -13.12% | maturity:6.0y |
| SFMF | -10.97% | liquidity:low |
| SIGS2 | -9.00% | liquidity:low |
| NMBHF2 | -8.97% | maturity:9.0y |
| KDBY | -8.87% | maturity:6.4y |
| NSIF2 | -8.68% | liquidity:low; maturity:6.5y |
| NICGF2 | -8.58% | maturity:4.7y |
| GIBF1 | -8.15% | maturity:6.4y |
| MBLEF | -7.50% | maturity:11.1y |
| GSY | -7.43% | maturity:8.8y |
| PRSF | -7.40% | maturity:6.0y |
| C30MF | -7.36% | maturity:7.2y |
| MNMF1 | -7.32% | maturity:8.8y |
| NIBSF2 | -7.23% | maturity:5.2y |
| GBIMESY2 | -7.16% | maturity:9.4y |
| RSY | -7.15% | maturity:9.2y |
| KEF | -7.14% | maturity:5.0y |
| RMF2 | -6.72% | maturity:7.2y |
| KSY | -6.63% | liquidity:low; maturity:8.1y |
| SIGS3 | -6.21% | liquidity:low; maturity:7.2y |
| NBF3 | -5.88% | maturity:5.6y |
| NIBLSTF | -5.83% | maturity:9.9y |
| SAGF | -5.53% | liquidity:low; maturity:7.7y |
| RBBF40 | -4.55% | maturity:11.7y |
| NICBF | -4.28% | liquidity:low |
| NICFC | -3.99% | valuation:small_discount |
| HLICF | -3.97% | valuation:small_discount; liquidity:low; maturity:9.5y |
| SEF | -3.48% | valuation:small_discount |
| CMF2 | -1.75% | valuation:small_discount |
| MMF1 | -1.57% | valuation:small_discount; maturity:5.5y |
| H8020 | -1.40% | valuation:small_discount; maturity:7.6y |
| NICSF | -0.52% | valuation:small_discount |
| NIBLGF | 1.12% | valuation:premium; maturity:6.9y |
| NMB50 | 2.03% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 41
- Symbols with issues: 19
- NAV data age: median 20 days, max 282 days

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
