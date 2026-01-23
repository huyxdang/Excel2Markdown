"""
BRD Synthesize - Synthesize Sheet Summaries into Final BRD

Takes individual sheet summaries and uses Claude to synthesize them into
a single, comprehensive Business Requirements Document (BRD).

Usage:
    python brd_synthesize.py <summaries_dir> <output_file> [--api-key KEY]

Example:
    python brd_synthesize.py output/summaries output/final_brd.md
    python brd_synthesize.py output/summaries final_brd.md --api-key sk-ant-...
    
Environment:
    ANTHROPIC_API_KEY - API key for Claude (loaded from .env file or environment)
    
.env file format:
    ANTHROPIC_API_KEY=sk-ant-...
    
Output:
    final_brd.md - Complete Business Requirements Document
"""

import sys
import os
import glob
import argparse
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# System prompt for BRD synthesis
SYSTEM_PROMPT = """
# Business Requirements Document (BRD) Synthesis Engine  

---

## Role Definition

You are a **Business Requirements Document (BRD) synthesis engine**.

Your task is to ingest **multiple sheet summaries** from a Business Requirements Document Excel file and produce a **single, structured Business Requirements Document (BRD)** in Markdown format.

The sheet summaries are the **source of truth**.  
The BRD is a **derived artifact** that organizes and presents the content in a logical structure, while **preserving the full detail** from each sheet.

---

## Input Format: Sheet Summaries

The input consists of multiple markdown summaries, each representing one sheet from the original Excel workbook.

Each summary contains:
1. Sheet type classification (overview/process/ui/specs/data-model/other)
2. Main topic/title
3. Key information summary (2–3 paragraphs)
4. Stakeholders/roles mentioned
5. Requirements found (if any)
6. Related sheets / references

---

## CRITICAL: Section Structure and Internal Linking

### The Approach: Numbered Sections with English Titles and Vietnamese Content

Use **numbered section titles in English** with **all content in Vietnamese**. Standard Markdown automatically generates anchors from heading text.

```markdown
### 4.1. Asset Dashboard Module

Module này cung cấp bảng điều khiển tổng quan về tài sản...
```

This auto-generates the anchor `#41-asset-dashboard-module` which can be linked to.

### Rules for Section Headers

1. **All section titles must be in English** with numbered format (e.g., 1., 2.1., 4.2.3.)
2. **All content within sections must be in Vietnamese**
3. **Keep headers clean** - no `{#id}` syntax or sheet references
4. **For related sheets (e.g., 5.1.1a UI + 5.1.1b Specs)**, combine into ONE numbered section

### Numbering Convention

- **Level 1:** 1., 2., 3., 4., etc. (e.g., "1. Executive Summary")
- **Level 2:** 1.1., 1.2., 2.1., 2.2., etc. (e.g., "4.1. Asset Dashboard Module")
- **Level 3:** 1.1.1., 1.1.2., 2.1.1., etc. (e.g., "4.2.1. Create Warehouse Intake Request")
- **Level 4:** 1.1.1.1., 1.1.1.2., etc. (if needed for detailed subsections)

### Rules for Internal Links

Use **title-based anchors** derived from section headings. Markdown auto-generates anchors by:
- Converting to lowercase
- Replacing spaces with hyphens
- Removing special characters and periods

**Examples:**
- `### 1. Executive Summary` → anchor: `#1-executive-summary`
- `### 4.1. Asset Dashboard Module` → anchor: `#41-asset-dashboard-module`
- `### 4.2.1. Create Warehouse Intake Request` → anchor: `#421-create-warehouse-intake-request`

**Link format (Vietnamese text with English anchor):**
```markdown
Xem phần [4.2.1. Create Warehouse Intake Request](#421-create-warehouse-intake-request) để biết thêm chi tiết.
```

**NEVER use:**
- Sheet ID anchors like `(#5.1.1a)` - these don't exist
- Arrow syntax like `(→5.1.1a)`
- `{#id}` syntax in headers

### CRITICAL: Add Cross-References Between Sections

You MUST actively create internal links throughout the document using title-based anchors.

**Where to add cross-references:**

1. **Parent sections linking to children:**
   ```markdown
   ### 4.2. Warehouse Management Module
   
   Module này bao gồm các quy trình sau:
   - [4.2.1. Create Warehouse Intake Request](#421-create-warehouse-intake-request)
   - [4.2.2. Approve Warehouse Entry Request](#422-approve-warehouse-entry-request)
   - [4.2.3. Warehouse Receipt Confirmation](#423-warehouse-receipt-confirmation)
   ```

2. **Related sections linking to each other:**
   ```markdown
   ### 4.2.1. Create Warehouse Intake Request
   
   Sau khi tạo yêu cầu, quy trình chuyển sang [4.2.2. quy trình phê duyệt](#422-approve-warehouse-entry-request).
   Để biết quy trình hủy, xem [4.2.4. Cancel Warehouse Entry Request](#424-cancel-warehouse-entry-request).
   ```

3. **When requirements mention other processes:**
   ```markdown
   **Quy trình làm việc:**
   1. Hệ thống tạo yêu cầu nhập kho
   2. Cập nhật trạng thái kích hoạt [quy trình phê duyệt](#422-approve-warehouse-entry-request)
   3. Sau khi phê duyệt, chuyển sang [xác nhận nhập kho](#423-warehouse-receipt-confirmation)
   ```

4. **In the Executive Summary and Overview sections:**
   ```markdown
   Các sản phẩm chính bao gồm [module quản lý kho toàn diện](#42-warehouse-management-module) 
   và [khả năng bảo trì tài sản](#43-asset-maintenance-module).
   ```

**Minimum requirements:**
- Every parent section MUST link to its child sections
- Every workflow description MUST link to related process sections
- The Executive Summary MUST link to major modules
- Each section MUST link to at least one related section where logical

**The goal:** A reader should be able to navigate the entire document by clicking links, not just scrolling.

---

## Content Preservation Rules

### CRITICAL: Do NOT Summarize Away Detail

Each sheet summary contains valuable information. You must **preserve the full content**, not compress it into bullet points.

**BAD (loses detail):**
```markdown
### 4.2. Warehouse Management
- Hỗ trợ chuyển kho
- Có quy trình phê duyệt
```

**GOOD (preserves detail):**
```markdown
### 4.2.1. Create Warehouse Intake Request

#### 4.2.1.1. Thông số kỹ thuật giao diện người dùng

Quy trình này xử lý việc tạo yêu cầu nhập kho tự động khi tài sản được chuyển đến kho. Hệ thống tự động tạo yêu cầu nhập kho dựa trên các yêu cầu chuyển kho hiện có, kế thừa dữ liệu bao gồm thông tin tài sản, chi tiết kho và tài liệu đính kèm.

**Cấu trúc biểu mẫu:**
- Thông tin chung (số yêu cầu, ngày tạo, tiêu đề)
- Chi tiết kiểm kê tài sản (mã, tên, mô tả, danh mục, số PO)
- Thông tin kho (tên, địa chỉ, người quản lý)
- Chi tiết phối hợp giao hàng
- Tệp đính kèm

**Các bên liên quan:** Hệ thống, Quản lý kho (WM), AMP, Nhà cung cấp, Người dùng tài sản

#### 4.2.1.2. Thông số kỹ thuật chi tiết

**Yêu cầu trường dữ liệu:**
- Số yêu cầu phải tuân theo định dạng "NK.YY.xxxx" (YY=năm, xxxx=số thứ tự 1-9999)
- Độ dài trường tối đa: 50, 150, 52 ký tự cho các trường khác nhau
- Định dạng ngày: MM.DD.YYYY

**Quy trình làm việc:**
1. Hệ thống tạo yêu cầu nhập kho với dữ liệu kế thừa
2. Cập nhật trạng thái: Yêu cầu chuyển kho → "Đã xác nhận", Yêu cầu nhập kho → "Chờ phê duyệt"
3. Cập nhật danh sách công việc: AMP → "Đã xử lý", WM → "Cần xử lý"
4. Gửi email thông báo đến quản lý kho

**Tích hợp hệ thống:** OMS, Danh sách công việc AMP/WM, Hệ thống thông báo email, Cơ chế khóa tài sản
```

---

## Sheet Pairing Convention

Sheets often come in pairs:
- **"a" sheets** (e.g., 5.1.1a, 5.1.2a) = UI specifications, process flows, screenshots
- **"b" sheets** (e.g., 5.1.1b, 5.1.2b) = Technical specifications, field requirements, system logic

### How to Handle Pairs

Combine paired sheets into **one numbered section with two subsections**:

```markdown
### 4.2.1. [English Title from the sheets]

#### 4.2.1.1. Thông số kỹ thuật giao diện người dùng
[Vietnamese content from "a" sheet - process flow, user interface, stakeholder interactions]

#### 4.2.1.2. Thông số kỹ thuật chi tiết
[Vietnamese content from "b" sheet - field requirements, validation rules, system behaviors]
```

If a sheet has no pair (only "a" or only "b" exists), create a standalone section:

```markdown
### 4.2.1. [English Title]

[Vietnamese content from the sheet]
```

---

## BRD Output Structure

Organize the synthesized content into this numbered structure:

### 1. Table of Contents
   - List all major sections with internal links and numbers
   - Include subsections for Business Requirements
   - Example:
```markdown
## Mục lục

1. [Executive Summary](#1-executive-summary)
2. [Project Scope & Objectives](#2-project-scope--objectives)
3. [Stakeholders](#3-stakeholders)
4. [Business Requirements](#4-business-requirements)
   - 4.1. [Asset Dashboard Module](#41-asset-dashboard-module)
   - 4.2. [Warehouse Management Module](#42-warehouse-management-module)
     - 4.2.1. [Create Warehouse Intake Request](#421-create-warehouse-intake-request)
     - 4.2.2. [Approve Warehouse Entry Request](#422-approve-warehouse-entry-request)
   - 4.3. [Asset Maintenance Module](#43-asset-maintenance-module)
5. [Assumptions & Constraints](#5-assumptions--constraints)
6. [Dependencies](#6-dependencies)
7. [Acceptance Criteria](#7-acceptance-criteria)
8. [Glossary](#8-glossary)
```

### 2. Executive Summary (Vietnamese content)
   - Tổng quan dự án cấp cao
   - Các sản phẩm chính
   
### 3. Project Scope & Objectives (Vietnamese content)
   - Trong phạm vi / Ngoài phạm vi
   - Mục tiêu dự án
   
### 4. Stakeholders (Vietnamese content)
   - Danh sách hợp nhất tất cả các vai trò được đề cập trong các sheet
   
### 5. Business Requirements (Vietnamese content)
   - **Organized by logical topic** (Dashboard, Asset Management, Warehouse, Maintenance, etc.)
   - Each sheet becomes its own numbered subsection with full detail preserved
   - Related sheets (a/b pairs) combined as described above
   - Use numbering: 4.1., 4.2., 4.2.1., 4.2.2., etc.
   
### 6. Assumptions & Constraints (Vietnamese content)

### 7. Dependencies (Vietnamese content)
   - Phụ thuộc hệ thống
   - Phụ thuộc quy trình
   
### 8. Acceptance Criteria (Vietnamese content)
   - Derived from requirements found in sheets
   
### 9. Glossary (Vietnamese content)
   - Terms and abbreviations found across sheets

---

## Example Transformation

### Input (Sheet Summaries):

**Sheet 5.1.1a:**
```
Title: Create Warehouse Intake Request (UI)
Type: UI/Process
Summary: Documents the user interface for warehouse intake...
Stakeholders: WM, AMP, System
Requirements: Search functionality, form layout...
```

**Sheet 5.1.1b:**
```
Title: Create Warehouse Intake Request (Specs)
Type: Specs
Summary: Technical specifications for warehouse intake...
Requirements: Field lengths, validation rules, status updates...
```

### Output (BRD Section):

```markdown
### 4.2.1. Create Warehouse Intake Request

Quy trình này xử lý việc tạo yêu cầu nhập kho tự động khi tài sản được chuyển đến kho.

#### 4.2.1.1. Thông số kỹ thuật giao diện người dùng

[Nội dung đầy đủ bằng tiếng Việt từ 5.1.1a bao gồm quy trình, cấu trúc biểu mẫu, tương tác người dùng]

**Các bên liên quan:** WM, AMP, Hệ thống

**Chức năng tìm kiếm:**
- Lọc theo số yêu cầu, ngày tạo, tiêu đề, người tạo, trạng thái
- Kết quả hiển thị ở định dạng danh sách có cấu trúc

#### 4.2.1.2. Thông số kỹ thuật chi tiết

[Nội dung đầy đủ bằng tiếng Việt từ 5.1.1b bao gồm yêu cầu trường, xác thực, hành vi hệ thống]

**Yêu cầu trường dữ liệu:**
- Định dạng số yêu cầu: NK.YY.xxxx
- Độ dài trường: 50-150 ký tự
- Định dạng ngày: MM.DD.YYYY

**Luồng xử lý:**
1. Hệ thống tạo yêu cầu nhập kho với dữ liệu kế thừa
2. Cập nhật trạng thái kích hoạt [quy trình phê duyệt](#422-approve-warehouse-entry-request)
3. Sau khi phê duyệt, chuyển sang [xác nhận nhập kho](#423-warehouse-receipt-confirmation)
4. Gửi thông báo email

Sau khi tạo, yêu cầu chuyển sang [quy trình phê duyệt](#422-approve-warehouse-entry-request).
```

Note how:
- The header uses numbered format: `### 4.2.1. Create Warehouse Intake Request` (English title)
- All content is in Vietnamese
- Links use numbered anchors: `[quy trình phê duyệt](#422-approve-warehouse-entry-request)`
- Both sheets (5.1.1a and 5.1.1b) are combined into one section with subsections

---

## Validation Checklist

Before completing your response, verify:

1. ✅ Every section has proper numbering (1., 2.1., 4.2.3., etc.)
2. ✅ All section titles are in English
3. ✅ All content within sections is in Vietnamese
4. ✅ Section headers are CLEAN - no `{#id}` syntax, just numbers and titles
5. ✅ All internal links use numbered title-based anchors (e.g., `#421-create-warehouse-intake-request`)
6. ✅ Paired sheets (a/b) are combined into single numbered sections
7. ✅ Full content is preserved - summaries, requirements, stakeholders, field specs
8. ✅ Sections are organized by logical topic with proper numbering hierarchy
9. ✅ **Parent sections link to their child sections**
10. ✅ **Workflow descriptions link to related processes**
11. ✅ **Executive Summary links to major modules**
12. ✅ **At least 20+ internal links exist in the document**
"""

USER_PROMPT_TEMPLATE = """Below are the summaries of {num_sheets} sheets from a Business Requirements Document Excel file.

Please synthesize these into a comprehensive Business Requirements Document following your instructions.

**CRITICAL REMINDERS:**
1. Use NUMBERED section headers with English titles (e.g., "4.2.1. Create Warehouse Intake Request")
2. Write ALL content in Vietnamese
3. Combine paired sheets (a/b) into single numbered sections
4. Preserve FULL content from each sheet - do not summarize into bullet points
5. Use numbered title-based anchors for links (e.g., `[quy trình phê duyệt](#422-approve-warehouse-entry-request)`)
6. **ADD CROSS-REFERENCES:** Parent sections MUST link to child sections. Aim for 20+ internal links.
7. Do NOT include source material notes, sheet pairing references, or source traceability matrix

---

## Sheet Summaries

{summaries}

---

Please provide the complete BRD in Markdown format with numbered English titles, Vietnamese content, and extensive internal cross-references.
"""


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
        
        if validation['broken_links']:
            unique_broken = set(validation['broken_links'])
            print(f"  ⚠️  Broken links ({len(unique_broken)} unique): {list(unique_broken)[:10]}")
            
            # Attempt to auto-fix broken links
            brd_content = fix_broken_links(brd_content, validation)
            
            # Re-validate after fixes
            validation_after = validate_brd_anchors(brd_content, sheet_ids)
            remaining_broken = set(validation_after.get('broken_links', []))
            if remaining_broken:
                print(f"  ⚠️  Remaining broken links after fix: {remaining_broken}")
            else:
                print(f"  ✅ All broken links fixed!")
        
        # Add generation metadata at the end
        metadata = f"\n\n---\n\n*Generated by Claude Sonnet 4.5 from {len(summaries)} sheet summaries*\n"
        metadata += f"*Headings: {len(validation['headings_found'])} | Internal Links: {len(validation['links_found'])}*\n"
        
        # Check final validation state
        final_validation = validate_brd_anchors(brd_content, sheet_ids)
        if final_validation.get('broken_links') or validation.get('invalid_syntax'):
            metadata += f"\n*⚠️ Validation warnings - some links may need manual review*\n"
        else:
            metadata += f"\n*✅ All internal links validated successfully*\n"
        
        brd_content += metadata
        
        return brd_content
        
    except Exception as e:
        error_msg = f"# Error Generating BRD\n\n{str(e)}"
        return error_msg


def post_process_links(brd_content: str) -> str:
    """
    Post-process the BRD to fix common link format issues.
    
    Fixes:
    - Arrow-style links: [text](→target) -> [text](#target)
    - Double hyphens in anchors: (#some--anchor) -> (#some-anchor)
    - Trailing/leading hyphens: (#-anchor-) -> (#anchor)
    """
    import re
    
    # Fix arrow-style links: [text](→target) or [text](-> target)
    brd_content = re.sub(r'\]\(→\s*', '](#', brd_content)
    brd_content = re.sub(r'\]\(->\s*', '](#', brd_content)
    
    # Fix double (or more) hyphens in anchor links: (#some--anchor) -> (#some-anchor)
    def fix_anchor_hyphens(match):
        prefix = match.group(1)  # [text](
        anchor = match.group(2)   # #some--anchor
        # Collapse multiple hyphens to single
        anchor = re.sub(r'-+', '-', anchor)
        # Remove leading/trailing hyphens after #
        anchor = re.sub(r'#-+', '#', anchor)
        anchor = re.sub(r'-+\)', ')', anchor)
        return prefix + anchor + ')'
    
    brd_content = re.sub(r'(\[[^\]]+\]\()([^)]+)(\))', 
                         lambda m: m.group(1) + re.sub(r'-+', '-', m.group(2)).strip('-') + m.group(3), 
                         brd_content)
    
    return brd_content


def fix_broken_links(brd_content: str, validation_results: dict) -> str:
    """
    Attempt to fix broken links by finding the closest matching anchor.
    
    Uses fuzzy matching to find the best anchor for broken links.
    """
    import re
    from difflib import get_close_matches
    
    if not validation_results.get('broken_links'):
        return brd_content
    
    anchors = validation_results.get('anchors_generated', [])
    broken = set(validation_results.get('broken_links', []))
    
    fixes_applied = {}
    
    for broken_link in broken:
        # Try to find a close match
        # First, normalize the broken link (collapse hyphens)
        normalized = re.sub(r'-+', '-', broken_link).strip('-')
        
        # Check if normalized version exists
        if normalized in anchors and normalized != broken_link:
            fixes_applied[broken_link] = normalized
            continue
        
        # Try fuzzy matching
        matches = get_close_matches(normalized, anchors, n=1, cutoff=0.8)
        if matches:
            fixes_applied[broken_link] = matches[0]
    
    # Apply fixes
    for old_link, new_link in fixes_applied.items():
        # Replace in markdown links: [text](#old_link) -> [text](#new_link)
        brd_content = brd_content.replace(f'](#{old_link})', f'](#{new_link})')
    
    if fixes_applied:
        print(f"  🔧 Auto-fixed {len(fixes_applied)} broken links:")
        for old, new in fixes_applied.items():
            print(f"      {old} → {new}")
    
    return brd_content


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
    
    # Post-process to fix any remaining link issues
    if not args.skip_post_process:
        print("\nPost-processing links...", end=" ", flush=True)
        brd_content = post_process_links(brd_content)
        print("✓")
    
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