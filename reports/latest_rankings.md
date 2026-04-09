# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-09 11:18*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-09 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 16 |
| Median Discount | -7.43% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 22.0% |
| -10% to -6% | 20 | 48.8% |
| -6% to -4% | 8 | 19.5% |
| -4% to 0% | 2 | 4.9% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.50 | -9.70% | 3.2y | medium | 7d | 4.26% | 63.8 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 12.75 | 12.06 | -5.41% | 2.2y | medium | 9d | 5.81% | 63.0 | ↑ narrowing | — |
| 3 | SIGS2 | Siddhartha Investment Gro | 10.98 | 10.03 | -8.65% | 3.4y | medium | 2d | 5.17% | 57.2 | ↓ widening | — |
| 4 | SLCF | Sanima Large Cap Fund | 10.60 | 9.91 | -6.51% | 1.9y | medium | 2d | 4.43% | 51.8 | ↑ narrowing | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.87 | -6.53% | 2.3y | medium | 7d | 5.28% | 51.6 | ↑ narrowing | high_vol |
| 6 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.83 | -6.11% | 3.4y | medium | 1d | 4.39% | 48.5 | ↑ narrowing | high_vol |
| 7 | NICSF | NIC Asia Select-30 | 10.04 | 9.30 | -7.37% | 2.2y | medium | 2d | 5.35% | 47.2 | ↓ widening | — |
| 8 | SEF | Siddhartha Equity Fund | 10.55 | 9.90 | -6.16% | 1.6y | medium | 7d | 4.98% | 40.6 | ↓ widening | high_vol |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -16.72% | maturity:4.3y |
| LVF2 | -13.23% | liquidity:low; maturity:7.4y |
| SBCF | -11.90% | maturity:5.0y |
| MBLEF | -11.87% | maturity:11.0y |
| SFEF | -11.55% | maturity:5.8y |
| NICGF2 | -11.25% | liquidity:low; maturity:4.6y |
| RMF2 | -10.83% | maturity:7.1y |
| NSIF2 | -10.25% | maturity:6.4y |
| KSY | -10.23% | liquidity:low; maturity:8.0y |
| NIBLSTF | -9.84% | maturity:9.8y |
| RSY | -9.39% | maturity:9.1y |
| GIBF1 | -8.72% | maturity:6.3y |
| H8020 | -8.59% | maturity:7.5y |
| GBIMESY2 | -8.08% | maturity:9.3y |
| MNMF1 | -7.92% | maturity:8.7y |
| GSY | -7.83% | maturity:8.7y |
| SIGS3 | -7.58% | liquidity:low; maturity:7.1y |
| C30MF | -7.45% | maturity:7.1y |
| RBBF40 | -7.43% | maturity:11.6y |
| NIBSF2 | -7.32% | maturity:5.1y |
| NMBHF2 | -7.07% | maturity:8.9y |
| SAGF | -6.75% | liquidity:low; maturity:7.6y |
| SFMF | -5.22% | liquidity:low |
| MMF1 | -4.83% | maturity:5.4y |
| PRSF | -4.70% | maturity:5.9y |
| NMB50 | -4.24% | liquidity:low |
| CMF2 | -4.05% | liquidity:low |
| NBF2 | -4.01% | liquidity:low |
| NIBLGF | -4.00% | liquidity:low; maturity:6.8y |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.5y |
| HLICF | -3.01% | valuation:small_discount; maturity:9.4y |
| KEF | 0.28% | valuation:premium; maturity:4.9y |
| KDBY | 1.75% | valuation:premium; maturity:6.3y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 15
- NAV data age: median 25 days, max 315 days

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
