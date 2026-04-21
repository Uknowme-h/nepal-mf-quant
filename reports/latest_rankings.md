# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-21 11:24*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-21 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 20 |
| Median Discount | -7.73% |
| CONSIDER | 8 |
| IGNORE | 33 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 11 | 26.8% |
| -10% to -6% | 18 | 43.9% |
| -6% to -4% | 5 | 12.2% |
| -4% to 0% | 4 | 9.8% |
| ≥ 0% (premium) | 3 | 7.3% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.66 | -8.52% | 2.3y | medium | 1d | 5.28% | 60.6 | → stable | high_vol |
| 2 | SEF | Siddhartha Equity Fund | 10.55 | 10.00 | -5.21% | 1.6y | high | 2d | 4.98% | 60.4 | ↑ narrowing | high_vol |
| 3 | SIGS2 | Siddhartha Investment Gro | 10.98 | 10.23 | -6.83% | 3.4y | medium | 3d | 5.17% | 59.4 | ↑ narrowing | — |
| 4 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.39 | -10.74% | 3.1y | medium | 3d | 4.26% | 59.4 | ↓ widening | — |
| 5 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.52 | -9.07% | 3.4y | medium | 1d | 4.39% | 56.1 | ↑ narrowing | high_vol |
| 6 | NICSF | NIC Asia Select-30 | 10.04 | 9.21 | -8.27% | 2.2y | medium | 4d | 5.35% | 52.7 | ↓ widening | — |
| 7 | SLCF | Sanima Large Cap Fund | 10.60 | 9.83 | -7.26% | 1.8y | medium | 9d | 4.43% | 48.8 | ↓ widening | — |
| 8 | CMF2 | Citizens Mutual Fund - 2 | 10.62 | 10.07 | -5.18% | 0.2y | medium | 1d | 3.31% | 43.0 | ↓ widening | — |

## IGNORE Summary

*33 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 7 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LUK | -15.01% | liquidity:low; maturity:4.3y |
| SBCF | -13.58% | maturity:4.9y |
| LVF2 | -13.23% | liquidity:low; maturity:7.4y |
| NICGF2 | -12.56% | liquidity:low; maturity:4.6y |
| MBLEF | -11.43% | maturity:10.9y |
| RMF2 | -11.27% | liquidity:low; maturity:7.1y |
| SFEF | -11.20% | maturity:5.8y |
| NSIF2 | -11.07% | maturity:6.4y |
| NIBLSTF | -10.23% | maturity:9.8y |
| GIBF1 | -10.10% | maturity:6.3y |
| RSY | -9.65% | maturity:9.0y |
| KSY | -9.21% | maturity:7.9y |
| MMF1 | -9.06% | maturity:5.4y |
| NIBLGF | -8.28% | liquidity:low; maturity:6.8y |
| GSY | -8.11% | maturity:8.7y |
| MNMF1 | -8.01% | maturity:8.7y |
| C30MF | -7.73% | liquidity:low; maturity:7.1y |
| GBIMESY2 | -7.69% | maturity:9.2y |
| NMBHF2 | -7.53% | maturity:8.9y |
| RBBF40 | -7.43% | maturity:11.6y |
| NIBSF2 | -7.32% | maturity:5.1y |
| SAGF | -7.12% | liquidity:low; maturity:7.6y |
| SFMF | -7.08% | liquidity:low |
| H8020 | -5.41% | maturity:7.5y |
| NBF2 | -5.06% | liquidity:low |
| HLICF | -4.56% | maturity:9.4y |
| SIGS3 | -3.96% | valuation:small_discount; liquidity:low; maturity:7.0y |
| NBF3 | -3.39% | valuation:small_discount; maturity:5.4y |
| NMB50 | -2.39% | valuation:small_discount |
| PSF | -2.35% | valuation:small_discount |
| PRSF | 0.08% | valuation:premium; maturity:5.9y |
| KDBY | 2.45% | valuation:premium; maturity:6.3y |
| KEF | 2.94% | valuation:premium; maturity:4.9y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 17
- NAV data age: median 37 days, max 327 days

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
