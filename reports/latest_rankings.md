# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-17 11:13*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-17 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 15 |
| Median Discount | -7.44% |
| CONSIDER | 5 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 6 | 14.6% |
| -10% to -6% | 23 | 56.1% |
| -6% to -4% | 5 | 12.2% |
| -4% to 0% | 4 | 9.8% |
| ≥ 0% (premium) | 3 | 7.3% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SIGS2 | Siddhartha Investment Gro | 10.98 | 10.31 | -6.10% | 3.4y | medium | 1d | 5.17% | 60.6 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.45 | -10.17% | 3.2y | medium | 1d | 4.26% | 55.6 | → stable | — |
| 3 | SLCF | Sanima Large Cap Fund | 10.60 | 9.95 | -6.13% | 1.9y | medium | 7d | 4.43% | 53.8 | → stable | — |
| 4 | NICSF | NIC Asia Select-30 | 10.04 | 9.27 | -7.67% | 2.2y | medium | 2d | 5.35% | 53.8 | → stable | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.89 | -6.34% | 2.3y | medium | 12d | 5.28% | 53.7 | → stable | high_vol |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 9 |
| valuation | 7 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -14.24% | maturity:4.3y |
| LVF2 | -12.36% | maturity:7.4y |
| SBCF | -11.90% | maturity:4.9y |
| SFEF | -11.46% | maturity:5.8y |
| NSIF2 | -10.66% | maturity:6.4y |
| MBLEF | -9.69% | liquidity:low; maturity:10.9y |
| NIBLSTF | -9.65% | maturity:9.8y |
| KSY | -9.21% | liquidity:low; maturity:7.9y |
| NICBF | -9.07% | liquidity:low |
| RMF2 | -9.05% | maturity:7.1y |
| GIBF1 | -8.97% | maturity:6.3y |
| NIBSF2 | -8.68% | maturity:5.1y |
| GBIMESY2 | -8.65% | maturity:9.3y |
| SFMF | -8.41% | liquidity:low |
| GSY | -7.93% | maturity:8.7y |
| RBBF40 | -7.91% | maturity:11.6y |
| C30MF | -7.73% | maturity:7.1y |
| MNMF1 | -7.46% | maturity:8.7y |
| RSY | -7.44% | maturity:9.1y |
| NIBLGF | -7.41% | maturity:6.8y |
| NMBHF2 | -7.26% | maturity:8.9y |
| NICGF2 | -6.84% | liquidity:low; maturity:4.6y |
| SAGF | -6.48% | liquidity:low; maturity:7.6y |
| H8020 | -6.04% | maturity:7.5y |
| HLICF | -5.71% | liquidity:low; maturity:9.4y |
| SEF | -5.40% | liquidity:low |
| SIGS3 | -5.29% | maturity:7.0y |
| NMB50 | -5.16% | liquidity:low |
| MMF1 | -4.53% | maturity:5.4y |
| CMF2 | -3.95% | valuation:small_discount |
| NBF2 | -3.82% | valuation:small_discount |
| PSF | -3.14% | valuation:small_discount |
| NBF3 | -2.13% | valuation:small_discount; maturity:5.4y |
| PRSF | 1.23% | valuation:premium; maturity:5.9y |
| KEF | 4.17% | valuation:premium; maturity:4.9y |
| KDBY | 5.61% | valuation:premium; maturity:6.3y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 16
- NAV data age: median 33 days, max 323 days

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
