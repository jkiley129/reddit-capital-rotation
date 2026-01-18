#!/usr/bin/env python3
"""
Runner script that executes web searches and generates live reports
This script should be called from Claude Code which has access to WebSearch
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

import live_report_generator

def main():
    """
    Main runner function

    NOTE: This script is designed to be called from Claude Code environment
    which will provide web search capabilities. When run standalone, it will
    generate a template report.
    """
    print("🚀 Starting Live Reddit Capital Rotation Report Generation\n")

    print("⚠️  NOTICE: This script requires WebSearch capability")
    print("   Please run this from Claude Code environment for live data")
    print("   Running standalone will generate a template report\n")

    try:
        # When called from Claude Code, search_results will be injected
        # For now, generate with empty results
        live_report_generator.main(search_results=None)

    except KeyboardInterrupt:
        print("\n\n⚠️  Report generation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error generating report: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
