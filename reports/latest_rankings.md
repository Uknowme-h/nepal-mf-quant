# Nepal MF Quant — Full Analysis Report

*Generated: 2026-10-27 15:53*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-10-27 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 23 |
| Median Discount | -8.50% |
| CONSIDER | 7 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 10 | 25.6% |
| -10% to -6% | 22 | 56.4% |
| -6% to -4% | 4 | 10.3% |
| -4% to 0% | 3 | 7.7% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.46 | -16.28% | 3.0y | medium | 1d | -2.04% | 76.8 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 9.94 | 9.02 | -9.26% | 2.6y | medium | 2d | -1.29% | 64.6 | ↑ narrowing | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.22 | 9.07 | -11.25% | 1.7y | high | 16d | -0.87% | 60.5 | ↓ widening | high_vol |
| 4 | SEF | Siddhartha Equity Fund | 10.49 | 9.95 | -5.15% | 1.0y | high | 9d | 1.06% | 60.3 | ↑ narrowing | — |
| 5 | SIGS2 | Siddhartha Investment Gro | 10.31 | 9.55 | -7.37% | 2.8y | medium | 2d | -5.84% | 54.9 | ↑ narrowing | — |
| 6 | NICSF | NIC Asia Select-30 | 9.28 | 8.78 | -5.39% | 1.7y | medium | 18d | -2.11% | 54.4 | ↑ narrowing | high_vol |
| 7 | PSF | Prabhu Select Fund | 12.00 | 11.24 | -6.33% | 1.6y | high | 8d | -8.33% | 47.6 | ↑ narrowing | — |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -19.34% | maturity:5.3y |
| LVF2 | -19.11% | liquidity:low; maturity:6.9y |
| LUK | -18.01% | liquidity:low |
| SBCF | -16.40% | maturity:4.4y |
| NBF2 | -13.09% | liquidity:low |
| RMF2 | -11.19% | liquidity:low; maturity:6.6y |
| C30MF | -10.81% | liquidity:low; maturity:6.5y |
| GIBF1 | -10.56% | maturity:5.8y |
| NBF3 | -9.88% | maturity:4.9y |
| MNMF1 | -9.69% | maturity:8.2y |
| NICGF2 | -9.63% | liquidity:low; maturity:4.1y |
| KSY | -9.17% | maturity:7.4y |
| H8020 | -9.02% | maturity:6.9y |
| NICBF | -8.99% | liquidity:low |
| RBBF40 | -8.91% | maturity:11.1y |
| NIBLGF | -8.54% | maturity:6.2y |
| GBIMESY2 | -8.50% | liquidity:low; maturity:8.7y |
| NIBLSTF | -8.37% | maturity:9.3y |
| SLCF | -8.37% | liquidity:low |
| NIBSF2 | -8.13% | maturity:4.6y |
| NMBHF2 | -7.96% | maturity:8.3y |
| RSY | -7.69% | maturity:8.5y |
| MBLEF | -7.50% | maturity:10.4y |
| KEF | -7.44% | maturity:4.4y |
| SAGF | -7.20% | maturity:7.1y |
| GSY | -6.61% | maturity:8.2y |
| KDBY | -6.33% | maturity:5.8y |
| MMF1 | -5.89% | maturity:4.9y |
| PRSF | -4.30% | maturity:5.4y |
| NSIF2 | -2.75% | valuation:small_discount; maturity:5.8y |
| SIGS3 | -2.52% | valuation:small_discount; liquidity:low; maturity:6.5y |
| HLICF | -0.12% | valuation:small_discount; maturity:8.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 28
- NAV data age: median 42 days, max 516 days

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
