# Nepal MF Quant — Full Analysis Report

*Generated: 2026-02-11 00:13*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-02-10 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 10 |
| Median Discount | -6.69% |
| CONSIDER | 6 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 30 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 0 | 0.0% |
| -10% to -6% | 23 | 56.1% |
| -6% to -4% | 7 | 17.1% |
| -4% to 0% | 9 | 22.0% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.02 | 9.15 | -8.68% | 3.4y | medium | 2d | 0.00% | 66.8 | → stable | — |
| 2 | PSF | Prabhu Select Fund | 12.03 | 11.18 | -7.07% | 2.4y | medium | 1d | 0.00% | 65.5 | ↑ narrowing | — |
| 3 | NICBF | NIC ASIA Balanced Fund | 10.04 | 9.30 | -7.37% | 3.5y | medium | 2d | 0.00% | 61.8 | → stable | — |
| 4 | NICSF | NIC Asia Select-30 | 9.54 | 8.91 | -6.60% | 2.4y | high | 1d | — | 59.2 | → stable | — |
| 5 | NBF2 | Nabil Balanced Fund - 2 | 10.42 | 9.58 | -8.06% | 3.3y | high | 2d | -1.05% | 58.4 | ↓ widening | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.02 | 9.35 | -6.69% | 2.5y | medium | 2d | — | 46.3 | ↓ widening | high_vol |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 11 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| NMBHF2 | -9.75% | maturity:9.1y |
| PRSF | -9.03% | liquidity:low; maturity:6.1y |
| SFEF | -9.01% | liquidity:low; maturity:6.0y |
| GIBF1 | -8.90% | liquidity:low; maturity:6.5y |
| NSIF2 | -8.77% | maturity:6.6y |
| KDBY | -8.49% | maturity:6.5y |
| KSY | -8.38% | maturity:8.1y |
| NBF3 | -8.06% | maturity:5.6y |
| RSY | -7.98% | maturity:9.2y |
| LVF2 | -7.71% | liquidity:low; maturity:7.6y |
| SIGS2 | -7.59% | liquidity:low |
| GBIMESY2 | -7.13% | liquidity:low; maturity:9.4y |
| MBLEF | -7.02% | maturity:11.1y |
| SAGF | -6.97% | maturity:7.8y |
| NICGF2 | -6.80% | maturity:4.8y |
| RMF2 | -6.72% | maturity:7.3y |
| C30MF | -6.11% | maturity:7.3y |
| GSY | -5.94% | maturity:8.9y |
| MMF1 | -5.24% | maturity:5.6y |
| KEF | -4.96% | maturity:5.1y |
| MNMF1 | -4.89% | maturity:8.9y |
| NIBLSTF | -4.82% | maturity:10.0y |
| NIBSF2 | -4.81% | liquidity:low; maturity:5.3y |
| SIGS3 | -4.36% | liquidity:low; maturity:7.2y |
| SBCF | -3.46% | valuation:small_discount; maturity:5.1y |
| SEF | -3.19% | valuation:small_discount |
| SLCF | -2.67% | valuation:small_discount |
| H8020 | -1.68% | valuation:small_discount; maturity:7.6y |
| HLICF | -0.93% | valuation:small_discount; liquidity:low; maturity:9.6y |
| RBBF40 | -0.90% | valuation:small_discount; maturity:11.8y |
| SFMF | -0.87% | valuation:small_discount |
| LUK | -0.80% | valuation:small_discount; liquidity:low; maturity:4.5y |
| CMF2 | -0.30% | valuation:small_discount |
| NMB50 | 1.94% | valuation:premium |
| NIBLGF | 4.50% | valuation:premium; maturity:6.9y |

</details>

## Data Quality

- Symbols checked: 41
- Symbols with issues: 30
- NAV data age: median 58 days, max 58 days

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
