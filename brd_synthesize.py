"""
Takes individual sheet summaries and uses Claude to synthesize them into
a single, comprehensive Business Requirements Document (BRD).

Usage:
    python brd_synthesize.py <summaries_dir> <output_file> [--api-key KEY]
    
Output:
    final_brd.md - Complete Business Requirements Document
"""

import sys
import os
import re
import glob
import argparse
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv
from pathlib import Path

def load_prompt(filepath: str) -> str:
    """Load prompt from markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

# Load environment variables from .env file
load_dotenv()


# System prompt for BRD synthesis

SCRIPT_DIR = Path(__file__).parent

SYSTEM_PROMPT = load_prompt(SCRIPT_DIR / "prompts" / "system_prompt.md")
USER_PROMPT_TEMPLATE = load_prompt(SCRIPT_DIR / "prompts" / "user_prompt.md")

def load_all_summaries(summaries_dir: str) -> dict:
    """
    Load all markdown summaries from the directory.
    
    Returns:
        Dictionary with sheet_name -> summary_content
    """
    summaries = {}
    
    # Find all .md files except _index.md
    md_files = sorted(glob.glob(os.path.join(summaries_dir, "*.md")))
    md_files = [f for f in md_files if not f.endswith("_index.md")]
    
    for md_path in md_files:
        sheet_name = os.path.splitext(os.path.basename(md_path))[0]
        
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()
                summaries[sheet_name] = content
        except Exception as e:
            print(f"Warning: Could not read {md_path}: {e}")
    
    return summaries


def combine_summaries(summaries: dict) -> str:
    """
    Combine all summaries into a single text block for the prompt.
    """
    combined = []
    
    for sheet_name in sorted(summaries.keys()):
        summary = summaries[sheet_name]
        combined.append(f"### Sheet ID: {sheet_name}\n\n{summary}\n")
        combined.append("-" * 80 + "\n")
    
    return "\n".join(combined)


def extract_sheet_ids(summaries: dict) -> list:
    """
    Extract all sheet IDs from summaries for validation.
    
    Returns:
        List of sheet IDs found in summaries
    """
    return list(summaries.keys())


def identify_sheet_pairs(sheet_ids: list) -> dict:
    """
    Identify paired sheets (a/b pairs).
    
    Returns:
        Dictionary mapping base_id -> [sheet_a, sheet_b] or [sheet_only]
    """
    pairs = {}
    
    for sheet_id in sheet_ids:
        # Check if ends with 'a' or 'b' and has a numeric prefix
        if sheet_id.endswith('a') or sheet_id.endswith('b'):
            base = sheet_id[:-1]
            if base not in pairs:
                pairs[base] = []
            pairs[base].append(sheet_id)
        else:
            # Standalone sheet
            if sheet_id not in pairs:
                pairs[sheet_id] = [sheet_id]
    
    return pairs


def validate_brd_anchors(brd_content: str, sheet_ids: list) -> dict:
    """
    Validate that the BRD has proper title-based anchors and links.
    
    Returns:
        Dictionary with validation results
    """
    import re
    
    results = {
        'headings_found': [],
        'anchors_generated': [],
        'links_found': [],
        'broken_links': [],
        'invalid_syntax': []
    }
    
    # Find all markdown headings (## or ### or ####)
    heading_pattern = r'^(#{2,4})\s+(.+?)(?:\s*\{#[^}]+\})*\s*$'
    for match in re.finditer(heading_pattern, brd_content, re.MULTILINE):
        heading_text = match.group(2).strip()
        # Remove any {#id} syntax if present (shouldn't be, but clean up)
        heading_text = re.sub(r'\s*\{#[^}]+\}', '', heading_text)
        results['headings_found'].append(heading_text)
        
        # Generate the anchor that Markdown would create
        anchor = heading_text.lower()
        anchor = re.sub(r'[^\w\s-]', '', anchor)  # Remove special chars except hyphens
        anchor = re.sub(r'\s+', '-', anchor)  # Replace spaces with hyphens
        anchor = re.sub(r'-+', '-', anchor)  # Collapse multiple hyphens
        anchor = anchor.strip('-')
        results['anchors_generated'].append(anchor)
    
    # Find all internal links: [text](#anchor)
    link_pattern = r'\[([^\]]+)\]\(#([^)]+)\)'
    links = re.findall(link_pattern, brd_content)
    results['links_found'] = [link[1] for link in links]
    
    # Find invalid {#id} syntax in headers (should not exist)
    invalid_pattern = r'^#{2,4}.*\{#[^}]+\}'
    results['invalid_syntax'] = re.findall(invalid_pattern, brd_content, re.MULTILINE)
    
    # Check for broken links (links without matching anchors)
    anchor_set = set(results['anchors_generated'])
    for link_target in results['links_found']:
        if link_target not in anchor_set:
            results['broken_links'].append(link_target)
    
    return results


def validate_image_paths(brd_content: str, summaries: dict) -> dict:
    """
    Validate that image tokens in BRD match those in Section 10 of summaries.
    
    Returns:
        Dictionary with validation results
    """
    import re
    
    # Extract all valid image filenames from Section 10 of all summaries
    valid_filenames = set()
    section_10_pattern = r'## 10\. Danh sách hình ảnh.*?(?=\n## |\n---|\Z)'
    token_pattern = r'<<IMAGE:([^>]+)>>'
    
    for sheet_name, summary in summaries.items():
        # Find Section 10
        section_match = re.search(section_10_pattern, summary, re.DOTALL)
        if section_match:
            section_content = section_match.group(0)
            # Extract filenames from tokens in Section 10
            for match in re.finditer(token_pattern, section_content):
                valid_filenames.add(match.group(1))
    
    # Extract all image tokens used in BRD
    brd_tokens = re.findall(token_pattern, brd_content)
    
    # Also check for any markdown image syntax (should not exist)
    markdown_images = re.findall(r'!\[[^\]]*\]\(images/([^)]+)\)', brd_content)
    
    # Check for invalid tokens
    invalid_tokens = []
    for token in brd_tokens:
        if token not in valid_filenames:
            invalid_tokens.append(token)
    
    return {
        'valid_filenames': list(valid_filenames),
        'brd_tokens': brd_tokens,
        'invalid_tokens': invalid_tokens,
        'missing_images': list(valid_filenames - set(brd_tokens)),
        'markdown_images_found': markdown_images  # Should be empty
    }


def convert_image_tokens(brd_content: str, valid_filenames: set) -> tuple:
    """
    Convert <<IMAGE:filename>> tokens to proper markdown image syntax.
    
    Also handles:
    - Invalid tokens (not in valid_filenames) are removed with a warning comment
    - Missing images are appended to an appendix
    
    Returns:
        Tuple of (converted_content, conversion_stats)
    """
    import re
    
    stats = {
        'converted': 0,
        'invalid_removed': 0,
        'invalid_list': []
    }
    
    def replace_token(match):
        filename = match.group(1)
        if filename in valid_filenames:
            stats['converted'] += 1
            # Generate a description from filename
            # 5_2_1a_B5_image1.png -> "5.2.1a B5"
            desc = filename.replace('_', '.').replace('.png', '').replace('.jpg', '').replace('.jpeg', '')
            # Clean up: 5.2.1a.B5.image1 -> 5.2.1a B5
            parts = desc.split('.')
            if len(parts) >= 2:
                desc = f"{'.'.join(parts[:-2])} {parts[-2]}" if len(parts) > 2 else desc
            return f"![{desc}](images/{filename})"
        else:
            stats['invalid_removed'] += 1
            stats['invalid_list'].append(filename)
            return f"<!-- Invalid image token removed: {filename} -->"
    
    converted = re.sub(r'<<IMAGE:([^>]+)>>', replace_token, brd_content)
    
    return converted, stats


def append_missing_images(brd_content: str, missing_images: list) -> str:
    """
    Append missing images to the end of the BRD in an appendix section.
    """
    if not missing_images:
        return brd_content
    
    appendix = "\n\n---\n\n## Phụ lục: Hình ảnh bổ sung\n\n"
    appendix += "Các hình ảnh sau được trích xuất từ tài liệu gốc nhưng chưa được đặt vào nội dung chính:\n\n"
    
    for filename in missing_images:
        desc = filename.replace('_', ' ').replace('.png', '').replace('.jpg', '')
        appendix += f"![{desc}](images/{filename})\n\n"
    
    # Insert before the final metadata section if it exists
    if "\n---\n\n*Generated by Claude" in brd_content:
        parts = brd_content.rsplit("\n---\n\n*Generated by Claude", 1)
        return parts[0] + appendix + "\n---\n\n*Generated by Claude" + parts[1]
    else:
        return brd_content + appendix


def synthesize_brd(client: Anthropic, summaries: dict, max_tokens: int = 32000) -> str:
    """
    Use Claude API to synthesize all summaries into a final BRD.
    Uses streaming to handle long-running requests.
    
    Returns:
        Complete BRD in Markdown format
    """
    if not summaries:
        return "# Error\n\nNo summaries provided for synthesis."
    
    # Combine all summaries
    summaries_text = combine_summaries(summaries)
    sheet_ids = extract_sheet_ids(summaries)
    pairs = identify_sheet_pairs(sheet_ids)
    
    # Create user prompt
    user_prompt = USER_PROMPT_TEMPLATE.format(
        num_sheets=len(summaries),
        summaries=summaries_text
    )
    
    print(f"Synthesizing {len(summaries)} sheet summaries into BRD...")
    print(f"Sheet IDs: {sheet_ids}")
    print(f"Identified pairs: {pairs}")
    print(f"Input size: {len(summaries_text):,} characters")
    print(f"Using Claude Sonnet 4.5 with max_tokens={max_tokens}")
    print("-" * 60)
    print("\nGenerating BRD (streaming)...", flush=True)
    
    try:
        # Use streaming for long-running requests
        brd_content = ""
        
        with client.messages.stream(
            model="claude-sonnet-4-20250514",
            max_tokens=max_tokens,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        ) as stream:
            for text in stream.text_stream:
                brd_content += text
                # Print progress indicator
                print(".", end="", flush=True)
        
        print(" Done!")
        
        # Validate anchors and links
        print("\nValidating internal links...")
        validation = validate_brd_anchors(brd_content, sheet_ids)
        
        print(f"  Headings found: {len(validation['headings_found'])}")
        print(f"  Auto-generated anchors: {len(validation['anchors_generated'])}")
        print(f"  Internal links found: {len(validation['links_found'])}")
        
        if validation['invalid_syntax']:
            print(f"  ⚠️  Invalid {{#id}} syntax found in {len(validation['invalid_syntax'])} headers")
        
        # Validate image tokens
        print("\nValidating image tokens...")
        image_validation = validate_image_paths(brd_content, summaries)
        print(f"  Valid filenames from Section 10: {len(image_validation['valid_filenames'])}")
        print(f"  Image tokens in BRD: {len(image_validation['brd_tokens'])}")
        
        if image_validation['markdown_images_found']:
            print(f"  ⚠️  Found markdown image syntax (should use tokens): {image_validation['markdown_images_found'][:5]}")
        
        if image_validation['invalid_tokens']:
            print(f"  ⚠️  Invalid tokens (will be removed): {image_validation['invalid_tokens']}")
        
        if image_validation['missing_images']:
            print(f"  ⚠️  Missing images (will be added to appendix): {image_validation['missing_images'][:10]}")
        
        # Convert image tokens to markdown
        print("\nConverting image tokens to markdown...")
        valid_filenames_set = set(image_validation['valid_filenames'])
        brd_content, conversion_stats = convert_image_tokens(brd_content, valid_filenames_set)
        print(f"  ✅ Converted {conversion_stats['converted']} tokens")
        if conversion_stats['invalid_removed'] > 0:
            print(f"  ⚠️  Removed {conversion_stats['invalid_removed']} invalid tokens: {conversion_stats['invalid_list']}")
        
        # Append missing images
        if image_validation['missing_images']:
            print(f"\nAppending {len(image_validation['missing_images'])} missing images to appendix...")
            brd_content = append_missing_images(brd_content, image_validation['missing_images'])
            print(f"  ✅ Added appendix with missing images")
        
        # Final image count
        final_image_count = len(re.findall(r'!\[[^\]]*\]\(images/[^)]+\)', brd_content))
        print(f"\n📊 Final image count: {final_image_count}")
        
        # Add generation metadata at the end
        metadata = f"\n\n---\n\n*Generated by Claude Sonnet 4.5 from {len(summaries)} sheet summaries*\n"
        metadata += f"*Headings: {len(validation['headings_found'])} | Internal Links: {len(validation['links_found'])} | Images: {final_image_count}*\n"
        
        # Check final validation state
        final_validation = validate_brd_anchors(brd_content, sheet_ids)
        if final_validation.get('broken_links') or validation.get('invalid_syntax'):
            metadata += f"\n*⚠️ Link validation warnings - some links may need manual review*\n"
        else:
            metadata += f"\n*✅ All internal links validated successfully*\n"
        
        if conversion_stats['invalid_removed'] > 0:
            metadata += f"*⚠️ {conversion_stats['invalid_removed']} invalid image tokens were removed*\n"
        else:
            metadata += f"*✅ All image tokens converted successfully*\n"
        
        brd_content += metadata
        
        return brd_content
        
    except Exception as e:
        error_msg = f"# Error Generating BRD\n\n{str(e)}"
        return error_msg

def main():
    parser = argparse.ArgumentParser(
        description="Synthesize sheet summaries into a final BRD",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        'summaries_dir',
        help='Directory containing sheet summary markdown files'
    )
    
    parser.add_argument(
        'output_file',
        help='Output path for final BRD markdown file'
    )
    
    parser.add_argument(
        '--api-key',
        help='Anthropic API key (uses .env file or ANTHROPIC_API_KEY env var if not provided)'
    )
    
    parser.add_argument(
        '--max-tokens',
        type=int,
        default=32000,
        help='Maximum tokens for Claude response (default: 32000)'
    )
    
    parser.add_argument(
        '--skip-post-process',
        action='store_true',
        help='Skip post-processing link fixes'
    )
    
    args = parser.parse_args()
    
    if not os.path.exists(args.summaries_dir):
        print(f"Error: Summaries directory not found: {args.summaries_dir}")
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
    
    print(f"Summaries dir: {args.summaries_dir}")
    print(f"Output file: {args.output_file}")
    print(f"Model: Claude Sonnet 4.5")
    print("=" * 60)
    
    # Initialize Anthropic client
    client = Anthropic(api_key=api_key)
    
    # Load all summaries
    print("Loading summaries...", end=" ", flush=True)
    summaries = load_all_summaries(args.summaries_dir)
    print(f"✓ ({len(summaries)} sheets)")
    
    if not summaries:
        print("Error: No summaries found in directory")
        sys.exit(1)
    
    # Synthesize BRD
    brd_content = synthesize_brd(client, summaries, args.max_tokens)
    
    # Write output
    print("Writing BRD...", end=" ", flush=True)
    output_dir = os.path.dirname(args.output_file)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.write(brd_content)
    
    file_size = os.path.getsize(args.output_file)
    print(f"✓ ({file_size:,} bytes)")
    
    print("=" * 60)
    print(f"✅ BRD synthesis complete")
    print(f"   Output: {args.output_file}")
    print(f"   Size: {file_size:,} bytes")


if __name__ == "__main__":
    main()