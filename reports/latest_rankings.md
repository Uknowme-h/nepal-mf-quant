# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-20 12:28*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-20 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 20 |
| Median Discount | -8.36% |
| CONSIDER | 6 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 14 | 35.0% |
| -10% to -6% | 15 | 37.5% |
| -6% to -4% | 3 | 7.5% |
| -4% to 0% | 6 | 15.0% |
| ≥ 0% (premium) | 2 | 5.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.69 | 12.00 | -12.34% | 1.9y | medium | 33d | -4.60% | 66.6 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.30 | -9.71% | 2.9y | medium | 2d | 0.88% | 61.9 | ↑ narrowing | — |
| 3 | NICBF | NIC ASIA Balanced Fund | 10.32 | 9.10 | -11.82% | 3.1y | medium | 1d | 0.88% | 59.2 | ↑ narrowing | high_vol |
| 4 | SEF | Siddhartha Equity Fund | 10.65 | 10.20 | -4.23% | 1.3y | high | 12d | 0.00% | 54.0 | ↑ narrowing | — |
| 5 | NICSF | NIC Asia Select-30 | 9.80 | 9.27 | -5.41% | 2.0y | medium | 11d | 1.45% | 47.3 | ↑ narrowing | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.75 | -6.70% | 2.0y | high | 2d | 0.38% | 45.3 | → stable | high_vol |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 9 |
| valuation | 8 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -14.67% | liquidity:low; maturity:4.1y |
| PRSF | -14.08% | maturity:5.7y |
| LVF2 | -14.02% | maturity:7.1y |
| KDBY | -13.21% | maturity:6.0y |
| SIGS3 | -12.86% | maturity:6.8y |
| SFEF | -12.51% | liquidity:low; maturity:5.6y |
| NSIF2 | -12.32% | liquidity:low; maturity:6.1y |
| GIBF1 | -12.28% | maturity:6.0y |
| KEF | -12.13% | maturity:4.7y |
| RSY | -11.01% | maturity:8.8y |
| SBCF | -10.49% | maturity:4.7y |
| NICGF2 | -10.10% | maturity:4.3y |
| RMF2 | -9.67% | maturity:6.8y |
| RBBF40 | -9.56% | maturity:11.3y |
| NIBSF2 | -9.37% | maturity:4.9y |
| NIBLSTF | -9.08% | maturity:9.6y |
| MBLEF | -8.80% | maturity:10.7y |
| H8020 | -7.92% | liquidity:low; maturity:7.2y |
| KSY | -7.76% | liquidity:low; maturity:7.7y |
| NMBHF2 | -7.48% | maturity:8.6y |
| C30MF | -7.31% | maturity:6.8y |
| SFMF | -7.08% | liquidity:low |
| GBIMESY2 | -7.05% | maturity:9.0y |
| MNMF1 | -6.78% | maturity:8.4y |
| SIGS2 | -6.42% | liquidity:low |
| GSY | -4.67% | maturity:8.5y |
| NBF2 | -3.53% | valuation:small_discount |
| SLCF | -3.47% | valuation:small_discount |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.2y |
| SAGF | -3.05% | valuation:small_discount; liquidity:low; maturity:7.4y |
| HLICF | -2.46% | valuation:small_discount; maturity:9.2y |
| MMF1 | -0.31% | valuation:small_discount; maturity:5.1y |
| NMB50 | 2.64% | valuation:premium |
| NIBLGF | 5.71% | valuation:premium; liquidity:low; maturity:6.5y |

</details>

## Data Quality

- Symbols checked: 44
- Symbols with issues: 30
- NAV data age: median 35 days, max 417 days

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
