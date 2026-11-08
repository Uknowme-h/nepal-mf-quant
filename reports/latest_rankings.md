# Nepal MF Quant — Full Analysis Report

*Generated: 2026-11-08 16:41*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-11-06 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 21 |
| Median Discount | -8.65% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 13 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 10 | 25.6% |
| -10% to -6% | 19 | 48.7% |
| -6% to -4% | 7 | 17.9% |
| -4% to 0% | 2 | 5.1% |
| ≥ 0% (premium) | 1 | 2.6% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 12.40 | 11.80 | -4.84% | 1.6y | high | 0d | 3.33% | 67.3 | ↑ narrowing | — |
| 2 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.12 | -12.89% | 2.6y | medium | 7d | 0.48% | 65.8 | ↓ widening | — |
| 3 | SEF | Siddhartha Equity Fund | 10.78 | 10.00 | -7.24% | 1.0y | medium | 16d | 2.76% | 60.8 | ↑ narrowing | — |
| 4 | SIGS2 | Siddhartha Investment Gro | 10.65 | 9.70 | -8.92% | 2.8y | medium | 2d | 3.30% | 59.5 | ↓ widening | — |
| 5 | NICSF | NIC Asia Select-30 | 9.50 | 8.91 | -6.21% | 1.7y | medium | 25d | 2.37% | 58.2 | ↑ narrowing | high_vol |
| 6 | NICFC | NIC Asia Flexi Cap Fund | 9.94 | 9.35 | -5.94% | 2.6y | high | 3d | -1.29% | 54.0 | ↑ narrowing | — |
| 7 | SLCF | Sanima Large Cap Fund | 10.10 | 9.15 | -9.41% | 1.3y | medium | 2d | 0.60% | 52.0 | ↓ widening | — |
| 8 | RMF1 | RBB Mutual Fund 1 | 10.21 | 9.10 | -10.87% | 1.7y | medium | 23d | -0.10% | 50.5 | ↓ widening | high_vol |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 8 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -20.21% | maturity:5.3y |
| LUK | -17.67% | liquidity:low |
| LVF2 | -17.62% | maturity:6.8y |
| SBCF | -17.11% | liquidity:low; maturity:4.4y |
| SFMF | -12.39% | liquidity:low |
| NBF3 | -12.02% | maturity:4.9y |
| NIBSF2 | -10.36% | maturity:4.6y |
| MBLEF | -10.18% | liquidity:low; maturity:10.4y |
| NIBLSTF | -9.92% | maturity:9.3y |
| KSY | -9.22% | maturity:7.4y |
| GSY | -9.14% | maturity:8.2y |
| C30MF | -9.09% | liquidity:low; maturity:6.5y |
| NMBHF2 | -8.82% | maturity:8.3y |
| NICGF2 | -8.81% | maturity:4.0y |
| NIBLGF | -8.66% | maturity:6.2y |
| RSY | -8.65% | maturity:8.5y |
| MNMF1 | -8.51% | maturity:8.1y |
| NICBF | -7.99% | liquidity:low |
| RBBF40 | -7.87% | maturity:11.0y |
| RMF2 | -7.78% | maturity:6.5y |
| MMF1 | -7.70% | maturity:4.8y |
| GBIMESY2 | -7.08% | maturity:8.7y |
| KDBY | -6.98% | maturity:5.7y |
| KEF | -5.77% | liquidity:low; maturity:4.4y |
| NSIF2 | -5.77% | maturity:5.8y |
| SAGF | -5.30% | maturity:7.1y |
| GIBF1 | -4.96% | liquidity:low; maturity:5.7y |
| PRSF | -4.69% | maturity:5.4y |
| SIGS3 | -2.73% | valuation:small_discount; maturity:6.5y |
| HLICF | -0.35% | valuation:small_discount; maturity:8.9y |
| H8020 | 2.88% | valuation:premium; maturity:6.9y |

</details>

## Data Quality

- Symbols checked: 49
- Symbols with issues: 33
- NAV data age: median 24 days, max 528 days

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
