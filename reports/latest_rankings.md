# Nepal MF Quant — Full Analysis Report

*Generated: 2026-10-08 17:25*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-10-08 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 31 |
| Median Discount | -9.81% |
| CONSIDER | 7 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 18 | 46.2% |
| -10% to -6% | 18 | 46.2% |
| -6% to -4% | 1 | 2.6% |
| -4% to 0% | 2 | 5.1% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | LUK | Laxmi Unnati Kosh | 11.66 | 9.31 | -20.15% | 3.9y | medium | 1d | -1.17% | 66.4 | → stable | — |
| 2 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.32 | -10.98% | 2.6y | medium | 1d | 0.48% | 59.7 | ↓ widening | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.22 | 9.25 | -9.49% | 1.8y | medium | 9d | -0.87% | 57.3 | ↑ narrowing | high_vol |
| 4 | SEF | Siddhartha Equity Fund | 10.49 | 9.71 | -7.44% | 1.1y | high | 2d | 1.06% | 51.4 | → stable | — |
| 5 | SLCF | Sanima Large Cap Fund | 10.04 | 9.40 | -6.37% | 1.4y | medium | 6d | -0.99% | 49.0 | ↑ narrowing | — |
| 6 | PSF | Prabhu Select Fund | 12.00 | 10.90 | -9.17% | 1.7y | medium | 1d | -8.33% | 48.2 | ↑ narrowing | — |
| 7 | NICSF | NIC Asia Select-30 | 9.28 | 8.40 | -9.48% | 1.7y | medium | 11d | -2.11% | 45.0 | ↑ narrowing | high_vol |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 8 |
| valuation | 2 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -21.87% | maturity:5.3y |
| SBCF | -19.84% | maturity:4.5y |
| SFMF | -19.56% | liquidity:low |
| RMF2 | -16.74% | maturity:6.6y |
| LVF2 | -16.39% | maturity:6.9y |
| NSIF2 | -13.86% | maturity:5.9y |
| NMBHF2 | -13.63% | liquidity:low; maturity:8.4y |
| NBF3 | -12.79% | maturity:5.0y |
| SAGF | -12.48% | liquidity:low; maturity:7.1y |
| NIBLSTF | -11.55% | maturity:9.3y |
| NIBLGF | -11.28% | maturity:6.3y |
| GIBF1 | -10.99% | maturity:5.8y |
| NICFC | -10.87% | liquidity:low |
| NICGF2 | -10.84% | liquidity:low; maturity:4.1y |
| KSY | -10.28% | maturity:7.5y |
| NIBSF2 | -10.19% | maturity:4.6y |
| GSY | -9.96% | maturity:8.2y |
| RBBF40 | -9.81% | maturity:11.1y |
| MBLEF | -9.76% | maturity:10.5y |
| SIGS2 | -9.70% | liquidity:low |
| RSY | -9.62% | maturity:8.6y |
| GBIMESY2 | -9.60% | maturity:8.8y |
| C30MF | -9.57% | maturity:6.6y |
| MNMF1 | -9.50% | maturity:8.2y |
| KDBY | -9.41% | liquidity:low; maturity:5.8y |
| H8020 | -9.10% | maturity:7.0y |
| KEF | -7.93% | maturity:4.4y |
| PRSF | -7.76% | maturity:5.4y |
| MMF1 | -7.05% | maturity:4.9y |
| NICBF | -4.80% | liquidity:low |
| HLICF | -3.62% | valuation:small_discount; maturity:8.9y |
| SIGS3 | -3.54% | valuation:small_discount; maturity:6.6y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 26
- NAV data age: median 23 days, max 497 days

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
