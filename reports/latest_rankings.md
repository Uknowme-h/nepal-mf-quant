# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-18 10:45*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-18 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 20 |
| Median Discount | -8.14% |
| CONSIDER | 6 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 11 | 27.5% |
| -10% to -6% | 16 | 40.0% |
| -6% to -4% | 9 | 22.5% |
| -4% to 0% | 4 | 10.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.10 | -10.62% | 3.2y | medium | 2d | -2.04% | 58.2 | ↓ widening | — |
| 2 | NICSF | NIC Asia Select-30 | 9.55 | 8.51 | -10.89% | 1.9y | medium | 5d | -2.55% | 57.8 | ↓ widening | — |
| 3 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.81 | -6.30% | 2.8y | medium | 1d | 0.48% | 57.5 | → stable | — |
| 4 | PSF | Prabhu Select Fund | 13.04 | 12.00 | -7.98% | 1.8y | medium | 53d | -4.26% | 57.0 | ↑ narrowing | — |
| 5 | NMB50 | NMB 50 | 10.45 | 9.90 | -5.26% | 0.0y | high | 2d | -1.42% | 51.5 | ↓ widening | — |
| 6 | SEF | Siddhartha Equity Fund | 10.36 | 9.50 | -8.30% | 1.2y | high | 1d | -2.72% | 50.5 | ↓ widening | — |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -15.43% | maturity:7.0y |
| LUK | -14.32% | liquidity:low |
| SFEF | -14.26% | liquidity:low; maturity:5.5y |
| NICGF2 | -13.46% | liquidity:low; maturity:4.3y |
| NICFC | -11.94% | liquidity:low |
| SBCF | -11.82% | liquidity:low; maturity:4.6y |
| NIBLGF | -11.48% | maturity:6.4y |
| NIBLSTF | -11.32% | liquidity:low; maturity:9.5y |
| NICBF | -10.76% | liquidity:low |
| KDBY | -9.87% | maturity:5.9y |
| NIBSF2 | -9.74% | maturity:4.8y |
| RBBF40 | -9.05% | maturity:11.2y |
| PRSF | -8.77% | maturity:5.6y |
| GBIMESY2 | -8.76% | maturity:8.9y |
| MBLEF | -8.57% | maturity:10.6y |
| KSY | -8.36% | maturity:7.6y |
| GIBF1 | -8.32% | maturity:6.0y |
| MNMF1 | -7.44% | maturity:8.3y |
| NBF3 | -7.17% | maturity:5.1y |
| RMF2 | -7.00% | liquidity:low; maturity:6.8y |
| GSY | -6.63% | maturity:8.4y |
| MMF1 | -6.12% | maturity:5.1y |
| RSY | -5.91% | maturity:8.7y |
| SAGF | -5.88% | maturity:7.3y |
| NSIF2 | -5.66% | maturity:6.0y |
| RMF1 | -5.64% | liquidity:low |
| SIGS3 | -5.59% | maturity:6.7y |
| NMBHF2 | -5.53% | maturity:8.5y |
| C30MF | -5.03% | liquidity:low; maturity:6.7y |
| KEF | -4.02% | maturity:4.6y |
| H8020 | -2.99% | valuation:small_discount; maturity:7.1y |
| SIGS2 | -2.95% | valuation:small_discount |
| SLCF | -2.58% | valuation:small_discount |
| HLICF | -0.34% | valuation:small_discount; maturity:9.1y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 23
- NAV data age: median 15 days, max 446 days

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
