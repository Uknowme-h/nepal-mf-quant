# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-02 11:07*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-30 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 30 |
| Median Discount | -10.30% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 17 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 24 | 58.5% |
| -10% to -6% | 8 | 19.5% |
| -6% to -4% | 6 | 14.6% |
| -4% to 0% | 3 | 7.3% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SIGS2 | Siddhartha Investment Gro | 11.53 | 9.99 | -13.36% | 3.3y | medium | 4d | 5.01% | 67.6 | ↓ widening | — |
| 2 | SEF | Siddhartha Equity Fund | 10.95 | 9.82 | -10.32% | 1.5y | high | 2d | 3.79% | 63.5 | ↓ widening | high_vol |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.18 | -12.74% | 3.1y | medium | 1d | 4.26% | 60.2 | ↓ widening | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.64 | 9.76 | -8.27% | 2.2y | high | 8d | 0.76% | 58.9 | ↑ narrowing | high_vol |
| 5 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.38 | -8.14% | 3.5y | medium | 2d | -2.04% | 54.6 | ↑ narrowing | — |
| 6 | NICSF | NIC Asia Select-30 | 9.89 | 9.38 | -5.16% | 2.2y | medium | 1d | -1.49% | 53.3 | ↑ narrowing | — |
| 7 | SLCF | Sanima Large Cap Fund | 10.65 | 9.70 | -8.92% | 1.8y | medium | 16d | 0.47% | 48.8 | ↓ widening | — |
| 8 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.50 | -9.26% | 3.3y | medium | 3d | 4.39% | 40.5 | ↓ widening | high_vol |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| KEF | -17.68% | maturity:4.9y |
| SBCF | -16.05% | liquidity:low; maturity:4.9y |
| KDBY | -14.85% | maturity:6.2y |
| LUK | -14.75% | maturity:4.3y |
| SIGS3 | -12.79% | liquidity:low; maturity:7.0y |
| NICGF2 | -12.75% | liquidity:low; maturity:4.6y |
| SFEF | -12.60% | liquidity:low; maturity:5.8y |
| GBIMESY2 | -12.05% | maturity:9.2y |
| NMBHF2 | -11.91% | maturity:8.8y |
| MBLEF | -11.82% | maturity:10.9y |
| KSY | -11.53% | liquidity:low; maturity:7.9y |
| NSIF2 | -11.39% | maturity:6.3y |
| GIBF1 | -10.93% | liquidity:low; maturity:6.2y |
| RSY | -10.67% | liquidity:low; maturity:9.0y |
| LVF2 | -10.60% | maturity:7.3y |
| NIBLSTF | -10.36% | maturity:9.8y |
| RBBF40 | -10.32% | maturity:11.6y |
| RMF2 | -10.30% | liquidity:low; maturity:7.1y |
| MNMF1 | -10.21% | maturity:8.6y |
| GSY | -10.19% | maturity:8.7y |
| H8020 | -10.15% | maturity:7.4y |
| C30MF | -8.37% | maturity:7.0y |
| NIBSF2 | -8.22% | maturity:5.1y |
| SAGF | -7.85% | maturity:7.6y |
| CMF2 | -6.37% | liquidity:low |
| NBF3 | -5.23% | maturity:5.4y |
| NIBLGF | -4.74% | maturity:6.7y |
| NBF2 | -4.49% | liquidity:low |
| MMF1 | -4.21% | maturity:5.4y |
| HLICF | -4.18% | maturity:9.4y |
| PSF | -3.53% | valuation:small_discount |
| NMB50 | -3.31% | valuation:small_discount |
| PRSF | 0.00% | valuation:premium; maturity:5.9y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 25
- NAV data age: median 17 days, max 338 days

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
