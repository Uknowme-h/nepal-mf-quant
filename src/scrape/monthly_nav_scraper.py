"""
Monthly NAV Scraper — Direct Provider APIs

Fetches historical monthly NAV data from 7 fund management company
websites, converts Bikram Sambat dates to AD, and writes per-symbol
CSVs compatible with the existing data/raw/nav/{SYMBOL}.csv format.

Providers:
    Laxmi Capital          — LUK, LVF2, SFEF, SFMF, SBCF
    NMB Capital            — NMB50, NSIF2, NMBHF2
    NIC Asia Capital       — NICBF, NICFC, NICGF2
    Nabil Investment       — NBF2, NBF3
    Kumari Capital         — KSY
    Prabhu Capital         — PRSF, PSF
    Sanima Capital         — SAGF

Output: data/raw/nav/{SYMBOL}.csv  (columns: date, nav, source)
"""

from __future__ import annotations

import asyncio
import csv
import logging
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import httpx
import pandas as pd

try:
    import nepali_datetime
    HAS_NEPALI_DATETIME = True
except ImportError:
    HAS_NEPALI_DATETIME = False

logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------
# BS date helpers
# -----------------------------------------------------------------------

_BS_MONTH_NAMES: Dict[str, int] = {
    "baisakh": 1,   "baishakh": 1,  "baishak": 1,   "baisakha": 1,
    "jestha": 2,    "jeth": 2,      "jesth": 2,
    "ashadh": 3,    "asar": 3,      "ashad": 3,     "ashar": 3,
    "shrawan": 4,   "sawan": 4,     "shravan": 4,   "shrawn": 4,
    "bhadra": 5,    "bhadau": 5,    "bhado": 5,
    "ashwin": 6,    "asoj": 6,      "ashoj": 6,
    "kartik": 7,    "kartick": 7,
    "mangsir": 8,   "mangshir": 8,  "marga": 8,
    "poush": 9,     "paush": 9,     "push": 9,
    "magh": 10,     "magha": 10,
    "falgun": 11,   "phalgun": 11,  "fagun": 11,
    "chaitra": 12,  "chait": 12,    "chaita": 12,
}

_BS_MONTH_OFFSET = {
    1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9,
    7: 10, 8: 11, 9: 12, 10: 1, 11: 2, 12: 3,
}


def bs_to_ad(year: int, month: int, day: int) -> str:
    """Convert BS date to AD ISO string using nepali-datetime (precise)."""
    if HAS_NEPALI_DATETIME:
        try:
            bs_date = nepali_datetime.date(year, month, day)
            ad_date = bs_date.to_datetime_date()
            return ad_date.isoformat()
        except (ValueError, OverflowError):
            pass
    # Fallback: approximate conversion
    ad_month = _BS_MONTH_OFFSET.get(month, month)
    ad_year = year - 56 if month >= 10 else year - 57
    try:
        d = datetime(ad_year, ad_month, min(day, 28))
        return d.strftime("%Y-%m-%d")
    except ValueError:
        return f"{ad_year:04d}-{ad_month:02d}-15"


def parse_bs_month_str(text: str) -> Optional[str]:
    """Parse 'Poush 2082' or 'Baisakh 2080' to AD ISO date."""
    m = re.search(r"([A-Za-z]+)\s+(\d{4})", text.strip())
    if not m:
        return None
    name = m.group(1).lower()
    year = int(m.group(2))
    month = _BS_MONTH_NAMES.get(name)
    if month is None:
        logger.debug("Unknown BS month name: %s", name)
        return None
    return bs_to_ad(year, month, 15)


def parse_bs_numeric_str(text: str) -> Optional[str]:
    """Parse '2082-09-30' (BS) to AD ISO date."""
    m = re.match(r"(\d{4})-(\d{1,2})-(\d{1,2})", text.strip())
    if not m:
        return None
    year, month, day = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if year < 2000:
        return None  # Not a BS date
    return bs_to_ad(year, month, day)


def _parse_ad_date(text: str) -> Optional[str]:
    """Try multiple AD date formats and return ISO string."""
    text = text.strip()
    for fmt in (
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%d-%m-%Y",
        "%b %d, %Y",
        "%B %d, %Y",
    ):
        try:
            return datetime.strptime(text, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None


# -----------------------------------------------------------------------
# Data structures
# -----------------------------------------------------------------------

@dataclass
class NavRecord:
    symbol: str
    date: str           # ISO YYYY-MM-DD
    nav: float
    source: str         # e.g. "laxmi_monthly"


# -----------------------------------------------------------------------
# Provider scheme mappings
# -----------------------------------------------------------------------

_LAXMI_SCHEMES: Dict[int, str] = {
    1: "SBCF",     # Sunrise Blue Chip Fund
    2: "SFMF",     # Sunrise First Mutual Fund
    3: "SFEF",     # Sunrise Focused Equity Fund
    6: "LUK",      # Laxmi Unnati Kosh
    7: "LVF2",     # Laxmi Value Fund II
}

_NMB_SCHEMES: Dict[int, str] = {
    3: "NMB50",
    5: "NSIF2",
    6: "NMBHF2",
}

_NICASIA_CATEGORIES: Dict[int, str] = {
    2: "NICBF",
    7: "NICFC",
    8: "NICGF2",
}

_NABIL_SCHEMES: Dict[int, str] = {
    3: "NBF2",
    4: "NBF3",
}

_PRABHU_TICKERS = ["PRSF", "PSF"]

_SANIMA_SCHEME_ID = 3  # SAGF
_KUMARI_SCHEME_ID = 2  # KSY


# -----------------------------------------------------------------------
# Provider fetch functions
# -----------------------------------------------------------------------

async def _fetch_laxmi_monthly(client: httpx.AsyncClient) -> List[NavRecord]:
    """Laxmi Capital: Vue SPA API with per-year monthly NAV.

    /scheme returns {"scheme": [...], "years": {"2019":"2019",...}}.
    /getMutualFund returns {"date": ["Poush 2080",...], "data": [11.06,...]}.
    Dates are BS month names.
    """
    records: List[NavRecord] = []
    base = "https://lscapital.com.np/frontapi/en"
    try:
        resp = await client.get(f"{base}/scheme", timeout=15)
        resp.raise_for_status()
        payload = resp.json()
        # payload is {"scheme": [...], "years": {"2019":"2019", ...}}
        years_dict = payload.get("years", {}) if isinstance(payload, dict) else {}
        years = sorted(years_dict.keys())
    except Exception as exc:
        logger.warning("Laxmi scheme list failed: %s", exc)
        return records

    if not years:
        logger.warning("Laxmi: no years found")
        return records

    for scheme_id, symbol in _LAXMI_SCHEMES.items():
        for year in years:
            try:
                r = await client.get(
                    f"{base}/getMutualFund",
                    params={"schemeId": scheme_id, "year": year, "type": "monthly"},
                    timeout=15,
                )
                r.raise_for_status()
                data = r.json()
                if not isinstance(data, dict):
                    continue
                # Parallel arrays: {"date": [...], "data": [...]}
                dates = data.get("date", [])
                values = data.get("data", [])
                for label, value in zip(dates, values):
                    if value is None:
                        continue
                    iso = parse_bs_month_str(str(label))
                    if iso:
                        try:
                            records.append(NavRecord(symbol, iso, float(value), "laxmi_monthly"))
                        except (ValueError, TypeError):
                            continue
            except Exception:
                continue

    logger.info("Laxmi: %d monthly records across %d symbols", len(records), len(_LAXMI_SCHEMES))
    return records


async def _fetch_nmb_monthly(client: httpx.AsyncClient) -> List[NavRecord]:
    """NMB Capital: Same Vue SPA pattern, per-year queries required.

    /scheme returns {"scheme": [...], "years": {"2019":"2019",...}}.
    /getMutualFund returns {"date": ["2081-09-29",...], "data": [11.18,...]}.
    Dates are BS numeric strings.
    """
    records: List[NavRecord] = []
    base = "https://nmbcl.com.np/frontapi/en"
    try:
        resp = await client.get(f"{base}/scheme", timeout=15)
        resp.raise_for_status()
        payload = resp.json()
        # payload is {"scheme": [...], "years": {"2019":"2019", ...}}
        years_dict = payload.get("years", {}) if isinstance(payload, dict) else {}
        years = sorted(years_dict.keys())
    except Exception as exc:
        logger.warning("NMB scheme list failed: %s", exc)
        return records

    if not years:
        logger.warning("NMB: no years found")
        return records

    for scheme_id, symbol in _NMB_SCHEMES.items():
        for year in years:
            try:
                r = await client.get(
                    f"{base}/getMutualFund",
                    params={"schemeId": scheme_id, "type": "monthly", "year": year},
                    timeout=15,
                )
                r.raise_for_status()
                data = r.json()
                if not isinstance(data, dict):
                    continue
                # Parallel arrays: {"date": [...], "data": [...]}
                dates = data.get("date", [])
                values = data.get("data", [])
                for label, value in zip(dates, values):
                    if value is None:
                        continue
                    # NMB returns BS numeric dates like "2081-09-29"
                    iso = parse_bs_numeric_str(str(label)) or parse_bs_month_str(str(label))
                    if iso:
                        try:
                            records.append(NavRecord(symbol, iso, float(value), "nmb_monthly"))
                        except (ValueError, TypeError):
                            continue
            except Exception:
                continue

    logger.info("NMB: %d monthly records", len(records))
    return records


async def _fetch_nicasia_monthly(client: httpx.AsyncClient) -> List[NavRecord]:
    """NIC Asia Capital: HTML table scrape, AD dates."""
    records: List[NavRecord] = []
    base = "https://www.nicasiacapital.com/nav-details"

    try:
        from bs4 import BeautifulSoup
    except ImportError:
        logger.warning("NIC Asia requires beautifulsoup4 — skipping")
        return records

    for cat_id, symbol in _NICASIA_CATEGORIES.items():
        try:
            r = await client.get(
                base,
                params={"category": cat_id, "type": 2},  # type=2 for monthly
                timeout=20,
            )
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "html.parser")
            table = soup.find("table")
            if not table:
                continue
            rows = table.find_all("tr")[1:]  # skip header
            for row in rows:
                cells = row.find_all("td")
                if len(cells) < 3:
                    continue
                # Table columns: [AD date, BS date, NAV]
                date_text = cells[0].get_text(strip=True)
                nav_text = cells[2].get_text(strip=True).replace(",", "")
                iso = _parse_ad_date(date_text)
                if iso and nav_text:
                    try:
                        records.append(NavRecord(symbol, iso, float(nav_text), "nicasia_monthly"))
                    except ValueError:
                        continue
        except Exception as exc:
            logger.warning("NIC Asia category %d failed: %s", cat_id, exc)

    logger.info("NIC Asia: %d monthly records", len(records))
    return records


def _fetch_nabil_monthly_sync() -> List[NavRecord]:
    """Nabil Investment: WordPress AJAX endpoint (uses requests, not httpx).

    httpx gets 403; requests.Session with cookie warmup works.
    Response: {"success": true, "data": [{"eng_date":"2023-10-17","nav":"10.33",...}, ...]}.
    scheme_id: 2=NBF2, 3=NBF3.
    """
    import requests as req_lib
    import time

    records: List[NavRecord] = []
    session = req_lib.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    })

    # Warm up cookies
    try:
        session.get("https://nabilinvest.com.np/", timeout=20)
        time.sleep(0.5)  # Brief delay after warmup
    except Exception as exc:
        logger.warning("Nabil cookie warmup failed: %s", exc)
        return records

    for scheme_id, symbol in _NABIL_SCHEMES.items():
        try:
            r = session.post(
                "https://nabilinvest.com.np/wp-admin/admin-ajax.php",
                data={
                    "action": "scheme_data_filter",
                    "scheme_id": scheme_id,
                    "type": "monthly",
                },
                headers={
                    "Referer": "https://nabilinvest.com.np/",
                    "X-Requested-With": "XMLHttpRequest",
                },
                timeout=20,
            )
            r.raise_for_status()
            data = r.json()
            entries = data.get("data", []) if isinstance(data, dict) else data
            if not isinstance(entries, list):
                logger.warning("Nabil scheme %d: unexpected data type %s", scheme_id, type(entries))
                continue
            for entry in entries:
                eng_date = entry.get("eng_date", "")
                nav_val = entry.get("nav") or entry.get("nav_value")
                if not eng_date or nav_val is None:
                    continue
                iso = _parse_ad_date(eng_date)
                if iso:
                    try:
                        records.append(NavRecord(symbol, iso, float(nav_val), "nabil_monthly"))
                    except ValueError:
                        continue
        except Exception as exc:
            logger.warning("Nabil scheme %d failed: %s", scheme_id, exc)

    logger.info("Nabil: %d monthly records", len(records))
    return records


async def _fetch_kumari_monthly(client: httpx.AsyncClient) -> List[NavRecord]:
    """Kumari Capital: Directus REST API."""
    records: List[NavRecord] = []
    url = "https://api-web.kumaricapital.com/items/navs"

    try:
        import json
        filter_json = json.dumps({
            "scheme": {"_eq": _KUMARI_SCHEME_ID},
            "frequency": {"_eq": "monthly"},
        })
        r = await client.get(
            url,
            params={"fields": "value,date_ad", "filter": filter_json, "sort": "date_ad", "limit": -1},
            timeout=15,
        )
        r.raise_for_status()
        data = r.json().get("data", [])
        for entry in data:
            date_ad = entry.get("date_ad", "")
            value = entry.get("value")
            if not date_ad or value is None:
                continue
            iso = _parse_ad_date(date_ad)
            if iso:
                records.append(NavRecord("KSY", iso, float(value), "kumari_monthly"))
    except Exception as exc:
        logger.warning("Kumari fetch failed: %s", exc)

    logger.info("Kumari: %d monthly records", len(records))
    return records


async def _fetch_prabhu_monthly(client: httpx.AsyncClient) -> List[NavRecord]:
    """Prabhu Capital: REST API with monthlyNavData."""
    records: List[NavRecord] = []

    for ticker in _PRABHU_TICKERS:
        try:
            r = await client.get(
                f"https://www.prabhucapital.com/adminapi/v1/public/hist-nav",
                params={"ticker": ticker},
                timeout=15,
            )
            r.raise_for_status()
            data = r.json()
            # API nests data: {"status":..., "data": {"monthlyNavData":[...]}}
            inner = data.get("data", data) if isinstance(data, dict) else data
            monthly = inner.get("monthlyNavData", []) if isinstance(inner, dict) else []
            for entry in monthly:
                # Format: [date_str, nav_value, fund_name, month_name]
                if not isinstance(entry, (list, tuple)) or len(entry) < 2:
                    continue
                date_str = str(entry[0])
                nav_val = entry[1]
                if nav_val is None:
                    continue
                iso = _parse_ad_date(date_str)
                if iso:
                    try:
                        records.append(NavRecord(ticker, iso, float(nav_val), "prabhu_monthly"))
                    except ValueError:
                        continue
        except Exception as exc:
            logger.warning("Prabhu %s failed: %s", ticker, exc)

    logger.info("Prabhu: %d monthly records", len(records))
    return records


async def _fetch_sanima_monthly(client: httpx.AsyncClient) -> List[NavRecord]:
    """Sanima Capital: Vue SPA API with year=all support.

    Returns {"date": ["2079-08-29",...], "data": [9.93,...]} (parallel arrays).
    Dates are BS numeric strings.
    """
    records: List[NavRecord] = []
    base = "https://www.sanima.capital/frontapi/en"

    try:
        r = await client.get(
            f"{base}/fund-data",
            params={"scheme_id": _SANIMA_SCHEME_ID, "type": "monthly", "year": "all"},
            timeout=30,
        )
        r.raise_for_status()
        payload = r.json()

        if isinstance(payload, dict):
            # Parallel-array format: {"date": [...], "data": [...]}
            dates = payload.get("date", [])
            values = payload.get("data", [])
            for bs_date_str, nav_val in zip(dates, values):
                if nav_val is None:
                    continue
                iso = parse_bs_numeric_str(str(bs_date_str))
                if iso:
                    try:
                        records.append(NavRecord("SAGF", iso, float(nav_val), "sanima_monthly"))
                    except (ValueError, TypeError):
                        continue
        elif isinstance(payload, list):
            # Fallback: list of {"label":..., "value":...}
            for entry in payload:
                label = entry.get("label", "")
                value = entry.get("value")
                if value is None:
                    continue
                iso = parse_bs_numeric_str(label) or parse_bs_month_str(label)
                if iso:
                    records.append(NavRecord("SAGF", iso, float(value), "sanima_monthly"))
    except Exception as exc:
        logger.warning("Sanima fetch failed: %s", exc)

    logger.info("Sanima: %d monthly records", len(records))
    return records


# -----------------------------------------------------------------------
# Orchestration
# -----------------------------------------------------------------------

async def fetch_all_monthly_navs() -> List[NavRecord]:
    """Run all 7 provider scrapers concurrently."""
    async with httpx.AsyncClient(
        follow_redirects=True,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"},
    ) as client:
        results = await asyncio.gather(
            _fetch_laxmi_monthly(client),
            _fetch_nmb_monthly(client),
            _fetch_nicasia_monthly(client),
            asyncio.to_thread(_fetch_nabil_monthly_sync),
            _fetch_kumari_monthly(client),
            _fetch_prabhu_monthly(client),
            _fetch_sanima_monthly(client),
            return_exceptions=True,
        )

    all_records: List[NavRecord] = []
    for result in results:
        if isinstance(result, Exception):
            logger.error("Provider failed: %s", result)
        elif isinstance(result, list):
            all_records.extend(result)

    logger.info("Total monthly NAV records fetched: %d", len(all_records))
    return all_records


def update_nav_csvs(
    records: List[NavRecord],
    project_root: Path,
    universe_symbols: set | None = None,
) -> Dict[str, int]:
    """
    Write NavRecords to per-symbol CSVs (idempotent: skips existing dates).

    Returns dict of {symbol: new_rows_written}.
    """
    nav_dir = project_root / "data" / "raw" / "nav"
    nav_dir.mkdir(parents=True, exist_ok=True)

    # Group by symbol
    by_symbol: Dict[str, List[NavRecord]] = {}
    for rec in records:
        if universe_symbols and rec.symbol not in universe_symbols:
            continue
        by_symbol.setdefault(rec.symbol, []).append(rec)

    stats: Dict[str, int] = {}

    for symbol, recs in sorted(by_symbol.items()):
        csv_path = nav_dir / f"{symbol}.csv"

        # Load existing
        existing_dates: set = set()
        existing_rows: list = []
        if csv_path.exists():
            try:
                with open(csv_path, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        existing_rows.append(row)
                        existing_dates.add(row["date"])
            except Exception as exc:
                logger.warning("Error reading %s: %s", csv_path, exc)

        # Add new records
        new_count = 0
        for rec in recs:
            if rec.date not in existing_dates:
                existing_rows.append({
                    "date": rec.date,
                    "nav": f"{rec.nav:.2f}",
                    "source": rec.source,
                })
                existing_dates.add(rec.date)
                new_count += 1

        if new_count > 0:
            existing_rows.sort(key=lambda x: x["date"])
            with open(csv_path, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["date", "nav", "source"])
                writer.writeheader()
                writer.writerows(existing_rows)
            logger.info("\u2713 %s: +%d new rows (total %d)", symbol, new_count, len(existing_rows))

        stats[symbol] = new_count

    return stats


# -----------------------------------------------------------------------
# Entry point
# -----------------------------------------------------------------------

def run(project_root: Path) -> Dict[str, int]:
    """
    Main entry point: fetch all provider NAVs and update CSVs.

    Returns dict of {symbol: new_rows_written}.
    """
    logger.info("=" * 60)
    logger.info("Monthly NAV Scraper — Direct Provider APIs")
    logger.info("=" * 60)

    # Load fund universe for filtering
    universe_path = project_root / "data" / "raw" / "fund_universe.csv"
    universe_symbols: set | None = None
    if universe_path.exists():
        try:
            df = pd.read_csv(universe_path)
            universe_symbols = set(df["symbol"].unique())
            logger.info("Fund universe: %d symbols loaded", len(universe_symbols))
        except Exception:
            pass

    # Fetch from all providers
    records = asyncio.run(fetch_all_monthly_navs())

    # Update CSVs
    stats = update_nav_csvs(records, project_root, universe_symbols)

    total_new = sum(stats.values())
    symbols_updated = sum(1 for v in stats.values() if v > 0)
    logger.info("Summary: %d new records across %d symbols", total_new, symbols_updated)
    logger.info("=" * 60)

    return stats


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    project_root = Path(__file__).resolve().parent.parent.parent
    run(project_root)
