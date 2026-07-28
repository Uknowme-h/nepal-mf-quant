# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-28 12:12*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-28 |
| Funds Tracked | 38 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 25 |
| Median Discount | -9.48% |
| CONSIDER | 6 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 16 | 42.1% |
| -10% to -6% | 16 | 42.1% |
| -6% to -4% | 2 | 5.3% |
| -4% to 0% | 4 | 10.5% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.22 | -10.49% | 2.9y | medium | 8d | 0.88% | 67.3 | ↑ narrowing | — |
| 2 | NICSF | NIC Asia Select-30 | 9.80 | 8.90 | -9.18% | 1.9y | high | 3d | 1.45% | 60.9 | ↓ widening | — |
| 3 | PSF | Prabhu Select Fund | 13.69 | 11.85 | -13.44% | 1.9y | medium | 39d | -4.60% | 59.0 | ↓ widening | — |
| 4 | SIGS2 | Siddhartha Investment Gro | 11.22 | 10.50 | -6.42% | 3.1y | medium | 3d | -0.09% | 52.9 | ↑ narrowing | — |
| 5 | SEF | Siddhartha Equity Fund | 10.65 | 9.79 | -8.08% | 1.3y | high | 1d | 0.00% | 47.6 | ↓ widening | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.68 | -7.37% | 2.0y | medium | 8d | 0.38% | 43.8 | ↓ widening | high_vol |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 27 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -18.05% | liquidity:low; maturity:7.1y |
| SBCF | -14.64% | maturity:4.7y |
| KDBY | -13.60% | maturity:6.0y |
| PRSF | -13.41% | maturity:5.6y |
| SFEF | -12.51% | maturity:5.5y |
| KEF | -11.80% | maturity:4.6y |
| RBBF40 | -11.33% | maturity:11.3y |
| SIGS3 | -10.92% | maturity:6.8y |
| GBIMESY2 | -10.86% | maturity:9.0y |
| GIBF1 | -10.78% | maturity:6.0y |
| NICGF2 | -10.58% | maturity:4.3y |
| SFMF | -10.53% | liquidity:low |
| NIBLSTF | -10.20% | liquidity:low; maturity:9.5y |
| RSY | -10.13% | maturity:8.8y |
| MNMF1 | -9.60% | maturity:8.4y |
| RMF2 | -9.58% | liquidity:low; maturity:6.8y |
| NICBF | -9.50% | liquidity:low |
| NIBSF2 | -9.47% | maturity:4.8y |
| MBLEF | -9.26% | maturity:10.7y |
| NMBHF2 | -9.00% | maturity:8.6y |
| NSIF2 | -8.72% | maturity:6.1y |
| NIBLGF | -7.62% | liquidity:low; maturity:6.5y |
| SAGF | -7.12% | liquidity:low; maturity:7.3y |
| MMF1 | -6.75% | maturity:5.1y |
| H8020 | -6.42% | liquidity:low; maturity:7.2y |
| HLICF | -6.14% | liquidity:low; maturity:9.1y |
| NBF3 | -5.91% | maturity:5.2y |
| KSY | -5.87% | maturity:7.7y |
| SLCF | -3.76% | valuation:small_discount |
| NBF2 | -2.58% | valuation:small_discount; liquidity:low |
| NMB50 | -2.36% | valuation:small_discount |
| GSY | -0.29% | valuation:small_discount; maturity:8.4y |

</details>

## Data Quality

- Symbols checked: 44
- Symbols with issues: 24
- NAV data age: median 43 days, max 425 days

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
