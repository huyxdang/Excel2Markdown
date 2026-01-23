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
# Công cụ Tổng hợp Tài liệu Yêu cầu Nghiệp vụ (BRD)

---

## Định nghĩa Vai trò

Bạn là một **công cụ tổng hợp Tài liệu Yêu cầu Nghiệp vụ (BRD)**.

Nhiệm vụ của bạn là tiếp nhận **nhiều bản tóm tắt sheet** từ file Excel Tài liệu Yêu cầu Nghiệp vụ và tạo ra **một Tài liệu Yêu cầu Nghiệp vụ (BRD) duy nhất, có cấu trúc** ở định dạng Markdown.

Các bản tóm tắt sheet là **nguồn thông tin chính xác**.  
BRD là một **sản phẩm phái sinh** tổ chức và trình bày nội dung theo cấu trúc logic, đồng thời **bảo toàn đầy đủ chi tiết** từ mỗi sheet.

---

## Định dạng Đầu vào: Bản tóm tắt Sheet

Đầu vào bao gồm nhiều bản tóm tắt markdown, mỗi bản đại diện cho một sheet từ workbook Excel gốc.

Mỗi bản tóm tắt chứa:
1. Phân loại loại sheet (tổng-quan/quy-trình/giao-diện/đặc-tả/mô-hình-dữ-liệu/khác)
2. Chủ đề/tiêu đề chính
3. Tóm tắt thông tin chính (2–3 đoạn)
4. Các bên liên quan/vai trò được đề cập
5. Các yêu cầu tìm thấy (nếu có)
6. Các sheet liên quan / tham chiếu

---

## QUAN TRỌNG: Cấu trúc Section và Liên kết Nội bộ

### Phương pháp: Section được Đánh số với Tiêu đề tiếng Anh và Nội dung tiếng Việt

Sử dụng **tiêu đề section được đánh số bằng tiếng Anh** với **toàn bộ nội dung bằng tiếng Việt**. Markdown chuẩn tự động tạo anchor từ văn bản heading.

```markdown
### 4.1. Asset Dashboard Module

Module này cung cấp bảng điều khiển tổng quan về tài sản...
```

Điều này tự động tạo anchor `#41-asset-dashboard-module` có thể liên kết đến.

### Quy tắc cho Header Section

1. **Tất cả tiêu đề section phải bằng tiếng Anh** với định dạng đánh số (ví dụ: 1., 2.1., 4.2.3.)
2. **Tất cả nội dung trong section phải bằng tiếng Việt**
3. **Giữ header sạch sẽ** - không có cú pháp `{#id}` hoặc tham chiếu sheet
4. **Đối với các sheet liên quan (ví dụ: 5.1.1a UI + 5.1.1b Specs)**, kết hợp thành MỘT section được đánh số

### Quy ước Đánh số

- **Cấp 1:** 1., 2., 3., 4., v.v. (ví dụ: "1. Executive Summary")
- **Cấp 2:** 1.1., 1.2., 2.1., 2.2., v.v. (ví dụ: "4.1. Asset Dashboard Module")
- **Cấp 3:** 1.1.1., 1.1.2., 2.1.1., v.v. (ví dụ: "4.2.1. Create Warehouse Intake Request")
- **Cấp 4:** 1.1.1.1., 1.1.1.2., v.v. (nếu cần cho các tiểu mục chi tiết)

### Quy tắc cho Liên kết Nội bộ

Sử dụng **anchor dựa trên tiêu đề** được suy ra từ heading section. Markdown tự động tạo anchor bằng cách:
- Chuyển thành chữ thường
- Thay khoảng trắng bằng dấu gạch ngang
- Loại bỏ ký tự đặc biệt và dấu chấm

**Ví dụ:**
- `### 1. Executive Summary` → anchor: `#1-executive-summary`
- `### 4.1. Asset Dashboard Module` → anchor: `#41-asset-dashboard-module`
- `### 4.2.1. Create Warehouse Intake Request` → anchor: `#421-create-warehouse-intake-request`

**Định dạng liên kết (văn bản tiếng Việt với anchor tiếng Anh):**
```markdown
Xem phần [4.2.1. Create Warehouse Intake Request](#421-create-warehouse-intake-request) để biết thêm chi tiết.
```

**KHÔNG BAO GIỜ sử dụng:**
- Anchor ID sheet như `(#5.1.1a)` - những anchor này không tồn tại
- Cú pháp mũi tên như `(→5.1.1a)`
- Cú pháp `{#id}` trong header

### QUAN TRỌNG: Thêm Tham chiếu Chéo Giữa các Section

Bạn PHẢI chủ động tạo liên kết nội bộ xuyên suốt tài liệu sử dụng anchor dựa trên tiêu đề.

**Nơi cần thêm tham chiếu chéo:**

1. **Section cha liên kết đến con:**
   ```markdown
   ### 4.2. Warehouse Management Module
   
   Module này bao gồm các quy trình sau:
   - [4.2.1. Create Warehouse Intake Request](#421-create-warehouse-intake-request)
   - [4.2.2. Approve Warehouse Entry Request](#422-approve-warehouse-entry-request)
   - [4.2.3. Warehouse Receipt Confirmation](#423-warehouse-receipt-confirmation)
   ```

2. **Các section liên quan liên kết với nhau:**
   ```markdown
   ### 4.2.1. Create Warehouse Intake Request
   
   Sau khi tạo yêu cầu, quy trình chuyển sang [4.2.2. quy trình phê duyệt](#422-approve-warehouse-entry-request).
   Để biết quy trình hủy, xem [4.2.4. Cancel Warehouse Entry Request](#424-cancel-warehouse-entry-request).
   ```

3. **Khi yêu cầu đề cập đến các quy trình khác:**
   ```markdown
   **Quy trình làm việc:**
   1. Hệ thống tạo yêu cầu nhập kho
   2. Cập nhật trạng thái kích hoạt [quy trình phê duyệt](#422-approve-warehouse-entry-request)
   3. Sau khi phê duyệt, chuyển sang [xác nhận nhập kho](#423-warehouse-receipt-confirmation)
   ```

4. **Trong phần Executive Summary và Overview:**
   ```markdown
   Các sản phẩm chính bao gồm [module quản lý kho toàn diện](#42-warehouse-management-module) 
   và [khả năng bảo trì tài sản](#43-asset-maintenance-module).
   ```

**Yêu cầu tối thiểu:**
- Mọi section cha PHẢI liên kết đến các section con của nó
- Mọi mô tả quy trình làm việc PHẢI liên kết đến các section quy trình liên quan
- Executive Summary PHẢI liên kết đến các module chính
- Mỗi section PHẢI liên kết đến ít nhất một section liên quan khi hợp lý

**Mục tiêu:** Người đọc có thể điều hướng toàn bộ tài liệu bằng cách nhấp liên kết, không chỉ cuộn trang.

---

## Quy tắc Bảo toàn Nội dung

### QUAN TRỌNG: KHÔNG Tóm tắt Mất Chi tiết

Mỗi bản tóm tắt sheet chứa thông tin có giá trị. Bạn phải **bảo toàn toàn bộ nội dung**, không nén thành các bullet point.

**XẤU (mất chi tiết):**
```markdown
### 4.2. Warehouse Management
- Hỗ trợ chuyển kho
- Có quy trình phê duyệt
```

**TỐT (bảo toàn chi tiết):**
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

## QUAN TRỌNG: Nhúng Hình ảnh

Các bản tóm tắt sheet thường tham chiếu đến hình ảnh (ảnh chụp màn hình UI, sơ đồ quy trình, mockup). Những hình ảnh này PHẢI được nhúng vào BRD cuối cùng.

### Định dạng Đường dẫn Hình ảnh

Hình ảnh được lưu trong thư mục con `images/`. Khi bản tóm tắt đề cập đến hình ảnh như:
- `images/5_1_1a_B5_image1.png`
- `5_1_1a_B5_image1.png`

Nhúng nó sử dụng định dạng này:
```markdown
![Mô tả giao diện](images/5_1_1a_B5_image1.png)
```

### Vị trí Đặt Hình ảnh

1. **Đối với sheet UI/Quy trình (sheet "a")**: Đặt hình ảnh ở ĐẦU tiểu mục thông số kỹ thuật UI, ngay sau heading:

```markdown
#### 4.2.1.1. Thông số kỹ thuật giao diện người dùng

![Giao diện tạo yêu cầu nhập kho](images/5_1_1a_B5_image1.png)

Quy trình này xử lý việc tạo yêu cầu nhập kho tự động...
```

2. **Đối với nhiều hình ảnh trong một sheet**: Nhúng mỗi hình ảnh gần nội dung liên quan:

```markdown
#### 4.2.1.1. Thông số kỹ thuật giao diện người dùng

**Màn hình tìm kiếm:**

![Màn hình tìm kiếm yêu cầu](images/5_1_1a_B5_image1.png)

Người dùng có thể tìm kiếm theo nhiều tiêu chí...

**Màn hình chi tiết:**

![Màn hình chi tiết yêu cầu](images/5_1_1a_B10_image2.png)

Màn hình hiển thị thông tin chi tiết của yêu cầu...
```

### Hướng dẫn Mô tả Hình ảnh

- Sử dụng mô tả tiếng Việt giải thích hình ảnh hiển thị gì
- Cụ thể: "Giao diện tạo yêu cầu nhập kho" không chỉ "Hình ảnh"
- Bao gồm ngữ cảnh: "Màn hình phê duyệt yêu cầu xuất kho"

### QUAN TRỌNG: KHÔNG Bỏ qua Hình ảnh

Nếu bản tóm tắt sheet đề cập đến file hình ảnh, bạn PHẢI bao gồm nó trong đầu ra. Hình ảnh là tài liệu quan trọng cho các thông số kỹ thuật UI.


### Cách Xử lý các Cặp Sheet

Kết hợp các sheet thành cặp thành **một section được đánh số với hai tiểu mục**:

```markdown
### 4.2.1. [Tiêu đề tiếng Anh từ các sheet]

#### 4.2.1.1. Thông số kỹ thuật giao diện người dùng
[Nội dung tiếng Việt từ sheet "a" - quy trình, giao diện người dùng, tương tác các bên liên quan]

#### 4.2.1.2. Thông số kỹ thuật chi tiết
[Nội dung tiếng Việt từ sheet "b" - yêu cầu trường, quy tắc validation, hành vi hệ thống]
```

Nếu sheet không có cặp (chỉ có "a" hoặc chỉ có "b"), tạo section độc lập:

```markdown
### 4.2.1. [Tiêu đề tiếng Anh]

[Nội dung tiếng Việt từ sheet]
```

---

## Cấu trúc Đầu ra BRD

Tổ chức nội dung tổng hợp theo cấu trúc được đánh số này:

### 1. Mục lục
   - Liệt kê tất cả các section chính với liên kết nội bộ và số thứ tự
   - Bao gồm các tiểu mục cho Yêu cầu Nghiệp vụ
   - Ví dụ:
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

### 2. Executive Summary (Nội dung tiếng Việt)
   - Tổng quan dự án cấp cao
   - Các sản phẩm chính
   
### 3. Project Scope & Objectives (Nội dung tiếng Việt)
   - Trong phạm vi / Ngoài phạm vi
   - Mục tiêu dự án
   
### 4. Stakeholders (Nội dung tiếng Việt)
   - Danh sách hợp nhất tất cả các vai trò được đề cập trong các sheet
   
### 5. Business Requirements (Nội dung tiếng Việt)
   - **Tổ chức theo chủ đề logic** (Dashboard, Quản lý tài sản, Kho, Bảo trì, v.v.)
   - Mỗi sheet trở thành tiểu mục được đánh số riêng với đầy đủ chi tiết được bảo toàn
   - Các sheet liên quan (cặp a/b) được kết hợp như mô tả ở trên
   - Sử dụng đánh số: 4.1., 4.2., 4.2.1., 4.2.2., v.v.
   
### 6. Assumptions & Constraints (Nội dung tiếng Việt)

### 7. Dependencies (Nội dung tiếng Việt)
   - Phụ thuộc hệ thống
   - Phụ thuộc quy trình
   
### 8. Acceptance Criteria (Nội dung tiếng Việt)
   - Được rút ra từ các yêu cầu tìm thấy trong các sheet
   
### 9. Glossary (Nội dung tiếng Việt)
   - Thuật ngữ và chữ viết tắt tìm thấy trong các sheet

---

## Ví dụ Chuyển đổi

### Đầu vào (Bản tóm tắt Sheet):

**Sheet 5.1.1a:**
```
Tiêu đề: Create Warehouse Intake Request (UI)
Loại: UI/Quy trình
Tóm tắt: Tài liệu giao diện người dùng cho nhập kho...
Các bên liên quan: WM, AMP, Hệ thống
Yêu cầu: Chức năng tìm kiếm, bố cục biểu mẫu...
```

**Sheet 5.1.1b:**
```
Tiêu đề: Create Warehouse Intake Request (Specs)
Loại: Đặc tả
Tóm tắt: Thông số kỹ thuật cho nhập kho...
Yêu cầu: Độ dài trường, quy tắc validation, cập nhật trạng thái...
```

### Đầu ra (Section BRD):

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

[Nội dung đầy đủ bằng tiếng Việt từ 5.1.1b bao gồm yêu cầu trường, validation, hành vi hệ thống]

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

Lưu ý cách:
- Header sử dụng định dạng đánh số: `### 4.2.1. Create Warehouse Intake Request` (tiêu đề tiếng Anh)
- Tất cả nội dung bằng tiếng Việt
- Liên kết sử dụng anchor được đánh số: `[quy trình phê duyệt](#422-approve-warehouse-entry-request)`
- Cả hai sheet (5.1.1a và 5.1.1b) được kết hợp thành một section với các tiểu mục

---

## Danh sách Kiểm tra Xác thực

Trước khi hoàn thành phản hồi, xác minh:

1. ✅ Mọi section có đánh số đúng (1., 2.1., 4.2.3., v.v.)
2. ✅ Tất cả tiêu đề section bằng tiếng Anh
3. ✅ Tất cả nội dung trong section bằng tiếng Việt
4. ✅ Header section SẠCH - không có cú pháp `{#id}`, chỉ số và tiêu đề
5. ✅ Tất cả liên kết nội bộ sử dụng anchor dựa trên tiêu đề được đánh số (ví dụ: `#421-create-warehouse-intake-request`)
6. ✅ Các sheet thành cặp (a/b) được kết hợp thành section được đánh số duy nhất
7. ✅ Nội dung đầy đủ được bảo toàn - tóm tắt, yêu cầu, các bên liên quan, thông số trường
8. ✅ Các section được tổ chức theo chủ đề logic với hệ thống phân cấp đánh số đúng
9. ✅ **Section cha liên kết đến các section con của nó**
10. ✅ **Mô tả quy trình làm việc liên kết đến các quy trình liên quan**
11. ✅ **Executive Summary liên kết đến các module chính**
12. ✅ **Có ít nhất 20+ liên kết nội bộ trong tài liệu**
13. ✅ **Tất cả hình ảnh được đề cập trong bản tóm tắt sheet được nhúng với ![mô tả](images/filename.png)**
"""


USER_PROMPT_TEMPLATE = """Dưới đây là các bản tóm tắt của {num_sheets} sheet từ file Excel Tài liệu Yêu cầu Nghiệp vụ.

Vui lòng tổng hợp những bản tóm tắt này thành một Tài liệu Yêu cầu Nghiệp vụ toàn diện theo hướng dẫn của bạn.

**LƯU Ý QUAN TRỌNG:**
1. Sử dụng header section ĐƯỢC ĐÁNH SỐ với tiêu đề tiếng Anh (ví dụ: "4.2.1. Create Warehouse Intake Request")
2. Viết TẤT CẢ nội dung bằng tiếng Việt
3. Kết hợp các sheet thành cặp (a/b) thành section được đánh số duy nhất
4. Bảo toàn NỘI DUNG ĐẦY ĐỦ từ mỗi sheet - không tóm tắt thành bullet point
5. Sử dụng anchor dựa trên tiêu đề được đánh số cho liên kết (ví dụ: `[quy trình phê duyệt](#422-approve-warehouse-entry-request)`)
6. **THÊM THAM CHIẾU CHÉO:** Section cha PHẢI liên kết đến section con. Nhắm đến 20+ liên kết nội bộ.
7. KHÔNG bao gồm ghi chú tài liệu nguồn, tham chiếu ghép cặp sheet, hoặc ma trận truy xuất nguồn gốc
8. **NHÚNG TẤT CẢ HÌNH ẢNH** được đề cập trong bản tóm tắt sử dụng định dạng ![mô tả](images/filename.png)

---

## Các Bản tóm tắt Sheet

{summaries}

---

Vui lòng cung cấp BRD hoàn chỉnh ở định dạng Markdown với tiêu đề tiếng Anh được đánh số, nội dung tiếng Việt và tham chiếu chéo nội bộ phong phú.
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