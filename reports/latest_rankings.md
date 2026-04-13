# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-13 11:41*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-13 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 19 |
| Median Discount | -7.80% |
| CONSIDER | 6 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 8 | 19.5% |
| -10% to -6% | 20 | 48.8% |
| -6% to -4% | 7 | 17.1% |
| -4% to 0% | 4 | 9.8% |
| ≥ 0% (premium) | 2 | 4.9% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.50 | -9.70% | 3.2y | high | 9d | 4.26% | 67.3 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 12.75 | 12.18 | -4.47% | 2.2y | high | 11d | 5.81% | 61.7 | ↑ narrowing | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.67 | -8.43% | 2.3y | medium | 9d | 5.28% | 58.0 | → stable | high_vol |
| 4 | NICSF | NIC Asia Select-30 | 10.04 | 9.43 | -6.08% | 2.2y | medium | 4d | 5.35% | 54.8 | ↑ narrowing | — |
| 5 | SLCF | Sanima Large Cap Fund | 10.60 | 10.05 | -5.19% | 1.9y | medium | 4d | 4.43% | 51.5 | ↑ narrowing | — |
| 6 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.01 | -4.39% | 3.1y | high | 2d | 0.48% | 42.4 | → stable | — |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 6 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -13.81% | maturity:4.3y |
| LVF2 | -13.58% | liquidity:low; maturity:7.4y |
| SFEF | -11.64% | liquidity:low; maturity:5.8y |
| KSY | -11.63% | maturity:7.9y |
| GBIMESY2 | -10.96% | maturity:9.3y |
| SBCF | -10.93% | maturity:5.0y |
| MBLEF | -10.91% | maturity:11.0y |
| NICBF | -10.79% | liquidity:low |
| NICGF2 | -9.93% | liquidity:low; maturity:4.6y |
| NSIF2 | -9.84% | maturity:6.4y |
| NIBLSTF | -9.45% | maturity:9.8y |
| GIBF1 | -9.37% | maturity:6.3y |
| RSY | -9.30% | maturity:9.1y |
| MNMF1 | -9.21% | maturity:8.7y |
| NMBHF2 | -8.37% | maturity:8.9y |
| SIGS2 | -8.29% | liquidity:low |
| GSY | -8.11% | maturity:8.7y |
| SEF | -7.87% | liquidity:low |
| NIBSF2 | -7.80% | maturity:5.1y |
| RMF2 | -7.72% | maturity:7.1y |
| SIGS3 | -7.49% | maturity:7.0y |
| RBBF40 | -7.43% | liquidity:low; maturity:11.6y |
| NIBLGF | -7.41% | maturity:6.8y |
| C30MF | -7.36% | maturity:7.1y |
| MMF1 | -7.29% | maturity:5.4y |
| H8020 | -5.56% | maturity:7.5y |
| SAGF | -5.47% | maturity:7.6y |
| SFMF | -5.13% | liquidity:low |
| NMB50 | -4.70% | liquidity:low |
| NBF3 | -3.39% | valuation:small_discount; maturity:5.5y |
| HLICF | -2.49% | valuation:small_discount; liquidity:low; maturity:9.4y |
| PRSF | -1.93% | valuation:small_discount; maturity:5.9y |
| CMF2 | -1.88% | valuation:small_discount |
| KEF | 2.75% | valuation:premium; maturity:4.9y |
| KDBY | 4.12% | valuation:premium; maturity:6.3y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 17
- NAV data age: median 29 days, max 319 days

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
