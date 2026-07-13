# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-13 12:43*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-13 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 27 |
| Median Discount | -10.00% |
| CONSIDER | 8 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 20 | 50.0% |
| -10% to -6% | 13 | 32.5% |
| -6% to -4% | 3 | 7.5% |
| -4% to 0% | 4 | 10.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 11.60 | -15.27% | 1.9y | high | 28d | -4.60% | 67.9 | ↓ widening | — |
| 2 | NICSF | NIC Asia Select-30 | 9.80 | 9.20 | -6.12% | 2.0y | high | 6d | 1.45% | 60.8 | → stable | — |
| 3 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.03 | -4.20% | 2.9y | medium | 4d | 0.48% | 58.8 | ↑ narrowing | — |
| 4 | SEF | Siddhartha Equity Fund | 10.65 | 10.00 | -6.10% | 1.3y | medium | 7d | 0.00% | 54.0 | → stable | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.79 | -6.32% | 2.0y | medium | 6d | 0.38% | 52.8 | → stable | high_vol |
| 6 | SLCF | Sanima Large Cap Fund | 10.36 | 9.90 | -4.44% | 1.6y | medium | 1d | 0.19% | 47.8 | ↓ widening | — |
| 7 | NICBF | NIC ASIA Balanced Fund | 10.38 | 8.98 | -13.49% | 3.1y | medium | 3d | -0.86% | 45.9 | ↓ widening | high_vol |
| 8 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.20 | -9.73% | 3.3y | medium | 1d | -2.04% | 45.5 | ↓ widening | — |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| KDBY | -16.34% | maturity:6.0y |
| SBCF | -15.34% | maturity:4.7y |
| PRSF | -15.09% | maturity:5.7y |
| NIBSF2 | -14.80% | maturity:4.9y |
| LVF2 | -14.37% | liquidity:low; maturity:7.2y |
| LUK | -14.24% | liquidity:low; maturity:4.1y |
| NIBLSTF | -14.08% | maturity:9.6y |
| GIBF1 | -13.53% | maturity:6.0y |
| NICGF2 | -12.61% | liquidity:low; maturity:4.4y |
| SFEF | -12.51% | maturity:5.6y |
| RMF2 | -12.21% | liquidity:low; maturity:6.9y |
| RSY | -11.89% | maturity:8.8y |
| NICFC | -11.84% | liquidity:low |
| SIGS3 | -11.76% | maturity:6.8y |
| NSIF2 | -11.48% | liquidity:low; maturity:6.1y |
| KEF | -10.79% | maturity:4.7y |
| KSY | -10.12% | maturity:7.7y |
| MBLEF | -10.07% | maturity:10.7y |
| NMBHF2 | -9.94% | maturity:8.6y |
| RBBF40 | -9.85% | maturity:11.3y |
| NIBLGF | -9.82% | maturity:6.5y |
| SIGS2 | -9.09% | liquidity:low |
| C30MF | -8.14% | maturity:6.8y |
| SAGF | -8.04% | liquidity:low; maturity:7.4y |
| MNMF1 | -7.72% | maturity:8.4y |
| H8020 | -7.29% | liquidity:low; maturity:7.2y |
| GBIMESY2 | -7.05% | maturity:9.0y |
| GSY | -5.15% | maturity:8.5y |
| NBF3 | -3.29% | valuation:small_discount; maturity:5.2y |
| HLICF | -2.34% | valuation:small_discount; liquidity:low; maturity:9.2y |
| NMB50 | -1.04% | valuation:small_discount |
| MMF1 | -0.82% | valuation:small_discount; maturity:5.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 21
- NAV data age: median 28 days, max 410 days

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
