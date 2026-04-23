# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-23 11:24*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-23 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 22 |
| Median Discount | -8.28% |
| CONSIDER | 7 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 22.0% |
| -10% to -6% | 22 | 53.7% |
| -6% to -4% | 4 | 9.8% |
| -4% to 0% | 4 | 9.8% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.50 | -9.70% | 3.1y | medium | 1d | 4.26% | 72.0 | ↑ narrowing | — |
| 2 | NMB50 | NMB 50 | 10.86 | 10.33 | -4.88% | 0.4y | medium | 1d | 5.23% | 56.1 | ↓ widening | — |
| 3 | SLCF | Sanima Large Cap Fund | 10.60 | 9.88 | -6.79% | 1.8y | medium | 11d | 4.43% | 53.8 | ↓ widening | — |
| 4 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.70 | -7.35% | 3.4y | medium | 3d | 4.39% | 53.0 | ↑ narrowing | high_vol |
| 5 | NICSF | NIC Asia Select-30 | 10.04 | 9.18 | -8.57% | 2.2y | medium | 6d | 5.35% | 51.5 | ↓ widening | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.65 | -8.62% | 2.2y | medium | 3d | 5.28% | 50.7 | ↓ widening | high_vol |
| 7 | SEF | Siddhartha Equity Fund | 10.55 | 9.90 | -6.16% | 1.6y | medium | 4d | 4.98% | 39.0 | ↓ widening | high_vol |

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
| LUK | -15.01% | liquidity:low; maturity:4.3y |
| LVF2 | -13.23% | maturity:7.4y |
| SBCF | -12.87% | maturity:4.9y |
| SFEF | -12.07% | maturity:5.8y |
| NICGF2 | -11.90% | liquidity:low; maturity:4.6y |
| NSIF2 | -11.31% | maturity:6.4y |
| KSY | -10.70% | maturity:7.9y |
| MBLEF | -10.12% | maturity:10.9y |
| GBIMESY2 | -10.10% | liquidity:low; maturity:9.2y |
| NIBLSTF | -9.84% | maturity:9.8y |
| RBBF40 | -9.55% | maturity:11.6y |
| GIBF1 | -9.53% | liquidity:low; maturity:6.3y |
| SFMF | -9.29% | liquidity:low |
| NIBSF2 | -8.78% | maturity:5.1y |
| RSY | -8.77% | maturity:9.0y |
| RMF2 | -8.61% | maturity:7.1y |
| NIBLGF | -8.38% | liquidity:low; maturity:6.7y |
| NMBHF2 | -8.28% | maturity:8.8y |
| C30MF | -8.18% | liquidity:low; maturity:7.1y |
| GSY | -7.83% | maturity:8.7y |
| SAGF | -7.76% | maturity:7.6y |
| MNMF1 | -7.46% | maturity:8.7y |
| MMF1 | -6.31% | maturity:5.4y |
| HLICF | -6.22% | maturity:9.4y |
| SIGS2 | -6.19% | liquidity:low |
| CMF2 | -5.84% | liquidity:low |
| SIGS3 | -5.11% | liquidity:low; maturity:7.0y |
| H8020 | -5.01% | maturity:7.5y |
| NBF3 | -3.97% | valuation:small_discount; maturity:5.4y |
| PSF | -3.76% | valuation:small_discount |
| NBF2 | -3.53% | valuation:small_discount |
| KDBY | -0.35% | valuation:small_discount; maturity:6.3y |
| PRSF | 1.31% | valuation:premium; maturity:5.9y |
| KEF | 2.37% | valuation:premium; maturity:4.9y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 23
- NAV data age: median 39 days, max 329 days

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
