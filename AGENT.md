# Excel2Markdown

Converts Excel BRD (Business Requirements Document) files into structured Markdown using a 3-step Claude API pipeline.

## Pipeline

```
Excel (.xlsx) → Step 1: extract → CSV + images → Step 2: summarize → per-sheet .md → Step 3: synthesize → final_brd.md
```

1. **Extract** (`extract_all_sheets.py` + `sheet_converter.py`) — Parallel extraction of all sheets to sparse CSV. Images extracted by parsing the .xlsx ZIP's internal XML directly (openpyxl can't reliably extract images). Hyperlinks preserved as markdown links.
2. **Summarize** (`summarize_sheets.py`) — Each CSV sent to Claude Haiku 4.5 with attached images (base64). Output: one `.md` summary per sheet.
3. **Synthesize** (`brd_synthesize.py`) — All summaries combined and sent to Claude Sonnet 4.6 (streaming). Output: `final_brd.md`.

## Key Conventions

- **Image token system**: Images flow as `<<IMAGE:filename>>` tokens through the pipeline. Only converted to `![](images/...)` markdown in the final synthesis step. This prevents hallucinated filenames.
- **Sheet pairing**: Sheets come in `a`/`b` pairs (e.g., `5.1.1a` = UI screenshots, `5.1.1b` = technical specs). The synthesis prompt merges each pair into one section.
- **Sparse CSV format**: Only non-empty cells are emitted (e.g., `A1: Header,C1: Value`) to minimize token usage.
- **Prompts are in Vietnamese**: The BRD domain is Vietnamese business documents. All prompts in `prompts/` are written in Vietnamese.

## File Structure

```
main.py                  — Pipeline orchestrator (runs steps 1-3 as subprocesses)
extract_all_sheets.py    — Step 1: discovers sheets, dispatches parallel extraction
sheet_converter.py       — Step 1 core: Excel → sparse CSV, hyperlinks
image_extractor.py       — Step 1 core: extract images from .xlsx via ZIP/XML parsing
summarize_sheets.py      — Step 2: parallel Claude API summarization
brd_synthesize.py        — Step 3: streaming synthesis into final BRD
prompts/
  summarization_prompt.md  — Per-sheet summarization prompt (Step 2)
  system_prompt.md         — BRD synthesis system prompt (Step 3)
  user_prompt.md           — BRD synthesis user prompt template (Step 3)
```

## Common Commands

```bash
# Full pipeline
python main.py data/input.xlsx -o output

# Skip re-extraction (reuse existing CSVs)
python main.py data/input.xlsx -o output --skip-extract

# Skip summarization too (reuse existing summaries)
python main.py data/input.xlsx -o output --skip-extract --skip-summarize

# Individual steps
python extract_all_sheets.py data/input.xlsx output
python summarize_sheets.py output/sheets output/summaries --images-dir output/images
python brd_synthesize.py output/summaries output/final_brd.md
```

## Models & Costs

| Step | Model | Pricing |
|------|-------|---------|
| Summarize | `claude-haiku-4-5-20251001` | $0.80/MTok in, $4/MTok out |
| Synthesize | `claude-sonnet-4-6` | $3/MTok in, $15/MTok out |

Cost details per run are written to `output/summaries/token_report.md`.

## Environment

- Python 3.9+
- `ANTHROPIC_API_KEY` in `.env` or passed via `--api-key`
- Dependencies: `openpyxl`, `anthropic`, `python-dotenv`