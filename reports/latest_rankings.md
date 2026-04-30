# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-30 11:55*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-30 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 25 |
| Median Discount | -8.77% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 43 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

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
| 1 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.76 | -7.58% | 2.2y | high | 8d | 5.28% | 63.3 | ↑ narrowing | high_vol |
| 2 | NICSF | NIC Asia Select-30 | 10.04 | 9.38 | -6.57% | 2.2y | medium | 1d | 5.35% | 62.8 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.18 | -12.74% | 3.1y | medium | 1d | 4.26% | 58.9 | ↓ widening | — |
| 4 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.38 | -8.14% | 3.5y | medium | 2d | -2.04% | 57.8 | ↑ narrowing | — |
| 5 | SIGS2 | Siddhartha Investment Gro | 10.98 | 9.99 | -9.02% | 3.3y | medium | 4d | 5.17% | 56.6 | ↓ widening | — |
| 6 | SEF | Siddhartha Equity Fund | 10.55 | 9.82 | -6.92% | 1.5y | high | 2d | 4.98% | 56.0 | ↓ widening | high_vol |
| 7 | SLCF | Sanima Large Cap Fund | 10.60 | 9.70 | -8.49% | 1.8y | medium | 16d | 4.43% | 50.7 | ↓ widening | — |
| 8 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.50 | -9.26% | 3.3y | medium | 3d | 4.39% | 41.6 | ↓ widening | high_vol |

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
| SBCF | -16.05% | liquidity:low; maturity:4.9y |
| LUK | -14.75% | maturity:4.3y |
| NICGF2 | -12.75% | liquidity:low; maturity:4.6y |
| MBLEF | -12.74% | maturity:10.9y |
| SFEF | -12.60% | liquidity:low; maturity:5.8y |
| NIBLSTF | -12.28% | maturity:9.8y |
| NMBHF2 | -11.91% | maturity:8.8y |
| GBIMESY2 | -11.54% | maturity:9.2y |
| KSY | -11.53% | liquidity:low; maturity:7.9y |
| NSIF2 | -11.39% | maturity:6.3y |
| RBBF40 | -11.19% | maturity:11.6y |
| GIBF1 | -11.15% | liquidity:low; maturity:6.2y |
| LVF2 | -10.60% | maturity:7.3y |
| RMF2 | -10.38% | liquidity:low; maturity:7.1y |
| GSY | -9.86% | maturity:8.7y |
| NIBSF2 | -9.56% | maturity:5.1y |
| MNMF1 | -9.30% | maturity:8.6y |
| RSY | -8.77% | liquidity:low; maturity:9.0y |
| H8020 | -8.51% | maturity:7.4y |
| C30MF | -8.45% | maturity:7.0y |
| SAGF | -7.85% | maturity:7.6y |
| HLICF | -7.37% | maturity:9.4y |
| CMF2 | -7.25% | liquidity:low |
| NIBLGF | -5.95% | maturity:6.7y |
| MMF1 | -5.81% | maturity:5.4y |
| SIGS3 | -5.64% | liquidity:low; maturity:7.0y |
| NBF3 | -5.23% | maturity:5.4y |
| NBF2 | -4.49% | liquidity:low |
| PSF | -3.53% | valuation:small_discount |
| NMB50 | -3.31% | valuation:small_discount |
| PRSF | 0.00% | valuation:premium; maturity:5.9y |
| KEF | 0.19% | valuation:premium; maturity:4.9y |
| KDBY | 2.54% | valuation:premium; maturity:6.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 43
- NAV data age: median 46 days, max 336 days

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
