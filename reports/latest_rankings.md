# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-10 13:50*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-10 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 19 |
| Median Discount | -7.65% |
| CONSIDER | 6 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 11 | 26.8% |
| -10% to -6% | 13 | 31.7% |
| -6% to -4% | 8 | 19.5% |
| -4% to 0% | 7 | 17.1% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.24 | -9.38% | 3.4y | medium | 1d | -2.04% | 67.8 | → stable | — |
| 2 | PSF | Prabhu Select Fund | 13.69 | 12.10 | -11.61% | 2.0y | medium | 6d | -4.60% | 59.8 | ↓ widening | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.35 | -10.01% | 3.0y | medium | 2d | -1.24% | 58.7 | ↓ widening | — |
| 4 | NICBF | NIC ASIA Balanced Fund | 10.38 | 9.20 | -11.37% | 3.2y | medium | 1d | -0.86% | 58.5 | ↓ widening | high_vol |
| 5 | SEF | Siddhartha Equity Fund | 10.65 | 10.10 | -5.16% | 1.4y | high | 21d | -2.74% | 56.7 | ↑ narrowing | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.41 | 9.85 | -5.38% | 2.1y | medium | 7d | -2.16% | 52.9 | → stable | high_vol |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 9 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -14.11% | liquidity:low; maturity:7.2y |
| LUK | -13.38% | liquidity:low; maturity:4.2y |
| SBCF | -13.14% | maturity:4.8y |
| KDBY | -12.20% | maturity:6.1y |
| PRSF | -11.73% | maturity:5.8y |
| SFEF | -11.64% | maturity:5.7y |
| GIBF1 | -10.59% | maturity:6.1y |
| KEF | -10.16% | maturity:4.8y |
| NSIF2 | -9.28% | liquidity:low; maturity:6.2y |
| NMBHF2 | -8.61% | maturity:8.7y |
| GBIMESY2 | -8.60% | maturity:9.1y |
| RSY | -8.48% | maturity:8.9y |
| NICGF2 | -8.21% | maturity:4.5y |
| RBBF40 | -8.10% | liquidity:low; maturity:11.4y |
| RMF2 | -8.07% | liquidity:low; maturity:7.0y |
| H8020 | -7.76% | liquidity:low; maturity:7.3y |
| SIGS3 | -7.65% | maturity:6.9y |
| C30MF | -7.43% | maturity:6.9y |
| MBLEF | -7.36% | maturity:10.8y |
| NIBSF2 | -6.38% | maturity:5.0y |
| SAGF | -5.94% | maturity:7.5y |
| NBF2 | -5.92% | liquidity:low |
| KSY | -5.79% | liquidity:low; maturity:7.8y |
| NIBLGF | -5.53% | maturity:6.6y |
| MNMF1 | -5.21% | maturity:8.5y |
| GSY | -4.87% | maturity:8.6y |
| NIBLSTF | -3.90% | valuation:small_discount; maturity:9.7y |
| SIGS2 | -3.74% | valuation:small_discount |
| NBF3 | -3.68% | valuation:small_discount; maturity:5.3y |
| CMF2 | -3.23% | valuation:small_discount; liquidity:low |
| SLCF | -3.00% | valuation:small_discount |
| MMF1 | -2.58% | valuation:small_discount; maturity:5.2y |
| NICSF | -1.76% | valuation:small_discount |
| HLICF | 1.58% | valuation:premium; maturity:9.3y |
| NMB50 | 4.55% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 24
- NAV data age: median 26 days, max 377 days

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
