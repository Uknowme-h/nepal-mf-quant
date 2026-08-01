# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-01 11:35*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-31 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 21 |
| Median Discount | -8.54% |
| CONSIDER | 7 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 33 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 15 | 37.5% |
| -10% to -6% | 15 | 37.5% |
| -6% to -4% | 5 | 12.5% |
| -4% to 0% | 5 | 12.5% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.15 | -10.18% | 3.3y | high | 1d | -2.04% | 70.9 | ↑ narrowing | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.10 | -11.65% | 2.9y | medium | 11d | 0.88% | 63.0 | ↓ widening | — |
| 3 | NICBF | NIC ASIA Balanced Fund | 10.32 | 9.50 | -7.95% | 3.1y | medium | 1d | 0.88% | 61.0 | ↑ narrowing | high_vol |
| 4 | PSF | Prabhu Select Fund | 13.69 | 11.74 | -14.24% | 1.9y | medium | 42d | -4.60% | 55.6 | ↓ widening | — |
| 5 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.78 | -6.41% | 2.0y | high | 11d | 0.38% | 55.4 | ↑ narrowing | high_vol |
| 6 | NICSF | NIC Asia Select-30 | 9.80 | 9.00 | -8.16% | 1.9y | medium | 6d | 1.45% | 55.1 | ↓ widening | — |
| 7 | SEF | Siddhartha Equity Fund | 10.36 | 9.80 | -5.41% | 1.3y | high | 4d | -2.72% | 44.5 | → stable | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 5 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -15.34% | maturity:4.7y |
| KEF | -13.81% | maturity:4.6y |
| LVF2 | -13.58% | maturity:7.1y |
| KDBY | -13.21% | maturity:6.0y |
| NICGF2 | -13.08% | liquidity:low; maturity:4.3y |
| PRSF | -12.87% | maturity:5.6y |
| LUK | -12.52% | maturity:4.0y |
| SFEF | -12.51% | liquidity:low; maturity:5.5y |
| NIBLSTF | -12.04% | maturity:9.5y |
| NIBSF2 | -11.38% | maturity:4.8y |
| RBBF40 | -11.03% | maturity:11.3y |
| NSIF2 | -10.65% | liquidity:low; maturity:6.1y |
| MNMF1 | -9.60% | maturity:8.4y |
| RSY | -9.25% | maturity:8.8y |
| NMBHF2 | -9.19% | maturity:8.6y |
| RMF2 | -8.95% | liquidity:low; maturity:6.8y |
| SIGS3 | -8.92% | maturity:6.8y |
| GIBF1 | -7.81% | maturity:6.0y |
| KSY | -7.38% | maturity:7.6y |
| SAGF | -7.12% | liquidity:low; maturity:7.3y |
| MBLEF | -6.91% | liquidity:low; maturity:10.7y |
| GBIMESY2 | -6.85% | maturity:9.0y |
| C30MF | -6.85% | liquidity:low; maturity:6.8y |
| MMF1 | -6.44% | maturity:5.1y |
| H8020 | -5.98% | maturity:7.2y |
| NBF2 | -5.44% | liquidity:low |
| SLCF | -4.54% | liquidity:low |
| NBF3 | -4.26% | maturity:5.2y |
| NIBLGF | -3.81% | valuation:small_discount; maturity:6.5y |
| SIGS2 | -3.23% | valuation:small_discount; liquidity:low |
| GSY | -3.11% | valuation:small_discount; maturity:8.4y |
| HLICF | -2.06% | valuation:small_discount; maturity:9.1y |
| NMB50 | -1.98% | valuation:small_discount |

</details>

## Data Quality

- Symbols checked: 44
- Symbols with issues: 41
- NAV data age: median 47 days, max 429 days

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
