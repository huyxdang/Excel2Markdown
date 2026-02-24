#!/usr/bin/env python3
"""
Synthesize sheet summaries into a final Business Requirements Document.

Two-pass hierarchical synthesis:
  Pass 1: Group summaries by module, synthesize each group in parallel (Haiku)
  Pass 2: Combine module sections into final BRD (Sonnet, with prompt caching)

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
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

SCRIPT_DIR = Path(__file__).parent

# Pricing per million tokens (USD)
HAIKU_INPUT_COST = 0.80
HAIKU_OUTPUT_COST = 4.0
SONNET_INPUT_COST = 3.0
SONNET_OUTPUT_COST = 15.0
# Prompt caching: writes cost 25% more, reads cost 90% less
SONNET_CACHE_WRITE_COST = SONNET_INPUT_COST * 1.25
SONNET_CACHE_READ_COST = SONNET_INPUT_COST * 0.10


def load_prompt(filepath: Path) -> str:
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def load_all_summaries(summaries_dir: str) -> dict:
    """Load all markdown summaries from directory."""
    summaries = {}
    md_files = sorted(glob.glob(os.path.join(summaries_dir, "*.md")))

    for md_path in md_files:
        if md_path.endswith("_index.md") or md_path.endswith("token_report.md"):
            continue
        sheet_name = Path(md_path).stem
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                summaries[sheet_name] = f.read()
        except Exception as e:
            print(f"Warning: Could not read {md_path}: {e}")

    return summaries


def strip_section_10(summary: str) -> str:
    """Remove Section 10 (auto-extracted image list) from a summary.

    Section 10 data is already parsed separately by extract_valid_image_filenames(),
    so including it in the API input wastes tokens.
    """
    return re.sub(
        r'\n## 10\. Danh sách hình ảnh.*',
        '',
        summary,
        flags=re.DOTALL,
    )


def group_sheets_by_module(summaries: dict) -> dict:
    """Group sheet summaries by their module prefix.

    Examples:
        '5.1.1a', '5.1.1b', '5.1.2a' → module '5.1'
        '5.2.1a', '5.2.3b'            → module '5.2'
        '0', '1', 'Status'            → module 'overview'

    Returns:
        Dict mapping module name to dict of {sheet_name: content}
    """
    groups = defaultdict(dict)

    for sheet_name, content in summaries.items():
        match = re.match(r'^(\d+\.\d+)', sheet_name)
        if match:
            module = match.group(1)
        else:
            module = 'overview'
        groups[module][sheet_name] = content

    return dict(groups)


def combine_summaries_for_module(summaries: dict) -> str:
    """Combine summaries within a module group into a single text block."""
    parts = []
    for sheet_name in sorted(summaries.keys()):
        stripped = strip_section_10(summaries[sheet_name])
        parts.append(f"### Sheet: {sheet_name}\n\n{stripped}\n")
        parts.append("-" * 40 + "\n")
    return "\n".join(parts)


def combine_module_sections(module_sections: dict) -> str:
    """Combine synthesized module sections into input for Pass 2."""
    parts = []
    for module_name in sorted(module_sections.keys()):
        parts.append(f"## Module: {module_name}\n\n{module_sections[module_name]}\n")
        parts.append("=" * 60 + "\n")
    return "\n".join(parts)


def synthesize_module(
    client: Anthropic,
    module_name: str,
    summaries: dict,
    module_prompt: str,
    max_tokens: int = 8000,
) -> tuple[str, dict]:
    """Pass 1: Synthesize a single module's sheets using Haiku.

    Returns:
        (section_markdown, usage_dict)
    """
    empty_usage = {'input_tokens': 0, 'output_tokens': 0}

    combined = combine_summaries_for_module(summaries)

    user_prompt = (
        f"Tổng hợp các bản tóm tắt sau thuộc module **{module_name}** "
        f"({len(summaries)} sheets).\n\n"
        f"**Hình ảnh:** CHỈ dùng token `<<IMAGE:filename>>` — copy chính xác từ Section 10.\n\n"
        f"---\n\n{combined}"
    )

    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=max_tokens,
            system=module_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
        usage = {
            'input_tokens': response.usage.input_tokens,
            'output_tokens': response.usage.output_tokens,
        }
        return response.content[0].text, usage
    except Exception as e:
        print(f"  Error synthesizing module {module_name}: {e}")
        # Fallback: return raw combined summaries
        return combined, empty_usage


def _process_module(
    client: Anthropic,
    module_name: str,
    summaries: dict,
    module_prompt: str,
    index: int,
    total: int,
) -> dict:
    """Worker function for parallel module synthesis."""
    section, usage = synthesize_module(client, module_name, summaries, module_prompt)
    in_tok = usage['input_tokens']
    out_tok = usage['output_tokens']
    print(f"  [{index}/{total}] Module '{module_name}' "
          f"({len(summaries)} sheets | {in_tok:,}+{out_tok:,} tokens)")
    return {
        'module': module_name,
        'section': section,
        'input_tokens': in_tok,
        'output_tokens': out_tok,
    }


def extract_valid_image_filenames(summaries: dict) -> set:
    """Extract valid image filenames from Section 10 of all summaries."""
    valid = set()
    section_pattern = r'## 10\. Danh sách hình ảnh.*?(?=\n## |\n---|\Z)'
    token_pattern = r'<<IMAGE:([^>]+)>>'

    for summary in summaries.values():
        match = re.search(section_pattern, summary, re.DOTALL)
        if match:
            for m in re.finditer(token_pattern, match.group(0)):
                valid.add(m.group(1))
    return valid


def convert_image_tokens(brd_content: str, valid_filenames: set):
    """Convert <<IMAGE:filename>> tokens to markdown image syntax."""
    stats = {'converted': 0, 'invalid_removed': 0, 'invalid_list': []}

    def replace_token(match):
        filename = match.group(1)
        if filename in valid_filenames:
            stats['converted'] += 1
            desc = filename.replace('_', '.').replace('.png', '').replace('.jpg', '')
            parts = desc.split('.')
            desc = f"{'.'.join(parts[:-2])} {parts[-2]}" if len(parts) > 2 else desc
            return f"![{desc}](images/{filename})"
        else:
            stats['invalid_removed'] += 1
            stats['invalid_list'].append(filename)
            return f"<!-- Invalid image token removed: {filename} -->"

    return re.sub(r'<<IMAGE:([^>]+)>>', replace_token, brd_content), stats


def append_missing_images(brd_content: str, missing: list) -> str:
    """Append missing images to BRD as appendix."""
    if not missing:
        return brd_content

    appendix = "\n\n---\n\n## Phụ lục: Hình ảnh bổ sung\n\n"
    for filename in missing:
        desc = filename.replace('_', ' ').replace('.png', '').replace('.jpg', '')
        appendix += f"![{desc}](images/{filename})\n\n"

    if "\n---\n\n*Generated by Claude" in brd_content:
        parts = brd_content.rsplit("\n---\n\n*Generated by Claude", 1)
        return parts[0] + appendix + "\n---\n\n*Generated by Claude" + parts[1]
    return brd_content + appendix


def synthesize_brd(
    client: Anthropic,
    summaries: dict,
    max_tokens: int = 32000,
    max_workers: int = 5,
) -> tuple[str, dict]:
    """Two-pass hierarchical synthesis.

    Pass 1: Parallel module synthesis with Haiku
    Pass 2: Final BRD synthesis with Sonnet (prompt caching)

    Returns:
        (brd_content, usage_dict) with combined token usage from both passes.
    """
    empty_usage = {
        'input_tokens': 0, 'output_tokens': 0,
        'cache_creation_input_tokens': 0, 'cache_read_input_tokens': 0,
        'pass1_input': 0, 'pass1_output': 0,
        'pass2_input': 0, 'pass2_output': 0,
    }

    if not summaries:
        return "# Error\n\nNo summaries provided for synthesis.", empty_usage

    # Extract valid image filenames BEFORE stripping Section 10
    valid_filenames = extract_valid_image_filenames(summaries)

    # ── Pass 1: Parallel module synthesis with Haiku ─────────────────────
    groups = group_sheets_by_module(summaries)
    module_prompt = load_prompt(SCRIPT_DIR / "prompts" / "module_synthesis_prompt.md")

    print(f"\n── Pass 1: Module synthesis ({len(groups)} modules, Haiku) ──")

    module_sections = {}
    pass1_usage = {'input_tokens': 0, 'output_tokens': 0}

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(
                _process_module, client, name, sheets, module_prompt, i + 1, len(groups)
            ): name
            for i, (name, sheets) in enumerate(sorted(groups.items()))
        }
        for future in as_completed(futures):
            result = future.result()
            module_sections[result['module']] = result['section']
            pass1_usage['input_tokens'] += result['input_tokens']
            pass1_usage['output_tokens'] += result['output_tokens']

    pass1_cost = (
        pass1_usage['input_tokens'] * HAIKU_INPUT_COST
        + pass1_usage['output_tokens'] * HAIKU_OUTPUT_COST
    ) / 1_000_000
    print(f"  Pass 1 total: {pass1_usage['input_tokens']:,} in + "
          f"{pass1_usage['output_tokens']:,} out = ${pass1_cost:.4f}")

    # ── Pass 2: Final BRD synthesis with Sonnet + prompt caching ─────────
    system_prompt = load_prompt(SCRIPT_DIR / "prompts" / "system_prompt.md")
    user_template = load_prompt(SCRIPT_DIR / "prompts" / "user_prompt.md")

    combined_modules = combine_module_sections(module_sections)
    user_prompt = user_template.format(
        num_modules=len(module_sections),
        num_sheets=len(summaries),
        summaries=combined_modules,
    )

    print(f"\n── Pass 2: Final BRD synthesis (Sonnet, {len(combined_modules):,} chars) ──")
    print("Generating BRD (streaming)...", end="", flush=True)

    try:
        brd_content = ""
        with client.messages.stream(
            model="claude-sonnet-4-6",
            max_tokens=max_tokens,
            system=[{
                "type": "text",
                "text": system_prompt,
                "cache_control": {"type": "ephemeral"},
            }],
            messages=[{"role": "user", "content": user_prompt}],
        ) as stream:
            for text in stream.text_stream:
                brd_content += text
                print(".", end="", flush=True)

            final_message = stream.get_final_message()
            pass2_usage = {
                'input_tokens': final_message.usage.input_tokens,
                'output_tokens': final_message.usage.output_tokens,
                'cache_creation_input_tokens': getattr(
                    final_message.usage, 'cache_creation_input_tokens', 0
                ) or 0,
                'cache_read_input_tokens': getattr(
                    final_message.usage, 'cache_read_input_tokens', 0
                ) or 0,
            }
        print(" Done!")

    except Exception as e:
        return f"# Error Generating BRD\n\n{e}", empty_usage

    # ── Post-processing ──────────────────────────────────────────────────
    brd_tokens = set(re.findall(r'<<IMAGE:([^>]+)>>', brd_content))
    missing = sorted(valid_filenames - brd_tokens)

    brd_content, stats = convert_image_tokens(brd_content, valid_filenames)
    print(f"Images: {stats['converted']} converted, "
          f"{stats['invalid_removed']} invalid, {len(missing)} missing")

    if missing:
        brd_content = append_missing_images(brd_content, missing)

    image_count = len(re.findall(r'!\[[^\]]*\]\(images/[^)]+\)', brd_content))
    brd_content += f"\n\n---\n\n*Generated from {len(summaries)} sheets | Images: {image_count}*\n"

    # ── Combine usage ────────────────────────────────────────────────────
    combined_usage = {
        'input_tokens': pass1_usage['input_tokens'] + pass2_usage['input_tokens'],
        'output_tokens': pass1_usage['output_tokens'] + pass2_usage['output_tokens'],
        'cache_creation_input_tokens': pass2_usage['cache_creation_input_tokens'],
        'cache_read_input_tokens': pass2_usage['cache_read_input_tokens'],
        'pass1_input': pass1_usage['input_tokens'],
        'pass1_output': pass1_usage['output_tokens'],
        'pass2_input': pass2_usage['input_tokens'],
        'pass2_output': pass2_usage['output_tokens'],
    }

    # Cost summary
    pass2_cost = (
        pass2_usage['input_tokens'] * SONNET_INPUT_COST
        + pass2_usage['output_tokens'] * SONNET_OUTPUT_COST
        + pass2_usage['cache_creation_input_tokens'] * SONNET_CACHE_WRITE_COST
        + pass2_usage['cache_read_input_tokens'] * SONNET_CACHE_READ_COST
    ) / 1_000_000
    total_cost = pass1_cost + pass2_cost

    cache_info = ""
    if pass2_usage['cache_read_input_tokens']:
        cache_info = f" (cache hit: {pass2_usage['cache_read_input_tokens']:,} tokens)"
    elif pass2_usage['cache_creation_input_tokens']:
        cache_info = f" (cache written: {pass2_usage['cache_creation_input_tokens']:,} tokens)"

    print(f"\n── Cost Summary ──")
    print(f"  Pass 1 (Haiku):  {pass1_usage['input_tokens']:,} in + "
          f"{pass1_usage['output_tokens']:,} out = ${pass1_cost:.4f}")
    print(f"  Pass 2 (Sonnet): {pass2_usage['input_tokens']:,} in + "
          f"{pass2_usage['output_tokens']:,} out = ${pass2_cost:.4f}{cache_info}")
    print(f"  Total: ${total_cost:.4f}")

    return brd_content, combined_usage


def _compute_synthesis_cost(usage: dict) -> float:
    """Compute total synthesis cost from combined usage dict."""
    pass1 = (
        usage.get('pass1_input', 0) * HAIKU_INPUT_COST
        + usage.get('pass1_output', 0) * HAIKU_OUTPUT_COST
    ) / 1_000_000
    pass2 = (
        usage.get('pass2_input', 0) * SONNET_INPUT_COST
        + usage.get('pass2_output', 0) * SONNET_OUTPUT_COST
        + usage.get('cache_creation_input_tokens', 0) * SONNET_CACHE_WRITE_COST
        + usage.get('cache_read_input_tokens', 0) * SONNET_CACHE_READ_COST
    ) / 1_000_000
    return pass1 + pass2


def main():
    parser = argparse.ArgumentParser(description="Synthesize sheet summaries into final BRD")
    parser.add_argument('summaries_dir', help='Directory with summary markdown files')
    parser.add_argument('output_file', help='Output BRD markdown file')
    parser.add_argument('--api-key', help='Anthropic API key')
    parser.add_argument('--max-tokens', type=int, default=32000, help='Max tokens (default: 32000)')
    parser.add_argument('--workers', '-w', type=int, default=5, help='Parallel workers for Pass 1')
    args = parser.parse_args()

    if not os.path.exists(args.summaries_dir):
        sys.exit(f"Error: Directory not found: {args.summaries_dir}")

    api_key = args.api_key or os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        sys.exit("Error: No API key. Set ANTHROPIC_API_KEY or use --api-key")

    summaries = load_all_summaries(args.summaries_dir)
    if not summaries:
        sys.exit("Error: No summaries found")

    print(f"Loaded {len(summaries)} summaries")

    client = Anthropic(api_key=api_key)
    brd_content, usage = synthesize_brd(
        client, summaries, args.max_tokens, args.workers
    )

    output_dir = os.path.dirname(args.output_file)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.write(brd_content)

    # Append synthesis cost to token_report.md if it exists
    report_path = os.path.join(args.summaries_dir, 'token_report.md')
    if os.path.exists(report_path) and (usage['pass1_input'] or usage['pass2_input']):
        synth_cost = _compute_synthesis_cost(usage)

        # Parse existing summarization total cost
        with open(report_path, 'r', encoding='utf-8') as f:
            existing = f.read()

        summ_cost = 0.0
        for line in existing.splitlines():
            if line.startswith('| **Total**'):
                parts = line.split('|')
                try:
                    summ_cost = float(parts[-2].strip().strip('*'))
                except (ValueError, IndexError):
                    pass

        grand_total = summ_cost + synth_cost

        with open(report_path, 'a', encoding='utf-8') as f:
            # Pass 1
            f.write("\n## Synthesis Pass 1 (claude-haiku-4.5)\n\n")
            f.write("| Step | Input Tokens | Output Tokens | Cost ($) |\n")
            f.write("|------|-------------|--------------|----------|\n")
            p1_cost = (usage['pass1_input'] * HAIKU_INPUT_COST
                       + usage['pass1_output'] * HAIKU_OUTPUT_COST) / 1_000_000
            f.write(f"| Module synthesis | {usage['pass1_input']:,} "
                    f"| {usage['pass1_output']:,} | {p1_cost:.4f} |\n")

            # Pass 2
            f.write("\n## Synthesis Pass 2 (claude-sonnet-4.6)\n\n")
            f.write("| Step | Input Tokens | Output Tokens | Cost ($) |\n")
            f.write("|------|-------------|--------------|----------|\n")
            p2_cost = synth_cost - p1_cost
            cache_note = ""
            if usage.get('cache_read_input_tokens'):
                cache_note = f" (cache hit: {usage['cache_read_input_tokens']:,})"
            f.write(f"| BRD synthesis{cache_note} | {usage['pass2_input']:,} "
                    f"| {usage['pass2_output']:,} | {p2_cost:.4f} |\n")

            f.write(f"\n## Grand Total: ${grand_total:.4f}\n")

        print(f"Updated: {report_path}")

    print(f"Done: {args.output_file} ({os.path.getsize(args.output_file):,} bytes)")


if __name__ == "__main__":
    main()
