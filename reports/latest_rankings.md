# Nepal MF Quant — Full Analysis Report

*Generated: 2026-11-04 18:00*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-11-04 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 25 |
| Median Discount | -8.63% |
| CONSIDER | 7 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 15 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 10 | 25.6% |
| -10% to -6% | 23 | 59.0% |
| -6% to -4% | 2 | 5.1% |
| -4% to 0% | 3 | 7.7% |
| ≥ 0% (premium) | 1 | 2.6% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.10 | -13.09% | 2.6y | medium | 5d | 0.48% | 64.4 | → stable | — |
| 2 | RMF1 | RBB Mutual Fund 1 | 10.21 | 9.14 | -10.48% | 1.7y | medium | 21d | -0.10% | 61.7 | ↑ narrowing | high_vol |
| 3 | LUK | Laxmi Unnati Kosh | 11.66 | 9.51 | -18.44% | 3.8y | medium | 1d | -1.17% | 61.5 | → stable | — |
| 4 | NICFC | NIC Asia Flexi Cap Fund | 9.94 | 9.28 | -6.64% | 2.6y | medium | 1d | -1.29% | 56.3 | ↑ narrowing | — |
| 5 | NICBF | NIC ASIA Balanced Fund | 10.01 | 9.31 | -6.99% | 2.8y | high | 3d | -0.99% | 54.9 | ↑ narrowing | — |
| 6 | SEF | Siddhartha Equity Fund | 10.78 | 9.95 | -7.70% | 1.0y | medium | 14d | 2.76% | 52.8 | → stable | — |
| 7 | NICSF | NIC Asia Select-30 | 9.50 | 8.71 | -8.32% | 1.7y | high | 23d | 2.37% | 52.6 | ↓ widening | high_vol |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SFEF | -20.38% | maturity:5.3y |
| SBCF | -18.69% | maturity:4.4y |
| LVF2 | -17.62% | maturity:6.8y |
| SFMF | -12.39% | liquidity:low |
| NIBSF2 | -10.36% | maturity:4.6y |
| RMF2 | -10.18% | maturity:6.5y |
| NBF3 | -10.08% | maturity:4.9y |
| NIBLGF | -9.85% | maturity:6.2y |
| KSY | -9.71% | maturity:7.4y |
| GBIMESY2 | -9.44% | liquidity:low; maturity:8.7y |
| NICGF2 | -9.42% | liquidity:low; maturity:4.0y |
| SIGS2 | -9.30% | liquidity:low |
| MNMF1 | -9.21% | maturity:8.1y |
| GSY | -9.14% | maturity:8.2y |
| RSY | -8.65% | maturity:8.5y |
| RBBF40 | -8.65% | liquidity:low; maturity:11.0y |
| MBLEF | -8.63% | liquidity:low; maturity:10.4y |
| MMF1 | -8.62% | maturity:4.8y |
| NMBHF2 | -8.42% | maturity:8.3y |
| SLCF | -8.32% | liquidity:low |
| KEF | -8.17% | maturity:4.4y |
| NIBLSTF | -7.93% | maturity:9.3y |
| KDBY | -7.87% | liquidity:low; maturity:5.7y |
| SAGF | -7.70% | maturity:7.1y |
| C30MF | -7.49% | maturity:6.5y |
| NSIF2 | -6.05% | liquidity:low; maturity:5.8y |
| GIBF1 | -5.34% | liquidity:low; maturity:5.7y |
| SIGS3 | -4.73% | maturity:6.5y |
| PSF | -3.58% | valuation:small_discount |
| PRSF | -2.92% | valuation:small_discount; maturity:5.4y |
| HLICF | -0.35% | valuation:small_discount; maturity:8.9y |
| H8020 | 2.43% | valuation:premium; maturity:6.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 32
- NAV data age: median 20 days, max 524 days

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
