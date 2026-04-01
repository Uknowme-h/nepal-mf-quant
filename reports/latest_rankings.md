# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-01 11:15*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-01 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 41 |
| At Premium (price ≥ NAV) | 0 |
| Deep Discount (≤ -8%) | 20 |
| Median Discount | -7.92% |
| CONSIDER | 9 |
| IGNORE | 32 |

> ⚠️ **NAV Staleness Warning**: 10 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 10 | 24.4% |
| -10% to -6% | 24 | 58.5% |
| -6% to -4% | 3 | 7.3% |
| -4% to 0% | 4 | 9.8% |
| ≥ 0% (premium) | 0 | 0.0% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | SIGS2 | Siddhartha Investment Gro | 10.98 | 9.98 | -9.11% | 3.4y | medium | 2d | 5.17% | 70.6 | ↓ widening | — |
| 2 | PSF | Prabhu Select Fund | 12.75 | 11.90 | -6.67% | 2.2y | high | 3d | 5.81% | 68.7 | → stable | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.66 | -8.52% | 2.3y | medium | 1d | 5.28% | 51.1 | ↓ widening | high_vol |
| 4 | NICSF | NIC Asia Select-30 | 10.04 | 9.40 | -6.37% | 2.3y | medium | 1d | 5.35% | 48.8 | ↓ widening | — |
| 5 | SEF | Siddhartha Equity Fund | 10.55 | 9.90 | -6.16% | 1.6y | medium | 1d | 4.98% | 46.7 | ↓ widening | high_vol |
| 6 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.98 | -4.68% | 3.2y | medium | 2d | 0.48% | 45.9 | ↓ widening | — |
| 7 | CMF2 | Citizens Mutual Fund - 2 | 10.62 | 10.13 | -4.61% | 0.3y | medium | 1d | 3.31% | 44.3 | ↓ widening | — |
| 8 | NICFC | NIC Asia Flexi Cap Fund | 10.09 | 9.36 | -7.23% | 3.2y | medium | 2d | 0.70% | 39.3 | ↓ widening | — |
| 9 | NICBF | NIC ASIA Balanced Fund | 10.03 | 9.39 | -6.38% | 3.4y | medium | 1d | -0.10% | 27.8 | ↓ widening | high_vol |

## IGNORE Summary

*32 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 4 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -16.58% | maturity:5.0y |
| LUK | -15.52% | maturity:4.4y |
| LVF2 | -12.36% | maturity:7.4y |
| SFEF | -11.55% | maturity:5.9y |
| NSIF2 | -11.23% | maturity:6.4y |
| KSY | -10.88% | liquidity:low; maturity:8.0y |
| GIBF1 | -10.58% | maturity:6.3y |
| RSY | -10.54% | maturity:9.1y |
| MBLEF | -10.12% | maturity:11.0y |
| NIBSF2 | -10.05% | maturity:5.2y |
| RMF2 | -9.49% | liquidity:low; maturity:7.1y |
| NIBLGF | -9.16% | liquidity:low; maturity:6.8y |
| NIBLSTF | -8.97% | maturity:9.9y |
| RBBF40 | -8.39% | liquidity:low; maturity:11.6y |
| SIGS3 | -8.28% | maturity:7.1y |
| H8020 | -8.27% | maturity:7.5y |
| C30MF | -8.18% | maturity:7.1y |
| PRSF | -8.09% | maturity:6.0y |
| MNMF1 | -7.92% | maturity:8.7y |
| NMBHF2 | -7.91% | maturity:8.9y |
| SAGF | -7.85% | liquidity:low; maturity:7.7y |
| GSY | -7.83% | maturity:8.8y |
| GBIMESY2 | -7.69% | liquidity:low; maturity:9.3y |
| SFMF | -7.08% | liquidity:low |
| SLCF | -6.60% | liquidity:low |
| KEF | -6.35% | maturity:5.0y |
| KDBY | -6.13% | maturity:6.3y |
| NICGF2 | -5.81% | liquidity:low; maturity:4.6y |
| NMB50 | -3.87% | valuation:small_discount |
| MMF1 | -3.45% | valuation:small_discount; maturity:5.4y |
| HLICF | -3.22% | valuation:small_discount; liquidity:low; maturity:9.5y |
| NBF3 | -3.20% | valuation:small_discount; maturity:5.5y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 14
- NAV data age: median 17 days, max 307 days

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
