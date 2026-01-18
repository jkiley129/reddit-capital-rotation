# How to Use the Reddit Capital Rotation Tool

## Quick Start (5 Minutes)

### 1. Configure Your Settings

Copy the example config and customize it:

```bash
cd ~/Development/reddit-capital-rotation
cp config.example.json config.json
```

Edit `config.json` with your preferences:

```json
{
  "obsidian_vault_path": "~/path/to/your/obsidian/vault",
  "reports_subfolder": "Investment Research/Reddit Capital Rotation",
  "run_frequency_days": 3,
  "tickers": {
    "Tier 1": ["ASTS", "AVGO", "POET", ...],
    "Tier 2": ["GOOGL", "IONQ", ...],
    "Tier 3": ["VSTS", "HFWA", ...]
  }
}
```

**Note:** `config.json` is in `.gitignore` and won't be committed to GitHub (keeps your paths private).

### 2. Generate Your First Report

```bash
python3 scripts/run_report.py
```

This will:
- Create folder structure in your Obsidian vault
- Generate a report template with today's date
- Initialize tracking data (CSV + JSON)
- Create an index file linking all reports

### 3. View in Obsidian

Open Obsidian and navigate to:
```
Your Vault/Investment Research/Reddit Capital Rotation/
```

You'll find:
- `2026-01-18_analysis.md` - Today's report
- `_index.md` - Master index of all reports
- `README.md` - Folder documentation
- `data/` - Historical tracking data

## What Gets Generated

### Report Structure

Each report (`YYYY-MM-DD_analysis.md`) contains:

1. **Executive Summary** - Key findings
2. **Top Emerging Themes** - Tiered by conviction
3. **Ticker Momentum Analysis** - Gaining/stable/losing
4. **Newly Discovered Tickers** - Fresh opportunities
5. **Cross-Subreddit Analysis** - Where discussions are happening
6. **Recommended Actions** - Initiate/hold/reduce/watch
7. **Risk & Red Flags** - Pump & dumps, excessive hype
8. **Data Sources** - All sources used
9. **Changes Since Last Report** - Week-over-week comparison

### Tracking Data

**ticker_history.csv:**
```csv
date,ticker,mentions,tier,theme,sentiment
2026-01-18,ASTS,247,T1,Space Connectivity,positive
2026-01-18,AVGO,189,T1,Custom AI Chips,positive
```

**theme_evolution.json:**
```json
[
  {
    "date": "2026-01-18",
    "themes": [
      {"name": "Space Connectivity", "tier": 1, "conviction": 5}
    ]
  }
]
```

## Running on a Schedule

### macOS (cron)

Edit your crontab:
```bash
crontab -e
```

Add this line to run every 3 days at 9am:
```cron
0 9 */3 * * cd ~/Development/reddit-capital-rotation && /usr/bin/python3 scripts/run_report.py >> logs/cron.log 2>&1
```

### Manual Runs

Just run whenever you want an update:
```bash
cd ~/Development/reddit-capital-rotation
python3 scripts/run_report.py
```

## Customizing Tracked Tickers

Edit `config.json` to add/remove tickers:

```json
{
  "tickers": {
    "Tier 1": ["YOUR", "TOP", "PICKS"],
    "Tier 2": ["MODERATE", "CONVICTION"],
    "Tier 3": ["SPECULATIVE", "PLAYS"]
  }
}
```

Run the report again and it'll track your new tickers.

## Analyzing Trends Over Time

### View All Reports

Open `_index.md` in Obsidian for links to all reports.

### Compare Week-Over-Week

1. Open two reports side-by-side in Obsidian
2. Look at "Ticker Momentum Analysis" sections
3. Compare "Changes Since Last Report"

### CSV Analysis

Import `data/ticker_history.csv` into Excel/Google Sheets:
- Filter by ticker to see mention trends
- Create charts of momentum over time
- Identify which themes are accelerating

## Tips for Best Results

### 1. Run Consistently

Generate reports every 2-3 days for best trend detection.

### 2. Read the Reddit Posts

The tool links to sources - always read the actual discussions before investing.

### 3. Track Your Decisions

Add notes in Obsidian about which tickers you invested in and why.

### 4. Update Tiers

As your conviction changes, update `config.json` tier assignments.

### 5. Watch for Saturation

When a ticker hits "Peak Saturation" phase, consider taking profits.

## Troubleshooting

### "config.json not found"

```bash
cp config.example.json config.json
```

Then edit with your settings.

### "Permission denied"

```bash
chmod +x scripts/run_report.py
```

### Reports not appearing in Obsidian

Check your `obsidian_vault_path` in `config.json` is correct:
```bash
ls ~/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/
```

### Want to save locally instead of Obsidian?

Change `config.json`:
```json
{
  "obsidian_vault_path": "~/Documents/Investment-Research",
  "reports_subfolder": "Reddit-Capital-Rotation"
}
```

## Advanced Usage

### Adding Web Search Integration

The current version generates report templates. To enable automatic data collection, you would need to:

1. Implement WebSearch API calls (see `report_generator.py`)
2. Parse search results for ticker mentions
3. Extract themes and sentiment

This requires additional development but the framework is in place.

### Integrating with Reddit API

For live Reddit data instead of web search:

1. Follow instructions in `SETUP.md` to get Reddit API credentials
2. Use the `reddit_monitor.py` script
3. Modify `report_generator.py` to pull from Reddit directly

## Next Steps

1. ✅ Generate your first report
2. ⏳ Open in Obsidian and review
3. ⏳ Run again in 2-3 days
4. ⏳ Compare the two reports
5. ⏳ Start tracking your investment decisions

---

**Questions?** Open an issue on GitHub or check the main README.md
