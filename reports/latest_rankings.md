# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-07 11:07*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-07 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 17 |
| Median Discount | -7.45% |
| CONSIDER | 6 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 13 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 7 | 17.5% |
| -10% to -6% | 19 | 47.5% |
| -6% to -4% | 8 | 20.0% |
| -4% to 0% | 5 | 12.5% |
| ≥ 0% (premium) | 1 | 2.5% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 12.00 | -12.34% | 1.9y | medium | 46d | -4.60% | 64.5 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.37 | -9.03% | 2.9y | medium | 2d | 0.88% | 64.5 | ↑ narrowing | — |
| 3 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.20 | -9.73% | 3.2y | medium | 5d | -2.04% | 62.2 | → stable | — |
| 4 | NICSF | NIC Asia Select-30 | 9.55 | 8.90 | -6.81% | 1.9y | medium | 1d | -2.55% | 56.1 | ↑ narrowing | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.28 | 9.67 | -5.93% | 2.0y | high | 15d | -1.63% | 51.1 | ↑ narrowing | high_vol |
| 6 | SEF | Siddhartha Equity Fund | 10.36 | 9.91 | -4.34% | 1.2y | medium | 8d | -2.72% | 45.5 | ↑ narrowing | — |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 6 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -20.60% | maturity:7.1y |
| SBCF | -16.67% | maturity:4.6y |
| PRSF | -13.01% | maturity:5.6y |
| SFEF | -12.69% | maturity:5.5y |
| NICGF2 | -11.73% | liquidity:low; maturity:4.3y |
| NIBSF2 | -10.15% | liquidity:low; maturity:4.8y |
| RMF2 | -9.85% | liquidity:low; maturity:6.8y |
| KDBY | -9.54% | maturity:6.0y |
| RBBF40 | -9.45% | maturity:11.3y |
| GIBF1 | -8.74% | maturity:6.0y |
| LUK | -8.32% | maturity:4.0y |
| GBIMESY2 | -8.26% | maturity:8.9y |
| KEF | -8.22% | maturity:4.6y |
| RSY | -8.06% | maturity:8.7y |
| SIGS3 | -7.78% | liquidity:low; maturity:6.7y |
| KSY | -7.48% | maturity:7.6y |
| NBF3 | -7.46% | maturity:5.1y |
| NMBHF2 | -7.44% | maturity:8.6y |
| NSIF2 | -7.38% | maturity:6.1y |
| NICBF | -7.27% | liquidity:low |
| NIBLSTF | -6.98% | maturity:9.5y |
| MMF1 | -6.33% | maturity:5.1y |
| C30MF | -5.98% | liquidity:low; maturity:6.8y |
| SLCF | -5.56% | liquidity:low |
| MBLEF | -5.25% | maturity:10.6y |
| NIBLGF | -5.23% | liquidity:low; maturity:6.5y |
| GSY | -4.42% | maturity:8.4y |
| MNMF1 | -4.11% | maturity:8.4y |
| NBF2 | -3.53% | valuation:small_discount |
| SAGF | -2.66% | valuation:small_discount; liquidity:low; maturity:7.3y |
| H8020 | -1.37% | valuation:small_discount; maturity:7.2y |
| NMB50 | -0.67% | valuation:small_discount |
| SIGS2 | -0.46% | valuation:small_discount; liquidity:low |
| HLICF | 2.41% | valuation:premium; maturity:9.1y |

</details>

## Data Quality

- Symbols checked: 45
- Symbols with issues: 28
- NAV data age: median 4 days, max 435 days

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
