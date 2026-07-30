# Nepal MF Quant — Full Analysis Report

*Generated: 2026-07-30 12:04*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-07-30 |
| Funds Tracked | 40 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 25 |
| Median Discount | -9.80% |
| CONSIDER | 5 |
| IGNORE | 35 |

> ⚠️ **NAV Staleness Warning**: 17 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 18 | 45.0% |
| -10% to -6% | 17 | 42.5% |
| -6% to -4% | 2 | 5.0% |
| -4% to 0% | 2 | 5.0% |
| ≥ 0% (premium) | 1 | 2.5% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICFC | NIC Asia Flexi Cap Fund | 10.30 | 9.28 | -9.90% | 2.9y | medium | 10d | 0.88% | 66.8 | ↑ narrowing | — |
| 2 | PSF | Prabhu Select Fund | 13.69 | 11.80 | -13.81% | 1.9y | high | 41d | -4.60% | 66.1 | ↓ widening | — |
| 3 | NICSF | NIC Asia Select-30 | 9.80 | 8.80 | -10.20% | 1.9y | medium | 5d | 1.45% | 57.2 | ↓ widening | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.45 | 9.68 | -7.37% | 2.0y | high | 10d | 0.38% | 47.0 | ↓ widening | high_vol |
| 5 | SEF | Siddhartha Equity Fund | 10.65 | 9.81 | -7.89% | 1.3y | high | 3d | 0.00% | 46.6 | ↓ widening | — |

## IGNORE Summary

*35 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -19.98% | maturity:7.1y |
| SBCF | -16.23% | maturity:4.7y |
| KEF | -13.97% | maturity:4.6y |
| PRSF | -13.95% | liquidity:low; maturity:5.6y |
| KDBY | -13.21% | maturity:6.0y |
| SFEF | -12.51% | maturity:5.5y |
| GBIMESY2 | -11.55% | liquidity:low; maturity:9.0y |
| NICGF2 | -11.54% | maturity:4.3y |
| NIBSF2 | -11.38% | maturity:4.8y |
| RBBF40 | -11.13% | maturity:11.3y |
| GIBF1 | -10.94% | maturity:6.0y |
| NSIF2 | -10.65% | maturity:6.1y |
| NIBLSTF | -10.51% | liquidity:low; maturity:9.5y |
| LUK | -10.29% | maturity:4.0y |
| SFMF | -10.18% | liquidity:low |
| SIGS3 | -10.08% | maturity:6.8y |
| NIBLGF | -9.82% | maturity:6.5y |
| MNMF1 | -9.79% | maturity:8.4y |
| RSY | -9.69% | maturity:8.8y |
| NICBF | -9.50% | liquidity:low |
| RMF2 | -8.95% | maturity:6.8y |
| MBLEF | -8.35% | maturity:10.7y |
| MMF1 | -7.98% | maturity:5.1y |
| NMBHF2 | -7.67% | maturity:8.6y |
| H8020 | -7.29% | maturity:7.2y |
| C30MF | -6.85% | maturity:6.8y |
| SAGF | -6.65% | maturity:7.3y |
| GSY | -6.58% | maturity:8.4y |
| SIGS2 | -6.42% | liquidity:low |
| KSY | -6.34% | liquidity:low; maturity:7.6y |
| NBF2 | -5.44% | liquidity:low |
| NBF3 | -4.55% | maturity:5.2y |
| SLCF | -3.57% | valuation:small_discount |
| HLICF | -3.01% | valuation:small_discount; liquidity:low; maturity:9.1y |
| NMB50 | 0.85% | valuation:premium; liquidity:low |

</details>

## Data Quality

- Symbols checked: 44
- Symbols with issues: 31
- NAV data age: median 45 days, max 427 days

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
