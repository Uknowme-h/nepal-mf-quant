# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-06 11:13*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-06 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 40 |
| At Premium (price ≥ NAV) | 1 |
| Deep Discount (≤ -8%) | 22 |
| Median Discount | -8.29% |
| CONSIDER | 9 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 10 | 24.4% |
| -10% to -6% | 21 | 51.2% |
| -6% to -4% | 7 | 17.1% |
| -4% to 0% | 2 | 4.9% |
| ≥ 0% (premium) | 1 | 2.4% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | PSF | Prabhu Select Fund | 12.75 | 11.85 | -7.06% | 2.2y | high | 6d | 5.81% | 65.0 | → stable | — |
| 2 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.63 | -8.81% | 2.3y | medium | 4d | 5.28% | 60.7 | → stable | high_vol |
| 3 | NICFC | NIC Asia Flexi Cap Fund | 10.52 | 9.31 | -11.50% | 3.2y | medium | 5d | 4.26% | 57.1 | ↓ widening | — |
| 4 | SLCF | Sanima Large Cap Fund | 10.60 | 9.81 | -7.45% | 1.9y | medium | 3d | 4.43% | 56.5 | ↓ widening | — |
| 5 | NICSF | NIC Asia Select-30 | 10.04 | 9.31 | -7.27% | 2.2y | medium | 4d | 5.35% | 55.1 | ↓ widening | — |
| 6 | SEF | Siddhartha Equity Fund | 10.55 | 9.85 | -6.64% | 1.6y | high | 4d | 4.98% | 53.3 | ↓ widening | high_vol |
| 7 | CMF2 | Citizens Mutual Fund - 2 | 10.62 | 9.92 | -6.59% | 0.2y | medium | 4d | 3.31% | 40.6 | ↓ widening | — |
| 8 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 10.00 | -4.49% | 3.1y | medium | 2d | 0.48% | 40.6 | → stable | — |
| 9 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.96 | -4.87% | 3.4y | medium | 4d | 4.39% | 31.8 | ↓ widening | high_vol |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 3 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| LVF2 | -15.86% | liquidity:low; maturity:7.4y |
| LUK | -15.61% | liquidity:low; maturity:4.4y |
| SBCF | -15.34% | maturity:5.0y |
| GIBF1 | -13.49% | maturity:6.3y |
| NSIF2 | -13.44% | maturity:6.4y |
| SFEF | -11.64% | liquidity:low; maturity:5.9y |
| KSY | -10.79% | liquidity:low; maturity:8.0y |
| NICGF2 | -10.59% | maturity:4.6y |
| SIGS3 | -10.13% | liquidity:low; maturity:7.1y |
| NIBLSTF | -9.94% | maturity:9.8y |
| RSY | -9.65% | maturity:9.1y |
| MBLEF | -9.25% | maturity:11.0y |
| C30MF | -9.18% | maturity:7.1y |
| RMF2 | -8.61% | liquidity:low; maturity:7.1y |
| NMBHF2 | -8.56% | maturity:8.9y |
| H8020 | -8.43% | maturity:7.5y |
| KDBY | -8.41% | maturity:6.3y |
| RBBF40 | -8.39% | liquidity:low; maturity:11.6y |
| GSY | -8.29% | maturity:8.8y |
| PRSF | -8.24% | maturity:5.9y |
| SAGF | -7.85% | maturity:7.7y |
| GBIMESY2 | -7.69% | liquidity:low; maturity:9.3y |
| SFMF | -7.17% | liquidity:low |
| MNMF1 | -6.08% | maturity:8.7y |
| MMF1 | -5.62% | maturity:5.4y |
| SIGS2 | -5.28% | liquidity:low |
| KEF | -4.74% | maturity:5.0y |
| HLICF | -4.56% | maturity:9.4y |
| NBF3 | -4.07% | maturity:5.5y |
| NMB50 | -2.03% | valuation:small_discount |
| NIBSF2 | -1.27% | valuation:small_discount; maturity:5.2y |
| NIBLGF | 4.68% | valuation:premium; maturity:6.8y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 17
- NAV data age: median 22 days, max 312 days

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
