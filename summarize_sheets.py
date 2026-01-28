"""
Summarize Sheets using Claude API (Parallel Processing)

Analyzes each extracted CSV sheet using Claude Sonnet 4.5 and generates
structured markdown summaries suitable for BRD synthesis.

Uses parallel API calls for faster processing.

Usage:
    python summarize_sheets.py <sheets_dir> <output_dir> [--api-key KEY] [--workers N]

Example:
    python summarize_sheets.py output/sheets output/summaries
    python summarize_sheets.py output/sheets output/summaries --api-key sk-ant-...
    python summarize_sheets.py output/sheets output/summaries --workers 10
    
Environment:
    ANTHROPIC_API_KEY - API key for Claude (loaded from .env file or environment)
    
.env file format:
    ANTHROPIC_API_KEY=sk-ant-...
    
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
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


SUMMARIZATION_PROMPT = """Đọc sheet này từ tài liệu Yêu cầu Nghiệp vụ (BRD) và phân tích nội dung.

Tên sheet: {sheet_name}
Nội dung sheet (định dạng CSV):
{content}

Vui lòng đưa ra:

1. **Loại sheet**: Phân loại là một trong các loại: tổng-quan/quy-trình/giao-diện/đặc-tả/mô-hình-dữ-liệu/khác

2. **Mức độ chi tiết**: Phân loại là một trong hai loại:
   - `chi-tiết-cao`: Sheet chứa nhiều thông số kỹ thuật, số liệu cụ thể, validation rules, field specifications, hoặc data mapping → CẦN GIỮ NGUYÊN DẠNG BẢNG
   - `tổng-quan`: Sheet chứa mô tả quy trình, luồng công việc, hoặc thông tin high-level → CÓ THỂ CHUYỂN THÀNH PROSE/SECTIONS

3. **Chủ đề/tiêu đề chính**: Chủ đề hoặc mục đích chính của sheet này là gì?

4. **Tóm tắt thông tin chính**: Cung cấp 2-3 đoạn văn tóm tắt các thông tin thiết yếu, logic nghiệp vụ và yêu cầu trong sheet này.

5. **Các bên liên quan/vai trò được đề cập**: Liệt kê các cá nhân, nhóm, vai trò hoặc phòng ban được đề cập.

6. **Các yêu cầu tìm thấy**: Trích xuất các yêu cầu, đặc tả hoặc ràng buộc rõ ràng (nếu có).

7. **Các sheet liên quan**: Xác định các tham chiếu đến sheet khác, tài liệu hoặc hệ thống khác.

8. **Bảng cần giữ nguyên** (CHỈ khi mức độ chi tiết = `chi-tiết-cao`):
   Nếu sheet chứa bảng với thông số kỹ thuật quan trọng, hãy chuyển đổi sang định dạng Markdown table và đưa vào đây.
   
   Các loại bảng CẦN giữ nguyên:
   - Bảng field specifications (tên trường, kiểu dữ liệu, độ dài, bắt buộc/không)
   - Bảng validation rules
   - Bảng status/state transitions
   - Bảng data mapping (source → target)
   - Bảng API specifications
   - Bảng error codes
   - Bảng permission/role matrix
   
   Định dạng Markdown table:
   ```markdown
   | Tên trường | Kiểu dữ liệu | Độ dài | Bắt buộc | Mô tả |
   |------------|--------------|--------|----------|-------|
   | ma_yeu_cau | VARCHAR      | 50     | Có       | Mã yêu cầu theo format NK.YY.xxxx |
   ```

9. **Hình ảnh trong sheet** (QUAN TRỌNG - GIỮ NGUYÊN CHÍNH XÁC):
   Tìm TẤT CẢ các tham chiếu hình ảnh trong sheet (có dạng `![...](images/...)`).
   Liệt kê CHÍNH XÁC từng tham chiếu, KHÔNG thay đổi bất kỳ ký tự nào.
   
   Ví dụ nếu trong CSV có: `B5: ![5.2.1a_B5](images/5_2_1a_B5_image1.png)`
   Thì ghi:
   ```
   - Cell B5: `![5.2.1a_B5](images/5_2_1a_B5_image1.png)`
   ```
   
   KHÔNG tự đặt tên file. KHÔNG đoán. Copy CHÍNH XÁC từ CSV.
   Nếu không có hình ảnh, ghi "Không có hình ảnh."

Trình bày phân tích của bạn dưới dạng markdown ngôn ngữ tự nhiên (KHÔNG phải JSON). Ngắn gọn nhưng đầy đủ."""


# Thread-safe print lock
print_lock = Lock()


def safe_print(*args, **kwargs):
    """Thread-safe print function."""
    with print_lock:
        print(*args, **kwargs)


def load_csv_content(csv_path: str, max_rows: int = 500) -> tuple[str, int]:
    """
    Load CSV content as text, limited to max_rows.
    
    Returns:
        (content_text, total_row_count)
    """
    rows = []
    total_rows = 0
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                total_rows += 1
                if i < max_rows:
                    rows.append(','.join(row))
                    
        content = '\n'.join(rows)
        
        if total_rows > max_rows:
            content += f"\n\n... ({total_rows - max_rows} more rows truncated)"
            
        return content, total_rows
        
    except Exception as e:
        safe_print(f"Error reading {csv_path}: {e}")
        return "", 0


def extract_image_references(csv_content: str) -> list[dict]:
    """
    Extract all markdown image references from CSV content.
    
    Looks for patterns like: ![description](images/filename.png)
    Also captures the cell reference if available.
    
    Returns:
        List of dicts with 'cell' and 'markdown' keys
    """
    results = []
    
    # Pattern to match cell reference followed by image markdown
    # e.g., "B5: ![5.2.1a_B5](images/5_2_1a_B5_image1.png)"
    cell_pattern = r'([A-Z]+\d+):\s*(!\[[^\]]*\]\(images/[^)]+\))'
    
    for match in re.finditer(cell_pattern, csv_content):
        results.append({
            'cell': match.group(1),
            'markdown': match.group(2)
        })
    
    # Also catch any standalone image references without cell prefix
    # (in case format varies)
    standalone_pattern = r'(!\[[^\]]*\]\(images/[^)]+\))'
    all_images = set(re.findall(standalone_pattern, csv_content))
    found_images = {r['markdown'] for r in results}
    
    for img in all_images:
        if img not in found_images:
            results.append({
                'cell': 'Unknown',
                'markdown': img
            })
    
    return results


def summarize_sheet(client: Anthropic, sheet_name: str, csv_path: str, max_tokens: int = 2000) -> str:
    """
    Use Claude API to summarize a single sheet.
    
    Returns:
        Markdown summary text
    """
    content, row_count = load_csv_content(csv_path)
    
    if not content:
        return f"# {sheet_name}\n\n*Error: Could not read sheet content*"
    
    # Extract image references programmatically (backup guarantee)
    images = extract_image_references(content)
    
    prompt = SUMMARIZATION_PROMPT.format(
        sheet_name=sheet_name,
        content=content
    )
    
    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=max_tokens,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        summary = message.content[0].text
        
        # Programmatically append image references as GUARANTEED section
        # This ensures exact paths are preserved even if Claude's summary misses them
        if images:
            summary += "\n\n## 10. Danh sách hình ảnh (trích xuất tự động)\n\n"
            summary += "**QUAN TRỌNG: Sử dụng CHÍNH XÁC các đường dẫn dưới đây khi nhúng hình ảnh vào BRD.**\n\n"
            for img in images:
                summary += f"- Cell {img['cell']}: `{img['markdown']}`\n"
        
        # Add metadata footer
        summary += f"\n\n---\n*Source: {sheet_name}.csv | Rows: {row_count} | Images: {len(images)} | Generated by Claude Sonnet 4.5*\n"
        
        return summary
        
    except Exception as e:
        error_msg = f"# {sheet_name}\n\n*Error generating summary: {e}*"
        return error_msg


def get_sheet_name_from_filename(filename: str) -> str:
    """
    Extract sheet name from CSV filename.
    
    Examples:
        '5.1.1a.csv' -> '5.1.1a'
        'Status.csv' -> 'Status'
    """
    return os.path.splitext(os.path.basename(filename))[0]


def process_single_sheet(
    args: tuple
) -> dict:
    """
    Process a single sheet - worker function for parallel execution.
    
    Args:
        args: Tuple of (csv_path, output_dir, api_key, index, total)
        
    Returns:
        Dictionary with result info
    """
    csv_path, output_dir, api_key, index, total = args
    
    sheet_name = get_sheet_name_from_filename(csv_path)
    output_md = os.path.join(output_dir, f"{sheet_name}.md")
    
    # Create a new client for each thread (thread-safe)
    client = Anthropic(api_key=api_key)
    
    try:
        summary = summarize_sheet(client, sheet_name, csv_path)
        
        # Write summary to file
        with open(output_md, 'w', encoding='utf-8') as f:
            f.write(summary)
        
        file_size = os.path.getsize(output_md)
        safe_print(f"[{index}/{total}] ✓ '{sheet_name}' ({file_size:,} bytes)")
        
        return {
            'status': 'success',
            'sheet_name': sheet_name,
            'csv_path': csv_path,
            'md_path': output_md,
            'size': file_size
        }
        
    except Exception as e:
        safe_print(f"[{index}/{total}] ✗ '{sheet_name}' - {e}")
        return {
            'status': 'failed',
            'sheet_name': sheet_name,
            'error': str(e)
        }


def summarize_all_sheets(
    sheets_dir: str, 
    output_dir: str, 
    api_key: str = None,
    max_workers: int = 5
) -> dict:
    """
    Summarize all CSV sheets in the directory using parallel processing.
    
    Args:
        sheets_dir: Directory containing CSV files
        output_dir: Directory to save markdown summaries
        api_key: Optional API key (uses env var if not provided)
        max_workers: Maximum number of parallel API calls (default: 5)
        
    Returns:
        Dictionary with summarization results
    """
    # Get API key
    api_key = api_key or os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        raise ValueError("No API key provided")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all CSV files
    csv_files = sorted(glob.glob(os.path.join(sheets_dir, "*.csv")))
    
    if not csv_files:
        print(f"No CSV files found in {sheets_dir}")
        return {'success': [], 'failed': []}
    
    total = len(csv_files)
    print(f"Found {total} CSV files")
    print(f"Using {max_workers} parallel workers")
    print("-" * 60)
    
    results = {
        'success': [],
        'failed': [],
        'summaries': {}
    }
    
    # Prepare arguments for each worker
    work_items = [
        (csv_path, output_dir, api_key, i + 1, total)
        for i, csv_path in enumerate(csv_files)
    ]
    
    # Process in parallel
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_sheet = {
            executor.submit(process_single_sheet, item): item[0]
            for item in work_items
        }
        
        # Collect results as they complete
        for future in as_completed(future_to_sheet):
            result = future.result()
            
            if result['status'] == 'success':
                results['success'].append(result['sheet_name'])
                results['summaries'][result['sheet_name']] = {
                    'csv_path': result['csv_path'],
                    'md_path': result['md_path'],
                    'size': result['size']
                }
            else:
                results['failed'].append(result['sheet_name'])
    
    # Create index file
    create_index(results, output_dir)
    
    return results


def create_index(results: dict, output_dir: str):
    """Create an index markdown file listing all summaries."""
    index_path = os.path.join(output_dir, "_index.md")
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# Sheet Summaries Index\n\n")
        f.write(f"Total sheets: {len(results['success']) + len(results['failed'])}\n")
        f.write(f"- Successfully summarized: {len(results['success'])}\n")
        f.write(f"- Failed: {len(results['failed'])}\n\n")
        
        if results['success']:
            f.write("## Summaries\n\n")
            for sheet_name in sorted(results['success']):
                info = results['summaries'][sheet_name]
                f.write(f"- [{sheet_name}](./{sheet_name}.md) ({info['size']:,} bytes)\n")
        
        if results['failed']:
            f.write("\n## Failed\n\n")
            for sheet_name in results['failed']:
                f.write(f"- {sheet_name}\n")
    
    print(f"\n📄 Index created: {index_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Summarize Excel sheets using Claude API (parallel processing)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        'sheets_dir',
        help='Directory containing CSV sheet files'
    )
    
    parser.add_argument(
        'output_dir',
        help='Directory to save markdown summaries'
    )
    
    parser.add_argument(
        '--api-key',
        help='Anthropic API key (uses .env file or ANTHROPIC_API_KEY env var if not provided)'
    )
    
    parser.add_argument(
        '--workers', '-w',
        type=int,
        default=5,
        help='Number of parallel workers for API calls (default: 5)'
    )
    
    args = parser.parse_args()
    
    if not os.path.exists(args.sheets_dir):
        print(f"Error: Sheets directory not found: {args.sheets_dir}")
        sys.exit(1)
    
    # Check for API key
    api_key = args.api_key or os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: No API key provided.")
        print("Please either:")
        print("  1. Create a .env file with: ANTHROPIC_API_KEY=sk-ant-...")
        print("  2. Set ANTHROPIC_API_KEY environment variable")
        print("  3. Use --api-key argument")
        sys.exit(1)
    
    print(f"Sheets dir: {args.sheets_dir}")
    print(f"Output dir: {args.output_dir}")
    print(f"Model: Claude Sonnet 4.5")
    print(f"Workers: {args.workers}")
    print("=" * 60)
    
    results = summarize_all_sheets(
        args.sheets_dir, 
        args.output_dir, 
        api_key,
        max_workers=args.workers
    )
    
    print("=" * 60)
    print(f"✅ Summarization complete")
    print(f"   Success: {len(results['success'])} sheets")
    print(f"   Failed:  {len(results['failed'])} sheets")
    print(f"   Output:  {args.output_dir}/")
    
    if results['failed']:
        print(f"\n⚠️  Failed sheets: {results['failed']}")


if __name__ == "__main__":
    main()