# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-16 11:54*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-16 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 19 |
| Median Discount | -7.72% |
| CONSIDER | 5 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 14 | 35.0% |
| -10% to -6% | 9 | 22.5% |
| -6% to -4% | 5 | 12.5% |
| -4% to 0% | 10 | 25.0% |
| ≥ 0% (premium) | 2 | 5.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.90 | -5.44% | 2.9y | medium | 7d | 0.48% | 56.9 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 13.69 | 11.80 | -13.81% | 1.9y | medium | 31d | -4.60% | 55.9 | ↓ widening | — |
| 3 | SEF | Siddhartha Equity Fund | 10.65 | 10.02 | -5.92% | 1.3y | medium | 10d | 0.00% | 55.5 | ↑ narrowing | — |
| 4 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.00 | -11.50% | 3.3y | medium | 4d | -2.04% | 51.8 | ↓ widening | — |
| 5 | NICSF | NIC Asia Select-30 | 9.80 | 9.10 | -7.14% | 2.0y | medium | 9d | 1.45% | 48.7 | ↓ widening | — |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| valuation | 12 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -16.78% | maturity:5.7y |
| KDBY | -16.03% | maturity:6.0y |
| LUK | -15.09% | liquidity:low; maturity:4.1y |
| KEF | -14.98% | liquidity:low; maturity:4.7y |
| LVF2 | -14.37% | maturity:7.1y |
| NSIF2 | -14.25% | liquidity:low; maturity:6.1y |
| SBCF | -14.02% | maturity:4.7y |
| NICFC | -12.80% | liquidity:low |
| GIBF1 | -12.28% | maturity:6.0y |
| SIGS3 | -11.76% | liquidity:low; maturity:6.8y |
| NICBF | -10.98% | liquidity:low |
| SFEF | -10.85% | maturity:5.6y |
| RSY | -9.78% | maturity:8.8y |
| RMF2 | -9.58% | maturity:6.8y |
| NICGF2 | -9.36% | maturity:4.3y |
| MBLEF | -9.26% | liquidity:low; maturity:10.7y |
| NIBSF2 | -8.36% | maturity:4.9y |
| NIBLSTF | -7.76% | maturity:9.6y |
| H8020 | -7.69% | maturity:7.2y |
| MNMF1 | -6.78% | maturity:8.4y |
| C30MF | -5.64% | liquidity:low; maturity:6.8y |
| KSY | -5.11% | liquidity:low; maturity:7.7y |
| NMBHF2 | -4.07% | maturity:8.6y |
| NMB50 | -3.96% | valuation:small_discount |
| RMF1 | -3.83% | valuation:small_discount |
| NBF3 | -3.78% | valuation:small_discount; maturity:5.2y |
| SAGF | -3.42% | valuation:small_discount; liquidity:low; maturity:7.4y |
| HLICF | -2.90% | valuation:small_discount; maturity:9.2y |
| GBIMESY2 | -2.35% | valuation:small_discount; maturity:9.0y |
| SIGS2 | -1.96% | valuation:small_discount |
| GSY | -1.81% | valuation:small_discount; maturity:8.5y |
| RBBF40 | -1.58% | valuation:small_discount; maturity:11.3y |
| MMF1 | -0.31% | valuation:small_discount; maturity:5.2y |
| SLCF | 1.83% | valuation:premium |
| NIBLGF | 9.32% | valuation:premium; maturity:6.5y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 25
- NAV data age: median 31 days, max 413 days

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
