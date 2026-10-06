# Nepal MF Quant — Full Analysis Report

*Generated: 2026-10-06 16:52*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-10-06 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 32 |
| Median Discount | -10.03% |
| CONSIDER | 6 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 21 | 53.8% |
| -10% to -6% | 15 | 38.5% |
| -6% to -4% | 1 | 2.6% |
| -4% to 0% | 2 | 5.1% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.05 | -19.91% | 3.1y | high | 6d | -2.04% | 74.5 | → stable | — |
| 2 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.11 | -12.99% | 2.6y | medium | 2d | 0.48% | 69.9 | ↓ widening | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.22 | 9.00 | -11.94% | 1.8y | medium | 7d | -0.87% | 57.4 | ↓ widening | high_vol |
| 4 | SLCF | Sanima Large Cap Fund | 10.04 | 9.38 | -6.57% | 1.4y | medium | 4d | -0.99% | 54.5 | ↑ narrowing | — |
| 5 | NICSF | NIC Asia Select-30 | 9.28 | 8.35 | -10.02% | 1.8y | medium | 9d | -2.11% | 53.3 | ↑ narrowing | high_vol |
| 6 | PSF | Prabhu Select Fund | 12.00 | 10.90 | -9.17% | 1.7y | medium | 82d | -8.33% | 47.3 | → stable | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 2 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -21.26% | maturity:5.4y |
| LVF2 | -21.12% | liquidity:low; maturity:6.9y |
| LUK | -18.87% | liquidity:low |
| SBCF | -17.11% | maturity:4.5y |
| NSIF2 | -16.17% | maturity:5.9y |
| NMBHF2 | -13.53% | maturity:8.4y |
| SAGF | -13.04% | maturity:7.2y |
| NBF3 | -12.79% | maturity:5.0y |
| GIBF1 | -12.69% | maturity:5.8y |
| NIBLGF | -12.60% | maturity:6.3y |
| NICBF | -12.59% | liquidity:low |
| H8020 | -11.41% | maturity:7.0y |
| NIBLSTF | -11.23% | maturity:9.3y |
| NIBSF2 | -10.70% | liquidity:low; maturity:4.7y |
| RBBF40 | -10.31% | maturity:11.1y |
| GSY | -10.06% | maturity:8.2y |
| NICGF2 | -10.03% | maturity:4.1y |
| MNMF1 | -9.99% | maturity:8.2y |
| KSY | -9.98% | liquidity:low; maturity:7.5y |
| NICFC | -9.96% | liquidity:low |
| RSY | -9.81% | liquidity:low; maturity:8.6y |
| SIGS2 | -9.80% | liquidity:low |
| RMF2 | -9.44% | maturity:6.6y |
| KDBY | -9.05% | maturity:5.8y |
| KEF | -8.91% | maturity:4.5y |
| MBLEF | -8.48% | liquidity:low; maturity:10.5y |
| MMF1 | -8.32% | maturity:4.9y |
| PRSF | -7.84% | maturity:5.4y |
| SEF | -7.53% | liquidity:low |
| C30MF | -6.60% | maturity:6.6y |
| GBIMESY2 | -5.00% | maturity:8.8y |
| SIGS3 | -3.54% | valuation:small_discount; maturity:6.6y |
| HLICF | -1.98% | valuation:small_discount; maturity:8.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 30
- NAV data age: median 21 days, max 495 days

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
