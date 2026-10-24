# Nepal MF Quant — Full Analysis Report

*Generated: 2026-10-24 14:02*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-10-16 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 39 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 21 |
| Median Discount | -8.95% |
| CONSIDER | 8 |
| IGNORE | 31 |

> ⚠️ **NAV Staleness Warning**: 9 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 11 | 28.2% |
| -10% to -6% | 22 | 56.4% |
| -6% to -4% | 3 | 7.7% |
| -4% to 0% | 3 | 7.7% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | LUK | Laxmi Unnati Kosh | 11.66 | 9.85 | -15.52% | 3.8y | high | 6d | -1.17% | 83.5 | ↑ narrowing | — |
| 2 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.10 | -13.09% | 2.6y | medium | 6d | 0.48% | 66.5 | ↓ widening | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.22 | 9.30 | -9.00% | 1.8y | high | 14d | -0.87% | 57.6 | → stable | high_vol |
| 4 | SEF | Siddhartha Equity Fund | 10.49 | 9.80 | -6.58% | 1.1y | high | 7d | 1.06% | 54.7 | ↑ narrowing | — |
| 5 | PSF | Prabhu Select Fund | 12.00 | 11.22 | -6.50% | 1.7y | high | 6d | -8.33% | 54.4 | ↑ narrowing | — |
| 6 | NICSF | NIC Asia Select-30 | 9.28 | 8.40 | -9.48% | 1.7y | high | 16d | -2.11% | 53.3 | → stable | high_vol |
| 7 | NICBF | NIC ASIA Balanced Fund | 10.01 | 9.06 | -9.49% | 2.9y | medium | 1d | -0.99% | 47.7 | ↓ widening | — |
| 8 | SLCF | Sanima Large Cap Fund | 10.04 | 9.25 | -7.87% | 1.4y | medium | 1d | -0.99% | 47.0 | ↓ widening | — |

## IGNORE Summary

*31 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -19.11% | liquidity:low; maturity:6.9y |
| SBCF | -18.25% | maturity:4.4y |
| SFEF | -16.89% | liquidity:low; maturity:5.3y |
| SFMF | -16.81% | liquidity:low |
| RMF2 | -14.43% | liquidity:low; maturity:6.6y |
| GIBF1 | -12.86% | maturity:5.8y |
| NBF3 | -12.50% | maturity:4.9y |
| C30MF | -11.67% | liquidity:low; maturity:6.6y |
| NICGF2 | -10.44% | maturity:4.1y |
| NIBLSTF | -9.85% | maturity:9.3y |
| NIBLGF | -9.55% | liquidity:low; maturity:6.3y |
| NICFC | -9.46% | liquidity:low |
| MBLEF | -9.17% | maturity:10.4y |
| MNMF1 | -9.00% | maturity:8.2y |
| NIBSF2 | -8.95% | maturity:4.6y |
| KSY | -8.17% | maturity:7.4y |
| RBBF40 | -7.91% | maturity:11.1y |
| RSY | -7.88% | maturity:8.6y |
| H8020 | -7.58% | maturity:7.0y |
| GBIMESY2 | -7.50% | maturity:8.8y |
| SIGS2 | -7.08% | liquidity:low |
| SAGF | -7.00% | liquidity:low; maturity:7.1y |
| KEF | -6.95% | maturity:4.4y |
| GSY | -6.80% | maturity:8.2y |
| MMF1 | -6.32% | maturity:4.9y |
| KDBY | -5.97% | maturity:5.8y |
| NMBHF2 | -5.75% | maturity:8.4y |
| PRSF | -5.46% | maturity:5.4y |
| NSIF2 | -3.23% | valuation:small_discount; maturity:5.9y |
| SIGS3 | -2.52% | valuation:small_discount; maturity:6.5y |
| HLICF | -1.40% | valuation:small_discount; liquidity:low; maturity:8.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 34
- NAV data age: median 39 days, max 513 days

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
