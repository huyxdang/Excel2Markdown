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
2. **Mức độ chi tiết** (chi-tiết-cao / tổng-quan) - QUAN TRỌNG cho việc quyết định format
3. **Tên sheet gốc** - Tiêu đề chính xác từ Excel (có thể tiếng Anh hoặc tiếng Việt)
4. Tóm tắt thông tin chính (2–3 đoạn)
5. Các bên liên quan/vai trò được đề cập
6. Các yêu cầu tìm thấy (nếu có)
7. Các sheet liên quan / tham chiếu
8. **Bảng cần giữ nguyên** (nếu có) - Markdown tables từ sheet gốc
9. Hình ảnh trong sheet (Claude's extraction - có thể không chính xác)
10. **Danh sách hình ảnh (trích xuất tự động)** - NGUỒN CHÍNH XÁC cho đường dẫn hình ảnh

---

## QUAN TRỌNG NHẤT: Quy tắc Nhúng Hình ảnh

### NGUỒN DUY NHẤT CHO ĐƯỜNG DẪN HÌNH ẢNH

**CHỈ sử dụng đường dẫn hình ảnh từ "Section 10: Danh sách hình ảnh (trích xuất tự động)".**

Section 10 được tạo bởi code programmatically và LUÔN CHÍNH XÁC.
Section 9 (Hình ảnh trong sheet) có thể KHÔNG chính xác - KHÔNG sử dụng.

### QUY TẮC TUYỆT ĐỐI

1. **COPY-PASTE CHÍNH XÁC** từ Section 10
   - Nếu Section 10 ghi: `![5.2.1a_B5](images/5_2_1a_B5_image1.png)`
   - Thì BRD phải ghi: `![5.2.1a_B5](images/5_2_1a_B5_image1.png)`
   
2. **KHÔNG BAO GIỜ:**
   - Tự đặt tên file như `images/warehouse_confirmation.png`
   - Thay đổi underscore `_` thành dot `.`
   - Thay đổi dot `.` thành underscore `_`
   - Đoán hoặc suy luận tên file
   - Sử dụng thông tin từ Section 9

3. **NẾU KHÔNG TÌM THẤY Section 10:**
   - Kiểm tra lại bản tóm tắt
   - Nếu thực sự không có → sheet không có hình ảnh → không nhúng gì

### Ví dụ ĐÚNG vs SAI

| Trong Section 10 | ✅ ĐÚNG | ❌ SAI |
|------------------|---------|--------|
| `![5.2.1a_B5](images/5_2_1a_B5_image1.png)` | `![Giao diện nhập kho](images/5_2_1a_B5_image1.png)` | `![Giao diện](images/5.2.1a_B5_image1.png)` |
| `![5_1_3a_B5](images/5_1_3a_B5_image2.png)` | `![Màn hình xác nhận](images/5_1_3a_B5_image2.png)` | `![Màn hình](images/warehouse_confirm.png)` |

**LƯU Ý:** Bạn CÓ THỂ thay đổi phần mô tả `![...]` nhưng KHÔNG ĐƯỢC thay đổi phần đường dẫn `(images/...)`.

---

## QUAN TRỌNG: Quy tắc Giữ Bảng vs Dùng Prose

### Khi nào GIỮ NGUYÊN BẢNG (Markdown Table)

Giữ nguyên dạng bảng khi bản tóm tắt có:
- Mức độ chi tiết = `chi-tiết-cao`
- Phần "Bảng cần giữ nguyên" có nội dung

**Các loại bảng PHẢI giữ nguyên:**

| Loại bảng | Ví dụ | Lý do |
|-----------|-------|-------|
| Field Specifications | Tên trường, kiểu dữ liệu, độ dài, constraints | Dev cần tra cứu chính xác |
| Validation Rules | Điều kiện, error message, action | QA cần test từng rule |
| Status Transitions | Trạng thái hiện tại → Trạng thái mới, điều kiện | Logic phức tạp, dễ nhầm nếu viết prose |
| Data Mapping | Source field → Target field, transformation | Integration cần mapping chính xác |
| API Specs | Endpoint, method, params, response | Dev cần reference |
| Error Codes | Mã lỗi, message, nguyên nhân, xử lý | Support cần tra cứu |
| Permission Matrix | Role × Action × Allowed/Denied | Security review |

**Ví dụ GIỮ BẢNG:**

```markdown
#### 4.2.1.2. Thông số kỹ thuật chi tiết

**Đặc tả trường dữ liệu:**

| Tên trường | Kiểu dữ liệu | Độ dài | Bắt buộc | Validation | Mô tả |
|------------|--------------|--------|----------|------------|-------|
| so_yeu_cau | VARCHAR | 50 | Có | Format: NK.YY.xxxx | Số yêu cầu tự động sinh |
| ngay_tao | DATE | - | Có | >= ngày hiện tại | Ngày tạo yêu cầu |
| tieu_de | NVARCHAR | 150 | Có | Không chứa ký tự đặc biệt | Tiêu đề yêu cầu |
| trang_thai | VARCHAR | 20 | Có | Enum: Draft/Pending/Approved/Rejected | Trạng thái hiện tại |

**Quy tắc chuyển trạng thái:**

| Trạng thái hiện tại | Hành động | Trạng thái mới | Điều kiện | Người thực hiện |
|---------------------|-----------|----------------|-----------|-----------------|
| Draft | Submit | Pending | Đủ thông tin bắt buộc | Người tạo |
| Pending | Approve | Approved | Có quyền phê duyệt | WM Manager |
| Pending | Reject | Rejected | Có quyền phê duyệt | WM Manager |
| Rejected | Resubmit | Pending | Đã sửa theo feedback | Người tạo |
```

### Khi nào DÙNG PROSE/SECTIONS

Dùng prose khi bản tóm tắt có:
- Mức độ chi tiết = `tổng-quan`
- Không có phần "Bảng cần giữ nguyên"
- Nội dung mô tả quy trình, luồng công việc, business logic

**Ví dụ DÙNG PROSE:**

```markdown
#### 4.2.1.1. Thông số kỹ thuật giao diện người dùng

Quy trình tạo yêu cầu nhập kho được khởi tạo tự động khi có yêu cầu chuyển kho được xác nhận. Hệ thống sẽ kế thừa toàn bộ thông tin từ yêu cầu chuyển kho bao gồm thông tin tài sản, chi tiết kho đích và các tệp đính kèm.

**Cấu trúc màn hình:**
- Phần header hiển thị số yêu cầu và trạng thái
- Phần thông tin chung cho phép nhập tiêu đề và ghi chú
- Phần chi tiết tài sản hiển thị danh sách tài sản được chuyển
- Phần tệp đính kèm cho phép upload thêm tài liệu

**Các bên liên quan:** Hệ thống (tự động tạo), Quản lý kho (phê duyệt), AMP (theo dõi)
```

### Quy tắc Kết hợp

Một section có thể KẾT HỢP cả prose và tables:

```markdown
### 4.2.1. Tạo Yêu Cầu Nhập Kho

#### 4.2.1.1. Thông số kỹ thuật giao diện người dùng

[PROSE - mô tả quy trình, màn hình, tương tác]

Quy trình này xử lý việc tạo yêu cầu nhập kho tự động...

#### 4.2.1.2. Thông số kỹ thuật chi tiết

[PROSE giới thiệu ngắn]

Dưới đây là đặc tả chi tiết các trường dữ liệu và quy tắc validation:

[TABLE - field specs]

| Tên trường | Kiểu dữ liệu | ... |
|------------|--------------|-----|

[PROSE chuyển tiếp]

Hệ thống áp dụng các quy tắc chuyển trạng thái sau:

[TABLE - status transitions]

| Trạng thái hiện tại | Hành động | ... |
|---------------------|-----------|-----|
```

---

## QUAN TRỌNG: Cấu trúc Section và Liên kết Nội bộ

### Phương pháp: GIỮ NGUYÊN TÊN SHEET GỐC

**NGUYÊN TẮC CHÍNH:** Tiêu đề section PHẢI giữ nguyên y hệt tên sheet trong Excel gốc - có thể là tiếng Anh, tiếng Việt, hoặc kết hợp cả hai. KHÔNG dịch, KHÔNG thay đổi.

**Ví dụ:**
- Nếu sheet tên "Create Warehouse Intake Request" → header: `### 4.2.1. Create Warehouse Intake Request`
- Nếu sheet tên "Tạo Yêu Cầu Nhập Kho" → header: `### 4.2.1. Tạo Yêu Cầu Nhập Kho`
- Nếu sheet tên "Asset Dashboard - Bảng Điều Khiển" → header: `### 4.1. Asset Dashboard - Bảng Điều Khiển`

### Quy tắc cho Header Section

1. **Tiêu đề section = Tên sheet gốc** (giữ nguyên ngôn ngữ từ Excel)
2. **Thêm số thứ tự** trước tiêu đề (1., 2.1., 4.2.3., v.v.)
3. **Giữ header sạch sẽ** - không có cú pháp `{#id}` hoặc tham chiếu sheet
4. **Đối với các sheet liên quan (ví dụ: 5.1.1a UI + 5.1.1b Specs)**, kết hợp thành MỘT section với tên từ sheet chính

### Quy ước Đánh số

- **Cấp 1:** 1., 2., 3., 4., v.v. (ví dụ: "1. Executive Summary" hoặc "1. Tóm Tắt Điều Hành")
- **Cấp 2:** 1.1., 1.2., 2.1., 2.2., v.v. (ví dụ: "4.1. Dashboard Tài Sản")
- **Cấp 3:** 1.1.1., 1.1.2., 2.1.1., v.v. (ví dụ: "4.2.1. Tạo Yêu Cầu Nhập Kho")
- **Cấp 4:** 1.1.1.1., 1.1.1.2., v.v. (nếu cần cho các tiểu mục chi tiết)

### Quy tắc cho Liên kết Nội bộ

Sử dụng **anchor dựa trên tiêu đề** được suy ra từ heading section. Markdown tự động tạo anchor bằng cách:
- Chuyển thành chữ thường
- Thay khoảng trắng bằng dấu gạch ngang
- Loại bỏ ký tự đặc biệt và dấu chấm
- **Giữ nguyên ký tự tiếng Việt** (dấu sẽ bị loại bỏ trong một số renderer)

**Ví dụ:**
- `### 1. Executive Summary` → anchor: `#1-executive-summary`
- `### 4.1. Dashboard Tài Sản` → anchor: `#41-dashboard-tài-sản`
- `### 4.2.1. Tạo Yêu Cầu Nhập Kho` → anchor: `#421-tạo-yêu-cầu-nhập-kho`

**Định dạng liên kết:**
```markdown
Xem phần [4.2.1. Tạo Yêu Cầu Nhập Kho](#421-tạo-yêu-cầu-nhập-kho) để biết thêm chi tiết.
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
   ### 4.2. Module Quản Lý Kho
   
   Module này bao gồm các quy trình sau:
   - [4.2.1. Tạo Yêu Cầu Nhập Kho](#421-tạo-yêu-cầu-nhập-kho)
   - [4.2.2. Xác Nhận Nhập Kho](#422-xác-nhận-nhập-kho)
   - [4.2.3. Phê Duyệt Yêu Cầu Nhập Kho](#423-phê-duyệt-yêu-cầu-nhập-kho)
   ```

2. **Các section liên quan liên kết với nhau:**
   ```markdown
   ### 4.2.1. Tạo Yêu Cầu Nhập Kho
   
   Sau khi tạo yêu cầu, quy trình chuyển sang [4.2.2. quy trình phê duyệt](#422-quy-trình-phê-duyệt).
   Để biết quy trình hủy, xem [4.2.4. Huỷ Quy Trình Nhập Kho](#424-huỷ-quy-trình-nhập-kho).
   ```

3. **Khi yêu cầu đề cập đến các quy trình khác:**
   ```markdown
   **Quy trình làm việc:**
   1. Hệ thống tạo yêu cầu nhập kho
   2. Cập nhật trạng thái kích hoạt [quy trình phê duyệt](#422-quy-trình-phê-duyệt)
   3. Sau khi phê duyệt, chuyển sang [xác nhận nhập kho](#423-xác-nhận-nhập-kho)
   ```

4. **Trong phần Executive Summary và Overview:**
   ```markdown
   Các sản phẩm chính bao gồm [module quản lý kho toàn diện](#42-module-quản-lý-kho) 
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

Mỗi bản tóm tắt sheet chứa thông tin có giá trị. Bạn phải **bảo toàn toàn bộ nội dung**, không nén thành các bullet point đơn giản.

**XẤU (mất chi tiết):**
```markdown
### 4.2. Warehouse Management
- Hỗ trợ chuyển kho
- Có quy trình phê duyệt
- Có validation
```

**TỐT (bảo toàn chi tiết với BẢNG khi cần):**
```markdown
### 4.2.1. Create Warehouse Intake Request

#### 4.2.1.1. Thông số kỹ thuật giao diện người dùng

Quy trình này xử lý việc tạo yêu cầu nhập kho tự động khi tài sản được chuyển đến kho...

[Prose mô tả quy trình]

#### 4.2.1.2. Thông số kỹ thuật chi tiết

**Đặc tả trường dữ liệu:**

| Tên trường | Kiểu dữ liệu | Độ dài | Bắt buộc | Validation |
|------------|--------------|--------|----------|------------|
| so_yeu_cau | VARCHAR | 50 | Có | NK.YY.xxxx |
| ngay_tao | DATE | - | Có | >= today |
| ... | ... | ... | ... | ... |

**Quy tắc chuyển trạng thái:**

| Từ trạng thái | Hành động | Đến trạng thái | Điều kiện |
|---------------|-----------|----------------|-----------|
| Draft | Submit | Pending | Required fields filled |
| ... | ... | ... | ... |
```

---

## Vị trí Đặt Hình ảnh trong BRD

### Quy tắc Vị trí

1. **Đối với sheet UI/Quy trình (sheet "a")**: Đặt hình ảnh ở ĐẦU tiểu mục thông số kỹ thuật UI, ngay sau heading:

```markdown
#### 4.2.1.1. Thông số kỹ thuật giao diện người dùng

![Giao diện tạo yêu cầu nhập kho](images/5_1_1a_B5_image1.png)

Quy trình này xử lý việc tạo yêu cầu nhập kho tự động...
```

2. **Nhiều hình ảnh trong một sheet**: Đặt theo thứ tự cell (B5 trước C10, v.v.)

3. **Mô tả hình ảnh**: Có thể viết tiếng Việt mô tả nội dung, nhưng KHÔNG thay đổi đường dẫn

---

## Cách Xử lý các Cặp Sheet

Kết hợp các sheet thành cặp thành **một section được đánh số với hai tiểu mục**, sử dụng **tên sheet gốc** làm tiêu đề chính:

```markdown
### 4.2.1. [TÊN SHEET GỐC - giữ nguyên ngôn ngữ]

#### 4.2.1.1. Thông số kỹ thuật giao diện người dùng
[Nội dung từ sheet "a" - quy trình, giao diện người dùng, tương tác các bên liên quan]
[HÌNH ẢNH từ Section 10 của sheet "a"]
[Thường là PROSE vì mô tả flow]

#### 4.2.1.2. Thông số kỹ thuật chi tiết
[Nội dung từ sheet "b" - yêu cầu trường, quy tắc validation, hành vi hệ thống]
[Thường có TABLES vì chi tiết specs]
```

**Ví dụ với tên tiếng Anh:**
```markdown
### 4.2.1. Create Warehouse Intake Request

#### 4.2.1.1. Thông số kỹ thuật giao diện người dùng

![Giao diện tạo yêu cầu](images/5_1_1a_B5_image1.png)

...

#### 4.2.1.2. Thông số kỹ thuật chi tiết
...
```

---

## Cấu trúc Đầu ra BRD

Tổ chức nội dung tổng hợp theo cấu trúc được đánh số này. **Các section cố định** (1-4, 6-9) giữ nguyên tiêu đề tiếng Anh. **Section 5 (Business Requirements)** sử dụng tên sheet gốc.

### 1. Table of Contents
   - Liệt kê tất cả các section chính với liên kết nội bộ và số thứ tự
   
### 2. Executive Summary
   - Tổng quan dự án cấp cao
   - Các sản phẩm chính
   
### 3. Project Scope & Objectives
   - Trong phạm vi / Ngoài phạm vi
   - Mục tiêu dự án
   
### 4. Stakeholders
   - Danh sách hợp nhất tất cả các vai trò
   
### 5. Business Requirements
   - **Tổ chức theo chủ đề logic**
   - **Tiêu đề mỗi tiểu mục = Tên sheet gốc** (giữ nguyên tiếng Anh hoặc tiếng Việt)
   - **GIỮ NGUYÊN TABLES** từ bản tóm tắt khi có
   - **NHÚNG HÌNH ẢNH** từ Section 10 với đường dẫn chính xác
   - Sử dụng đánh số: 5.1., 5.2., 5.2.1., v.v.
   
### 6. Assumptions & Constraints

### 7. Dependencies

### 8. Acceptance Criteria

### 9. Glossary

---

## Danh sách Kiểm tra Xác thực

Trước khi hoàn thành phản hồi, xác minh:

1. ✅ Mọi section có đánh số đúng (1., 2.1., 5.2.3., v.v.)
2. ✅ **Tiêu đề section Business Requirements = Tên sheet gốc** (giữ nguyên ngôn ngữ)
3. ✅ Các section cố định (1-4, 6-9) giữ tiêu đề tiếng Anh
4. ✅ **TABLES được giữ nguyên** cho sheets có mức độ chi tiết = `chi-tiết-cao`
5. ✅ **PROSE được sử dụng** cho sheets có mức độ chi tiết = `tổng-quan`
6. ✅ Tất cả liên kết nội bộ sử dụng anchor đúng
7. ✅ Các sheet thành cặp (a/b) được kết hợp thành section duy nhất
8. ✅ Nội dung đầy đủ được bảo toàn
9. ✅ Section cha liên kết đến các section con
10. ✅ Có ít nhất 20+ liên kết nội bộ
11. ✅ **TẤT CẢ hình ảnh từ Section 10 được nhúng**
12. ✅ **ĐƯỜNG DẪN HÌNH ẢNH CHÍNH XÁC 100%** - copy từ Section 10, KHÔNG tự đặt tên
"""


USER_PROMPT_TEMPLATE = """Dưới đây là các bản tóm tắt của {num_sheets} sheet từ file Excel Tài liệu Yêu cầu Nghiệp vụ.

Vui lòng tổng hợp những bản tóm tắt này thành một Tài liệu Yêu cầu Nghiệp vụ toàn diện theo hướng dẫn của bạn.

**LƯU Ý QUAN TRỌNG VỀ HÌNH ẢNH:**

⚠️ **CHỈ sử dụng đường dẫn hình ảnh từ "Section 10: Danh sách hình ảnh (trích xuất tự động)"**

- Section 10 được tạo bởi code và LUÔN CHÍNH XÁC
- Section 9 có thể KHÔNG chính xác - KHÔNG sử dụng
- Copy-paste CHÍNH XÁC đường dẫn từ Section 10
- KHÔNG thay đổi bất kỳ ký tự nào trong đường dẫn (underscore, dot, số, v.v.)
- KHÔNG tự đặt tên file mô tả như `warehouse_confirmation.png`

**CÁC LƯU Ý KHÁC:**
1. **GIỮ NGUYÊN TÊN SHEET GỐC** làm tiêu đề section (tiếng Anh hoặc tiếng Việt - KHÔNG dịch)
2. Thêm số thứ tự trước tiêu đề (1., 2.1., 5.2.3., v.v.)
3. Kết hợp các sheet thành cặp (a/b) thành section duy nhất
4. **GIỮ NGUYÊN MARKDOWN TABLES** từ bản tóm tắt cho các sheet có mức độ chi tiết = `chi-tiết-cao`
5. **DÙNG PROSE** cho các sheet có mức độ chi tiết = `tổng-quan`
6. Bảo toàn NỘI DUNG ĐẦY ĐỦ từ mỗi sheet
7. **THÊM THAM CHIẾU CHÉO:** Nhắm đến 20+ liên kết nội bộ

---

## Các Bản tóm tắt Sheet

{summaries}

---

Vui lòng cung cấp BRD hoàn chỉnh ở định dạng Markdown với:
- Tiêu đề section giữ nguyên từ tên sheet gốc
- Tables được giữ nguyên khi cần
- Tham chiếu chéo nội bộ phong phú
- **Đường dẫn hình ảnh CHÍNH XÁC 100% từ Section 10**
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


def validate_image_paths(brd_content: str, summaries: dict) -> dict:
    """
    Validate that image paths in BRD match those in Section 10 of summaries.
    
    Returns:
        Dictionary with validation results
    """
    import re
    
    # Extract all image paths from Section 10 of all summaries
    valid_paths = set()
    section_10_pattern = r'## 10\. Danh sách hình ảnh.*?(?=\n## |\n---|\Z)'
    image_pattern = r'!\[[^\]]*\]\((images/[^)]+)\)'
    
    for sheet_name, summary in summaries.items():
        # Find Section 10
        section_match = re.search(section_10_pattern, summary, re.DOTALL)
        if section_match:
            section_content = section_match.group(0)
            # Extract image paths from Section 10
            for match in re.finditer(image_pattern, section_content):
                valid_paths.add(match.group(1))
    
    # Extract all image paths used in BRD
    brd_images = re.findall(image_pattern, brd_content)
    
    # Check for invalid paths
    invalid_paths = []
    for path in brd_images:
        if path not in valid_paths:
            invalid_paths.append(path)
    
    return {
        'valid_paths': list(valid_paths),
        'brd_images': brd_images,
        'invalid_paths': invalid_paths,
        'missing_images': list(valid_paths - set(brd_images))
    }


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
        
        # Validate image paths
        print("\nValidating image paths...")
        image_validation = validate_image_paths(brd_content, summaries)
        print(f"  Valid paths from Section 10: {len(image_validation['valid_paths'])}")
        print(f"  Images in BRD: {len(image_validation['brd_images'])}")
        
        if image_validation['invalid_paths']:
            print(f"  ⚠️  Invalid/hallucinated paths: {image_validation['invalid_paths']}")
        if image_validation['missing_images']:
            print(f"  ⚠️  Missing images (in Section 10 but not in BRD): {image_validation['missing_images'][:10]}")
        if not image_validation['invalid_paths'] and not image_validation['missing_images']:
            print(f"  ✅ All image paths valid!")
        
        # Add generation metadata at the end
        metadata = f"\n\n---\n\n*Generated by Claude Sonnet 4.5 from {len(summaries)} sheet summaries*\n"
        metadata += f"*Headings: {len(validation['headings_found'])} | Internal Links: {len(validation['links_found'])} | Images: {len(image_validation['brd_images'])}*\n"
        
        # Check final validation state
        final_validation = validate_brd_anchors(brd_content, sheet_ids)
        if final_validation.get('broken_links') or validation.get('invalid_syntax'):
            metadata += f"\n*⚠️ Link validation warnings - some links may need manual review*\n"
        else:
            metadata += f"\n*✅ All internal links validated successfully*\n"
        
        if image_validation['invalid_paths']:
            metadata += f"*⚠️ Image path warnings - {len(image_validation['invalid_paths'])} paths may be incorrect*\n"
        elif image_validation['missing_images']:
            metadata += f"*⚠️ {len(image_validation['missing_images'])} images from summaries not included in BRD*\n"
        else:
            metadata += f"*✅ All image paths validated successfully*\n"
        
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