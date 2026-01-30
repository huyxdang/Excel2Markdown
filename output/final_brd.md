# Tài liệu Yêu cầu Nghiệp vụ (BRD)
## Hệ thống Quản lý Tài sản FAM - Wave 4

---

## 1. Table of Contents

- [1. Table of Contents](#1-table-of-contents)
- [2. Executive Summary](#2-executive-summary)
- [3. Project Scope & Objectives](#3-project-scope--objectives)
- [4. Stakeholders](#4-stakeholders)
- [5. Business Requirements](#5-business-requirements)
  - [5.1. FAM UPGRADE - WAVE 4](#51-fam-upgrade---wave-4)
  - [5.2. Dashboard Tài Sản](#52-dashboard-tài-sản)
  - [5.3. Module Quản Lý Kho](#53-module-quản-lý-kho)
    - [5.3.1. Điều chuyển về kho - Tạo yêu cầu nhập kho](#531-điều-chuyển-về-kho---tạo-yêu-cầu-nhập-kho)
    - [5.3.2. Điều chuyển về kho - Phê duyệt yêu cầu nhập kho](#532-điều-chuyển-về-kho---phê-duyệt-yêu-cầu-nhập-kho)
    - [5.3.3. Điều chuyển về kho - Xác nhận nhập kho](#533-điều-chuyển-về-kho---xác-nhận-nhập-kho)
    - [5.3.4. Nhập kho thủ công - Tạo yêu cầu](#534-nhập-kho-thủ-công---tạo-yêu-cầu)
    - [5.3.5. Nhập kho thủ công - Phê duyệt yêu cầu](#535-nhập-kho-thủ-công---phê-duyệt-yêu-cầu)
    - [5.3.6. Nhập kho thủ công - Xác nhận nhập kho](#536-nhập-kho-thủ-công---xác-nhận-nhập-kho)
    - [5.3.7. Hủy yêu cầu nhập kho](#537-hủy-yêu-cầu-nhập-kho)
  - [5.4. Xuất kho từ cấp tài sản](#54-xuất-kho-từ-cấp-tài-sản)
    - [5.4.1. Phê duyệt yêu cầu cấp tài sản](#541-phê-duyệt-yêu-cầu-cấp-tài-sản)
    - [5.4.2. Tạo yêu cầu xuất kho](#542-tạo-yêu-cầu-xuất-kho)
    - [5.4.3. Tiếp nhận yêu cầu xuất kho](#543-tiếp-nhận-yêu-cầu-xuất-kho)
    - [5.4.4. Phê duyệt yêu cầu xuất kho](#544-phê-duyệt-yêu-cầu-xuất-kho)
    - [5.4.5. Nhận tài sản](#545-nhận-tài-sản)
    - [5.4.6. Hủy yêu cầu xuất kho](#546-hủy-yêu-cầu-xuất-kho)
  - [5.5. Điều chuyển tài sản giữa các kho](#55-điều-chuyển-tài-sản-giữa-các-kho)
    - [5.5.1. Tạo yêu cầu điều chuyển kho](#551-tạo-yêu-cầu-điều-chuyển-kho)
    - [5.5.2. Phê duyệt yêu cầu điều chuyển kho](#552-phê-duyệt-yêu-cầu-điều-chuyển-kho)
  - [5.6. Quản lý trạng thái (Status)](#56-quản-lý-trạng-thái-status)
  - [5.7. Quản lý Tasklist](#57-quản-lý-tasklist)
- [6. Assumptions & Constraints](#6-assumptions--constraints)
- [7. Dependencies](#7-dependencies)
- [8. Acceptance Criteria](#8-acceptance-criteria)
- [9. Glossary](#9-glossary)

---

## 2. Executive Summary

Dự án FAM UPGRADE - WAVE 4 là giai đoạn nâng cấp quan trọng của hệ thống Quản lý Tài sản Cố định (Fixed Asset Management - FAM), tập trung vào việc cải thiện và mở rộng các chức năng quản lý kho, dashboard tài sản, và tích hợp với các hệ thống liên quan.

**Các sản phẩm chính bao gồm:**

1. **[Dashboard Tài sản](#52-dashboard-tài-sản)**: Giao diện tổng quan trực quan hóa dữ liệu tài sản với khả năng customize theo nhiều tiêu chí, hỗ trợ đưa ra quyết định nhanh chóng.

2. **[Module Quản Lý Kho](#53-module-quản-lý-kho)**: Module hoàn toàn mới cho phép quản lý xuất-nhập kho tài sản, bao gồm các quy trình:
   - Điều chuyển tài sản về kho
   - Nhập kho thủ công
   - Hủy yêu cầu nhập kho

3. **[Xuất kho từ cấp tài sản](#54-xuất-kho-từ-cấp-tài-sản)**: Quy trình tự động tạo yêu cầu xuất kho khi có phê duyệt cấp tài sản hoặc thanh lý.

4. **[Điều chuyển tài sản giữa các kho](#55-điều-chuyển-tài-sản-giữa-các-kho)**: Cho phép di chuyển tài sản từ kho này sang kho khác với quy trình phê duyệt đầy đủ.

5. **Tích hợp hệ thống**: Đồng bộ dữ liệu với OMS (Organization Management System) và EMS (Enterprise Management System).

**Mục tiêu dự án:**
- Tự động hóa quy trình quản lý kho tài sản
- Cung cấp khả năng theo dõi và báo cáo real-time
- Đảm bảo tính nhất quán dữ liệu giữa các hệ thống
- Nâng cao trải nghiệm người dùng với giao diện trực quan

---

## 3. Project Scope & Objectives

### 3.1. Trong phạm vi (In Scope)

| Nhóm | Loại | Chi tiết | Mức ưu tiên |
|------|------|----------|-------------|
| Tài sản | Enhancement | Dashboard tài sản hiển thị theo hướng visualize; có thể customize theo nhiều tiêu chí | 1 |
| Tài sản | Enhancement | Ẩn hiện tùy chọn tài sản vô hiệu hóa khỏi danh sách tài sản | 2 |
| Tài sản | Enhancement | Đổi vị trí hiển thị một số cột trong danh sách tài sản | 2 |
| Cấp tài sản | Enhancement | Upload phiếu cấp tài sản theo danh sách | 3 |
| Cấp tài sản | Enhancement | Auto xác nhận phiếu cấp tài sản sau 20 ngày | 2 |
| Integration | Enhancement | Auto đồng bộ OMS khi orgchart thay đổi | 2 |
| Integration | Enhancement | Đồng bộ tiêu đề PO từ EMS sang FAM | 2 |
| Integration | Enhancement | Đồng bộ thông tin thời gian từ EMS | 2 |
| Thanh lý | Enhancement | Bổ sung luồng phê duyệt cho ATM | 3 |
| Module kho | New launch | Xuất - nhập kho tài sản | 1 |
| Module sửa chữa | New launch | Tạo yêu cầu sửa chữa tài sản tích hợp ITSM | 4 |

### 3.2. Ngoài phạm vi (Out of Scope)

- Module sửa chữa tài sản chi tiết (Ưu tiên 4 - cần clear quy trình)
- Tích hợp với cổng hỗ trợ chi nhánh trên intranet (pending)
- Báo cáo tài chính và khấu hao tài sản
- Quản lý bảo hiểm tài sản

### 3.3. Mục tiêu dự án

1. **Tự động hóa**: Giảm 60% thao tác thủ công trong quy trình xuất-nhập kho
2. **Minh bạch**: 100% yêu cầu được theo dõi trạng thái real-time
3. **Tích hợp**: Đồng bộ dữ liệu với OMS và EMS trong vòng 5 phút
4. **Trải nghiệm**: Dashboard cung cấp insights trong 3 click
5. **Kiểm soát**: Quy trình phê duyệt đa cấp cho mọi thay đổi tài sản

---

## 4. Stakeholders

| Vai trò | Mô tả | Trách nhiệm chính |
|---------|-------|-------------------|
| **AMP** (Asset Management Personnel) | Nhân viên quản lý tài sản | Tạo yêu cầu, xử lý điều chuyển, quản lý tasklist |
| **AM** (Asset Manager) | Quản lý tài sản | Phê duyệt yêu cầu cấp tài sản, giám sát quy trình |
| **BU User** | Người dùng đơn vị kinh doanh | Tạo yêu cầu, xác nhận nhận tài sản |
| **BU Head/BU Mgr** | Trưởng đơn vị kinh doanh | Phê duyệt yêu cầu từ đơn vị |
| **WK** (Warehouse Keeper) | Thủ kho | Thực hiện xuất/nhập kho, xác nhận vật lý |
| **Warehouse Mgr** | Quản lý kho | Phê duyệt yêu cầu xuất/nhập kho |
| **Checker** | Người kiểm soát | Kiểm soát yêu cầu thanh lý |
| **Approver** | Người phê duyệt | Phê duyệt các yêu cầu theo phân quyền |
| **Initiator** | Người khởi tạo | Tạo và theo dõi yêu cầu |
| **System** | Hệ thống tự động | Tự động tạo yêu cầu, cập nhật trạng thái, gửi thông báo |

---

## 5. Business Requirements

### 5.1. FAM UPGRADE - WAVE 4

Đây là tổng quan các yêu cầu nâng cấp hệ thống FAM trong Wave 4, được phân loại theo nhóm chức năng và mức độ ưu tiên.

| STT | Nhóm | Loại | Chi tiết | Mức ưu tiên | Ghi chú |
|-----|------|------|----------|-------------|---------|
| 1 | Tài sản | Enhancement | Dashboard tài sản hiển thị theo hướng visualize; có thể customize theo nhiều tiêu chí | 1 | Login vào là nhìn thấy luôn. Cần liệt kê rõ ràng role |
| 2 | Tài sản | Enhancement | Ẩn hiện tùy chọn tài sản vô hiệu hóa khỏi danh sách tài sản | 2 | |
| 3 | Tài sản | Enhancement | Đổi vị trí hiển thị một số cột trong danh sách tài sản | 2 | |
| 4 | Cấp tài sản | Enhancement | Upload phiếu cấp tài sản theo danh sách | 3 | |
| 5 | Cấp tài sản | Enhancement | Auto xác nhận phiếu cấp tài sản sau 20 ngày kể từ khi request bàn giao tài sản được tạo, user không có phản hồi | 2 | |
| 6 | Integration | Enhancement | Auto đồng bộ OMS khi orgchart thay đổi | 2 | |
| 7 | Integration | Enhancement | Đồng bộ tiêu đề PO từ EMS sang FAM | 2 | |
| 8 | Integration | Enhancement | Tài sản từ EMS, cột "Thông tin thời gian đưa vào sử dụng, Thời gian bắt đầu bảo hành" = thời gian PO được phê duyệt | 2 | |
| 9 | Thanh lý | Enhancement | Bổ sung luồng phê duyệt cho ATM | 3 | Thêm thông tin as is và to be |
| 10 | Modul kho | New launch | Xuất - nhập kho tài sản. Tiếp nhận yêu cầu xuất - nhập kho từ yêu cầu cấp ts, thanh lý tài sản, điều chuyển ts về kho | 1 | |
| 11 | Modul sửa chữa tài sản | New launch | Tạo yêu cầu sửa chữa tài sản thực hiện trên FAM => Hệ thống tạo yêu cầu (gửi link) sang Hệ thống ITSM và Cổng hỗ trợ chi nhánh trên intranet | 4 | Cần Clear qui trình |

**Liên kết chi tiết:**
- Yêu cầu Dashboard tài sản: Xem [5.2. Dashboard Tài Sản](#52-dashboard-tài-sản)
- Module kho: Xem [5.3. Module Quản Lý Kho](#53-module-quản-lý-kho)

---

### 5.2. Dashboard Tài Sản

Dashboard Tài sản cung cấp giao diện tổng quan và trực quan hóa dữ liệu để hỗ trợ đưa ra quyết định nhanh chóng về quản lý tài sản.

#### 5.2.1. Mục tiêu và Phạm vi

**Mục tiêu:**
- Cung cấp giao diện tổng quan trực quan hóa dữ liệu tài sản
- Hỗ trợ đưa ra quyết định nhanh chóng
- Hiển thị biến động tài sản theo thời gian
- Theo dõi tài sản hết bảo hành và thời gian sử dụng > 3, 5 năm

**Phạm vi dữ liệu:**
- Dữ liệu tài sản theo phòng ban orgchart
- Trạng thái tài sản
- Biến động theo thời gian
- Tỷ lệ sử dụng
- Tài sản hết bảo hành hoặc có thời gian sử dụng trên 3-5 năm

#### 5.2.2. Đặc tả chi tiết

**Dashboard Tổng quan:**

| STT | Nội dung | Giá trị/Mô tả | Loại biểu đồ | Ghi chú |
|-----|----------|---------------|--------------|---------|
| 1 | Total assets | Count số lượng (All tài sản - Đã thanh lý - Vô hiệu hóa) | - | - |
| 2 | Total value | Sum nguyên giá (All tài sản - Đã thanh lý - Vô hiệu hóa) | - | - |
| 3 | Warranty status | Tỷ lệ % tài sản còn hạn bảo hành/(All tài sản - Vô hiệu hóa - Đã thanh lý) | - | - |
| 4 | Utilization rate | Tỷ lệ % tài sản đang sử dụng/(All tài sản - Vô hiệu hóa - Đã thanh lý) | - | - |

**Bộ lọc dùng chung:**

| STT | Bộ lọc | Loại | Ghi chú |
|-----|--------|------|---------|
| 1 | Vùng | LOV | - |
| 2 | Đơn vị sử dụng | LOV đồng bộ từ OMS | - |
| 3 | CAT 1 | LOV | - |
| 4 | Group name | LOV | - |
| 5 | Asset status | LOV (Không bao gồm Đã thanh lý, Vô hiệu hóa) | - |

**Biểu đồ:**

| STT | Tên biểu đồ | Giá trị | Loại biểu đồ | Ghi chú |
|-----|-------------|---------|--------------|---------|
| 1 | Asset Distribution - Cơ cấu nhóm tài sản theo trạng thái | Nguyên giá | Sunburst (Vòng trong: IT/ADM/CMD, Vòng ngoài: Trạng thái) | Hover hiển thị số lượng và giá trị |
| 2 | Asset Distribution - Cơ cấu theo Vùng, Đơn vị sử dụng | Nguyên giá | Stacked Column | - |
| 3 | Asset Value by Group Name | Nguyên giá | Column | - |
| 4 | Asset Fluctuation Over Time (Month/Year) | Nguyên giá | Line | - |
| 5 | Asset by Time in Use | Số lượng | Scatter | - |

#### 5.2.3. Yêu cầu kỹ thuật

- Biểu đồ tương tác với khả năng hover để xem chi tiết và click để chuyển sang module liên quan
- Bộ lọc đa tiêu chí (phòng ban, nhóm tài sản, trạng thái, thời gian)
- Xuất dữ liệu dashboard ra file Excel
- Tích hợp với hệ thống OMS để đồng bộ dữ liệu đơn vị sử dụng
- Loại bỏ tài sản đã thanh lý và vô hiệu hóa khỏi các tính toán

---

### 5.3. Module Quản Lý Kho

Module Quản Lý Kho là một phần quan trọng của hệ thống FAM Wave 4, bao gồm 6 nhóm quy trình chính:

1. [Điều chuyển nội bộ về kho](#531-điều-chuyển-về-kho---tạo-yêu-cầu-nhập-kho)
2. [Nhập kho thủ công](#534-nhập-kho-thủ-công---tạo-yêu-cầu)
3. [Hủy nhập kho](#537-hủy-yêu-cầu-nhập-kho)
4. [Cấp tài sản từ kho](#54-xuất-kho-từ-cấp-tài-sản)
5. [Thanh lý tài sản từ kho](#54-xuất-kho-từ-cấp-tài-sản)
6. [Điều chuyển giữa các kho](#55-điều-chuyển-tài-sản-giữa-các-kho)

**Đặc điểm chính của quy trình To-be:**
- Tự động hóa nhiều bước xử lý
- Hệ thống tự động tạo yêu cầu nhập/xuất kho khi có xác nhận
- Cơ chế duyệt đa cấp với khả năng từ chối và quay về bước đầu
- Tự động cập nhật trạng thái giữa các yêu cầu liên quan

---

#### 5.3.1. Điều chuyển về kho - Tạo yêu cầu nhập kho

##### 5.3.1.1. Thông số kỹ thuật giao diện người dùng

![5.1.1a B5](images/5_1_1a_B5_image1.png)

**Các bước thực hiện:**
1. Hệ thống tự động tạo yêu cầu nhập kho từ yêu cầu điều chuyển
2. Cập nhật trạng thái yêu cầu điều chuyển thành "Đã xác nhận"
3. Cập nhật trạng thái yêu cầu nhập kho thành "Chờ phê duyệt"
4. Cập nhật tasklist cho AMP và Warehouse Manager
5. Gửi thông báo email cho Warehouse Manager

**Mô tả quy trình:**

Quy trình tạo yêu cầu nhập kho được khởi tạo tự động khi có yêu cầu điều chuyển tài sản về kho được xác nhận. Hệ thống sẽ kế thừa toàn bộ thông tin từ yêu cầu điều chuyển bao gồm thông tin tài sản, chi tiết kho đích và các tệp đính kèm.

Hệ thống quản lý trạng thái lock/unlock tài sản một cách thông minh: khi yêu cầu điều chuyển hoàn thành thì tài sản được unlock khỏi yêu cầu điều chuyển, nhưng ngay lập tức được lock bởi yêu cầu nhập kho mới tạo. Thông tin tài sản sẽ không được cập nhật cho đến khi yêu cầu nhập kho hoàn thành.

**Các bên liên quan:** System (tự động tạo), AMP (nhận tasklist), Warehouse Manager (nhận thông báo và xử lý)

##### 5.3.1.2. Thông số kỹ thuật chi tiết

**Đặc tả trường dữ liệu - Thông tin chung:**

| STT | Tab/Section | Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Format | Default Value | Data Rule |
|-----|-------------|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| 1 | Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| 2 | Thông tin chung | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| 3 | Thông tin chung | System | Display | Tiêu đề | M | Text | N | 150 | | | = Tiêu đề RQ điều chuyển |

**Đặc tả danh sách tài sản:**

| Field Name VN | M/O | Editable | Data Rule |
|---------------|-----|----------|-----------|
| Mã tài sản | M | N | Hiển thị mặc định |
| Tên Tài sản | M | N | Hiển thị mặc định |
| Mô tả TS | M | N | Hiển thị mặc định |
| Trạng thái TS | M | N | Hiển thị mặc định |
| Phân nhóm TS (group name) | M | N | Hiển thị mặc định |
| Nhóm TS (CAT1) | M | N | Hiển thị mặc định |
| Số PO | M | N | Hiển thị mặc định |
| Tên nhà cung cấp | O | N | Ẩn hiện tùy biến |
| Nguyên giá TS (VAT incl) | M | N | Ẩn hiện tùy biến |
| Tên người sử dụng | M | N | Hiển thị mặc định |
| Tên đơn vị | M | N | Hiển thị mặc định |

**Đặc tả thông tin kho và giao hàng:**

| Tab/Section | Field Name VN | M/O | Field Type | Max Length | Data Source | Data Rule |
|-------------|---------------|-----|------------|------------|-------------|-----------|
| Thông tin kho nhập | Tên kho | M | List | 50 | | = Kho trong RQ điều chuyển |
| Thông tin kho nhập | Địa chỉ kho | M | Text | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Thông tin kho nhập | Quản lý kho | M | Text | 50 | OMS | Tự động nhận diện (Tên \| Phòng ban \| Email) |
| Thông tin đầu mối giao hàng | Đầu mối | M | Text | 50 | | = Đầu mối giao hàng trong RQ điều chuyển |
| Thông tin đầu mối giao hàng | Số điện thoại | M | Number | 52 | | |
| Thông tin đầu mối giao hàng | Thời gian bàn giao | O | Date | 50 | | |

**Cập nhật trạng thái và tasklist:**

| Action | Target | Status/Value |
|--------|--------|--------------|
| Update | Trạng thái RQ điều chuyển | Đã xác nhận |
| Update | Trạng thái RQ nhập kho | Chờ phê duyệt |
| Update | Tasklist AMP | Đã xử lý |
| Update | Tasklist WM | Cần xử lý |
| Send | Email notification | Gửi cho Warehouse Manager |

**Liên kết:** Sau khi tạo yêu cầu, quy trình chuyển sang [5.3.2. Phê duyệt yêu cầu nhập kho](#532-điều-chuyển-về-kho---phê-duyệt-yêu-cầu-nhập-kho)

---

#### 5.3.2. Điều chuyển về kho - Phê duyệt yêu cầu nhập kho

##### 5.3.2.1. Thông số kỹ thuật giao diện người dùng

![5.1.2a B6](images/5_1_2a_B6_image2.png)

**Các bước thực hiện:**
1. Warehouse Manager nhập thông tin tìm kiếm yêu cầu
2. Hệ thống hiển thị kết quả tìm kiếm
3. Chọn yêu cầu cần xử lý và xem chi tiết
4. Đưa ra quyết định phê duyệt hoặc từ chối
5. Nếu phê duyệt: Cập nhật trạng thái, tasklist và gửi email
6. Nếu từ chối: Nhập lý do, unlock tài sản, cập nhật trạng thái

**Luồng xử lý:**
- **Luồng phê duyệt:** Cập nhật trạng thái → Cập nhật tasklist → Gửi email → Chuyển sang [5.3.3. Xác nhận nhập kho](#533-điều-chuyển-về-kho---xác-nhận-nhập-kho)
- **Luồng từ chối:** Nhập lý do → Unlock tài sản → Cập nhật trạng thái → Gửi email thông báo

##### 5.3.2.2. Thông số kỹ thuật chi tiết

**Bảng tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Bảng danh sách tài sản nhập kho:**

| Field name VN | M/O | Data rule |
|---------------|-----|-----------|
| Mã tài sản | M | Hiển thị mặc định |
| Tên Tài sản | M | Hiển thị mặc định |
| Mô tả TS | M | Hiển thị mặc định |
| Trạng thái TS | M | Hiển thị mặc định |
| Phân nhóm TS (group name) | M | Hiển thị mặc định |
| Nhóm TS (CAT1) | M | Hiển thị mặc định |
| Số PO | M | Hiển thị mặc định |
| Tên nhà cung cấp | O | Ẩn hiện tùy biến |
| Nguyên giá TS (VAT incl) | M | Ẩn hiện tùy biến |
| Mã TS liên quan | O | Ẩn hiện tùy biến |
| Tên người sử dụng | M | Hiển thị mặc định |
| Tên đơn vị | M | Hiển thị mặc định |
| Mã nhân viên | M | Ẩn hiện tùy biến |
| Đơn vị sử dụng cha | M | Hiển thị mặc định |

**Bảng thông tin kho và đầu mối:**

| Field name VN | M/O | Field type | Max length | Data source | Data rule |
|---------------|-----|------------|------------|-------------|-----------|
| Tên kho | M | List | 50 | | |
| Địa chỉ kho | M | Text | 50 | OMS | Tự động nhận diện theo Tên kho |
| Quản lý kho | M | Text | 50 | OMS | Hiển thị Tên, Phòng ban, Email |
| Đầu mối | M | Text | 50 | | |
| Số điện thoại | M | Number | 52 | | |
| Thời gian bàn giao | O | Date | 50 | | |
| Ghi chú | M | Text | 150 | | |

**Các bên liên quan:** Warehouse Manager (phê duyệt), AMP (nhận thông báo), WK (nhận task tiếp theo)

---

#### 5.3.3. Điều chuyển về kho - Xác nhận nhập kho

##### 5.3.3.1. Thông số kỹ thuật giao diện người dùng

![5.1.3a B5](images/5_1_3a_B5_image3.png)

**Các bước thực hiện:**
1. Warehouse Keeper tìm kiếm yêu cầu nhập kho đã được phê duyệt
2. Xem chi tiết thông tin yêu cầu và tài sản
3. Quyết định xác nhận hoặc từ chối nhập kho
4. Nếu xác nhận: Nhập thông tin nhận hàng, cập nhật thông tin tài sản
5. Nếu từ chối: Nhập lý do, unlock tài sản
6. Hệ thống cập nhật trạng thái và gửi thông báo

**Luồng xử lý:**
- **Luồng xác nhận:** Nhập thông tin nhận hàng → Cập nhật thông tin tài sản (kho mới, ngày bắt đầu sử dụng) → Cập nhật trạng thái → Gửi email
- **Luồng từ chối:** Nhập lý do → Unlock tài sản → Cập nhật trạng thái → Gửi email

##### 5.3.3.2. Thông số kỹ thuật chi tiết

**Bảng tìm kiếm yêu cầu:**

| Field name VN | M/O | Field type | Editable | Max length | Operator |
|---------------|-----|------------|----------|------------|----------|
| Số yêu cầu | O | Text | Y | 20 | User Input |
| Ngày tạo | O | Date | Y | 20 | User Input |
| Tiêu đề | O | Text | Y | 150 | User Input |
| Người tạo | O | List | Y | 20 | User Select |
| Trạng thái yêu cầu | O | List | Y | 20 | User Select |
| Người xử lý | O | List | Y | 20 | User Select |
| Ngày xác nhận | O | Date | Y | 20 | User Input |

**Yêu cầu nghiệp vụ:**
- Bắt buộc nhập lý do khi từ chối yêu cầu (tối đa 150 ký tự)
- Tự động cập nhật "Ngày bắt đầu sử dụng" khi xác nhận nếu trường này đang là N/A
- Hệ thống phải tự động unlock tài sản khi từ chối để cho phép pickup cho request khác
- Gửi email thông báo tự động cho AMP và BU

**Các bên liên quan:** WK (xác nhận), AMP (nhận thông báo), BU (nhận thông báo)

**Liên kết:** Quay lại [5.3.2. Phê duyệt yêu cầu nhập kho](#532-điều-chuyển-về-kho---phê-duyệt-yêu-cầu-nhập-kho) hoặc [5.3.7. Hủy yêu cầu nhập kho](#537-hủy-yêu-cầu-nhập-kho)

---

#### 5.3.4. Nhập kho thủ công - Tạo yêu cầu

##### 5.3.4.1. Thông số kỹ thuật giao diện người dùng

![5.2.1a B5](images/5_2_1a_B5_image4.png)

**Các bước thực hiện:**
1. Người dùng tạo yêu cầu nhập kho mới
2. Tìm kiếm và chọn tài sản cần nhập kho
3. Nhập thông tin kho nhập và đầu mối giao hàng
4. Đính kèm hồ sơ liên quan (nếu có)
5. Gửi yêu cầu
6. Hệ thống lock tài sản và cập nhật trạng thái
7. Gửi thông báo cho Warehouse Manager

**Mô tả quy trình:**

Chức năng này cho phép người dùng tạo yêu cầu nhập kho thủ công, khác với quy trình tự động từ điều chuyển. Người dùng có thể tìm kiếm và chọn nhiều tài sản trong một yêu cầu. Hệ thống sẽ cảnh báo nếu tài sản đã bị lock trong một request đang xử lý.

##### 5.3.4.2. Thông số kỹ thuật chi tiết

**Đặc tả các trường tìm kiếm tài sản:**

| Trường | Operator | Action | Tên trường VN | M/O | Field type | Editable | Max length |
|--------|----------|--------|---------------|-----|------------|----------|------------|
| - | User | Input | Mã tài sản | O | Text | N | 20 |
| - | User | Input | Tên tài sản | O | Text | Y | 20 |
| - | User | Select | Phân loại tài sản | O | List | N | 20 |
| - | User | Select | Nhóm tài sản | O | List | N | 20 |
| - | User | Input | PO number | O | Text | Y | 20 |
| - | User | Select | Trạng thái TS | O | List | N | 50 |
| - | User | Select | Tên nhà cung cấp | O | List | N | 50 |
| - | User | Input | Tên kho | O | List | Y | 50 |
| - | User | Select | Vị trí đặt tài sản | O | Text | N | 100 |

**Đặc tả thông tin kho và đầu mối:**

| Trường | Operator | Action | Tên trường VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|--------|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| - | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | - | - |
| - | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện theo Tên kho |
| - | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Hiển thị: Tên \| Phòng ban \| Email |
| - | User | Input | Đầu mối | M | Text | Y | 50 | - | - |
| - | User | Input | Số điện thoại | M | Number | Y | 52 | - | - |
| - | User | Input | Thời gian bàn giao | O | Date | Y | 50 | - | - |
| - | User | Input | Ghi chú | M | Text | Y | 150 | - | - |

**Yêu cầu nghiệp vụ:**
- Số yêu cầu theo format NK.YY.xxxx (YY=năm, xxxx=số chạy 1-9999 không dùng lại)
- Có thể chọn nhiều tài sản trong một yêu cầu
- Cảnh báo khi tài sản đã bị lock trong request đang xử lý
- Tài sản bị lock không thể được sử dụng cho request khác

**Liên kết:** Sau khi tạo, chuyển sang [5.3.5. Phê duyệt yêu cầu nhập kho thủ công](#535-nhập-kho-thủ-công---phê-duyệt-yêu-cầu)

---

#### 5.3.5. Nhập kho thủ công - Phê duyệt yêu cầu

##### 5.3.5.1. Thông số kỹ thuật giao diện người dùng

![5.2.2a B5](images/5_2_2a_B5_image5.png)

**Các bước thực hiện:**
1. Warehouse Manager tìm kiếm yêu cầu cần xử lý
2. Xem chi tiết thông tin yêu cầu
3. Quyết định phê duyệt hoặc từ chối
4. Nếu từ chối: Nhập lý do, unlock tài sản
5. Nếu phê duyệt: Cập nhật trạng thái thành "Chờ nhập kho"
6. Tạo task cho Warehouse Keeper

**Luồng xử lý:**
- **Luồng phê duyệt:** Cập nhật trạng thái → Tạo tasklist cho WK → Gửi email → Chuyển sang [5.3.6. Xác nhận nhập kho](#536-nhập-kho-thủ-công---xác-nhận-nhập-kho)
- **Luồng từ chối:** Nhập lý do (bắt buộc, tối đa 150 ký tự) → Unlock tài sản → Cập nhật trạng thái "Từ chối" → Thông báo cho AMP

##### 5.3.5.2. Thông số kỹ thuật chi tiết

**Bảng tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Bảng hiển thị danh sách tài sản:**

| Field name VN | M/O | Data rule |
|---------------|-----|-----------|
| Mã tài sản | M | Hiển thị mặc định |
| Tên Tài sản | M | Hiển thị mặc định |
| Mô tả TS | M | Hiển thị mặc định |
| Trạng thái TS | M | Hiển thị mặc định |
| Phân nhóm TS (group name) | M | Hiển thị mặc định |
| Nhóm TS (CAT1) | M | Hiển thị mặc định |
| Số PO | M | Hiển thị mặc định |
| Tên nhà cung cấp | O | Ẩn hiện tùy biến |
| Nguyên giá TS (VAT incl) | M | Ẩn hiện tùy biến |
| Mã TS liên quan | O | Ẩn hiện tùy biến |
| Mô tả TS liên quan | O | Ẩn hiện tùy biến |
| Tên người sử dụng | M | Hiển thị mặc định |
| Tên đơn vị | M | Hiển thị mặc định |
| Mã nhân viên | M | Ẩn hiện tùy biến |
| Đơn vị sử dụng cha | M | Hiển thị mặc định |
| Email nhân viên | M | Ẩn hiện tùy biến |
| Địa chỉ đặt TS | O | Ẩn hiện tùy biến |
| Tầng đặt TS | O | Ẩn hiện tùy biến |
| Phòng đặt TS | O | Ẩn hiện tùy biến |
| Ngày bắt đầu bảo hành | O | Ẩn hiện tùy biến |
| Thời hạn bảo hành | O | Ẩn hiện tùy biến |
| Ngày kết thúc bảo hành | O | Ẩn hiện tùy biến |
| Công ty bảo hành | O | Ẩn hiện tùy biến |
| Tên người liên hệ bảo hành | O | Ẩn hiện tùy biến |
| Điện thoại người liên hệ | O | Ẩn hiện tùy biến |
| Ngày bắt đầu sử dụng | O | Ẩn hiện tùy biến |

**Các bên liên quan:** Warehouse Manager (phê duyệt), AMP (nhận thông báo), WK (nhận task)

---

#### 5.3.6. Nhập kho thủ công - Xác nhận nhập kho

##### 5.3.6.1. Thông số kỹ thuật giao diện người dùng

![5.2.3a B6](images/5_2_3a_B6_image6.png)

**Các bước thực hiện:**
1. Warehouse Keeper tìm kiếm yêu cầu đã được phê duyệt
2. Xem chi tiết thông tin yêu cầu
3. Quyết định xác nhận hoặc từ chối nhập kho
4. Nếu xác nhận: Unlock và cập nhật thông tin tài sản
5. Nếu từ chối: Nhập lý do, unlock tài sản
6. Cập nhật trạng thái và gửi thông báo

**Yêu cầu nghiệp vụ:**
- Tự động cập nhật "Ngày bắt đầu sử dụng" khi xác nhận thành công nếu trường này đang để trống
- Khi từ chối, phải unlock tài sản để cho phép pickup cho request khác
- Cập nhật tasklist và gửi notification tự động

##### 5.3.6.2. Thông số kỹ thuật chi tiết

**Bảng thông tin kho và giao hàng:**

| Trường | M/O | Kiểu | Editable | Độ dài | Data source | Quy tắc |
|--------|-----|------|----------|--------|-------------|---------|
| Tên kho | M | List | N | 50 | | |
| Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động theo Tên kho |
| Quản lý kho | M | Text | N | 50 | OMS | Hiển thị Tên, Phòng ban, Email |
| Đầu mối | M | Text | Y | 50 | | |
| Số điện thoại | M | Number | Y | 52 | | |
| Thời gian bàn giao | O | Date | Y | 50 | | |
| Ghi chú | M | Text | Y | 150 | | |

**Các bên liên quan:** WK (xác nhận), AMP (nhận thông báo), WM (nhận cập nhật tasklist)

**Liên kết:** Hoàn thành quy trình hoặc chuyển sang [5.3.7. Hủy yêu cầu nhập kho](#537-hủy-yêu-cầu-nhập-kho) nếu cần

---

#### 5.3.7. Hủy yêu cầu nhập kho

##### 5.3.7.1. Thông số kỹ thuật giao diện người dùng

![5.3.1a B5](images/5_3_1a_B5_image7.png)

**Các bước thực hiện:**
1. Người dùng tìm kiếm yêu cầu nhập kho cần hủy
2. Xem chi tiết thông tin để xác nhận yêu cầu đúng
3. Chọn hành động "Hủy" hoặc "Thoát"
4. Nếu hủy: Nhập lý do hủy (bắt buộc)
5. Hệ thống cập nhật trạng thái thành "Đã hủy"
6. Unlock tài sản liên quan
7. Cập nhật tasklist và thông báo cho người dùng cuối

**Điều kiện áp dụng:** Chỉ cho phép hủy yêu cầu nhập kho có trạng thái khác "Đã nhập kho"

##### 5.3.7.2. Thông số kỹ thuật chi tiết

**Bảng Tìm Kiếm Yêu Cầu:**

| Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Yêu cầu nghiệp vụ:**
- Bắt buộc nhập lý do hủy khi thực hiện hủy yêu cầu (tối đa 150 ký tự)
- Hệ thống phải unlock tài sản sau khi hủy để cho phép sử dụng cho yêu cầu khác
- Cập nhật trạng thái tasklist cho các bên liên quan
- Gửi email thông báo cho BU/user khi yêu cầu đã được hủy

**Các bên liên quan:** AMP/User (thực hiện hủy), WM (nhận thông báo), BU User (nhận thông báo)

---

### 5.4. Xuất kho từ cấp tài sản

Module xuất kho từ cấp tài sản xử lý quy trình cấp phát tài sản từ kho cho người dùng, bao gồm các bước từ phê duyệt yêu cầu cấp tài sản đến khi người nhận xác nhận nhận hàng.

**Các quy trình con:**
- [5.4.1. Phê duyệt yêu cầu cấp tài sản](#541-phê-duyệt-yêu-cầu-cấp-tài-sản)
- [5.4.2. Tạo yêu cầu xuất kho](#542-tạo-yêu-cầu-xuất-kho)
- [5.4.3. Tiếp nhận yêu cầu xuất kho](#543-tiếp-nhận-yêu-cầu-xuất-kho)
- [5.4.4. Phê duyệt yêu cầu xuất kho](#544-phê-duyệt-yêu-cầu-xuất-kho)
- [5.4.5. Nhận tài sản](#545-nhận-tài-sản)
- [5.4.6. Hủy yêu cầu xuất kho](#546-hủy-yêu-cầu-xuất-kho)

---

#### 5.4.1. Phê duyệt yêu cầu cấp tài sản

##### 5.4.1.1. Thông số kỹ thuật giao diện người dùng

![5.4.0a A4](images/5_4_0a_A4_image8.png)

**Các bước thực hiện:**
1. Asset Manager tìm kiếm yêu cầu cấp tài sản cần xử lý
2. Xem chi tiết thông tin yêu cầu và tài sản
3. Quyết định phê duyệt hoặc từ chối
4. Nếu phê duyệt: Nhập địa chỉ, cập nhật trạng thái
5. Nếu từ chối: Unlock tài sản, thông báo AMP
6. Chuyển sang quy trình tạo yêu cầu xuất kho

**Luồng xử lý:**
- **Luồng phê duyệt:** Cập nhật trạng thái → Unlock tài sản → Cập nhật tasklist → Thông báo AMP → Chuyển sang [5.4.2. Tạo yêu cầu xuất kho](#542-tạo-yêu-cầu-xuất-kho)
- **Luồng từ chối:** Unlock tài sản → Cập nhật trạng thái → Thông báo

##### 5.4.1.2. Thông số kỹ thuật chi tiết

**Bảng tìm kiếm yêu cầu:**

| Operator | Field name VN | M/O | Field type | Editable | Max length |
|----------|---------------|-----|------------|----------|------------|
| User Input | Mã yêu cầu | M | Text | Y | 20 |
| User Input | Tiêu đề | M | Text | Y | 150 |
| User Select | Người tạo | M | List | Y | 20 |
| User Select | Trạng thái | M | List | Y | 20 |
| User Input | Ngày tạo | M | Date | Y | 20 |
| User Select | Loại cấp tài sản | M | List | Y | 100 |
| User Select | Người xử lý | M | List | Y | 20 |
| User Input | Ngày xác nhận | M | Date | Y | 20 |

**Bảng thông tin tài sản chi tiết:**

| Field name VN | M/O | Editable | Data rule |
|---------------|-----|----------|-----------|
| Mã tài sản | M | N | Hiển thị mặc định |
| Tên Tài sản | M | N | Hiển thị mặc định |
| Mô tả TS | M | N | Hiển thị mặc định |
| Trạng thái TS | M | N | Hiển thị mặc định |
| Phân nhóm TS (group name) | M | N | Hiển thị mặc định |
| Nhóm TS (CAT1) | M | N | Hiển thị mặc định |
| Số PO | M | N | Hiển thị mặc định |
| Tên nhà cung cấp | O | N | Ẩn hiện tùy biến |
| Nguyên giá TS (VAT incl) | M | N | Ẩn hiện tùy biến |
| Mã TS liên quan | O | N | Ẩn hiện tùy biến |
| Mô tả TS liên quan | O | N | Ẩn hiện tùy biến |
| Tên người sử dụng | M | N | Hiển thị mặc định |
| Tên đơn vị | M | N | Hiển thị mặc định |
| Mã nhân viên | M | N | Ẩn hiện tùy biến |
| Đơn vị sử dụng cha | M | N | Hiển thị mặc định |
| Email nhân viên | M | N | Ẩn hiện tùy biến |

**Bảng thông tin đầu mối và người nhận:**

| Operator | Field name VN | M/O | Max length | Default value | Data source | Data rule |
|----------|---------------|-----|------------|---------------|-------------|-----------|
| System Display | Đơn vị cung cấp | M | 50 | | | |
| User Display | Đầu mối | M | 50 | | | |
| User Display | Số điện thoại | M | 52 | | | |
| User Input | Thời gian bàn giao | O | 50 | | | |
| System/User Display/Search/Select | Tên Người nhận | M | 50 | = Người khởi tạo | OMS | |
| System Display | Tên ĐVKD/ Phòng ban HO | M | 50 | | OMS | Tự động nhận diện, hiển thị tên đơn vị Người khởi tạo |
| System Display | Địa chỉ nhận | M | 150 | | OMS | Tự động nhận diện, hiển thị Khối theo Người khởi tạo |
| System/User Display/Input | Điện thoại di động | M | 50 | | OMS | Tự động nhận diện, hiển thị số điện thoại của Người khởi tạo |

**Yêu cầu nghiệp vụ:**
- AM có thể add/delete file do người nhận đính kèm, nhưng không được delete file đính kèm bởi người khởi tạo
- Khi từ chối yêu cầu, hệ thống phải unlock asset để có thể được pickup cho request khác
- Tasklist phải được cập nhật: AM chuyển sang "Đã xử lý", AMP chuyển sang "Cần xử lý"

**Các bên liên quan:** AM (phê duyệt), AMP (nhận thông báo), User (người khởi tạo)

---

#### 5.4.2. Tạo yêu cầu xuất kho

##### 5.4.2.1. Thông số kỹ thuật giao diện người dùng

![5.4.1a. B5](images/5_4_1a__B5_image9.png)

**Các bước thực hiện:**
1. Hệ thống tự động tạo yêu cầu xuất kho sau khi phiếu cấp được phê duyệt
2. Kế thừa thông tin từ phiếu cấp/thanh lý
3. Cập nhật trạng thái yêu cầu
4. Cập nhật tasklist cho các bên liên quan
5. Gửi thông báo cho Warehouse Keeper

**Mô tả quy trình:**

Quy trình tạo yêu cầu xuất kho được hệ thống tự động khởi tạo khi có phiếu cấp tài sản hoặc thanh lý tài sản được phê duyệt. Hệ thống sẽ tự động sinh ra yêu cầu xuất kho với đầy đủ thông tin về tài sản, kho xuất, đầu mối nhận hàng.

##### 5.4.2.2. Thông số kỹ thuật chi tiết

**Thông tin chung:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|---------|---------------|-----------|
| System | Display | Số yêu cầu | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| System | Input | Tiêu đề | O | Text | Y | 150 | | | =Tiêu đề RQ Cấp/Thanh lý |

**Danh sách tài sản xuất kho:**

| Operator | Action | Field name VN | M/O | Editable | Data rule |
|----------|--------|---------------|-----|----------|-----------|
| System | Display | Mã tài sản | M | N | Hiển thị mặc định |
| System | Display | Tên Tài sản | M | N | Hiển thị mặc định |
| System | Display | Mô tả TS | M | N | Hiển thị mặc định |
| System | Display | Trạng thái TS | M | N | Hiển thị mặc định |
| System | Display | Phân nhóm TS (group name) | M | N | Hiển thị mặc định |
| System | Display | Nhóm TS (CAT1) | M | N | Hiển thị mặc định |
| System | Display | Số PO | M | N | Hiển thị mặc định |
| System | Display | Tên nhà cung cấp | O | N | Ẩn hiện tùy biến |
| System | Display | Nguyên giá TS (VAT incl) | M | N | Ẩn hiện tùy biến |
| System | Display | Tên người sử dụng | M | N | Hiển thị mặc định |
| System | Display | Tên đơn vị | M | N | Hiển thị mặc định |
| System | Display | Đơn vị sử dụng cha | M | N | Hiển thị mặc định |

**Thông tin kho xuất và đầu mối nhận hàng:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | = Thông tin kho trên RQ cấp/Thanh lý |
| System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | |
| System | Display | Quản lý kho | M | Text | N | 50 | OMS | |
| User | Input | Đầu mối | M | Text | Y | 50 | | |
| User | Input | Số điện thoại | M | Number | Y | 52 | | |
| User | Input | Thời gian bàn giao | O | Date | Y | 50 | | |
| User | Input | Ghi chú | M | Text | Y | 150 | | = Mã RQ cấp/thanh lý |

**Cập nhật trạng thái và tasklist:**

| Operator | Action | Object | Status/Result |
|----------|--------|--------|---------------|
| System | Update | RQ Cấp tài sản/RQ Thanh lý | Đã xác nhận/Đã cập nhật kết quả thanh lý/Đã phê duyệt kết quả thanh lý |
| System | Update | RQ Xuất kho | Chờ xuất kho |
| System | Update | Tasklist AM | Đã xử lý |
| System | Update | Tasklist WK | Cần xử lý |
| System | Update | Tasklist AMP | Đã xử lý |
| System | Send | Email notification | (Gửi cho WK) |

**Liên kết:** Chuyển sang [5.4.3. Tiếp nhận yêu cầu xuất kho](#543-tiếp-nhận-yêu-cầu-xuất-kho)

---

#### 5.4.3. Tiếp nhận yêu cầu xuất kho

##### 5.4.3.1. Thông số kỹ thuật giao diện người dùng

![5.4.2a. B5](images/5_4_2a__B5_image10.png)

**Các bước thực hiện:**
1. Warehouse Keeper tìm kiếm yêu cầu xuất kho cần xử lý
2. Xem chi tiết thông tin yêu cầu và tài sản
3. Quyết định đồng ý hoặc từ chối
4. Nếu từ chối: Thông báo AMP và kết thúc
5. Nếu đồng ý: Cập nhật trạng thái, unlock tài sản, thông báo Warehouse Manager
6. Chuyển sang quy trình phê duyệt xuất kho

**Lưu ý quan trọng:** Ẩn nút "Từ chối" nếu yêu cầu xuất kho xuất phát từ yêu cầu thanh lý

##### 5.4.3.2. Thông số kỹ thuật chi tiết

**Bảng tìm kiếm yêu cầu (Input fields):**

| Trường | Operator | Field Type | M/O | Editable | Max Length | Mô tả |
|--------|----------|------------|-----|----------|------------|-------|
| Mã yêu cầu | User Input | Text | M | Y | 20 | |
| Tiêu đề | User Input | Text | M | Y | 150 | |
| Người tạo | User Select | List | M | Y | 20 | |
| Trạng thái | User Select | List | M | Y | 20 | |
| Ngày tạo | User Input | Date | M | Y | 20 | |
| Nghiệp vụ kho | User Select | List | M | Y | 100 | |
| Người xử lý | User Select | List | M | Y | 20 | |
| Ngày xác nhận | User Input | Date | M | Y | 20 | |

**Bảng cập nhật trạng thái và tasklist:**

| Bước | Operator | Đối tượng | Trạng thái mới | Ghi chú |
|------|----------|-----------|----------------|---------|
| Từ chối | System Update | RQ Cấp tài sản | Từ chối | |
| Từ chối | System Update | RQ Xuất kho | Từ chối | |
| Từ chối | System Update | Tasklist AM | Đã xử lý | |
| Từ chối | System Update | Tasklist AMP | Cần xử lý | |
| Đồng ý | System Update | RQ Cấp tài sản | Đã xác nhận | |
| Đồng ý | System Update | RQ Xuất kho | Chờ xác nhận | |
| Đồng ý | System Update | Tasklist WK | Đã xử lý | |
| Đồng ý | System Update | Tasklist Warehouse Mgr. | Cần xử lý | |

**Các bên liên quan:** WK (tiếp nhận), AM (cập nhật tasklist), AMP (nhận thông báo), Warehouse Manager (nhận task)

**Liên kết:** Chuyển sang [5.4.4. Phê duyệt yêu cầu xuất kho](#544-phê-duyệt-yêu-cầu-xuất-kho)

---

#### 5.4.4. Phê duyệt yêu cầu xuất kho

##### 5.4.4.1. Thông số kỹ thuật giao diện người dùng

![5.4.3a. B5](images/5_4_3a__B5_image11.png)

**Các bước thực hiện:**
1. Warehouse Manager tìm kiếm yêu cầu xuất kho cần phê duyệt
2. Xem chi tiết thông tin yêu cầu
3. Quyết định phê duyệt hoặc từ chối
4. Nếu từ chối: Nhập lý do, cập nhật trạng thái, thông báo BU user/WK
5. Nếu phê duyệt: Cập nhật trạng thái, unlock tài sản, thông báo AMD/WK
6. Chuyển sang màn hình "Nhận tài sản"

**Lưu ý:** Ẩn nút "Từ chối" nếu RQ xuất kho xuất phát từ yêu cầu thanh lý

##### 5.4.4.2. Thông số kỹ thuật chi tiết

**Bảng tìm kiếm yêu cầu (Tasklist):**

| Field name VN | M/O | Field type | Editable | Max length | Operator |
|---------------|-----|------------|----------|------------|----------|
| Mã yêu cầu | M | Text | N | 20 | User |
| Tiêu đề | M | Text | N | 150 | User |
| Người tạo | M | List | N | 20 | User |
| Trạng thái | M | List | N | 20 | User |
| Ngày tạo | M | Date | N | 20 | User |
| Nghiệp vụ kho | M | List | N | 100 | User |
| Người xử lý | O | List | N | 20 | User |
| Ngày xác nhận | O | Date | N | 20 | User |

**Bảng thông tin kho và đầu mối:**

| Field name VN | M/O | Field type | Editable | Max length | Data source | Operator |
|---------------|-----|------------|----------|------------|-------------|----------|
| Tên kho | M | List | N | 50 | From RQ cấp tài sản | System/User |
| Địa chỉ kho | M | Text | Y | 50 | OMS | System |
| Quản lý kho | M | Text | N | 50 | OMS | System |
| Đầu mối | M | Text | Y | 50 | - | User |
| Số điện thoại | M | Number | Y | 52 | - | User |
| Thời gian bàn giao | O | Date | Y | 50 | - | User |
| Ghi chú | M | Text | Y | 150 | - | User |

**Các bên liên quan:** Warehouse Manager (phê duyệt), WK (nhận thông báo), BU User (nhận thông báo), AMP (nhận thông báo)

**Liên kết:** Chuyển sang [5.4.5. Nhận tài sản](#545-nhận-tài-sản)

---

#### 5.4.5. Nhận tài sản

##### 5.4.5.1. Thông số kỹ thuật giao diện người dùng

![5.4.4a B6](images/5_4_4a_B6_image12.png)

**Các bước thực hiện:**
1. BU User/Nhân viên tìm kiếm yêu cầu cần xử lý
2. Xem chi tiết thông tin yêu cầu và tài sản
3. Chọn hành động: "Tự chối" hoặc "Xác nhận"
4. Nếu xác nhận: Cập nhật trạng thái, unlock tài sản
5. Cập nhật tasklist và thông báo cho VK và AMP

**Mô tả quy trình:**

Quy trình "Nhận tài sản" là bước cuối cùng trong chuỗi xuất kho từ cấp tài sản. BU User sẽ xác nhận việc nhận tài sản vật lý từ kho, sau đó hệ thống cập nhật trạng thái tài sản và hoàn tất quy trình.

##### 5.4.5.2. Thông số kỹ thuật chi tiết

**Bảng tìm kiếm yêu cầu:**

| Operator | Field name VN | M/O | Field type | Editable | Max length | Format |
|----------|---------------|-----|------------|----------|------------|---------|
| User | Mã yêu cầu | M | Text | Y | 20 | |
| User | Tiêu đề | M | Text | Y | 150 | |
| User | Người tạo | M | List | Y | 20 | |
| User | Trạng thái | M | List | Y | 20 | |
| User | Ngày tạo | M | Date | Y | 20 | |
| User | Nghiệp vụ kho | M | List | Y | 100 | |
| User | Người xử lý | M | List | Y | 20 | |
| User | Ngày xác nhận | M | Date | Y | 20 | |

**Bảng thông tin chung:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|---------|---------------|-----------|
| System | Display | Số yêu cầu | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| System | Input | Tiêu đề | O | Text | Y | 150 | | | |

**Các bên liên quan:** BU User (xác nhận nhận tài sản), WK (nhận thông báo), AMP (nhận thông báo)

---

#### 5.4.6. Hủy yêu cầu xuất kho

##### 5.4.6.1. Thông số kỹ thuật giao diện người dùng

![5.5.1a B5](images/5_5_1a_B5_image13.png)

**Các bước thực hiện:**
1. Người dùng tìm kiếm yêu cầu xuất kho cần hủy
2. Xem chi tiết thông tin yêu cầu
3. Chọn hành động "Hủy" hoặc "Thoát"
4. Nếu hủy: Nhập lý do hủy (bắt buộc)
5. Cập nhật trạng thái thành "Đã hủy"
6. Unlock tài sản và thông báo cho WK

**Điều kiện áp dụng:** Chỉ cho phép hủy yêu cầu xuất kho có trạng thái khác "Đã xác nhận"

##### 5.4.6.2. Thông số kỹ thuật chi tiết

**Bảng thông tin tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Mã yêu cầu | M | Text | Y | 20 |
| User | Input | Tiêu đề | M | Text | Y | 150 |
| User | Select | Người tạo | M | List | Y | 20 |
| User | Select | Trạng thái | M | List | Y | 20 |
| User | Input | Ngày tạo | M | Date | Y | 20 |
| User | Select | Nghiệp vụ kho | M | List | Y | 100 |
| User | Select | Người xử lý | M | List | Y | 20 |
| User | Input | Ngày xác nhận | M | Date | Y | 20 |

**Bảng cập nhật trạng thái:**

| Operator | Action | Đối tượng | Status |
|----------|--------|-----------|--------|
| System | Update | RQ Cấp/Thanh lý | Đã hủy |
| System | Update | RQ xuất kho | Đã hủy |
| System | Update | Tasklist AMP | Đã xử lý |

**Yêu cầu nghiệp vụ:**
- Ẩn nút "Từ chối" đối với yêu cầu xuất kho liên kết với yêu cầu thanh lý
- Hệ thống phải unlock tài sản sau khi hủy để cho phép sử dụng trong yêu cầu khác
- Gửi email thông báo cho WK khi hoàn tất quy trình hủy

**Các bên liên quan:** AMP (thực hiện hủy), WK (nhận thông báo)

---

### 5.5. Điều chuyển tài sản giữa các kho

Module điều chuyển tài sản giữa các kho cho phép di chuyển tài sản từ kho này sang kho khác với quy trình phê duyệt đầy đủ.

**Các quy trình con:**
- [5.5.1. Tạo yêu cầu điều chuyển kho](#551-tạo-yêu-cầu-điều-chuyển-kho)
- [5.5.2. Phê duyệt yêu cầu điều chuyển kho](#552-phê-duyệt-yêu-cầu-điều-chuyển-kho)

---

#### 5.5.1. Tạo yêu cầu điều chuyển kho

##### 5.5.1.1. Thông số kỹ thuật giao diện người dùng

![5.6.1a B6](images/5_6_1a_B6_image14.png)

**Các bước thực hiện:**
1. Người dùng tạo yêu cầu điều chuyển kho mới
2. Tìm kiếm và chọn tài sản cần điều chuyển
3. Chọn kho đi và kho nhập
4. Nhập thông tin đầu mối giao hàng
5. Đính kèm tài liệu (nếu có)
6. Gửi yêu cầu
7. Hệ thống lock tài sản và cập nhật trạng thái
8. Gửi thông báo cho Approver

**Mô tả quy trình:**

Quy trình điều chuyển tài sản giữa các kho cho phép di chuyển tài sản từ kho này sang kho khác. Quy trình bao gồm việc tạo yêu cầu, lock tài sản, cập nhật trạng thái và thông báo cho người phê duyệt.

##### 5.5.1.2. Thông số kỹ thuật chi tiết

**Bảng thông tin chung và tìm kiếm tài sản:**

| Tab/Section | Operator | Action | Field Name | M/O | Field Type | Editable | Max Length | Format | Default Value | Data Rule |
|-------------|----------|--------|------------|-----|------------|----------|------------|---------|---------------|-----------|
| Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Thông tin chung | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| Thông tin chung | User | Input | Tiêu đề | O | Text | Y | 150 | | | |
| Tìm kiếm tài sản | User | Input | Mã tài sản | O | Text | N | 20 | | | |
| Tìm kiếm tài sản | User | Input | Tên tài sản | O | Text | Y | 20 | | | |
| Tìm kiếm tài sản | User | Select | Phân loại tài sản | O | List | N | 20 | | | |
| Tìm kiếm tài sản | User | Select | Nhóm tài sản | O | List | N | 20 | | | |
| Tìm kiếm tài sản | User | Input | PO number | O | Text | Y | 20 | | | |
| Tìm kiếm tài sản | User | Select | Trạng thái TS | O | List | N | 50 | | | |
| Tìm kiếm tài sản | User | Select | Tên nhà cung cấp | O | List | N | 50 | | | |
| Tìm kiếm tài sản | User | Input | Tên kho | O | List | Y | 50 | | | |
| Tìm kiếm tài sản | User | Select | Vị trí đặt tài sản | O | Text | N | 100 | | | |

**Bảng thông tin kho và giao hàng:**

| Section | Operator | Action | Field Name | M/O | Field Type | Editable | Max Length | Data Source | Data Rule |
|---------|----------|--------|------------|-----|------------|----------|------------|-------------|-----------|
| Thông tin kho đi | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | |
| Thông tin kho đi | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Thông tin kho đi | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Thông tin kho nhập | User | Select | Tên kho | M | List | N | 50 | | |
| Thông tin kho nhập | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Thông tin kho nhập | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Đầu mối giao hàng | User | Input | Đầu mối | M | Text | Y | 50 | | |
| Đầu mối giao hàng | User | Input | Số điện thoại | M | Number | Y | 52 | | |
| Đầu mối giao hàng | User | Input | Thời gian bàn giao | O | Date | Y | 50 | | |

**Yêu cầu nghiệp vụ:**
- Mã yêu cầu phải theo format CK.YY.xxxx (YY = năm, xxxx = số chạy từ 1-9999 không dùng lại)
- Tài sản bị lock không thể được sử dụng cho request khác cho đến khi hoàn thành
- Trạng thái yêu cầu sau khi tạo là "Chờ phê duyệt"
- Hệ thống phải tự động cập nhật tasklist với trạng thái "Cần xử lý"
- Gửi email notification cho AM và Warehouse Manager

**Liên kết:** Chuyển sang [5.5.2. Phê duyệt yêu cầu điều chuyển kho](#552-phê-duyệt-yêu-cầu-điều-chuyển-kho)

---

#### 5.5.2. Phê duyệt yêu cầu điều chuyển kho

##### 5.5.2.1. Thông số kỹ thuật giao diện người dùng

![5.6.2a B5](images/5_6_2a_B5_image15.png)

**Các bước thực hiện:**
1. Approver tìm kiếm yêu cầu điều chuyển cần xử lý
2. Xem chi tiết thông tin yêu cầu và tài sản
3. Quyết định phê duyệt hoặc từ chối
4. Nếu phê duyệt: Cập nhật trạng thái, unlock tài sản, tạo phiếu xuất/nhập kho
5. Nếu từ chối: Nhập lý do, unlock tài sản
6. Gửi thông báo cho các bên liên quan

**Luồng xử lý:**
- **Luồng phê duyệt:** Cập nhật trạng thái → Unlock tài sản → Cập nhật tasklist → Gửi thông báo → Ghi nhận thông tin kho → Tự động tạo phiếu xuất/nhập kho → Cập nhật cho WK
- **Luồng từ chối:** Unlock tài sản → Cập nhật trạng thái → Thông báo AMP

##### 5.5.2.2. Thông số kỹ thuật chi tiết

**Bảng tìm kiếm yêu cầu:**

| Field name VN | M/O | Field type | Editable | Max length |
|---------------|-----|------------|----------|------------|
| Số yêu cầu | O | Text | Y | 20 |
| Ngày tạo | O | Date | Y | 20 |
| Tiêu đề | O | Text | Y | 150 |
| Người tạo | O | List | Y | 20 |
| Trạng thái yêu cầu | O | List | Y | 20 |
| Người xử lý | O | List | Y | 20 |
| Ngày xác nhận | O | Date | Y | 20 |

**Bảng thông tin chung yêu cầu:**

| Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | O | Text | Y | 150 | | | |
| Thêm tài sản | M | Button | N | | | | |

**Bảng thông tin kho và giao hàng:**

| Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|---------------|-----|------------|----------|------------|-------------|-----------|
| Tên kho (đi) | M | List | N | 50 | | |
| Địa chỉ kho (đi) | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Quản lý kho (đi) | M | Text | N | 50 | OMS | Tự động nhận diện (Tên \| Phòng ban \| Email) |
| Tên kho (nhập) | M | List | N | 50 | | |
| Địa chỉ kho (nhập) | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Quản lý kho (nhập) | M | Text | N | 50 | OMS | Tự động nhận diện (Tên \| Phòng ban \| Email) |
| Đầu mối | M | Text | N | 50 | | |
| Số điện thoại | M | Number | N | 52 | | |
| Thời gian bàn giao | O | Date | N | 50 | | |

**Yêu cầu nghiệp vụ:**
- Khi phê duyệt, hệ thống tự động tạo phiếu xuất kho và phiếu nhập kho tương ứng
- Bắt buộc nhập lý do khi từ chối (tối đa 150 ký tự)
- Tự động cập nhật thông tin kho và trạng thái lock/unlock tài sản
- Gửi email thông báo đến các bên liên quan theo từng giai đoạn

**Các bên liên quan:** Approver (phê duyệt), AMP (nhận thông báo), WK kho đi (xuất hàng), WK kho đến (nhập hàng)

---

### 5.6. Quản lý trạng thái (Status)

Phần này định nghĩa chi tiết các trạng thái và luồng chuyển đổi trạng thái cho các quy trình quản lý tài sản.

#### 5.6.1. Trạng thái quy trình Cấp tài sản không ở kho

| Sub-process | PIC | Action | Rq Status | Asset Status | Note |
|-------------|-----|--------|-----------|--------------|------|
| 1 Tạo yêu cầu | AMP | Lưu | Đang tạo | | |
| | | Gửi | Chờ xác nhận | | |
| 2. Xác nhận | BU User | Từ chối | Từ chối | | |
| | | Xác nhận | Đã xác nhận | Đang sử dụng | Đã xác nhận >>> Đã nhận tài sản |
| | | Bổ sung thông tin | Bổ sung thông tin | | |
| 3. Bổ sung TT | AMP | Bổ sung thông tin | Chờ xác nhận | | |

#### 5.6.2. Trạng thái quy trình Cấp tài sản từ kho

| Sub-process | PIC | Action | Rq Status | Asset Status | Note |
|-------------|-----|--------|-----------|--------------|------|
| 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | | |
| | | Gửi | Chờ xác nhận | | |
| 2. Phê duyệt | AM | Từ chối | Từ chối | | |
| | | Duyệt | Đã xác nhận | | |
| 3. Tạo yêu cầu | System | | Đã xác nhận | Chờ xuất kho | |
| 4. Xuất kho | WK | Từ chối | Từ chối | Từ chối | |
| | | Đồng ý | Đã xác nhận | Chờ phê duyệt | |
| 5. Phê duyệt | Warehouse Mgr. | Từ chối | Từ chối | Từ chối | |
| | | Duyệt | Đã xác nhận | Chờ xác nhận | |
| 6. Nhận hàng | BU User | Từ chối | Từ chối | Từ chối | |
| | | Xác nhận | Đã xác nhận | Đã nhận tài sản | Đang sử dụng |

#### 5.6.3. Trạng thái quy trình Thanh lý - Bán trực tiếp

| Sub-process | PIC | Action | Rq Status | Asset Status | Note |
|-------------|-----|--------|-----------|--------------|------|
| 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | | |
| | | Gửi | Chờ kiểm soát | | |
| 2. Kiểm soát | Checker | Từ chối | Từ chối | | |
| | | Yêu cầu bổ sung thông tin | Bổ sung thông tin | | |
| | | Đồng ý | Chờ phê duyệt | | |
| 3. Phê duyệt | Approver | Từ chối | Đang tạo | | |
| | | Yêu cầu bổ sung thông tin | Bổ sung thông tin | | |
| | | Phê duyệt | Chờ cập nhật kết quả | | |
| 4. Cập nhật kết quả thanh lý | AMP | Hủy | Đã hủy | | |
| | | Cập nhật kết quả | Đã cập nhật kết quả thanh lý | Đã thanh lý | |

**Liên kết:** Xem chi tiết các quy trình tại:
- [5.3. Module Quản Lý Kho](#53-module-quản-lý-kho)
- [5.4. Xuất kho từ cấp tài sản](#54-xuất-kho-từ-cấp-tài-sản)
- [5.5. Điều chuyển tài sản giữa các kho](#55-điều-chuyển-tài-sản-giữa-các-kho)

---

### 5.7. Quản lý Tasklist

Tasklist quản lý danh sách công việc cần xử lý và đã xử lý cho từng vai trò trong hệ thống.

#### 5.7.1. Cấu trúc Tasklist

| Sub-process | Action | Role | Tasklist Điều chuyển (Cần xử lý) | Tasklist Điều chuyển (Đã xử lý) | Tasklist Kho (Cần xử lý) | Tasklist Kho (Đã xử lý) | Ghi chú |
|-------------|--------|------|----------------------------------|--------------------------------|---------------------------|-------------------------|---------|
| 2.3.1a Tạo yêu cầu điều chuyển | Lưu | Initator | x | | | | |
| | Gửi | | | x | | | |
| 2.3.3a Phê duyệt yêu cầu điều chuyển | Từ chối | Initator | x | | | | |
| | | BUH | | x | | | |
| | Duyệt | Initator | | x | | | |
| | | BUH | | x | | | |
| | | AMP | x | | | | |
| | Bổ sung thông tin | Initator | x | | | | |
| | | BUH | | x | | | |
| 5.2.2a Xác nhận yêu cầu điều chuyển | Từ chối | Initator | x | | | | |
| | | BUH | | x | | | |
| | | AMP | | x | | | |
| | Bổ sung thông tin | Initator | x | | | | |
| | | BUH | | x | | | |
| | | AMP | | x | | | |
| | Xác nhận & Yêu cầu nhập kho | Gửi | Initator | x | | | |
| | | BUH | | x | | | |
| | | AMP | | x | | x | |
| | | WM | | | x | | |

**Loại Tasklist:**
- **Tasklist Điều chuyển:** Quản lý công việc liên quan đến quy trình điều chuyển tài sản
- **Tasklist Kho:** Quản lý công việc liên quan đến xuất/nhập kho

**Trạng thái Tasklist:**
- **Cần xử lý:** Công việc đang chờ người dùng xử lý
- **Đã xử lý:** Công việc đã được hoàn thành

**Liên kết:** Xem chi tiết quy trình tại [5.3. Module Quản Lý Kho](#53-module-quản-lý-kho) và [5.5. Điều chuyển tài sản giữa các kho](#55-điều-chuyển-tài-sản-giữa-các-kho)

---

## 6. Assumptions & Constraints

### 6.1. Giả định (Assumptions)

1. **Hệ thống OMS** đã sẵn sàng và cung cấp API để đồng bộ thông tin đơn vị, kho và quản lý kho
2. **Hệ thống EMS** hỗ trợ webhook hoặc API để đồng bộ thông tin PO
3. **Người dùng** đã được đào tạo về quy trình nghiệp vụ cơ bản
4. **Hạ tầng email** sẵn sàng để gửi thông báo tự động
5. **Quyền truy cập** được phân bổ đúng theo vai trò

### 6.2. Ràng buộc (Constraints)

1. **Thời gian:** Dự án phải hoàn thành trong timeline Wave 4
2. **Kỹ thuật:** 
   - Số yêu cầu không được dùng lại sau khi đã tạo
   - Tài sản bị lock không thể sử dụng cho request khác
3. **Nghiệp vụ:**
   - Không cho phép từ chối yêu cầu xuất kho từ thanh lý
   - Quy trình phê duyệt phải tuần tự theo đúng luồng đã định nghĩa
4. **Tích hợp:** Phụ thuộc vào tính sẵn sàng của OMS và EMS

---

## 7. Dependencies

### 7.1. Phụ thuộc hệ thống

| Hệ thống | Loại phụ thuộc | Mô tả |
|----------|----------------|-------|
| OMS | Data | Thông tin đơn vị, kho, quản lý kho, orgchart |
| EMS | Data | Thông tin PO, thời gian bảo hành |
| Email System | Infrastructure | Gửi thông báo tự động |
| ITSM | Integration (Future) | Yêu cầu sửa chữa tài sản |

### 7.2. Phụ thuộc nội bộ giữa các module

| Module nguồn | Module đích | Loại phụ thuộc |
|--------------|-------------|----------------|
| [Yêu cầu điều chuyển](#531-điều-chuyển-về-kho---tạo-yêu-cầu-nhập-kho) | [Yêu cầu nhập kho](#532-điều-chuyển-về-kho---phê-duyệt-yêu-cầu-nhập-kho) | Tự động tạo |
| [Yêu cầu cấp tài sản](#541-phê-duyệt-yêu-cầu-cấp-tài-sản) | [Yêu cầu xuất kho](#542-tạo-yêu-cầu-xuất-kho) | Tự động tạo |
| [Yêu cầu thanh lý](#541-phê-duyệt-yêu-cầu-cấp-tài-sản) | [Yêu cầu xuất kho](#542-tạo-yêu-cầu-xuất-kho) | Tự động tạo |
| [Điều chuyển giữa kho](#552-phê-duyệt-yêu-cầu-điều-chuyển-kho) | Phiếu xuất/nhập kho | Tự động tạo |

---

## 8. Acceptance Criteria

### 8.1. Tiêu chí chức năng

| ID | Tiêu chí | Module liên quan |
|----|----------|------------------|
| AC-01 | Dashboard hiển thị đúng số liệu tổng quan tài sản | [Dashboard](#52-dashboard-tài-sản) |
| AC-02 | Biểu đồ tương tác và có thể drill-down | [Dashboard](#52-dashboard-tài-sản) |
| AC-03 | Tự động tạo yêu cầu nhập kho khi xác nhận điều chuyển | [Module Kho](#531-điều-chuyển-về-kho---tạo-yêu-cầu-nhập-kho) |
| AC-04 | Tự động tạo yêu cầu xuất kho khi phê duyệt cấp tài sản | [Xuất kho](#542-tạo-yêu-cầu-xuất-kho) |
| AC-05 | Lock/Unlock tài sản đúng theo quy trình | Tất cả module |
| AC-06 | Gửi email thông báo cho đúng người theo từng bước | Tất cả module |
| AC-07 | Cập nhật tasklist chính xác | [Tasklist](#57-quản-lý-tasklist) |
| AC-08 | Số yêu cầu sinh theo đúng format (NK/XK/CK.YY.xxxx) | Tất cả module |

### 8.2. Tiêu chí phi chức năng

| ID | Tiêu chí | Giá trị mục tiêu |
|----|----------|------------------|
| NF-01 | Thời gian tải Dashboard | < 3 giây |
| NF-02 | Thời gian đồng bộ OMS | < 5 phút |
| NF-03 | Thời gian gửi email | < 1 phút |
| NF-04 | Độ chính xác dữ liệu | 100% |
| NF-05 | Uptime hệ thống | > 99.5% |

---

## 9. Glossary

| Thuật ngữ | Viết tắt | Định nghĩa |
|-----------|----------|------------|
| Asset Management Personnel | AMP | Nhân viên quản lý tài sản |
| Asset Manager | AM | Quản lý tài sản |
| Business Unit | BU | Đơn vị kinh doanh |
| Business Unit Head | BUH | Trưởng đơn vị kinh doanh |
| Warehouse Keeper | WK | Thủ kho |
| Warehouse Manager | WM/Warehouse Mgr. | Quản lý kho |
| Organization Management System | OMS | Hệ thống quản lý tổ chức |
| Enterprise Management System | EMS | Hệ thống quản lý doanh nghiệp |
| Fixed Asset Management | FAM | Hệ thống quản lý tài sản cố định |
| Purchase Order | PO | Đơn đặt hàng |
| Request | RQ | Yêu cầu |
| List of Values | LOV | Danh sách giá trị |
| Mandatory | M | Bắt buộc |
| Optional | O | Tùy chọn |
| Nhập Kho | NK | Mã prefix cho yêu cầu nhập kho |
| Xuất Kho | XK | Mã prefix cho yêu cầu xuất kho |
| Chuyển Kho | CK | Mã prefix cho yêu cầu điều chuyển kho |

---

*Tài liệu này được tạo dựa trên các bản tóm tắt sheet từ file Excel BRD FAM UPGRADE - WAVE 4.*

---

*Generated from 37 sheets | Images: 15*
