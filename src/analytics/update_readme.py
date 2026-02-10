"""
README Auto-Updater for Mutual Fund Decision System

Automatically generates and updates a "Daily Decision Summary" section in README.md
with current screening results. Preserves all other README content.

This is for research dashboard purposes only - NO investment advice.
"""

import pandas as pd
import logging
from pathlib import Path
from datetime import datetime
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ReadmeUpdater:
    """
    Updates README.md with current decision analysis summary.
    
    Only modifies the auto-generated section, preserves all other content.
    """
    
    # Section markers for detection
    SECTION_HEADER = "## 📊 Daily Mutual Fund Decision Summary"
    SECTION_START_MARKER = "<!-- AUTO-GENERATED-START -->"
    SECTION_END_MARKER = "<!-- AUTO-GENERATED-END -->"
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.history_path = project_root / 'data' / 'history' / 'mf_decision_history.csv'
        self.readme_path = project_root / 'README.md'
    
    def load_history(self) -> pd.DataFrame:
        """
        Load decision history file.
        
        Returns:
            DataFrame with complete history
        """
        if not self.history_path.exists():
            logger.warning(f"⚠ History file not found: {self.history_path}")
            logger.warning("  Run decision_history.py first to generate history")
            return pd.DataFrame()
        
        df = pd.read_csv(self.history_path)
        df['date'] = pd.to_datetime(df['date'])
        
        logger.info(f"✓ Loaded history: {len(df)} records")
        logger.info(f"  Date range: {df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}")
        
        return df
    
    def calculate_consider_streaks(self, history: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate consecutive CONSIDER days for each symbol.
        
        Args:
            history: Complete decision history
            
        Returns:
            DataFrame with symbol and current consider_streak
        """
        if len(history) == 0:
            return pd.DataFrame(columns=['symbol', 'consider_streak'])
        
        # Sort by symbol and date
        df = history.sort_values(['symbol', 'date']).copy()
        
        # Create binary CONSIDER flag
        df['is_consider'] = (df['decision_flag'] == 'CONSIDER').astype(int)
        
        # Calculate streak - reset counter when decision changes
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
        
        # Get most recent record for each symbol
        latest_date = df['date'].max()
        latest = df[df['date'] == latest_date][['symbol', 'consider_streak']].copy()
        
        return latest
    
    def get_latest_summary(self, history: pd.DataFrame) -> dict:
        """
        Generate summary statistics from latest history records.
        
        Args:
            history: Complete decision history
            
        Returns:
            Dictionary with summary stats
        """
        if len(history) == 0:
            return {
                'last_date': None,
                'total_funds': 0,
                'consider_count': 0,
                'ignore_count': 0,
                'consider_funds': pd.DataFrame()
            }
        
        # Get latest date
        latest_date = history['date'].max()
        latest = history[history['date'] == latest_date].copy()
        
        # Calculate streaks
        streaks = self.calculate_consider_streaks(history)
        
        # Merge streaks with latest data
        latest = latest.merge(streaks, on='symbol', how='left')
        latest['consider_streak'] = latest['consider_streak'].fillna(0).astype(int)
        
        # Get CONSIDER funds only
        consider_funds = latest[latest['decision_flag'] == 'CONSIDER'].copy()
        
        # Sort by: longest streak first, then deepest discount
        consider_funds = consider_funds.sort_values(
            ['consider_streak', 'discount_pct'], 
            ascending=[False, True]  # Longer streaks first, more negative discount first
        )
        
        summary = {
            'last_date': latest_date,
            'total_funds': len(latest),
            'consider_count': len(consider_funds),
            'ignore_count': len(latest) - len(consider_funds),
            'consider_funds': consider_funds
        }
        
        return summary
    
    def generate_markdown_content(self, summary: dict) -> str:
        """
        Generate markdown content for the auto-updated section.
        
        Args:
            summary: Summary statistics dictionary
            
        Returns:
            Markdown string
        """
        lines = []
        
        # Section header
        lines.append(self.SECTION_HEADER)
        lines.append("")
        lines.append(self.SECTION_START_MARKER)
        lines.append("")
        
        # Check if we have data
        if summary['last_date'] is None:
            lines.append("**Status**: No analysis data available yet.")
            lines.append("")
            lines.append("Run the screening pipeline to generate decision data:")
            lines.append("```bash")
            lines.append("python src/analytics/decision_layer.py")
            lines.append("python src/analytics/decision_history.py")
            lines.append("python src/analytics/update_readme.py")
            lines.append("```")
            lines.append("")
            lines.append(self.SECTION_END_MARKER)
            return "\n".join(lines)
        
        # 1. Run metadata
        lines.append(f"**Last updated**: {summary['last_date'].strftime('%Y-%m-%d')}")
        lines.append(f"**Funds analyzed**: {summary['total_funds']}")
        lines.append(f"**CONSIDER**: {summary['consider_count']}")
        lines.append(f"**IGNORE**: {summary['ignore_count']}")
        lines.append("")
        
        # 2. Top CONSIDER candidates table
        lines.append("### Current CONSIDER Candidates")
        lines.append("")
        
        consider_funds = summary['consider_funds']
        
        if len(consider_funds) == 0:
            lines.append("**No funds currently meet CONSIDER criteria.**")
            lines.append("")
            lines.append("All funds are flagged as IGNORE due to:")
            lines.append("- Insufficient discount to NAV (< 4%)")
            lines.append("- Low liquidity (bottom 25% volume)")
            lines.append("- Long maturity (> 4 years)")
            lines.append("")
        else:
            # Table header
            lines.append("| Symbol | Discount % | Days to Maturity | Liquidity | CONSIDER Streak |")
            lines.append("|--------|------------|------------------|-----------|-----------------|")
            
            # Table rows
            for _, row in consider_funds.iterrows():
                symbol = row['symbol']
                discount = f"{row['discount_pct']:.2f}%"
                days = f"{int(row['days_to_maturity']):,}"
                liquidity = row['liquidity_bucket']
                streak = f"{int(row['consider_streak'])} day{'s' if row['consider_streak'] != 1 else ''}"
                
                lines.append(f"| {symbol} | {discount} | {days} | {liquidity} | {streak} |")
            
            lines.append("")
        
        # 3. Interpretation notes (static text - exact wording required)
        lines.append("### Interpretation")
        lines.append("")
        lines.append("This table highlights closed-end mutual funds that are trading at a discount to NAV, have sufficient liquidity, and are approaching maturity.")
        lines.append("The system is rule-based and intended for research and monitoring purposes only.")
        lines.append("")
        
        lines.append(self.SECTION_END_MARKER)
        
        return "\n".join(lines)
    
    def update_readme(self, new_content: str) -> None:
        """
        Update README.md with new content for the auto-generated section.
        
        Only modifies the section between markers. Preserves all other content.
        
        Args:
            new_content: New markdown content for the section
        """
        # Read existing README (or create if doesn't exist)
        if self.readme_path.exists():
            with open(self.readme_path, 'r', encoding='utf-8') as f:
                existing_content = f.read()
            logger.info(f"✓ Read existing README: {len(existing_content)} characters")
        else:
            existing_content = ""
            logger.info("✓ README does not exist - will create new file")
        
        # Check if auto-generated section exists
        if self.SECTION_HEADER in existing_content:
            # Section exists - replace it
            logger.info("✓ Found existing auto-generated section - replacing")
            
            # Find section boundaries
            # Pattern: from SECTION_HEADER to SECTION_END_MARKER (inclusive)
            pattern = re.escape(self.SECTION_HEADER) + r'.*?' + re.escape(self.SECTION_END_MARKER)
            
            # Replace the section
            updated_content = re.sub(
                pattern,
                new_content,
                existing_content,
                flags=re.DOTALL
            )
            
            operation = "Updated"
        else:
            # Section doesn't exist - append at end
            logger.info("✓ No existing section found - appending to end")
            
            # Ensure there's spacing before new section
            if existing_content and not existing_content.endswith('\n\n'):
                if existing_content.endswith('\n'):
                    existing_content += '\n'
                else:
                    existing_content += '\n\n'
            
            updated_content = existing_content + new_content + '\n'
            operation = "Appended"
        
        # Write updated README
        with open(self.readme_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        logger.info(f"✓ {operation} README: {self.readme_path}")
        logger.info(f"  Total size: {len(updated_content)} characters")
    
    def run(self) -> None:
        """Execute README update pipeline"""
        logger.info("")
        logger.info("=" * 80)
        logger.info("README AUTO-UPDATER")
        logger.info("=" * 80)
        logger.info("")
        
        try:
            # Step 1: Load history
            logger.info("Step 1: Load Decision History")
            logger.info("-" * 80)
            history = self.load_history()
            
            # Step 2: Calculate summary
            logger.info("")
            logger.info("Step 2: Calculate Summary Statistics")
            logger.info("-" * 80)
            summary = self.get_latest_summary(history)
            
            if summary['last_date']:
                logger.info(f"✓ Latest analysis date: {summary['last_date'].strftime('%Y-%m-%d')}")
                logger.info(f"  Total funds: {summary['total_funds']}")
                logger.info(f"  CONSIDER: {summary['consider_count']}")
                logger.info(f"  IGNORE: {summary['ignore_count']}")
                
                if summary['consider_count'] > 0:
                    logger.info(f"\n  Top CONSIDER funds:")
                    for _, row in summary['consider_funds'].head(5).iterrows():
                        logger.info(f"    • {row['symbol']}: {row['discount_pct']:.2f}% discount, {int(row['consider_streak'])} day streak")
            else:
                logger.info("⚠ No history data available")
            
            # Step 3: Generate markdown
            logger.info("")
            logger.info("Step 3: Generate Markdown Content")
            logger.info("-" * 80)
            markdown_content = self.generate_markdown_content(summary)
            logger.info(f"✓ Generated {len(markdown_content)} characters of markdown")
            
            # Step 4: Update README
            logger.info("")
            logger.info("Step 4: Update README.md")
            logger.info("-" * 80)
            self.update_readme(markdown_content)
            
            # Success
            logger.info("")
            logger.info("=" * 80)
            logger.info("README UPDATE COMPLETE")
            logger.info("=" * 80)
            logger.info(f"\n✓ README.md updated successfully")
            logger.info(f"✓ Section: {self.SECTION_HEADER}")
            
            if summary['consider_count'] > 0:
                logger.info(f"✓ Displayed {summary['consider_count']} CONSIDER funds")
            else:
                logger.info(f"✓ No CONSIDER funds currently")
            
            logger.info("")
            logger.info("=" * 80)
            
        except Exception as e:
            logger.error("")
            logger.error("=" * 80)
            logger.error("README UPDATE FAILED")
            logger.error("=" * 80)
            logger.error(f"Error: {e}")
            logger.error("=" * 80)
            raise


def main():
    """Entry point"""
    project_root = Path(__file__).parent.parent.parent
    updater = ReadmeUpdater(project_root)
    updater.run()


if __name__ == '__main__':
    main()
