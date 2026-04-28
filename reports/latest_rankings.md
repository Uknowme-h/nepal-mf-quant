# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-28 12:04*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-28 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 23 |
| Median Discount | -8.76% |
| CONSIDER | 7 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 13 | 31.7% |
| -10% to -6% | 16 | 39.0% |
| -6% to -4% | 8 | 19.5% |
| -4% to 0% | 2 | 4.9% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.88 | -6.44% | 2.2y | high | 6d | 5.28% | 61.8 | ↑ narrowing | high_vol |
| 2 | NICSF | NIC Asia Select-30 | 10.04 | 9.16 | -8.76% | 2.2y | medium | 9d | 5.35% | 61.7 | → stable | — |
| 3 | SIGS2 | Siddhartha Investment Gro | 10.98 | 10.50 | -4.37% | 3.3y | medium | 2d | 5.17% | 57.6 | ↑ narrowing | — |
| 4 | SLCF | Sanima Large Cap Fund | 10.60 | 9.75 | -8.02% | 1.8y | medium | 14d | 4.43% | 55.2 | ↓ widening | — |
| 5 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.47 | -9.55% | 3.3y | medium | 1d | 4.39% | 54.6 | → stable | high_vol |
| 6 | PSF | Prabhu Select Fund | 12.75 | 12.17 | -4.55% | 2.1y | high | 1d | 5.81% | 47.8 | ↓ widening | — |
| 7 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.94 | -5.06% | 3.1y | medium | 3d | 0.48% | 46.1 | → stable | — |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -15.61% | maturity:4.3y |
| SBCF | -15.34% | maturity:4.9y |
| MBLEF | -12.30% | maturity:10.9y |
| NIBLSTF | -12.09% | maturity:9.8y |
| NICFC | -11.88% | liquidity:low |
| KSY | -11.72% | liquidity:low; maturity:7.9y |
| RSY | -11.69% | maturity:9.0y |
| SFEF | -11.64% | liquidity:low; maturity:5.8y |
| NICGF2 | -10.97% | maturity:4.6y |
| LVF2 | -10.96% | maturity:7.4y |
| NMBHF2 | -10.51% | maturity:8.8y |
| RBBF40 | -10.22% | maturity:11.6y |
| GBIMESY2 | -10.10% | maturity:9.2y |
| GIBF1 | -9.85% | maturity:6.2y |
| NSIF2 | -9.59% | maturity:6.3y |
| RMF2 | -9.49% | maturity:7.1y |
| NIBLGF | -9.45% | maturity:6.7y |
| C30MF | -9.09% | liquidity:low; maturity:7.0y |
| MNMF1 | -8.93% | maturity:8.7y |
| GSY | -8.76% | maturity:8.7y |
| SAGF | -7.76% | liquidity:low; maturity:7.6y |
| SEF | -7.39% | liquidity:low |
| NIBSF2 | -7.32% | maturity:5.1y |
| H8020 | -6.92% | maturity:7.4y |
| HLICF | -6.43% | maturity:9.4y |
| SFMF | -5.31% | liquidity:low |
| SIGS3 | -5.11% | liquidity:low; maturity:7.0y |
| CMF2 | -4.90% | liquidity:low |
| MMF1 | -4.83% | maturity:5.4y |
| NBF3 | -4.46% | maturity:5.4y |
| NMB50 | -3.22% | valuation:small_discount; liquidity:low |
| PRSF | 0.00% | valuation:premium; maturity:5.9y |
| KDBY | 1.14% | valuation:premium; maturity:6.2y |
| KEF | 2.27% | valuation:premium; maturity:4.9y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 21
- NAV data age: median 44 days, max 334 days

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
