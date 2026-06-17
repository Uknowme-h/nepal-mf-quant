# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-17 14:00*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-17 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 16 |
| Median Discount | -7.26% |
| CONSIDER | 5 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 7 | 17.1% |
| -10% to -6% | 17 | 41.5% |
| -6% to -4% | 8 | 19.5% |
| -4% to 0% | 8 | 19.5% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICBF | NIC ASIA Balanced Fund | 10.38 | 9.41 | -9.34% | 3.2y | high | 1d | -0.86% | 72.3 | ↑ narrowing | high_vol |
| 2 | PSF | Prabhu Select Fund | 13.69 | 12.19 | -10.96% | 2.0y | medium | 11d | -4.60% | 69.2 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.45 | -9.05% | 3.0y | medium | 7d | -1.24% | 68.5 | ↑ narrowing | — |
| 4 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.85 | -5.92% | 3.0y | medium | 1d | 0.48% | 56.0 | → stable | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.41 | 9.81 | -5.76% | 2.1y | medium | 1d | -2.16% | 42.3 | → stable | high_vol |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 9 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -15.35% | liquidity:low; maturity:4.2y |
| PRSF | -13.95% | maturity:5.8y |
| LVF2 | -13.67% | maturity:7.2y |
| KDBY | -12.51% | maturity:6.1y |
| SBCF | -11.82% | maturity:4.8y |
| SFEF | -11.81% | liquidity:low; maturity:5.7y |
| RSY | -9.72% | maturity:8.9y |
| NSIF2 | -9.70% | maturity:6.2y |
| KEF | -9.66% | maturity:4.8y |
| NICGF2 | -9.26% | maturity:4.4y |
| GBIMESY2 | -9.09% | maturity:9.1y |
| NMBHF2 | -8.80% | maturity:8.7y |
| NIBSF2 | -8.21% | maturity:5.0y |
| MBLEF | -7.81% | maturity:10.8y |
| RMF2 | -7.52% | liquidity:low; maturity:6.9y |
| RBBF40 | -7.51% | liquidity:low; maturity:11.4y |
| KSY | -7.50% | maturity:7.8y |
| GIBF1 | -7.26% | maturity:6.1y |
| C30MF | -7.06% | liquidity:low; maturity:6.9y |
| SIGS3 | -6.22% | maturity:6.9y |
| SAGF | -6.22% | liquidity:low; maturity:7.5y |
| NIBLGF | -5.94% | liquidity:low; maturity:6.6y |
| GSY | -5.64% | maturity:8.6y |
| SFMF | -5.31% | liquidity:low |
| H8020 | -5.23% | maturity:7.3y |
| MNMF1 | -5.21% | maturity:8.5y |
| NIBLSTF | -4.00% | maturity:9.7y |
| NICSF | -3.73% | valuation:small_discount |
| NBF3 | -2.62% | valuation:small_discount; maturity:5.3y |
| SLCF | -2.61% | valuation:small_discount |
| CMF2 | -2.25% | valuation:small_discount; liquidity:low |
| SEF | -2.25% | valuation:small_discount |
| SIGS2 | -1.51% | valuation:small_discount |
| MMF1 | -1.24% | valuation:small_discount; maturity:5.2y |
| NMB50 | -0.76% | valuation:small_discount; liquidity:low |
| HLICF | 1.58% | valuation:premium; maturity:9.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 23
- NAV data age: median 33 days, max 384 days

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
