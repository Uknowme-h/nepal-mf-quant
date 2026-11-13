# Nepal MF Quant — Full Analysis Report

*Generated: 2026-11-13 17:44*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-11-13 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 21 |
| Median Discount | -8.66% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 13 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 12 | 30.8% |
| -10% to -6% | 18 | 46.2% |
| -6% to -4% | 6 | 15.4% |
| -4% to 0% | 2 | 5.1% |
| ≥ 0% (premium) | 1 | 2.6% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.20 | -12.13% | 2.5y | medium | 8d | 0.48% | 70.8 | → stable | — |
| 2 | SEF | Siddhartha Equity Fund | 10.78 | 10.00 | -7.24% | 1.0y | high | 17d | 2.76% | 66.2 | → stable | — |
| 3 | PSF | Prabhu Select Fund | 12.40 | 11.72 | -5.48% | 1.6y | medium | 1d | 3.33% | 63.3 | ↑ narrowing | — |
| 4 | SIGS2 | Siddhartha Investment Gro | 10.65 | 9.96 | -6.48% | 2.8y | medium | 3d | 3.30% | 62.8 | ↑ narrowing | — |
| 5 | SLCF | Sanima Large Cap Fund | 10.10 | 9.11 | -9.80% | 1.3y | medium | 3d | 0.60% | 50.8 | ↓ widening | — |
| 6 | NICFC | NIC Asia Flexi Cap Fund | 9.94 | 9.32 | -6.24% | 2.6y | medium | 4d | -1.29% | 48.9 | ↑ narrowing | — |
| 7 | NICBF | NIC ASIA Balanced Fund | 10.01 | 9.21 | -7.99% | 2.8y | medium | 1d | -0.99% | 48.2 | → stable | — |
| 8 | NICSF | NIC Asia Select-30 | 9.50 | 8.69 | -8.53% | 1.6y | medium | 26d | 2.37% | 48.0 | ↓ widening | high_vol |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -21.69% | maturity:4.4y |
| SFEF | -20.21% | liquidity:low; maturity:5.2y |
| LVF2 | -20.07% | maturity:6.8y |
| LUK | -19.38% | liquidity:low |
| SFMF | -12.39% | liquidity:low |
| RMF1 | -11.07% | liquidity:low |
| NBF3 | -10.85% | maturity:4.9y |
| MBLEF | -10.77% | maturity:10.4y |
| RMF2 | -10.47% | liquidity:low; maturity:6.5y |
| RBBF40 | -10.23% | maturity:11.0y |
| GSY | -10.02% | maturity:8.1y |
| KEF | -9.62% | maturity:4.3y |
| MNMF1 | -9.21% | maturity:8.1y |
| RSY | -9.13% | maturity:8.5y |
| C30MF | -9.09% | liquidity:low; maturity:6.5y |
| NIBSF2 | -8.83% | maturity:4.5y |
| NICGF2 | -8.81% | maturity:4.0y |
| NIBLGF | -8.66% | liquidity:low; maturity:6.2y |
| KSY | -7.83% | liquidity:low; maturity:7.3y |
| NIBLSTF | -7.83% | maturity:9.2y |
| MMF1 | -7.60% | maturity:4.8y |
| GBIMESY2 | -7.57% | maturity:8.7y |
| KDBY | -7.25% | maturity:5.7y |
| NMBHF2 | -5.85% | maturity:8.3y |
| SAGF | -5.30% | liquidity:low; maturity:7.0y |
| NSIF2 | -5.12% | maturity:5.8y |
| GIBF1 | -4.96% | liquidity:low; maturity:5.7y |
| PRSF | -4.69% | maturity:5.3y |
| HLICF | -3.24% | valuation:small_discount; maturity:8.8y |
| SIGS3 | -2.18% | valuation:small_discount; maturity:6.5y |
| H8020 | 3.77% | valuation:premium; maturity:6.9y |

</details>

## Data Quality

- Symbols checked: 49
- Symbols with issues: 34
- NAV data age: median 29 days, max 533 days

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
