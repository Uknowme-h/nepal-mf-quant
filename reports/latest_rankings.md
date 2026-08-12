# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-12 11:11*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-12 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 19 |
| Median Discount | -7.76% |
| CONSIDER | 5 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 7 | 17.5% |
| -10% to -6% | 20 | 50.0% |
| -6% to -4% | 6 | 15.0% |
| -4% to 0% | 7 | 17.5% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.30 | -9.71% | 2.8y | medium | 5d | 0.88% | 77.1 | ↑ narrowing | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.30 | -8.85% | 3.2y | medium | 2d | -2.04% | 64.9 | → stable | — |
| 3 | PSF | Prabhu Select Fund | 13.04 | 12.00 | -7.98% | 1.9y | medium | 49d | -4.26% | 62.2 | ↑ narrowing | — |
| 4 | NICSF | NIC Asia Select-30 | 9.55 | 8.83 | -7.54% | 1.9y | high | 1d | -2.55% | 60.5 | → stable | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.28 | 9.84 | -4.28% | 1.9y | high | 18d | -1.63% | 59.1 | ↑ narrowing | high_vol |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 7 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -18.40% | maturity:7.1y |
| SBCF | -17.46% | maturity:4.6y |
| SFEF | -14.26% | maturity:5.5y |
| LUK | -12.95% | maturity:4.0y |
| NICGF2 | -12.69% | maturity:4.3y |
| NICBF | -10.85% | liquidity:low |
| KDBY | -10.44% | maturity:6.0y |
| RMF2 | -9.67% | liquidity:low; maturity:6.8y |
| NIBLSTF | -9.52% | maturity:9.5y |
| NIBSF2 | -9.44% | liquidity:low; maturity:4.8y |
| GIBF1 | -9.25% | maturity:6.0y |
| KSY | -9.04% | maturity:7.6y |
| NIBLGF | -8.91% | maturity:6.4y |
| NMBHF2 | -8.87% | maturity:8.6y |
| PRSF | -8.84% | maturity:5.6y |
| RBBF40 | -8.54% | maturity:11.3y |
| GBIMESY2 | -8.26% | liquidity:low; maturity:8.9y |
| SIGS3 | -7.34% | maturity:6.7y |
| NBF3 | -7.07% | maturity:5.1y |
| RSY | -6.81% | maturity:8.7y |
| NSIF2 | -6.78% | maturity:6.1y |
| MNMF1 | -6.65% | liquidity:low; maturity:8.4y |
| NBF2 | -6.02% | liquidity:low |
| KEF | -5.33% | maturity:4.6y |
| C30MF | -5.03% | liquidity:low; maturity:6.8y |
| MMF1 | -4.96% | maturity:5.1y |
| MBLEF | -4.70% | maturity:10.6y |
| GSY | -4.62% | maturity:8.4y |
| SLCF | -3.57% | valuation:small_discount |
| SAGF | -3.23% | valuation:small_discount; maturity:7.3y |
| SEF | -2.99% | valuation:small_discount |
| H8020 | -2.43% | valuation:small_discount; liquidity:low; maturity:7.1y |
| HLICF | -2.29% | valuation:small_discount; maturity:9.1y |
| SIGS2 | -1.38% | valuation:small_discount; liquidity:low |
| NMB50 | -0.38% | valuation:small_discount; liquidity:low |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 27
- NAV data age: median 9 days, max 440 days

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
