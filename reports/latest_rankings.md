# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-22 11:22*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-22 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 22 |
| Median Discount | -8.19% |
| CONSIDER | 7 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 14 | 34.1% |
| -10% to -6% | 15 | 36.6% |
| -6% to -4% | 6 | 14.6% |
| -4% to 0% | 3 | 7.3% |
| ≥ 0% (premium) | 3 | 7.3% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICSF | NIC Asia Select-30 | 10.04 | 9.39 | -6.47% | 2.2y | medium | 5d | 5.35% | 55.7 | → stable | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.50 | -7.08% | 3.5y | medium | 1d | -2.04% | 54.0 | → stable | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.70 | -8.14% | 2.2y | medium | 2d | 5.28% | 51.6 | ↓ widening | high_vol |
| 4 | SLCF | Sanima Large Cap Fund | 10.60 | 10.00 | -5.66% | 1.8y | medium | 10d | 4.43% | 51.5 | → stable | — |
| 5 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.32 | -10.98% | 3.4y | medium | 2d | 4.39% | 49.0 | ↓ widening | high_vol |
| 6 | SEF | Siddhartha Equity Fund | 10.55 | 9.90 | -6.16% | 1.6y | medium | 3d | 4.98% | 43.5 | ↓ widening | high_vol |
| 7 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.85 | -5.92% | 3.1y | medium | 1d | 0.48% | 42.0 | ↓ widening | — |

## IGNORE Summary

*34 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 6 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -15.01% | liquidity:low; maturity:4.3y |
| SBCF | -13.67% | maturity:4.9y |
| NICGF2 | -13.59% | liquidity:low; maturity:4.6y |
| MNMF1 | -12.06% | maturity:8.7y |
| SFEF | -11.99% | liquidity:low; maturity:5.8y |
| MBLEF | -11.61% | maturity:10.9y |
| NSIF2 | -11.48% | maturity:6.4y |
| NIBLSTF | -11.40% | maturity:9.8y |
| KSY | -11.35% | maturity:7.9y |
| RMF2 | -11.27% | liquidity:low; maturity:7.1y |
| NICFC | -11.22% | liquidity:low |
| LVF2 | -11.13% | maturity:7.4y |
| GIBF1 | -10.34% | liquidity:low; maturity:6.3y |
| RBBF40 | -9.84% | maturity:11.6y |
| RSY | -9.65% | maturity:9.0y |
| NMBHF2 | -9.58% | maturity:8.9y |
| NIBSF2 | -9.07% | maturity:5.1y |
| GSY | -8.76% | maturity:8.7y |
| SAGF | -8.49% | maturity:7.6y |
| NIBLGF | -8.19% | maturity:6.8y |
| GBIMESY2 | -7.69% | liquidity:low; maturity:9.2y |
| SIGS2 | -7.56% | liquidity:low |
| C30MF | -7.45% | maturity:7.1y |
| MMF1 | -7.19% | maturity:5.4y |
| CMF2 | -5.84% | liquidity:low |
| HLICF | -5.08% | maturity:9.4y |
| SIGS3 | -4.85% | liquidity:low; maturity:7.0y |
| H8020 | -4.61% | maturity:7.5y |
| NBF3 | -3.10% | valuation:small_discount; maturity:5.4y |
| PSF | -2.43% | valuation:small_discount |
| NMB50 | -2.12% | valuation:small_discount |
| KDBY | 0.35% | valuation:premium; maturity:6.3y |
| KEF | 0.76% | valuation:premium; maturity:4.9y |
| PRSF | 0.92% | valuation:premium; maturity:5.9y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 26
- NAV data age: median 38 days, max 328 days

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
