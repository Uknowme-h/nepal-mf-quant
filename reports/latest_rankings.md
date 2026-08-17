# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-17 10:48*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-17 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 2 |
| Deep Discount (≤ -8%) | 18 |
| Median Discount | -6.98% |
| CONSIDER | 6 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 22.5% |
| -10% to -6% | 15 | 37.5% |
| -6% to -4% | 8 | 20.0% |
| -4% to 0% | 6 | 15.0% |
| ≥ 0% (premium) | 2 | 5.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | LUK | Laxmi Unnati Kosh | 11.66 | 10.60 | -9.09% | 4.0y | medium | 2d | -1.17% | 72.2 | ↑ narrowing | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.00 | -11.50% | 3.2y | medium | 1d | -2.04% | 71.6 | → stable | — |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.10 | -11.65% | 2.8y | medium | 8d | 0.88% | 65.9 | ↓ widening | — |
| 4 | PSF | Prabhu Select Fund | 13.04 | 12.05 | -7.59% | 1.9y | medium | 52d | -4.26% | 59.8 | ↑ narrowing | — |
| 5 | NICSF | NIC Asia Select-30 | 9.55 | 8.73 | -8.59% | 1.9y | medium | 4d | -2.55% | 56.4 | ↑ narrowing | — |
| 6 | NMB50 | NMB 50 | 10.45 | 10.00 | -4.31% | 0.0y | high | 1d | -1.42% | 52.8 | ↓ widening | — |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 9 |
| valuation | 8 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -17.53% | liquidity:low; maturity:7.0y |
| SFEF | -13.82% | liquidity:low; maturity:5.5y |
| NICGF2 | -11.35% | liquidity:low; maturity:4.3y |
| NIBLSTF | -10.79% | maturity:9.5y |
| NICBF | -10.76% | liquidity:low |
| SBCF | -10.49% | maturity:4.6y |
| KSY | -10.11% | maturity:7.6y |
| GBIMESY2 | -9.77% | maturity:8.9y |
| NIBSF2 | -9.54% | liquidity:low; maturity:4.8y |
| KDBY | -9.46% | maturity:5.9y |
| RBBF40 | -9.45% | maturity:11.2y |
| NIBLGF | -9.32% | maturity:6.4y |
| PRSF | -9.12% | maturity:5.6y |
| GIBF1 | -8.57% | maturity:6.0y |
| RMF2 | -7.00% | liquidity:low; maturity:6.8y |
| NMBHF2 | -6.97% | maturity:8.5y |
| GSY | -6.63% | maturity:8.4y |
| NBF2 | -6.40% | liquidity:low |
| RSY | -6.36% | maturity:8.7y |
| SAGF | -5.88% | liquidity:low; maturity:7.3y |
| NSIF2 | -5.83% | maturity:6.0y |
| NBF3 | -5.52% | maturity:5.1y |
| MMF1 | -5.17% | maturity:5.1y |
| C30MF | -5.03% | liquidity:low; maturity:6.8y |
| SIGS3 | -4.98% | maturity:6.7y |
| MNMF1 | -4.79% | maturity:8.3y |
| KEF | -3.85% | valuation:small_discount; maturity:4.6y |
| HLICF | -3.78% | valuation:small_discount; maturity:9.1y |
| MBLEF | -3.69% | valuation:small_discount; maturity:10.6y |
| H8020 | -2.99% | valuation:small_discount; maturity:7.1y |
| RMF1 | -2.72% | valuation:small_discount |
| SEF | -1.25% | valuation:small_discount |
| SIGS2 | 1.57% | valuation:premium |
| SLCF | 3.17% | valuation:premium |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 25
- NAV data age: median 14 days, max 445 days

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
