# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-19 10:46*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-19 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 21 |
| Median Discount | -8.34% |
| CONSIDER | 6 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 10 | 25.0% |
| -10% to -6% | 17 | 42.5% |
| -6% to -4% | 7 | 17.5% |
| -4% to 0% | 6 | 15.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.30 | -8.85% | 3.2y | medium | 3d | -2.04% | 65.1 | → stable | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.00 | -12.62% | 2.8y | medium | 1d | 0.88% | 60.1 | ↓ widening | — |
| 3 | NMB50 | NMB 50 | 10.45 | 9.81 | -6.12% | 0.0y | high | 3d | -1.42% | 57.8 | ↓ widening | — |
| 4 | NICSF | NIC Asia Select-30 | 9.55 | 8.30 | -13.09% | 1.9y | medium | 6d | -2.55% | 54.1 | ↓ widening | — |
| 5 | SEF | Siddhartha Equity Fund | 10.36 | 9.34 | -9.85% | 1.2y | high | 2d | -2.72% | 53.9 | ↓ widening | — |
| 6 | PSF | Prabhu Select Fund | 13.04 | 11.84 | -9.20% | 1.8y | medium | 54d | -4.26% | 52.6 | ↓ widening | — |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 6 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -15.08% | maturity:4.6y |
| LUK | -14.32% | liquidity:low |
| SFEF | -14.26% | liquidity:low; maturity:5.5y |
| NICGF2 | -13.75% | maturity:4.3y |
| LVF2 | -13.58% | maturity:7.0y |
| NIBLSTF | -11.01% | maturity:9.5y |
| KSY | -10.88% | liquidity:low; maturity:7.6y |
| MBLEF | -10.60% | maturity:10.6y |
| GBIMESY2 | -9.87% | liquidity:low; maturity:8.9y |
| KDBY | -9.87% | maturity:5.9y |
| NIBSF2 | -9.74% | maturity:4.8y |
| NIBLGF | -8.91% | maturity:6.4y |
| GIBF1 | -8.66% | maturity:6.0y |
| MMF1 | -8.54% | maturity:5.1y |
| RBBF40 | -8.54% | maturity:11.2y |
| NICBF | -8.14% | liquidity:low |
| PRSF | -7.98% | maturity:5.6y |
| RMF2 | -7.00% | liquidity:low; maturity:6.8y |
| NBF3 | -6.98% | maturity:5.1y |
| GSY | -6.33% | maturity:8.4y |
| NBF2 | -6.30% | liquidity:low |
| RSY | -5.73% | maturity:8.7y |
| NSIF2 | -5.66% | maturity:6.0y |
| NMBHF2 | -5.63% | maturity:8.5y |
| MNMF1 | -5.58% | maturity:8.3y |
| SAGF | -5.31% | maturity:7.3y |
| C30MF | -5.03% | maturity:6.7y |
| H8020 | -4.69% | liquidity:low; maturity:7.1y |
| SIGS3 | -3.85% | valuation:small_discount; maturity:6.7y |
| KEF | -3.85% | valuation:small_discount; maturity:4.6y |
| SIGS2 | -2.95% | valuation:small_discount; liquidity:low |
| RMF1 | -2.72% | valuation:small_discount |
| HLICF | -1.37% | valuation:small_discount; maturity:9.1y |
| SLCF | -0.79% | valuation:small_discount; liquidity:low |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 26
- NAV data age: median 16 days, max 447 days

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
