"""
Monthly NAV scraper for Nepal mutual funds.

Fetches current monthly NAV snapshot from ShareSansar.com
Only collects the latest monthly NAV (no historical data).
"""

import csv
import os
import re
import requests
from datetime import datetime
from pathlib import Path
from typing import Dict, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Symbols whose NAV is fetched from dedicated provider APIs
# (monthly_nav_scraper.py). ShareSansar is skipped for these
# to avoid duplicate / less-accurate data.
PROVIDER_SYMBOLS = {
    # Laxmi Capital
    'LUK', 'LVF2', 'SFEF', 'SFMF', 'SBCF',
    # NMB Capital
    'NMB50', 'NSIF2', 'NMBHF2',
    # NIC Asia Capital
    'NICBF', 'NICFC', 'NICGF2',
    # Nabil Investment
    'NBF2', 'NBF3',
    # Kumari Capital
    'KSY',
    # Prabhu Capital
    'PRSF', 'PSF',
    # Sanima Capital
    'SAGF',
}


# Nepali calendar month mapping (approximate mid-month Gregorian dates)
# Format: {nepali_year: {nepali_month: (gregorian_year, gregorian_month)}}
NEPALI_MONTH_MAP = {
    'baisakh': 1, 'baishakh': 1,
    'jestha': 2, 'jeth': 2,
    'ashadh': 3, 'asar': 3, 'ashad': 3,
    'shrawan': 4, 'sawan': 4, 'shravan': 4,
    'bhadra': 5, 'bhadau': 5,
    'ashwin': 6, 'asoj': 6, 'ashoj': 6,
    'kartik': 7, 'kartick': 7,
    'mangsir': 8, 'mangshir': 8, 'marga': 8,
    'poush': 9, 'paush': 9, 'push': 9,
    'magh': 10, 'magha': 10,
    'falgun': 11, 'phalgun': 11,
    'chaitra': 12, 'chait': 12
}

# Approximate conversion: Nepali month -> (Gregorian month, year offset)
# Each Nepali month starts mid-way through a Gregorian month, so the
# majority of each BS month falls in the *next* Gregorian month.
# year_offset: subtract from BS year to get the Gregorian year.
NEPALI_TO_GREGORIAN = {
    1:  (5,  57),  # Baisakh  -> mid-Apr to mid-May   -> May
    2:  (6,  57),  # Jestha   -> mid-May to mid-Jun   -> June
    3:  (7,  57),  # Ashadh   -> mid-Jun to mid-Jul   -> July
    4:  (8,  57),  # Shrawan  -> mid-Jul to mid-Aug   -> August
    5:  (9,  57),  # Bhadra   -> mid-Aug to mid-Sep   -> September
    6:  (10, 57),  # Ashwin   -> mid-Sep to mid-Oct   -> October
    7:  (11, 57),  # Kartik   -> mid-Oct to mid-Nov   -> November
    8:  (12, 57),  # Mangsir  -> mid-Nov to mid-Dec   -> December
    9:  (1,  56),  # Poush    -> mid-Dec to mid-Jan   -> January (next GY)
    10: (2,  56),  # Magh     -> mid-Jan to mid-Feb   -> February
    11: (3,  56),  # Falgun   -> mid-Feb to mid-Mar   -> March
    12: (4,  56),  # Chaitra  -> mid-Mar to mid-Apr   -> April
}


def parse_nepali_date(nepali_date_str: str) -> Optional[str]:
    """
    Convert Nepali date string to ISO format (YYYY-MM-DD).
    
    Args:
        nepali_date_str: Date in format "Poush 2082" or similar
        
    Returns:
        ISO format date string or None if parsing fails
    """
    if not nepali_date_str or nepali_date_str.strip() == '':
        return None
    
    try:
        # Parse pattern like "Poush 2082"
        match = re.search(r'([A-Za-z]+)\s+(\d{4})', nepali_date_str)
        if not match:
            logger.warning(f"Could not parse Nepali date: {nepali_date_str}")
            return None
        
        month_name = match.group(1).lower()
        nepali_year = int(match.group(2))
        
        # Get Nepali month number
        nepali_month = NEPALI_MONTH_MAP.get(month_name)
        if not nepali_month:
            logger.warning(f"Unknown Nepali month: {month_name}")
            return None
        
        # Convert to Gregorian using (month, year_offset) lookup
        gregorian_month, year_offset = NEPALI_TO_GREGORIAN[nepali_month]
        gregorian_year = nepali_year - year_offset
        
        # Use mid-month (15th) as default day
        iso_date = f"{gregorian_year:04d}-{gregorian_month:02d}-15"
        
        # Validate the date is reasonable
        date_obj = datetime.strptime(iso_date, '%Y-%m-%d')
        return iso_date
        
    except (ValueError, AttributeError) as e:
        logger.warning(f"Error parsing Nepali date '{nepali_date_str}': {e}")
        return None


def fetch_current_monthly_nav() -> Dict[str, Tuple[str, float]]:
    """
    Fetch current monthly NAV for all funds from ShareSansar API.
    
    Returns:
        Dictionary mapping symbol -> (date, nav)
        Example: {'SEF': ('2026-02-15', 10.02), ...}
    """
    logger.info("Fetching monthly NAVs from ShareSansar...")
    
    url = "https://www.sharesansar.com/mutual-fund-navs"
    params = {
        'type': -1,  # Close-end funds
        'draw': 1,
        'start': 0,
        'length': 50,  # API might not support larger values
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest'
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        funds = data.get('data', [])
        
        logger.info(f"Retrieved {len(funds)} funds from API")
        
        nav_data = {}
        skipped = 0
        
        for fund in funds:
            symbol = fund.get('symbol', '').strip()
            monthly_nav_price = fund.get('monthly_nav_price')
            monthly_date = fund.get('monthly_date')
            
            # Skip if no symbol
            if not symbol:
                continue
            
            # Skip if NAV is missing or invalid
            if not monthly_nav_price or monthly_nav_price in ('null', 'None', ''):
                logger.warning(f"Skipping {symbol}: No monthly NAV available")
                skipped += 1
                continue
            
            # Parse NAV value
            try:
                nav = float(monthly_nav_price)
            except (ValueError, TypeError):
                logger.warning(f"Skipping {symbol}: Invalid NAV value '{monthly_nav_price}'")
                skipped += 1
                continue
            
            # Parse date
            iso_date = parse_nepali_date(monthly_date) if monthly_date else None
            
            if not iso_date:
                # Fallback: use published_date or current date
                published_date = fund.get('published_date')
                if published_date:
                    try:
                        # Validate it's in ISO format
                        datetime.strptime(published_date, '%Y-%m-%d')
                        iso_date = published_date
                    except ValueError:
                        pass
                
                if not iso_date:
                    logger.warning(f"Skipping {symbol}: Could not determine date")
                    skipped += 1
                    continue
            
            nav_data[symbol] = (iso_date, nav)
        
        logger.info(f"Successfully parsed {len(nav_data)} NAV records")
        if skipped > 0:
            logger.info(f"Skipped {skipped} funds (missing/invalid data)")
        
        return nav_data
        
    except requests.RequestException as e:
        logger.error(f"HTTP error fetching NAV data: {e}")
        return {}
    except ValueError as e:
        logger.error(f"JSON parsing error: {e}")
        return {}


def update_fund_nav_csv(symbol: str, date: str, nav: float, data_dir: Path) -> None:
    """
    Update NAV CSV file for a specific fund (idempotent).
    
    Creates new file if it doesn't exist.
    Appends new row only if date doesn't already exist.
    Sorts all rows by date before saving.
    
    Args:
        symbol: Fund symbol (e.g., 'SEF')
        date: ISO format date (YYYY-MM-DD)
        nav: NAV value
        data_dir: Path to data/raw/nav directory
    """
    nav_dir = data_dir / 'nav'
    nav_dir.mkdir(parents=True, exist_ok=True)
    
    csv_path = nav_dir / f'{symbol}.csv'
    source = 'sharesansar_monthly'
    
    # Read existing data
    existing_rows = []
    dates_seen = set()
    
    if csv_path.exists():
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    existing_rows.append(row)
                    dates_seen.add(row['date'])
        except Exception as e:
            logger.warning(f"Error reading {csv_path}: {e}")
    
    # Check if this date already exists
    if date in dates_seen:
        logger.debug(f"{symbol}: Date {date} already exists, skipping")
        return
    
    # Add new row
    new_row = {
        'date': date,
        'nav': f'{nav:.2f}',
        'source': source
    }
    existing_rows.append(new_row)
    
    # Sort by date
    existing_rows.sort(key=lambda x: x['date'])
    
    # Write back to file
    try:
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['date', 'nav', 'source'])
            writer.writeheader()
            writer.writerows(existing_rows)
        
        logger.info(f"✓ {symbol}: Added NAV {nav:.2f} for {date}")
    except Exception as e:
        logger.error(f"Error writing {csv_path}: {e}")


def load_fund_universe(universe_path: Path) -> list:
    """
    Load fund symbols from fund_universe.csv.
    
    Args:
        universe_path: Path to fund_universe.csv
        
    Returns:
        List of fund symbols
    """
    try:
        with open(universe_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            symbols = [row['symbol'] for row in reader]
        logger.info(f"Loaded {len(symbols)} funds from universe")
        return symbols
    except Exception as e:
        logger.error(f"Error loading fund universe: {e}")
        return []


def main():
    """Main scraper execution"""
    logger.info("=" * 60)
    logger.info("Monthly NAV Scraper - ShareSansar")
    logger.info("=" * 60)
    
    # Setup paths
    project_root = Path(__file__).parent.parent.parent
    universe_path = project_root / 'data' / 'raw' / 'fund_universe.csv'
    data_dir = project_root / 'data' / 'raw'
    
    # Validate fund universe exists
    if not universe_path.exists():
        logger.error(f"Fund universe not found: {universe_path}")
        logger.error("Please run fund_universe.py first to generate the universe")
        return
    
    # Load fund universe
    universe_symbols = load_fund_universe(universe_path)
    if not universe_symbols:
        logger.error("No funds found in universe")
        return
    
    # Fetch current monthly NAVs from API
    nav_data = fetch_current_monthly_nav()
    if not nav_data:
        logger.error("Failed to fetch NAV data from API")
        return
    
    # Update CSV files for each fund
    logger.info(f"\nUpdating NAV CSV files...")
    updated_count = 0
    skipped_count = 0
    
    for symbol in universe_symbols:
        if symbol in PROVIDER_SYMBOLS:
            logger.debug(f"{symbol}: Skipped (dedicated provider scraper)")
            skipped_count += 1
            continue
        if symbol in nav_data:
            date, nav = nav_data[symbol]
            update_fund_nav_csv(symbol, date, nav, data_dir)
            updated_count += 1
        else:
            logger.debug(f"{symbol}: No NAV data available from API")
            skipped_count += 1
    
    # Summary
    logger.info(f"\n" + "=" * 60)
    logger.info(f"Summary:")
    logger.info(f"  Funds in universe: {len(universe_symbols)}")
    logger.info(f"  NAVs fetched: {len(nav_data)}")
    logger.info(f"  Files updated: {updated_count}")
    logger.info(f"  Skipped: {skipped_count}")
    logger.info("=" * 60)


if __name__ == '__main__':
    main()
