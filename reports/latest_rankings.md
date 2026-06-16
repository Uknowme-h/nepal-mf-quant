# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-16 15:25*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-16 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 17 |
| Median Discount | -6.97% |
| CONSIDER | 4 |
| IGNORE | 37 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 10 | 24.4% |
| -10% to -6% | 13 | 31.7% |
| -6% to -4% | 9 | 22.0% |
| -4% to 0% | 7 | 17.1% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 12.22 | -10.74% | 2.0y | high | 10d | -4.60% | 67.4 | → stable | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.39 | -9.62% | 3.0y | medium | 6d | -1.24% | 60.4 | ↓ widening | — |
| 3 | SEF | Siddhartha Equity Fund | 10.65 | 10.16 | -4.60% | 1.4y | high | 25d | -2.74% | 59.3 | ↑ narrowing | — |
| 4 | SLCF | Sanima Large Cap Fund | 10.34 | 9.92 | -4.06% | 1.7y | medium | 1d | -2.91% | 40.4 | ↓ widening | — |

## IGNORE Summary

*37 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 9 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -15.26% | liquidity:low; maturity:4.8y |
| LVF2 | -15.25% | liquidity:low; maturity:7.2y |
| PRSF | -13.68% | maturity:5.8y |
| KDBY | -12.59% | maturity:6.1y |
| LUK | -12.52% | maturity:4.2y |
| SFEF | -11.99% | maturity:5.7y |
| NICGF2 | -11.94% | maturity:4.4y |
| NICBF | -11.85% | liquidity:low |
| KEF | -10.07% | maturity:4.8y |
| GIBF1 | -9.92% | maturity:6.1y |
| RSY | -9.63% | maturity:8.9y |
| MBLEF | -9.17% | maturity:10.8y |
| NSIF2 | -8.69% | maturity:6.2y |
| KSY | -8.44% | maturity:7.8y |
| GBIMESY2 | -8.11% | maturity:9.1y |
| NIBSF2 | -7.80% | maturity:5.0y |
| RMF2 | -7.62% | maturity:6.9y |
| NMBHF2 | -7.28% | maturity:8.7y |
| H8020 | -6.97% | maturity:7.3y |
| RBBF40 | -6.13% | maturity:11.4y |
| C30MF | -6.04% | liquidity:low; maturity:6.9y |
| RMF1 | -5.86% | liquidity:low |
| NIBLGF | -5.84% | maturity:6.6y |
| GSY | -5.83% | maturity:8.6y |
| NBF2 | -5.83% | liquidity:low |
| SAGF | -5.57% | liquidity:low; maturity:7.5y |
| MNMF1 | -5.21% | maturity:8.5y |
| SIGS3 | -4.46% | maturity:6.9y |
| SFMF | -3.54% | valuation:small_discount |
| NIBLSTF | -3.49% | valuation:small_discount; maturity:9.7y |
| CMF2 | -3.23% | valuation:small_discount; liquidity:low |
| NBF3 | -3.20% | valuation:small_discount; maturity:5.3y |
| NMB50 | -1.52% | valuation:small_discount; liquidity:low |
| MMF1 | -1.44% | valuation:small_discount; maturity:5.2y |
| NICSF | -1.35% | valuation:small_discount |
| SIGS2 | 1.51% | valuation:premium; liquidity:low |
| HLICF | 3.84% | valuation:premium; maturity:9.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 21
- NAV data age: median 32 days, max 383 days

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
