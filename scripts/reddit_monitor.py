#!/usr/bin/env python3
"""
Reddit Capital Rotation Monitor
Tracks mention frequency and sentiment for key tickers across target subreddits
"""

import praw
import pandas as pd
from datetime import datetime, timedelta
from collections import Counter
import re

# Configuration
SUBREDDITS = [
    'wallstreetbets',
    'stocks',
    'investing',
    'StockMarket',
    'options',
    'biotechplays',
    'Semiconductors'
]

TICKERS_TO_TRACK = {
    'Tier 1': ['ASTS', 'RKLB', 'AVGO', 'MRVL', 'POET', 'TSMC', 'QBTS', 'SMR', 'CEG', 'D', 'LEU', 'BWXT'],
    'Tier 2': ['GOOGL', 'IONQ', 'RGTI', 'NBIS', 'FCX', 'SCCO', 'ALB', 'RDDT', 'META'],
    'Tier 3': ['VSTS', 'HFWA', 'EBF']
}

ALL_TICKERS = [ticker for tier in TICKERS_TO_TRACK.values() for ticker in tier]

# Reddit API Setup (requires credentials)
def setup_reddit():
    """
    Setup Reddit API connection
    Requires: reddit API credentials in environment or config file
    Get credentials at: https://www.reddit.com/prefs/apps
    """
    # TODO: Add your Reddit API credentials
    reddit = praw.Reddit(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        user_agent='capital_rotation_monitor/1.0'
    )
    return reddit

def extract_tickers(text):
    """Extract ticker mentions from text using regex"""
    # Match $TICKER or TICKER in context
    pattern = r'\b(?:\$)?([A-Z]{2,5})\b'
    matches = re.findall(pattern, text.upper())
    return [m for m in matches if m in ALL_TICKERS]

def analyze_subreddit(reddit, subreddit_name, lookback_days=7):
    """
    Analyze ticker mentions in a subreddit over specified time period
    """
    subreddit = reddit.subreddit(subreddit_name)

    mention_counts = Counter()
    post_data = []

    # Get posts from time period
    time_filter = datetime.now() - timedelta(days=lookback_days)

    try:
        for post in subreddit.new(limit=1000):
            post_time = datetime.fromtimestamp(post.created_utc)

            if post_time < time_filter:
                break

            # Extract tickers from title and body
            text = f"{post.title} {post.selftext}"
            tickers = extract_tickers(text)

            if tickers:
                for ticker in tickers:
                    mention_counts[ticker] += 1
                    post_data.append({
                        'subreddit': subreddit_name,
                        'ticker': ticker,
                        'title': post.title,
                        'score': post.score,
                        'num_comments': post.num_comments,
                        'url': post.url,
                        'created': post_time
                    })

    except Exception as e:
        print(f"Error analyzing r/{subreddit_name}: {e}")

    return mention_counts, pd.DataFrame(post_data)

def calculate_momentum(current_mentions, historical_baseline):
    """
    Calculate mention momentum vs. baseline
    Returns tickers with >3x increase
    """
    momentum_signals = {}

    for ticker, current_count in current_mentions.items():
        baseline = historical_baseline.get(ticker, 0)

        if baseline > 0:
            momentum = current_count / baseline
            if momentum >= 3.0:
                momentum_signals[ticker] = {
                    'current': current_count,
                    'baseline': baseline,
                    'momentum': momentum
                }

    return momentum_signals

def generate_report(all_mentions, momentum_signals, output_file='data/daily_report.txt'):
    """Generate daily monitoring report"""

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    report = f"""
╔═══════════════════════════════════════════════════════════════╗
║          REDDIT CAPITAL ROTATION DAILY REPORT                 ║
║          {timestamp}                          ║
╚═══════════════════════════════════════════════════════════════╝

═══════════════════════════════════════════════════════════════
TOP 20 MOST MENTIONED TICKERS (7-Day Window)
═══════════════════════════════════════════════════════════════

"""

    # Top 20 mentions
    for i, (ticker, count) in enumerate(all_mentions.most_common(20), 1):
        tier = 'T1' if ticker in TICKERS_TO_TRACK['Tier 1'] else 'T2' if ticker in TICKERS_TO_TRACK['Tier 2'] else 'T3'
        report += f"{i:2}. {ticker:6} - {count:4} mentions [{tier}]\n"

    report += """
═══════════════════════════════════════════════════════════════
⚠️  MOMENTUM ALERTS (3x+ vs 30-day baseline)
═══════════════════════════════════════════════════════════════

"""

    if momentum_signals:
        for ticker, data in sorted(momentum_signals.items(), key=lambda x: x[1]['momentum'], reverse=True):
            report += f"🔥 {ticker}: {data['momentum']:.1f}x momentum ({data['current']} vs {data['baseline']} baseline)\n"
    else:
        report += "No significant momentum alerts detected.\n"

    report += """
═══════════════════════════════════════════════════════════════
TIER 1 TRACKER (High Conviction Holdings)
═══════════════════════════════════════════════════════════════

"""

    for ticker in TICKERS_TO_TRACK['Tier 1']:
        count = all_mentions.get(ticker, 0)
        status = "📈" if count > 50 else "📊" if count > 20 else "📉"
        report += f"{status} {ticker:6} - {count:4} mentions\n"

    report += "\n" + "="*63 + "\n"

    # Save report
    with open(output_file, 'w') as f:
        f.write(report)

    print(report)
    return report

def main():
    """Main execution function"""

    print("Initializing Reddit Capital Rotation Monitor...")
    print("="*63)

    # Note: This is a template - requires Reddit API credentials to run
    print("\n⚠️  SETUP REQUIRED:")
    print("1. Create Reddit app at: https://www.reddit.com/prefs/apps")
    print("2. Add credentials to setup_reddit() function")
    print("3. Install dependencies: pip install praw pandas")
    print("\nExample output format generated below:\n")

    # Generate example report with mock data
    mock_mentions = Counter({
        'ASTS': 247, 'AVGO': 189, 'TSMC': 156, 'POET': 98, 'SMR': 76,
        'RDDT': 145, 'GOOGL': 134, 'IONQ': 87, 'CEG': 65, 'RKLB': 54,
        'NVDA': 312, 'AAPL': 298, 'MSFT': 267, 'AMZN': 234, 'TSLA': 223
    })

    mock_momentum = {
        'POET': {'current': 98, 'baseline': 25, 'momentum': 3.9},
        'SMR': {'current': 76, 'baseline': 20, 'momentum': 3.8},
    }

    generate_report(mock_mentions, mock_momentum, output_file='../data/example_report.txt')

    print("\n✅ Example report generated!")
    print("💡 Implement Reddit API connection to enable live monitoring")

if __name__ == "__main__":
    main()
