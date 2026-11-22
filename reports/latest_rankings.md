# Nepal MF Quant — Full Analysis Report

*Generated: 2026-11-22 17:49*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-11-20 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 16 |
| Median Discount | -7.59% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 11 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 6 | 15.4% |
| -10% to -6% | 21 | 53.8% |
| -6% to -4% | 8 | 20.5% |
| -4% to 0% | 3 | 7.7% |
| ≥ 0% (premium) | 1 | 2.6% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SEF | Siddhartha Equity Fund | 10.78 | 9.97 | -7.51% | 1.0y | high | 18d | 2.76% | 65.0 | ↑ narrowing | — |
| 2 | NICSF | NIC Asia Select-30 | 9.50 | 9.05 | -4.74% | 1.6y | high | 27d | 2.37% | 60.9 | ↑ narrowing | high_vol |
| 3 | SLCF | Sanima Large Cap Fund | 10.10 | 9.32 | -7.72% | 1.3y | medium | 4d | 0.60% | 60.4 | ↑ narrowing | — |
| 4 | RMF1 | RBB Mutual Fund 1 | 10.21 | 9.32 | -8.72% | 1.7y | medium | 1d | -0.10% | 58.2 | ↑ narrowing | high_vol |
| 5 | NBF2 | Nabil Balanced Fund - 2 | 9.78 | 9.30 | -4.91% | 2.5y | medium | 9d | -3.26% | 53.1 | ↑ narrowing | — |
| 6 | NICGF2 | NIC Asia Growth Fund 2 | 9.87 | 9.01 | -8.71% | 4.0y | medium | 1d | -2.18% | 52.2 | ↑ narrowing | high_vol |
| 7 | NICBF | NIC ASIA Balanced Fund | 10.01 | 9.25 | -7.59% | 2.8y | medium | 2d | -0.99% | 48.3 | → stable | — |
| 8 | NICFC | NIC Asia Flexi Cap Fund | 9.94 | 9.35 | -5.94% | 2.6y | medium | 5d | -1.29% | 44.6 | ↑ narrowing | — |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 27 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -21.25% | liquidity:low; maturity:4.3y |
| LVF2 | -20.07% | liquidity:low; maturity:6.8y |
| SFEF | -19.34% | maturity:5.2y |
| LUK | -18.52% | liquidity:low |
| SFMF | -11.95% | liquidity:low |
| MMF1 | -10.47% | maturity:4.8y |
| NIBLGF | -9.65% | maturity:6.2y |
| NIBSF2 | -9.14% | maturity:4.5y |
| NIBLSTF | -9.08% | maturity:9.2y |
| RBBF40 | -8.75% | maturity:11.0y |
| KSY | -8.72% | maturity:7.3y |
| GSY | -8.64% | maturity:8.1y |
| NMBHF2 | -8.62% | maturity:8.3y |
| MBLEF | -8.34% | liquidity:low; maturity:10.4y |
| NBF3 | -7.99% | maturity:4.8y |
| MNMF1 | -7.92% | maturity:8.1y |
| RMF2 | -7.20% | liquidity:low; maturity:6.5y |
| SIGS2 | -7.04% | liquidity:low |
| SAGF | -7.00% | liquidity:low; maturity:7.0y |
| KDBY | -6.98% | maturity:5.7y |
| RSY | -6.56% | maturity:8.4y |
| GBIMESY2 | -6.39% | maturity:8.7y |
| NSIF2 | -5.77% | maturity:5.8y |
| C30MF | -5.59% | liquidity:low; maturity:6.5y |
| KEF | -4.52% | maturity:4.3y |
| GIBF1 | -4.49% | maturity:5.7y |
| PRSF | -4.10% | maturity:5.3y |
| PSF | -3.39% | valuation:small_discount |
| SIGS3 | -2.37% | valuation:small_discount; maturity:6.5y |
| HLICF | -1.04% | valuation:small_discount; liquidity:low; maturity:8.8y |
| H8020 | 3.14% | valuation:premium; maturity:6.9y |

</details>

## Data Quality

- Symbols checked: 49
- Symbols with issues: 25
- NAV data age: median 38 days, max 542 days

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
