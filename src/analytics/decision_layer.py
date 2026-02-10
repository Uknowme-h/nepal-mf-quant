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
        self.scored_path = project_root / 'data' / 'processed' / 'mf_scored.csv'
        self.risk_path = project_root / 'data' / 'processed' / 'mf_risk_metrics.csv'
        self.returns_path = project_root / 'data' / 'processed' / 'mf_returns.csv'
        self.output_path = project_root / 'data' / 'processed' / 'mf_decision_table.csv'
    
    def load_data(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        """
        Load valuation snapshot and fund universe data.
        Filters snapshot to latest date only (fixes multi-date leakage).
        
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
        
        # Filter to latest date only — prevents stale multi-date decisions
        latest_date = snapshot['date'].max()
        snapshot = snapshot[snapshot['date'] == latest_date].copy()
        logger.info(f"✓ Loaded {len(snapshot)} records from daily snapshot (date: {latest_date.date()})")
        
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
            
            Returns ('CONSIDER'/'IGNORE', 'reason_string')
            """
            reasons = []
            
            # Check valuation: must be discounted meaningfully
            good_valuation = row['valuation_bucket'] in ['deep_discount', 'moderate_discount']
            if not good_valuation:
                reasons.append(f"valuation:{row['valuation_bucket']}")
            
            # Check liquidity: must be tradable
            good_liquidity = row['liquidity_bucket'] != 'low'
            if not good_liquidity:
                reasons.append("liquidity:low")
            
            # Check maturity: must be reasonable horizon
            good_maturity = row['years_to_maturity'] <= 4
            if not good_maturity:
                reasons.append(f"maturity:{row['years_to_maturity']:.1f}y")
            
            if good_valuation and good_liquidity and good_maturity:
                return "CONSIDER", ""
            else:
                return "IGNORE", "; ".join(reasons)
        
        decisions = df.apply(make_decision, axis=1, result_type='expand')
        df['decision_flag'] = decisions[0]
        df['ignore_reasons'] = decisions[1]
        
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
    
    def enrich_with_scores_and_risk(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Enrich decision table with composite score, risk flag, and discount trend
        from the scoring and risk pipeline outputs (if available).
        """
        logger.info("")
        logger.info("=" * 80)
        logger.info("Enriching Decisions with Scores & Risk")
        logger.info("=" * 80)
        
        # --- Composite score & priority rank ---
        if self.scored_path.exists():
            scored = pd.read_csv(self.scored_path)
            score_cols = ['symbol', 'composite_score', 'rank']
            score_cols = [c for c in score_cols if c in scored.columns]
            df = df.merge(scored[score_cols].drop_duplicates('symbol'),
                          on='symbol', how='left')
            # Priority rank within CONSIDER only
            consider_mask = df['decision_flag'] == 'CONSIDER'
            df['priority_rank'] = np.nan
            if consider_mask.any():
                df.loc[consider_mask, 'priority_rank'] = (
                    df.loc[consider_mask, 'composite_score']
                    .rank(ascending=False, method='min')
                    .astype('Int64')
                )
            logger.info("  Merged composite scores")
        else:
            df['composite_score'] = np.nan
            df['priority_rank'] = np.nan
            logger.warning("  Scored file not found — composite_score will be NaN")
        
        # --- Risk flag ---
        if self.risk_path.exists():
            risk = pd.read_csv(self.risk_path)
            if 'parkinson_vol' in risk.columns:
                p75 = risk['parkinson_vol'].quantile(0.75)
                risk['risk_flag'] = risk['parkinson_vol'].apply(
                    lambda v: 'high_vol' if pd.notna(v) and v > p75 else ''
                )
                df = df.merge(risk[['symbol', 'risk_flag']].drop_duplicates('symbol'),
                              on='symbol', how='left')
                flagged = (df['risk_flag'] == 'high_vol').sum()
                logger.info("  Risk flags: %d symbols flagged as high_vol (>75th pctile)", flagged)
            else:
                df['risk_flag'] = ''
        else:
            df['risk_flag'] = ''
            logger.warning("  Risk file not found — risk_flag will be empty")
        
        # --- Discount trend & NAV growth ---
        if self.returns_path.exists():
            returns = pd.read_csv(self.returns_path)
            returns['date'] = pd.to_datetime(returns['date'])
            latest_date = returns['date'].max()
            ret_latest = returns[returns['date'] == latest_date].copy()
            
            # Use 1-week discount change if available, else 1-day
            trend_col = 'discount_change_1w'
            if trend_col not in ret_latest.columns or ret_latest[trend_col].isna().all():
                trend_col = 'discount_change_1d'
            
            if trend_col in ret_latest.columns:
                def classify_trend(val):
                    if pd.isna(val):
                        return 'unknown'
                    if val > 0.5:
                        return 'narrowing'
                    elif val < -0.5:
                        return 'widening'
                    return 'stable'
                
                ret_latest['discount_trend'] = ret_latest[trend_col].apply(classify_trend)
                df = df.merge(ret_latest[['symbol', 'discount_trend']].drop_duplicates('symbol'),
                              on='symbol', how='left')
                df['discount_trend'] = df['discount_trend'].fillna('unknown')
                logger.info("  Discount trends: %s", df['discount_trend'].value_counts().to_dict())
            else:
                df['discount_trend'] = 'unknown'

            # NAV growth rate (monthly)
            if 'nav_return_1m' in ret_latest.columns:
                df = df.merge(
                    ret_latest[['symbol', 'nav_return_1m']].drop_duplicates('symbol'),
                    on='symbol', how='left',
                )
                nav_avail = df['nav_return_1m'].notna().sum()
                logger.info("  NAV growth: %d symbols with monthly NAV return", nav_avail)
            else:
                df['nav_return_1m'] = np.nan
        else:
            df['discount_trend'] = 'unknown'
            df['nav_return_1m'] = np.nan
            logger.warning("  Returns file not found — discount_trend will be unknown")
        
        return df

    def save_decision_table(self, df: pd.DataFrame) -> None:
        """
        Save decision table with extended columns.
        
        Args:
            df: Complete decision table
        """
        # Ensure output directory exists
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Extended output columns
        output_cols = [
            'date', 'symbol', 'nav', 'ltp', 'discount_pct', 'volume',
            'years_to_maturity', 'days_to_maturity', 'valuation_bucket',
            'liquidity_bucket', 'decision_flag', 'ignore_reasons',
            'composite_score', 'priority_rank', 'discount_trend', 'risk_flag',
            'nav_return_1m',
        ]
        
        # Keep only columns that exist
        output_cols = [c for c in output_cols if c in df.columns]
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
            
            # Step 6: Enrich with scores, risk, and trend
            df = self.enrich_with_scores_and_risk(df)
            
            # Step 7: Save decision table
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
