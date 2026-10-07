# Nepal MF Quant — Full Analysis Report

*Generated: 2026-10-07 17:27*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-10-07 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 32 |
| Median Discount | -9.96% |
| CONSIDER | 7 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 12 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 19 | 48.7% |
| -10% to -6% | 18 | 46.2% |
| -6% to -4% | 1 | 2.6% |
| -4% to 0% | 1 | 2.6% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | RMF1 | RBB Mutual Fund 1 | 10.22 | 9.30 | -9.00% | 1.8y | high | 8d | -0.87% | 58.3 | ↑ narrowing | high_vol |
| 2 | SEF | Siddhartha Equity Fund | 10.49 | 9.50 | -9.44% | 1.1y | medium | 1d | 1.06% | 54.5 | ↓ widening | — |
| 3 | NICBF | NIC ASIA Balanced Fund | 10.01 | 9.26 | -7.49% | 2.9y | high | 1d | -0.99% | 52.3 | ↑ narrowing | — |
| 4 | SLCF | Sanima Large Cap Fund | 10.04 | 9.20 | -8.37% | 1.4y | medium | 5d | -0.99% | 51.1 | ↑ narrowing | — |
| 5 | NICFC | NIC Asia Flexi Cap Fund | 9.94 | 8.83 | -11.17% | 2.7y | medium | 1d | -1.29% | 48.9 | ↓ widening | — |
| 6 | NICSF | NIC Asia Select-30 | 9.28 | 8.40 | -9.48% | 1.8y | high | 10d | -2.11% | 48.7 | ↓ widening | high_vol |
| 7 | SIGS2 | Siddhartha Investment Gro | 10.31 | 9.57 | -7.18% | 2.9y | medium | 1d | -5.84% | 43.6 | → stable | — |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 9 |
| valuation | 1 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -22.31% | maturity:5.3y |
| LVF2 | -21.12% | liquidity:low; maturity:6.9y |
| LUK | -20.24% | liquidity:low |
| SFMF | -19.91% | liquidity:low |
| SBCF | -17.55% | maturity:4.5y |
| NSIF2 | -13.86% | maturity:5.9y |
| NMBHF2 | -13.82% | maturity:8.4y |
| NBF3 | -13.47% | maturity:5.0y |
| SAGF | -12.85% | maturity:7.2y |
| MMF1 | -12.32% | maturity:4.9y |
| NIBLGF | -11.79% | liquidity:low; maturity:6.3y |
| NICGF2 | -11.55% | maturity:4.1y |
| GIBF1 | -11.41% | maturity:5.8y |
| RSY | -11.06% | maturity:8.6y |
| NIBSF2 | -10.91% | maturity:4.6y |
| NBF2 | -10.41% | liquidity:low |
| KSY | -10.28% | liquidity:low; maturity:7.5y |
| GBIMESY2 | -10.00% | maturity:8.8y |
| NIBLSTF | -9.96% | maturity:9.3y |
| GSY | -9.86% | maturity:8.2y |
| MBLEF | -9.66% | maturity:10.5y |
| RMF2 | -9.44% | liquidity:low; maturity:6.6y |
| KDBY | -9.41% | maturity:5.8y |
| PSF | -9.17% | liquidity:low |
| C30MF | -9.09% | maturity:6.6y |
| H8020 | -9.02% | maturity:7.0y |
| MNMF1 | -9.00% | maturity:8.2y |
| KEF | -7.93% | maturity:4.5y |
| PRSF | -7.92% | maturity:5.4y |
| RBBF40 | -7.11% | maturity:11.1y |
| SIGS3 | -4.76% | liquidity:low; maturity:6.6y |
| HLICF | -3.73% | valuation:small_discount; maturity:8.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 30
- NAV data age: median 22 days, max 496 days

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
