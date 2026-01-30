#!/usr/bin/env python3
"""
BRD Pipeline - Excel to Markdown Business Requirements Document

Usage:
    python main.py <excel_file> [--output-dir DIR] [--api-key KEY]
"""

import sys
import os
import argparse
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def run_command(cmd: list, description: str) -> tuple[bool, float]:
    """Run a command and return (success, duration_seconds)."""
    print(f"\n{'='*60}\n📋 {description}\n{'='*60}\n")
    
    start = datetime.now()
    try:
        subprocess.run(cmd, check=True, text=True)
        return True, (datetime.now() - start).total_seconds()
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"\n❌ Error: {e}")
        return False, (datetime.now() - start).total_seconds()


def format_duration(seconds: float) -> str:
    """Format duration in human-readable format."""
    m, s = divmod(seconds, 60)
    h, m = divmod(int(m), 60)
    if h:
        return f"{h}h {m}m {s:.1f}s"
    elif m:
        return f"{m}m {s:.1f}s"
    return f"{s:.1f}s"


def main():
    parser = argparse.ArgumentParser(description="Convert Excel BRD to Markdown")
    parser.add_argument('excel_file', help='Input Excel file (.xlsx)')
    parser.add_argument('--output-dir', '-o', default='./output', help='Output directory')
    parser.add_argument('--api-key', help='Anthropic API key')
    parser.add_argument('--max-tokens', type=int, default=32000, help='Max tokens for synthesis')
    parser.add_argument('--skip-extract', action='store_true', help='Skip extraction step')
    parser.add_argument('--skip-summarize', action='store_true', help='Skip summarization step')
    parser.add_argument('--skip-images', action='store_true', help='Skip image analysis')
    parser.add_argument('--workers', '-w', type=int, default=10, help='Parallel workers')
    parser.add_argument('--clean', action='store_true', help='Clean output directory first')
    args = parser.parse_args()
    
    # Validate inputs
    excel_path = Path(args.excel_file).resolve()
    if not excel_path.exists():
        sys.exit(f"❌ Error: Excel file not found: {excel_path}")
    
    api_key = args.api_key or os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        sys.exit("❌ Error: No API key. Set ANTHROPIC_API_KEY or use --api-key")
    
    # Setup paths
    script_dir = Path(__file__).parent.resolve()
    output_dir = Path(args.output_dir).resolve()
    sheets_dir = output_dir / 'sheets'
    images_dir = output_dir / 'images'
    summaries_dir = output_dir / 'summaries'
    final_brd_path = output_dir / 'final_brd.md'
    
    if args.clean and output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n🚀 BRD PIPELINE: {excel_path.name} → {output_dir}")
    
    start_time = datetime.now()
    timings = {}
    
    # Step 1: Extract
    if not args.skip_extract:
        success, timings['extract'] = run_command(
            [sys.executable, str(script_dir / 'extract_all_sheets.py'), str(excel_path), str(output_dir)],
            "Step 1/3: Extracting sheets"
        )
        if not success:
            sys.exit(1)
    
    # Step 2: Summarize
    if not args.skip_summarize:
        cmd = [
            sys.executable, str(script_dir / 'summarize_sheets.py'),
            str(sheets_dir), str(summaries_dir),
            '--api-key', api_key, '--workers', str(args.workers)
        ]
        if not args.skip_images and images_dir.exists() and any(images_dir.glob('*')):
            cmd.extend(['--images-dir', str(images_dir)])
        
        success, timings['summarize'] = run_command(cmd, "Step 2/3: Summarizing sheets")
        if not success:
            sys.exit(1)
    
    # Step 3: Synthesize
    success, timings['synthesize'] = run_command(
        [sys.executable, str(script_dir / 'brd_synthesize.py'),
         str(summaries_dir), str(final_brd_path),
         '--api-key', api_key, '--max-tokens', str(args.max_tokens)],
        "Step 3/3: Synthesizing BRD"
    )
    if not success:
        sys.exit(1)
    
    # Summary
    total = (datetime.now() - start_time).total_seconds()
    print(f"\n{'='*60}")
    print(f"✅ COMPLETE in {format_duration(total)}")
    print(f"📄 Output: {final_brd_path}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()