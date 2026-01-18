#!/usr/bin/env python3
"""
Simple runner script for generating Reddit Capital Rotation reports
"""

import sys
from pathlib import Path

# Add parent directory to path so we can import report_generator
sys.path.insert(0, str(Path(__file__).parent))

import report_generator

if __name__ == "__main__":
    print("🚀 Starting Reddit Capital Rotation Report Generation\n")

    try:
        report_generator.main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Report generation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error generating report: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
