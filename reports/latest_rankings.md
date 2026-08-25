# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-25 10:48*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-25 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 24 |
| Median Discount | -8.98% |
| CONSIDER | 8 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 17 | 42.5% |
| -10% to -6% | 16 | 40.0% |
| -6% to -4% | 5 | 12.5% |
| -4% to 0% | 2 | 5.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | LUK | Laxmi Unnati Kosh | 11.66 | 9.55 | -18.10% | 4.0y | medium | 1d | -1.17% | 67.4 | ↓ widening | — |
| 2 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 8.90 | -13.59% | 2.8y | medium | 5d | 0.88% | 67.1 | ↓ widening | — |
| 3 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.60 | -15.04% | 3.2y | medium | 7d | -2.04% | 62.2 | ↓ widening | — |
| 4 | NICSF | NIC Asia Select-30 | 9.55 | 8.67 | -9.21% | 1.9y | medium | 10d | -2.55% | 60.9 | ↑ narrowing | — |
| 5 | NMB50 | NMB 50 | 10.45 | 9.70 | -7.18% | 0.0y | medium | 7d | -1.42% | 58.5 | ↓ widening | — |
| 6 | PSF | Prabhu Select Fund | 13.04 | 12.10 | -7.21% | 1.8y | high | 58d | -4.26% | 57.8 | ↑ narrowing | — |
| 7 | SEF | Siddhartha Equity Fund | 10.36 | 9.28 | -10.42% | 1.2y | medium | 6d | -2.72% | 56.8 | ↓ widening | — |
| 8 | SIGS2 | Siddhartha Investment Gro | 10.85 | 10.36 | -4.52% | 3.0y | medium | 1d | -3.30% | 45.9 | ↓ widening | — |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 2 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -21.82% | maturity:7.0y |
| SBCF | -18.78% | liquidity:low; maturity:4.6y |
| KDBY | -18.03% | maturity:5.9y |
| NICGF2 | -15.96% | liquidity:low; maturity:4.2y |
| SFEF | -15.66% | liquidity:low; maturity:5.5y |
| NSIF2 | -13.55% | maturity:6.0y |
| KEF | -12.59% | maturity:4.6y |
| NIBSF2 | -12.51% | maturity:4.8y |
| NICBF | -12.50% | liquidity:low |
| NMBHF2 | -12.21% | maturity:8.5y |
| MBLEF | -11.89% | maturity:10.6y |
| NIBLSTF | -11.01% | liquidity:low; maturity:9.5y |
| GBIMESY2 | -10.37% | liquidity:low; maturity:8.9y |
| NIBLGF | -9.84% | maturity:6.4y |
| PRSF | -9.12% | maturity:5.6y |
| RMF1 | -8.85% | liquidity:low |
| GIBF1 | -8.74% | maturity:5.9y |
| MNMF1 | -8.51% | maturity:8.3y |
| MMF1 | -8.23% | maturity:5.0y |
| KSY | -7.97% | liquidity:low; maturity:7.6y |
| RMF2 | -7.92% | maturity:6.7y |
| GSY | -7.83% | maturity:8.4y |
| SLCF | -7.74% | liquidity:low |
| RBBF40 | -6.53% | maturity:11.2y |
| NBF2 | -6.11% | liquidity:low |
| NBF3 | -6.01% | maturity:5.1y |
| RSY | -5.56% | maturity:8.7y |
| C30MF | -5.03% | maturity:6.7y |
| HLICF | -4.93% | maturity:9.1y |
| SAGF | -4.17% | maturity:7.3y |
| SIGS3 | -3.85% | valuation:small_discount; maturity:6.7y |
| H8020 | -1.46% | valuation:small_discount; maturity:7.1y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 24
- NAV data age: median 22 days, max 453 days

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
