# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-30 16:25*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-30 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 36 |
| Median Discount | -12.80% |
| CONSIDER | 9 |
| IGNORE | 30 |

> ⚠️ **NAV Staleness Warning**: 36 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 30 | 76.9% |
| -10% to -6% | 7 | 17.9% |
| -6% to -4% | 2 | 5.1% |
| -4% to 0% | 0 | 0.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICBF | NIC ASIA Balanced Fund | 10.32 | 9.00 | -12.79% | 2.9y | high | 1d | 0.88% | 67.7 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 13.09 | 10.82 | -17.34% | 1.7y | medium | 79d | 0.38% | 67.2 | ↓ widening | — |
| 3 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.10 | -19.47% | 3.1y | medium | 3d | -2.04% | 66.8 | ↓ widening | — |
| 4 | SIGS2 | Siddhartha Investment Gro | 10.95 | 9.65 | -11.87% | 2.9y | medium | 2d | -3.30% | 62.6 | ↑ narrowing | — |
| 5 | LUK | Laxmi Unnati Kosh | 11.66 | 9.30 | -20.24% | 3.9y | medium | 1d | -1.17% | 59.6 | ↓ widening | — |
| 6 | SLCF | Sanima Large Cap Fund | 10.14 | 9.27 | -8.58% | 1.4y | medium | 1d | -2.12% | 50.4 | ↑ narrowing | — |
| 7 | SEF | Siddhartha Equity Fund | 10.36 | 9.75 | -5.89% | 1.1y | high | 27d | -2.72% | 49.1 | → stable | — |
| 8 | NICSF | NIC Asia Select-30 | 9.48 | 8.32 | -12.24% | 1.8y | medium | 6d | -3.27% | 44.2 | ↓ widening | high_vol |
| 9 | RMF1 | RBB Mutual Fund 1 | 10.31 | 8.99 | -12.80% | 1.8y | medium | 4d | -1.63% | 43.1 | ↓ widening | high_vol |

## IGNORE Summary

*30 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -21.96% | maturity:5.4y |
| LVF2 | -19.81% | liquidity:low; maturity:6.9y |
| SBCF | -18.25% | maturity:4.5y |
| KEF | -17.81% | liquidity:low; maturity:4.5y |
| KDBY | -17.22% | maturity:5.8y |
| MBLEF | -17.02% | maturity:10.5y |
| RSY | -16.59% | liquidity:low; maturity:8.6y |
| RMF2 | -15.77% | maturity:6.6y |
| PRSF | -14.72% | maturity:5.5y |
| GIBF1 | -13.75% | maturity:5.8y |
| NSIF2 | -13.69% | maturity:5.9y |
| NICGF2 | -13.56% | maturity:4.1y |
| NMBHF2 | -13.53% | maturity:8.4y |
| NICFC | -13.30% | liquidity:low |
| C30MF | -13.02% | maturity:6.6y |
| NIBSF2 | -12.99% | maturity:4.7y |
| H8020 | -12.76% | maturity:7.0y |
| MNMF1 | -11.89% | liquidity:low; maturity:8.2y |
| NIBLGF | -11.66% | maturity:6.3y |
| RBBF40 | -11.52% | liquidity:low; maturity:11.1y |
| NBF3 | -11.24% | maturity:5.0y |
| SAGF | -11.06% | liquidity:low; maturity:7.2y |
| SIGS3 | -10.56% | maturity:6.6y |
| GSY | -9.64% | maturity:8.3y |
| NBF2 | -9.46% | liquidity:low |
| NIBLSTF | -9.44% | maturity:9.4y |
| KSY | -9.27% | liquidity:low; maturity:7.5y |
| MMF1 | -8.47% | maturity:4.9y |
| GBIMESY2 | -7.96% | maturity:8.8y |
| HLICF | -4.14% | liquidity:low; maturity:9.0y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 42
- NAV data age: median 46 days, max 489 days

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
