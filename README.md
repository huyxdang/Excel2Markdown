# Excel-to-LLM Pipeline

This system converts Excel workbooks into structured CSV files optimized for large language models. It solves the problem of extracting tabular and text data from complex, multi-sheet Excel files in a deterministic, inspectable format. 

## High-Level Workflow

1. **Excel File** → Input workbook with multiple sheets, tables, text, and images.
2. **Converter** → `excel_converter.py` scans all sheets and cells, extracts values row-major, saves images separately.
3. **CSV Output** → `output.csv` contains all cell values indexed by coordinates (A1, B2, etc.).

[Optional]
4. **LLM Processing** → You paste the CSV and `prompt.md` into an LLM (Claude, GPT, etc.) which interprets the structured data.
5. **Markdown Output** → The LLM generates Markdown formatted for documentation systems.
6. **Rendering** → Paste the Markdown into a renderer (Markdown Live Preview, Confluence, etc.) for final output.

## Inputs and Outputs

### Input

**Excel Workbook (.xlsx)**
- Multiple sheets (numbered, named, or both)
- Tables, text, and structured data
- Embedded images (extracted separately)

### Output

**CSV File: `output.csv`**

Why CSV? It's:
- Deterministic (no rendering ambiguity)
- Human-readable (easy to inspect and debug)
- Efficient for LLM processing (lower token cost, clearer structure)

## How to Run

### Prerequisites

1. Ensure Python 3.9+ is installed.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Converter

**Usage:**
```bash
python excel_converter.py <excel_file> [output_csv]
```

**Example:**
```bash
python excel_converter.py BRD_input.xlsx output.csv
```

**Output Files:**
- `output.csv` — Combined CSV with all sheets
- `images/` — Directory containing all extracted images
  - Filenames follow the pattern: `<sheet_name>_<cell_coordinate>_image<N>.png`

**Example Output Directory:**
```
images/
  5_1_1a_B6_image2.png
  5_2_1a_C10_image3.png
  5_4_2b_D15_image1.png
```

### Optional Flags

**List all sheets without processing:**
```bash
python excel_converter.py BRD_input.xlsx --list
```

**Process only selected sheets:**
```bash
python excel_converter.py BRD_input.xlsx output.csv --sheets "5.1.1a" "5.1.2b" "Status"
```

## CSV Structure

The CSV file is organized by sheet, with cell coordinates and values listed row-major (left-to-right, top-to-bottom).

**Format:**

```
================================================================================
Sheet: 5.1.1a
================================================================================
A1: Project Title,B1: Q1 2026,C1: Status
A2: Feature A,B2: 50%,C2: In Progress
A3: Feature B,B3: 75%,C3: Complete
A4: ,B4: ![image](images/5_1_1a_B4_image1.png),C4: Review

================================================================================
Sheet: 5.1.2b
================================================================================
A1: Task,B1: Owner,C1: Due Date
A2: Design Phase,B2: Alice,C2: 2026-02-15
...
```

**Key Details:**
- One section per sheet (marked with `================...`)
- Cells listed row-major order (row by row, left-to-right within each row)
- Empty cells are omitted (not listed)
- Cell coordinates follow Excel notation: `A1`, `B2`, `C10`, etc.
- Image references use Markdown syntax: `![image](images/<filename>.png)`


## Testing and Performance

Run benchmarks to measure conversion speed and output quality:

```bash
python measure.py BRD_input.xlsx output.csv
```

Benchmarks are stored in the `benchmark/` directory for tracking performance over time.


## Images Handling

**Hard Requirement:** Images are not embedded in the CSV. Instead:

1. **CSV contains file paths only**, using Markdown syntax:
   ```
   ![image](images/5_1_1a_B4_image1.png)
   ```

2. **Images are extracted to the `images/` directory** during converter execution.

3. **Filenames must match exactly** between the CSV reference and the actual image file. If a CSV references `images/5_1_1a_B4_image1.png`, the file must exist at `images/5_1_1a_B4_image1.png`.

4. **When passing the CSV to the LLM**, the LLM sees only the file paths. It does not need direct access to image files (the LLM uses the path as metadata, not the image content).

5. **When rendering the final Markdown**, the renderer (Confluence, Markdown viewer, etc.) must have access to the `images/` directory to resolve paths.
