# Nepal MF Quant — Full Analysis Report

*Generated: 2026-03-02 11:03*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-03-01 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 19 |
| Median Discount | -7.65% |
| CONSIDER | 4 |
| IGNORE | 37 |

> ⚠️ **NAV Staleness Warning**: 14 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 5 | 12.2% |
| -10% to -6% | 22 | 53.7% |
| -6% to -4% | 8 | 19.5% |
| -4% to 0% | 6 | 14.6% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NBF2 | Nabil Balanced Fund - 2 | 10.42 | 9.53 | -8.54% | 3.2y | high | 4d | 2.26% | 64.2 | ↓ widening | — |
| 2 | PSF | Prabhu Select Fund | 12.03 | 10.87 | -9.64% | 2.3y | medium | 7d | 3.35% | 63.7 | ↓ widening | — |
| 3 | SIGS2 | Siddhartha Investment Gro | 10.44 | 9.58 | -8.24% | 3.5y | medium | 3d | 0.29% | 55.5 | ↓ widening | — |
| 4 | SEF | Siddhartha Equity Fund | 10.05 | 9.60 | -4.48% | 1.7y | medium | 3d | 0.30% | 54.4 | ↑ narrowing | — |

## IGNORE Summary

*37 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 6 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -16.67% | maturity:5.1y |
| LUK | -15.95% | maturity:4.5y |
| LVF2 | -15.86% | maturity:7.5y |
| SFEF | -14.70% | maturity:6.0y |
| SFMF | -10.97% | liquidity:low |
| GIBF1 | -9.76% | liquidity:low; maturity:6.4y |
| KDBY | -9.33% | maturity:6.4y |
| KEF | -8.93% | maturity:5.0y |
| PRSF | -8.79% | liquidity:low; maturity:6.0y |
| NMBHF2 | -8.78% | maturity:9.0y |
| GSY | -8.58% | maturity:8.8y |
| RMF2 | -8.40% | liquidity:low; maturity:7.2y |
| KSY | -8.38% | maturity:8.1y |
| MBLEF | -8.14% | maturity:11.1y |
| RSY | -8.08% | maturity:9.2y |
| NSIF2 | -8.08% | maturity:6.5y |
| GBIMESY2 | -7.77% | maturity:9.4y |
| NBF3 | -7.65% | maturity:5.6y |
| C30MF | -7.36% | maturity:7.2y |
| NICGF2 | -7.30% | maturity:4.7y |
| MNMF1 | -6.74% | maturity:8.8y |
| SLCF | -6.40% | liquidity:low |
| NIBSF2 | -6.11% | maturity:5.2y |
| NICBF | -6.08% | liquidity:low |
| NICFC | -5.79% | liquidity:low |
| SAGF | -5.53% | maturity:7.8y |
| NIBLSTF | -5.02% | maturity:9.9y |
| HLICF | -4.92% | liquidity:low; maturity:9.6y |
| SIGS3 | -4.54% | maturity:7.2y |
| RBBF40 | -4.24% | liquidity:low; maturity:11.7y |
| H8020 | -4.13% | maturity:7.6y |
| NICSF | -3.67% | valuation:small_discount |
| MMF1 | -3.44% | valuation:small_discount; maturity:5.5y |
| RMF1 | -2.79% | valuation:small_discount |
| NMB50 | -1.84% | valuation:small_discount |
| NIBLGF | -0.82% | valuation:small_discount; maturity:6.9y |
| CMF2 | -0.49% | valuation:small_discount; liquidity:low |

</details>

## Data Quality

- Symbols checked: 41
- Symbols with issues: 21
- NAV data age: median 15 days, max 277 days

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
