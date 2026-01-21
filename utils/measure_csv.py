"""
Measure CSV file size and statistics
"""

import os
import sys


def measure_csv(csv_path):
    """
    Measure CSV file size and statistics
    
    Args:
        csv_path: Path to CSV file
    
    Returns:
        Dictionary with size metrics
    """
    if not os.path.exists(csv_path):
        print(f"Error: File not found: {csv_path}")
        return None
    
    # File size in bytes
    size_bytes = os.path.getsize(csv_path)
    size_kb = size_bytes / 1024
    size_mb = size_kb / 1024
    
    # Line count
    line_count = 0
    with open(csv_path, 'r', encoding='utf-8') as f:
        line_count = sum(1 for _ in f)
    
    # Character count
    char_count = 0
    with open(csv_path, 'r', encoding='utf-8') as f:
        char_count = sum(len(line) for line in f)
    
    metrics = {
        'file': csv_path,
        'size_bytes': size_bytes,
        'size_kb': round(size_kb, 2),
        'size_mb': round(size_mb, 4),
        'lines': line_count,
        'chars': char_count,
    }
    
    return metrics


def print_metrics(metrics):
    """Pretty print metrics"""
    print(f"\nCSV File: {metrics['file']}")
    print(f"{'─' * 50}")
    print(f"File Size:     {metrics['size_bytes']:,} bytes")
    print(f"               {metrics['size_kb']} KB")
    print(f"               {metrics['size_mb']} MB")
    print(f"Lines:         {metrics['lines']:,}")
    print(f"Characters:    {metrics['chars']:,}")
    print(f"Avg Line Size: {round(metrics['size_bytes'] / metrics['lines'], 2)} bytes")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python measure_csv.py <csv_file>")
        print("\nExample:")
        print("  python measure_csv.py output.csv")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    metrics = measure_csv(csv_file)
    
    if metrics:
        print_metrics(metrics)
