# Nepal MF Quant — Full Analysis Report

*Generated: 2026-10-15 14:59*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-10-15 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 27 |
| Median Discount | -9.46% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 15 | 38.5% |
| -10% to -6% | 21 | 53.8% |
| -6% to -4% | 3 | 7.7% |
| -4% to 0% | 0 | 0.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | LUK | Laxmi Unnati Kosh | 11.66 | 9.88 | -15.27% | 3.8y | high | 5d | -1.17% | 81.9 | ↑ narrowing | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.40 | -16.81% | 3.1y | medium | 4d | -2.04% | 78.6 | ↑ narrowing | — |
| 3 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.10 | -13.09% | 2.6y | high | 5d | 0.48% | 71.8 | ↓ widening | — |
| 4 | SEF | Siddhartha Equity Fund | 10.49 | 9.81 | -6.48% | 1.1y | high | 6d | 1.06% | 60.6 | ↑ narrowing | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.22 | 9.32 | -8.81% | 1.8y | high | 13d | -0.87% | 55.4 | → stable | high_vol |
| 6 | NICSF | NIC Asia Select-30 | 9.28 | 8.60 | -7.33% | 1.7y | medium | 15d | -2.11% | 51.9 | ↑ narrowing | high_vol |
| 7 | PSF | Prabhu Select Fund | 12.00 | 10.94 | -8.83% | 1.7y | medium | 5d | -8.33% | 49.5 | → stable | — |
| 8 | SIGS2 | Siddhartha Investment Gro | 10.31 | 9.58 | -7.08% | 2.9y | medium | 1d | -5.84% | 47.8 | → stable | — |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -20.63% | liquidity:low; maturity:4.5y |
| LVF2 | -19.11% | liquidity:low; maturity:6.9y |
| SFEF | -16.89% | maturity:5.3y |
| RMF2 | -14.89% | liquidity:low; maturity:6.6y |
| GIBF1 | -12.86% | maturity:5.8y |
| NBF3 | -12.21% | maturity:4.9y |
| NICGF2 | -11.75% | liquidity:low; maturity:4.1y |
| C30MF | -11.67% | liquidity:low; maturity:6.6y |
| NIBLSTF | -10.81% | maturity:9.3y |
| KSY | -10.79% | liquidity:low; maturity:7.4y |
| NICBF | -10.79% | liquidity:low |
| RBBF40 | -10.41% | maturity:11.1y |
| GSY | -9.86% | maturity:8.2y |
| H8020 | -9.82% | maturity:7.0y |
| NIBLGF | -9.55% | maturity:6.3y |
| RSY | -9.52% | maturity:8.6y |
| NICFC | -9.46% | liquidity:low |
| NIBSF2 | -9.36% | maturity:4.6y |
| MNMF1 | -9.00% | maturity:8.2y |
| KEF | -8.42% | maturity:4.4y |
| SLCF | -8.37% | liquidity:low |
| NMBHF2 | -8.06% | maturity:8.4y |
| KDBY | -7.51% | maturity:5.8y |
| MBLEF | -7.40% | maturity:10.4y |
| MMF1 | -7.37% | maturity:4.9y |
| SAGF | -7.00% | maturity:7.1y |
| GBIMESY2 | -6.90% | maturity:8.8y |
| PRSF | -6.23% | maturity:5.4y |
| HLICF | -4.20% | maturity:8.9y |
| SIGS3 | -4.20% | liquidity:low; maturity:6.5y |
| NSIF2 | -4.08% | maturity:5.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 29
- NAV data age: median 30 days, max 504 days

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
