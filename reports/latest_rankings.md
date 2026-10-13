# Nepal MF Quant — Full Analysis Report

*Generated: 2026-10-13 17:36*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-10-13 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 30 |
| Median Discount | -9.90% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 19 | 48.7% |
| -10% to -6% | 16 | 41.0% |
| -6% to -4% | 3 | 7.7% |
| -4% to 0% | 1 | 2.6% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.19 | -12.23% | 2.6y | medium | 3d | 0.48% | 78.7 | ↑ narrowing | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 9.20 | -18.58% | 3.1y | high | 2d | -2.04% | 72.8 | → stable | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.22 | 9.25 | -9.49% | 1.8y | medium | 11d | -0.87% | 60.8 | ↑ narrowing | high_vol |
| 4 | LUK | Laxmi Unnati Kosh | 11.66 | 9.50 | -18.52% | 3.8y | medium | 3d | -1.17% | 60.3 | ↓ widening | — |
| 5 | NICSF | NIC Asia Select-30 | 9.28 | 8.15 | -12.18% | 1.7y | high | 13d | -2.11% | 59.1 | ↓ widening | high_vol |
| 6 | SEF | Siddhartha Equity Fund | 10.49 | 9.67 | -7.82% | 1.1y | high | 4d | 1.06% | 58.6 | ↑ narrowing | — |
| 7 | NICFC | NIC Asia Flexi Cap Fund | 9.94 | 8.72 | -12.27% | 2.7y | medium | 2d | -1.29% | 57.6 | ↓ widening | — |
| 8 | PSF | Prabhu Select Fund | 12.00 | 11.02 | -8.17% | 1.7y | medium | 3d | -8.33% | 46.7 | ↑ narrowing | — |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 1 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -21.26% | maturity:5.3y |
| SBCF | -20.63% | maturity:4.5y |
| LVF2 | -16.74% | liquidity:low; maturity:6.9y |
| RMF2 | -16.28% | maturity:6.6y |
| GIBF1 | -12.69% | maturity:5.8y |
| NBF3 | -12.69% | maturity:5.0y |
| NIBLGF | -12.30% | maturity:6.3y |
| MNMF1 | -11.77% | maturity:8.2y |
| C30MF | -11.10% | liquidity:low; maturity:6.6y |
| RBBF40 | -10.91% | maturity:11.1y |
| NIBLSTF | -10.81% | maturity:9.3y |
| NIBSF2 | -10.49% | maturity:4.6y |
| NICBF | -10.09% | liquidity:low |
| MMF1 | -10.00% | maturity:4.9y |
| GBIMESY2 | -9.90% | maturity:8.8y |
| H8020 | -9.82% | maturity:7.0y |
| SIGS2 | -9.70% | liquidity:low |
| RSY | -9.23% | liquidity:low; maturity:8.6y |
| NMBHF2 | -9.17% | liquidity:low; maturity:8.4y |
| KSY | -8.77% | maturity:7.4y |
| KDBY | -8.60% | liquidity:low; maturity:5.8y |
| SLCF | -8.37% | liquidity:low |
| GSY | -8.28% | maturity:8.2y |
| MBLEF | -7.50% | maturity:10.5y |
| KEF | -7.44% | maturity:4.4y |
| NICGF2 | -7.29% | maturity:4.1y |
| PRSF | -6.38% | liquidity:low; maturity:5.4y |
| NSIF2 | -5.03% | maturity:5.9y |
| SAGF | -5.00% | liquidity:low; maturity:7.1y |
| HLICF | -4.67% | maturity:8.9y |
| SIGS3 | -3.92% | valuation:small_discount; maturity:6.5y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 27
- NAV data age: median 28 days, max 502 days

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
