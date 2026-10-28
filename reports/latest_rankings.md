# Nepal MF Quant — Full Analysis Report

*Generated: 2026-10-28 16:38*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-10-28 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 17 |
| Median Discount | -7.65% |
| CONSIDER | 10 |
| IGNORE | 29 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 10 | 25.6% |
| -10% to -6% | 21 | 53.8% |
| -6% to -4% | 4 | 10.3% |
| -4% to 0% | 3 | 7.7% |
| ≥ 0% (premium) | 1 | 2.6% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.32 | -10.98% | 2.6y | high | 1d | 0.48% | 78.5 | ↑ narrowing | — |
| 2 | LUK | Laxmi Unnati Kosh | 11.66 | 9.56 | -18.01% | 3.8y | high | 1d | -1.17% | 77.2 | ↑ narrowing | — |
| 3 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.50 | -15.93% | 3.0y | medium | 2d | -2.04% | 64.7 | → stable | — |
| 4 | NICFC | NIC Asia Flexi Cap Fund | 9.94 | 9.18 | -7.65% | 2.6y | medium | 3d | -1.29% | 63.6 | ↑ narrowing | — |
| 5 | NICBF | NIC ASIA Balanced Fund | 10.01 | 9.24 | -7.69% | 2.8y | medium | 1d | -0.99% | 60.5 | ↑ narrowing | — |
| 6 | SEF | Siddhartha Equity Fund | 10.49 | 9.85 | -6.10% | 1.0y | high | 10d | 1.06% | 57.4 | ↑ narrowing | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.22 | 9.06 | -11.35% | 1.7y | medium | 17d | -0.87% | 56.4 | ↓ widening | high_vol |
| 8 | SIGS2 | Siddhartha Investment Gro | 10.31 | 9.89 | -4.07% | 2.8y | medium | 3d | -5.84% | 52.4 | ↑ narrowing | — |
| 9 | PSF | Prabhu Select Fund | 12.00 | 11.30 | -5.83% | 1.6y | high | 9d | -8.33% | 49.5 | ↑ narrowing | — |
| 10 | NICSF | NIC Asia Select-30 | 9.28 | 8.60 | -7.33% | 1.7y | medium | 19d | -2.11% | 47.4 | ↑ narrowing | high_vol |

## IGNORE Summary

*29 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -20.25% | liquidity:low; maturity:6.8y |
| SFEF | -19.34% | liquidity:low; maturity:5.3y |
| SBCF | -15.61% | maturity:4.4y |
| GIBF1 | -12.27% | liquidity:low; maturity:5.8y |
| RMF2 | -11.19% | liquidity:low; maturity:6.6y |
| MNMF1 | -10.09% | maturity:8.2y |
| NBF3 | -9.88% | maturity:4.9y |
| H8020 | -9.82% | maturity:6.9y |
| GSY | -9.17% | liquidity:low; maturity:8.2y |
| RBBF40 | -8.91% | maturity:11.1y |
| NICGF2 | -8.51% | maturity:4.1y |
| SLCF | -8.37% | liquidity:low |
| RSY | -8.17% | liquidity:low; maturity:8.5y |
| GBIMESY2 | -7.90% | liquidity:low; maturity:8.7y |
| NIBSF2 | -7.51% | maturity:4.6y |
| MBLEF | -7.50% | maturity:10.4y |
| NIBLSTF | -7.42% | maturity:9.3y |
| NMBHF2 | -7.26% | maturity:8.3y |
| NIBLGF | -7.01% | maturity:6.2y |
| SAGF | -6.50% | maturity:7.1y |
| KEF | -6.46% | maturity:4.4y |
| C30MF | -6.41% | liquidity:low; maturity:6.5y |
| KSY | -6.05% | maturity:7.4y |
| KDBY | -5.79% | maturity:5.8y |
| MMF1 | -5.79% | maturity:4.9y |
| PRSF | -3.92% | valuation:small_discount; maturity:5.4y |
| NSIF2 | -2.18% | valuation:small_discount; maturity:5.8y |
| SIGS3 | -1.59% | valuation:small_discount; maturity:6.5y |
| HLICF | 0.35% | valuation:premium; liquidity:low; maturity:8.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 25
- NAV data age: median 43 days, max 517 days

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
