# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-17 14:59*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-17 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 37 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 31 |
| Median Discount | -11.86% |
| CONSIDER | 7 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 29 | 74.4% |
| -10% to -6% | 7 | 17.9% |
| -6% to -4% | 0 | 0.0% |
| -4% to 0% | 1 | 2.6% |
| ≥ 0% (premium) | 2 | 5.1% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 13.09 | 10.98 | -16.12% | 1.8y | high | 72d | 0.38% | 73.8 | ↑ narrowing | — |
| 2 | LUK | Laxmi Unnati Kosh | 11.66 | 9.35 | -19.81% | 3.9y | medium | 1d | -1.17% | 58.7 | ↓ widening | — |
| 3 | SIGS2 | Siddhartha Investment Gro | 10.95 | 9.62 | -12.15% | 2.9y | high | 4d | -3.30% | 57.7 | → stable | — |
| 4 | NICSF | NIC Asia Select-30 | 9.48 | 8.68 | -8.44% | 1.8y | medium | 2d | -3.27% | 53.2 | ↑ narrowing | — |
| 5 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.30 | -11.17% | 2.7y | medium | 5d | 0.48% | 52.6 | ↓ widening | — |
| 6 | SEF | Siddhartha Equity Fund | 10.36 | 9.67 | -6.66% | 1.1y | high | 20d | -2.72% | 48.3 | ↑ narrowing | — |
| 7 | RMF1 | RBB Mutual Fund 1 | 10.31 | 9.50 | -7.86% | 1.9y | medium | 14d | -1.63% | 41.5 | ↑ narrowing | high_vol |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -20.60% | liquidity:low; maturity:7.0y |
| SFEF | -20.38% | maturity:5.4y |
| SFMF | -18.58% | liquidity:low |
| SBCF | -17.99% | maturity:4.5y |
| NICGF2 | -17.69% | maturity:4.2y |
| KEF | -16.30% | maturity:4.5y |
| KDBY | -15.81% | maturity:5.9y |
| MBLEF | -15.74% | liquidity:low; maturity:10.5y |
| RSY | -15.53% | maturity:8.6y |
| PRSF | -15.29% | maturity:5.5y |
| NMBHF2 | -15.07% | maturity:8.4y |
| NICFC | -14.56% | liquidity:low |
| NIBSF2 | -12.59% | maturity:4.7y |
| MNMF1 | -12.56% | maturity:8.3y |
| KSY | -12.50% | maturity:7.5y |
| NSIF2 | -12.23% | maturity:6.0y |
| NIBLSTF | -11.86% | maturity:9.4y |
| RBBF40 | -11.62% | maturity:11.2y |
| NIBLGF | -11.46% | maturity:6.3y |
| SIGS3 | -11.34% | liquidity:low; maturity:6.6y |
| NICBF | -11.24% | liquidity:low |
| RMF2 | -10.63% | liquidity:low; maturity:6.7y |
| GSY | -10.54% | maturity:8.3y |
| GBIMESY2 | -10.37% | maturity:8.8y |
| SAGF | -10.21% | maturity:7.2y |
| SLCF | -9.27% | liquidity:low |
| C30MF | -6.98% | liquidity:low; maturity:6.7y |
| MMF1 | -6.17% | maturity:5.0y |
| NBF3 | -6.01% | maturity:5.0y |
| HLICF | -3.34% | valuation:small_discount; liquidity:low; maturity:9.0y |
| H8020 | 0.08% | valuation:premium; maturity:7.0y |
| GIBF1 | 0.42% | valuation:premium; maturity:5.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 28
- NAV data age: median 33 days, max 476 days

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
