#!/usr/bin/env python3
"""
Live Reddit Monitor - Browser-Based Version
Uses Chrome automation to scrape Reddit in real-time
No API credentials required
"""

import json
import re
from datetime import datetime
from collections import Counter, defaultdict
from pathlib import Path

# Tickers to track
TICKERS = {
    'Tier 1': ['ASTS', 'RKLB', 'AVGO', 'MRVL', 'POET', 'TSMC', 'QBTS', 'SMR', 'CEG', 'D', 'LEU', 'BWXT'],
    'Tier 2': ['GOOGL', 'IONQ', 'RGTI', 'NBIS', 'FCX', 'SCCO', 'ALB', 'RDDT', 'META'],
    'Tier 3': ['VSTS', 'HFWA', 'EBF']
}

ALL_TICKERS = []
for tier_list in TICKERS.values():
    ALL_TICKERS.extend(tier_list)

# Subreddits to monitor
SUBREDDITS = [
    'wallstreetbets',
    'stocks',
    'investing',
    'stockmarket'
]

def get_ticker_tier(ticker):
    """Get the tier for a ticker"""
    for tier, tickers in TICKERS.items():
        if ticker in tickers:
            return tier.replace('Tier ', 'T')
    return '--'

def extract_tickers_from_text(text):
    """Extract ticker symbols from text"""
    if not text:
        return []

    # Pattern for $TICKER or standalone TICKER
    pattern = r'\$?([A-Z]{2,5})\b'
    potential_tickers = re.findall(pattern, text.upper())

    # Filter to only tracked tickers
    found = [t for t in potential_tickers if t in ALL_TICKERS]
    return list(set(found))  # Remove duplicates

def analyze_posts(posts_data):
    """Analyze collected posts for ticker mentions"""
    ticker_mentions = Counter()
    ticker_posts = defaultdict(list)

    for post in posts_data:
        text = f"{post.get('title', '')} {post.get('body', '')}"
        tickers = extract_tickers_from_text(text)

        for ticker in tickers:
            ticker_mentions[ticker] += 1
            ticker_posts[ticker].append({
                'title': post.get('title', ''),
                'subreddit': post.get('subreddit', ''),
                'score': post.get('score', 0),
                'url': post.get('url', '')
            })

    return ticker_mentions, ticker_posts

def generate_report(ticker_mentions, ticker_posts, output_file='data/live_report.txt'):
    """Generate monitoring report"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    report = f"""
╔═══════════════════════════════════════════════════════════════╗
║          REDDIT LIVE MONITORING REPORT                        ║
║          {timestamp}                          ║
╚═══════════════════════════════════════════════════════════════╝

═══════════════════════════════════════════════════════════════
TOP MENTIONED TICKERS (Current Scan)
═══════════════════════════════════════════════════════════════

"""

    if not ticker_mentions:
        report += "No tracked tickers found in current scan.\n"
    else:
        for i, (ticker, count) in enumerate(ticker_mentions.most_common(20), 1):
            tier = get_ticker_tier(ticker)
            marker = "⭐" if tier.startswith('T1') else "📊" if tier.startswith('T2') else "💎"
            report += f"{i:2}. {ticker:6} - {count:4} mentions [{tier}] {marker}\n"

    report += """
═══════════════════════════════════════════════════════════════
TIER 1 TRACKER (High Conviction Holdings)
═══════════════════════════════════════════════════════════════

"""

    for ticker in TICKERS['Tier 1']:
        count = ticker_mentions.get(ticker, 0)
        status = "📈" if count >= 5 else "📊" if count >= 2 else "📉"
        report += f"{status} {ticker:6} - {count:4} mentions\n"

    report += """
═══════════════════════════════════════════════════════════════
TOP POSTS BY TRACKED TICKERS
═══════════════════════════════════════════════════════════════

"""

    for ticker in list(ticker_mentions.most_common(10)):
        ticker_symbol = ticker[0]
        posts = ticker_posts[ticker_symbol]

        if posts:
            # Sort by score and take top 2
            top_posts = sorted(posts, key=lambda x: x['score'], reverse=True)[:2]
            report += f"\n{ticker_symbol} ({len(posts)} total mentions):\n"

            for post in top_posts:
                report += f"  • r/{post['subreddit']}: {post['title'][:60]}...\n"
                report += f"    Score: {post['score']} | {post['url']}\n"

    report += "\n" + "="*63 + "\n"
    report += f"\nScan completed at: {timestamp}\n"
    report += f"Subreddits monitored: {', '.join(SUBREDDITS)}\n"
    report += f"Tickers tracked: {len(ALL_TICKERS)}\n"

    # Save report
    output_path = Path(__file__).parent.parent / output_file
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, 'w') as f:
        f.write(report)

    print(report)
    return report

def save_posts_json(posts_data, filename='data/latest_posts.json'):
    """Save raw posts data to JSON"""
    output_path = Path(__file__).parent.parent / filename
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(posts_data, f, indent=2)

if __name__ == "__main__":
    print("This script is designed to work with browser automation.")
    print("Run run_live_monitor.py instead to execute the full monitoring.")
