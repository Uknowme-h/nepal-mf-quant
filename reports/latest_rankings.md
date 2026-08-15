# Nepal MF Quant — Full Analysis Report

*Generated: 2026-08-15 10:38*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-08-14 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 17 |
| Median Discount | -7.64% |
| CONSIDER | 5 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 7 | 17.5% |
| -10% to -6% | 16 | 40.0% |
| -6% to -4% | 11 | 27.5% |
| -4% to 0% | 6 | 15.0% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.10 | -11.65% | 2.8y | medium | 7d | 0.88% | 65.6 | ↓ widening | — |
| 2 | LUK | Laxmi Unnati Kosh | 11.66 | 9.80 | -15.95% | 4.0y | medium | 1d | -1.17% | 59.8 | ↓ widening | — |
| 3 | PSF | Prabhu Select Fund | 13.04 | 12.01 | -7.90% | 1.9y | medium | 51d | -4.26% | 57.2 | → stable | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.28 | 9.60 | -6.61% | 1.9y | high | 1d | -1.63% | 55.5 | ↓ widening | high_vol |
| 5 | NICSF | NIC Asia Select-30 | 9.55 | 9.00 | -5.76% | 1.9y | medium | 3d | -2.55% | 55.1 | ↑ narrowing | — |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 6 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -19.98% | maturity:7.1y |
| SBCF | -17.02% | maturity:4.6y |
| SFEF | -11.64% | maturity:5.5y |
| KSY | -11.47% | liquidity:low; maturity:7.6y |
| NICBF | -10.85% | liquidity:low |
| SFMF | -9.73% | liquidity:low |
| KDBY | -9.46% | maturity:6.0y |
| RBBF40 | -9.45% | maturity:11.2y |
| GBIMESY2 | -9.37% | maturity:8.9y |
| PRSF | -9.34% | liquidity:low; maturity:5.6y |
| NIBLSTF | -9.31% | maturity:9.5y |
| GIBF1 | -9.25% | maturity:6.0y |
| NIBLGF | -9.22% | maturity:6.4y |
| NICGF2 | -8.65% | maturity:4.3y |
| NSIF2 | -8.49% | maturity:6.0y |
| NMBHF2 | -7.92% | maturity:8.6y |
| NIBSF2 | -7.69% | maturity:4.8y |
| SIGS3 | -7.60% | liquidity:low; maturity:6.7y |
| RMF2 | -7.00% | maturity:6.8y |
| RSY | -5.91% | maturity:8.7y |
| NBF3 | -5.81% | maturity:5.1y |
| MMF1 | -5.70% | maturity:5.1y |
| NBF2 | -5.64% | liquidity:low |
| MNMF1 | -5.19% | maturity:8.3y |
| SAGF | -5.12% | maturity:7.3y |
| C30MF | -4.75% | liquidity:low; maturity:6.8y |
| KEF | -4.72% | maturity:4.6y |
| H8020 | -4.61% | liquidity:low; maturity:7.1y |
| MBLEF | -4.33% | maturity:10.6y |
| SLCF | -3.77% | valuation:small_discount |
| GSY | -3.61% | valuation:small_discount; maturity:8.4y |
| SEF | -2.99% | valuation:small_discount; liquidity:low |
| HLICF | -1.49% | valuation:small_discount; maturity:9.1y |
| SIGS2 | -1.38% | valuation:small_discount; liquidity:low |
| NMB50 | -0.77% | valuation:small_discount |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 33
- NAV data age: median 12 days, max 443 days

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
