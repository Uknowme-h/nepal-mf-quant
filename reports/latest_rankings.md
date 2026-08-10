# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-10 11:21*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-10 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 19 |
| Median Discount | -7.41% |
| CONSIDER | 6 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 22.5% |
| -10% to -6% | 16 | 40.0% |
| -6% to -4% | 11 | 27.5% |
| -4% to 0% | 4 | 10.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.20 | -10.68% | 2.9y | medium | 3d | 0.88% | 74.2 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 13.04 | 11.90 | -8.74% | 1.9y | medium | 47d | -4.26% | 64.4 | ↑ narrowing | — |
| 3 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.86 | -5.83% | 2.8y | medium | 1d | 0.48% | 58.4 | → stable | — |
| 4 | NICSF | NIC Asia Select-30 | 9.55 | 8.64 | -9.53% | 1.9y | high | 2d | -2.55% | 56.4 | ↓ widening | — |
| 5 | SEF | Siddhartha Equity Fund | 10.36 | 9.90 | -4.44% | 1.2y | medium | 9d | -2.72% | 50.1 | ↑ narrowing | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.28 | 9.70 | -5.64% | 1.9y | medium | 16d | -1.63% | 42.9 | ↓ widening | high_vol |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -20.25% | maturity:7.1y |
| SBCF | -17.11% | maturity:4.6y |
| LUK | -13.72% | maturity:4.0y |
| SFEF | -13.30% | liquidity:low; maturity:5.5y |
| SFMF | -11.42% | liquidity:low |
| NICGF2 | -11.25% | maturity:4.3y |
| RMF2 | -10.41% | maturity:6.8y |
| KDBY | -10.28% | maturity:6.0y |
| NICBF | -9.88% | liquidity:low |
| NIBLGF | -9.84% | liquidity:low; maturity:6.4y |
| NIBLSTF | -9.63% | maturity:9.5y |
| NIBSF2 | -9.03% | maturity:4.8y |
| NMBHF2 | -8.97% | maturity:8.6y |
| PRSF | -8.41% | maturity:5.6y |
| RBBF40 | -8.34% | maturity:11.3y |
| NSIF2 | -8.23% | maturity:6.1y |
| KSY | -7.97% | maturity:7.6y |
| GBIMESY2 | -6.85% | maturity:8.9y |
| RSY | -6.81% | maturity:8.7y |
| GIBF1 | -6.62% | maturity:6.0y |
| NBF3 | -6.49% | maturity:5.1y |
| MNMF1 | -6.46% | maturity:8.4y |
| C30MF | -5.89% | liquidity:low; maturity:6.8y |
| SLCF | -5.75% | liquidity:low |
| KEF | -5.59% | maturity:4.6y |
| MMF1 | -5.27% | maturity:5.1y |
| MBLEF | -5.25% | maturity:10.6y |
| SIGS3 | -4.81% | maturity:6.7y |
| GSY | -4.52% | maturity:8.4y |
| SAGF | -4.08% | liquidity:low; maturity:7.3y |
| H8020 | -2.91% | valuation:small_discount; liquidity:low; maturity:7.2y |
| SIGS2 | -0.46% | valuation:small_discount; liquidity:low |
| NMB50 | -0.38% | valuation:small_discount; liquidity:low |
| HLICF | -0.11% | valuation:small_discount; maturity:9.1y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 27
- NAV data age: median 7 days, max 438 days

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
