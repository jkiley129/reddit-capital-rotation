# Setup Guide

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/reddit-capital-rotation.git
cd reddit-capital-rotation
```

### 2. Install Dependencies (Optional - for monitoring script)
```bash
pip install -r requirements.txt
```

### 3. Reddit API Setup (Optional - for live monitoring)

To use the automated monitoring script, you'll need Reddit API credentials:

1. Go to https://www.reddit.com/prefs/apps
2. Click "Create App" or "Create Another App"
3. Fill in the form:
   - **Name**: reddit-capital-rotation-monitor
   - **App type**: Select "script"
   - **Description**: Personal capital rotation monitoring
   - **About URL**: (leave blank)
   - **Redirect URI**: http://localhost:8080
4. Click "Create app"

5. Create a `.env` file in the project root:
```bash
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=reddit_capital_rotation_monitor/1.0
```

6. Update `scripts/reddit_monitor.py` to load credentials from `.env`:
```python
from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_USER_AGENT')
)
```

### 4. Run the Monitoring Script
```bash
python scripts/reddit_monitor.py
```

## Project Structure

```
reddit-capital-rotation/
├── README.md                                    # Main documentation
├── SETUP.md                                     # This file
├── LICENSE                                      # MIT License
├── requirements.txt                             # Python dependencies
├── .gitignore                                   # Git ignore rules
├── reddit_capital_rotation_strategy.md          # Full strategy methodology
├── TOP_10_THEMES_QUICK_REFERENCE.md            # Quick reference guide
├── analysis/
│   └── 2026_emerging_themes_analysis.md        # Current theme analysis
├── data/
│   └── example_report.txt                       # Example monitoring output
└── scripts/
    └── reddit_monitor.py                        # Monitoring script
```

## Usage Without Coding

If you don't want to set up the Python monitoring script, you can still use this strategy manually:

1. Read `reddit_capital_rotation_strategy.md` for the full methodology
2. Review `analysis/2026_emerging_themes_analysis.md` for current themes
3. Use `TOP_10_THEMES_QUICK_REFERENCE.md` for quick positioning guide
4. Manually browse the key subreddits listed in the strategy
5. Track mention frequency and sentiment yourself

## Contributing

This is a personal research repository, but if you'd like to suggest improvements:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request with your improvements

## Security Note

**NEVER commit API keys or credentials to the repository!**

The `.gitignore` file is configured to exclude:
- `.env` files
- `credentials.json`
- Any files with `_credentials.txt` suffix

## Support

For questions or issues:
- Open an issue on GitHub
- Review the strategy documentation
- Check the example report for expected output format

## Disclaimer

This is not financial advice. All investments carry risk. See LICENSE for full disclaimer.
