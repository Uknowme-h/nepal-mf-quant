"""
Dividend History Scraper for Nepal Closed-End Mutual Funds

Scrapes dividend history from two sources:
  1. ShareSansar  (primary)   — company detail page dividend table
  2. Merolagani   (fallback)  — CompanyDetail page dividend history section

For each fund, collects:
  fiscal_year, dividend_type, dividend_rate_pct, record_date,
  payment_date, source, scraped_at

Storage pattern mirrors data/raw/nav/:
  - data/raw/dividends/{SYMBOL}.csv  — per-fund history
  - data/raw/dividend_history.csv    — consolidated all-fund file

Design:
  - Idempotent: identifies records by (symbol, fiscal_year, dividend_type);
    only appends rows that are not already present.
  - Graceful degradation: network failures are logged and skipped.
  - Runs on monthly cadence (dividend events are infrequent).

Usage:
  python src/scrape/dividend_scraper.py                  # incremental update
  python src/scrape/dividend_scraper.py --full-history   # re-fetch all history
"""

import argparse
import csv
import logging
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SHARESANSAR_BASE = "https://www.sharesansar.com"
MEROLAGANI_BASE = "https://merolagani.com"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
}

JSON_HEADERS = {
    **HEADERS,
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
}

CSV_FIELDNAMES = [
    "fiscal_year",
    "dividend_type",
    "dividend_rate_pct",
    "record_date",
    "payment_date",
    "source",
    "scraped_at",
]

REQUEST_DELAY = 0.5  # seconds between requests to be polite


# ---------------------------------------------------------------------------
# ShareSansar scraper
# ---------------------------------------------------------------------------

def _fetch_sharesansar_dividends(symbol: str) -> List[Dict]:
    """
    Fetch dividend history for *symbol* from ShareSansar company page.

    ShareSansar embeds a dividend table in the company detail HTML at
    https://www.sharesansar.com/company/{symbol}

    Returns a list of normalised dividend records (may be empty).
    """
    url = f"{SHARESANSAR_BASE}/company/{symbol.lower()}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=20)
        if resp.status_code == 404:
            logger.debug("%s: ShareSansar 404 — symbol not found", symbol)
            return []
        resp.raise_for_status()
    except requests.RequestException as exc:
        logger.warning("%s: ShareSansar request failed: %s", symbol, exc)
        return []

    return _parse_sharesansar_dividend_html(resp.text, symbol)


def _parse_sharesansar_dividend_html(html: str, symbol: str) -> List[Dict]:
    """Parse dividend rows from ShareSansar company page HTML."""
    soup = BeautifulSoup(html, "lxml")
    records: List[Dict] = []
    now = datetime.utcnow().isoformat()

    # ShareSansar dividend table has class "table" inside a div with
    # id or heading that contains "Dividend"
    dividend_table = None

    # Strategy 1: look for a section heading containing "Dividend"
    for heading in soup.find_all(["h3", "h4", "h5", "div"], class_=re.compile(r"title|heading|panel", re.I)):
        if "dividend" in heading.get_text(strip=True).lower():
            parent = heading.find_parent(["div", "section"])
            if parent:
                dividend_table = parent.find("table")
                if dividend_table:
                    break

    # Strategy 2: any table whose headers mention "dividend" or "fiscal"
    if dividend_table is None:
        for table in soup.find_all("table"):
            headers_text = table.get_text(" ", strip=True).lower()
            if "dividend" in headers_text or "fiscal" in headers_text:
                dividend_table = table
                break

    if dividend_table is None:
        logger.debug("%s: No dividend table found on ShareSansar page", symbol)
        return []

    rows = dividend_table.find_all("tr")
    if not rows:
        return []

    # Extract header names
    header_row = rows[0]
    headers = [th.get_text(strip=True).lower() for th in header_row.find_all(["th", "td"])]

    for row in rows[1:]:
        cells = [td.get_text(strip=True) for td in row.find_all(["td", "th"])]
        if not cells or len(cells) < 2:
            continue

        record = _extract_dividend_record(headers, cells, "sharesansar", now)
        if record:
            records.append(record)

    logger.debug("%s: ShareSansar — parsed %d dividend records", symbol, len(records))
    return records


# ---------------------------------------------------------------------------
# Merolagani scraper (fallback)
# ---------------------------------------------------------------------------

def _fetch_merolagani_dividends(symbol: str) -> List[Dict]:
    """
    Fetch dividend history for *symbol* from Merolagani company detail page.

    URL: https://merolagani.com/CompanyDetail.aspx?companySymbol={symbol}

    Returns a list of normalised dividend records (may be empty).
    """
    url = f"{MEROLAGANI_BASE}/CompanyDetail.aspx?companySymbol={symbol}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=20)
        if resp.status_code == 404:
            logger.debug("%s: Merolagani 404 — symbol not found", symbol)
            return []
        resp.raise_for_status()
    except requests.RequestException as exc:
        logger.warning("%s: Merolagani request failed: %s", symbol, exc)
        return []

    return _parse_merolagani_dividend_html(resp.text, symbol)


def _parse_merolagani_dividend_html(html: str, symbol: str) -> List[Dict]:
    """Parse dividend rows from Merolagani company page HTML."""
    soup = BeautifulSoup(html, "lxml")
    records: List[Dict] = []
    now = datetime.utcnow().isoformat()

    # Merolagani has a table with id containing "Dividend" or "dividend"
    dividend_table = None

    for table in soup.find_all("table"):
        table_id = table.get("id", "").lower()
        table_class = " ".join(table.get("class", [])).lower()
        surrounding_text = ""
        parent = table.parent
        if parent:
            heading = parent.find(["h3", "h4", "h5", "label", "span"])
            if heading:
                surrounding_text = heading.get_text(strip=True).lower()

        if (
            "dividend" in table_id
            or "dividend" in table_class
            or "dividend" in surrounding_text
        ):
            dividend_table = table
            break

    # Fallback: table whose header row mentions "dividend"
    if dividend_table is None:
        for table in soup.find_all("table"):
            header_text = ""
            first_row = table.find("tr")
            if first_row:
                header_text = first_row.get_text(" ", strip=True).lower()
            if "dividend" in header_text or "bonus" in header_text:
                dividend_table = table
                break

    if dividend_table is None:
        logger.debug("%s: No dividend table found on Merolagani page", symbol)
        return []

    rows = dividend_table.find_all("tr")
    if not rows:
        return []

    header_row = rows[0]
    headers = [th.get_text(strip=True).lower() for th in header_row.find_all(["th", "td"])]

    for row in rows[1:]:
        cells = [td.get_text(strip=True) for td in row.find_all(["td", "th"])]
        if not cells or len(cells) < 2:
            continue

        record = _extract_dividend_record(headers, cells, "merolagani", now)
        if record:
            records.append(record)

    logger.debug("%s: Merolagani — parsed %d dividend records", symbol, len(records))
    return records


# ---------------------------------------------------------------------------
# Record normalisation
# ---------------------------------------------------------------------------

def _extract_dividend_record(
    headers: List[str],
    cells: List[str],
    source: str,
    scraped_at: str,
) -> Optional[Dict]:
    """
    Map raw table cells to a normalised dividend record dict.

    Handles varying column orders from different pages by matching
    header keywords rather than relying on fixed column indices.
    """
    data = dict(zip(headers, cells))

    # ---- fiscal year ----
    fiscal_year = _find_field(data, ["fiscal year", "year", "f.y.", "fy"])
    if not fiscal_year:
        # If first cell looks like a year, use it
        if cells and re.match(r"^\d{4}", cells[0]):
            fiscal_year = cells[0]
    if not fiscal_year:
        return None

    # ---- dividend type ----
    # Merolagani / ShareSansar separate bonus, right, and cash columns
    dividend_type = "cash"  # default
    rate_pct = None

    # Try explicit type column
    dtype_raw = _find_field(data, ["type", "dividend type"])
    if dtype_raw:
        dtype_lower = dtype_raw.lower()
        if "bonus" in dtype_lower:
            dividend_type = "bonus"
        elif "right" in dtype_lower:
            dividend_type = "right"
        else:
            dividend_type = "cash"

    # ---- dividend rate (%) ----
    # Try cash dividend column first
    rate_raw = _find_field(data, [
        "cash dividend", "cash(%)", "cash (%)", "cash",
        "dividend rate", "dividend(%)", "dividend (%)",
        "rate(%)", "rate (%)", "rate", "amount",
    ])
    if rate_raw:
        rate_pct = _parse_pct(rate_raw)

    # If rate is still None, check bonus or right columns
    if rate_pct is None:
        bonus_raw = _find_field(data, ["bonus(%)", "bonus (%)", "bonus share", "bonus"])
        if bonus_raw:
            val = _parse_pct(bonus_raw)
            if val and val > 0:
                dividend_type = "bonus"
                rate_pct = val

    if rate_pct is None:
        right_raw = _find_field(data, ["right(%)", "right (%)", "right share", "right"])
        if right_raw:
            val = _parse_pct(right_raw)
            if val and val > 0:
                dividend_type = "right"
                rate_pct = val

    # Skip rows with no dividend rate
    if rate_pct is None or rate_pct == 0:
        return None

    # ---- dates ----
    record_date = _find_field(data, [
        "book close date", "book close", "record date", "record",
        "closing date", "close date",
    ])
    payment_date = _find_field(data, [
        "payment date", "payment", "distributed date", "distribute date",
    ])

    record_date = _normalise_date(record_date)
    payment_date = _normalise_date(payment_date)

    return {
        "fiscal_year": fiscal_year.strip(),
        "dividend_type": dividend_type,
        "dividend_rate_pct": round(float(rate_pct), 4),
        "record_date": record_date or "",
        "payment_date": payment_date or "",
        "source": source,
        "scraped_at": scraped_at,
    }


def _find_field(data: Dict[str, str], keywords: List[str]) -> Optional[str]:
    """Return the first dict value whose key contains any of the keywords."""
    for key, val in data.items():
        key_lower = key.lower().strip()
        for kw in keywords:
            if kw in key_lower:
                val = val.strip()
                if val and val not in ("-", "—", "N/A", "n/a", ""):
                    return val
    return None


def _parse_pct(raw: str) -> Optional[float]:
    """
    Extract a numeric percentage from a raw string.
    Handles formats like "10%", "10.00", "10.00%", "10.00 %", "-".
    Returns None if unparseable or zero-valued strings like "-".
    """
    if not raw or raw.strip() in ("-", "—", "", "N/A", "n/a", "0", "0.00", "0%"):
        return None
    # Remove % and whitespace, keep digits and decimal point
    cleaned = re.sub(r"[^\d.]", "", raw.strip())
    try:
        val = float(cleaned)
        return val if val > 0 else None
    except ValueError:
        return None


def _normalise_date(raw: Optional[str]) -> Optional[str]:
    """
    Try to parse a date string into ISO format (YYYY-MM-DD).
    Returns None if parsing fails.
    """
    if not raw or raw.strip() in ("-", "—", "", "N/A"):
        return None

    raw = raw.strip()

    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%d %b %Y",
        "%b %d, %Y",
        "%B %d, %Y",
    ]
    for fmt in formats:
        try:
            return datetime.strptime(raw, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None


# ---------------------------------------------------------------------------
# Per-fund CSV persistence
# ---------------------------------------------------------------------------

def _load_existing_records(csv_path: Path) -> List[Dict]:
    """Load existing dividend records from a per-fund CSV file."""
    if not csv_path.exists():
        return []
    try:
        with open(csv_path, "r", encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))
    except Exception as exc:
        logger.warning("Could not read %s: %s", csv_path, exc)
        return []


def _record_key(record: Dict) -> tuple:
    """Composite key used for deduplication."""
    return (
        record.get("fiscal_year", "").strip(),
        record.get("dividend_type", "").strip(),
    )


def _save_fund_dividends(symbol: str, new_records: List[Dict], div_dir: Path) -> int:
    """
    Idempotent save: append only records not already present.

    Returns the count of newly added rows.
    """
    div_dir.mkdir(parents=True, exist_ok=True)
    csv_path = div_dir / f"{symbol}.csv"

    existing = _load_existing_records(csv_path)
    existing_keys = {_record_key(r) for r in existing}

    added = []
    for rec in new_records:
        if _record_key(rec) not in existing_keys:
            added.append(rec)
            existing_keys.add(_record_key(rec))

    if not added:
        return 0

    all_records = existing + added
    # Sort by fiscal_year descending for readability
    all_records.sort(key=lambda r: r.get("fiscal_year", ""), reverse=True)

    try:
        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDNAMES)
            writer.writeheader()
            writer.writerows(all_records)
    except Exception as exc:
        logger.error("Could not write %s: %s", csv_path, exc)
        return 0

    return len(added)


def _build_consolidated_file(symbols: List[str], div_dir: Path, output_path: Path) -> None:
    """
    Re-build the consolidated dividend_history.csv from per-fund files.
    Adds a 'symbol' column at the front.
    """
    all_rows: List[Dict] = []
    for symbol in symbols:
        csv_path = div_dir / f"{symbol}.csv"
        for rec in _load_existing_records(csv_path):
            all_rows.append({"symbol": symbol, **rec})

    all_rows.sort(key=lambda r: (r.get("symbol", ""), r.get("fiscal_year", "")))

    try:
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["symbol"] + CSV_FIELDNAMES)
            writer.writeheader()
            writer.writerows(all_rows)
        logger.info("Consolidated dividend history: %d records → %s", len(all_rows), output_path)
    except Exception as exc:
        logger.error("Could not write consolidated file: %s", exc)


# ---------------------------------------------------------------------------
# Main scraping entry point
# ---------------------------------------------------------------------------

def scrape_fund_dividends(symbol: str) -> List[Dict]:
    """
    Fetch dividend history for *symbol* using ShareSansar (primary) and
    Merolagani (fallback). Returns deduplicated list of normalised records.
    """
    records: List[Dict] = []

    # --- Primary: ShareSansar ---
    ss_records = _fetch_sharesansar_dividends(symbol)
    if ss_records:
        records.extend(ss_records)
        logger.info("%s: %d records from ShareSansar", symbol, len(ss_records))
    else:
        logger.debug("%s: ShareSansar returned 0 records — trying Merolagani", symbol)

    # --- Fallback: Merolagani (always run to supplement) ---
    time.sleep(REQUEST_DELAY)
    ml_records = _fetch_merolagani_dividends(symbol)
    if ml_records:
        # Merge Merolagani records that aren't already covered by ShareSansar
        existing_keys = {_record_key(r) for r in records}
        for rec in ml_records:
            if _record_key(rec) not in existing_keys:
                records.append(rec)
                existing_keys.add(_record_key(rec))
        logger.info("%s: %d unique records after Merolagani merge", symbol, len(records))

    return records


def run(project_root: Path, full_history: bool = False) -> Dict[str, int]:
    """
    Main entry point for pipeline integration.

    Scrapes dividend history for all funds in fund_universe.csv.
    Saves per-fund CSVs and a consolidated file.

    Args:
        project_root: Project root directory.
        full_history:  If True, re-fetches and merges all available records.
                       If False, only adds records not already on disk.

    Returns:
        Dict mapping symbol -> number of newly added records.
    """
    logger.info("=" * 60)
    logger.info("Dividend History Scraper")
    logger.info("=" * 60)

    universe_path = project_root / "data" / "raw" / "fund_universe.csv"
    div_dir = project_root / "data" / "raw" / "dividends"
    consolidated_path = project_root / "data" / "raw" / "dividend_history.csv"

    if not universe_path.exists():
        raise FileNotFoundError(
            f"Fund universe not found: {universe_path}. Run step 1 first."
        )

    # Load symbols
    symbols: List[str] = []
    try:
        with open(universe_path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                sym = row.get("symbol", "").strip()
                if sym:
                    symbols.append(sym)
    except Exception as exc:
        raise RuntimeError(f"Could not load fund universe: {exc}") from exc

    logger.info("Scraping dividends for %d funds...", len(symbols))

    stats: Dict[str, int] = {}
    for idx, symbol in enumerate(symbols, 1):
        logger.info("[%d/%d] %s", idx, len(symbols), symbol)
        try:
            records = scrape_fund_dividends(symbol)
            if records:
                added = _save_fund_dividends(symbol, records, div_dir)
                stats[symbol] = added
                if added:
                    logger.info("  ✓ %s: %d new records saved", symbol, added)
                else:
                    logger.debug("  %s: no new records (all already present)", symbol)
            else:
                stats[symbol] = 0
                logger.debug("  %s: no dividend data found", symbol)
        except Exception as exc:
            logger.error("  %s: unexpected error: %s", symbol, exc)
            stats[symbol] = 0
        # Polite delay between funds
        time.sleep(REQUEST_DELAY)

    # Rebuild consolidated file
    _build_consolidated_file(symbols, div_dir, consolidated_path)

    total_added = sum(stats.values())
    funds_with_data = sum(1 for v in stats.values() if v > 0)
    logger.info("=" * 60)
    logger.info(
        "Summary: %d new records across %d funds (%d funds with existing data)",
        total_added,
        funds_with_data,
        sum(1 for sym in symbols if (div_dir / f"{sym}.csv").exists()),
    )
    logger.info("=" * 60)

    return stats


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Scrape dividend history for Nepal closed-end mutual funds."
    )
    parser.add_argument(
        "--full-history",
        action="store_true",
        help="Re-fetch all available historical records (default: incremental only)",
    )
    args = parser.parse_args()

    project_root = Path(__file__).parent.parent.parent
    run(project_root, full_history=args.full_history)


if __name__ == "__main__":
    main()
