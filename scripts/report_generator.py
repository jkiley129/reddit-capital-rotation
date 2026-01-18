#!/usr/bin/env python3
"""
Reddit Capital Rotation Report Generator
Generates comprehensive investment theme analysis reports using web search
"""

import os
import json
import csv
import sys
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Load configuration
def load_config():
    """Load configuration from config.json"""
    config_path = Path(__file__).parent.parent / "config.json"

    if not config_path.exists():
        print("❌ Error: config.json not found!")
        print(f"   Expected at: {config_path}")
        print("\n📝 Please copy config.example.json to config.json and update with your settings:")
        print("   cp config.example.json config.json")
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
TICKERS = CONFIG['tickers']

def ensure_directories():
    """Create necessary directories if they don't exist"""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def get_search_queries():
    """Generate search queries for data collection"""
    today = datetime.now().strftime("%B %Y")

    queries = [
        # Reddit sentiment tracking
        f"reddit wallstreetbets trending stocks {today}",
        f"reddit stocks discussion momentum {today}",
        f"reddit investing emerging themes {today}",

        # Specific themes
        f"AI stocks quantum computing biotech momentum {today}",
        f"space stocks satellite companies {today}",
        f"nuclear energy stocks SMR {today}",
        f"custom AI chips Broadcom alternatives {today}",

        # Market analysis
        f"emerging investment themes {today}",
        f"capital rotation sectors {today}",
        f"small cap stocks insider buying {today}",
    ]

    return queries

def generate_report_content(search_results, previous_data=None):
    """
    Generate markdown report content

    In a real implementation, this would:
    1. Parse search results for ticker mentions
    2. Extract theme information
    3. Identify catalysts and news
    4. Compare to previous reports

    For now, returns a template that the user can run with actual search
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_str = datetime.now().strftime("%Y-%m-%d")

    report = f"""# Reddit Capital Rotation Analysis - {date_str}

*Generated: {timestamp}*

## 📊 Executive Summary

This report analyzes emerging investment themes from Reddit social media discussions, financial news, and analyst sentiment to identify early-stage capital rotation opportunities.

**Key Finding:** [Summary of major trends this period]

---

## 🔥 Top Emerging Themes

### Tier 1 - Highest Conviction

#### 1. [Theme Name]
**Signal Strength:** ⭐⭐⭐⭐⭐

**Top Tickers:**
- **TICKER** - [Brief description]
- **TICKER** - [Brief description]

**Key Catalysts:**
- [Catalyst 1]
- [Catalyst 2]

**Reddit Sentiment:** [Increasing/Stable/Declining]

**Risk Factors:**
- [Risk 1]
- [Risk 2]

---

#### 2. [Theme Name]
**Signal Strength:** ⭐⭐⭐⭐⭐

**Top Tickers:**
- **TICKER** - [Brief description]

**Key Catalysts:**
- [Catalyst 1]

**Reddit Sentiment:** [Status]

---

### Tier 2 - Strong Conviction

#### 3. [Theme Name]
**Signal Strength:** ⭐⭐⭐⭐

[Similar structure]

---

## 📈 Ticker Momentum Analysis

### Gaining Momentum (↗️)
| Ticker | Current Mentions | vs Previous | Theme | Action |
|--------|-----------------|-------------|-------|---------|
| ASTS   | [#]             | +XX%        | Space | Hold/Add |
| POET   | [#]             | +XX%        | Optical | Initiate |

### Stable (→)
| Ticker | Current Mentions | Status | Theme |
|--------|-----------------|--------|-------|
| AVGO   | [#]             | Steady | AI Chips |

### Losing Momentum (↘️)
| Ticker | Current Mentions | vs Previous | Action |
|--------|-----------------|-------------|---------|
| [TICKER] | [#]           | -XX%        | Monitor |

---

## 🆕 Newly Discovered Tickers

**[TICKER]** - [Description]
- Theme: [Theme]
- Why interesting: [Reason]
- Risk level: [High/Medium/Low]
- Reddit presence: [Subreddits]

---

## 📊 Cross-Subreddit Analysis

### r/wallstreetbets
- Top discussions: [Topics]
- Trending tickers: [List]
- Sentiment: [Overall mood]

### r/stocks
- Focus areas: [Topics]
- Quality of DD: [Assessment]

### r/investing
- Longer-term themes: [Topics]

---

## 🎯 Recommended Actions

### Initiate Positions (Phase 2 - Building Momentum)
- **TICKER** (X% allocation) - [Rationale]

### Hold/Accumulate
- **TICKER** - [Rationale]

### Take Profits / Reduce
- **TICKER** - [Rationale]

### Watch List
- **TICKER** - [Why watching]

---

## 📉 Risk & Red Flags

**Potential Pump & Dumps Detected:**
- [Ticker if any] - [Warning signs]

**Excessive Hype Warnings:**
- [Themes reaching saturation]

**Macro Headwinds:**
- [Market risks]

---

## 🔍 Data Sources

This report synthesized information from:
- Reddit mention tracking (AltIndex, Tradestie, ApeWisdom)
- Financial news aggregators
- Analyst reports
- Social sentiment platforms

**Search Queries Used:**
{chr(10).join(f"- {q}" for q in get_search_queries())}

---

## 📝 Notes & Observations

[Key takeaways from this analysis period]

---

## 🔄 Changes Since Last Report

{f'**Previous Report Date:** {previous_data.get("date") if previous_data else "N/A"}' if previous_data else '**First Report**'}

**Theme Progression:**
- [Theme] moved from Phase X → Phase Y
- [Theme] conviction increased/decreased

**Ticker Changes:**
- [Ticker] added to watchlist
- [Ticker] removed (reason)

---

*Next Update: {(datetime.now()).strftime("%Y-%m-%d")} (run report generator)*

**Disclaimer:** This analysis is for informational purposes only. Not financial advice. Always conduct your own due diligence before investing.
"""

    return report

def save_report(content, filename=None):
    """Save report to Obsidian vault"""
    if filename is None:
        filename = f"{datetime.now().strftime('%Y-%m-%d')}_analysis.md"

    report_path = REPORTS_DIR / filename

    with open(report_path, 'w') as f:
        f.write(content)

    print(f"✅ Report saved to: {report_path}")
    return report_path

def update_index():
    """Update index file with links to all reports"""
    reports = sorted(REPORTS_DIR.glob("*_analysis.md"), reverse=True)

    index_content = f"""# Reddit Capital Rotation - Report Index

*Last Updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*

## 📚 All Reports

"""

    for report in reports:
        date_str = report.stem.replace("_analysis", "")
        index_content += f"- [[{report.stem}|{date_str}]]\n"

    index_content += f"""

---

## 🔄 Quick Access

- [[{reports[0].stem}|Latest Report]]
- [[ticker_tracking|Ticker Performance Tracker]]
- [[theme_evolution|Theme Evolution Analysis]]

## 📊 Data Files

- [Ticker History CSV](data/ticker_history.csv)
- [Theme Evolution JSON](data/theme_evolution.json)

---

## 🎯 How to Use These Reports

1. **Weekly Review**: Read the latest report for current market themes
2. **Trend Analysis**: Compare 2-3 recent reports to spot momentum shifts
3. **Action Items**: Focus on "Recommended Actions" section for positioning
4. **Risk Management**: Always review "Risk & Red Flags" before making moves

---

*Reports generated by Reddit Capital Rotation Strategy*
*Repository: https://github.com/jkiley129/reddit-capital-rotation*
"""

    index_path = REPORTS_DIR / "_index.md"
    with open(index_path, 'w') as f:
        f.write(index_content)

    print(f"✅ Index updated: {index_path}")

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
        'themes': themes_data
    })

    # Save updated history
    with open(evolution_file, 'w') as f:
        json.dump(history, f, indent=2)

    print(f"✅ Theme evolution updated: {evolution_file}")

def create_readme():
    """Create README in the Obsidian folder"""
    readme_content = """# Reddit Capital Rotation Reports

This folder contains automated investment theme analysis reports generated from Reddit social media sentiment, financial news, and analyst coverage.

## 📁 Structure

- `YYYY-MM-DD_analysis.md` - Individual reports
- `_index.md` - Master index of all reports
- `data/` - Historical tracking data

## 🚀 How to Generate Reports

From the project directory:

```bash
cd ~/Development/reddit-capital-rotation
python scripts/run_report.py
```

## 📊 What's Tracked

- **Top 10 Investment Themes** ranked by conviction
- **30+ Tickers** across 3 tiers
- **Reddit Sentiment** from r/wallstreetbets, r/stocks, r/investing
- **Momentum Changes** week-over-week
- **Catalysts & Risk Factors**

## ⏰ Recommended Schedule

Run every 2-3 days to track momentum shifts effectively.

## 🔗 Links

- [GitHub Repository](https://github.com/jkiley129/reddit-capital-rotation)
- [Strategy Documentation](../../../Development/reddit-capital-rotation/README.md)

---

*Last updated: {datetime.now().strftime("%Y-%m-%d")}*
"""

    readme_path = REPORTS_DIR / "README.md"
    with open(readme_path, 'w') as f:
        f.write(readme_content)

    print(f"✅ README created: {readme_path}")

def main():
    """Main execution function"""
    print("="*70)
    print("Reddit Capital Rotation Report Generator")
    print("="*70)
    print()

    # Setup
    print("📁 Setting up directories...")
    ensure_directories()
    print()

    # Generate report
    print("📝 Generating report...")
    report_content = generate_report_content({})
    report_path = save_report(report_content)
    print()

    # Update index
    print("📚 Updating index...")
    update_index()
    print()

    # Create README
    print("📄 Creating README...")
    create_readme()
    print()

    # Save sample tracker data
    print("💾 Initializing data trackers...")
    sample_ticker_data = {
        'ASTS': {'mentions': 0, 'tier': 'T1', 'theme': 'Space Connectivity', 'sentiment': 'neutral'},
        'AVGO': {'mentions': 0, 'tier': 'T1', 'theme': 'Custom AI Chips', 'sentiment': 'neutral'},
    }
    save_ticker_history(sample_ticker_data)

    sample_themes = [
        {'name': 'Space Connectivity', 'tier': 1, 'conviction': 5},
        {'name': 'Custom AI Chips', 'tier': 1, 'conviction': 5},
    ]
    save_theme_evolution(sample_themes)
    print()

    print("="*70)
    print("✅ Report generation complete!")
    print("="*70)
    print()
    print(f"📍 Location: {report_path}")
    print(f"📍 Index: {REPORTS_DIR / '_index.md'}")
    print()
    print("💡 Next steps:")
    print("   1. Open in Obsidian to view the report")
    print("   2. Fill in the template with actual search results")
    print("   3. Run again in 2-3 days to track momentum")
    print()
    print("🔧 To enable automated search, configure WebSearch in run_report.py")
    print()

if __name__ == "__main__":
    main()
