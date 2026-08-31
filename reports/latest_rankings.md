# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-31 17:38*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-31 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 33 |
| Median Discount | -12.82% |
| CONSIDER | 7 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 17 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 27 | 69.2% |
| -10% to -6% | 8 | 20.5% |
| -6% to -4% | 3 | 7.7% |
| -4% to 0% | 1 | 2.6% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | LUK | Laxmi Unnati Kosh | 11.66 | 9.12 | -21.78% | 4.0y | high | 1d | -1.17% | 70.0 | ↓ widening | — |
| 2 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.72 | -7.16% | 2.8y | medium | 3d | 0.48% | 53.3 | ↓ widening | — |
| 3 | SEF | Siddhartha Equity Fund | 10.36 | 9.21 | -11.10% | 1.2y | medium | 9d | -2.72% | 53.1 | ↓ widening | — |
| 4 | NICSF | NIC Asia Select-30 | 9.55 | 8.20 | -14.14% | 1.9y | medium | 13d | -2.55% | 52.4 | ↓ widening | — |
| 5 | PSF | Prabhu Select Fund | 13.04 | 11.91 | -8.67% | 1.8y | medium | 61d | -4.26% | 51.0 | → stable | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.28 | 9.30 | -9.53% | 1.9y | medium | 3d | -1.63% | 47.4 | ↓ widening | high_vol |
| 7 | SIGS2 | Siddhartha Investment Gro | 10.85 | 9.90 | -8.76% | 3.0y | high | 2d | -3.30% | 47.0 | ↓ widening | — |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 9 |
| valuation | 1 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -23.02% | maturity:4.6y |
| MBLEF | -21.66% | maturity:10.6y |
| LVF2 | -21.12% | liquidity:low; maturity:7.0y |
| KDBY | -20.07% | maturity:5.9y |
| NMBHF2 | -18.89% | maturity:8.5y |
| KEF | -16.96% | maturity:4.5y |
| NICGF2 | -16.35% | maturity:4.2y |
| NSIF2 | -15.95% | maturity:6.0y |
| SFMF | -14.96% | liquidity:low |
| NICFC | -14.76% | liquidity:low |
| NIBLGF | -14.75% | liquidity:low; maturity:6.4y |
| NICBF | -14.53% | liquidity:low |
| KSY | -14.24% | maturity:7.5y |
| RSY | -13.89% | liquidity:low; maturity:8.7y |
| SFEF | -13.82% | maturity:5.5y |
| NIBLSTF | -13.44% | liquidity:low; maturity:9.4y |
| SIGS3 | -13.37% | maturity:6.7y |
| NIBSF2 | -12.82% | maturity:4.8y |
| MNMF1 | -10.96% | maturity:8.3y |
| SLCF | -10.62% | liquidity:low |
| GSY | -10.44% | maturity:8.3y |
| GBIMESY2 | -10.17% | maturity:8.9y |
| RMF2 | -10.13% | maturity:6.7y |
| GIBF1 | -10.02% | maturity:5.9y |
| RBBF40 | -9.75% | liquidity:low; maturity:11.2y |
| PRSF | -9.48% | maturity:5.5y |
| NBF3 | -9.40% | maturity:5.1y |
| SAGF | -7.50% | maturity:7.2y |
| C30MF | -5.51% | maturity:6.7y |
| MMF1 | -5.49% | maturity:5.0y |
| H8020 | -5.42% | maturity:7.1y |
| HLICF | -2.63% | valuation:small_discount; maturity:9.1y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 33
- NAV data age: median 28 days, max 459 days

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
