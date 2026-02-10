"""
Investment Decision Layer for Closed-End Mutual Funds

Converts valuation metrics into rule-based screening decisions.
This is NOT prediction - it's a deterministic classification system.

Decision Logic:
- Valuation: How cheap is the fund vs NAV?
- Liquidity: Can you actually trade it?
- Maturity: Time horizon alignment
- Action: Should you consider this fund?
"""

import pandas as pd
import numpy as np
import logging
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class InvestmentDecisionLayer:
    """
    Rule-based decision system for mutual fund screening.
    
    Converts quantitative metrics into actionable classifications.
    """
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.snapshot_path = project_root / 'data' / 'processed' / 'mf_daily_snapshot.csv'
        self.universe_path = project_root / 'data' / 'raw' / 'fund_universe.csv'
        self.output_path = project_root / 'data' / 'processed' / 'mf_decision_table.csv'
    
    def load_data(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        """
        Load valuation snapshot and fund universe data.
        
        Returns:
            Tuple of (snapshot_df, universe_df)
        """
        logger.info("=" * 80)
        logger.info("Loading Data")
        logger.info("=" * 80)
        
        # Load daily snapshot
        if not self.snapshot_path.exists():
            raise FileNotFoundError(f"Snapshot not found: {self.snapshot_path}")
        
        snapshot = pd.read_csv(self.snapshot_path)
        snapshot['date'] = pd.to_datetime(snapshot['date'])
        logger.info(f"✓ Loaded {len(snapshot)} records from daily snapshot")
        
        # Load fund universe
        if not self.universe_path.exists():
            raise FileNotFoundError(f"Fund universe not found: {self.universe_path}")
        
        universe = pd.read_csv(self.universe_path)
        logger.info(f"✓ Loaded {len(universe)} funds from universe")
        
        return snapshot, universe
    
    def calculate_years_to_maturity(
        self, 
        df: pd.DataFrame, 
        universe: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Calculate years remaining until fund maturity.
        
        Why this matters:
        - Closed-end funds have fixed maturity dates
        - At maturity, market price converges to NAV (discount disappears)
        - Shorter maturity = faster NAV realization = lower risk
        - We prefer funds maturing within 4 years (manageable horizon)
        
        Args:
            df: Daily snapshot with 'date' and 'symbol'
            universe: Fund universe with 'symbol' and 'maturity_date'
            
        Returns:
            DataFrame with 'maturity_date' and 'years_to_maturity' added
        """
        logger.info("")
        logger.info("=" * 80)
        logger.info("Calculating Time to Maturity")
        logger.info("=" * 80)
        
        # Merge maturity dates
        df = df.merge(
            universe[['symbol', 'maturity_date']], 
            on='symbol', 
            how='left'
        )
        
        # Convert maturity date to datetime
        df['maturity_date'] = pd.to_datetime(df['maturity_date'], errors='coerce')
        
        # Count missing maturity dates
        missing_maturity = df['maturity_date'].isna().sum()
        if missing_maturity > 0:
            logger.warning(f"⚠ {missing_maturity} funds missing maturity_date - will be dropped")
        
        # Drop funds without maturity date
        initial_count = len(df)
        df = df.dropna(subset=['maturity_date'])
        dropped = initial_count - len(df)
        
        if dropped > 0:
            logger.info(f"Dropped {dropped} funds without maturity_date")
        
        # Calculate days and years to maturity
        df['days_to_maturity'] = (df['maturity_date'] - df['date']).dt.days
        df['years_to_maturity'] = (df['days_to_maturity'] / 365.0).round(2)
        
        # Log summary
        logger.info(f"\nYears to Maturity Statistics:")
        logger.info(f"  Min: {df['years_to_maturity'].min():.2f} years")
        logger.info(f"  Max: {df['years_to_maturity'].max():.2f} years")
        logger.info(f"  Mean: {df['years_to_maturity'].mean():.2f} years")
        logger.info(f"  Median: {df['years_to_maturity'].median():.2f} years")
        
        # Count funds by maturity horizon
        near_term = (df['years_to_maturity'] <= 2).sum()
        mid_term = ((df['years_to_maturity'] > 2) & (df['years_to_maturity'] <= 4)).sum()
        long_term = (df['years_to_maturity'] > 4).sum()
        
        logger.info(f"\nMaturity Horizons:")
        logger.info(f"  Near-term (<= 2 years): {near_term}")
        logger.info(f"  Mid-term (2-4 years): {mid_term}")
        logger.info(f"  Long-term (> 4 years): {long_term}")
        
        return df
    
    def classify_valuation(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Classify funds into valuation buckets based on discount to NAV.
        
        Why these thresholds:
        - Deep discount (<= -8%): Significant undervaluation, strong value signal
        - Moderate discount (-8% to -4%): Notable discount, good value
        - Small discount (-4% to 0%): Mild discount, marginal value
        - Premium (>= 0%): Trading at or above NAV, no discount benefit
        
        Thresholds based on:
        - Historical Nepal CEF discount patterns
        - Risk/reward balance
        - Practical trading significance
        
        Args:
            df: DataFrame with 'discount_pct' column
            
        Returns:
            DataFrame with 'valuation_bucket' added
        """
        logger.info("")
        logger.info("=" * 80)
        logger.info("Classifying Valuation")
        logger.info("=" * 80)
        
        def bucket_valuation(discount):
            """Apply valuation classification rules"""
            if discount <= -8:
                return "deep_discount"
            elif discount <= -4:
                return "moderate_discount"
            elif discount < 0:
                return "small_discount"
            else:
                return "premium"
        
        df['valuation_bucket'] = df['discount_pct'].apply(bucket_valuation)
        
        # Count funds in each bucket
        bucket_counts = df['valuation_bucket'].value_counts()
        
        logger.info("Valuation Distribution:")
        for bucket in ['deep_discount', 'moderate_discount', 'small_discount', 'premium']:
            count = bucket_counts.get(bucket, 0)
            pct = (count / len(df) * 100) if len(df) > 0 else 0
            logger.info(f"  {bucket:<20}: {count:>3} ({pct:>5.1f}%)")
        
        return df
    
    def classify_liquidity(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Classify funds into liquidity buckets using volume percentiles.
        
        Why percentile-based:
        - Absolute volume thresholds become outdated
        - Percentiles adapt to market conditions
        - Relative ranking captures tradability within current market
        
        Buckets:
        - High (top 25%): Most liquid, easy execution
        - Medium (middle 50%): Adequate liquidity for most trades
        - Low (bottom 25%): Difficult execution, price impact risk
        
        Why liquidity matters:
        A fund at -10% discount with 100 shares/day volume is useless.
        You need sufficient liquidity to actually execute the trade.
        
        Args:
            df: DataFrame with 'volume' column
            
        Returns:
            DataFrame with 'liquidity_bucket' added
        """
        logger.info("")
        logger.info("=" * 80)
        logger.info("Classifying Liquidity")
        logger.info("=" * 80)
        
        # Calculate volume percentiles for this day
        # (If multiple days, group by date - but current data is single day)
        p25 = df['volume'].quantile(0.25)
        p75 = df['volume'].quantile(0.75)
        
        logger.info(f"Volume Percentiles:")
        logger.info(f"  25th percentile: {p25:,.0f} shares")
        logger.info(f"  75th percentile: {p75:,.0f} shares")
        
        def bucket_liquidity(volume):
            """Apply liquidity classification rules"""
            if volume >= p75:
                return "high"
            elif volume >= p25:
                return "medium"
            else:
                return "low"
        
        df['liquidity_bucket'] = df['volume'].apply(bucket_liquidity)
        
        # Count funds in each bucket
        bucket_counts = df['liquidity_bucket'].value_counts()
        
        logger.info("\nLiquidity Distribution:")
        for bucket in ['high', 'medium', 'low']:
            count = bucket_counts.get(bucket, 0)
            pct = (count / len(df) * 100) if len(df) > 0 else 0
            logger.info(f"  {bucket:<10}: {count:>3} ({pct:>5.1f}%)")
        
        return df
    
    def apply_decision_rules(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply deterministic investment screening rules.
        
        Decision Logic:
        CONSIDER if ALL of:
        1. Valuation: deep_discount OR moderate_discount
           (at least -4% discount = meaningful value)
        
        2. Liquidity: NOT low
           (must be tradable - high or medium volume)
        
        3. Maturity: <= 4 years
           (reasonable horizon, discount likely to converge)
        
        Otherwise: IGNORE
        
        Why these rules:
        - Combines value (cheap) + execution (liquid) + timing (maturity)
        - Conservative: only flags clear opportunities
        - Avoids illiquid traps and overpriced funds
        - Time horizon aligns with discount convergence
        
        Args:
            df: DataFrame with classification columns
            
        Returns:
            DataFrame with 'decision_flag' added
        """
        logger.info("")
        logger.info("=" * 80)
        logger.info("Applying Decision Rules")
        logger.info("=" * 80)
        
        def make_decision(row):
            """
            Deterministic decision rule.
            
            Returns 'CONSIDER' or 'IGNORE'
            """
            # Check valuation: must be discounted meaningfully
            good_valuation = row['valuation_bucket'] in ['deep_discount', 'moderate_discount']
            
            # Check liquidity: must be tradable
            good_liquidity = row['liquidity_bucket'] != 'low'
            
            # Check maturity: must be reasonable horizon
            good_maturity = row['years_to_maturity'] <= 4
            
            # All conditions must be true
            if good_valuation and good_liquidity and good_maturity:
                return "CONSIDER"
            else:
                return "IGNORE"
        
        df['decision_flag'] = df.apply(make_decision, axis=1)
        
        # Count decisions
        consider_count = (df['decision_flag'] == 'CONSIDER').sum()
        ignore_count = (df['decision_flag'] == 'IGNORE').sum()
        
        logger.info(f"\nDecision Summary:")
        logger.info(f"  CONSIDER: {consider_count} ({consider_count/len(df)*100:.1f}%)")
        logger.info(f"  IGNORE: {ignore_count} ({ignore_count/len(df)*100:.1f}%)")
        
        # Show why funds are ignored
        ignored = df[df['decision_flag'] == 'IGNORE']
        
        if len(ignored) > 0:
            logger.info(f"\nReasons for IGNORE:")
            
            # Poor valuation
            bad_val = ignored[~ignored['valuation_bucket'].isin(['deep_discount', 'moderate_discount'])]
            logger.info(f"  Not discounted enough: {len(bad_val)}")
            
            # Poor liquidity
            bad_liq = ignored[ignored['liquidity_bucket'] == 'low']
            logger.info(f"  Insufficient liquidity: {len(bad_liq)}")
            
            # Too long maturity
            bad_mat = ignored[ignored['years_to_maturity'] > 4]
            logger.info(f"  Maturity > 4 years: {len(bad_mat)}")
        
        return df
    
    def save_decision_table(self, df: pd.DataFrame) -> None:
        """
        Save decision table with exact required columns.
        
        Output columns (in order):
        - date
        - symbol
        - nav
        - ltp
        - discount_pct
        - volume
        - years_to_maturity
        - days_to_maturity
        - valuation_bucket
        - liquidity_bucket
        - decision_flag
        
        Args:
            df: Complete decision table
        """
        # Ensure output directory exists
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Select and order columns exactly as specified
        output_cols = [
            'date', 'symbol', 'nav', 'ltp', 'discount_pct', 'volume',
            'years_to_maturity', 'days_to_maturity', 'valuation_bucket', 'liquidity_bucket', 'decision_flag'
        ]
        
        output_df = df[output_cols].copy()
        
        # Convert date to string for CSV
        output_df['date'] = output_df['date'].dt.strftime('%Y-%m-%d')
        
        # Round numeric columns
        output_df['nav'] = output_df['nav'].round(2)
        output_df['ltp'] = output_df['ltp'].round(2)
        output_df['discount_pct'] = output_df['discount_pct'].round(2)
        output_df['years_to_maturity'] = output_df['years_to_maturity'].round(2)
        
        # Sort by decision flag (CONSIDER first), then by discount
        output_df = output_df.sort_values(
            ['decision_flag', 'discount_pct'], 
            ascending=[False, True]  # CONSIDER before IGNORE, deeper discount first
        ).reset_index(drop=True)
        
        # Save
        output_df.to_csv(self.output_path, index=False)
        
        logger.info("")
        logger.info(f"✓ Saved decision table: {self.output_path}")
        logger.info(f"  Total rows: {len(output_df)}")
    
    def run(self) -> None:
        """Execute complete decision layer pipeline"""
        logger.info("")
        logger.info("=" * 80)
        logger.info("MUTUAL FUND DECISION LAYER")
        logger.info("=" * 80)
        logger.info("")
        
        try:
            # Step 1: Load data
            snapshot, universe = self.load_data()
            
            # Step 2: Calculate time to maturity
            df = self.calculate_years_to_maturity(snapshot, universe)
            
            # Step 3: Classify valuation
            df = self.classify_valuation(df)
            
            # Step 4: Classify liquidity
            df = self.classify_liquidity(df)
            
            # Step 5: Apply decision rules
            df = self.apply_decision_rules(df)
            
            # Step 6: Save decision table
            self.save_decision_table(df)
            
            # Success summary
            logger.info("")
            logger.info("=" * 80)
            logger.info("DECISION LAYER COMPLETE")
            logger.info("=" * 80)
            
            # Show top CONSIDER funds
            consider_funds = df[df['decision_flag'] == 'CONSIDER'].sort_values('discount_pct')
            
            if len(consider_funds) > 0:
                logger.info(f"\n🎯 Top Funds to CONSIDER ({len(consider_funds)} total):")
                logger.info("")
                logger.info(f"{'Symbol':<12}{'Discount':<12}{'Liquidity':<12}{'Maturity':<12}{'Reason'}")
                logger.info("-" * 72)
                
                for _, row in consider_funds.head(5).iterrows():
                    reason = f"{row['valuation_bucket']}, {row['years_to_maturity']:.1f}y"
                    logger.info(
                        f"{row['symbol']:<12}{row['discount_pct']:>8.2f}%   "
                        f"{row['liquidity_bucket']:<12}{row['years_to_maturity']:>7.2f}y   {reason}"
                    )
            else:
                logger.info("\n⚠ No funds meet CONSIDER criteria today")
            
            logger.info("")
            logger.info("=" * 80)
            logger.info("Next Steps:")
            logger.info("  1. Review CONSIDER funds in: data/processed/mf_decision_table.csv")
            logger.info("  2. Conduct additional due diligence (fund strategy, expenses)")
            logger.info("  3. Verify position size aligns with liquidity")
            logger.info("  4. Consider market conditions and personal investment goals")
            logger.info("=" * 80)
            
        except Exception as e:
            logger.error("")
            logger.error("=" * 80)
            logger.error("DECISION LAYER FAILED")
            logger.error("=" * 80)
            logger.error(f"Error: {e}")
            logger.error("=" * 80)
            raise


def main():
    """Entry point"""
    project_root = Path(__file__).parent.parent.parent
    pipeline = InvestmentDecisionLayer(project_root)
    pipeline.run()


if __name__ == '__main__':
    main()
