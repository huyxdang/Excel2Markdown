#!/usr/bin/env python3
"""
BRD Pipeline - Excel to Markdown Business Requirements Document

Orchestrates the full pipeline:
1. extract_all_sheets.py - Extract all sheets from Excel to CSV
2. summarize_sheets.py - Summarize each sheet using Claude API
3. brd_synthesize.py - Synthesize summaries into final BRD

Usage:
    python main.py <excel_file> [--output-dir DIR] [--api-key KEY]

Example:
    python main.py input.xlsx
    python main.py input.xlsx --output-dir ./output
    python main.py input.xlsx --output-dir ./output --api-key sk-ant-...

Output Structure:
    output/
    ├── sheets/          # Extracted CSV files
    │   ├── 0.csv
    │   ├── 1.csv
    │   └── ...
    ├── images/          # Extracted images
    │   ├── 5_1_1a_B5_image1.png
    │   └── ...
    ├── summaries/       # Sheet summaries (markdown)
    │   ├── 0.md
    │   ├── 1.md
    │   └── ...
    └── final_brd.md     # Final Business Requirements Document

Environment:
    ANTHROPIC_API_KEY - API key for Claude (or use --api-key)
"""

import sys
import os
import argparse
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_script_dir() -> Path:
    """Get the directory where this script is located."""
    return Path(__file__).parent.resolve()


def run_command(cmd: list, description: str) -> tuple[bool, float]:
    """
    Run a command and return success status and duration.
    
    Args:
        cmd: Command and arguments as list
        description: Description for logging
        
    Returns:
        Tuple of (success: bool, duration_seconds: float)
    """
    print(f"\n{'='*60}")
    print(f"📋 {description}")
    print(f"{'='*60}")
    print(f"Command: {' '.join(cmd)}\n")
    
    start = datetime.now()
    
    try:
        result = subprocess.run(
            cmd,
            check=True,
            text=True
        )
        duration = (datetime.now() - start).total_seconds()
        return True, duration
    except subprocess.CalledProcessError as e:
        duration = (datetime.now() - start).total_seconds()
        print(f"\n❌ Error: {description} failed with exit code {e.returncode}")
        return False, duration
    except FileNotFoundError as e:
        duration = (datetime.now() - start).total_seconds()
        print(f"\n❌ Error: Script not found - {e}")
        return False, duration


def format_duration(seconds: float) -> str:
    """Format duration in human-readable format."""
    if seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        secs = seconds % 60
        return f"{minutes}m {secs:.1f}s"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = seconds % 60
        return f"{hours}h {minutes}m {secs:.1f}s"


def check_dependencies(script_dir: Path) -> bool:
    """
    Check that all required scripts exist.
    
    Returns:
        True if all dependencies found, False otherwise
    """
    required_scripts = [
        'extract_all_sheets.py',
        'summarize_sheets.py',
        'brd_synthesize.py'
    ]
    
    missing = []
    for script in required_scripts:
        script_path = script_dir / script
        if not script_path.exists():
            missing.append(script)
    
    if missing:
        print("❌ Missing required scripts:")
        for script in missing:
            print(f"   - {script}")
        return False
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Convert Excel BRD to Markdown - Full Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        'excel_file',
        help='Input Excel file (.xlsx)'
    )
    
    parser.add_argument(
        '--output-dir', '-o',
        default='./output',
        help='Output directory (default: ./output)'
    )
    
    parser.add_argument(
        '--api-key',
        help='Anthropic API key (uses ANTHROPIC_API_KEY env var if not provided)'
    )
    
    parser.add_argument(
        '--max-tokens',
        type=int,
        default=32000,
        help='Maximum tokens for BRD synthesis (default: 32000)'
    )
    
    parser.add_argument(
        '--skip-extract',
        action='store_true',
        help='Skip extraction step (use existing CSVs)'
    )
    
    parser.add_argument(
        '--skip-summarize',
        action='store_true',
        help='Skip summarization step (use existing summaries)'
    )
    
    parser.add_argument(
        '--clean',
        action='store_true',
        help='Clean output directory before starting'
    )
    
    args = parser.parse_args()
    
    # Validate input file
    excel_path = Path(args.excel_file).resolve()
    if not excel_path.exists():
        print(f"❌ Error: Excel file not found: {excel_path}")
        sys.exit(1)
    
    if not excel_path.suffix.lower() in ['.xlsx', '.xls', '.xlsm']:
        print(f"⚠️  Warning: File may not be an Excel file: {excel_path.suffix}")
    
    # Check API key
    api_key = args.api_key or os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ Error: No API key provided.")
        print("Please either:")
        print("  1. Create a .env file with: ANTHROPIC_API_KEY=sk-ant-...")
        print("  2. Set ANTHROPIC_API_KEY environment variable")
        print("  3. Use --api-key argument")
        sys.exit(1)
    
    # Setup paths
    script_dir = get_script_dir()
    output_dir = Path(args.output_dir).resolve()
    sheets_dir = output_dir / 'sheets'
    images_dir = output_dir / 'images'
    summaries_dir = output_dir / 'summaries'
    final_brd_path = output_dir / 'final_brd.md'
    
    # Check dependencies
    if not check_dependencies(script_dir):
        print("\n💡 Make sure all pipeline scripts are in the same directory as main.py")
        sys.exit(1)
    
    # Clean output directory if requested
    if args.clean and output_dir.exists():
        print(f"\n🧹 Cleaning output directory: {output_dir}")
        shutil.rmtree(output_dir)
    
    # Create output directories
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Print configuration
    print("\n" + "="*60)
    print("🚀 BRD PIPELINE - Excel to Markdown")
    print("="*60)
    print(f"Input:       {excel_path}")
    print(f"Output dir:  {output_dir}")
    print(f"Started:     {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    # Track timing
    start_time = datetime.now()
    timings = {}
    
    # =========================================================================
    # STEP 1: Extract all sheets from Excel
    # =========================================================================
    if not args.skip_extract:
        extract_script = script_dir / 'extract_all_sheets.py'
        success, duration = run_command(
            [sys.executable, str(extract_script), str(excel_path), str(output_dir)],
            "Step 1/3: Extracting sheets from Excel"
        )
        timings['extract'] = duration
        
        if not success:
            print("\n❌ Pipeline failed at extraction step")
            sys.exit(1)
        
        # Check that sheets were extracted
        if not sheets_dir.exists() or not any(sheets_dir.glob('*.csv')):
            print(f"\n❌ Error: No CSV files found in {sheets_dir}")
            sys.exit(1)
        
        csv_count = len(list(sheets_dir.glob('*.csv')))
        print(f"\n✅ Extracted {csv_count} sheets in {format_duration(duration)}")
    else:
        print("\n⏭️  Skipping extraction (--skip-extract)")
        timings['extract'] = 0
        if not sheets_dir.exists() or not any(sheets_dir.glob('*.csv')):
            print(f"❌ Error: No existing CSVs found in {sheets_dir}")
            sys.exit(1)
    
    # =========================================================================
    # STEP 2: Summarize each sheet using Claude
    # =========================================================================
    if not args.skip_summarize:
        summarize_script = script_dir / 'summarize_sheets.py'
        
        cmd = [
            sys.executable, str(summarize_script),
            str(sheets_dir), str(summaries_dir),
            '--api-key', api_key
        ]
        
        success, duration = run_command(
            cmd,
            "Step 2/3: Summarizing sheets with Claude"
        )
        timings['summarize'] = duration
        
        if not success:
            print("\n❌ Pipeline failed at summarization step")
            sys.exit(1)
        
        # Check that summaries were created
        if not summaries_dir.exists() or not any(summaries_dir.glob('*.md')):
            print(f"\n❌ Error: No summary files found in {summaries_dir}")
            sys.exit(1)
        
        summary_count = len([f for f in summaries_dir.glob('*.md') if f.name != '_index.md'])
        print(f"\n✅ Created {summary_count} summaries in {format_duration(duration)}")
    else:
        print("\n⏭️  Skipping summarization (--skip-summarize)")
        timings['summarize'] = 0
        if not summaries_dir.exists() or not any(summaries_dir.glob('*.md')):
            print(f"❌ Error: No existing summaries found in {summaries_dir}")
            sys.exit(1)
    
    # =========================================================================
    # STEP 3: Synthesize final BRD
    # =========================================================================
    synthesize_script = script_dir / 'brd_synthesize.py'
    
    cmd = [
        sys.executable, str(synthesize_script),
        str(summaries_dir), str(final_brd_path),
        '--api-key', api_key,
        '--max-tokens', str(args.max_tokens)
    ]
    
    success, duration = run_command(
        cmd,
        "Step 3/3: Synthesizing final BRD"
    )
    timings['synthesize'] = duration
    
    if not success:
        print("\n❌ Pipeline failed at synthesis step")
        sys.exit(1)
    
    # Check that BRD was created
    if not final_brd_path.exists():
        print(f"\n❌ Error: Final BRD not created at {final_brd_path}")
        sys.exit(1)
    
    print(f"\n✅ BRD synthesized in {format_duration(duration)}")
    
    # =========================================================================
    # COMPLETE
    # =========================================================================
    end_time = datetime.now()
    total_duration = (end_time - start_time).total_seconds()
    timings['total'] = total_duration
    
    # Get file sizes
    brd_size = final_brd_path.stat().st_size
    
    print("\n" + "="*60)
    print("✅ PIPELINE COMPLETE")
    print("="*60)
    
    # Timing breakdown
    print("\n⏱️  TIMING BREAKDOWN:")
    print("-"*40)
    if timings.get('extract', 0) > 0:
        print(f"  Step 1 (Extract):    {format_duration(timings['extract']):>12}")
    if timings.get('summarize', 0) > 0:
        print(f"  Step 2 (Summarize):  {format_duration(timings['summarize']):>12}")
    if timings.get('synthesize', 0) > 0:
        print(f"  Step 3 (Synthesize): {format_duration(timings['synthesize']):>12}")
    print("-"*40)
    print(f"  TOTAL:               {format_duration(total_duration):>12}")
    
    print(f"\n📁 Output directory: {output_dir}")
    print(f"\n📊 GENERATED FILES:")
    print("-"*40)
    print(f"  sheets/      - {len(list(sheets_dir.glob('*.csv'))):>3} CSV files")
    if images_dir.exists():
        image_count = len(list(images_dir.glob('*')))
        print(f"  images/      - {image_count:>3} images")
    print(f"  summaries/   - {len([f for f in summaries_dir.glob('*.md') if f.name != '_index.md']):>3} summaries")
    print(f"  final_brd.md - {brd_size:,} bytes")
    
    print("\n" + "="*60)
    print(f"📄 Final BRD: {final_brd_path}")
    print("="*60)


if __name__ == "__main__":
    main()