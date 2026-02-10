"""
Daily Market Price & Liquidity Scraper for NEPSE Closed-End Mutual Funds

Uses Playwright (headless Chromium) to intercept JSON responses from NEPSE's
Angular SPA and extract daily trading data.

Data Source: https://nepalstock.com.np/company/detail/{security_id}
API Intercepted: /api/nots/security/{security_id}

Output: data/raw/market_prices.csv (append-only, no duplicates)
"""

import asyncio
import csv
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from playwright.async_api import async_playwright, Page

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MarketDataExtractor:
    """Extracts market price data from NEPSE using Playwright"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.mapping_path = project_root / 'data' / 'reference' / 'symbol_nepse_map.csv'
        self.output_path = project_root / 'data' / 'raw' / 'market_prices.csv'
        self.symbol_to_id: Dict[str, int] = {}
        self.id_to_symbol: Dict[int, str] = {}
        
    def load_mappings(self) -> None:
        """Load symbol → security_id mappings from reference CSV"""
        logger.info(f"Loading mappings from: {self.mapping_path}")
        
        if not self.mapping_path.exists():
            raise FileNotFoundError(f"Mapping file not found: {self.mapping_path}")
        
        with open(self.mapping_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                symbol = row['symbol'].strip().upper()
                security_id = int(row['security_id'])
                self.symbol_to_id[symbol] = security_id
                self.id_to_symbol[security_id] = symbol
        
        logger.info(f"✓ Loaded {len(self.symbol_to_id)} symbol mappings")
    
    def get_existing_data(self) -> set:
        """Get existing (date, symbol) pairs to avoid duplicates"""
        existing = set()
        
        if self.output_path.exists():
            with open(self.output_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    key = (row['date'], row['symbol'])
                    existing.add(key)
            logger.info(f"Found {len(existing)} existing records")
        else:
            logger.info("No existing market_prices.csv - will create new file")
        
        return existing
    
    async def fetch_security_data(
        self, 
        page: Page, 
        security_id: int, 
        symbol: str
    ) -> Optional[Dict]:
        """
        Fetch market data for a single security by intercepting API response.
        
        Args:
            page: Playwright page instance
            security_id: NEPSE security ID
            symbol: Fund symbol
            
        Returns:
            Dictionary with extracted data or None if failed
        """
        target_api = f'/api/nots/security/{security_id}'
        captured_data = {'found': False, 'json': None}
        
        async def handle_response(response):
            if target_api in response.url and response.status == 200:
                try:
                    data = await response.json()
                    captured_data['found'] = True
                    captured_data['json'] = data
                except Exception as e:
                    logger.warning(f"Failed to parse JSON for {symbol}: {e}")
        
        page.on("response", handle_response)
        
        try:
            url = f'https://nepalstock.com.np/company/detail/{security_id}'
            logger.info(f"Fetching {symbol} (ID: {security_id})...")
            
            await page.goto(url, timeout=30000)
            await page.wait_for_timeout(2000)  # Wait for API calls
            
            if not captured_data['found']:
                logger.warning(f"✗ {symbol}: API response not captured")
                return None
            
            # Extract data from JSON response
            json_data = captured_data['json']
            trade_data = json_data.get('securityDailyTradeDto', {})
            
            if not trade_data:
                logger.warning(f"✗ {symbol}: Missing securityDailyTradeDto")
                return None
            
            # Validate required fields
            required_fields = [
                'businessDate', 'openPrice', 'highPrice', 'lowPrice',
                'lastTradedPrice', 'totalTradeQuantity', 'totalTrades'
            ]
            
            missing = [f for f in required_fields if f not in trade_data or trade_data[f] is None]
            
            if missing:
                logger.warning(f"✗ {symbol}: Missing fields: {', '.join(missing)}")
                return None
            
            # Convert business date to ISO-8601
            business_date = trade_data['businessDate']
            if isinstance(business_date, str):
                # Parse YYYY-MM-DD format
                date_iso = business_date.split('T')[0] if 'T' in business_date else business_date
            else:
                logger.warning(f"✗ {symbol}: Invalid date format: {business_date}")
                return None
            
            extracted = {
                'date': date_iso,
                'symbol': symbol,
                'ltp': float(trade_data['lastTradedPrice']),
                'open': float(trade_data['openPrice']),
                'high': float(trade_data['highPrice']),
                'low': float(trade_data['lowPrice']),
                'volume': int(trade_data['totalTradeQuantity']),
                'trades': int(trade_data['totalTrades']),
                'source': 'nepse_playwright'
            }
            
            logger.info(f"✓ {symbol}: {extracted['date']} | LTP={extracted['ltp']:.2f} | Vol={extracted['volume']}")
            return extracted
            
        except Exception as e:
            logger.error(f"✗ {symbol}: Error during fetch: {e}")
            return None
    
    async def scrape_all(self) -> Tuple[List[Dict], List[str], int]:
        """
        Scrape market data for all mutual funds.
        
        Returns:
            Tuple of (new_records, failed_symbols, scraped_count)
            - new_records: Records to save (excluding duplicates)
            - failed_symbols: Symbols that failed to scrape
            - scraped_count: Total successfully scraped (including duplicates)
        """
        logger.info("=" * 80)
        logger.info("Starting Daily Market Price Scraper (Playwright)")
        logger.info("=" * 80)
        
        self.load_mappings()
        existing_data = self.get_existing_data()
        
        new_records = []
        failed = []
        scraped_count = 0
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=['--disable-blink-features=AutomationControlled']
            )
            
            context = await browser.new_context(
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                viewport={'width': 1920, 'height': 1080},
                locale='en-US',
                ignore_https_errors=True
            )
            
            page = await context.new_page()
            
            logger.info(f"\nProcessing {len(self.symbol_to_id)} securities...")
            logger.info("-" * 80)
            
            for symbol, security_id in sorted(self.symbol_to_id.items()):
                data = await self.fetch_security_data(page, security_id, symbol)
                
                if data:
                    scraped_count += 1
                    
                    # Check for duplicates
                    key = (data['date'], data['symbol'])
                    if key in existing_data:
                        logger.info(f"  → Skipping {symbol} (already exists for {data['date']})")
                    else:
                        new_records.append(data)
                else:
                    failed.append(symbol)
                
                # Rate limiting: small delay between requests
                await page.wait_for_timeout(1000)
            
            await browser.close()
        
        return new_records, failed, scraped_count
    
    def save_results(self, records: List[Dict]) -> None:
        """
        Append new records to market_prices.csv.
        
        Args:
            records: List of data dictionaries to append
        """
        if not records:
            logger.info("No new records to save")
            return
        
        # Ensure output directory exists
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Check if file exists to determine if we need headers
        file_exists = self.output_path.exists()
        
        fieldnames = ['date', 'symbol', 'ltp', 'open', 'high', 'low', 'volume', 'trades', 'source']
        
        with open(self.output_path, 'a', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader()
            
            for record in records:
                writer.writerow(record)
        
        logger.info(f"✓ Saved {len(records)} new records to: {self.output_path}")
    
    def validate_success_rate(
        self, 
        scraped_count: int,
        failed: List[str],
        new_count: int
    ) -> None:
        """
        Validate that at least 80% of symbols were successfully scraped.
        
        Args:
            scraped_count: Number of successfully scraped records
            failed: List of failed symbols
            new_count: Number of new records (excluding duplicates)
            
        Raises:
            ValueError: If success rate is below 80%
        """
        total = scraped_count + len(failed)
        success_rate = (scraped_count / total * 100) if total > 0 else 0
        
        logger.info("")
        logger.info("=" * 80)
        logger.info("SCRAPE SUMMARY")
        logger.info("=" * 80)
        logger.info(f"Total symbols: {total}")
        logger.info(f"Successfully scraped: {scraped_count}")
        logger.info(f"New records (to save): {new_count}")
        logger.info(f"Duplicates (skipped): {scraped_count - new_count}")
        logger.info(f"Failed: {len(failed)}")
        logger.info(f"Success rate: {success_rate:.1f}%")
        
        if failed:
            logger.warning(f"\nFailed symbols: {', '.join(failed)}")
        
        if success_rate < 80:
            logger.error("")
            logger.error("=" * 80)
            logger.error("VALIDATION FAILED")
            logger.error("=" * 80)
            logger.error(f"Success rate ({success_rate:.1f}%) is below minimum threshold (80%)")
            logger.error("This indicates a systemic issue with the scraper or NEPSE website.")
            logger.error("Script will exit with error status.")
            raise ValueError(f"Success rate {success_rate:.1f}% below 80% threshold")
        
        logger.info("")
        logger.info("=" * 80)
        logger.info("✓ VALIDATION PASSED")
        logger.info("=" * 80)
        logger.info(f"Success rate {success_rate:.1f}% meets 80% threshold")


async def main():
    """Main execution"""
    extractor = MarketDataExtractor(Path(__file__).parent.parent.parent)
    
    try:
        # Scrape all securities
        new_records, failed, scraped_count = await extractor.scrape_all()
        
        # Validate success rate (will raise exception if < 80%)
        extractor.validate_success_rate(scraped_count, failed, len(new_records))
        
        # Save results
        extractor.save_results(new_records)
        
        logger.info("")
        logger.info("=" * 80)
        logger.info("SCRAPER COMPLETED SUCCESSFULLY")
        logger.info("=" * 80)
        logger.info("✓ Data collection complete")
        logger.info("✓ Validation passed")
        logger.info("✓ Results saved")
        logger.info("✓ Ready for downstream analytics")
        logger.info("=" * 80)
        
    except Exception as e:
        logger.error("")
        logger.error("=" * 80)
        logger.error("SCRAPER FAILED")
        logger.error("=" * 80)
        logger.error(f"Error: {e}")
        logger.error("=" * 80)
        raise


if __name__ == '__main__':
    asyncio.run(main())
