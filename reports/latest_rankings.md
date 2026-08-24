# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-24 10:52*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-24 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 23 |
| Median Discount | -9.33% |
| CONSIDER | 6 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 16 | 40.0% |
| -10% to -6% | 16 | 40.0% |
| -6% to -4% | 3 | 7.5% |
| -4% to 0% | 5 | 12.5% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.20 | -10.68% | 2.8y | medium | 4d | 0.88% | 72.1 | ↑ narrowing | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.70 | -14.16% | 3.2y | high | 6d | -2.04% | 70.8 | ↓ widening | — |
| 3 | NMB50 | NMB 50 | 10.45 | 9.75 | -6.70% | 0.0y | high | 6d | -1.42% | 60.6 | ↓ widening | — |
| 4 | PSF | Prabhu Select Fund | 13.04 | 12.03 | -7.75% | 1.8y | high | 57d | -4.26% | 58.6 | → stable | — |
| 5 | NICSF | NIC Asia Select-30 | 9.55 | 8.85 | -7.33% | 1.9y | medium | 9d | -2.55% | 58.2 | ↑ narrowing | — |
| 6 | SEF | Siddhartha Equity Fund | 10.36 | 9.27 | -10.52% | 1.2y | high | 5d | -2.72% | 53.6 | ↓ widening | — |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 9 |
| valuation | 5 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -20.25% | maturity:7.0y |
| SBCF | -18.69% | maturity:4.6y |
| KDBY | -18.52% | maturity:5.9y |
| LUK | -16.81% | liquidity:low |
| KEF | -15.21% | maturity:4.6y |
| NIBSF2 | -14.05% | maturity:4.8y |
| NICGF2 | -13.85% | maturity:4.2y |
| SFEF | -13.74% | maturity:5.5y |
| NSIF2 | -13.38% | maturity:6.0y |
| MBLEF | -11.98% | maturity:10.6y |
| KSY | -10.59% | liquidity:low; maturity:7.6y |
| NIBLSTF | -10.37% | maturity:9.5y |
| GBIMESY2 | -10.17% | maturity:8.9y |
| NICBF | -9.88% | liquidity:low |
| NMBHF2 | -9.73% | liquidity:low; maturity:8.5y |
| RBBF40 | -9.55% | maturity:11.2y |
| RMF1 | -9.34% | liquidity:low |
| NIBLGF | -9.32% | maturity:6.4y |
| PRSF | -9.27% | maturity:5.6y |
| GIBF1 | -8.32% | maturity:5.9y |
| RMF2 | -7.83% | liquidity:low; maturity:6.8y |
| SLCF | -7.64% | liquidity:low |
| GSY | -7.63% | maturity:8.4y |
| MNMF1 | -7.05% | maturity:8.3y |
| C30MF | -6.27% | liquidity:low; maturity:6.7y |
| NBF3 | -6.01% | maturity:5.1y |
| MMF1 | -5.59% | maturity:5.0y |
| SAGF | -5.12% | maturity:7.3y |
| RSY | -4.12% | maturity:8.7y |
| SIGS3 | -3.85% | valuation:small_discount; maturity:6.7y |
| NBF2 | -3.63% | valuation:small_discount |
| SIGS2 | -3.13% | valuation:small_discount; liquidity:low |
| H8020 | -2.99% | valuation:small_discount; maturity:7.1y |
| HLICF | -2.63% | valuation:small_discount; maturity:9.1y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 28
- NAV data age: median 21 days, max 452 days

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
