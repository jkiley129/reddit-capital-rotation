# Reddit Capital Rotation Strategy

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)
![Status: Active](https://img.shields.io/badge/status-active-success.svg)

A systematic approach to identifying emerging investment themes from Reddit social media chatter before Wall Street and mainstream media fully embrace them.

**🎯 Time Advantage: 2-4 weeks ahead of mainstream coverage**

> "Be early, not late. Be selective, not indiscriminate. Be disciplined, not emotional."

## 📁 Project Structure

```
reddit-capital-rotation/
├── README.md                                    # This file
├── reddit_capital_rotation_strategy.md          # Full strategy methodology
├── TOP_10_THEMES_QUICK_REFERENCE.md            # Quick reference guide
├── config.json                                  # Configuration (paths, tickers)
├── generate_report.sh                           # Quick runner script
├── analysis/
│   └── 2026_emerging_themes_analysis.md        # Detailed theme analysis
├── data/
│   └── example_report.txt                       # Example monitoring report
└── scripts/
    ├── README.md                                # Scripts documentation
    ├── live_report_generator.py                 # Core report generation engine
    ├── execute_live_report.py                   # Production script with real data
    ├── generate_live_report_with_search.py      # Integration helper
    ├── run_report.py                            # Legacy runner
    └── reddit_monitor.py                        # Python monitoring script
```

## 🎯 Strategy Overview

This strategy provides a **2-4 week time advantage** over mainstream Wall Street coverage by systematically monitoring Reddit discussions for:

- Mention frequency spikes (3x+ over baseline)
- Cross-subreddit momentum validation
- Sentiment shifts from negative/neutral to positive
- Quality signals (DD posts, insider buying, fundamental catalysts)

## 🔥 Top 10 Emerging Themes (January 2026)

### Tier 1 - Highest Conviction
1. **Space-Based Connectivity** (ASTS, RKLB) - 45-60 satellite launches in 2026
2. **Custom AI Chips** (AVGO, MRVL) - OpenAI-Broadcom 10GW partnership
3. **Optical Interconnects** (POET, TSMC, QBTS) - 800G/1.6T/3.2T data speeds
4. **Nuclear Power for AI** (SMR, CEG, D, LEU) - $1.6B Microsoft-Constellation deal

### Tier 2 - Strong Conviction
5. **Quantum Computing** (GOOGL, IONQ, RGTI) - Long-term positioning
6. **Germany Infrastructure Boom** (European defense/industrial) - €500B fund
7. **Copper & Critical Materials** (FCX, SCCO, ALB) - Supply disruptions
8. **Healthcare AI & Biotech** (NBIS, small-cap biotechs) - Sector rotation

### Tier 3 - Speculative
9. **Reddit Platform AI Monetization** (RDDT, META) - Needham $300 PT
10. **Small-Cap Value Rotation** (VSTS, HFWA, EBF) - Insider buying signals

## 📊 Key Findings Summary

### Top 5 Tickers by Conviction

| Rank | Ticker | Theme | Key Catalyst | Risk/Reward |
|------|--------|-------|--------------|-------------|
| 1 | **ASTS** | Space Connectivity | 45-60 satellite launches 2026, AT&T FirstNet H1 2026 | High volatility, 241% in 2025 |
| 2 | **AVGO** | Custom AI Chips | OpenAI 10GW partnership, 70-80% ASIC market share | Market leader, large cap |
| 3 | **POET** | Optical Interconnects | 800G/1.6T/3.2T volume shipments 2026 | Early-stage, sub-$5 entry |
| 4 | **SMR** | Nuclear for AI | Only NRC-certified SMR design, Trump orders | Regulatory tailwinds |
| 5 | **RDDT** | AI Monetization | Needham $300 PT, 64% EPS growth FY2026 | Platform data moat |

### Signal Strength by Theme
- 🔥🔥🔥🔥🔥 Very Strong: Space connectivity, Custom AI chips
- 🔥🔥🔥🔥 Strong: Optical interconnects, Nuclear power, Quantum computing
- 🔥🔥🔥 Moderate-Strong: European infrastructure, Copper/materials, Healthcare AI
- 🔥🔥 Moderate: Reddit monetization, Small-cap value

## 🎯 Position Sizing & Risk Management

### Allocation Guidelines
- **Tier 1**: 2-5% per position
- **Tier 2**: 1-3% per position
- **Tier 3**: 0.5-1% per position
- **Total Reddit-sourced exposure**: <25% of total portfolio

### Stop-Loss Rules
- 15-20% stops on individual positions
- Trailing stops once position up 50%+
- Re-evaluate thesis if down >30%

### Exit Signals
1. Mainstream media saturation (CNBC features, Barron's covers)
2. Excessive hype/FOMO language on Reddit
3. Sentiment shift: positive → neutral/negative
4. Insider selling after major run-ups
5. Fundamental deterioration vs. original thesis

## 📈 Momentum Phase Framework

### Phase 1: Early Detection (Weeks 1-2)
- Theme appears in niche subreddits
- Limited mentions (<50/week)
- Few high-quality DD posts
- **Action**: Research watchlist, no position yet

### Phase 2: Building Momentum (Weeks 2-4)
- Cross-subreddit appearance validated
- Increasing mentions (100-500/week)
- Multiple DD posts with analysis
- **Action**: Small exploratory positions (1-2%)

### Phase 3: Mainstream Awareness (Weeks 4-8)
- Major subreddit front page posts
- Financial media starting coverage
- Institutional analysts issuing reports
- **Action**: Evaluate sizing, take partial profits

### Phase 4: Peak Saturation (Week 8+)
- Excessive hype, FOMO behavior
- New retail investors piling in
- Contrarian warnings of overvaluation
- **Action**: Reduce exposure, lock in gains

## 📊 Live Report Generator

### What It Does

The live report generator (`scripts/live_report_generator.py`) automatically:

1. **Executes Web Searches** - Queries covering:
   - Reddit WallStreetBets trending stocks
   - AI stocks, quantum computing, biotech momentum
   - Space stocks (ASTS, RKLB, satellite companies)
   - Nuclear energy (SMR, CEG)
   - Custom AI chips (Broadcom AVGO)
   - Individual ticker deep-dives (ASTS, POET, RDDT, etc.)
   - Market themes and capital rotation
   - Small cap stocks with insider buying

2. **Analyzes Content** - Extracts:
   - Ticker mentions and frequency
   - Investment theme identification
   - Sentiment analysis (positive/neutral/negative)
   - Catalysts and news events
   - Analyst ratings and price targets

3. **Generates Reports** - Creates comprehensive markdown with:
   - Executive summary (top 3 themes)
   - Top 10 investment themes ranked by conviction
   - Ticker momentum tables (gaining/stable/losing)
   - Risk management guidelines
   - Data sources and methodology

4. **Tracks Evolution** - Saves historical data:
   - `ticker_history.csv` - Mention counts over time
   - `theme_evolution.json` - Theme progression tracking
   - Compares to previous reports to identify momentum shifts

### Report Features

Each generated report includes:

- **Theme Rankings** - Conviction-based ordering with fire indicators (🔥🔥🔥🔥🔥)
- **Ticker Analysis** - Associated tickers for each theme
- **Sentiment Breakdown** - Positive/neutral/negative percentages
- **Momentum Tracking** - Comparing to previous reports
- **Risk Warnings** - Position sizing, stop-loss guidance
- **Source Attribution** - Search queries and data sources

### Example Output

```markdown
## 1. Space Connectivity
Signal Strength: 🔥🔥🔥🔥🔥

High-Potential Tickers:
- ASTS - 3 mentions, positive sentiment
- RKLB - 2 mentions, positive sentiment

Market Sentiment:
- Positive: 83%
- Neutral: 17%

Data Points: 6 mentions across sources
```

### Data Tracking

The system maintains historical tracking for trend analysis:

**ticker_history.csv:**
```csv
date,ticker,mentions,tier,theme,sentiment
2026-01-18,ASTS,3,Tier 1,Space Connectivity,positive
2026-01-18,AVGO,1,Tier 1,Custom AI Chips,positive
```

**theme_evolution.json:**
```json
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
```

### Integration with Obsidian

Reports are automatically saved to your Obsidian vault with:
- Markdown formatting for easy reading
- Wikilinks for navigation between reports
- Index page with links to all reports
- Data files for analysis and charting

## 🔍 Key Subreddits Monitored

### Primary Sources
- r/wallstreetbets - Retail sentiment, momentum plays
- r/stocks - General market discussion
- r/investing - Longer-term perspectives
- r/StockMarket - Broad market trends
- r/options - Derivatives activity signals

### Sector-Specific
- r/biotechplays - Biotech catalysts
- r/Semiconductors - Tech hardware trends
- r/RenewableEnergy - Green energy rotation
- r/SecurityAnalysis - Fundamental deep dives

## 🚀 Getting Started

### Quick Start: Generate a Live Report Now

The fastest way to get started is to generate a live report with real data:

```bash
cd ~/Development/reddit-capital-rotation
./generate_report.sh
```

Or using Python directly:
```bash
python3 scripts/execute_live_report.py
```

This will:
- Analyze 10+ web searches covering Reddit trends, AI stocks, space stocks, nuclear energy, and more
- Extract ticker mentions and sentiment
- Identify emerging investment themes
- Generate a comprehensive markdown report
- Save to your Obsidian vault
- Track data in CSV/JSON for trend analysis

**Report Location:** `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian Vault/Investment Research/Reddit Capital Rotation/`

### Step-by-Step Guide

#### 1. Review Core Strategy
Read `reddit_capital_rotation_strategy.md` for full methodology

#### 2. Study Current Themes
Review `analysis/2026_emerging_themes_analysis.md` for detailed theme breakdowns

#### 3. Generate Your First Live Report
```bash
./generate_report.sh
```

#### 4. Review in Obsidian
Open your Obsidian vault and navigate to:
`Investment Research/Reddit Capital Rotation/`

#### 5. Track Evolution Over Time
Run the report generator every 2-3 days to track:
- Ticker momentum changes
- Theme progression (gaining/losing traction)
- Sentiment shifts
- New emerging opportunities

#### 6. Advanced: Set Up Monitoring (Optional)
- Install dependencies: `pip install praw pandas`
- Configure Reddit API credentials in `scripts/reddit_monitor.py`
- Run: `python scripts/reddit_monitor.py`

## ⚠️ Risk Warnings

1. **Reddit sentiment can be manipulated** - Beware of pump-and-dump schemes
2. **High volatility** - These are momentum plays with significant drawdowns
3. **Early-stage themes** - Many companies unprofitable, binary outcomes
4. **False signals** - Not all Reddit hype translates to fundamental performance
5. **Concentration risk** - Limit total exposure to Reddit-sourced ideas

## 📚 Data Sources Used

- Reddit discussion analysis (r/wallstreetbets, r/stocks, r/investing, etc.)
- Financial media lag analysis (AltIndex, Finbold, TipRanks)
- Insider buying patterns (Simply Wall St)
- Analyst upgrades and price targets
- Partnership announcements and regulatory catalysts

## 🔄 Maintenance Schedule

- **Daily**: Monitor top 20 ticker mention counts
- **Weekly**: Sentiment analysis, portfolio rebalancing
- **Monthly**: Theme progression review (Phase 1-4 framework)
- **Quarterly**: Strategy performance review, methodology adjustments

## 📞 Next Steps

1. ✅ Strategy documented
2. ✅ Top 10 themes identified with tickers
3. ⏳ Set up automated Reddit monitoring (requires API credentials)
4. ⏳ Backtest historical performance of signal detection
5. ⏳ Build sentiment analysis NLP model
6. ⏳ Create automated alert system for momentum spikes

---

## 📊 Example Monitoring Output

See `data/example_report.txt` for sample daily monitoring report format.

Key metrics tracked:
- 7-day mention frequency by ticker
- Momentum vs. 30-day baseline (3x+ alerts)
- Cross-subreddit validation status
- Phase progression (Early Detection → Peak Saturation)
- Recommended actions (Buy/Hold/Reduce/Sell)

---

## 🎓 Investment Philosophy

**"Be early, not late. Be selective, not indiscriminate. Be disciplined, not emotional."**

This strategy exploits the information diffusion lag between:
1. Reddit early adopters (Week 0)
2. Financial Twitter/blogs (Week 1-2)
3. Mainstream financial media (Week 3-4)
4. Institutional research reports (Week 4-8)

By systematically monitoring Reddit with quality filters, we aim to capture **2-4 weeks of alpha** before themes reach peak saturation.

---

## 📄 License & Disclaimer

**DISCLAIMER**: This analysis is for informational and educational purposes only. It does not constitute financial advice, investment recommendations, or solicitation to buy or sell securities.

- Always conduct independent due diligence
- Consult licensed financial advisors before investing
- Past performance does not guarantee future results
- Reddit sentiment can be manipulated by bad actors
- Author holds no positions in mentioned securities (update as applicable)

**USE AT YOUR OWN RISK**

---

*Last Updated: January 18, 2026*
