"""
Decision History Tracker for Closed-End Mutual Funds

Maintains an append-only temporal log of investment decisions.
This enables persistence analysis (NOT prediction).

Key Properties:
- Append-only (never overwrites)
- Idempotent (safe to run multiple times per day)
- No historical mutation
- Source of truth: mf_decision_table.csv only
"""

import pandas as pd
import logging
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DecisionHistoryTracker:
    """
    Append-only history tracker for decision flags.
    
    Tracks decision persistence over time without prediction.
    """
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.decision_table_path = project_root / 'data' / 'processed' / 'mf_decision_table.csv'
        self.history_path = project_root / 'data' / 'history' / 'mf_decision_history.csv'
        
        # Columns to extract from decision table
        self.history_cols = [
            'date', 'symbol', 'discount_pct', 'days_to_maturity', 
            'liquidity_bucket', 'decision_flag'
        ]
    
    def load_current_decisions(self) -> pd.DataFrame:
        """
        Load today's decision table.
        
        Returns:
            DataFrame with current decisions
        """
        if not self.decision_table_path.exists():
            raise FileNotFoundError(
                f"Decision table not found: {self.decision_table_path}\n"
                f"Run decision_layer.py first to generate today's decisions."
            )
        
        df = pd.read_csv(self.decision_table_path)
        df['date'] = pd.to_datetime(df['date'])
        
        logger.info(f"✓ Loaded {len(df)} decisions from today's table")
        logger.info(f"  Date: {df['date'].iloc[0].strftime('%Y-%m-%d')}")
        logger.info(f"  Symbols: {len(df['symbol'].unique())}")
        
        # Select only history columns
        df_history = df[self.history_cols].copy()
        
        return df_history
    
    def load_existing_history(self) -> pd.DataFrame:
        """
        Load existing history file if it exists.
        
        Returns:
            DataFrame with historical records, or empty DataFrame if file doesn't exist
        """
        if not self.history_path.exists():
            logger.info(f"✓ History file does not exist yet (first run)")
            logger.info(f"  Will create: {self.history_path}")
            return pd.DataFrame(columns=self.history_cols)
        
        df = pd.read_csv(self.history_path)
        df['date'] = pd.to_datetime(df['date'])
        
        logger.info(f"✓ Loaded existing history")
        logger.info(f"  Total records: {len(df)}")
        logger.info(f"  Date range: {df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}")
        logger.info(f"  Unique dates: {df['date'].nunique()}")
        logger.info(f"  Unique symbols: {df['symbol'].nunique()}")
        
        return df
    
    def identify_new_records(
        self, 
        current: pd.DataFrame, 
        history: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Identify records from current decisions that don't exist in history.
        
        Idempotency logic:
        - Skip records where (date, symbol) already exists in history
        - This prevents duplicate entries if script runs multiple times per day
        
        Args:
            current: Today's decisions
            history: Historical records
            
        Returns:
            DataFrame with only new records to append
        """
        if len(history) == 0:
            logger.info(f"✓ All {len(current)} records are new (first run)")
            return current
        
        # Create composite key for deduplication
        current['_key'] = current['date'].astype(str) + '_' + current['symbol']
        history['_key'] = history['date'].astype(str) + '_' + history['symbol']
        
        # Find records not in history
        new_records = current[~current['_key'].isin(history['_key'])].copy()
        
        # Remove temporary key column
        new_records = new_records.drop(columns=['_key'])
        
        # Log statistics
        duplicate_count = len(current) - len(new_records)
        
        logger.info(f"\nIdempotency Check:")
        logger.info(f"  Current records: {len(current)}")
        logger.info(f"  Already in history: {duplicate_count}")
        logger.info(f"  New records to append: {len(new_records)}")
        
        if duplicate_count > 0:
            logger.info(f"\n⚠ Skipped {duplicate_count} duplicate (date, symbol) pairs")
            logger.info(f"  This is expected if running multiple times per day")
        
        return new_records
    
    def append_to_history(
        self, 
        new_records: pd.DataFrame, 
        existing_history: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Append new records to history.
        
        This does NOT overwrite the file yet - that happens in save_history().
        
        Args:
            new_records: Records to append
            existing_history: Current history
            
        Returns:
            Combined DataFrame
        """
        if len(new_records) == 0:
            logger.info("\n✓ No new records to append (already up to date)")
            return existing_history
        
        # Concatenate
        combined = pd.concat([existing_history, new_records], ignore_index=True)
        
        # Remove temporary key column if it exists
        if '_key' in combined.columns:
            combined = combined.drop(columns=['_key'])
        
        # Sort by date, then symbol
        combined = combined.sort_values(['date', 'symbol']).reset_index(drop=True)
        
        logger.info(f"\n✓ Prepared {len(new_records)} records for append")
        
        return combined
    
    def save_history(self, df: pd.DataFrame) -> None:
        """
        Save history to CSV file.
        
        Args:
            df: Complete history DataFrame
        """
        # Ensure directory exists
        self.history_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Convert date to string for CSV
        df_output = df.copy()
        df_output['date'] = df_output['date'].dt.strftime('%Y-%m-%d')
        
        # Round numeric columns
        df_output['discount_pct'] = df_output['discount_pct'].round(2)
        
        # Save
        df_output.to_csv(self.history_path, index=False)
        
        logger.info(f"\n✓ Saved history: {self.history_path}")
        logger.info(f"  Total records: {len(df_output)}")
    
    def calculate_consider_streaks(self, history: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate consecutive CONSIDER days for each symbol.
        
        This is for inspection/logging only, NOT saved to file.
        
        Why this matters:
        - Persistent CONSIDER = reliable opportunity (discount hasn't converged)
        - Single-day CONSIDER = possibly noise
        - Streak length indicates signal stability
        
        Args:
            history: Complete history DataFrame
            
        Returns:
            DataFrame with symbol and current consider_streak
        """
        if len(history) == 0:
            logger.info("\n⚠ No history to calculate streaks")
            return pd.DataFrame(columns=['symbol', 'consider_streak'])
        
        logger.info("")
        logger.info("=" * 80)
        logger.info("Calculating Persistence Metrics (Inspection Only)")
        logger.info("=" * 80)
        
        # Sort by symbol and date
        df = history.sort_values(['symbol', 'date']).copy()
        
        # Create binary CONSIDER flag
        df['is_consider'] = (df['decision_flag'] == 'CONSIDER').astype(int)
        
        # Calculate streak for each symbol
        # Reset streak counter when decision changes
        df['streak_reset'] = (
            df.groupby('symbol')['is_consider']
            .diff()
            .fillna(0) != 0
        ).astype(int)
        
        df['streak_group'] = df.groupby('symbol')['streak_reset'].cumsum()
        
        # Count consecutive days within each streak group
        df['streak_length'] = df.groupby(['symbol', 'streak_group']).cumcount() + 1
        
        # Only keep CONSIDER streaks (ignore IGNORE streaks)
        df['consider_streak'] = df['is_consider'] * df['streak_length']
        
        # Get most recent streak for each symbol
        latest_date = df['date'].max()
        latest_streaks = df[df['date'] == latest_date][['symbol', 'consider_streak']].copy()
        
        # Sort by streak length (longest first)
        latest_streaks = latest_streaks.sort_values('consider_streak', ascending=False)
        
        # Log top persistent CONSIDER funds
        consider_funds = latest_streaks[latest_streaks['consider_streak'] > 0]
        
        if len(consider_funds) > 0:
            logger.info(f"\nPersistent CONSIDER Funds (as of {latest_date.strftime('%Y-%m-%d')}):")
            logger.info("")
            logger.info(f"{'Symbol':<12}{'Days CONSIDER':<20}{'Interpretation'}")
            logger.info("-" * 70)
            
            for _, row in consider_funds.head(10).iterrows():
                symbol = row['symbol']
                streak = int(row['consider_streak'])
                
                if streak == 1:
                    interpretation = "New signal (first day)"
                elif streak <= 3:
                    interpretation = "Emerging pattern"
                elif streak <= 7:
                    interpretation = "Short-term persistence"
                else:
                    interpretation = "Strong persistence (sticky discount)"
                
                logger.info(f"{symbol:<12}{streak:<20}{interpretation}")
        else:
            logger.info(f"\n⚠ No funds currently flagged as CONSIDER")
        
        # Log statistics
        total_days = history['date'].nunique()
        logger.info(f"\nHistory Statistics:")
        logger.info(f"  Total days tracked: {total_days}")
        logger.info(f"  Unique symbols seen: {history['symbol'].nunique()}")
        logger.info(f"  Current CONSIDER funds: {len(consider_funds)}")
        
        if len(consider_funds) > 0:
            avg_streak = consider_funds['consider_streak'].mean()
            max_streak = consider_funds['consider_streak'].max()
            logger.info(f"  Average CONSIDER streak: {avg_streak:.1f} days")
            logger.info(f"  Longest current streak: {int(max_streak)} days")
        
        return latest_streaks
    
    def run(self) -> None:
        """Execute complete history tracking pipeline"""
        logger.info("")
        logger.info("=" * 80)
        logger.info("DECISION HISTORY TRACKER")
        logger.info("=" * 80)
        logger.info("")
        
        try:
            # Step 1: Load current decisions
            logger.info("=" * 80)
            logger.info("Step 1: Load Current Decisions")
            logger.info("=" * 80)
            current = self.load_current_decisions()
            
            # Step 2: Load existing history
            logger.info("")
            logger.info("=" * 80)
            logger.info("Step 2: Load Existing History")
            logger.info("=" * 80)
            existing = self.load_existing_history()
            
            # Step 3: Identify new records (idempotency)
            logger.info("")
            logger.info("=" * 80)
            logger.info("Step 3: Identify New Records")
            logger.info("=" * 80)
            new_records = self.identify_new_records(current, existing)
            
            # Step 4: Append to history
            logger.info("")
            logger.info("=" * 80)
            logger.info("Step 4: Append to History")
            logger.info("=" * 80)
            updated_history = self.append_to_history(new_records, existing)
            
            # Step 5: Save history
            logger.info("")
            logger.info("=" * 80)
            logger.info("Step 5: Save History")
            logger.info("=" * 80)
            self.save_history(updated_history)
            
            # Step 6: Calculate persistence metrics (inspection only)
            if len(updated_history) > 0:
                self.calculate_consider_streaks(updated_history)
            
            # Success summary
            logger.info("")
            logger.info("=" * 80)
            logger.info("HISTORY TRACKING COMPLETE")
            logger.info("=" * 80)
            
            logger.info(f"\n✓ History file: {self.history_path}")
            logger.info(f"✓ Total records: {len(updated_history)}")
            logger.info(f"✓ Records appended this run: {len(new_records)}")
            
            if len(new_records) > 0:
                logger.info(f"\n📊 Breakdown of appended records:")
                new_consider = (new_records['decision_flag'] == 'CONSIDER').sum()
                new_ignore = (new_records['decision_flag'] == 'IGNORE').sum()
                logger.info(f"  CONSIDER: {new_consider}")
                logger.info(f"  IGNORE: {new_ignore}")
            
            logger.info("")
            logger.info("=" * 80)
            logger.info("Purpose:")
            logger.info("  This history enables analysis of:")
            logger.info("  - Persistent discounts (sticky CONSIDER funds)")
            logger.info("  - Decision stability over time")
            logger.info("  - False positives vs real opportunities")
            logger.info("  - Discount convergence patterns")
            logger.info("=" * 80)
            
        except Exception as e:
            logger.error("")
            logger.error("=" * 80)
            logger.error("HISTORY TRACKING FAILED")
            logger.error("=" * 80)
            logger.error(f"Error: {e}")
            logger.error("=" * 80)
            raise


def main():
    """Entry point"""
    project_root = Path(__file__).parent.parent.parent
    tracker = DecisionHistoryTracker(project_root)
    tracker.run()


if __name__ == '__main__':
    main()
