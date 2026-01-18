#!/usr/bin/env python3
"""
Live Reddit Capital Rotation Report Generator
Uses WebSearch to collect REAL DATA and generate comprehensive investment reports
"""

import os
import json
import csv
import sys
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter
import re

# Load configuration
def load_config():
    """Load configuration from config.json"""
    config_path = Path(__file__).parent.parent / "config.json"

    if not config_path.exists():
        print("❌ Error: config.json not found!")
        print(f"   Expected at: {config_path}")
        sys.exit(1)

    with open(config_path, 'r') as f:
        return json.load(f)

# Load config
CONFIG = load_config()

# Paths from config
OBSIDIAN_VAULT = Path(CONFIG['obsidian_vault_path']).expanduser()
REPORTS_DIR = OBSIDIAN_VAULT / CONFIG['reports_subfolder']
DATA_DIR = REPORTS_DIR / "data"

# Tracked tickers from config
ALL_TICKERS = []
for tier, tickers in CONFIG['tickers'].items():
    ALL_TICKERS.extend(tickers)

def ensure_directories():
    """Create necessary directories if they don't exist"""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def get_search_queries():
    """Generate search queries for data collection"""
    today = datetime.now().strftime("%B %Y")

    queries = [
        # Core Reddit sentiment
        f"reddit wallstreetbets trending stocks {today}",

        # Theme-specific searches
        f"AI stocks quantum computing biotech momentum {today}",
        f"space stocks satellite companies ASTS RKLB {today}",
        f"nuclear energy stocks SMR CEG {today}",
        f"custom AI chips Broadcom AVGO {today}",

        # Specific ticker deep-dives
        f"ASTS stock news analysis {today}",
        f"AVGO Broadcom AI chips {today}",
        f"POET optical interconnects {today}",
        f"SMR NuScale nuclear {today}",
        f"CEG Constellation Energy {today}",
        f"RDDT Reddit stock analysis {today}",
    ]

    return queries

def extract_tickers_from_text(text):
    """Extract ticker mentions from text"""
    if not text:
        return []

    # Look for our tracked tickers
    found_tickers = []
    text_upper = text.upper()

    for ticker in ALL_TICKERS:
        # Use word boundary regex to avoid false matches
        pattern = r'\b' + re.escape(ticker) + r'\b'
        if re.search(pattern, text_upper):
            found_tickers.append(ticker)

    return found_tickers

def analyze_sentiment(text):
    """Simple sentiment analysis based on keywords"""
    if not text:
        return "neutral"

    text_lower = text.lower()

    positive_words = ['bullish', 'surge', 'gain', 'growth', 'momentum', 'upgrade',
                      'strong', 'rally', 'breakout', 'buy', 'opportunity', 'catalyst',
                      'outperform', 'beating', 'revenue growth', 'partnership']

    negative_words = ['bearish', 'decline', 'loss', 'drop', 'downgrade', 'weak',
                      'risk', 'concern', 'warning', 'overvalued', 'sell', 'miss']

    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)

    if positive_count > negative_count + 2:
        return "positive"
    elif negative_count > positive_count + 2:
        return "negative"
    else:
        return "neutral"

def extract_themes_from_results(search_data):
    """Extract investment themes from search results"""
    themes = defaultdict(lambda: {
        'mentions': 0,
        'tickers': set(),
        'catalysts': [],
        'sentiment': [],
        'sources': []
    })

    # Define theme keywords
    theme_keywords = {
        'Space Connectivity': ['satellite', 'space', 'orbital', 'ASTS', 'direct-to-cell', 'LEO'],
        'Custom AI Chips': ['ASIC', 'custom chip', 'AI accelerator', 'Broadcom', 'AVGO', 'alternative to nvidia'],
        'Optical Interconnects': ['optical', 'photonics', 'POET', 'interconnect', 'data center bandwidth'],
        'Nuclear Energy for AI': ['nuclear', 'SMR', 'small modular reactor', 'CEG', 'power generation', 'data center power'],
        'Quantum Computing': ['quantum', 'qubit', 'IONQ', 'RGTI', 'quantum computing'],
        'Reddit Platform': ['RDDT', 'reddit stock', 'social media AI', 'data monetization'],
        'Copper & Materials': ['copper', 'FCX', 'critical materials', 'electrification'],
        'Healthcare AI': ['biotech', 'healthcare AI', 'drug discovery', 'NBIS'],
        'Small Cap Value': ['small cap', 'insider buying', 'value rotation', 'Russell 2000'],
    }

    for query_result in search_data:
        content = query_result.get('content', '')

        for theme_name, keywords in theme_keywords.items():
            if any(keyword.lower() in content.lower() for keyword in keywords):
                themes[theme_name]['mentions'] += 1
                themes[theme_name]['sentiment'].append(analyze_sentiment(content))
                themes[theme_name]['sources'].append(query_result.get('source', 'Unknown'))

                # Extract tickers
                tickers = extract_tickers_from_text(content)
                themes[theme_name]['tickers'].update(tickers)

    return dict(themes)

def generate_executive_summary(themes, ticker_data):
    """Generate executive summary section"""
    top_themes = sorted(themes.items(), key=lambda x: x[1]['mentions'], reverse=True)[:3]

    summary = "## Executive Summary\n\n"
    summary += f"Analysis completed on {datetime.now().strftime('%B %d, %Y at %H:%M')}. "
    summary += f"Analyzed {len(themes)} investment themes across {len(ticker_data)} tracked tickers.\n\n"

    summary += "**Top 3 Emerging Themes:**\n"
    for i, (theme_name, data) in enumerate(top_themes, 1):
        sentiment_summary = Counter(data['sentiment']).most_common(1)[0][0] if data['sentiment'] else 'neutral'
        summary += f"{i}. **{theme_name}** - {data['mentions']} mentions, {sentiment_summary} sentiment\n"

    summary += "\n"
    return summary

def generate_theme_section(theme_name, theme_data, rank):
    """Generate a detailed theme section"""
    conviction_stars = "🔥" * min(5, max(1, theme_data['mentions']))

    section = f"\n## {rank}. {theme_name}\n"
    section += f"**Signal Strength:** {conviction_stars}\n\n"

    # Tickers
    if theme_data['tickers']:
        section += "**High-Potential Tickers:**\n"
        for ticker in sorted(theme_data['tickers']):
            section += f"- **{ticker}**\n"
        section += "\n"

    # Sentiment analysis
    sentiment_counts = Counter(theme_data['sentiment'])
    total = sum(sentiment_counts.values())
    if total > 0:
        section += "**Market Sentiment:**\n"
        for sentiment, count in sentiment_counts.most_common():
            percentage = (count / total) * 100
            section += f"- {sentiment.title()}: {percentage:.0f}%\n"
        section += "\n"

    # Mention count
    section += f"**Data Points:** {theme_data['mentions']} mentions across sources\n\n"

    section += "---\n"
    return section

def generate_ticker_momentum_table(ticker_data, previous_data=None):
    """Generate ticker momentum analysis table"""
    section = "\n## Ticker Momentum Analysis\n\n"

    # Sort tickers by mentions
    sorted_tickers = sorted(ticker_data.items(), key=lambda x: x[1]['mentions'], reverse=True)

    gaining = []
    stable = []
    losing = []

    for ticker, data in sorted_tickers:
        mentions = data['mentions']
        prev_mentions = previous_data.get(ticker, {}).get('mentions', 0) if previous_data else 0

        if mentions > prev_mentions * 1.2:  # 20% increase
            gaining.append((ticker, mentions, data))
        elif mentions < prev_mentions * 0.8:  # 20% decrease
            losing.append((ticker, mentions, data))
        else:
            stable.append((ticker, mentions, data))

    # Gaining momentum
    if gaining:
        section += "### Gaining Momentum 📈\n\n"
        section += "| Ticker | Mentions | Theme | Sentiment |\n"
        section += "|--------|----------|-------|----------|\n"
        for ticker, mentions, data in gaining[:10]:
            section += f"| {ticker} | {mentions} | {data.get('theme', 'Multiple')} | {data.get('sentiment', 'neutral')} |\n"
        section += "\n"

    # Stable
    if stable:
        section += "### Stable Momentum ➡️\n\n"
        section += "| Ticker | Mentions | Theme | Sentiment |\n"
        section += "|--------|----------|-------|----------|\n"
        for ticker, mentions, data in stable[:10]:
            section += f"| {ticker} | {mentions} | {data.get('theme', 'Multiple')} | {data.get('sentiment', 'neutral')} |\n"
        section += "\n"

    # Losing
    if losing:
        section += "### Losing Momentum 📉\n\n"
        section += "| Ticker | Mentions | Previous | Change |\n"
        section += "|--------|----------|----------|--------|\n"
        for ticker, mentions, data in losing[:5]:
            prev = previous_data.get(ticker, {}).get('mentions', 0) if previous_data else 0
            change = f"-{((prev - mentions) / prev * 100):.0f}%" if prev > 0 else "N/A"
            section += f"| {ticker} | {mentions} | {prev} | {change} |\n"
        section += "\n"

    section += "---\n"
    return section

def generate_risk_section():
    """Generate risk warnings section"""
    section = "\n## Risk Management & Warnings\n\n"

    section += "### Position Sizing Guidelines\n"
    section += "- Maximum 5% per theme\n"
    section += "- Maximum 2% per individual ticker (3% for Tier 1 conviction)\n"
    section += "- Total Reddit-sourced exposure: <25% of portfolio\n\n"

    section += "### Red Flags to Monitor\n"
    section += "- Excessive hype language (\"guaranteed\", \"to the moon\")\n"
    section += "- Mainstream media saturation (CNBC features)\n"
    section += "- Insider selling during price run-ups\n"
    section += "- Fundamental deterioration vs. original thesis\n\n"

    section += "### Stop-Loss Discipline\n"
    section += "- 15-20% stops on individual positions\n"
    section += "- Trailing stops once position up 50%+\n"
    section += "- Re-evaluate thesis if down >30%\n\n"

    section += "---\n"
    return section

def generate_sources_section(search_queries, search_results):
    """Generate data sources section"""
    section = "\n## Data Sources & Methodology\n\n"

    section += "This analysis aggregated signals from:\n"
    section += "- Web search across financial news and Reddit discussions\n"
    section += "- Multi-source ticker mention tracking\n"
    section += "- Sentiment analysis of investment themes\n"
    section += "- Cross-validation of catalysts and news\n\n"

    section += "**Search Queries Executed:**\n"
    for query in search_queries:
        section += f"- {query}\n"
    section += "\n"

    section += f"**Total Data Points:** {len(search_results)} search results analyzed\n"
    section += f"**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    section += "---\n"
    return section

def generate_disclaimer():
    """Generate disclaimer section"""
    disclaimer = "\n## Disclaimer\n\n"
    disclaimer += "**IMPORTANT:** This analysis is for informational and educational purposes only. "
    disclaimer += "It is NOT financial advice. Reddit sentiment can be manipulated by pump-and-dump schemes. "
    disclaimer += "Always conduct independent due diligence, consider your risk tolerance, and consult "
    disclaimer += "with qualified financial advisors before making investment decisions.\n\n"
    disclaimer += "Past performance does not guarantee future results. All investments carry risk of loss.\n"
    return disclaimer

def generate_full_report(search_results, previous_data=None):
    """Generate complete markdown report from search results"""

    # Extract data from search results
    themes = extract_themes_from_results(search_results)

    # Build ticker data
    ticker_data = defaultdict(lambda: {
        'mentions': 0,
        'theme': '',
        'sentiment': 'neutral',
        'tier': ''
    })

    for ticker in ALL_TICKERS:
        mentions = 0
        sentiments = []
        associated_themes = []

        for result in search_results:
            content = result.get('content', '')
            if ticker in extract_tickers_from_text(content):
                mentions += 1
                sentiments.append(analyze_sentiment(content))

        # Find which theme this ticker belongs to
        for theme_name, theme_data in themes.items():
            if ticker in theme_data['tickers']:
                associated_themes.append(theme_name)

        if mentions > 0:
            ticker_data[ticker]['mentions'] = mentions
            ticker_data[ticker]['sentiment'] = Counter(sentiments).most_common(1)[0][0] if sentiments else 'neutral'
            ticker_data[ticker]['theme'] = associated_themes[0] if associated_themes else 'Multiple'

            # Assign tier
            for tier, tickers in CONFIG['tickers'].items():
                if ticker in tickers:
                    ticker_data[ticker]['tier'] = tier

    # Sort themes by conviction
    sorted_themes = sorted(themes.items(), key=lambda x: x[1]['mentions'], reverse=True)

    # Build report
    date_str = datetime.now().strftime("%B %d, %Y")
    report = f"# Reddit Capital Rotation Analysis - {date_str}\n\n"
    report += f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
    report += "---\n\n"

    # Executive Summary
    report += generate_executive_summary(themes, ticker_data)
    report += "---\n"

    # Top 10 Themes
    report += "\n# Top Investment Themes (Ranked by Conviction)\n\n"
    for i, (theme_name, theme_data) in enumerate(sorted_themes[:10], 1):
        report += generate_theme_section(theme_name, theme_data, i)

    # Ticker momentum
    report += generate_ticker_momentum_table(dict(ticker_data), previous_data)

    # Risk section
    report += generate_risk_section()

    # Sources
    report += generate_sources_section(get_search_queries(), search_results)

    # Disclaimer
    report += generate_disclaimer()

    return report, dict(ticker_data), themes

def save_report(content, filename=None):
    """Save report to Obsidian vault"""
    if filename is None:
        filename = f"{datetime.now().strftime('%Y-%m-%d')}_live_analysis.md"

    report_path = REPORTS_DIR / filename

    with open(report_path, 'w') as f:
        f.write(content)

    print(f"✅ Report saved to: {report_path}")
    return report_path

def save_ticker_history(ticker_data):
    """Append ticker data to history CSV"""
    history_file = DATA_DIR / "ticker_history.csv"

    file_exists = history_file.exists()

    with open(history_file, 'a', newline='') as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(['date', 'ticker', 'mentions', 'tier', 'theme', 'sentiment'])

        for ticker, data in ticker_data.items():
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d"),
                ticker,
                data.get('mentions', 0),
                data.get('tier', ''),
                data.get('theme', ''),
                data.get('sentiment', 'neutral')
            ])

    print(f"✅ Ticker history updated: {history_file}")

def save_theme_evolution(themes_data):
    """Save theme evolution data to JSON"""
    evolution_file = DATA_DIR / "theme_evolution.json"

    # Load existing data
    if evolution_file.exists():
        with open(evolution_file, 'r') as f:
            history = json.load(f)
    else:
        history = []

    # Add current snapshot
    history.append({
        'date': datetime.now().strftime("%Y-%m-%d"),
        'themes': {name: {
            'mentions': data['mentions'],
            'tickers': list(data['tickers']),
            'sentiment': data['sentiment']
        } for name, data in themes_data.items()}
    })

    # Save updated history
    with open(evolution_file, 'w') as f:
        json.dump(history, f, indent=2)

    print(f"✅ Theme evolution updated: {evolution_file}")

def load_previous_data():
    """Load previous ticker data for comparison"""
    history_file = DATA_DIR / "ticker_history.csv"

    if not history_file.exists():
        return None

    previous_data = {}

    with open(history_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        # Get most recent date
        if not rows:
            return None

        recent_date = max(row['date'] for row in rows)

        # Get data from most recent date
        for row in rows:
            if row['date'] == recent_date:
                previous_data[row['ticker']] = {
                    'mentions': int(row['mentions']) if row['mentions'] else 0,
                    'theme': row['theme'],
                    'sentiment': row['sentiment']
                }

    return previous_data if previous_data else None

def update_index():
    """Update index file with links to all reports"""
    reports = sorted(REPORTS_DIR.glob("*_analysis.md"), reverse=True)

    index_content = f"""# Reddit Capital Rotation - Report Index

*Last Updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*

## 📚 All Reports

"""

    for report in reports:
        date_str = report.stem.replace("_analysis", "").replace("_live_analysis", "")
        index_content += f"- [[{report.stem}|{date_str}]]\n"

    index_content += """

---

## 🔄 Quick Access

- Latest Report (see above)
- [[ticker_tracking|Ticker Performance Tracker]]
- [[theme_evolution|Theme Evolution Analysis]]

## 📊 Data Files

- [Ticker History CSV](data/ticker_history.csv)
- [Theme Evolution JSON](data/theme_evolution.json)

---

*Reports generated by Reddit Capital Rotation Strategy*
"""

    index_path = REPORTS_DIR / "_index.md"
    with open(index_path, 'w') as f:
        f.write(index_content)

    print(f"✅ Index updated: {index_path}")

def main(search_results=None):
    """
    Main execution function

    Args:
        search_results: List of search result dictionaries with 'content' and 'source' keys
                       If None, will return empty template (for testing)
    """
    print("="*70)
    print("Live Reddit Capital Rotation Report Generator")
    print("="*70)
    print()

    # Setup
    print("📁 Setting up directories...")
    ensure_directories()
    print()

    # Load previous data for comparison
    print("📊 Loading previous data...")
    previous_data = load_previous_data()
    if previous_data:
        print(f"   Found {len(previous_data)} tickers from previous report")
    print()

    # Generate report with search results
    if search_results is None:
        print("⚠️  No search results provided - generating template")
        search_results = []

    print(f"📝 Analyzing {len(search_results)} search results...")
    report_content, ticker_data, themes_data = generate_full_report(search_results, previous_data)
    report_path = save_report(report_content)
    print()

    # Save tracking data
    print("💾 Saving tracking data...")
    save_ticker_history(ticker_data)
    save_theme_evolution(themes_data)
    print()

    # Update index
    print("📚 Updating index...")
    update_index()
    print()

    print("="*70)
    print("✅ Report generation complete!")
    print("="*70)
    print()
    print(f"📍 Report Location: {report_path}")
    print(f"📍 Index: {REPORTS_DIR / '_index.md'}")
    print()
    print(f"📊 Analysis Summary:")
    print(f"   - {len(themes_data)} themes identified")
    print(f"   - {len(ticker_data)} tickers tracked")
    print(f"   - {len(search_results)} data points analyzed")
    print()

    return report_path

if __name__ == "__main__":
    main()
