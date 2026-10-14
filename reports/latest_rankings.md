# Nepal MF Quant — Full Analysis Report

*Generated: 2026-10-14 15:06*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-10-14 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 29 |
| Median Discount | -9.81% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 16 | 41.0% |
| -10% to -6% | 20 | 51.3% |
| -6% to -4% | 1 | 2.6% |
| -4% to 0% | 2 | 5.1% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.47 | -16.19% | 3.1y | medium | 3d | -2.04% | 80.5 | ↑ narrowing | — |
| 2 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.11 | -12.99% | 2.6y | medium | 4d | 0.48% | 70.0 | → stable | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.22 | 9.30 | -9.00% | 1.8y | medium | 12d | -0.87% | 61.7 | ↑ narrowing | high_vol |
| 4 | LUK | Laxmi Unnati Kosh | 11.66 | 9.30 | -20.24% | 3.8y | medium | 4d | -1.17% | 60.7 | ↓ widening | — |
| 5 | SEF | Siddhartha Equity Fund | 10.49 | 9.75 | -7.05% | 1.1y | high | 5d | 1.06% | 57.6 | → stable | — |
| 6 | NICSF | NIC Asia Select-30 | 9.28 | 8.55 | -7.87% | 1.7y | high | 14d | -2.11% | 55.5 | ↑ narrowing | high_vol |
| 7 | PSF | Prabhu Select Fund | 12.00 | 11.04 | -8.00% | 1.7y | medium | 4d | -8.33% | 51.7 | ↑ narrowing | — |
| 8 | SLCF | Sanima Large Cap Fund | 10.04 | 9.20 | -8.37% | 1.4y | medium | 1d | -0.99% | 42.4 | ↓ widening | — |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 2 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -20.63% | maturity:4.5y |
| SFEF | -19.16% | maturity:5.3y |
| LVF2 | -16.74% | liquidity:low; maturity:6.9y |
| RMF2 | -14.89% | liquidity:low; maturity:6.6y |
| GIBF1 | -12.86% | maturity:5.8y |
| NIBLGF | -11.79% | liquidity:low; maturity:6.3y |
| NICFC | -11.77% | liquidity:low |
| C30MF | -11.10% | liquidity:low; maturity:6.6y |
| NICBF | -11.09% | liquidity:low |
| KSY | -10.99% | maturity:7.4y |
| MNMF1 | -10.48% | maturity:8.2y |
| NIBSF2 | -10.39% | maturity:4.6y |
| NBF3 | -10.37% | maturity:5.0y |
| GBIMESY2 | -9.90% | maturity:8.8y |
| NICGF2 | -9.83% | maturity:4.1y |
| H8020 | -9.82% | maturity:7.0y |
| RBBF40 | -9.81% | liquidity:low; maturity:11.1y |
| SIGS2 | -9.70% | liquidity:low |
| MBLEF | -9.66% | maturity:10.5y |
| NIBLSTF | -9.43% | maturity:9.3y |
| RSY | -9.13% | maturity:8.6y |
| KEF | -9.01% | maturity:4.4y |
| KDBY | -8.24% | maturity:5.8y |
| MMF1 | -7.37% | maturity:4.9y |
| GSY | -7.30% | maturity:8.2y |
| SAGF | -7.00% | liquidity:low; maturity:7.1y |
| NMBHF2 | -6.85% | maturity:8.4y |
| PRSF | -6.30% | maturity:5.4y |
| NSIF2 | -4.18% | maturity:5.9y |
| SIGS3 | -3.92% | valuation:small_discount; liquidity:low; maturity:6.5y |
| HLICF | -3.03% | valuation:small_discount; maturity:8.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 30
- NAV data age: median 29 days, max 503 days

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
