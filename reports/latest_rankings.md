# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-02 14:23*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-02 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 15 |
| Median Discount | -6.71% |
| CONSIDER | 4 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 22.5% |
| -10% to -6% | 16 | 40.0% |
| -6% to -4% | 6 | 15.0% |
| -4% to 0% | 7 | 17.5% |
| ≥ 0% (premium) | 2 | 5.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.30 | -10.49% | 3.0y | medium | 4d | -1.24% | 61.8 | ↓ widening | — |
| 2 | SEF | Siddhartha Equity Fund | 10.65 | 10.00 | -6.10% | 1.4y | high | 15d | -2.74% | 45.9 | ↓ widening | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.41 | 9.80 | -5.86% | 2.1y | medium | 1d | -2.16% | 42.2 | ↓ widening | high_vol |
| 4 | NICSF | NIC Asia Select-30 | 9.66 | 9.13 | -5.49% | 2.1y | medium | 3d | -2.33% | 40.0 | ↓ widening | — |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 9 |
| valuation | 9 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -14.24% | liquidity:low; maturity:4.2y |
| SBCF | -13.76% | liquidity:low; maturity:4.8y |
| LVF2 | -13.23% | liquidity:low; maturity:7.3y |
| PRSF | -12.47% | maturity:5.8y |
| SFEF | -12.42% | maturity:5.7y |
| NICGF2 | -10.98% | maturity:4.5y |
| KDBY | -10.41% | maturity:6.2y |
| PSF | -10.15% | liquidity:low |
| SFMF | -9.73% | liquidity:low |
| NSIF2 | -9.70% | liquidity:low; maturity:6.2y |
| KEF | -9.49% | maturity:4.8y |
| RSY | -9.36% | maturity:8.9y |
| GIBF1 | -8.26% | maturity:6.2y |
| GBIMESY2 | -8.11% | maturity:9.1y |
| MBLEF | -7.36% | maturity:10.8y |
| NIBLGF | -7.34% | maturity:6.6y |
| KSY | -7.02% | maturity:7.8y |
| NMBHF2 | -7.00% | maturity:8.8y |
| NIBSF2 | -6.79% | maturity:5.0y |
| MNMF1 | -6.64% | maturity:8.6y |
| RBBF40 | -6.62% | maturity:11.4y |
| C30MF | -6.60% | liquidity:low; maturity:7.0y |
| NICBF | -6.55% | liquidity:low |
| SAGF | -5.76% | maturity:7.5y |
| RMF2 | -5.62% | liquidity:low; maturity:7.0y |
| SIGS3 | -5.38% | maturity:6.9y |
| H8020 | -5.07% | maturity:7.3y |
| SIGS2 | -3.74% | valuation:small_discount |
| GSY | -3.53% | valuation:small_discount; maturity:8.6y |
| SLCF | -3.29% | valuation:small_discount |
| CMF2 | -3.23% | valuation:small_discount |
| NBF3 | -3.20% | valuation:small_discount; maturity:5.3y |
| MMF1 | -2.58% | valuation:small_discount; maturity:5.3y |
| NBF2 | -0.76% | valuation:small_discount |
| HLICF | 1.47% | valuation:premium; maturity:9.3y |
| NMB50 | 2.47% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 20
- NAV data age: median 18 days, max 369 days

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
