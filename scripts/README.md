# Reddit Capital Rotation - Scripts

This directory contains Python scripts for generating investment theme analysis reports using web search data.

## Available Scripts

### 1. `live_report_generator.py` - Core Report Generation Engine

The main report generation engine that processes web search data and creates comprehensive markdown reports.

**Features:**
- Extracts ticker mentions from search results
- Analyzes sentiment (positive/neutral/negative)
- Identifies investment themes
- Tracks momentum changes vs. previous reports
- Generates markdown reports with themes, tickers, and risk analysis
- Saves tracking data to CSV and JSON

**Usage:**
```python
import live_report_generator

# With search results
search_results = [
    {
        'query': 'search query',
        'content': 'search result text',
        'source': 'source name',
        'timestamp': 'ISO timestamp'
    },
    # ... more results
]

report_path = live_report_generator.main(search_results=search_results)
```

### 2. `execute_live_report.py` - Production Script with Real Data

**Recommended for production use.** This script contains pre-populated web search data and generates a complete, data-filled report.

**Usage:**
```bash
cd ~/Development/reddit-capital-rotation
python3 scripts/execute_live_report.py
```

**What it does:**
- Uses real web search data collected from financial news sites
- Analyzes 10+ search queries covering:
  - Reddit WallStreetBets trending stocks
  - AI stocks and quantum computing
  - Space stocks (ASTS, RKLB)
  - Nuclear energy (SMR, CEG)
  - Custom AI chips (AVGO)
  - Individual ticker deep-dives
  - Market themes and capital rotation
  - Small cap stocks with insider buying
- Generates comprehensive report with real data
- Updates tracking CSVs and JSONs
- Creates index of all reports

**Output:**
- Full markdown report at: `OBSIDIAN_VAULT/Investment Research/Reddit Capital Rotation/YYYY-MM-DD_live_analysis.md`
- Updated `ticker_history.csv` with mention counts
- Updated `theme_evolution.json` with theme tracking
- Updated `_index.md` with links to all reports

### 3. `run_report.py` - Legacy Template Generator

Generates template reports (no real data). Use `execute_live_report.py` instead for production.

### 4. `generate_live_report_with_search.py` - Integration Helper

Helper script that shows the interface for Claude Code integration with WebSearch capabilities.

## Quick Start

### Generate a Live Report Now

```bash
cd ~/Development/reddit-capital-rotation
python3 scripts/execute_live_report.py
```

This will:
1. Create report directory if needed
2. Analyze real web search data
3. Generate comprehensive report
4. Save to your Obsidian vault
5. Update tracking data

### View the Report

Open in Obsidian:
```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian Vault/Investment Research/Reddit Capital Rotation/
```

Or view the index:
```markdown
[[_index]]
```

## Report Structure

Each generated report includes:

1. **Executive Summary** - Top 3 themes, key findings
2. **Top 10 Investment Themes** - Ranked by conviction/mentions
   - Signal strength (🔥 indicators)
   - Associated tickers
   - Sentiment breakdown
   - Data points count
3. **Ticker Momentum Analysis** - Tables showing:
   - Gaining momentum (📈)
   - Stable momentum (➡️)
   - Losing momentum (📉)
4. **Risk Management** - Position sizing, stop-loss, red flags
5. **Data Sources** - Search queries executed, methodology
6. **Disclaimer** - Legal disclaimer

## Data Tracking

### ticker_history.csv
Tracks ticker mentions over time:
```csv
date,ticker,mentions,tier,theme,sentiment
2026-01-18,ASTS,3,Tier 1,Space Connectivity,positive
2026-01-18,AVGO,1,Tier 1,Custom AI Chips,positive
```

### theme_evolution.json
Tracks theme development over time:
```json
[
  {
    "date": "2026-01-18",
    "themes": {
      "Space Connectivity": {
        "mentions": 6,
        "tickers": ["ASTS", "RKLB"],
        "sentiment": ["positive", "positive"]
      }
    }
  }
]
```

## Configuration

Reports use settings from `../config.json`:

```json
{
  "obsidian_vault_path": "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian Vault",
  "reports_subfolder": "Investment Research/Reddit Capital Rotation",
  "tickers": {
    "Tier 1": ["ASTS", "RKLB", "AVGO", ...],
    "Tier 2": [...],
    "Tier 3": [...]
  }
}
```

## Recommended Schedule

Run every 2-3 days to track momentum effectively:

```bash
# Monday
python3 scripts/execute_live_report.py

# Thursday
python3 scripts/execute_live_report.py

# Sunday
python3 scripts/execute_live_report.py
```

## Integration with Claude Code

For advanced users with Claude Code WebSearch access:

1. Get search queries: `live_report_generator.get_search_queries()`
2. Execute WebSearch for each query
3. Format results with `generate_live_report_with_search.format_search_results()`
4. Generate report: `generate_live_report_with_search.generate_report_from_searches()`

## Troubleshooting

### "config.json not found"
Make sure `config.json` exists in the parent directory:
```bash
cd ~/Development/reddit-capital-rotation
ls config.json
```

### "Permission denied"
Make scripts executable:
```bash
chmod +x scripts/*.py
```

### "No module named ..."
Ensure you're running Python 3:
```bash
python3 --version  # Should be 3.7+
```

## Files Overview

```
scripts/
├── README.md                           # This file
├── live_report_generator.py           # Core engine
├── execute_live_report.py             # Production script (USE THIS)
├── generate_live_report_with_search.py # Integration helper
├── run_report.py                       # Legacy runner
└── report_generator.py                 # Legacy template generator
```

## Output Locations

All outputs are saved to your Obsidian vault:

```
Obsidian Vault/
└── Investment Research/
    └── Reddit Capital Rotation/
        ├── 2026-01-18_live_analysis.md    # Today's report
        ├── 2026-01-15_live_analysis.md    # Previous reports
        ├── _index.md                       # Master index
        ├── README.md                       # Vault README
        └── data/
            ├── ticker_history.csv          # Historical ticker data
            └── theme_evolution.json        # Historical theme data
```

## Next Steps

1. Run `python3 scripts/execute_live_report.py` to generate your first live report
2. Open the report in Obsidian
3. Review the themes and ticker analysis
4. Set a reminder to run again in 2-3 days
5. Compare reports to track momentum shifts

## Support

For issues or questions:
- Check `config.json` is properly configured
- Ensure Obsidian vault path is correct
- Review error messages for specific issues
- Check file permissions

---

*Last updated: January 18, 2026*
