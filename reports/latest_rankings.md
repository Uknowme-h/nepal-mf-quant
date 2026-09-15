# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-15 15:00*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-15 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 32 |
| Median Discount | -12.28% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 28 | 71.8% |
| -10% to -6% | 6 | 15.4% |
| -6% to -4% | 3 | 7.7% |
| -4% to 0% | 2 | 5.1% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICBF | NIC ASIA Balanced Fund | 10.32 | 8.95 | -13.28% | 3.0y | medium | 1d | 0.88% | 67.6 | ↑ narrowing | — |
| 2 | LUK | Laxmi Unnati Kosh | 11.66 | 9.50 | -18.52% | 3.9y | medium | 3d | -1.17% | 66.2 | → stable | — |
| 3 | PSF | Prabhu Select Fund | 13.09 | 11.16 | -14.74% | 1.8y | high | 70d | 0.38% | 63.0 | ↓ widening | — |
| 4 | SEF | Siddhartha Equity Fund | 10.36 | 9.78 | -5.60% | 1.1y | high | 18d | -2.72% | 56.3 | ↑ narrowing | — |
| 5 | SLCF | Sanima Large Cap Fund | 10.14 | 9.20 | -9.27% | 1.4y | medium | 2d | -2.12% | 51.0 | ↑ narrowing | — |
| 6 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.83 | -6.11% | 2.7y | medium | 3d | 0.48% | 49.4 | → stable | — |
| 7 | SIGS2 | Siddhartha Investment Gro | 10.95 | 9.54 | -12.88% | 3.0y | medium | 2d | -3.30% | 48.2 | ↓ widening | — |
| 8 | RMF1 | RBB Mutual Fund 1 | 10.31 | 9.45 | -8.34% | 1.9y | medium | 12d | -1.63% | 37.0 | ↓ widening | high_vol |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 2 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFMF | -18.58% | liquidity:low |
| LVF2 | -18.14% | maturity:7.0y |
| RSY | -17.92% | maturity:8.6y |
| NICGF2 | -17.79% | liquidity:low; maturity:4.2y |
| SFEF | -17.76% | maturity:5.4y |
| SBCF | -17.72% | liquidity:low; maturity:4.5y |
| NICFC | -15.44% | liquidity:low |
| KEF | -15.41% | maturity:4.5y |
| KDBY | -15.22% | maturity:5.9y |
| NSIF2 | -14.88% | maturity:6.0y |
| MBLEF | -14.73% | maturity:10.5y |
| PRSF | -14.29% | maturity:5.5y |
| KSY | -14.24% | liquidity:low; maturity:7.5y |
| NIBLGF | -12.78% | maturity:6.3y |
| MNMF1 | -12.66% | maturity:8.3y |
| NIBLSTF | -12.28% | liquidity:low; maturity:9.4y |
| NIBSF2 | -12.08% | maturity:4.7y |
| NMBHF2 | -11.90% | maturity:8.5y |
| SAGF | -11.34% | maturity:7.2y |
| GBIMESY2 | -10.88% | liquidity:low; maturity:8.8y |
| NBF3 | -10.56% | maturity:5.0y |
| RMF2 | -10.54% | liquidity:low; maturity:6.7y |
| NICSF | -10.34% | liquidity:low |
| SIGS3 | -10.13% | maturity:6.6y |
| RBBF40 | -9.53% | liquidity:low; maturity:11.2y |
| GSY | -8.13% | maturity:8.3y |
| MMF1 | -7.01% | maturity:5.0y |
| HLICF | -4.95% | maturity:9.0y |
| C30MF | -4.25% | maturity:6.7y |
| H8020 | -1.67% | valuation:small_discount; maturity:7.0y |
| GIBF1 | -1.53% | valuation:small_discount; maturity:5.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 23
- NAV data age: median 31 days, max 474 days

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
