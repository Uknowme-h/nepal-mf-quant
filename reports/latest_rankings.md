# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-07 11:15*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-07 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 21 |
| Median Discount | -8.39% |
| CONSIDER | 4 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 22.5% |
| -10% to -6% | 19 | 47.5% |
| -6% to -4% | 8 | 20.0% |
| -4% to 0% | 4 | 10.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.55 | -9.56% | 2.3y | high | 5d | 5.28% | 60.4 | ↓ widening | high_vol |
| 2 | NMB50 | NMB 50 | 10.86 | 10.36 | -4.60% | 0.4y | high | 1d | 5.23% | 56.5 | ↓ widening | — |
| 3 | PSF | Prabhu Select Fund | 12.75 | 11.70 | -8.24% | 2.2y | high | 7d | 5.81% | 56.2 | ↓ widening | — |
| 4 | SEF | Siddhartha Equity Fund | 10.55 | 9.90 | -6.16% | 1.6y | medium | 5d | 4.98% | 44.0 | ↓ widening | high_vol |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -16.81% | maturity:4.4y |
| LVF2 | -15.86% | maturity:7.4y |
| SBCF | -15.43% | maturity:5.0y |
| KSY | -12.19% | maturity:8.0y |
| SFEF | -11.64% | liquidity:low; maturity:5.8y |
| NICGF2 | -11.62% | liquidity:low; maturity:4.6y |
| GIBF1 | -11.15% | maturity:6.3y |
| MBLEF | -10.99% | maturity:11.0y |
| NSIF2 | -10.98% | maturity:6.4y |
| RMF2 | -9.94% | maturity:7.1y |
| C30MF | -9.82% | maturity:7.1y |
| SIGS3 | -9.69% | maturity:7.1y |
| RSY | -9.48% | maturity:9.1y |
| GBIMESY2 | -9.42% | maturity:9.3y |
| NIBLSTF | -9.36% | maturity:9.8y |
| RBBF40 | -9.35% | liquidity:low; maturity:11.6y |
| GSY | -9.12% | maturity:8.8y |
| NMBHF2 | -8.74% | liquidity:low; maturity:8.9y |
| PRSF | -8.55% | liquidity:low; maturity:5.9y |
| MNMF1 | -7.92% | maturity:8.7y |
| SAGF | -7.66% | maturity:7.7y |
| NICSF | -7.17% | liquidity:low |
| SFMF | -7.17% | liquidity:low |
| SIGS2 | -7.01% | liquidity:low |
| SLCF | -6.60% | liquidity:low |
| MMF1 | -5.32% | maturity:5.4y |
| H8020 | -5.17% | maturity:7.5y |
| HLICF | -5.08% | maturity:9.4y |
| CMF2 | -4.80% | liquidity:low |
| KEF | -4.36% | maturity:5.0y |
| NIBSF2 | -4.29% | maturity:5.2y |
| NBF3 | -4.07% | maturity:5.5y |
| KDBY | -3.77% | valuation:small_discount; maturity:6.3y |
| NBF2 | -3.63% | valuation:small_discount |
| NIBLGF | -2.73% | valuation:small_discount; maturity:6.8y |
| NICBF | -1.24% | valuation:small_discount |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 18
- NAV data age: median 23 days, max 313 days

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
