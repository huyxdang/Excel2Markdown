# Excel2Markdown

Converts Excel BRD (Business Requirements Document) files into structured Markdown using a 3-step Claude API pipeline.

## Pipeline

```
Excel (.xlsx) → Step 1: extract → CSV + images → Step 2: summarize → per-sheet .md → Step 3: synthesize → final_brd.md
```

1. **Extract** (`extract_all_sheets.py` + `sheet_converter.py` + `image_extractor.py`) — Parallel extraction of all sheets to sparse CSV. Images extracted by parsing the .xlsx ZIP's internal XML directly (openpyxl can't reliably extract images). Hyperlinks preserved as markdown links.
2. **Summarize** (`summarize_sheets.py`) — Each CSV sent to Claude Haiku 4.5 with attached images (base64). Output: one `.md` summary per sheet.
3. **Synthesize** (`brd_synthesize.py`) — Two-pass hierarchical synthesis:
   - **Pass 1**: Group summaries by module (5.1.x, 5.2.x, etc.), synthesize each group in parallel with Haiku 4.5
   - **Pass 2**: Combine module sections into final BRD with Sonnet 4.6 (streaming, prompt caching)

## Key Conventions

- **Image token system**: Images flow as `<<IMAGE:filename>>` tokens through the pipeline. Only converted to `![](images/...)` markdown in the final post-processing step. This prevents hallucinated filenames.
- **Sheet pairing**: Sheets come in `a`/`b` pairs (e.g., `5.1.1a` = UI screenshots, `5.1.1b` = technical specs). The synthesis prompts merge each pair into one section.
- **Sparse CSV format**: Only non-empty cells are emitted (e.g., `A1: Header,C1: Value`) to minimize token usage.
- **Prompts are in Vietnamese**: The BRD domain is Vietnamese business documents. All prompts in `prompts/` are written in Vietnamese.
- **Section 10 stripping**: Auto-generated image lists (Section 10) are parsed for validation then stripped before synthesis to save tokens.

## File Structure

```
main.py                  — Pipeline orchestrator (runs steps 1-3 as subprocesses)
extract_all_sheets.py    — Step 1: discovers sheets, dispatches parallel extraction
sheet_converter.py       — Step 1 core: Excel → sparse CSV, hyperlinks
image_extractor.py       — Step 1 core: extract images from .xlsx via ZIP/XML parsing
summarize_sheets.py      — Step 2: parallel Claude API summarization
brd_synthesize.py        — Step 3: two-pass hierarchical synthesis
prompts/
  summarization_prompt.md      — Per-sheet summarization prompt (Step 2)
  module_synthesis_prompt.md   — Module-level synthesis prompt (Step 3, Pass 1)
  system_prompt.md             — BRD synthesis system prompt (Step 3, Pass 2)
  user_prompt.md               — BRD synthesis user prompt template (Step 3, Pass 2)
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
| Synthesize Pass 1 | `claude-haiku-4-5-20251001` | $0.80/MTok in, $4/MTok out |
| Synthesize Pass 2 | `claude-sonnet-4-6` | $3/MTok in, $15/MTok out |

Prompt caching on Pass 2 system prompt: cache writes +25%, cache reads -90%.

Cost details per run are written to `output/summaries/token_report.md`.

## Environment

- Python 3.9+
- `ANTHROPIC_API_KEY` in `.env` or passed via `--api-key`
- Dependencies: `openpyxl`, `anthropic`, `python-dotenv`
