# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-26 11:03*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-24 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 24 |
| Median Discount | -8.37% |
| CONSIDER | 7 |
| IGNORE | 34 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 22.0% |
| -10% to -6% | 21 | 51.2% |
| -6% to -4% | 5 | 12.2% |
| -4% to 0% | 3 | 7.3% |
| ≥ 0% (premium) | 3 | 7.3% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICSF | NIC Asia Select-30 | 10.04 | 9.20 | -8.37% | 2.2y | medium | 7d | 5.35% | 62.3 | ↓ widening | — |
| 2 | SFMF | Sunrise First Mutual Fund | 11.30 | 10.50 | -7.08% | 3.5y | medium | 1d | -2.04% | 54.0 | ↑ narrowing | — |
| 3 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.58 | -9.28% | 2.2y | high | 4d | 5.28% | 53.5 | ↓ widening | high_vol |
| 4 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.47 | -9.55% | 3.4y | medium | 4d | 4.39% | 52.2 | → stable | high_vol |
| 5 | SLCF | Sanima Large Cap Fund | 10.60 | 9.77 | -7.83% | 1.8y | medium | 12d | 4.43% | 51.8 | ↓ widening | — |
| 6 | SEF | Siddhartha Equity Fund | 10.55 | 9.90 | -6.16% | 1.5y | medium | 5d | 4.98% | 49.7 | ↓ widening | high_vol |
| 7 | NBF2 | Nabil Balanced Fund - 2 | 10.47 | 9.95 | -4.97% | 3.1y | medium | 1d | 0.48% | 44.9 | ↓ widening | — |

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
| LUK | -17.07% | liquidity:low; maturity:4.3y |
| SBCF | -14.90% | maturity:4.9y |
| NICGF2 | -13.59% | liquidity:low; maturity:4.6y |
| LVF2 | -13.58% | maturity:7.4y |
| NICFC | -12.55% | liquidity:low |
| MBLEF | -11.87% | maturity:10.9y |
| SFEF | -11.64% | liquidity:low; maturity:5.8y |
| RMF2 | -11.18% | maturity:7.1y |
| GBIMESY2 | -10.87% | liquidity:low; maturity:9.2y |
| NIBLSTF | -9.84% | maturity:9.8y |
| NSIF2 | -9.84% | maturity:6.4y |
| RSY | -9.83% | maturity:9.0y |
| NMBHF2 | -9.77% | maturity:8.8y |
| RBBF40 | -9.74% | maturity:11.6y |
| NIBSF2 | -9.56% | liquidity:low; maturity:5.1y |
| GIBF1 | -9.13% | maturity:6.3y |
| NIBLGF | -8.58% | maturity:6.7y |
| MNMF1 | -8.56% | maturity:8.7y |
| KSY | -8.28% | maturity:7.9y |
| SIGS2 | -8.20% | liquidity:low |
| C30MF | -8.18% | liquidity:low; maturity:7.1y |
| GSY | -7.83% | maturity:8.7y |
| SAGF | -7.39% | liquidity:low; maturity:7.6y |
| CMF2 | -6.78% | liquidity:low |
| MMF1 | -5.81% | maturity:5.4y |
| H8020 | -5.33% | maturity:7.4y |
| SIGS3 | -4.85% | maturity:7.0y |
| NBF3 | -4.07% | maturity:5.4y |
| HLICF | -3.53% | valuation:small_discount; maturity:9.4y |
| PSF | -3.53% | valuation:small_discount |
| NMB50 | -1.84% | valuation:small_discount |
| KDBY | 1.14% | valuation:premium; maturity:6.3y |
| PRSF | 1.85% | valuation:premium; maturity:5.9y |
| KEF | 2.94% | valuation:premium; maturity:4.9y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 22
- NAV data age: median 42 days, max 332 days

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
