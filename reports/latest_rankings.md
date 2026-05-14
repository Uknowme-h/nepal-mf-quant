# Nepal MF Quant — Full Analysis Report

*Generated: 2026-05-14 12:07*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-05-14 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 25 |
| Median Discount | -9.41% |
| CONSIDER | 5 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 17 | 41.5% |
| -10% to -6% | 18 | 43.9% |
| -6% to -4% | 2 | 4.9% |
| -4% to 0% | 4 | 9.8% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.34 | -11.22% | 3.1y | medium | 4d | 4.26% | 65.6 | ↑ narrowing | — |
| 2 | SEF | Siddhartha Equity Fund | 10.95 | 9.90 | -9.59% | 1.5y | medium | 4d | 3.79% | 54.4 | → stable | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.64 | 10.00 | -6.02% | 2.2y | high | 17d | 0.76% | 53.9 | ↑ narrowing | high_vol |
| 4 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.36 | -8.32% | 3.5y | medium | 1d | -2.04% | 48.1 | → stable | — |
| 5 | NICSF | NIC Asia Select-30 | 9.89 | 9.25 | -6.47% | 2.1y | high | 2d | -1.49% | 38.0 | ↓ widening | — |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| PRSF | -18.68% | maturity:5.8y |
| KEF | -17.06% | maturity:4.8y |
| KDBY | -17.03% | maturity:6.2y |
| PSF | -15.54% | liquidity:low |
| LVF2 | -15.34% | liquidity:low; maturity:7.3y |
| LUK | -14.58% | maturity:4.2y |
| GIBF1 | -13.77% | maturity:6.2y |
| SBCF | -13.67% | liquidity:low; maturity:4.9y |
| SIGS3 | -13.44% | liquidity:low; maturity:7.0y |
| KSY | -13.19% | maturity:7.8y |
| NSIF2 | -11.57% | liquidity:low; maturity:6.3y |
| SFEF | -11.29% | maturity:5.8y |
| NICGF2 | -10.97% | maturity:4.5y |
| MBLEF | -10.93% | maturity:10.9y |
| C30MF | -10.19% | maturity:7.0y |
| RSY | -10.15% | maturity:9.0y |
| SIGS2 | -9.89% | liquidity:low |
| MNMF1 | -9.57% | maturity:8.6y |
| RMF2 | -9.41% | liquidity:low; maturity:7.0y |
| GSY | -9.37% | maturity:8.6y |
| NMBHF2 | -8.43% | maturity:8.8y |
| RBBF40 | -8.37% | maturity:11.5y |
| NIBSF2 | -7.92% | maturity:5.0y |
| NIBLGF | -7.70% | maturity:6.7y |
| GBIMESY2 | -7.65% | maturity:9.2y |
| H8020 | -7.10% | maturity:7.4y |
| SAGF | -7.10% | maturity:7.5y |
| SLCF | -6.85% | liquidity:low |
| NICBF | -6.11% | liquidity:low |
| NIBLSTF | -6.08% | maturity:9.7y |
| MMF1 | -5.81% | maturity:5.3y |
| NBF2 | -4.49% | liquidity:low |
| CMF2 | -3.99% | valuation:small_discount |
| NBF3 | -3.59% | valuation:small_discount; maturity:5.4y |
| NMB50 | -2.42% | valuation:small_discount |
| HLICF | -0.54% | valuation:small_discount; maturity:9.3y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 24
- NAV data age: median 29 days, max 350 days

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
