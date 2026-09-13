# Nepal MF Quant — Full Analysis Report

*Generated: 2026-09-13 14:22*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-09-11 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 30 |
| Median Discount | -13.69% |
| CONSIDER | 6 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 30 | 76.9% |
| -10% to -6% | 6 | 15.4% |
| -6% to -4% | 0 | 0.0% |
| -4% to 0% | 3 | 7.7% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | LUK | Laxmi Unnati Kosh | 11.66 | 9.49 | -18.61% | 3.9y | medium | 1d | -1.17% | 65.5 | ↓ widening | — |
| 2 | PSF | Prabhu Select Fund | 13.09 | 10.83 | -17.27% | 1.8y | medium | 68d | 0.38% | 64.1 | ↓ widening | — |
| 3 | SEF | Siddhartha Equity Fund | 10.36 | 9.60 | -7.34% | 1.2y | high | 16d | -2.72% | 56.8 | ↑ narrowing | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.31 | 9.69 | -6.01% | 1.9y | high | 10d | -1.63% | 54.1 | ↑ narrowing | high_vol |
| 5 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.72 | -7.16% | 2.7y | medium | 1d | 0.48% | 50.1 | ↓ widening | — |
| 6 | NICSF | NIC Asia Select-30 | 9.48 | 8.20 | -13.50% | 1.8y | medium | 2d | -3.27% | 40.8 | ↓ widening | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 9 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -20.25% | maturity:7.0y |
| KEF | -18.97% | maturity:4.5y |
| SFMF | -18.58% | liquidity:low |
| NICBF | -17.93% | liquidity:low |
| SBCF | -17.72% | maturity:4.5y |
| RSY | -16.68% | maturity:8.6y |
| PRSF | -16.58% | maturity:5.5y |
| NICGF2 | -16.35% | liquidity:low; maturity:4.2y |
| SFEF | -16.10% | liquidity:low; maturity:5.4y |
| KDBY | -16.06% | maturity:5.9y |
| MBLEF | -15.74% | maturity:10.6y |
| NICFC | -15.53% | liquidity:low |
| NIBSF2 | -14.72% | liquidity:low; maturity:4.7y |
| NMBHF2 | -14.49% | maturity:8.5y |
| KSY | -14.34% | liquidity:low; maturity:7.5y |
| NIBLGF | -13.79% | maturity:6.4y |
| MNMF1 | -13.71% | maturity:8.3y |
| NSIF2 | -13.69% | maturity:6.0y |
| SIGS3 | -12.29% | maturity:6.6y |
| NIBLSTF | -11.86% | maturity:9.4y |
| SIGS2 | -11.78% | liquidity:low |
| GBIMESY2 | -11.38% | maturity:8.8y |
| SLCF | -11.24% | liquidity:low |
| SAGF | -11.15% | maturity:7.2y |
| RBBF40 | -10.63% | maturity:11.2y |
| RMF2 | -10.63% | maturity:6.7y |
| GSY | -10.14% | maturity:8.3y |
| C30MF | -7.92% | maturity:6.7y |
| NBF3 | -6.98% | maturity:5.0y |
| MMF1 | -6.38% | maturity:5.0y |
| HLICF | -3.91% | valuation:small_discount; maturity:9.0y |
| GIBF1 | -1.53% | valuation:small_discount; maturity:5.9y |
| H8020 | -1.12% | valuation:small_discount; maturity:7.1y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 31
- NAV data age: median 29 days, max 472 days

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
