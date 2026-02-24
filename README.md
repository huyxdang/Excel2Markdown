# Excel2Markdown

Chuyển đổi file Excel BRD (Business Requirements Document) phức tạp thành tài liệu Markdown có cấu trúc, sử dụng Claude API.

## Tổng quan

Pipeline gồm 3 bước tự động:

```
Excel (.xlsx) ──→ CSV + Hình ảnh ──→ Tóm tắt từng sheet ──→ BRD hoàn chỉnh (.md)
                  (Bước 1)            (Bước 2 - Claude)       (Bước 3 - Claude)
```

**Input:** File Excel (.xlsx) chứa nhiều sheet (BRD, đặc tả kỹ thuật, giao diện, v.v.)
**Output:** File Markdown duy nhất chứa toàn bộ nội dung đã được tổ chức lại

## Cấu trúc dự án

```
Excel2Markdown/
├── main.py                  # Điều phối pipeline 3 bước
├── extract_all_sheets.py    # Bước 1: Phát hiện và trích xuất tất cả sheet
├── sheet_converter.py       # Bước 1: Chuyển từng sheet → CSV + hyperlinks
├── image_extractor.py       # Bước 1: Trích xuất hình ảnh từ .xlsx (ZIP/XML)
├── summarize_sheets.py      # Bước 2: Tóm tắt từng sheet bằng Claude API
├── brd_synthesize.py        # Bước 3: Tổng hợp 2 lượt thành BRD hoàn chỉnh
├── prompts/
│   ├── summarization_prompt.md      # Prompt tóm tắt từng sheet
│   ├── module_synthesis_prompt.md   # Prompt tổng hợp module (Bước 3, Lượt 1)
│   ├── system_prompt.md             # System prompt tổng hợp BRD (Bước 3, Lượt 2)
│   └── user_prompt.md               # User prompt tổng hợp BRD (Bước 3, Lượt 2)
├── data/                    # Thư mục chứa file Excel đầu vào
├── output/                  # Thư mục đầu ra
│   ├── sheets/              # CSV của từng sheet
│   ├── images/              # Hình ảnh trích xuất từ Excel
│   ├── summaries/           # Markdown tóm tắt từng sheet
│   ├── manifest.txt         # Danh sách sheet đã trích xuất
│   └── final_brd.md         # BRD hoàn chỉnh
├── requirements.txt
└── .env                     # API key (không commit)
```

## Cài đặt

```bash
# Tạo môi trường ảo
python3 -m venv venv
source venv/bin/activate

# Cài đặt thư viện
pip install -r requirements.txt
```

Tạo file `.env` chứa API key:

```
ANTHROPIC_API_KEY=sk-ant-xxxxx
```

## Sử dụng

```bash
# Chạy toàn bộ pipeline
python main.py <file_excel> --output-dir <thư_mục_output>

# Ví dụ
python main.py data/BRD_input.xlsx --output-dir output
```

### Tham số

| Tham số | Mô tả | Mặc định |
|---------|--------|----------|
| `excel_file` | File Excel đầu vào (.xlsx) | Bắt buộc |
| `--output-dir`, `-o` | Thư mục đầu ra | `./output` |
| `--api-key` | Anthropic API key (thay cho .env) | — |
| `--max-tokens` | Giới hạn token cho bước tổng hợp | `32000` |
| `--workers`, `-w` | Số luồng xử lý song song | `10` |
| `--skip-extract` | Bỏ qua bước trích xuất (dùng CSV có sẵn) | — |
| `--skip-summarize` | Bỏ qua bước tóm tắt (dùng summary có sẵn) | — |
| `--skip-images` | Bỏ qua phân tích hình ảnh | — |
| `--clean` | Xóa thư mục output trước khi chạy | — |

### Chạy từng bước riêng lẻ

```bash
# Bước 1: Trích xuất sheet
python extract_all_sheets.py data/BRD_input.xlsx output

# Bước 2: Tóm tắt
python summarize_sheets.py output/sheets output/summaries --images-dir output/images

# Bước 3: Tổng hợp BRD
python brd_synthesize.py output/summaries output/final_brd.md
```

## Chi tiết Pipeline

### Bước 1 — Trích xuất (`extract_all_sheets.py` + `sheet_converter.py` + `image_extractor.py`)

**Dữ liệu ô:** Dùng `openpyxl` đọc từng sheet, xuất CSV với toạ độ ô (`A1: giá trị, B1: giá trị`). Hyperlink nội bộ được chuyển thành `[Text](→TênSheet)`, hyperlink ngoài giữ nguyên URL.

**Hình ảnh:** Vì `openpyxl` không trích xuất hình ảnh tin cậy, code trực tiếp parse cấu trúc XML bên trong file .xlsx (vốn là file ZIP):

```
.xlsx (ZIP)
├── xl/worksheets/_rels/sheet.xml.rels   → tìm file drawing
├── xl/drawings/drawing.xml              → vị trí neo hình ảnh (ô nào)
├── xl/drawings/_rels/drawing.xml.rels   → ánh xạ rId → đường dẫn ảnh
└── xl/media/image*.png                  → file ảnh gốc
```

Hình ảnh được lưu với tên `{sheet}_{ô}_{tên_gốc}.png` và tham chiếu dạng Markdown trong CSV.

**Đầu ra:** Mỗi sheet → 1 file CSV trong `output/sheets/`, hình ảnh trong `output/images/`.

### Bước 2 — Tóm tắt (`summarize_sheets.py`)

- Đọc từng file CSV, trích xuất tham chiếu hình ảnh
- Gửi nội dung CSV + hình ảnh (base64) đến **Claude Haiku 4.5** qua API
- Xử lý song song (mặc định 5-10 workers)
- Prompt yêu cầu phân loại sheet, tóm tắt nội dung, trích xuất yêu cầu, giữ nguyên bảng kỹ thuật

**Đầu ra:** Mỗi sheet → 1 file `.md` trong `output/summaries/`.

### Bước 3 — Tổng hợp (`brd_synthesize.py`)

Tổng hợp 2 lượt (hierarchical synthesis):

**Lượt 1 — Module synthesis (Haiku, song song):**
- Nhóm summary theo module (5.1.x, 5.2.x, v.v.)
- Tổng hợp từng nhóm bằng **Claude Haiku 4.5** qua ThreadPoolExecutor
- Ghép cặp sheet (a = giao diện, b = đặc tả) thành section duy nhất
- Section 10 (danh sách hình ảnh) được lọc trước khi gửi API để tiết kiệm token

**Lượt 2 — Final BRD synthesis (Sonnet, streaming):**
- Gộp các section module và gửi đến **Claude Sonnet 4.6** với prompt caching
- Tạo BRD hoàn chỉnh: Mục lục, Executive Summary, Business Requirements, v.v.
- Chuyển token `<<IMAGE:filename>>` thành cú pháp Markdown image
- Thêm hình ảnh thiếu vào phụ lục

**Đầu ra:** `output/final_brd.md`

## Model sử dụng

| Bước | Model | Mục đích |
|------|-------|----------|
| Tóm tắt | `claude-haiku-4-5-20251001` | Phân tích từng sheet + hình ảnh |
| Tổng hợp Lượt 1 | `claude-haiku-4-5-20251001` | Tổng hợp từng module |
| Tổng hợp Lượt 2 | `claude-sonnet-4-6` | Tổng hợp BRD hoàn chỉnh (prompt caching) |

## Chi phí & Hiệu suất

Kết quả thực nghiệm với file Excel **37 sheet**, 10 workers:

| Bước | Input Tokens | Output Tokens | Chi phí |
|------|-------------|--------------|---------|
| Tóm tắt (37 sheet) | 133,926 | 78,709 | $0.42 |
| Tổng hợp Lượt 1 — Module synthesis (Haiku) | 86,074 | 46,397 | $0.25 |
| Tổng hợp Lượt 2 — Final BRD (Sonnet) | 48,763 | 32,000 | $0.63 |
| **Tổng** | **268,763** | **157,106** | **$1.30** |

- **Thời gian:** ~9 phút (tuỳ số lượng sheet, hình ảnh, và số workers)
- **Đầu ra:** 75 KB BRD markdown, 15 hình ảnh
- **Pricing:**
  - Claude Haiku 4.5 — $0.80/MTok input, $4/MTok output
  - Claude Sonnet 4.6 — $3/MTok input, $15/MTok output
- Chi tiết từng sheet: xem `output/summaries/token_report.md` sau khi chạy pipeline

## Yêu cầu

- Python 3.9+
- Anthropic API key
- Thư viện: `openpyxl`, `anthropic`, `python-dotenv`
