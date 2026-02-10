"""
NEPSE Symbol to Security ID Mapper

Builds a deterministic mapping from fund symbols to NEPSE security IDs
using a static reference JSON file captured from NEPSE.

This script does NOT call any APIs - it uses pre-captured reference data.
"""

import csv
import json
import logging
from pathlib import Path
from typing import Dict, List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_security_reference(json_path: Path) -> List[Dict]:
    """
    Load NEPSE security master from static JSON file.
    
    Args:
        json_path: Path to securityid.json
        
    Returns:
        List of security dictionaries
    """
    logger.info(f"Loading security reference: {json_path}")
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            raise ValueError(f"Expected list, got {type(data)}")
        
        logger.info(f"✓ Loaded {len(data)} securities from reference file")
        return data
        
    except Exception as e:
        logger.error(f"Failed to load security reference: {e}")
        raise


def filter_securities(securities: List[Dict]) -> List[Dict]:
    """
    Filter securities based on business rules.
    
    Filters applied:
    - activeStatus == "A" (active securities only)
    
    Note: The reference JSON does not contain instrumentType.code or
    schemeDescription fields. The fund_universe.csv already contains
    only closed-end mutual funds, so we filter by activeStatus only.
    
    Args:
        securities: List of all securities
        
    Returns:
        Filtered list of securities
    """
    logger.info("Applying filters to securities...")
    
    filtered = []
    
    for security in securities:
        # Filter: activeStatus must be "A"
        if security.get('activeStatus') == 'A':
            filtered.append(security)
    
    logger.info(f"✓ Filtered to {len(filtered)} active securities")
    return filtered


def build_symbol_lookup(securities: List[Dict]) -> Dict[str, int]:
    """
    Build a lookup dictionary from symbol to security ID.
    
    Args:
        securities: List of security dictionaries
        
    Returns:
        Dictionary mapping symbol (uppercase) -> security_id
    """
    logger.info("Building symbol→ID lookup...")
    
    lookup = {}
    
    for security in securities:
        symbol = security.get('symbol', '').strip().upper()
        security_id = security.get('id')
        
        if symbol and security_id:
            lookup[symbol] = int(security_id)
    
    logger.info(f"✓ Built lookup for {len(lookup)} symbols")
    return lookup


def load_fund_universe(universe_path: Path) -> List[str]:
    """
    Load fund symbols from fund_universe.csv.
    
    Args:
        universe_path: Path to fund_universe.csv
        
    Returns:
        List of fund symbols (uppercase)
    """
    logger.info(f"Loading fund universe: {universe_path}")
    
    try:
        with open(universe_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            symbols = [row['symbol'].strip().upper() for row in reader]
        
        logger.info(f"✓ Loaded {len(symbols)} fund symbols")
        return symbols
        
    except Exception as e:
        logger.error(f"Failed to load fund universe: {e}")
        raise


def match_symbols(
    fund_symbols: List[str],
    security_lookup: Dict[str, int]
) -> Tuple[List[Tuple[str, int]], List[str]]:
    """
    Match fund symbols with NEPSE securities.
    
    Args:
        fund_symbols: List of fund symbols from universe
        security_lookup: Dictionary of symbol -> security_id
        
    Returns:
        Tuple of (matched_pairs, missing_symbols)
        - matched_pairs: List of (symbol, security_id) tuples
        - missing_symbols: List of symbols not found
    """
    logger.info("Matching fund symbols with NEPSE securities...")
    
    matched = []
    missing = []
    
    for symbol in fund_symbols:
        if symbol in security_lookup:
            security_id = security_lookup[symbol]
            matched.append((symbol, security_id))
            logger.debug(f"✓ {symbol} -> {security_id}")
        else:
            missing.append(symbol)
            logger.warning(f"✗ {symbol} not found")
    
    logger.info(f"Matched: {len(matched)}/{len(fund_symbols)} symbols")
    
    return matched, missing


def save_mapping(
    matched_pairs: List[Tuple[str, int]],
    output_path: Path
) -> None:
    """
    Save symbol→security_id mapping to CSV.
    
    Args:
        matched_pairs: List of (symbol, security_id) tuples
        output_path: Path to output CSV file
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Sort by symbol for deterministic output
    matched_pairs.sort(key=lambda x: x[0])
    
    try:
        with open(output_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['symbol', 'security_id', 'source'])
            
            for symbol, security_id in matched_pairs:
                writer.writerow([symbol, security_id, 'nepse_security_master_snapshot'])
        
        logger.info(f"✓ Saved mapping to: {output_path}")
        
    except Exception as e:
        logger.error(f"Failed to save mapping: {e}")
        raise


def main():
    """Main execution"""
    logger.info("=" * 60)
    logger.info("NEPSE Symbol → Security ID Mapper")
    logger.info("(Using static reference data)")
    logger.info("=" * 60)
    
    # Setup paths
    project_root = Path(__file__).parent.parent.parent
    reference_json = project_root / 'data' / 'reference' / 'securityid.json'
    universe_csv = project_root / 'data' / 'raw' / 'fund_universe.csv'
    output_csv = project_root / 'data' / 'reference' / 'symbol_nepse_map.csv'
    
    # Validate inputs exist
    if not reference_json.exists():
        logger.error(f"Reference JSON not found: {reference_json}")
        raise FileNotFoundError(f"Missing: {reference_json}")
    
    if not universe_csv.exists():
        logger.error(f"Fund universe not found: {universe_csv}")
        raise FileNotFoundError(f"Missing: {universe_csv}")
    
    # Load security reference
    securities = load_security_reference(reference_json)
    
    # Filter securities
    filtered_securities = filter_securities(securities)
    
    # Build lookup
    security_lookup = build_symbol_lookup(filtered_securities)
    
    # Load fund universe
    fund_symbols = load_fund_universe(universe_csv)
    
    # Match symbols
    matched_pairs, missing_symbols = match_symbols(fund_symbols, security_lookup)
    
    # MANDATORY VALIDATION: All symbols must match
    if missing_symbols:
        logger.error("=" * 60)
        logger.error("VALIDATION FAILED")
        logger.error("=" * 60)
        logger.error(f"The following {len(missing_symbols)} symbols from fund_universe.csv")
        logger.error("were NOT found in the security reference:")
        for symbol in missing_symbols:
            logger.error(f"  - {symbol}")
        logger.error("")
        logger.error("Possible causes:")
        logger.error("  1. Symbol mismatch (spelling/format)")
        logger.error("  2. Security not in reference snapshot")
        logger.error("  3. Reference data needs update")
        logger.error("")
        logger.error("Script FAILED - no mapping file created")
        raise ValueError(f"{len(missing_symbols)} symbols not found in reference data")
    
    # Save mapping
    save_mapping(matched_pairs, output_csv)
    
    # Success summary
    logger.info("")
    logger.info("=" * 60)
    logger.info("SUCCESS")
    logger.info("=" * 60)
    logger.info(f"✓ All {len(fund_symbols)} fund symbols mapped successfully")
    logger.info(f"✓ Mapping saved to: {output_csv}")
    logger.info(f"✓ Source: NEPSE security master snapshot")
    logger.info(f"✓ Ready for downstream price scrapers")
    logger.info("=" * 60)


if __name__ == '__main__':
    main()
