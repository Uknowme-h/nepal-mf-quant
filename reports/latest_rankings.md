# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-29 16:31*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-29 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 35 |
| Median Discount | -12.73% |
| CONSIDER | 7 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 32 | 82.1% |
| -10% to -6% | 6 | 15.4% |
| -6% to -4% | 1 | 2.6% |
| -4% to 0% | 0 | 0.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.20 | -18.58% | 3.1y | medium | 2d | -2.04% | 74.7 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 13.09 | 10.85 | -17.11% | 1.7y | medium | 78d | 0.38% | 69.5 | ↓ widening | — |
| 3 | SIGS2 | Siddhartha Investment Gro | 10.95 | 9.56 | -12.69% | 2.9y | medium | 1d | -3.30% | 60.4 | ↑ narrowing | — |
| 4 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.27 | -11.46% | 2.7y | medium | 5d | 0.48% | 59.5 | → stable | — |
| 5 | NICSF | NIC Asia Select-30 | 9.48 | 8.60 | -9.28% | 1.8y | medium | 5d | -3.27% | 49.4 | ↑ narrowing | high_vol |
| 6 | SEF | Siddhartha Equity Fund | 10.36 | 9.60 | -7.34% | 1.1y | medium | 26d | -2.72% | 47.2 | → stable | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.31 | 8.91 | -13.58% | 1.8y | medium | 3d | -1.63% | 45.6 | ↓ widening | high_vol |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -21.52% | liquidity:low; maturity:4.5y |
| SFEF | -21.26% | maturity:5.4y |
| LUK | -20.24% | liquidity:low |
| LVF2 | -19.72% | maturity:6.9y |
| KDBY | -16.81% | maturity:5.8y |
| NICGF2 | -16.44% | liquidity:low; maturity:4.2y |
| MBLEF | -16.19% | liquidity:low; maturity:10.5y |
| RSY | -16.15% | maturity:8.6y |
| KEF | -15.67% | maturity:4.5y |
| NSIF2 | -15.31% | maturity:5.9y |
| NMBHF2 | -15.07% | maturity:8.4y |
| PRSF | -14.72% | maturity:5.5y |
| RMF2 | -13.93% | liquidity:low; maturity:6.7y |
| C30MF | -13.02% | maturity:6.6y |
| H8020 | -12.84% | maturity:7.0y |
| MNMF1 | -12.75% | maturity:8.2y |
| GIBF1 | -12.73% | maturity:5.8y |
| NICBF | -12.40% | liquidity:low |
| NBF3 | -11.82% | maturity:5.0y |
| SIGS3 | -11.69% | maturity:6.6y |
| RBBF40 | -11.42% | maturity:11.1y |
| NIBLSTF | -11.33% | maturity:9.4y |
| NIBLGF | -11.26% | maturity:6.3y |
| NICFC | -11.17% | liquidity:low |
| SLCF | -11.14% | liquidity:low |
| MMF1 | -11.09% | maturity:5.0y |
| NIBSF2 | -11.07% | maturity:4.7y |
| GBIMESY2 | -9.26% | maturity:8.8y |
| GSY | -9.14% | maturity:8.3y |
| SAGF | -7.56% | liquidity:low; maturity:7.2y |
| KSY | -6.75% | liquidity:low; maturity:7.5y |
| HLICF | -4.37% | maturity:9.0y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 24
- NAV data age: median 45 days, max 488 days

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
