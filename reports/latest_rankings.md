# Nepal MF Quant — Full Analysis Report

*Generated: 2026-11-03 17:50*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-11-03 |
| Funds Tracked | 39 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 24 |
| Median Discount | -8.71% |
| CONSIDER | 5 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 15 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 23.1% |
| -10% to -6% | 22 | 56.4% |
| -6% to -4% | 4 | 10.3% |
| -4% to 0% | 3 | 7.7% |
| ≥ 0% (premium) | 1 | 2.6% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.16 | -12.51% | 2.6y | high | 4d | 0.48% | 76.5 | ↑ narrowing | — |
| 2 | RMF1 | RBB Mutual Fund 1 | 10.21 | 9.22 | -9.70% | 1.7y | high | 20d | -0.10% | 63.9 | ↑ narrowing | high_vol |
| 3 | SEF | Siddhartha Equity Fund | 10.78 | 9.90 | -8.16% | 1.0y | medium | 13d | 2.76% | 63.7 | ↑ narrowing | — |
| 4 | NICSF | NIC Asia Select-30 | 9.50 | 8.80 | -7.37% | 1.7y | medium | 22d | 2.37% | 56.4 | ↑ narrowing | high_vol |
| 5 | NICBF | NIC ASIA Balanced Fund | 10.01 | 9.30 | -7.09% | 2.8y | medium | 2d | -0.99% | 48.0 | ↑ narrowing | — |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 28 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -20.02% | maturity:4.4y |
| LUK | -18.44% | liquidity:low |
| SFEF | -17.94% | maturity:5.3y |
| LVF2 | -17.62% | maturity:6.8y |
| SFMF | -12.39% | liquidity:low |
| NBF3 | -11.34% | maturity:4.9y |
| NIBSF2 | -10.56% | liquidity:low; maturity:4.6y |
| KSY | -10.01% | maturity:7.4y |
| NMBHF2 | -9.91% | maturity:8.3y |
| GSY | -9.82% | liquidity:low; maturity:8.2y |
| NICGF2 | -9.73% | maturity:4.0y |
| GBIMESY2 | -9.54% | maturity:8.7y |
| MBLEF | -9.41% | liquidity:low; maturity:10.4y |
| NIBLSTF | -9.39% | maturity:9.3y |
| SIGS2 | -9.30% | liquidity:low |
| SLCF | -8.81% | liquidity:low |
| RBBF40 | -8.75% | maturity:11.0y |
| MNMF1 | -8.71% | maturity:8.1y |
| KEF | -8.65% | maturity:4.4y |
| RMF2 | -8.55% | liquidity:low; maturity:6.5y |
| KDBY | -8.23% | maturity:5.7y |
| RSY | -7.89% | maturity:8.5y |
| NIBLGF | -7.76% | maturity:6.2y |
| MMF1 | -7.60% | maturity:4.8y |
| NICFC | -6.74% | liquidity:low |
| NSIF2 | -6.33% | maturity:5.8y |
| C30MF | -5.99% | liquidity:low; maturity:6.5y |
| GIBF1 | -5.43% | maturity:5.7y |
| SAGF | -5.00% | maturity:7.1y |
| SIGS3 | -4.73% | maturity:6.5y |
| PSF | -3.67% | valuation:small_discount |
| PRSF | -3.23% | valuation:small_discount; maturity:5.4y |
| HLICF | -1.62% | valuation:small_discount; maturity:8.9y |
| H8020 | 2.52% | valuation:premium; maturity:6.9y |

</details>

## Data Quality

- Symbols checked: 47
- Symbols with issues: 29
- NAV data age: median 19 days, max 523 days

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
