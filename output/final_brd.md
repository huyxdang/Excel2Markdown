# Tài liệu Yêu cầu Nghiệp vụ (BRD)
## Hệ thống Quản lý Tài sản FAM - Nâng cấp Wave 4

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Project Scope & Objectives](#2-project-scope--objectives)
3. [Stakeholders](#3-stakeholders)
4. [Business Requirements](#4-business-requirements)
   - 4.1. [Dashboard Tài sản](#41-dashboard-tài-sản)
   - 4.2. [Module Quản lý Kho](#42-module-quản-lý-kho)
     - 4.2.1. [Điều chuyển về kho](#421-điều-chuyển-về-kho)
     - 4.2.2. [NHẬP KHO THỦ CÔNG](#422-nhập-kho-thủ-công)
     - 4.2.3. [Xác nhận nhập kho thủ công](#423-xác-nhận-nhập-kho-thủ-công)
     - 4.2.4. [Hủy yêu cầu nhập kho](#424-hủy-yêu-cầu-nhập-kho)
     - 4.2.5. [Phê duyệt yêu cầu cấp tài sản](#425-phê-duyệt-yêu-cầu-cấp-tài-sản)
     - 4.2.6. [Tạo yêu cầu xuất kho](#426-tạo-yêu-cầu-xuất-kho)
     - 4.2.7. [Xuất kho từ cấp tài sản - Tiếp nhận yêu cầu xuất kho](#427-xuất-kho-từ-cấp-tài-sản---tiếp-nhận-yêu-cầu-xuất-kho)
     - 4.2.8. [Xuất kho từ cấp tài sản - Phê duyệt yêu cầu xuất kho](#428-xuất-kho-từ-cấp-tài-sản---phê-duyệt-yêu-cầu-xuất-kho)
     - 4.2.9. [Xuất kho từ Cấp tài sản - Nhận tài sản](#429-xuất-kho-từ-cấp-tài-sản---nhận-tài-sản)
     - 4.2.10. [Hủy Yêu cầu Xuất kho](#4210-hủy-yêu-cầu-xuất-kho)
     - 4.2.11. [Tạo yêu cầu điều chuyển tài sản giữa các kho](#4211-tạo-yêu-cầu-điều-chuyển-tài-sản-giữa-các-kho)
     - 4.2.12. [Phê duyệt yêu cầu điều chuyển kho](#4212-phê-duyệt-yêu-cầu-điều-chuyển-kho)
5. [Assumptions & Constraints](#5-assumptions--constraints)
6. [Dependencies](#6-dependencies)
7. [Acceptance Criteria](#7-acceptance-criteria)
8. [Glossary](#8-glossary)

---

## 1. Executive Summary

Dự án nâng cấp hệ thống FAM Wave 4 nhằm cải thiện khả năng quản lý tài sản thông qua việc phát triển [4.1. Dashboard Tài sản](#41-dashboard-tài-sản) hiện đại với khả năng visualization và customization cao. Hệ thống sẽ được bổ sung [4.2. Module Quản lý Kho](#42-module-quản-lý-kho) toàn diện để xử lý các quy trình xuất-nhập kho tài sản một cách tự động và có kiểm soát.

Các sản phẩm chính bao gồm:

- **Dashboard tài sản nâng cao**: Cung cấp giao diện trực quan với 4 KPI chính, 5 loại biểu đồ tương tác và bộ lọc đa tiêu chí
- **Module quản lý kho**: Hỗ trợ đầy đủ quy trình [điều chuyển về kho](#421-điều-chuyển-về-kho), [nhập kho thủ công](#422-nhập-kho-thủ-công), [xuất kho từ cấp tài sản](#427-xuất-kho-từ-cấp-tài-sản---tiếp-nhận-yêu-cầu-xuất-kho) và [điều chuyển giữa các kho](#4211-tạo-yêu-cầu-điều-chuyển-tài-sản-giữa-các-kho)
- **Tích hợp tự động**: Đồng bộ với OMS, EMS và hệ thống ITSM

Dự án ưu tiên phát triển theo thứ tự: Dashboard (ưu tiên 1), Module kho (ưu tiên 1), các enhancement khác (ưu tiên 2-3), và Module sửa chữa (ưu tiên 4).

---

## 2. Project Scope & Objectives

### Trong phạm vi (In Scope):

- Phát triển dashboard tài sản với khả năng visualization và customization
- Xây dựng module quản lý kho hoàn chỉnh với các quy trình:
  - [Nhập kho tự động và thủ công](#422-nhập-kho-thủ-công)
  - [Xuất kho từ cấp tài sản](#427-xuất-kho-từ-cấp-tài-sản---tiếp-nhận-yêu-cầu-xuất-kho)
  - [Điều chuyển tài sản](#421-điều-chuyển-về-kho)
- Cải tiến giao diện quản lý tài sản hiện có
- Tích hợp tự động với các hệ thống EMS, OMS, ITSM

### Ngoài phạm vi (Out of Scope):

- Module sửa chữa tài sản (sẽ triển khai ở giai đoạn sau)
- Thay đổi cấu trúc database core của hệ thống hiện tại
- Tích hợp với các hệ thống ngoài OMS, EMS, ITSM

### Mục tiêu dự án:

1. Nâng cao trải nghiệm người dùng qua dashboard trực quan
2. Tự động hóa quy trình quản lý kho và giảm thiểu sai sót
3. Tăng cường khả năng theo dõi và kiểm soát tài sản
4. Đảm bảo tính toàn vẹn và truy xuất dữ liệu

---

## 3. Stakeholders

| Vai trò | Mô tả | Trách nhiệm chính |
|---------|-------|-------------------|
| **AMP (Asset Management Personnel)** | Nhân viên quản lý tài sản | Tạo và xử lý yêu cầu, quản lý lifecycle tài sản |
| **AM (Asset Manager)** | Quản lý tài sản cấp cao | Phê duyệt yêu cầu cấp tài sản, giám sát quy trình |
| **Warehouse Manager (WM)** | Quản lý kho | Phê duyệt yêu cầu xuất-nhập kho, giám sát hoạt động kho |
| **WK (Warehouse Keeper)** | Thủ kho | Thực hiện xuất-nhập kho thực tế, xác nhận giao hàng |
| **BU User** | Người dùng đơn vị kinh doanh | Nhận tài sản, xác nhận giao hàng |
| **BU Manager** | Quản lý đơn vị kinh doanh | Phê duyệt yêu cầu của đơn vị |
| **System Admin** | Quản trị hệ thống | Cấu hình hệ thống, quản lý người dùng |
| **Integration Team** | Đội tích hợp | Đảm bảo kết nối với EMS, OMS, ITSM |

---

## 4. Business Requirements

### 4.1. Dashboard Tài sản

Dashboard Tài sản cung cấp giao diện tổng quan và trực quan hóa dữ liệu nhằm hỗ trợ đưa ra quyết định nhanh chóng. Hệ thống hiển thị thông tin tài sản theo nhiều chiều khác nhau như phòng ban, trạng thái, thời gian sử dụng và biến động theo thời gian.

#### 4.1.1. Phạm vi Dashboard

Dashboard bao gồm dữ liệu tài sản theo orgchart, trạng thái, biến động thời gian, tỷ lệ sử dụng, và các tài sản hết bảo hành hoặc đã sử dụng trên 3-5 năm. Tất cả tính toán đều loại trừ tài sản "Đã thanh lý" và "Vô hiệu hóa".

#### 4.1.2. Thành phần Dashboard

**KPI Tổng quan:**
- Tổng số lượng tài sản (loại trừ đã thanh lý và vô hiệu hóa)
- Tổng giá trị tài sản (theo nguyên giá)
- Tỷ lệ tài sản còn bảo hành
- Tỷ lệ sử dụng tài sản (đang sử dụng/tổng số)

**Biểu đồ tương tác:**
- Sunburst Chart: Cơ cấu tài sản theo trạng thái (vòng trong: IT/ADM/CMD, vòng ngoài: trạng thái)
- Stacked Column: Phân bổ tài sản theo vùng/đơn vị
- Line Chart: Biến động giá trị tài sản theo thời gian
- Scatter Chart: Phân tích tài sản theo thời gian sử dụng

**Bộ lọc:**
- Vùng, Đơn vị sử dụng (đồng bộ từ OMS)
- CAT 1, Group name
- Trạng thái tài sản (không bao gồm đã thanh lý, vô hiệu hóa)

#### 4.1.3. Đặc tả kỹ thuật Dashboard

| STT | Component | Content | Value/Formula | Chart Type | Note |
|-----|-----------|---------|---------------|------------|------|
| 1 | Dashboard tổng quan | Total assets | Count số lượng (All tài sản - Đã thanh lý - Vô hiệu hóa) | - | - |
| 2 | | Total value | Sum nguyên giá (All tài sản - Đã thanh lý - Vô hiệu hóa) | - | - |
| 3 | | Warranty status | Tỷ lệ % theo số lượng tài sản còn hạn bảo hành/(All tài sản - Vô hiệu hóa - Đã thanh lý) | - | - |
| 4 | | Utilization rate | Tỷ lệ % theo số lượng tài sản đang sử dụng/(All tài sản - Vô hiệu hóa - Đã thanh lý) | - | - |

| STT | Filter Name | Data Source | Type |
|-----|-------------|-------------|------|
| 1 | Vùng | - | LOV |
| 2 | Đơn vị sử dụng | OMS | LOV đồng bộ |
| 3 | CAT 1 | - | LOV |
| 4 | Group name | - | LOV |
| 5 | Asset status | - | LOV (Không bao gồm Đã thanh lý, Vô hiệu hóa) |

| STT | Chart Name | Data Field | Chart Type | Note |
|-----|------------|------------|------------|------|
| 1 | Asset Distribution - Cơ cấu theo trạng thái | Nguyên giá | Sunburst (Vòng trong: Nhóm IT/ADM/CMD, Vòng ngoài: Trạng thái) | Hover hiển thị số lượng và giá trị |
| 2 | Asset Distribution - Cơ cấu theo Vùng/Đơn vị | Nguyên giá | Stacked Column | - |
| 3 | Asset Value by Group Name | Nguyên giá | Column | - |
| 4 | Asset Fluctuation Over Time | Nguyên giá | Line | - |
| 5 | Asset by Time in Use | Số lượng | Scatter | - |

Dashboard tích hợp chức năng hover để xem chi tiết, click chuyển module, và xuất dữ liệu Excel.

---

### 4.2. Module Quản lý Kho

Module Quản lý Kho là hệ thống hoàn chỉnh với 8 quy trình chính được thiết kế theo mô hình workflow với nhiều bước duyệt và phân quyền rõ ràng. Hệ thống có khả năng tự động tạo yêu cầu liên kết giữa các quy trình và hỗ trợ chức năng hủy yêu cầu với khả năng tìm kiếm và hủy cascade.

Các quy trình chính bao gồm:
- [Điều chuyển nội bộ](#421-điều-chuyển-về-kho) (chéo và về kho)
- [Nhập kho](#422-nhập-kho-thủ-công) (tự động và thủ công)  
- [Cấp tài sản](#425-phê-duyệt-yêu-cầu-cấp-tài-sản)
- Thanh lý tài sản (phân biệt bid và direct)
- [Xuất kho](#427-xuất-kho-từ-cấp-tài-sản---tiếp-nhận-yêu-cầu-xuất-kho)
- [Điều chuyển kho](#4211-tạo-yêu-cầu-điều-chuyển-tài-sản-giữa-các-kho)

#### 4.2.1. Điều chuyển về kho

Quy trình điều chuyển hàng hóa về kho thông qua việc tạo yêu cầu nhập kho tự động. Hệ thống kế thừa toàn bộ thông tin từ yêu cầu chuyển kho bao gồm thông tin tài sản, chi tiết kho đích và các tệp đính kèm.

##### 4.2.1.1. Thông số kỹ thuật giao diện người dùng

![5.1.1a B5](images/5_1_1a_B5_image1.png)

**Các bước thực hiện quy trình:**
1. Tạo yêu cầu nhập kho: Bước khởi tạo yêu cầu điều chuyển
2. Cập nhật trạng thái yêu cầu: Hệ thống tự động cập nhật trạng thái
3. Cập nhật tasklist: Cập nhật danh sách công việc cần thực hiện
4. Thông báo cho Warehouse Mgr: Gửi thông báo đến người quản lý kho
5. Phê duyệt yêu cầu: Quy trình phụ để phê duyệt yêu cầu

**Các thành phần giao diện:**
- Header hiển thị số yêu cầu và trạng thái
- Phần thông tin chung cho phép nhập tiêu đề và ghi chú
- Phần chi tiết tài sản hiển thị danh sách tài sản được chuyển
- Phần tệp đính kèm cho phép upload thêm tài liệu

Quy trình này xử lý việc tạo yêu cầu nhập kho tự động khi có yêu cầu chuyển kho được xác nhận. Sau khi tạo yêu cầu thành công, hệ thống chuyển đến [phê duyệt yêu cầu nhập kho](#421-điều-chuyển-về-kho).

**Các bên liên quan:** Hệ thống (tự động tạo), Quản lý kho (phê duyệt), AMP (theo dõi)

##### 4.2.1.2. Thông số kỹ thuật chi tiết

Hệ thống tự động tạo yêu cầu nhập kho với đầy đủ thông tin tài sản từ yêu cầu điều chuyển gốc. Sau khi tạo thành công, hệ thống cập nhật trạng thái yêu cầu điều chuyển thành "Đã xác nhận", trạng thái yêu cầu nhập kho thành "Chờ phê duyệt", và gửi thông báo email cho Warehouse Manager.

**Đặc tả trường thông tin chung:**

| STT | Tab/Section | Operator | Action | Field Name | M/O | Field Type | Editable | Max Length | Format | Default Value | Data Rule |
|-----|-------------|----------|---------|------------|-----|------------|----------|------------|--------|---------------|-----------|
| 1 | Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| 2 | Thông tin chung | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| 3 | Thông tin chung | System | Display | Tiêu đề | M | Text | N | 150 | | | =Tiêu đề RQ điều chuyển |

**Đặc tả thông tin kho và đầu mối:**

| Tab/Section | Operator | Action | Field Name | M/O | Field Type | Max Length | Data Source | Data Rule |
|-------------|----------|---------|------------|-----|------------|------------|-------------|-----------|
| Thông tin kho nhập | System | Display | Tên kho | M | List | 50 | | = Kho trong RQ điều chuyển |
| Thông tin kho nhập | System | Display | Địa chỉ kho | M | Text | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Thông tin kho nhập | System | Display | Quản lý kho | M | Text | 50 | OMS | Tự động nhận diện (Tên \| Phòng ban \| Email) |

**Quy trình phê duyệt yêu cầu nhập kho:**

![5.1.2a B6](images/5_1_2a_B6_image2.png)

Quy trình phê duyệt bao gồm hai luồng chính: nếu phê duyệt, hệ thống sẽ cập nhật trạng thái → cập nhật tasklist → gửi email thông báo → chuyển đến [xác nhận nhập kho](#421-điều-chuyển-về-kho). Nếu từ chối, yêu cầu được nhập lý do từ chối → unlock tài sản → cập nhật trạng thái và tasklist → gửi email thông báo.

**Đặc tả phê duyệt yêu cầu:**

Giao diện phê duyệt cho phép Warehouse Manager tìm kiếm yêu cầu nhập kho theo các tiêu chí, xem chi tiết yêu cầu với thông tin toàn diện về tài sản, và đưa ra quyết định phê duyệt hoặc từ chối.

| Field name VN | M/O | Field type | Editable | Max length |
|---------------|-----|------------|----------|------------|
| Số yêu cầu | O | Text | Y | 20 |
| Ngày tạo | O | Date | Y | 20 |
| Tiêu đề | O | Text | Y | 150 |
| Người tạo | O | List | Y | 20 |
| Trạng thái yêu cầu | O | List | Y | 20 |
| Người xử lý | O | List | Y | 20 |
| Ngày xác nhận | O | Date | Y | 20 |

**Xác nhận nhập kho:**

![5.1.3a B5](images/5_1_3a_B5_image3.png)

Quy trình xác nhận nhập kho có hai luồng: luồng xác nhận (khi đồng ý với yêu cầu) và luồng từ chối (khi không đồng ý). Cả hai luồng đều kết thúc bằng việc cập nhật trạng thái, gửi thông báo email và chuyển hướng về màn hình chính.

Khi xác nhận nhập kho, hệ thống tự động cập nhật "Ngày bắt đầu sử dụng" nếu trường này chưa có giá trị và hoàn tất quy trình nhập kho. Khi từ chối, hệ thống unlock tài sản để có thể được sử dụng cho yêu cầu khác.

---

#### 4.2.2. NHẬP KHO THỦ CÔNG

Quy trình nhập kho thủ công cho phép người dùng tạo yêu cầu nhập kho với việc tìm kiếm và chọn tài sản từ danh sách có sẵn, sau đó thực hiện các bước phê duyệt và xác nhận tự động.

##### 4.2.2.1. Thông số kỹ thuật giao diện người dùng

![5.2.1a B5](images/5_2_1a_B5_image4.png)

**Các bước thực hiện quy trình:**
1. **Khởi tạo**: Người dùng bắt đầu tạo yêu cầu
2. **Nhập thông tin**: Tạo yêu cầu nhập kho và đính kèm tài liệu
3. **Quyết định**: Lựa chọn "Gửi" để tiếp tục hoặc "Thoát" để hủy bỏ
4. **Xử lý tự động** (nếu chọn Gửi):
   - Lock tài sản
   - Cập nhật trạng thái yêu cầu  
   - Cập nhật tasklist người nhận
   - Gửi email thông báo cho WM
5. **Chuyển tiếp**: Đến bước phê duyệt yêu cầu

**Các thành phần giao diện:**
- Form nhập thông tin chung (số yêu cầu tự động sinh theo format NK.YY.xxxx)
- Tính năng tìm kiếm tài sản theo nhiều tiêu chí
- Thông tin chi tiết tài sản bao gồm thông tin bảo hành
- Thông tin kho đích, đầu mối giao hàng
- Chức năng đính kèm hồ sơ

##### 4.2.2.2. Thông số kỹ thuật chi tiết

Hệ thống hỗ trợ tìm kiếm tài sản theo mã tài sản, tên, phân loại, nhóm tài sản, PO number với cảnh báo khi tài sản đã bị lock. Thông tin kho tự động lấy từ hệ thống OMS.

**Thông tin form tìm kiếm tài sản:**

| Trường | Operator | Action | Tên field | M/O | Kiểu | Editable | Max length | Format | Ghi chú |
|--------|----------|--------|-----------|-----|------|----------|------------|---------|---------|
| Mã tài sản | User | Input | Mã tài sản | O | Text | N | 20 | | |
| Tên tài sản | User | Input | Tên tài sản | O | Text | Y | 20 | | |
| Phân loại tài sản | User | Select | Phân loại tài sản | O | List | N | 20 | | |
| Nhóm tài sản | User | Select | Nhóm tài sản | O | List | N | 20 | | |
| PO number | User | Input | PO number | O | Text | Y | 20 | | |
| Trạng thái TS | User | Select | Trạng thái TS | O | List | N | 50 | | |

**Thông tin kho và giao hàng:**

| Trường | Operator | Action | Tên field | M/O | Kiểu | Editable | Max length | Nguồn dữ liệu | Ghi chú |
|--------|----------|--------|-----------|-----|------|----------|------------|---------------|---------|
| Tên kho | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | |
| Địa chỉ kho | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động theo tên kho |
| Quản lý kho | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Hiển thị Tên, Phòng ban, Email |
| Đầu mối | User | Input | Đầu mối | M | Text | Y | 50 | | |
| Số điện thoại | User | Input | Số điện thoại | M | Number | Y | 52 | | |
| Thời gian bàn giao | User | Input | Thời gian bàn giao | O | Date | Y | 50 | | |

**Quy trình phê duyệt yêu cầu nhập kho thủ công:**

![5.2.2a B5](images/5_2_2a_B5_image5.png)

Quy trình phê duyệt có hai luồng: nhánh phê duyệt chuyển đến [xác nhận nhập kho](#423-xác-nhận-nhập-kho-thủ-công), nhánh từ chối thực hiện unlock tài sản và thông báo cho AMP.

Warehouse Manager có thể tìm kiếm và phê duyệt yêu cầu với giao diện hiển thị đầy đủ thông tin tài sản, kho nhập và đầu mối giao hàng. Khi từ chối, cần nhập lý do và hệ thống sẽ unlock tài sản, cập nhật trạng thái và gửi thông báo.

---

#### 4.2.3. Xác nhận nhập kho thủ công

Quy trình xác nhận nhập kho thủ công cho phép Warehouse Keeper xác nhận việc nhập kho tài sản sau khi yêu cầu được phê duyệt.

##### 4.2.3.1. Thông số kỹ thuật giao diện người dùng

![5.2.3a B6](images/5_2_3a_B6_image6.png)

**Các bước thực hiện quy trình:**
1. **Nhập thông tin tìm kiếm yêu cầu**: Form nhập liệu để tìm kiếm
2. **Hiển thị kết quả tìm kiếm**: Danh sách kết quả tìm kiếm  
3. **Chọn, xem yêu cầu**: Giao diện xem chi tiết yêu cầu
4. **Gateway quyết định**: "Xác nhận" - Điểm phân nhánh với hai lựa chọn

**Luồng công việc:**
- **Luồng đồng ý**: Xác nhận → Nhập thông tin nhận hàng → Unlock/cập nhật thông tin tài sản → Cập nhật trạng thái yêu cầu → Cập nhật tasklist → Gửi email thông báo
- **Luồng từ chối**: Xác nhận → Nhập lý do từ chối → Đồng ý → Unlock tài sản → Cập nhật trạng thái yêu cầu → Cập nhật tasklist → Gửi email thông báo

##### 4.2.3.2. Thông số kỹ thuật chi tiết

Giao diện cho phép WK tìm kiếm yêu cầu nhập kho, xem chi tiết và thực hiện xác nhận hoặc từ chối. Hệ thống tự động xử lý unlock tài sản, cập nhật trạng thái và gửi thông báo.

**Bảng tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |

**Bảng thông tin kho nhập:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| System | Display | Tên kho | M | List | N | 50 | | |
| System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

Khi xác nhận nhập kho, hệ thống tự động cập nhật "Ngày bắt đầu sử dụng" nếu giá trị hiện tại là N/A và thông báo hoàn tất cho các bên liên quan.

---

#### 4.2.4. Hủy yêu cầu nhập kho

Quy trình hủy yêu cầu nhập kho cho phép hủy các yêu cầu đã được tạo nhưng chưa hoàn thành, với điều kiện yêu cầu phải có trạng thái khác "Đã nhập kho".

##### 4.2.4.1. Thông số kỹ thuật giao diện người dùng

![5.3.1a B5](images/5_3_1a_B5_image7.png)

**Các bước thực hiện quy trình:**
1. **Nhập thông tin tìm kiếm yêu cầu**: Actor nhập thông tin để tìm yêu cầu cần hủy
2. **Liệt kê kết quả tìm kiếm**: Hệ thống hiển thị danh sách yêu cầu phù hợp
3. **Chọn yêu cầu cần xử lý**: Actor lựa chọn yêu cầu cụ thể
4. **Decision point**: Actor quyết định "Hủy" hoặc "Thoát"
   - Nếu chọn "Thoát": Quy trình kết thúc và chuyển về "bước 3"
   - Nếu chọn "Hủy": Tiếp tục các bước xử lý
5. **Nhập lý do hủy**: Actor nhập lý do hủy yêu cầu
6. **Cập nhật trạng thái yêu cầu**: Hệ thống cập nhật trạng thái thành "đã hủy"
7. **Unlock tài sản**: Hệ thống mở khóa các tài sản liên quan
8. **Cập nhật tasklist**: Hệ thống cập nhật danh sách công việc
9. **Thông báo cho End user**: Hệ thống gửi thông báo kết quả

##### 4.2.4.2. Thông số kỹ thuật chi tiết

Giao diện hủy yêu cầu nhập kho với các bộ lọc tìm kiếm và hiển thị thông tin chi tiết trước khi hủy.

**Bảng tìm kiếm yêu cầu:**

| Field name VN | M/O | Field type | Editable | Max length | Operator | Action |
|---------------|-----|------------|----------|------------|----------|---------|
| Số yêu cầu | O | Text | Y | 20 | User | Input |
| Ngày tạo | O | Date | Y | 20 | User | Input |
| Tiêu đề | O | Text | Y | 150 | User | Input |
| Người tạo | O | List | Y | 20 | User | Select |
| Trạng thái yêu cầu | O | List | Y | 20 | User | Select |

**Bảng thông tin kho nhập:**

| Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|---------------|-----|------------|----------|------------|-------------|-----------|
| Tên kho | M | List | Y | 50 | | |
| Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

Sau khi hủy, hệ thống tự động unlock tài sản, cập nhật trạng thái yêu cầu thành "Đã hủy" và gửi thông báo cho các bên liên quan.

---

#### 4.2.5. Phê duyệt yêu cầu cấp tài sản

Quy trình phê duyệt yêu cầu cấp tài sản được thực hiện bởi Asset Manager (AM) để kiểm soát và phê duyệt các yêu cầu cấp tài sản trước khi chuyển sang [tạo yêu cầu xuất kho](#426-tạo-yêu-cầu-xuất-kho).

##### 4.2.5.1. Thông số kỹ thuật giao diện người dùng

![5.4.0a A4](images/5_4_0a_A4_image8.png)

**Các bước thực hiện quy trình:**
1. **Nhập thông tin tìm kiếm yêu cầu** - Form nhập liệu để tìm kiếm
2. **Hiển thị kết quả tìm kiếm** - Danh sách kết quả
3. **Chọn yêu cầu cần xử lý** - Lựa chọn từ danh sách

**Điểm quyết định** với hai nhánh:
1. **Nhánh "Từ chối"**: Kết thúc tại node "Phê duyệt" và dừng quy trình
2. **Nhánh "Tự chọn"**: Tiếp tục với chuỗi các bước xử lý

**Chuỗi xử lý khi chấp nhận:**
- **Bước 4**: "Nhập lý do từ chối" 
- **Bước 5**: "Cập nhật trạng thái yêu cầu"
- **Bước 6**: "Unlock tài sản" 
- **Bước 7**: "Cập nhật tasklist"
- **Bước 8**: "Thông báo cho AMP"

##### 4.2.5.2. Thông số kỹ thuật chi tiết

Asset Manager có thể tìm kiếm yêu cầu cấp tài sản, xem chi tiết thông tin và quyết định phê duyệt hoặc từ chối.

**Bảng tìm kiếm yêu cầu:**

| Operator | Field name VN | M/O | Field type | Editable | Max length |
|----------|---------------|-----|------------|----------|------------|
| User | Mã yêu cầu | M | Text | Y | 20 |
| User | Tiêu đề | M | Text | Y | 150 |
| User | Người tạo | M | List | Y | 20 |
| User | Trạng thái | M | List | Y | 20 |
| User | Ngày tạo | M | Date | Y | 20 |
| User | Loại cấp tài sản | M | List | Y | 100 |

**Bảng thông tin đơn vị nhận:**

| Operator | Action | Field name VN | M/O | Max length | Default value | Data source | Data rule |
|----------|---------|---------------|-----|------------|---------------|-------------|-----------|
| System/User | Display/Search/Select | Tên Người nhận | M | 50 | = Người khởi tạo | OMS | |
| System | Display | Tên ĐVKD/ Phòng ban HO | M | 50 | | OMS | Tự động nhận diện, hiển thị tên đơn vị Người khởi tạo |
| System | Display | Địa chỉ nhận | M | 150 | | OMS | Tự động nhận diện, hiển thị Khối theo Người khởi tạo |
| System/User | Display/Input | Điện thoại di động | M | 50 | | OMS | Tự động nhận diện, hiển thị số điện thoại của Người khởi tạo |

AM có thể add/delete file do người nhận đính kèm nhưng không được delete file đính kèm bởi người khởi tạo. Khi từ chối, hệ thống tự động unlock asset và thông báo cho AMP xử lý tiếp.

---

#### 4.2.6. Tạo yêu cầu xuất kho

Quy trình tự động tạo yêu cầu xuất kho khi có phiếu cấp tài sản được phê duyệt, hệ thống sẽ copy thông tin từ yêu cầu gốc và chuyển sang [tiếp nhận yêu cầu xuất kho](#427-xuất-kho-từ-cấp-tài-sản---tiếp-nhận-yêu-cầu-xuất-kho).

##### 4.2.6.1. Thông số kỹ thuật giao diện người dùng

![5.4.1a. B5](images/5_4_1a__B5_image9.png)

**Các bước thực hiện quy trình:**
1. System khởi tạo → Tạo yêu cầu xuất kho
2. Cập nhật trạng thái yêu cầu 
3. Cập nhật tasklist
4. Thông báo cho WK
5. Chuyển sang sub-process [Tiếp nhận yêu cầu xuất kho](#427-xuất-kho-từ-cấp-tài-sản---tiếp-nhận-yêu-cầu-xuất-kho)

**Luồng công việc:** Quy trình tuần tự (sequential), mỗi bước hoàn thành sẽ kích hoạt bước tiếp theo, đảm bảo tính nhất quán trong xử lý yêu cầu xuất kho.

##### 4.2.6.2. Thông số kỹ thuật chi tiết

Hệ thống tự động tạo yêu cầu xuất kho với số yêu cầu theo format XK.YY.xxxx và copy toàn bộ thông tin từ phiếu cấp gốc.

**Bảng thông tin chung:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max Length | Format | Default | Data Rule |
|--------|----------|---------|------------|-----|------|----------|------------|---------|---------|-----------|
| Số yêu cầu | System | Display | Số yêu cầu | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Ngày tạo | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | System | Input | Tiêu đề | O | Text | Y | 150 | | | =Tiêu đề RQ Cấp/Thanh lý |

**Bảng cập nhật trạng thái:**

| Đối tượng | Action | Trạng thái mới |
|-----------|---------|----------------|
| RQ Cấp tài sản/RQ Thanh lý | Update | Đã xác nhận/Đã cập nhật kết quả thanh lý/Đã phê duyệt kết quả thanh lý |
| RQ Xuất kho | Update | Chờ xuất kho |
| Tasklist AM | Update | Đã xử lý |
| Tasklist WK | Update | Cần xử lý |
| Tasklist AMP | Update | Đã xử lý |

---

#### 4.2.7. Xuất kho từ cấp tài sản - Tiếp nhận yêu cầu xuất kho

Quy trình tiếp nhận và xử lý yêu cầu xuất kho từ cấp tài sản với hai luồng chính: từ chối hoặc đồng ý yêu cầu.

##### 4.2.7.1. Thông số kỹ thuật giao diện người dùng

![5.4.2a. B5](images/5_4_2a__B5_image10.png)

**Các bước thực hiện quy trình:**
1. **Khởi tạo**: Nhập thông tin tìm kiếm yêu cầu (điểm bắt đầu màu xanh)
2. **Tìm kiếm**: Hiển thị kết quả tìm kiếm 
3. **Lựa chọn**: Chọn yêu cầu cần xử lý
4. **Phân luồng**: Điểm quyết định với hai hướng:
   - **Luồng từ chối**: Cập nhật trạng thái yêu cầu → Cập nhật tasklist → Thông báo cho Warehouse Manager → Kết thúc
   - **Luồng đồng ý**: Cập nhật trạng thái yêu cầu → Unlock tài sản → Cập nhật tasklist → Thông báo cho AMP → Kết thúc

##### 4.2.7.2. Thông số kỹ thuật chi tiết

Warehouse Keeper tiếp nhận yêu cầu xuất kho và có thể từ chối hoặc đồng ý. Hệ thống tự động ẩn nút "Từ chối" nếu yêu cầu xuất kho xuất phát từ yêu cầu thanh lý.

**Bảng thông tin tìm kiếm yêu cầu:**

| STT | Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|-----|----------|--------|---------------|-----|------------|----------|------------|
| WK | User | Input | Mã yêu cầu | M | Text | Y | 20 |
| WK | User | Input | Tiêu đề | M | Text | Y | 150 |
| WK | User | Select | Người tạo | M | List | Y | 20 |
| WK | User | Select | Trạng thái | M | List | Y | 20 |
| WK | User | Input | Ngày tạo | M | Date | Y | 20 |

**Bảng thông tin đầu mối nhận hàng:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|---------|---------------|-----|------------|----------|------------|
| User | Input | Đầu mối | M | Text | Y | 50 |
| User | Input | Số điện thoại | M | Number | Y | 52 |
| User | Input | Thời gian bàn giao | O | Date | Y | 50 |
| User | Input | Ghi chú | M | Text | Y | 150 |

Khi đồng ý, hệ thống chuyển trạng thái sang "Chờ xác nhận" và thông báo cho Warehouse Manager để xử lý [phê duyệt xuất kho](#428-xuất-kho-từ-cấp-tài-sản---phê-duyệt-yêu-cầu-xuất-kho).

---

#### 4.2.8. Xuất kho từ cấp tài sản - Phê duyệt yêu cầu xuất kho

Quy trình phê duyệt yêu cầu xuất kho tài sản từ kho bởi Warehouse Manager với hai luồng xử lý chính.

##### 4.2.8.1. Thông số kỹ thuật giao diện người dùng

![5.4.3a. B5](images/5_4_3a__B5_image11.png)

**Các bước thực hiện quy trình:**
1. **Luồng từ chối** (nhánh trên): Từ chối → Cập nhật trạng thái yêu cầu → Unlock tài sản → Cập nhật tasklist → Thông báo cho AMD/WK → Kết thúc
2. **Luồng duyệt** (nhánh dưới): Duyệt → Cập nhật trạng thái yêu cầu → Cập nhật tasklist → Thông báo cho BU user/WK → Xuất hàng → Chuyển đến [màn hình nhận tài sản](#429-xuất-kho-từ-cấp-tài-sản---nhận-tài-sản)

##### 4.2.8.2. Thông số kỹ thuật chi tiết

Warehouse Manager có thể tìm kiếm và phê duyệt yêu cầu xuất kho với giao diện hiển thị đầy đủ thông tin tài sản và kho.

**Bảng tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Mã yêu cầu | M | Text | Y | 20 |
| User | Input | Tiêu đề | M | Text | Y | 150 |
| User | Select | Người tạo | M | List | Y | 20 |
| User | Select | Trạng thái | M | List | Y | 20 |
| User | Input | Ngày tạo | M | Date | Y | 20 |
| User | Select | Loại cấp tài sản | M | List | Y | 100 |

**Bảng thông tin kho xuất:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | = Thông tin kho trên RQ cấp tài sản |
| System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | |
| System | Display | Quản lý kho | M | Text | N | 50 | OMS | |

Hệ thống ẩn nút "Từ chối" nếu yêu cầu xuất kho xuất phát từ yêu cầu thanh lý. Khi từ chối, hệ thống unlock tài sản và thông báo cho AMP. Khi phê duyệt, chuyển sang [nhận tài sản](#429-xuất-kho-từ-cấp-tài-sản---nhận-tài-sản).

---

#### 4.2.9. Xuất kho từ Cấp tài sản - Nhận tài sản

Quy trình cuối cùng trong chuỗi xuất kho từ cấp tài sản, cho phép người dùng cuối nhận tài sản từ kho.

##### 4.2.9.1. Thông số kỹ thuật giao diện người dùng

![5.4.4a B6](images/5_4_4a_B6_image12.png)

**Các bước thực hiện quy trình:**

**Luồng chính (trên):**
1. Từ chối → Nhập lý do từ chối → Cập nhật trạng thái yêu cầu → Unlock tài sản → Cập nhật tasklist → Thông báo cho AMP/VK

**Luồng phụ (dưới):**  
1. Nhập thông tin tìm kiếm yêu cầu → Hiển thị kết quả tìm kiếm → Chọn yêu cầu cần xử lý
2. Xác nhận → Cập nhật trạng thái yêu cầu → Unlock tài sản → Cập nhật tasklist → Thông báo cho VK và AMP

##### 4.2.9.2. Thông số kỹ thuật chi tiết

BU user thực hiện nhận tài sản từ kho với khả năng xác nhận hoặc từ chối nhận hàng.

**Bảng tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Mã yêu cầu | M | Text | Y | 20 |
| User | Input | Tiêu đề | M | Text | Y | 150 |
| User | Select | Người tạo | M | List | Y | 20 |
| User | Select | Trạng thái | M | List | Y | 20 |
| User | Input | Ngày tạo | M | Date | Y | 20 |

**Bảng thông tin đầu mối nhận hàng:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|---------|---------------|-----|------------|----------|------------|
| User | Input | Đầu mối | M | Text | Y | 50 |
| User | Input | Số điện thoại | M | Number | Y | 52 |
| User | Input | Thời gian bàn giao | O | Date | Y | 50 |

Hệ thống tự động unlock tài sản khi bị từ chối để có thể sử dụng cho yêu cầu khác và cập nhật tasklist, gửi email thông báo cho các bên liên quan.

---

#### 4.2.10. Hủy Yêu cầu Xuất kho

Quy trình hủy yêu cầu xuất kho cho phép hủy các yêu cầu đã được tạo thành công và có trạng thái khác "Đã xác nhận".

##### 4.2.10.1. Thông số kỹ thuật giao diện người dùng

![5.5.1a B5](images/5_5_1a_B5_image13.png)

**Các bước thực hiện quy trình:**
1. **Nhập thông tin tìm kiếm yêu cầu** - Bước đầu để xác định yêu cầu cần hủy
2. **Tìm kiến qua tìm kiếm** - Thực hiện tìm kiếm trong hệ thống
3. **Chọn yêu cầu cần xử lý** - Lựa chọn yêu cầu cụ thể từ kết quả tìm kiếm
4. **Decision point**: Hủy/Thoát - Người dùng quyết định có thực hiện hủy hay không
5. **Nhập lý do hủy** - Bước bắt buộc khi chọn hủy
6. **Cập nhật trạng thái yêu cầu** - Hệ thống cập nhật status
7. **Unlock tài sản** - Giải phóng tài sản đã được lock cho yêu cầu
8. **Cập nhật tasklist** - Cập nhật danh sách công việc
9. **Thông báo cho WK** - Gửi thông báo về việc hủy yêu cầu

**Luồng công việc:**
- **Luồng chính (Hủy)**: Từ Start → các bước xử lý → Decision "Hủy" → các bước cập nhật → End
- **Luồng phụ (Thoát)**: Từ Decision "Thoát" → trực tiếp đến End với ghi chú "Về bước 3"

##### 4.2.10.2. Thông số kỹ thuật chi tiết

**Bảng tìm kiếm yêu cầu:**

| STT | Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|-----|----------|---------|---------------|-----|------------|----------|------------|
| 1 | User | Input | Mã yêu cầu | M | Text | Y | 20 |
| 2 | User | Input | Tiêu đề | M | Text | Y | 150 |
| 3 | User | Select | Người tạo | M | List | Y | 20 |
| 4 | User | Select | Trạng thái | M | List | Y | 20 |
| 5 | User | Input | Ngày tạo | M | Date | Y | 20 |

**Yêu cầu nghiệp vụ:**
- Điều kiện hủy: Yêu cầu xuất kho phải có trạng thái khác "Đã xác nhận"
- Lý do hủy là trường bắt buộc (M) với độ dài tối đa 150 ký tự
- Ẩn nút "Từ chối" đối với RQ xuất kho liên kết với RQ thanh lý
- Hệ thống phải unlock tài sản và trả về trạng thái trước khi thanh lý

---

#### 4.2.11. Tạo yêu cầu điều chuyển tài sản giữa các kho

Quy trình tạo yêu cầu điều chuyển tài sản giữa các kho trong hệ thống quản lý kho.

##### 4.2.11.1. Thông số kỹ thuật giao diện người dùng

![5.6.1a B6](images/5_6_1a_B6_image14.png)

**Các bước thực hiện quy trình:**
1. **Khởi tạo**: Tạo yêu cầu điều chuyển kho với thông tin đính kèm
2. **Quyết định**: Người dùng chọn "Gửi" để tiếp tục hoặc "Thoát" để hủy
3. **Lock tài sản**: Khóa tài sản cần điều chuyển
4. **Cập nhật trạng thái**: Cập nhật trạng thái yêu cầu trong hệ thống
5. **Thông báo**: Thông báo và gán người phê duyệt
6. **Cập nhật tasklist**: Cập nhật danh sách công việc
7. **Thông báo Warehouse Manager**: Gửi thông báo cho người quản lý kho
8. **Chuyển tiếp**: Chuyển sang quy trình [Phê duyệt yêu cầu điều chuyển kho](#4212-phê-duyệt-yêu-cầu-điều-chuyển-kho)

##### 4.2.11.2. Thông số kỹ thuật chi tiết

**Bảng thông tin chung:**

| STT | Tab/Section | Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Format | Default Value | Data Rule |
|-----|-------------|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| 1 | Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| 2 | | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| 3 | | User | Input | Tiêu đề | O | Text | Y | 150 | | | |

**Bảng thông tin kho:**

| Section | Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Data Source | Data Rule |
|---------|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| Thông tin kho đi | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | |
| | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Thông tin kho nhập | User | Select | Tên kho | M | List | N | 50 | | |
| | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

Giao diện cho phép tìm kiếm và chọn tài sản cần điều chuyển với nhiều tiêu chí lọc, nhập thông tin đầu mối giao hàng và đính kèm hồ sơ.

---

#### 4.2.12. Phê duyệt yêu cầu điều chuyển kho

Quy trình phê duyệt yêu cầu điều chuyển tài sản giữa các kho trong hệ thống quản lý tài sản.

##### 4.2.12.1. Thông số kỹ thuật giao diện người dùng

![5.6.2a B5](images/5_6_2a_B5_image15.png)

**Các bước thực hiện quy trình:**
1. **Bắt đầu**: Nhập thông tin kiểm yêu cầu
2. **Kiểm tra**: Hiển thị kết quả tìm kiếm → Chọn yêu cầu cần xử lý
3. **Quyết định**: Gateway phê duyệt với 3 hướng (Phê duyệt/Từ chối/Thoát)
4. **Luồng phê duyệt**: Cập nhật trạng thái → Cập nhật tasklist → Thông báo → Cập nhật kho → Bàn giao tài sản
5. **Luồng từ chối**: Cập nhật trạng thái yêu cầu → Unlock tài sản → Cập nhật tasklist → Thông báo → Kết thúc

##### 4.2.12.2. Thông số kỹ thuật chi tiết

**Bảng tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |

**Bảng thông tin kho đi:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|----------|---------|---------------|-----|------------|----------|------------|-------------|-----------|
| System | Display | Tên kho | M | List | N | 50 | | |
| System | Display | Địa chỉ kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

**Bảng thông tin kho nhập:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|----------|---------|---------------|-----|------------|----------|------------|-------------|-----------|
| User | Select | Tên kho | M | List | N | 50 | | |
| System | Display | Địa chỉ kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

Khi phê duyệt, hệ thống tự động tạo biên bản điều chuyển, cập nhật thông tin kho của tài sản và thông báo cho warehouse keeper của cả kho đi và kho đến.

---

## 5. Assumptions & Constraints

### Assumptions (Giả định):

1. **Kết nối hệ thống**: OMS, EMS và ITSM sẽ cung cấp API ổn định cho tích hợp
2. **Dữ liệu hiện tại**: Database FAM hiện tại có chất lượng dữ liệu tốt và không cần data cleansing lớn
3. **Người dùng**: Staff được đào tạo đầy đủ về quy trình mới trước khi go-live
4. **Hạ tầng**: Hệ thống có đủ capacity để xử lý khối lượng workflow tăng thêm

### Constraints (Ràng buộc):

1. **Thời gian**: Dự án phải hoàn thành trong Q2/2024
2. **Ngân sách**: Không được vượt quá ngân sách đã phê duyệt
3. **Tích hợp**: Không được thay đổi API của các hệ thống hiện tại (OMS, EMS, ITSM)
4. **Downtime**: Thời gian downtime khi deploy không được vượt quá 4 tiếng
5. **Phân quyền**: Phải tuân thủ security policy hiện tại của tổ chức

---

## 6. Dependencies

### Hệ thống phụ thuộc:

1. **OMS (Organization Management System)**
   - Cung cấp thông tin orgchart, thông tin kho, quản lý kho
   - Đảm bảo đồng bộ khi có thay đổi cơ cấu tổ chức

2. **EMS (Enterprise Management System)**  
   - Đồng bộ thông tin tài sản, tiêu đề PO, thời gian bảo hành
   - Cập nhật thông tin khi PO được phê duyệt

3. **ITSM (IT Service Management)**
   - Nhận yêu cầu sửa chữa từ FAM (giai đoạn sau)
   - Feedback kết quả xử lý về FAM

### Phụ thuộc nội bộ:

1. **Database Migration**: Hoàn thành trước khi phát triển các chức năng mới
2. **User Management**: Cập nhật role và permission cho các chức năng mới
3. **Testing Environment**: Sẵn sàng trước khi bắt đầu integration testing

---

## 7. Acceptance Criteria

### Dashboard Tài sản:
- [ ] Hiển thị đúng 4 KPI với công thức tính toán chính xác
- [ ] 5 loại biểu đồ hoạt động tương tác (hover, click)
- [ ] Bộ lọc đồng bộ với OMS và hoạt động real-time
- [ ] Chức năng export Excel hoạt động đúng
- [ ] Loại trừ đúng tài sản "Đã thanh lý" và "Vô hiệu hóa"

### Module Quản lý Kho:
- [ ] Tất cả 8 quy trình workflow hoạt động end-to-end
- [ ] Tự động tạo yêu cầu liên kết giữa các quy trình
- [ ] Chức năng hủy cascade hoạt động đúng
- [ ] Email notification gửi cho đúng vai trò tại đúng thời điểm
- [ ] Asset locking/unlocking mechanism hoạt động chính xác
- [ ] Tasklist cập nhật đúng trạng thái cho từng vai trò

### Tích hợp:
- [ ] Đồng bộ OMS khi orgchart thay đổi
- [ ] Đồng bộ tiêu đề PO và thời gian bảo hành từ EMS
- [ ] API integration hoạt động ổn định với 99.9% uptime

### Performance:
- [ ] Dashboard load trong vòng 3 giây
- [ ] Workflow response time < 2 giây
- [ ] Hệ thống hỗ trợ 200 concurrent users

---

## 8. Glossary

| Thuật ngữ | Định nghĩa |
|-----------|------------|
| **AMP** | Asset Management Personnel - Nhân viên quản lý tài sản |
| **AM** | Asset Manager - Quản lý tài sản |  
| **WM** | Warehouse Manager - Quản lý kho |
| **WK** | Warehouse Keeper - Thủ kho |
| **BU** | Business Unit - Đơn vị kinh doanh |
| **OMS** | Organization Management System - Hệ thống quản lý tổ chức |
| **EMS** | Enterprise Management System - Hệ thống quản lý doanh nghiệp |
| **ITSM** | IT Service Management - Quản lý dịch vụ IT |
| **CAT1** | Category 1 - Phân loại tài sản cấp 1 |
| **LOV** | List of Values - Danh sách giá trị |
| **Tasklist** | Danh sách công việc cần xử lý của từng vai trò |
| **Asset Locking** | Cơ chế khóa tài sản để tránh xung đột trong quy trình |
| **Workflow** | Quy trình công việc có các bước xử lý tuần tự |
| **Dashboard KPI** | Các chỉ số hiệu suất chính hiển thị trên dashboard |
| **Cascade Cancel** | Hủy liên tục các yêu cầu liên quan khi hủy yêu cầu gốc |

---

## Phụ lục: Hình ảnh bổ sung

Các hình ảnh sau được trích xuất từ tài liệu gốc nhưng chưa được đặt vào nội dung chính:

![filename](images/filename)



---

*Generated by Claude Sonnet 4.5 from 37 sheet summaries*
*Headings: 38 | Internal Links: 46 | Images: 16*

*⚠️ Link validation warnings - some links may need manual review*
*✅ All image tokens converted successfully*
