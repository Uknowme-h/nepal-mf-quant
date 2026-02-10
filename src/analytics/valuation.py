"""
Mutual Fund Valuation Analytics Pipeline

Combines monthly NAV data with daily market prices to identify:
- Funds trading at a discount to NAV (value opportunities)
- Sufficient liquidity for execution

This is a pure valuation analysis - no prediction or ML.
"""

import pandas as pd
import logging
from pathlib import Path
from typing import Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MutualFundValuation:
    """
    Analyzes closed-end mutual fund valuation based on NAV vs market price.
    
    Key metrics:
    - discount_pct: Measures how far market price deviates from NAV
        - Negative = trading below NAV (potential value)
        - Positive = trading above NAV (premium)
    - volume: Daily liquidity indicator (can you execute a trade?)
    """
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.nav_dir = project_root / 'data' / 'raw' / 'nav'
        self.price_path = project_root / 'data' / 'raw' / 'market_prices.csv'
        self.snapshot_path = project_root / 'data' / 'processed' / 'mf_daily_snapshot.csv'
        self.ranked_path = project_root / 'data' / 'processed' / 'mf_ranked_today.csv'
        
    def load_nav_files(self) -> pd.DataFrame:
        """
        Load all NAV CSV files from data/raw/nav/ directory.
        
        Each fund has its own CSV file named after the symbol (e.g., C30MF.csv)
        with columns: date, nav, source
        
        The symbol is extracted from the filename and added to the DataFrame.
        
        Returns:
            Combined DataFrame with columns: date, symbol, nav, source
        """
        if not self.nav_dir.exists():
            raise FileNotFoundError(f"NAV directory not found: {self.nav_dir}")
        
        nav_files = list(self.nav_dir.glob('*.csv'))
        
        if not nav_files:
            raise FileNotFoundError(f"No NAV CSV files found in {self.nav_dir}")
        
        logger.info(f"Loading NAV data from {len(nav_files)} fund files...")
        
        # Load and combine all NAV files
        nav_dataframes = []
        for nav_file in nav_files:
            try:
                df = pd.read_csv(nav_file)
                df['date'] = pd.to_datetime(df['date'])
                
                # Extract symbol from filename (e.g., C30MF.csv -> C30MF)
                symbol = nav_file.stem  # Gets filename without extension
                df['symbol'] = symbol
                
                nav_dataframes.append(df)
            except Exception as e:
                logger.warning(f"Failed to load {nav_file.name}: {e}")
        
        if not nav_dataframes:
            raise ValueError("No valid NAV files could be loaded")
        
        # Combine all NAV data
        combined_nav = pd.concat(nav_dataframes, ignore_index=True)
        
        # Sort by date for proper as-of joining
        combined_nav = combined_nav.sort_values(['symbol', 'date'])
        
        logger.info(f"✓ Loaded {len(combined_nav)} NAV records from {len(nav_files)} files")
        
        return combined_nav
    
    def load_data(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Load NAV and market price data.
        
        NAV data: Read from individual fund CSV files in data/raw/nav/
        Price data: Read from consolidated market_prices.csv
        
        Returns:
            Tuple of (nav_df, price_df)
        """
        logger.info("=" * 80)
        logger.info("Loading Data")
        logger.info("=" * 80)
        
        # Load NAV data from individual fund files
        nav_df = self.load_nav_files()
        logger.info(f"  Symbols: {nav_df['symbol'].nunique()}")
        logger.info(f"  Date range: {nav_df['date'].min().date()} to {nav_df['date'].max().date()}")
        
        # Load market price data
        if not self.price_path.exists():
            raise FileNotFoundError(f"Market price file not found: {self.price_path}")
        
        price_df = pd.read_csv(self.price_path)
        price_df['date'] = pd.to_datetime(price_df['date'])
        logger.info(f"✓ Loaded {len(price_df)} market price records")
        logger.info(f"  Symbols: {price_df['symbol'].nunique()}")
        logger.info(f"  Date range: {price_df['date'].min().date()} to {price_df['date'].max().date()}")
        
        return nav_df, price_df
    
    def join_nav_and_prices(
        self, 
        nav_df: pd.DataFrame, 
        price_df: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Join monthly NAV data with daily price data.
        
        For each (date, symbol) in prices:
        - Use the most recent NAV available on or before that date
        - Drop rows where NAV or price is missing
        
        This is called an "as-of join" or "point-in-time join".
        It prevents look-ahead bias (using future NAV data).
        
        Args:
            nav_df: DataFrame with columns [date, symbol, nav]
            price_df: DataFrame with columns [date, symbol, ltp, ...]
            
        Returns:
            Merged DataFrame with NAV joined to each price record
        """
        logger.info("")
        logger.info("=" * 80)
        logger.info("Joining NAV and Price Data")
        logger.info("=" * 80)
        
        # Sort NAV data by date for proper as-of join
        nav_df = nav_df.sort_values('date')
        price_df = price_df.sort_values('date')
        
        # Perform merge_asof for each symbol
        # This joins the most recent NAV on or before each price date
        merged = pd.merge_asof(
            price_df.sort_values('date'),
            nav_df[['date', 'symbol', 'nav']].sort_values('date'),
            on='date',
            by='symbol',
            direction='backward',  # Use NAV on or before price date
            suffixes=('', '_nav')
        )
        
        # Count missing data
        missing_nav = merged['nav'].isna().sum()
        missing_price = merged['ltp'].isna().sum()
        
        logger.info(f"Before filtering:")
        logger.info(f"  Total rows: {len(merged)}")
        logger.info(f"  Missing NAV: {missing_nav}")
        logger.info(f"  Missing price: {missing_price}")
        
        # Drop rows with missing NAV or price
        initial_count = len(merged)
        merged = merged.dropna(subset=['nav', 'ltp'])
        dropped = initial_count - len(merged)
        
        logger.info(f"\nAfter filtering:")
        logger.info(f"  Valid rows: {len(merged)}")
        logger.info(f"  Dropped: {dropped}")
        
        # Check for duplicates
        duplicates = merged.duplicated(subset=['date', 'symbol']).sum()
        if duplicates > 0:
            logger.warning(f"⚠ Found {duplicates} duplicate (date, symbol) pairs - removing")
            merged = merged.drop_duplicates(subset=['date', 'symbol'], keep='first')
        
        logger.info(f"✓ Final merged dataset: {len(merged)} rows")
        
        return merged
    
    def calculate_discount(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate discount/premium to NAV.
        
        discount_pct = (ltp - nav) / nav
        
        Interpretation:
        - discount_pct < 0: Trading below NAV (discount, potential value)
        - discount_pct > 0: Trading above NAV (premium, expensive)
        - discount_pct = 0: Trading at fair value
        
        Why this matters:
        Closed-end funds have a NAV (intrinsic value) and a market price.
        If price < NAV, you're buying assets at a discount.
        
        Args:
            df: DataFrame with 'ltp' and 'nav' columns
            
        Returns:
            DataFrame with 'discount_pct' column added
        """
        logger.info("")
        logger.info("=" * 80)
        logger.info("Calculating Valuation Metrics")
        logger.info("=" * 80)
        
        # Calculate discount percentage
        df['discount_pct'] = ((df['ltp'] - df['nav']) / df['nav']) * 100
        
        # Summary statistics
        logger.info(f"Discount Statistics:")
        logger.info(f"  Mean: {df['discount_pct'].mean():.2f}%")
        logger.info(f"  Median: {df['discount_pct'].median():.2f}%")
        logger.info(f"  Min (best value): {df['discount_pct'].min():.2f}%")
        logger.info(f"  Max (most expensive): {df['discount_pct'].max():.2f}%")
        
        # Count funds at discount vs premium
        at_discount = (df['discount_pct'] < 0).sum()
        at_premium = (df['discount_pct'] > 0).sum()
        at_nav = (df['discount_pct'] == 0).sum()
        
        logger.info(f"\nValuation Distribution:")
        logger.info(f"  Trading below NAV (discount): {at_discount}")
        logger.info(f"  Trading above NAV (premium): {at_premium}")
        logger.info(f"  Trading at NAV: {at_nav}")
        
        return df
    
    def save_daily_snapshot(self, df: pd.DataFrame) -> None:
        """
        Save daily valuation snapshot.
        
        Output columns: date, symbol, nav, ltp, discount_pct, volume, trades, source
        
        Args:
            df: Complete merged and calculated dataset
        """
        # Ensure output directory exists
        self.snapshot_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Select and order columns
        output_cols = ['date', 'symbol', 'nav', 'ltp', 'discount_pct', 'volume', 'trades', 'source']
        snapshot = df[output_cols].copy()
        
        # Convert date to string for CSV
        snapshot['date'] = snapshot['date'].dt.strftime('%Y-%m-%d')
        
        # Round numeric columns
        snapshot['nav'] = snapshot['nav'].round(2)
        snapshot['ltp'] = snapshot['ltp'].round(2)
        snapshot['discount_pct'] = snapshot['discount_pct'].round(2)
        
        # Save
        snapshot.to_csv(self.snapshot_path, index=False)
        logger.info(f"✓ Saved daily snapshot: {self.snapshot_path}")
        logger.info(f"  Records: {len(snapshot)}")
    
    def apply_liquidity_filter(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Filter funds by liquidity (daily trading volume).
        
        Why liquidity matters:
        A fund might trade at a huge discount, but if volume is tiny,
        you can't execute a meaningful position without moving the price.
        
        Filter: Keep funds with volume >= median(volume)
        This ensures we can actually trade these funds.
        
        Args:
            df: DataFrame with 'volume' column
            
        Returns:
            Filtered DataFrame with sufficient liquidity
        """
        logger.info("")
        logger.info("=" * 80)
        logger.info("Applying Liquidity Filter")
        logger.info("=" * 80)
        
        median_volume = df['volume'].median()
        logger.info(f"Median daily volume: {median_volume:,.0f}")
        
        initial_count = len(df)
        filtered = df[df['volume'] >= median_volume].copy()
        removed = initial_count - len(filtered)
        
        logger.info(f"Before filter: {initial_count} funds")
        logger.info(f"After filter: {len(filtered)} funds")
        logger.info(f"Removed: {removed} (insufficient liquidity)")
        
        return filtered
    
    def rank_by_valuation(
        self, 
        df: pd.DataFrame, 
        top_n: int = 10
    ) -> pd.DataFrame:
        """
        Rank funds by discount to NAV (most negative first).
        
        Returns top N funds with:
        - Largest discount to NAV (best value)
        - Sufficient liquidity
        
        Args:
            df: Liquidity-filtered DataFrame
            top_n: Number of top funds to return (default: 10)
            
        Returns:
            Top N funds sorted by discount_pct (ascending)
        """
        logger.info("")
        logger.info("=" * 80)
        logger.info("Ranking Funds by Valuation")
        logger.info("=" * 80)
        
        # Sort by discount (most negative first = best value)
        ranked = df.sort_values('discount_pct', ascending=True).copy()
        
        # Take top N
        top_funds = ranked.head(top_n)
        
        logger.info(f"Top {len(top_funds)} funds by discount:")
        logger.info("")
        logger.info(f"{'Rank':<6}{'Symbol':<12}{'Discount':<12}{'Volume':<12}{'NAV':<10}{'LTP':<10}")
        logger.info("-" * 72)
        
        for idx, (_, row) in enumerate(top_funds.iterrows(), 1):
            logger.info(
                f"{idx:<6}{row['symbol']:<12}{row['discount_pct']:>8.2f}%   "
                f"{row['volume']:>9,.0f}   {row['nav']:>7.2f}   {row['ltp']:>7.2f}"
            )
        
        return top_funds
    
    def save_ranked_output(self, df: pd.DataFrame) -> None:
        """
        Save ranked fund list for decision-making.
        
        Args:
            df: Ranked DataFrame
        """
        # Ensure output directory exists
        self.ranked_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Select columns
        output_cols = ['date', 'symbol', 'nav', 'ltp', 'discount_pct', 'volume', 'trades', 'source']
        output = df[output_cols].copy()
        
        # Convert date to string
        output['date'] = output['date'].dt.strftime('%Y-%m-%d')
        
        # Round numeric columns
        output['nav'] = output['nav'].round(2)
        output['ltp'] = output['ltp'].round(2)
        output['discount_pct'] = output['discount_pct'].round(2)
        
        # Save
        output.to_csv(self.ranked_path, index=False)
        logger.info("")
        logger.info(f"✓ Saved ranked output: {self.ranked_path}")
        logger.info(f"  Records: {len(output)}")
    
    def run(self, top_n: int = 10) -> None:
        """
        Execute complete valuation pipeline.
        
        Args:
            top_n: Number of top funds to output (default: 10)
        """
        logger.info("")
        logger.info("=" * 80)
        logger.info("MUTUAL FUND VALUATION PIPELINE")
        logger.info("=" * 80)
        logger.info("")
        
        try:
            # Step 1: Load data
            nav_df, price_df = self.load_data()
            
            # Step 2: Join NAV and prices (as-of join for point-in-time correctness)
            merged = self.join_nav_and_prices(nav_df, price_df)
            
            # Step 3: Calculate discount to NAV
            merged = self.calculate_discount(merged)
            
            # Step 4: Save complete daily snapshot
            self.save_daily_snapshot(merged)
            
            # Step 5: Apply liquidity filter
            liquid_funds = self.apply_liquidity_filter(merged)
            
            # Step 6: Rank by valuation
            top_funds = self.rank_by_valuation(liquid_funds, top_n=top_n)
            
            # Step 7: Save ranked output
            self.save_ranked_output(top_funds)
            
            # Summary
            logger.info("")
            logger.info("=" * 80)
            logger.info("PIPELINE COMPLETE")
            logger.info("=" * 80)
            logger.info(f"✓ Daily snapshot: {self.snapshot_path}")
            logger.info(f"✓ Ranked funds: {self.ranked_path}")
            logger.info("")
            logger.info("Next steps:")
            logger.info("  1. Review top-ranked funds")
            logger.info("  2. Verify liquidity is sufficient for your position size")
            logger.info("  3. Consider other factors (fund strategy, expense ratio, etc.)")
            logger.info("=" * 80)
            
        except Exception as e:
            logger.error("")
            logger.error("=" * 80)
            logger.error("PIPELINE FAILED")
            logger.error("=" * 80)
            logger.error(f"Error: {e}")
            logger.error("=" * 80)
            raise


def main():
    """Entry point"""
    project_root = Path(__file__).parent.parent.parent
    pipeline = MutualFundValuation(project_root)
    pipeline.run(top_n=10)


if __name__ == '__main__':
    main()
