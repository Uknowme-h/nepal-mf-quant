# Nepal MF Quant — Full Analysis Report

*Generated: 2026-06-30 12:25*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-06-30 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 21 |
| Median Discount | -8.10% |
| CONSIDER | 5 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 39 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 16 | 39.0% |
| -10% to -6% | 13 | 31.7% |
| -6% to -4% | 5 | 12.2% |
| -4% to 0% | 7 | 17.1% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.39 | 9.10 | -12.42% | 3.0y | medium | 2d | -1.24% | 63.9 | ↓ widening | — |
| 2 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.05 | -4.01% | 2.9y | medium | 1d | 0.48% | 59.3 | ↑ narrowing | — |
| 3 | PSF | Prabhu Select Fund | 13.69 | 11.70 | -14.54% | 2.0y | medium | 20d | -4.60% | 59.1 | ↓ widening | — |
| 4 | SEF | Siddhartha Equity Fund | 10.65 | 10.20 | -4.23% | 1.4y | medium | 1d | -2.74% | 39.9 | ↓ widening | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.41 | 9.80 | -5.86% | 2.1y | medium | 2d | -2.16% | 34.8 | ↓ widening | high_vol |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 7 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| KDBY | -16.16% | maturity:6.1y |
| PRSF | -15.97% | maturity:5.7y |
| LUK | -14.15% | maturity:4.1y |
| SFEF | -13.39% | liquidity:low; maturity:5.6y |
| NICGF2 | -12.89% | maturity:4.4y |
| NICBF | -12.52% | liquidity:low |
| KEF | -12.41% | maturity:4.7y |
| SBCF | -11.82% | maturity:4.7y |
| RSY | -11.66% | maturity:8.8y |
| GIBF1 | -10.76% | maturity:6.1y |
| NSIF2 | -10.73% | maturity:6.2y |
| LVF2 | -10.69% | maturity:7.2y |
| SIGS3 | -10.43% | maturity:6.8y |
| H8020 | -10.13% | maturity:7.3y |
| GBIMESY2 | -9.97% | liquidity:low; maturity:9.1y |
| MBLEF | -9.54% | maturity:10.8y |
| RMF2 | -9.34% | liquidity:low; maturity:6.9y |
| KSY | -8.70% | liquidity:low; maturity:7.7y |
| RBBF40 | -8.10% | maturity:11.4y |
| NMBHF2 | -7.77% | maturity:8.7y |
| MNMF1 | -7.58% | liquidity:low; maturity:8.5y |
| C30MF | -7.43% | liquidity:low; maturity:6.9y |
| NIBSF2 | -6.79% | maturity:4.9y |
| SAGF | -6.50% | maturity:7.4y |
| SIGS2 | -6.50% | liquidity:low |
| GSY | -6.40% | maturity:8.5y |
| NIBLGF | -6.34% | maturity:6.6y |
| SFMF | -4.42% | liquidity:low |
| NIBLSTF | -4.41% | maturity:9.6y |
| NMB50 | -3.96% | valuation:small_discount; liquidity:low |
| NICSF | -3.73% | valuation:small_discount |
| CMF2 | -3.52% | valuation:small_discount |
| HLICF | -1.92% | valuation:small_discount; maturity:9.2y |
| SLCF | -1.84% | valuation:small_discount |
| NBF3 | -1.65% | valuation:small_discount; maturity:5.2y |
| MMF1 | 0.00% | valuation:premium; maturity:5.2y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 42
- NAV data age: median 46 days, max 397 days

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
