# Nepal Mutual Fund Quantitative Analysis - Project Structure

## 📁 Complete Directory Tree

```
nepal-mf-quant/
│
├── .github/
│   └── workflows/
│       └── scheduled.yml              # GitHub Actions automation config
│
├── data/
│   ├── raw/                           # Raw scraped data (source of truth)
│   │   ├── nav/                       # Individual NAV files per fund
│   │   │   ├── C30MF.csv             # NAV history for C30MF fund
│   │   │   ├── NBF2.csv              # NAV history for NBF2 fund
│   │   │   └── ... (41 files total)  # One CSV per fund
│   │   ├── fund_universe.csv         # Fund metadata (symbol, name, maturity, size)
│   │   ├── market_prices.csv         # Daily OHLC prices from NEPSE
│   │   └── nav_data_*.csv            # Legacy consolidated NAV file (not used)
│   │
│   ├── processed/                     # Analytical outputs
│   │   ├── mf_daily_snapshot.csv     # All funds: NAV + prices + discount
│   │   ├── mf_decision_table.csv     # Today's screening decisions
│   │   └── mf_ranked_today.csv       # Top 10 ranked by discount + liquidity
│   │
│   ├── history/                       # Temporal tracking
│   │   └── mf_decision_history.csv   # Append-only decision log (all days)
│   │
│   ├── metrics/                       # Performance metrics (legacy)
│   └── reference/                     # Reference data
│
├── scrapers/                          # Data collection scripts
│   ├── market/
│   │   └── daily_price_scraper.py    # NEPSE market data scraper (Playwright)
│   │
│   └── mappings/
│       └── build_symbol_nepse_map.py # Generate symbol→security_id mapping
│
├── src/                               # Core analytics pipeline
│   ├── scrape/                        # Fund metadata scrapers
│   │   ├── fund_universe.py          # Scrape fund list from ShareSansar
│   │   ├── nav_scraper.py            # Scrape NAV data (monthly)
│   │   └── fund_metadata.py          # Extract fund details
│   │
│   ├── analytics/                     # Valuation & decision logic
│   │   ├── valuation.py              # NAV-price join + discount calculation
│   │   ├── decision_layer.py         # Rule-based screening system
│   │   ├── decision_history.py       # Append to history (temporal tracking)
│   │   ├── update_readme.py          # Auto-update README dashboard
│   │   ├── returns.py                # Returns calculation (legacy)
│   │   ├── risk.py                   # Risk metrics (legacy)
│   │   └── scoring.py                # Fund scoring (legacy)
│   │
│   └── pipeline.py                    # End-to-end orchestration script
│
├── reports/                           # Generated reports (legacy)
│   ├── latest_rankings.md            # Markdown fund rankings
│   └── metrics_table.csv             # Metrics CSV export
│
├── README.md                          # Project documentation + auto-updated dashboard
├── requirements.txt                   # Python dependencies
└── venv/                              # Python virtual environment
```

---

## 📄 File-by-File Description

### 🔧 Configuration & Setup

#### `.github/workflows/scheduled.yml`
**Purpose**: GitHub Actions workflow for daily automation  
**What it does**: Runs screening pipeline on schedule (4:00 PM NST, Mon-Fri)  
**Triggers**: 
- Cron schedule (daily market close)
- Manual workflow dispatch
**Actions**:
1. Setup Python environment
2. Install dependencies
3. Run scraping → analytics → history → README update
4. Commit and push results

#### `requirements.txt`
**Purpose**: Python package dependencies  
**Contains**:
- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `playwright` - Browser automation
- `lxml` - XML/HTML processing

---

### 📊 Data Files (Inputs)

#### `data/raw/nav/*.csv` (41 files)
**Purpose**: Individual NAV history per fund  
**Format**: `date, nav, source`  
**Example**: `C30MF.csv` contains NAV timeline for C30MF fund  
**Source**: Scraped from ShareSansar monthly statements  
**Usage**: Loaded by `valuation.py` to calculate discounts

#### `data/raw/fund_universe.csv`
**Purpose**: Master list of all closed-end mutual funds  
**Columns**: `id, symbol, name, maturity_date, fund_size, type, source, scraped_at`  
**Source**: Scraped from ShareSansar API  
**Created by**: `src/scrape/fund_universe.py`  
**Usage**: Provides metadata for decision analysis

#### `data/raw/market_prices.csv`
**Purpose**: Daily market prices (OHLC) from NEPSE  
**Columns**: `date, symbol, ltp, open, high, low, volume, trades, source`  
**Source**: Scraped from NEPSE website via Playwright  
**Created by**: `scrapers/market/daily_price_scraper.py`  
**Usage**: Joined with NAV data for discount calculation

---

### 📈 Data Files (Outputs)

#### `data/processed/mf_daily_snapshot.csv`
**Purpose**: Complete valuation snapshot for all funds today  
**Columns**: `date, symbol, nav, ltp, discount_pct, volume, trades, source`  
**Created by**: `src/analytics/valuation.py`  
**Usage**: Input to decision layer  
**Example row**: `2026-02-09, NBF2, 10.42, 9.72, -6.72, 105890, 450, NEPSE`

#### `data/processed/mf_decision_table.csv`
**Purpose**: Today's screening decisions with classifications  
**Columns**: `date, symbol, nav, ltp, discount_pct, volume, years_to_maturity, days_to_maturity, valuation_bucket, liquidity_bucket, decision_flag`  
**Created by**: `src/analytics/decision_layer.py`  
**Usage**: Input to history tracker and README updater  
**Key field**: `decision_flag` = CONSIDER or IGNORE

#### `data/processed/mf_ranked_today.csv`
**Purpose**: Top 10 funds ranked by discount + liquidity  
**Created by**: `src/analytics/valuation.py`  
**Usage**: Quick reference for best opportunities

#### `data/history/mf_decision_history.csv`
**Purpose**: Append-only temporal log of all decisions  
**Columns**: `date, symbol, discount_pct, days_to_maturity, liquidity_bucket, decision_flag`  
**Created by**: `src/analytics/decision_history.py`  
**Properties**: Idempotent, never overwrites, grows daily  
**Usage**: Track decision persistence, calculate CONSIDER streaks

---

### 🤖 Scraper Scripts

#### `scrapers/market/daily_price_scraper.py`
**Purpose**: Scrape daily market prices from NEPSE  
**Technology**: Playwright (headless browser automation)  
**Method**: Network interception of `/api/nots/security/{id}` JSON responses  
**Why Playwright?**: NEPSE is Angular SPA (no server-side HTML)  
**Output**: Appends to `data/raw/market_prices.csv`  
**Runtime**: ~2 minutes for 41 funds  
**Success rate**: 100% (with retry logic)

#### `scrapers/mappings/build_symbol_nepse_map.py`
**Purpose**: Generate mapping from fund symbol → NEPSE security_id  
**Why needed?**: NEPSE API requires numeric security_id, not symbol  
**Output**: `symbol_nepse_map.csv` (used by price scraper)  
**Run frequency**: One-time or when new funds added

#### `src/scrape/fund_universe.py`
**Purpose**: Scrape comprehensive fund metadata  
**Source**: ShareSansar DataTables API  
**Output**: `data/raw/fund_universe.csv`  
**Key fields extracted**: maturity_date, fund_size  
**Run frequency**: Weekly (metadata changes slowly)

#### `src/scrape/nav_scraper.py`
**Purpose**: Scrape monthly NAV data per fund  
**Source**: ShareSansar mutual fund NAV endpoint  
**Output**: Individual CSV files in `data/raw/nav/`  
**Run frequency**: Monthly (after fund disclosures)

---

### 📐 Analytics Scripts

#### `src/analytics/valuation.py`
**Purpose**: Calculate NAV-to-market-price discounts  
**Process**:
1. Load individual NAV files from `data/raw/nav/`
2. Load market prices from `data/raw/market_prices.csv`
3. Perform as-of join (point-in-time correct)
4. Calculate `discount_pct = (ltp - nav) / nav * 100`
5. Apply liquidity filter (volume >= median)
6. Rank by discount (most negative first)

**Outputs**:
- `mf_daily_snapshot.csv` - All 41 funds
- `mf_ranked_today.csv` - Top 10 ranked

**Key Innovation**: As-of join prevents look-ahead bias (uses NAV from on/before price date)

#### `src/analytics/decision_layer.py`
**Purpose**: Rule-based investment screening system  
**Decision Logic**:
```
CONSIDER if ALL of:
1. Valuation: discount_pct <= -4% (deep or moderate discount)
2. Liquidity: NOT in bottom 25% volume (tradable)
3. Maturity: <= 4 years (reasonable horizon)

Otherwise: IGNORE
```

**Classifications**:
- **Valuation buckets**: deep_discount, moderate_discount, small_discount, premium
- **Liquidity buckets**: high (top 25%), medium (middle 50%), low (bottom 25%)

**Output**: `data/processed/mf_decision_table.csv`

**Philosophy**: Deterministic, no prediction, research-only

#### `src/analytics/decision_history.py`
**Purpose**: Maintain append-only temporal decision log  
**Process**:
1. Load today's decision table
2. Load existing history (if exists)
3. Identify new records via composite key: `(date, symbol)`
4. Append only new records (idempotency)
5. Calculate CONSIDER streaks (inspection only)

**Output**: `data/history/mf_decision_history.csv`

**Properties**:
- Append-only (never overwrites)
- Idempotent (safe to run multiple times per day)
- No historical mutation

**Persistence Metrics**: Calculates consecutive CONSIDER days per fund

#### `src/analytics/update_readme.py`
**Purpose**: Auto-update README with current screening results  
**Process**:
1. Load decision history
2. Calculate summary stats (CONSIDER counts, streaks)
3. Generate markdown table sorted by streak + discount
4. Replace section between HTML markers in README

**Section Updated**: `## 📊 Daily Mutual Fund Decision Summary`

**Properties**:
- Only modifies marked section (`<!-- AUTO-GENERATED-START/END -->`)
- Preserves all other README content
- Idempotent (running multiple times = same result)

---

### 🏗️ Legacy/Placeholder Scripts

#### `src/analytics/returns.py`
**Status**: Legacy (not currently used)  
**Original purpose**: Calculate fund returns  
**Future use**: Backtesting, performance analysis

#### `src/analytics/risk.py`
**Status**: Legacy (not currently used)  
**Original purpose**: Risk metrics (volatility, Sharpe ratio)  
**Future use**: Risk-adjusted rankings

#### `src/analytics/scoring.py`
**Status**: Legacy (not currently used)  
**Original purpose**: Composite fund scoring  
**Future use**: Multi-factor rankings

#### `src/pipeline.py`
**Status**: Orchestration script (can be updated)  
**Purpose**: Run complete pipeline end-to-end  
**Usage**: Single entry point for full analysis

---

## 🔄 Complete Pipeline Flow

### Daily Execution Sequence

```bash
# 1. Scrape market prices (Playwright)
python scrapers/market/daily_price_scraper.py
# Output: data/raw/market_prices.csv (appended)

# 2. Calculate valuations (NAV-price join)
python src/analytics/valuation.py
# Outputs:
#   - data/processed/mf_daily_snapshot.csv
#   - data/processed/mf_ranked_today.csv

# 3. Apply decision rules
python src/analytics/decision_layer.py
# Output: data/processed/mf_decision_table.csv

# 4. Append to history (temporal tracking)
python src/analytics/decision_history.py
# Output: data/history/mf_decision_history.csv (appended)

# 5. Update README dashboard
python src/analytics/update_readme.py
# Output: README.md (section updated)
```

### Weekly/Monthly Tasks

```bash
# Scrape fund metadata (weekly)
python src/scrape/fund_universe.py
# Output: data/raw/fund_universe.csv

# Scrape NAV data (monthly, after fund disclosures)
python src/scrape/nav_scraper.py
# Output: data/raw/nav/*.csv (individual files updated)
```

### One-Time Setup

```bash
# Generate symbol mapping (once, or when funds change)
python scrapers/mappings/build_symbol_nepse_map.py
# Output: scrapers/mappings/symbol_nepse_map.csv
```

---

## 🎯 Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        DATA SOURCES                              │
├─────────────────┬───────────────────┬───────────────────────────┤
│  ShareSansar    │      NEPSE        │   ShareSansar             │
│  (NAV Data)     │  (Market Prices)  │  (Fund Metadata)          │
└────────┬────────┴──────────┬────────┴────────────┬──────────────┘
         │                   │                     │
         ▼                   ▼                     ▼
    nav_scraper.py    daily_price_      fund_universe.py
                      scraper.py
         │                   │                     │
         ▼                   ▼                     ▼
   data/raw/nav/    data/raw/          data/raw/
   *.csv            market_prices.csv  fund_universe.csv
         │                   │                     │
         └───────┬───────────┴──────────┬──────────┘
                 │                      │
                 ▼                      ▼
           valuation.py         (metadata joins)
                 │
                 ▼
       mf_daily_snapshot.csv
                 │
                 ▼
         decision_layer.py
                 │
                 ▼
       mf_decision_table.csv
                 │
                 ▼
      decision_history.py
                 │
                 ▼
    mf_decision_history.csv
                 │
                 ▼
        update_readme.py
                 │
                 ▼
            README.md
          (auto-updated)
```

---

## 🔑 Key Design Decisions

### 1. Individual NAV Files
**Decision**: Store NAV data in separate CSV files per fund  
**Why**: 
- Cleaner data model (one file = one fund)
- Easier debugging (inspect single fund)
- Prevents data loss (corruption isolated)
**Files**: `data/raw/nav/*.csv`

### 2. As-Of Join
**Decision**: Use `pd.merge_asof()` with `direction='backward'`  
**Why**: Point-in-time correctness (prevents look-ahead bias)  
**Implementation**: `valuation.py` line 87

### 3. Append-Only History
**Decision**: Never overwrite historical decision records  
**Why**: 
- Audit trail (reproducible)
- Persistence analysis (track streaks)
- No data loss on re-runs
**Implementation**: `decision_history.py` (idempotency checks)

### 4. Playwright for NEPSE
**Decision**: Use Playwright instead of requests + BeautifulSoup  
**Why**: NEPSE is Angular SPA (no server-side HTML)  
**Method**: Network interception of API responses  
**Implementation**: `daily_price_scraper.py`

### 5. Percentile-Based Liquidity
**Decision**: Liquidity buckets based on volume percentiles (not absolute thresholds)  
**Why**: Adapts to changing market conditions  
**Implementation**: `decision_layer.py` (P25, P75 thresholds)

### 6. HTML Comment Markers
**Decision**: Use `<!-- AUTO-GENERATED-START/END -->` in README  
**Why**: Precise section detection + preservation of manual edits  
**Implementation**: `update_readme.py`

---

## 🚀 Quick Start Commands

```bash
# Setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium

# Run daily pipeline (in order)
python scrapers/market/daily_price_scraper.py
python src/analytics/valuation.py
python src/analytics/decision_layer.py
python src/analytics/decision_history.py
python src/analytics/update_readme.py

# View results
cat data/processed/mf_decision_table.csv | grep CONSIDER
cat data/history/mf_decision_history.csv | tail -20
```

---

## 📊 File Size Reference

| File | Size | Growth |
|------|------|--------|
| `market_prices.csv` | ~50KB | ~1KB/day |
| `fund_universe.csv` | ~5KB | Static |
| `nav/*.csv` (each) | ~2KB | ~50B/month |
| `mf_daily_snapshot.csv` | ~3KB | Replaced daily |
| `mf_decision_table.csv` | ~4KB | Replaced daily |
| `mf_decision_history.csv` | ~2KB | ~50B/day (~18KB/year) |

**Total data directory**: ~200KB today → ~300KB after 1 year

---

## 🎓 System Philosophy

1. **Deterministic**: Same input → same output (no randomness)
2. **Idempotent**: Safe to re-run (no duplicates, no side effects)
3. **Append-only**: History never modified (audit trail)
4. **Research-only**: No prediction, no investment advice
5. **Transparent**: Clear logging, readable code, documented decisions

---

**Last Updated**: February 10, 2026  
**Total Files**: 50+ (excluding venv)  
**Lines of Code**: ~2,500  
**Dependencies**: 6 core packages
