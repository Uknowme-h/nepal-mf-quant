# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-29 11:56*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-29 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 22 |
| Median Discount | -8.34% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 17 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 15 | 36.6% |
| -10% to -6% | 16 | 39.0% |
| -6% to -4% | 5 | 12.2% |
| -4% to 0% | 3 | 7.3% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SIGS2 | Siddhartha Investment Gro | 10.98 | 10.20 | -7.10% | 3.3y | medium | 3d | 5.17% | 61.7 | → stable | — |
| 2 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.47 | -9.55% | 3.3y | medium | 2d | 4.39% | 57.1 | ↑ narrowing | high_vol |
| 3 | SEF | Siddhartha Equity Fund | 10.55 | 9.99 | -5.31% | 1.5y | high | 1d | 4.98% | 55.9 | ↑ narrowing | high_vol |
| 4 | SLCF | Sanima Large Cap Fund | 10.60 | 9.80 | -7.55% | 1.8y | high | 15d | 4.43% | 52.7 | ↓ widening | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.62 | -8.90% | 2.2y | medium | 7d | 5.28% | 52.6 | ↓ widening | high_vol |
| 6 | CMF2 | Citizens Mutual Fund - 2 | 10.62 | 9.85 | -7.25% | 0.2y | medium | 1d | 3.31% | 50.4 | ↓ widening | — |
| 7 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.69 | -5.40% | 3.5y | medium | 1d | -2.04% | 50.1 | ↑ narrowing | — |
| 8 | PSF | Prabhu Select Fund | 12.75 | 12.20 | -4.31% | 2.1y | medium | 2d | 5.81% | 42.7 | ↓ widening | — |

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
| SBCF | -15.87% | maturity:4.9y |
| LUK | -15.61% | liquidity:low; maturity:4.3y |
| MBLEF | -13.18% | liquidity:low; maturity:10.9y |
| SFEF | -12.60% | maturity:5.8y |
| GIBF1 | -12.36% | maturity:6.2y |
| NICFC | -11.88% | liquidity:low |
| NIBLSTF | -11.79% | maturity:9.8y |
| RMF2 | -11.27% | liquidity:low; maturity:7.1y |
| RSY | -10.89% | maturity:9.0y |
| KSY | -10.79% | liquidity:low; maturity:7.9y |
| NMBHF2 | -10.79% | maturity:8.8y |
| LVF2 | -10.60% | maturity:7.3y |
| GBIMESY2 | -10.48% | liquidity:low; maturity:9.2y |
| RBBF40 | -10.22% | liquidity:low; maturity:11.6y |
| C30MF | -10.00% | maturity:7.0y |
| NSIF2 | -9.92% | maturity:6.3y |
| GSY | -9.40% | maturity:8.7y |
| NIBLGF | -9.26% | maturity:6.7y |
| NICGF2 | -8.34% | maturity:4.6y |
| SAGF | -8.21% | maturity:7.6y |
| MNMF1 | -7.73% | maturity:8.7y |
| SIGS3 | -7.49% | liquidity:low; maturity:7.0y |
| H8020 | -7.39% | maturity:7.4y |
| NIBSF2 | -7.32% | maturity:5.1y |
| HLICF | -7.05% | maturity:9.4y |
| NICSF | -6.37% | liquidity:low |
| MMF1 | -5.42% | maturity:5.4y |
| NBF3 | -4.55% | maturity:5.4y |
| NBF2 | -3.06% | valuation:small_discount |
| NMB50 | -0.64% | valuation:small_discount; liquidity:low |
| KDBY | -0.26% | valuation:small_discount; maturity:6.2y |
| PRSF | 0.54% | valuation:premium; maturity:5.9y |
| KEF | 0.85% | valuation:premium; maturity:4.9y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 24
- NAV data age: median 45 days, max 335 days

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
