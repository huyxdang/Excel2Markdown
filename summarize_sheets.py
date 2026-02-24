#!/usr/bin/env python3
"""
Summarize Excel sheets using Claude API with optional image analysis.

Usage:
    python summarize_sheets.py <sheets_dir> <output_dir> [--api-key KEY] [--workers N]

(Example Usage) 
    python summarize_sheets.py output/sheets output/summaries

Output:
    output/summaries/
    ├── 0.md
    ├── 1.md
    ├── 5.md
    ├── 5.1.1a.md
    └── ...
    output/summaries/_index.md (summary index)
"""

import sys
import os
import csv
import glob
import re
import base64
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

SCRIPT_DIR = Path(__file__).parent

# Pricing per million tokens (USD) - Haiku 4.5
HAIKU_INPUT_COST = 0.80    # $0.80 / MTok
HAIKU_OUTPUT_COST = 4.0    # $4 / MTok


def load_prompt(filepath: Path) -> str:
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def load_sheet_content(csv_path: str, max_rows: int = 500) -> tuple[str, int]:
    """Load CSV sheet content as text, limited to max_rows."""
    rows = []
    total_rows = 0

    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            for i, row in enumerate(csv.reader(f)):
                total_rows += 1
                if i < max_rows:
                    rows.append(','.join(row))

        content = '\n'.join(rows)
        if total_rows > max_rows:
            content += f"\n\n... ({total_rows - max_rows} more rows truncated)"
        return content, total_rows
    except Exception as e:
        print(f"Error reading {csv_path}: {e}")
        return "", 0


def extract_image_references(csv_content: str) -> list[dict]:
    """Extract markdown image references from CSV content."""
    results = []
    
    # Pattern: "B5: ![desc](images/filename.png)"
    for match in re.finditer(r'([A-Z]+\d+):\s*(!\[[^\]]*\]\(images/[^)]+\))', csv_content):
        results.append({'cell': match.group(1), 'markdown': match.group(2)})
    
    # Standalone images without cell prefix
    found = {r['markdown'] for r in results}
    for img in re.findall(r'(!\[[^\]]*\]\(images/[^)]+\))', csv_content):
        if img not in found:
            results.append({'cell': 'Unknown', 'markdown': img})
    
    return results


def load_image_as_base64(image_path: str):
    """Load image file as (base64_data, media_type) or None."""
    if not os.path.exists(image_path):
        return None
    
    media_types = {'.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', 
                   '.gif': 'image/gif', '.webp': 'image/webp'}
    media_type = media_types.get(Path(image_path).suffix.lower())
    if not media_type:
        return None
    
    try:
        with open(image_path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8'), media_type
    except Exception:
        return None


def summarize_sheet(client: Anthropic, sheet_name: str, csv_path: str,
                    images_dir: str = None, max_tokens: int = 3000) -> tuple[str, dict]:
    """Use Claude API to summarize a single sheet with optional image analysis.

    Returns:
        (summary_text, usage_dict) where usage_dict has input_tokens and output_tokens.
    """
    empty_usage = {'input_tokens': 0, 'output_tokens': 0}

    content, row_count = load_sheet_content(csv_path)
    if not content:
        return f"# {sheet_name}\n\n*Error: Could not read sheet content*", empty_usage

    images = extract_image_references(content)
    prompt_template = load_prompt(SCRIPT_DIR / "prompts" / "summarization_prompt.md")
    prompt = prompt_template.format(sheet_name=sheet_name, content=content)

    # Load actual images if available
    loaded_images = []
    if images_dir and images:
        for img in images:
            match = re.search(r'\(images/([^)]+)\)', img['markdown'])
            if match:
                filename = match.group(1)
                image_data = load_image_as_base64(os.path.join(images_dir, filename))
                if image_data:
                    loaded_images.append({
                        'cell': img['cell'], 'markdown': img['markdown'],
                        'filename': filename, 'base64': image_data[0], 'media_type': image_data[1]
                    })

    # Build message content
    message_content = []

    if loaded_images:
        prompt += f"\n\n**HÌNH ẢNH ĐÍNH KÈM:** Sheet này có {len(loaded_images)} hình ảnh. Hãy phân tích từng hình ảnh.\n"
        for i, img in enumerate(loaded_images, 1):
            prompt += f"Hình {i} (Cell {img['cell']}): `{img['markdown']}`\n"

        message_content.append({"type": "text", "text": prompt})
        for img in loaded_images:
            message_content.append({
                "type": "image",
                "source": {"type": "base64", "media_type": img['media_type'], "data": img['base64']}
            })
    else:
        message_content.append({"type": "text", "text": prompt})

    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": message_content}]
        )
        summary = response.content[0].text
        usage = {
            'input_tokens': response.usage.input_tokens,
            'output_tokens': response.usage.output_tokens,
        }

        # Append guaranteed image reference section
        if images:
            summary += "\n\n## 10. Danh sách hình ảnh (trích xuất tự động)\n\n"
            for img in images:
                match = re.search(r'\(images/([^)]+)\)', img['markdown'])
                if match:
                    summary += f"- Cell {img['cell']}: `<<IMAGE:{match.group(1)}>>`\n"

        source_ext = Path(csv_path).suffix
        summary += f"\n\n---\n*Source: {sheet_name}{source_ext} | Rows: {row_count} | Images analyzed: {len(loaded_images)}*\n"
        return summary, usage

    except Exception as e:
        return f"# {sheet_name}\n\n*Error generating summary: {e}*", empty_usage


def process_sheet(csv_path: str, output_dir: str, images_dir: str, client: Anthropic,
                  index: int, total: int) -> dict:
    """Process a single sheet - worker function."""
    sheet_name = Path(csv_path).stem
    output_md = os.path.join(output_dir, f"{sheet_name}.md")

    try:
        summary, usage = summarize_sheet(client, sheet_name, csv_path, images_dir)
        with open(output_md, 'w', encoding='utf-8') as f:
            f.write(summary)

        size = os.path.getsize(output_md)
        in_tok = usage['input_tokens']
        out_tok = usage['output_tokens']
        print(f"[{index}/{total}] ✓ '{sheet_name}' ({size:,} bytes | {in_tok:,}+{out_tok:,} tokens)")
        return {'status': 'success', 'sheet_name': sheet_name, 'size': size,
                'input_tokens': in_tok, 'output_tokens': out_tok}
    except Exception as e:
        print(f"[{index}/{total}] ✗ '{sheet_name}' - {e}")
        return {'status': 'failed', 'sheet_name': sheet_name, 'error': str(e),
                'input_tokens': 0, 'output_tokens': 0}


def _compute_cost(r: dict) -> float:
    """Compute cost for a single sheet result using Haiku pricing."""
    return (
        r['input_tokens'] * HAIKU_INPUT_COST +
        r['output_tokens'] * HAIKU_OUTPUT_COST
    ) / 1_000_000


def _write_token_report(output_dir: str, sheet_results: list[dict]) -> str:
    """Write token usage report as markdown table. Returns report path."""
    report_path = os.path.join(output_dir, 'token_report.md')

    total_in = sum(r['input_tokens'] for r in sheet_results)
    total_out = sum(r['output_tokens'] for r in sheet_results)
    total_cost = sum(_compute_cost(r) for r in sheet_results)

    lines = [
        "# Token Usage Report\n",
        "## Summarization (claude-haiku-4.5)\n",
        "| Sheet | Input Tokens | Output Tokens | Cost ($) |",
        "|-------|-------------|--------------|----------|",
    ]

    for r in sorted(sheet_results, key=lambda x: x['sheet_name']):
        cost = _compute_cost(r)
        lines.append(f"| {r['sheet_name']} | {r['input_tokens']:,} | {r['output_tokens']:,} | {cost:.4f} |")

    lines.append(f"| **Total** | **{total_in:,}** | **{total_out:,}** | **{total_cost:.4f}** |")
    lines.append("")

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

    return report_path


def summarize_all_sheets(sheets_dir: str, output_dir: str, api_key: str,
                         max_workers: int = 5, images_dir: str = None) -> dict:
    """Summarize all CSV sheets using parallel processing."""
    os.makedirs(output_dir, exist_ok=True)
    sheet_files = sorted(glob.glob(os.path.join(sheets_dir, "*.csv")))

    if not sheet_files:
        print(f"No CSV files found in {sheets_dir}")
        return {'success': [], 'failed': []}

    total = len(sheet_files)
    print(f"Processing {total} sheets with {max_workers} workers\n" + "-" * 40)

    results = {'success': [], 'failed': []}
    all_sheet_results = []

    client = Anthropic(api_key=api_key)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(process_sheet, sf, output_dir, images_dir, client,
                          i+1, total): sf
            for i, sf in enumerate(sheet_files)
        }

        for future in as_completed(futures):
            result = future.result()
            all_sheet_results.append(result)
            results['success' if result['status'] == 'success' else 'failed'].append(result['sheet_name'])

    # Write token usage report
    successful = [r for r in all_sheet_results if r['status'] == 'success']
    if successful:
        report_path = _write_token_report(output_dir, successful)
        total_cost = sum(_compute_cost(r) for r in successful)
        total_in = sum(r['input_tokens'] for r in successful)
        total_out = sum(r['output_tokens'] for r in successful)
        print(f"\n📊 Tokens: {total_in:,} in + {total_out:,} out = ${total_cost:.4f}")
        print(f"📄 Report: {report_path}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Summarize Excel sheets using Claude API")
    parser.add_argument('sheets_dir', help='Directory containing CSV files')
    parser.add_argument('output_dir', help='Directory for markdown summaries')
    parser.add_argument('--api-key', help='Anthropic API key')
    parser.add_argument('--workers', '-w', type=int, default=5, help='Parallel workers (default: 5)')
    parser.add_argument('--images-dir', '-i', help='Directory with images for visual analysis')
    args = parser.parse_args()
    
    if not os.path.exists(args.sheets_dir):
        sys.exit(f"Error: Directory not found: {args.sheets_dir}")
    
    api_key = args.api_key or os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        sys.exit("Error: No API key. Set ANTHROPIC_API_KEY or use --api-key")
    
    images_dir = args.images_dir if args.images_dir and os.path.exists(args.images_dir) else None
    
    results = summarize_all_sheets(args.sheets_dir, args.output_dir, api_key, args.workers, images_dir)
    
    print(f"\n{'='*40}\n✅ Done: {len(results['success'])} success, {len(results['failed'])} failed")


if __name__ == "__main__":
    main()