#!/usr/bin/env python3
"""
Integration script for Claude Code to generate reports with real WebSearch data

This script demonstrates the interface for passing search results to the live report generator.
It should be called from Claude Code which has WebSearch capabilities.

Usage from Claude Code:
    1. Execute web searches for all queries
    2. Pass results to this script via the search_results parameter
    3. Generate comprehensive report with real data
"""

import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

import live_report_generator

def generate_report_from_searches(search_results_data):
    """
    Generate report from web search results

    Args:
        search_results_data: List of dicts with format:
            [
                {
                    'query': 'search query used',
                    'content': 'text content from search results',
                    'source': 'source URL or description',
                    'timestamp': 'when search was performed'
                },
                ...
            ]

    Returns:
        Path to generated report
    """
    print(f"\n{'='*70}")
    print("Generating Live Report with Web Search Data")
    print(f"{'='*70}\n")

    print(f"📊 Processing {len(search_results_data)} search result blocks\n")

    # Call the main report generator
    report_path = live_report_generator.main(search_results=search_results_data)

    return report_path

def format_search_results(raw_results):
    """
    Format raw search results into the expected structure

    Args:
        raw_results: Raw search results from WebSearch tool

    Returns:
        Formatted list of search result dictionaries
    """
    formatted = []

    for result in raw_results:
        formatted.append({
            'query': result.get('query', 'Unknown'),
            'content': result.get('content', ''),
            'source': result.get('source', 'Web Search'),
            'timestamp': datetime.now().isoformat()
        })

    return formatted

def main():
    """
    Main execution - expects search results to be provided

    For Claude Code integration:
    1. Claude executes WebSearch for all queries from get_search_queries()
    2. Claude formats results using format_search_results()
    3. Claude calls generate_report_from_searches() with formatted data
    """

    print("="*70)
    print("Live Report Generator - Claude Code Integration")
    print("="*70)
    print()
    print("📋 Search Queries Needed:")
    print()

    queries = live_report_generator.get_search_queries()
    for i, query in enumerate(queries, 1):
        print(f"   {i}. {query}")

    print()
    print("="*70)
    print()
    print("🤖 Instructions for Claude Code:")
    print()
    print("1. Execute WebSearch for each query above")
    print("2. Collect all search results")
    print("3. Format results using format_search_results()")
    print("4. Call generate_report_from_searches() with formatted data")
    print()
    print("This will generate a comprehensive report with REAL DATA")
    print()
    print("="*70)

if __name__ == "__main__":
    main()
