# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-22 10:39*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-21 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 20 |
| Median Discount | -7.95% |
| CONSIDER | 8 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 14 | 35.0% |
| -10% to -6% | 14 | 35.0% |
| -6% to -4% | 8 | 20.0% |
| -4% to 0% | 4 | 10.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | LUK | Laxmi Unnati Kosh | 11.66 | 9.74 | -16.47% | 4.0y | medium | 2d | -1.17% | 69.5 | ↓ widening | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.99 | -12.72% | 2.8y | medium | 3d | 0.88% | 66.5 | ↓ widening | — |
| 3 | NICBF | NIC ASIA Balanced Fund | 10.32 | 9.30 | -9.88% | 3.0y | medium | 2d | 0.88% | 64.9 | ↑ narrowing | high_vol |
| 4 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.90 | -12.39% | 3.2y | medium | 5d | -2.04% | 62.2 | ↓ widening | — |
| 5 | PSF | Prabhu Select Fund | 13.04 | 11.90 | -8.74% | 1.8y | medium | 56d | -4.26% | 58.0 | ↓ widening | — |
| 6 | NMB50 | NMB 50 | 10.45 | 9.86 | -5.65% | 0.0y | high | 5d | -1.42% | 54.6 | ↓ widening | — |
| 7 | NICSF | NIC Asia Select-30 | 9.55 | 8.77 | -8.17% | 1.9y | high | 8d | -2.55% | 54.4 | ↓ widening | — |
| 8 | SEF | Siddhartha Equity Fund | 10.36 | 9.51 | -8.20% | 1.2y | high | 4d | -2.72% | 51.6 | ↓ widening | — |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -20.42% | liquidity:low; maturity:7.0y |
| KDBY | -18.68% | maturity:5.9y |
| SBCF | -15.34% | liquidity:low; maturity:4.6y |
| KEF | -15.12% | maturity:4.6y |
| SFEF | -14.26% | liquidity:low; maturity:5.5y |
| NICGF2 | -13.46% | maturity:4.2y |
| MBLEF | -12.17% | maturity:10.6y |
| NIBSF2 | -12.10% | maturity:4.8y |
| NIBLSTF | -11.85% | maturity:9.5y |
| KSY | -10.98% | maturity:7.6y |
| RBBF40 | -10.45% | liquidity:low; maturity:11.2y |
| NIBLGF | -9.84% | maturity:6.4y |
| GBIMESY2 | -9.77% | maturity:8.9y |
| MNMF1 | -7.73% | maturity:8.3y |
| PRSF | -7.70% | maturity:5.6y |
| RMF1 | -7.59% | liquidity:low |
| GIBF1 | -7.47% | maturity:5.9y |
| RMF2 | -7.00% | maturity:6.8y |
| NBF3 | -6.30% | maturity:5.1y |
| C30MF | -6.27% | liquidity:low; maturity:6.7y |
| GSY | -6.12% | maturity:8.4y |
| NBF2 | -5.92% | liquidity:low |
| SLCF | -5.75% | liquidity:low |
| MMF1 | -5.59% | maturity:5.0y |
| NSIF2 | -5.57% | maturity:6.0y |
| NMBHF2 | -5.44% | maturity:8.5y |
| SAGF | -5.22% | liquidity:low; maturity:7.3y |
| RSY | -4.57% | maturity:8.7y |
| SIGS3 | -3.85% | valuation:small_discount; maturity:6.7y |
| SIGS2 | -3.13% | valuation:small_discount; liquidity:low |
| H8020 | -2.99% | valuation:small_discount; maturity:7.1y |
| HLICF | -2.06% | valuation:small_discount; maturity:9.1y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 26
- NAV data age: median 19 days, max 450 days

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
