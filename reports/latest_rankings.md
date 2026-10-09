# Nepal MF Quant — Full Analysis Report

*Generated: 2026-10-09 17:06*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-10-09 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 32 |
| Median Discount | -10.29% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 21 | 53.8% |
| -10% to -6% | 15 | 38.5% |
| -6% to -4% | 2 | 5.1% |
| -4% to 0% | 1 | 2.6% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.40 | -16.81% | 3.1y | high | 1d | -2.04% | 80.4 | ↑ narrowing | — |
| 2 | LUK | Laxmi Unnati Kosh | 11.66 | 9.35 | -19.81% | 3.9y | medium | 2d | -1.17% | 71.4 | → stable | — |
| 3 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.10 | -13.09% | 2.6y | high | 2d | 0.48% | 69.4 | ↓ widening | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.22 | 9.11 | -10.86% | 1.8y | medium | 10d | -0.87% | 56.7 | ↑ narrowing | high_vol |
| 5 | SEF | Siddhartha Equity Fund | 10.49 | 9.71 | -7.44% | 1.1y | medium | 3d | 1.06% | 56.3 | ↑ narrowing | — |
| 6 | PSF | Prabhu Select Fund | 12.00 | 11.00 | -8.33% | 1.7y | high | 2d | -8.33% | 52.4 | ↑ narrowing | — |
| 7 | NICFC | NIC Asia Flexi Cap Fund | 9.94 | 9.12 | -8.25% | 2.7y | medium | 1d | -1.29% | 51.4 | ↑ narrowing | — |
| 8 | NICSF | NIC Asia Select-30 | 9.28 | 8.50 | -8.41% | 1.7y | medium | 12d | -2.11% | 40.9 | → stable | high_vol |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 1 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -21.70% | liquidity:low; maturity:5.3y |
| SBCF | -20.55% | maturity:4.5y |
| LVF2 | -16.74% | maturity:6.9y |
| RMF2 | -14.15% | liquidity:low; maturity:6.6y |
| NMBHF2 | -13.92% | maturity:8.4y |
| NSIF2 | -13.60% | maturity:5.9y |
| NBF3 | -12.60% | maturity:5.0y |
| GIBF1 | -11.93% | maturity:5.8y |
| C30MF | -11.87% | liquidity:low; maturity:6.6y |
| NICGF2 | -11.75% | maturity:4.1y |
| KSY | -11.19% | maturity:7.5y |
| SAGF | -11.15% | liquidity:low; maturity:7.1y |
| NIBSF2 | -11.01% | maturity:4.6y |
| NIBLGF | -10.87% | maturity:6.3y |
| GSY | -10.85% | maturity:8.2y |
| RSY | -10.29% | maturity:8.6y |
| MNMF1 | -10.19% | maturity:8.2y |
| NIBLSTF | -9.96% | maturity:9.3y |
| SIGS2 | -9.70% | liquidity:low |
| RBBF40 | -9.51% | liquidity:low; maturity:11.1y |
| MBLEF | -9.17% | maturity:10.5y |
| KDBY | -8.87% | maturity:5.8y |
| SLCF | -8.76% | liquidity:low |
| H8020 | -8.62% | maturity:7.0y |
| MMF1 | -8.21% | maturity:4.9y |
| GBIMESY2 | -7.00% | liquidity:low; maturity:8.8y |
| PRSF | -6.99% | maturity:5.4y |
| KEF | -6.95% | maturity:4.4y |
| NICBF | -4.80% | liquidity:low |
| SIGS3 | -4.57% | liquidity:low; maturity:6.6y |
| HLICF | -1.98% | valuation:small_discount; maturity:8.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 31
- NAV data age: median 24 days, max 498 days

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
