#!/bin/bash
# Quick runner script for generating live Reddit Capital Rotation reports

echo "=================================="
echo "Reddit Capital Rotation Reporter"
echo "=================================="
echo ""

# Check if config exists
if [ ! -f "config.json" ]; then
    echo "❌ Error: config.json not found!"
    echo "   Please create config.json first"
    exit 1
fi

# Run the live report generator
echo "🚀 Generating live report with real web search data..."
echo ""

python3 scripts/execute_live_report.py

# Check if successful
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Report generation complete!"
    echo ""
    echo "📁 Open your Obsidian vault to view the report:"
    echo "   Investment Research/Reddit Capital Rotation/"
    echo ""
else
    echo ""
    echo "❌ Report generation failed"
    echo "   Check the error messages above"
    exit 1
fi
