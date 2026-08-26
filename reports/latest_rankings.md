# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-26 10:51*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-26 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 28 |
| Median Discount | -10.21% |
| CONSIDER | 8 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 21 | 52.5% |
| -10% to -6% | 13 | 32.5% |
| -6% to -4% | 5 | 12.5% |
| -4% to 0% | 1 | 2.5% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.92 | -13.40% | 2.8y | medium | 6d | 0.88% | 69.1 | ↓ widening | — |
| 2 | SEF | Siddhartha Equity Fund | 10.36 | 9.49 | -8.40% | 1.2y | high | 7d | -2.72% | 62.5 | ↑ narrowing | — |
| 3 | NICSF | NIC Asia Select-30 | 9.55 | 8.36 | -12.46% | 1.9y | medium | 11d | -2.55% | 61.9 | ↑ narrowing | — |
| 4 | NMB50 | NMB 50 | 10.45 | 9.68 | -7.37% | 0.0y | medium | 8d | -1.42% | 61.9 | ↓ widening | — |
| 5 | PSF | Prabhu Select Fund | 13.04 | 12.10 | -7.21% | 1.8y | high | 59d | -4.26% | 59.2 | ↑ narrowing | — |
| 6 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.67 | -7.64% | 2.8y | medium | 1d | 0.48% | 53.8 | ↓ widening | — |
| 7 | SLCF | Sanima Large Cap Fund | 10.08 | 9.05 | -10.22% | 1.5y | medium | 1d | -2.70% | 46.9 | ↓ widening | — |
| 8 | RMF1 | RBB Mutual Fund 1 | 10.28 | 9.45 | -8.07% | 1.9y | medium | 1d | -1.63% | 41.8 | ↓ widening | high_vol |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 1 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -21.12% | maturity:7.0y |
| SBCF | -18.78% | maturity:4.6y |
| KDBY | -18.19% | maturity:5.9y |
| KEF | -17.74% | maturity:4.6y |
| NICGF2 | -15.96% | liquidity:low; maturity:4.2y |
| SFEF | -15.75% | maturity:5.5y |
| LUK | -15.69% | liquidity:low |
| NMBHF2 | -15.65% | maturity:8.5y |
| SFMF | -15.04% | liquidity:low |
| NSIF2 | -14.67% | maturity:6.0y |
| NIBSF2 | -12.82% | maturity:4.8y |
| NIBLGF | -12.50% | maturity:6.4y |
| MBLEF | -11.71% | maturity:10.6y |
| RSY | -11.02% | maturity:8.7y |
| NIBLSTF | -11.01% | liquidity:low; maturity:9.5y |
| KSY | -10.69% | liquidity:low; maturity:7.6y |
| GBIMESY2 | -10.37% | liquidity:low; maturity:8.9y |
| PRSF | -10.19% | maturity:5.5y |
| NICBF | -9.88% | liquidity:low |
| GIBF1 | -9.85% | maturity:5.9y |
| RMF2 | -9.67% | liquidity:low; maturity:6.7y |
| MNMF1 | -9.10% | maturity:8.3y |
| GSY | -8.13% | maturity:8.4y |
| C30MF | -7.41% | maturity:6.7y |
| NBF3 | -7.17% | maturity:5.1y |
| RBBF40 | -6.53% | maturity:11.2y |
| SIGS3 | -5.16% | maturity:6.7y |
| HLICF | -4.93% | maturity:9.1y |
| SIGS2 | -4.52% | liquidity:low |
| MMF1 | -4.32% | maturity:5.0y |
| SAGF | -4.17% | liquidity:low; maturity:7.3y |
| H8020 | -3.31% | valuation:small_discount; maturity:7.1y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 27
- NAV data age: median 23 days, max 454 days

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
