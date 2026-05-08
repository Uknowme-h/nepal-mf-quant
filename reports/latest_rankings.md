# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-08 11:45*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-08 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 25 |
| Median Discount | -9.50% |
| CONSIDER | 5 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 19 | 47.5% |
| -10% to -6% | 10 | 25.0% |
| -6% to -4% | 7 | 17.5% |
| -4% to 0% | 3 | 7.5% |
| ≥ 0% (premium) | 1 | 2.5% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 14.35 | 12.35 | -13.94% | 2.1y | medium | 5d | 12.55% | 72.0 | → stable | — |
| 2 | SLCF | Sanima Large Cap Fund | 10.65 | 9.90 | -7.04% | 1.8y | high | 21d | 0.47% | 62.8 | ↑ narrowing | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.64 | 10.11 | -4.98% | 2.2y | high | 13d | 0.76% | 58.6 | ↑ narrowing | high_vol |
| 4 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.40 | -7.96% | 3.5y | medium | 3d | -2.04% | 49.2 | → stable | — |
| 5 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.95 | -4.97% | 3.3y | medium | 1d | 4.39% | 48.9 | ↑ narrowing | high_vol |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -18.17% | maturity:5.8y |
| KEF | -18.07% | maturity:4.9y |
| KDBY | -18.05% | maturity:6.2y |
| LVF2 | -16.65% | liquidity:low; maturity:7.3y |
| SIGS3 | -15.15% | maturity:7.0y |
| LUK | -14.24% | maturity:4.3y |
| SBCF | -13.58% | maturity:4.9y |
| KSY | -13.49% | liquidity:low; maturity:7.9y |
| GIBF1 | -12.55% | maturity:6.2y |
| SFEF | -12.51% | maturity:5.8y |
| RSY | -12.14% | maturity:9.0y |
| MNMF1 | -11.30% | maturity:8.6y |
| H8020 | -11.24% | liquidity:low; maturity:7.4y |
| NICGF2 | -10.78% | maturity:4.5y |
| GSY | -10.74% | maturity:8.7y |
| MBLEF | -10.67% | maturity:10.9y |
| NICFC | -10.65% | liquidity:low |
| NMBHF2 | -10.11% | maturity:8.8y |
| SEF | -9.59% | liquidity:low |
| RMF2 | -9.41% | liquidity:low; maturity:7.0y |
| NSIF2 | -9.26% | maturity:6.3y |
| RBBF40 | -9.15% | liquidity:low; maturity:11.5y |
| NIBSF2 | -8.71% | maturity:5.1y |
| C30MF | -8.46% | liquidity:low; maturity:7.0y |
| SIGS2 | -7.98% | liquidity:low |
| SAGF | -7.64% | maturity:7.6y |
| NIBLGF | -5.53% | maturity:6.7y |
| NIBLSTF | -5.48% | maturity:9.8y |
| CMF2 | -4.94% | liquidity:low |
| MMF1 | -4.81% | maturity:5.3y |
| NBF3 | -4.26% | maturity:5.4y |
| NBF2 | -2.77% | valuation:small_discount |
| NICSF | -1.92% | valuation:small_discount |
| HLICF | -1.29% | valuation:small_discount; maturity:9.4y |
| NMB50 | 0.28% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 24
- NAV data age: median 23 days, max 344 days

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
