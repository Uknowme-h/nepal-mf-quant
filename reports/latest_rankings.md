# Nepal MF Quant — Full Analysis Report

*Generated: 2026-10-31 15:45*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-10-30 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 16 |
| Median Discount | -7.00% |
| CONSIDER | 9 |
| IGNORE | 30 |

> ⚠️ **NAV Staleness Warning**: 38 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 23.1% |
| -10% to -6% | 17 | 43.6% |
| -6% to -4% | 8 | 20.5% |
| -4% to 0% | 5 | 12.8% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.90 | -12.39% | 3.0y | medium | 4d | -2.04% | 80.4 | ↑ narrowing | — |
| 2 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.23 | -11.84% | 2.6y | high | 3d | 0.48% | 80.4 | ↑ narrowing | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 9.94 | 9.25 | -6.94% | 2.6y | high | 5d | -1.29% | 67.7 | ↑ narrowing | — |
| 4 | NICBF | NIC ASIA Balanced Fund | 10.01 | 9.26 | -7.49% | 2.8y | medium | 1d | -0.99% | 61.8 | ↑ narrowing | — |
| 5 | SEF | Siddhartha Equity Fund | 10.49 | 9.95 | -5.15% | 1.0y | high | 12d | 1.06% | 58.2 | ↑ narrowing | — |
| 6 | RMF1 | RBB Mutual Fund 1 | 10.22 | 9.20 | -9.98% | 1.7y | medium | 19d | -0.87% | 56.1 | ↓ widening | high_vol |
| 7 | PSF | Prabhu Select Fund | 12.00 | 11.49 | -4.25% | 1.6y | high | 11d | -8.33% | 51.9 | ↑ narrowing | — |
| 8 | NICSF | NIC Asia Select-30 | 9.28 | 8.82 | -4.96% | 1.7y | medium | 21d | -2.11% | 50.5 | ↑ narrowing | high_vol |
| 9 | SIGS2 | Siddhartha Investment Gro | 10.31 | 9.66 | -6.30% | 2.8y | medium | 1d | -5.84% | 48.5 | ↑ narrowing | — |

## IGNORE Summary

*30 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 5 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -19.37% | liquidity:low; maturity:6.8y |
| SFEF | -19.34% | liquidity:low; maturity:5.3y |
| SBCF | -16.93% | maturity:4.4y |
| LUK | -15.52% | liquidity:low |
| GIBF1 | -13.12% | liquidity:low; maturity:5.8y |
| RMF2 | -10.45% | liquidity:low; maturity:6.6y |
| NBF3 | -10.37% | maturity:4.9y |
| H8020 | -9.82% | maturity:6.9y |
| RSY | -8.46% | maturity:8.5y |
| NIBSF2 | -8.44% | maturity:4.6y |
| RBBF40 | -8.21% | maturity:11.0y |
| C30MF | -8.04% | liquidity:low; maturity:6.5y |
| MNMF1 | -8.01% | maturity:8.1y |
| NICGF2 | -7.70% | maturity:4.1y |
| MBLEF | -7.10% | liquidity:low; maturity:10.4y |
| GSY | -7.00% | maturity:8.2y |
| GBIMESY2 | -6.90% | maturity:8.7y |
| NIBLSTF | -6.57% | maturity:9.3y |
| KSY | -6.35% | maturity:7.4y |
| SAGF | -6.20% | liquidity:low; maturity:7.1y |
| KDBY | -5.88% | maturity:5.7y |
| MMF1 | -5.68% | maturity:4.9y |
| NIBLGF | -5.59% | maturity:6.2y |
| NMBHF2 | -5.34% | maturity:8.3y |
| KEF | -5.00% | maturity:4.4y |
| PRSF | -3.69% | valuation:small_discount; maturity:5.4y |
| SLCF | -3.59% | valuation:small_discount; liquidity:low |
| NSIF2 | -2.75% | valuation:small_discount; maturity:5.8y |
| SIGS3 | -2.05% | valuation:small_discount; liquidity:low; maturity:6.5y |
| HLICF | -1.87% | valuation:small_discount; maturity:8.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 41
- NAV data age: median 46 days, max 520 days

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
