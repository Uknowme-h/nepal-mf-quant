# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-08 11:17*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-08 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 16 |
| Median Discount | -7.44% |
| CONSIDER | 7 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 22.0% |
| -10% to -6% | 17 | 41.5% |
| -6% to -4% | 9 | 22.0% |
| -4% to 0% | 4 | 9.8% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SIGS2 | Siddhartha Investment Gro | 10.98 | 10.12 | -7.83% | 3.4y | medium | 1d | 5.17% | 68.5 | ↑ narrowing | — |
| 2 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.85 | -6.72% | 2.3y | high | 6d | 5.28% | 62.7 | ↑ narrowing | high_vol |
| 3 | SLCF | Sanima Large Cap Fund | 10.60 | 10.09 | -4.81% | 1.9y | medium | 1d | 4.43% | 55.5 | ↑ narrowing | — |
| 4 | NICSF | NIC Asia Select-30 | 10.04 | 9.45 | -5.88% | 2.2y | medium | 1d | 5.35% | 53.5 | → stable | — |
| 5 | SEF | Siddhartha Equity Fund | 10.55 | 10.06 | -4.64% | 1.6y | medium | 6d | 4.98% | 52.8 | ↑ narrowing | high_vol |
| 6 | PSF | Prabhu Select Fund | 12.75 | 11.81 | -7.37% | 2.2y | medium | 8d | 5.81% | 52.6 | ↓ widening | — |
| 7 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.39 | -10.74% | 3.2y | medium | 6d | 4.26% | 50.7 | ↓ widening | — |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 6 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -15.18% | liquidity:low; maturity:4.3y |
| SBCF | -13.84% | maturity:5.0y |
| LVF2 | -13.15% | maturity:7.4y |
| KSY | -12.09% | liquidity:low; maturity:8.0y |
| SFEF | -12.07% | liquidity:low; maturity:5.8y |
| GIBF1 | -11.95% | maturity:6.3y |
| NICGF2 | -10.68% | maturity:4.6y |
| MBLEF | -10.65% | maturity:11.0y |
| NSIF2 | -9.84% | maturity:6.4y |
| RSY | -9.39% | maturity:9.1y |
| NIBLSTF | -9.36% | liquidity:low; maturity:9.8y |
| RMF2 | -9.32% | liquidity:low; maturity:7.1y |
| SIGS3 | -8.99% | maturity:7.1y |
| GSY | -8.94% | maturity:8.7y |
| MNMF1 | -8.20% | maturity:8.7y |
| RBBF40 | -7.91% | maturity:11.6y |
| GBIMESY2 | -7.79% | maturity:9.3y |
| C30MF | -7.73% | maturity:7.1y |
| NMBHF2 | -7.44% | maturity:8.9y |
| SAGF | -7.21% | maturity:7.6y |
| H8020 | -7.00% | liquidity:low; maturity:7.5y |
| PRSF | -6.70% | maturity:5.9y |
| SFMF | -5.22% | liquidity:low |
| NIBSF2 | -5.17% | maturity:5.1y |
| MMF1 | -5.02% | maturity:5.4y |
| CMF2 | -4.80% | liquidity:low |
| NIBLGF | -4.58% | liquidity:low; maturity:6.8y |
| NBF3 | -4.07% | maturity:5.5y |
| HLICF | -3.01% | valuation:small_discount; liquidity:low; maturity:9.4y |
| NMB50 | -2.76% | valuation:small_discount |
| NBF2 | -2.58% | valuation:small_discount |
| KDBY | -1.31% | valuation:small_discount; maturity:6.3y |
| KEF | 0.28% | valuation:premium; maturity:5.0y |
| NICBF | 0.67% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 18
- NAV data age: median 24 days, max 314 days

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
