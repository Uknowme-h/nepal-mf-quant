# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-27 12:00*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-27 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 22 |
| Median Discount | -8.49% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 12 | 29.3% |
| -10% to -6% | 18 | 43.9% |
| -6% to -4% | 6 | 14.6% |
| -4% to 0% | 2 | 4.9% |
| ≥ 0% (premium) | 3 | 7.3% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SIGS2 | Siddhartha Investment Gro | 10.98 | 10.30 | -6.19% | 3.3y | high | 1d | 5.17% | 67.4 | ↑ narrowing | — |
| 2 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.59 | -9.19% | 2.2y | medium | 5d | 5.28% | 66.1 | → stable | high_vol |
| 3 | NICSF | NIC Asia Select-30 | 10.04 | 9.26 | -7.77% | 2.2y | medium | 8d | 5.35% | 63.0 | ↑ narrowing | — |
| 4 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.26 | -11.98% | 3.1y | medium | 1d | 4.26% | 59.3 | ↓ widening | — |
| 5 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.70 | -5.31% | 3.5y | high | 2d | -2.04% | 56.3 | → stable | — |
| 6 | SLCF | Sanima Large Cap Fund | 10.60 | 9.70 | -8.49% | 1.8y | medium | 13d | 4.43% | 49.6 | ↓ widening | — |
| 7 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.00 | -4.49% | 3.1y | medium | 2d | 0.48% | 48.8 | → stable | — |
| 8 | SEF | Siddhartha Equity Fund | 10.55 | 9.90 | -6.16% | 1.5y | high | 6d | 4.98% | 45.5 | ↓ widening | high_vol |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 5 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -15.34% | maturity:4.9y |
| LUK | -14.92% | maturity:4.3y |
| SFEF | -12.95% | liquidity:low; maturity:5.8y |
| GIBF1 | -12.28% | maturity:6.3y |
| NICGF2 | -12.28% | maturity:4.6y |
| RSY | -11.43% | maturity:9.0y |
| LVF2 | -11.04% | liquidity:low; maturity:7.4y |
| KSY | -10.60% | maturity:7.9y |
| NIBLSTF | -10.33% | liquidity:low; maturity:9.8y |
| NMBHF2 | -10.23% | maturity:8.8y |
| MBLEF | -10.21% | maturity:10.9y |
| NSIF2 | -9.84% | maturity:6.3y |
| NICBF | -9.55% | liquidity:low |
| C30MF | -9.09% | liquidity:low; maturity:7.0y |
| NIBLGF | -8.87% | liquidity:low; maturity:6.7y |
| GSY | -8.76% | maturity:8.7y |
| RBBF40 | -8.58% | maturity:11.6y |
| NIBSF2 | -8.49% | maturity:5.1y |
| GBIMESY2 | -8.37% | maturity:9.2y |
| MNMF1 | -7.92% | maturity:8.7y |
| RMF2 | -7.72% | maturity:7.1y |
| SAGF | -7.39% | liquidity:low; maturity:7.6y |
| CMF2 | -7.16% | liquidity:low |
| HLICF | -6.33% | liquidity:low; maturity:9.4y |
| SIGS3 | -5.02% | liquidity:low; maturity:7.0y |
| H8020 | -4.61% | maturity:7.4y |
| MMF1 | -4.43% | maturity:5.4y |
| NBF3 | -4.36% | maturity:5.4y |
| PSF | -3.53% | valuation:small_discount |
| NMB50 | -1.10% | valuation:small_discount |
| PRSF | 1.69% | valuation:premium; maturity:5.9y |
| KDBY | 1.75% | valuation:premium; maturity:6.2y |
| KEF | 3.22% | valuation:premium; maturity:4.9y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 24
- NAV data age: median 43 days, max 333 days

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
