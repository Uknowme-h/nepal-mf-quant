# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-04 12:07*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-04 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 32 |
| Median Discount | -11.08% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 25 | 61.0% |
| -10% to -6% | 11 | 26.8% |
| -6% to -4% | 4 | 9.8% |
| -4% to 0% | 1 | 2.4% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SIGS2 | Siddhartha Investment Gro | 11.53 | 10.16 | -11.88% | 3.3y | high | 5d | 5.01% | 77.6 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 14.35 | 12.15 | -15.33% | 2.1y | medium | 1d | 12.55% | 73.2 | ↓ widening | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.15 | -13.02% | 3.1y | medium | 2d | 4.26% | 70.4 | → stable | — |
| 4 | SLCF | Sanima Large Cap Fund | 10.65 | 9.72 | -8.73% | 1.8y | medium | 17d | 0.47% | 55.4 | → stable | — |
| 5 | NICSF | NIC Asia Select-30 | 9.89 | 9.25 | -6.47% | 2.2y | high | 2d | -1.49% | 54.1 | ↑ narrowing | — |
| 6 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.31 | -11.08% | 3.3y | medium | 4d | 4.39% | 52.2 | ↓ widening | high_vol |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.64 | 10.00 | -6.02% | 2.2y | medium | 9d | 0.76% | 51.8 | ↑ narrowing | high_vol |
| 8 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.51 | -6.99% | 3.5y | medium | 3d | -2.04% | 51.5 | → stable | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 1 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -18.30% | maturity:5.9y |
| KEF | -17.68% | maturity:4.9y |
| KDBY | -17.10% | maturity:6.2y |
| SBCF | -16.75% | maturity:4.9y |
| LUK | -14.67% | liquidity:low; maturity:4.3y |
| SFEF | -14.52% | liquidity:low; maturity:5.8y |
| SIGS3 | -14.17% | liquidity:low; maturity:7.0y |
| GIBF1 | -14.01% | maturity:6.2y |
| RSY | -13.27% | maturity:9.0y |
| NMBHF2 | -13.20% | maturity:8.8y |
| MBLEF | -12.87% | maturity:10.9y |
| NSIF2 | -12.81% | maturity:6.3y |
| GBIMESY2 | -12.52% | maturity:9.2y |
| GSY | -11.85% | maturity:8.7y |
| KSY | -11.53% | liquidity:low; maturity:7.9y |
| MNMF1 | -11.49% | maturity:8.6y |
| RMF2 | -11.10% | maturity:7.0y |
| LVF2 | -10.69% | maturity:7.3y |
| NIBLSTF | -10.36% | maturity:9.8y |
| SEF | -10.32% | liquidity:low |
| NICGF2 | -10.31% | maturity:4.5y |
| NIBSF2 | -9.70% | maturity:5.1y |
| H8020 | -9.21% | maturity:7.4y |
| C30MF | -9.01% | liquidity:low; maturity:7.0y |
| NIBLGF | -8.98% | maturity:6.7y |
| RBBF40 | -8.47% | liquidity:low; maturity:11.5y |
| SAGF | -8.01% | maturity:7.6y |
| CMF2 | -6.84% | liquidity:low |
| NBF2 | -5.83% | liquidity:low |
| NBF3 | -4.26% | maturity:5.4y |
| MMF1 | -4.21% | maturity:5.3y |
| NMB50 | -4.18% | liquidity:low |
| HLICF | -3.11% | valuation:small_discount; maturity:9.4y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 28
- NAV data age: median 19 days, max 340 days

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
