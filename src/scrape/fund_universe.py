"""
Close-end Mutual Fund Universe Scraper for Nepal

Scrapes close-end mutual fund data from ShareSansar.com using their DataTables API
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import pandas as pd
from pathlib import Path
from typing import List, Dict
from datetime import datetime


class FundUniverseScraper:
    """Scraper for Nepal close-end mutual funds from ShareSansar"""
    
    BASE_URL = "https://www.sharesansar.com"
    MF_NAV_URL = f"{BASE_URL}/mutual-fund-navs"
    
    def __init__(self, project_root: 'Path | None' = None):
        self.project_root = Path(project_root) if project_root else None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest'
        }
    
    def fetch_mutual_funds_api(self, fund_type: int = -1) -> List[Dict]:
        """
        Fetch mutual funds directly from ShareSansar's DataTables API
        
        Args:
            fund_type: -1 for close-end, 1 for matured, 2 for open-end
            
        Returns:
            List of mutual fund dictionaries
        """
        print(f"Fetching mutual funds (type={fund_type})...")
        
        try:
            # Make multiple requests if needed to get all funds
            all_funds = []
            start = 0
            length = 50  # Use smaller batch size to avoid 202 status
            
            while True:
                params = {
                    'type': fund_type,
                    'draw': 1,
                    'start': start,
                    'length': length,
                }
                
                # Use fresh headers for each request (exactly like test_api.py)
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'X-Requested-With': 'XMLHttpRequest'
                }
                
                response = requests.get(self.MF_NAV_URL, params=params, headers=headers, timeout=30)
                
                if response.status_code != 200:
                    print(f"⚠ Unexpected status code: {response.status_code}")
                    break
                
                data = response.json()
                
                records_total = data.get('recordsTotal', 0)
                records_filtered = data.get('recordsFiltered', 0)
                funds_batch = data.get('data', [])
                
                if not funds_batch:
                    break
                
                all_funds.extend(funds_batch)
                print(f"  Fetched {len(all_funds)}/{records_filtered} funds...")
                
                # Check if we got all funds
                if len(all_funds) >= records_filtered:
                    break
                
                start += length
            
            print(f"✓ Found {len(all_funds)} mutual funds from API")
            return all_funds
                
        except requests.RequestException as e:
            print(f"Error fetching API: {e}")
            return []
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return []
    
    def scrape_all(self, save_html: bool = False) -> pd.DataFrame:
        """Main scraping function to get all close-end mutual funds"""
        print("Fetching close-end mutual funds from ShareSansar API...")
        
        # Fetch close-end funds (type = -1)
        funds = self.fetch_mutual_funds_api(fund_type=-1)
        
        if not funds:
            print("No funds found, trying fallback method...")
            # Fallback to HTML scraping if API fails
            funds = self.fetch_from_html()
        
        if funds:
            # Convert to DataFrame
            df = pd.DataFrame(funds)
            
            # Explicitly rename columns (don't assume order)
            df = df.rename(columns={
                'companyid': 'id',
                'companyname': 'name',
                'maturitydate': 'maturity_date',
                'fundsize': 'fund_size'
            })
            
            # Add machine-friendly type and source columns
            df['type'] = 'closed_end'
            df['source'] = 'sharesansar'
            df['scraped_at'] = pd.Timestamp.utcnow().isoformat()
            
            # Select only essential columns in desired order
            essential_cols = ['id', 'symbol', 'name', 'maturity_date', 'fund_size', 'type', 'source', 'scraped_at']
            available_cols = [col for col in essential_cols if col in df.columns]
            
            if available_cols:
                df = df[available_cols]
            
            # Sanity check: ensure we got a reasonable number of funds
            if len(df) < 20:
                raise RuntimeError(
                    f"Fund universe too small ({len(df)}). ShareSansar API may have changed."
                )
            
            # Sort deterministically for clean git diffs
            df = df.sort_values('symbol').reset_index(drop=True)
            
            print(f"✓ Successfully fetched {len(df)} close-end mutual funds")
            return df
        
        return pd.DataFrame()
    
    def fetch_from_html(self) -> List[Dict]:
        """Fallback method: Extract fund list from HTML page"""
        print("Attempting HTML fallback method...")
        
        try:
            response = requests.get(self.MF_NAV_URL, headers=self.headers, timeout=30)
            response.raise_for_status()
            html_content = response.text
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            return []
        
        # Extract cmpjson from HTML as fallback
        soup = BeautifulSoup(html_content, 'html.parser')
        
        for script in soup.find_all('script'):
            if not script.string:
                continue
            
            if 'cmpjson' not in script.string:
                continue
            
            # Extract the JSON data
            pattern = r'var\s+cmpjson\s*=\s*(\[.*?\]);'
            match = re.search(pattern, script.string, re.DOTALL)
            
            if match:
                try:
                    json_str = match.group(1)
                    all_companies = json.loads(json_str)
                    
                    # Filter for mutual funds only using strict criteria
                    mutual_funds = []
                    fund_keywords = ['Fund', 'Yojana', 'Kosh', 'Scheme', 'Mutual']
                    
                    for company in all_companies:
                        name = company.get('companyname', '')
                        symbol = company.get('symbol', '')
                        
                        # Must have fund keywords AND NOT be excluded patterns
                        excluded_patterns = ['Hydro', 'Power', 'Energy', 'Bank', 'Finance', 'Insurance', 
                                           'Hotel', 'Limited' if 'Fund' not in name else None]
                        
                        has_fund_keyword = any(kw in name for kw in fund_keywords)
                        is_excluded = any(ex and ex in name for ex in excluded_patterns if ex)
                        
                        if has_fund_keyword and not is_excluded:
                            mutual_funds.append(company)
                    
                    print(f"✓ Extracted {len(mutual_funds)} mutual funds from HTML")
                    return mutual_funds
                    
                except json.JSONDecodeError as e:
                    print(f"JSON decode error: {e}")
                    continue
        
        return []
    
    def save_to_csv(self, df: pd.DataFrame, filepath: str = None):
        """Save fund universe to CSV with deterministic filename"""
        if filepath is None:
            if self.project_root:
                filepath = str(self.project_root / 'data' / 'raw' / 'fund_universe.csv')
            else:
                # Legacy fallback: relative path (only works when CWD is src/scrape/)
                filepath = "../../data/raw/fund_universe.csv"
        
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(filepath, index=False)
        print(f"Saved {len(df)} funds to {filepath}")


def main():
    """Main execution function"""
    scraper = FundUniverseScraper()
    
    # Scrape fund universe using API
    funds_df = scraper.scrape_all()
    
    if not funds_df.empty:
        print("\n=== Close-End Mutual Funds ===")
        print(funds_df.to_string(index=False))
        
        # Save to CSV
        scraper.save_to_csv(funds_df)
        
        # Print summary
        print(f"\n✓ Successfully scraped {len(funds_df)} close-end mutual funds")
    else:
        print("No funds found")


if __name__ == "__main__":
    main()
