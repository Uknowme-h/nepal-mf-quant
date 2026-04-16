# Nepal MF Quant — Full Analysis Report

*Generated: 2026-04-16 11:21*

## Market Overview

| Metric | Value |
|--------|-------|
| Analysis Date | 2026-04-16 |
| Funds Tracked | 41 |
| At Discount (price < NAV) | 38 |
| At Premium (price ≥ NAV) | 3 |
| Deep Discount (≤ -8%) | 18 |
| Median Discount | -7.41% |
| CONSIDER | 5 |
| IGNORE | 36 |

> ⚠️ **NAV Staleness Warning**: 7 fund(s) have NAV data older than 45 days. Discount calculations may be less reliable.

## Discount Distribution

| Discount Range | Count | % of Universe |
|---------------|-------|---------------|
| < -10% | 9 | 22.0% |
| -10% to -6% | 16 | 39.0% |
| -6% to -4% | 8 | 19.5% |
| -4% to 0% | 5 | 12.2% |
| ≥ 0% (premium) | 3 | 7.3% |

## CONSIDER Candidates

| # | Symbol | Name | NAV | LTP | Discount | Maturity | Liquidity | Streak | NAV Δ | Score | Trend | Risk |
|---|--------|------|-----|-----|----------|----------|-----------|--------|-------|-------|-------|------|
| 1 | NICSF | NIC Asia Select-30 | 10.04 | 9.45 | -5.88% | 2.2y | medium | 1d | 5.35% | 56.0 | → stable | — |
| 2 | RMF1 | RBB Mutual Fund 1 | 10.56 | 9.90 | -6.25% | 2.3y | medium | 11d | 5.28% | 52.9 | → stable | high_vol |
| 3 | SLCF | Sanima Large Cap Fund | 10.60 | 9.99 | -5.75% | 1.9y | high | 6d | 4.43% | 51.2 | ↓ widening | — |
| 4 | SEF | Siddhartha Equity Fund | 10.55 | 10.06 | -4.64% | 1.6y | medium | 1d | 4.98% | 48.0 | → stable | high_vol |
| 5 | NICBF | NIC ASIA Balanced Fund | 10.47 | 9.60 | -8.31% | 3.4y | medium | 2d | 4.39% | 42.8 | ↓ widening | high_vol |

## IGNORE Summary

*36 funds are flagged IGNORE. Top reasons:*

| Gate Failed | Count |
|-------------|-------|
| maturity | 29 |
| liquidity | 10 |
| valuation | 8 |

<details>
<summary>Full IGNORE list (click to expand)</summary>

| Symbol | Discount | Reason |
|--------|----------|--------|
| SBCF | -13.14% | maturity:5.0y |
| LVF2 | -13.06% | maturity:7.4y |
| LUK | -12.61% | maturity:4.3y |
| MBLEF | -11.34% | maturity:10.9y |
| SFEF | -11.29% | maturity:5.8y |
| NICFC | -11.03% | liquidity:low |
| NSIF2 | -10.98% | maturity:6.4y |
| KSY | -10.70% | liquidity:low; maturity:7.9y |
| NIBLSTF | -10.04% | maturity:9.8y |
| GIBF1 | -9.69% | maturity:6.3y |
| RMF2 | -9.49% | maturity:7.1y |
| NIBSF2 | -9.46% | maturity:5.1y |
| RBBF40 | -9.06% | liquidity:low; maturity:11.6y |
| MNMF1 | -8.84% | maturity:8.7y |
| GBIMESY2 | -8.65% | maturity:9.3y |
| RSY | -8.59% | maturity:9.1y |
| GSY | -8.11% | maturity:8.7y |
| NMBHF2 | -7.91% | maturity:8.9y |
| SFMF | -7.52% | liquidity:low |
| NIBLGF | -7.41% | maturity:6.8y |
| SAGF | -6.93% | liquidity:low; maturity:7.6y |
| NICGF2 | -6.75% | maturity:4.6y |
| C30MF | -6.36% | maturity:7.1y |
| H8020 | -5.41% | maturity:7.5y |
| SIGS2 | -4.83% | liquidity:low |
| NBF2 | -4.68% | liquidity:low |
| SIGS3 | -4.05% | maturity:7.0y |
| NMB50 | -4.05% | liquidity:low |
| MMF1 | -3.94% | valuation:small_discount; maturity:5.4y |
| NBF3 | -3.59% | valuation:small_discount; maturity:5.4y |
| CMF2 | -3.39% | valuation:small_discount; liquidity:low |
| HLICF | -2.70% | valuation:small_discount; liquidity:low; maturity:9.4y |
| PSF | -2.67% | valuation:small_discount |
| PRSF | 1.08% | valuation:premium; maturity:5.9y |
| KDBY | 2.10% | valuation:premium; maturity:6.3y |
| KEF | 3.32% | valuation:premium; maturity:4.9y |

</details>

## Data Quality

- Symbols checked: 43
- Symbols with issues: 17
- NAV data age: median 32 days, max 322 days

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
