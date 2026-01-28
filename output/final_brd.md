# Tài liệu Yêu cầu Nghiệp vụ - FAM UPGRADE WAVE 4

---

## Mục lục

1. [Executive Summary](#1-executive-summary)
2. [Project Scope & Objectives](#2-project-scope-objectives)
3. [Stakeholders](#3-stakeholders)
4. [FAM UPGRADE WAVE 4](#4-fam-upgrade-wave-4)
5. [Business Requirements](#5-business-requirements)
   - [5.1. Dashboard Tài Sản](#51-dashboard-tài-sản)
   - [5.2. Module Quản lý Kho](#52-module-quản-lý-kho)
   - [5.3. Điều chuyển về kho - Tạo yêu cầu nhập kho](#53-điều-chuyển-về-kho-tạo-yêu-cầu-nhập-kho)
   - [5.4. Điều chuyển về kho - Phê duyệt yêu cầu nhập kho](#54-điều-chuyển-về-kho-phê-duyệt-yêu-cầu-nhập-kho)
   - [5.5. Nhập kho từ quy trình điều chuyển về kho](#55-nhập-kho-từ-quy-trình-điều-chuyển-về-kho)
   - [5.6. Nhập kho thủ công - Tạo yêu cầu](#56-nhập-kho-thủ-công-tạo-yêu-cầu)
   - [5.7. Nhập kho thủ công - Phê duyệt yêu cầu](#57-nhập-kho-thủ-công-phê-duyệt-yêu-cầu)
   - [5.8. Nhập kho thủ công - Xác nhận nhập kho](#58-nhập-kho-thủ-công-xác-nhận-nhập-kho)
   - [5.9. Hủy Yêu Cầu Nhập Kho](#59-hủy-yêu-cầu-nhập-kho)
   - [5.10. Phê duyệt yêu cầu cấp tài sản](#510-phê-duyệt-yêu-cầu-cấp-tài-sản)
   - [5.11. Tạo yêu cầu xuất kho](#511-tạo-yêu-cầu-xuất-kho)
   - [5.12. Xuất kho từ cấp tài sản - Tiếp nhận yêu cầu xuất kho](#512-xuất-kho-từ-cấp-tài-sản-tiếp-nhận-yêu-cầu-xuất-kho)
   - [5.13. Xuất kho từ cấp tài sản - Phê duyệt yêu cầu xuất kho](#513-xuất-kho-từ-cấp-tài-sản-phê-duyệt-yêu-cầu-xuất-kho)
   - [5.14. Xuất kho từ cấp tài sản - Nhận tài sản](#514-xuất-kho-từ-cấp-tài-sản-nhận-tài-sản)
   - [5.15. Hủy Yêu Cầu Xuất Kho](#515-hủy-yêu-cầu-xuất-kho)
   - [5.16. Điều chuyển tài sản giữa các kho - Tạo yêu cầu điều chuyển kho](#516-điều-chuyển-tài-sản-giữa-các-kho-tạo-yêu-cầu-điều-chuyển-kho)
   - [5.17. Điều chuyển tài sản giữa các kho - Phê duyệt yêu cầu điều chuyển kho](#517-điều-chuyển-tài-sản-giữa-các-kho-phê-duyệt-yêu-cầu-điều-chuyển-kho)
6. [System Status Matrix](#6-system-status-matrix)
7. [Task Assignment Matrix](#7-task-assignment-matrix)
8. [Assumptions & Constraints](#8-assumptions-constraints)
9. [Dependencies](#9-dependencies)
10. [Acceptance Criteria](#10-acceptance-criteria)
11. [Glossary](#11-glossary)

---

## 1. Executive Summary

Dự án **FAM UPGRADE WAVE 4** nhằm nâng cấp hệ thống quản lý tài sản cố định (Fixed Asset Management) với các enhancement quan trọng và module mới. Dự án tập trung vào ba nhóm sản phẩm chính:

**Dashboard tài sản với khả năng trực quan hóa cao** - Được phân loại ưu tiên cao (Priority 1), dashboard mới cho phép customize theo nhiều tiêu chí và hiển thị thông tin theo hướng visualize. Chi tiết xem [5.1. Dashboard Tài Sản](#51-dashboard-tài-sản).

**Module quản lý kho toàn diện** - Cũng được đánh giá Priority 1, module này hỗ trợ đầy đủ quy trình xuất-nhập kho tài sản, tiếp nhận yêu cầu từ các quy trình cấp tài sản, thanh lý và điều chuyển. Xem chi tiết tại [5.2. Module Quản lý Kho](#52-module-quản-lý-kho).

**Các cải tiến giao diện và quy trình** - Bao gồm nâng cấp tùy chọn ẩn/hiện tài sản, điều chỉnh vị trí cột, tự động hóa quy trình cấp phát và tích hợp với các hệ thống bên ngoài như OMS, EMS, ITSM.

Dự án được thiết kế để tích hợp chặt chẽ với hạ tầng hiện có, đồng thời cung cấp khả năng mở rộng cho các nâng cấp tương lai.

---

## 2. Project Scope & Objectives

### Trong phạm vi dự án

- **Dashboard tài sản**: Phát triển giao diện visualize với khả năng customize và báo cáo tương tác
- **Module kho**: Xây dựng module quản lý kho hoàn chỉnh với 7 luồng nghiệp vụ chính
- **Enhancement giao diện**: Cải tiến các tùy chọn hiển thị và tương tác người dùng
- **Tự động hóa quy trình**: Cải tiến quy trình cấp phát và phê duyệt
- **Tích hợp hệ thống**: Đồng bộ với OMS, EMS, ITSM và cổng hỗ trợ chi nhánh

### Ngoài phạm vi dự án

- Nâng cấp hạ tầng máy chủ hoặc database
- Thay đổi các quy trình nghiệp vụ cốt lõi không liên quan đến 11 yêu cầu được định nghĩa
- Phát triển mobile app riêng biệt

### Mục tiêu dự án

1. **Cải thiện trải nghiệm người dùng**: Dashboard trực quan và giao diện tùy biến
2. **Tự động hóa quy trình**: Giảm thao tác thủ công thông qua auto-confirmation và workflow tự động
3. **Tăng cường kiểm soát**: Module kho với đầy đủ tính năng quản lý xuất nhập
4. **Tích hợp dữ liệu**: Đồng bộ thông tin từ các hệ thống liên quan

---

## 3. Stakeholders

### Người dùng cuối cùng

- **Business User (BU)**: Người dùng thuộc đơn vị kinh doanh
- **Asset Management Personnel (AMP)**: Nhân viên quản lý tài sản
- **Warehouse Keeper (WK)**: Thủ kho
- **Warehouse Manager**: Quản lý kho
- **Asset Manager (AM)**: Quản lý tài sản cấp cao

### Vai trò phê duyệt

- **Business Unit Head (BUH)**: Trưởng đơn vị kinh doanh
- **Checker**: Người kiểm soát
- **Approver**: Người phê duyệt

### Hệ thống liên quan

- **OMS (Organization Management System)**: Quản lý thông tin tổ chức và kho
- **EMS**: Hệ thống quản lý doanh nghiệp
- **ITSM**: Hệ thống quản lý IT Service
- **Cổng hỗ trợ chi nhánh trên intranet**

---

## 4. FAM UPGRADE WAVE 4

Kế hoạch nâng cấp hệ thống FAM Wave 4 bao gồm 11 yêu cầu chính được phân loại theo mức độ ưu tiên và chức năng:

### Danh sách yêu cầu nâng cấp

| STT | Item | Loại | Chức năng | Chi tiết | Priority | Ghi chú |
|-----|------|------|-----------|----------|----------|---------|
| 1 | FAM Wave 4 | Enhancement | Tài sản | Dashboard tài sản hiển thị theo hướng visualize; có thể customize theo nhiều tiêu chí | 1 | Login vào là nhìn thấy luôn. Cần liệt kê rõ ràng role |
| 2 | | | | Ẩn hiện tùy chọn tài sản vô hiệu hóa khỏi danh sách tài sản | 2 | |
| 3 | | | | Đổi vị trí hiển thị một số cột trong danh sách tài sản | 2 | |
| 4 | | | Cấp tài sản | Upload phiếu cấp tài sản theo danh sách | 3 | |
| 5 | | | | Auto xác nhận phiếu cấp tài sản | 2 | Sau 20 ngày kể từ khi request bàn giao tài sản được tạo, user không có phản hồi, Hệ thống tự động xác nhận |
| 6 | | | Integration | Auto đồng bộ OMS khi orgchart thay đổi | 2 | |
| 7 | | | | Đồng bộ tiêu đề PO từ EMS sang FAM | 2 | |
| 8 | | | | Tài sản từ EMS, cột "Thông tin thời gian đưa vào sử dụng, Thời gian bắt đầu bảo hành" = thời gian PO được phê duyệt | 2 | |
| 9 | | | Thanh lý | Bổ sung luồng phê duyệt cho ATM | 3 | Thêm thông tin as is và to be |
| 10 | | New launch | Modul kho | Xuất - nhập kho tài sản. Tiếp nhận yêu cầu xuất - nhập kho từ yêu cầu cấp ts, thanh lý tài sản, điều chuyển ts về kho | 1 | |
| 11 | | | Modul sửa chữa tài sản | Tạo yêu cầu sửa chữa tài sản thực hiện trên FAM => Hệ thống tạo yêu cầu (gửi link) sang Hệ thống ITSM và Cổng hỗ trợ chi nhánh trên intranet. Hoàn tất, yêu cầu đc feed back qua FAM | 4 | Cần Clear qui trình |

### Phân loại theo mức độ ưu tiên

**Priority 1 (Cao nhất)**: [Dashboard tài sản](#51-dashboard-tài-sản) và [Module kho](#52-module-quản-lý-kho) - Đây là hai thành phần cốt lõi sẽ mang lại giá trị lớn nhất cho người dùng.

**Priority 2 (Trung bình-cao)**: Các cải tiến về tự động hóa và tích hợp, bao gồm auto-confirmation, đồng bộ OMS/EMS.

**Priority 3 (Trung bình)**: Upload batch và workflow thanh lý ATM.

**Priority 4 (Thấp)**: Module sửa chữa cần làm rõ quy trình trước khi triển khai.

---

## 5. Business Requirements

### 5.1. Dashboard Tài Sản

Dashboard Tài Sản được thiết kế để cung cấp giao diện tổng quan và trực quan hóa dữ liệu tài sản, hỗ trợ đưa ra quyết định nhanh chóng thông qua các biểu đồ tương tác và báo cáo có thể tùy biến.

#### 5.1.1. Thông số kỹ thuật tổng quan

Dashboard hiển thị thông tin tài sản theo nhiều khía cạnh khác nhau bao gồm phân bổ theo phòng ban/orgchart, trạng thái tài sản, biến động theo thời gian và tỷ lệ sử dụng. Hệ thống tích hợp với OMS (Organization Management System) để đồng bộ dữ liệu đơn vị sử dụng và cung cấp khả năng xuất báo cáo ra Excel.

**Các chỉ số KPI chính:**

| STT | Chỉ số | Mô tả tính toán | Loại giá trị |
|-----|---------|-----------------|--------------|
| 1 | Total assets | Count số lượng (All tài sản - Đã thanh lý - Vô hiệu hóa) | Số lượng |
| 2 | Total value | Sum nguyên giá (All tài sản - Đã thanh lý - Vô hiệu hóa) | Giá trị |
| 3 | Warranty status | Tỷ lệ % số lượng tài sản còn hạn bảo hành/(All tài sản - Vô hiệu hóa - Đã thanh lý) | Phần trăm |
| 4 | Utilization rate | Tỷ lệ % số lượng tài sản đang sử dụng/(All tài sản - Vô hiệu hóa - Đã thanh lý) | Phần trăm |

**Bộ lọc dùng chung:**

| STT | Tên bộ lọc | Kiểu dữ liệu | Nguồn dữ liệu |
|-----|------------|--------------|---------------|
| 1 | Vùng | LOV | - |
| 2 | Đơn vị sử dụng | LOV | Đồng bộ từ OMS |
| 3 | CAT 1 | LOV | - |
| 4 | Group name | LOV | - |
| 5 | Asset status | LOV | Không bao gồm "Đã thanh lý", "Vô hiệu hóa" |

#### 5.1.2. Đặc tả biểu đồ tương tác

| Tên biểu đồ | Dữ liệu hiển thị | Loại biểu đồ | Ghi chú |
|-------------|------------------|--------------|---------|
| Asset Distribution | Cơ cấu nhóm tài sản theo trạng thái | Sunburst | Vòng trong: IT/ADM/CMD, Vòng ngoài: Trạng thái. Hover hiển thị số lượng và giá trị |
| Asset Distribution | Cơ cấu theo Vùng/Đơn vị sử dụng | Stacked Column | Nguyên giá |
| Asset Value by Group Name | Giá trị theo Group Name | Column | Nguyên giá |
| Asset Fluctuation Over Time | Biến động theo tháng/năm | Line | Nguyên giá |
| Asset by Time in Use | Tài sản theo thời gian sử dụng | Scatter | Số lượng |

Các biểu đồ đều có tính năng tương tác với hover effects và khả năng drill-down. Khi click vào các phần tử biểu đồ, người dùng sẽ được chuyển đến danh sách tài sản chi tiết tương ứng.

---

### 5.2. Module Quản lý Kho

Module Quản lý Kho là một trong những thành phần ưu tiên cao nhất trong FAM Wave 4, cung cấp khả năng quản lý toàn diện các hoạt động xuất-nhập kho tài sản. Module này tích hợp chặt chẽ với các quy trình nghiệp vụ khác như [cấp tài sản](#510-phê-duyệt-yêu-cầu-cấp-tài-sản), [thanh lý tài sản](#515-hủy-yêu-cầu-xuất-kho), và [điều chuyển tài sản](#516-điều-chuyển-tài-sản-giữa-các-kho-tạo-yêu-cầu-điều-chuyển-kho).

#### 5.2.1. Tổng quan quy trình nghiệp vụ

Module bao gồm 7 luồng công việc chính:

1. **Điều chuyển nội bộ** - Xử lý điều chuyển chéo và về kho
2. **Nhập kho** - [Tự động](#53-điều-chuyển-về-kho-tạo-yêu-cầu-nhập-kho) và [thủ công](#56-nhập-kho-thủ-công-tạo-yêu-cầu)
3. **Hủy nhập kho** - [Quy trình hủy yêu cầu](#59-hủy-yêu-cầu-nhập-kho)
4. **Cấp tài sản** - Tích hợp với [quy trình cấp phát](#510-phê-duyệt-yêu-cầu-cấp-tài-sản)
5. **Thanh lý tài sản** - Xử lý xuất kho cho thanh lý
6. **Xuất kho** - [Tiếp nhận](#512-xuất-kho-từ-cấp-tài-sản-tiếp-nhận-yêu-cầu-xuất-kho) và [xử lý yêu cầu](#513-xuất-kho-từ-cấp-tài-sản-phê-duyệt-yêu-cầu-xuất-kho)
7. **Điều chuyển kho** - [Tạo](#516-điều-chuyển-tài-sản-giữa-các-kho-tạo-yêu-cầu-điều-chuyển-kho) và [phê duyệt yêu cầu](#517-điều-chuyển-tài-sản-giữa-các-kho-phê-duyệt-yêu-cầu-điều-chuyển-kho)

#### 5.2.2. Tích hợp tự động

**Khái niệm quan trọng**: Hệ thống được thiết kế với khả năng tích hợp giữa các quy trình. Khi hoàn thành [quy trình cấp tài sản](#510-phê-duyệt-yêu-cầu-cấp-tài-sản) hoặc thanh lý tài sản, hệ thống sẽ tự động tạo [yêu cầu xuất kho](#511-tạo-yêu-cầu-xuất-kho) tương ứng, đảm bảo tính liên kết và giảm thiểu thao tác thủ công.

**Quy tắc tự động hóa:**
- Tự động tạo yêu cầu nhập kho khi hoàn thành điều chuyển về kho
- Tự động tạo yêu cầu xuất kho khi hoàn thành cấp TS hoặc thanh lý TS  
- Tự động hủy các yêu cầu liên quan khi hủy yêu cầu chính
- Tự động sinh biên bản xuất/nhập kho và bút toán kế toán
- Tự động cập nhật kết quả ngược lại cho yêu cầu gốc khi hoàn thành

---

### 5.3. Điều chuyển về kho - Tạo yêu cầu nhập kho

Quy trình này xử lý việc tạo yêu cầu nhập kho tự động khi tài sản được chuyển đến kho từ nơi khác. Đây là một phần quan trọng của [Module Quản lý Kho](#52-module-quản-lý-kho).

#### 5.3.1. Thông số kỹ thuật giao diện người dùng

![5.1.1a B5](images/5_1_1a_B5_image1.png)

**Các bước thực hiện:**
1. **Tạo yêu cầu nhập kho** - Khởi tạo yêu cầu trong hệ thống
2. **Cập nhật trạng thái yêu cầu** - Hệ thống cập nhật status của yêu cầu
3. **Cập nhật tasklist** - Yêu cầu được thêm vào danh sách công việc cần xử lý
4. **Thông báo cho Warehouse Mgr.** - Gửi notification đến người quản lý kho
5. **Chuyển sang phê duyệt** - Liên kết đến [quy trình phê duyệt](#54-điều-chuyển-về-kho-phê-duyệt-yêu-cầu-nhập-kho)

**Luồng công việc:** Quy trình tuân theo mô hình tuyến tính từ trái sang phải, với mỗi bước được thực hiện tuần tự. Toàn bộ quy trình được thực hiện tự động bởi hệ thống khi có yêu cầu điều chuyển được xác nhận.

#### 5.3.2. Thông số kỹ thuật chi tiết

Hệ thống tự động tạo yêu cầu nhập kho khi xử lý điều chuyển tài sản về kho, kế thừa toàn bộ thông tin từ yêu cầu điều chuyển gốc.

**Đặc tả trường dữ liệu - Thông tin chung:**

| STT | Tab/Section | Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Format | Default Value | Data Rule |
|-----|-------------|----------|---------|---------------|-----|------------|----------|------------|---------|---------------|-----------|
| 1 | Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| 2 | Thông tin chung | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| 3 | Thông tin chung | System | Display | Tiêu đề | M | Text | N | 150 | | | =Tiêu đề RQ điều chuyển |

**Thông tin kho và đầu mối giao hàng:**

| Tab/Section | Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Data Source | Data Rule |
|-------------|----------|---------|---------------|-----|------------|----------|------------|-------------|-----------|
| Thông tin kho nhập | System | Display | Tên kho | M | List | N | 50 | | = Kho trong RQ điều chuyển |
| Thông tin kho nhập | System | Display | Địa chỉ kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Thông tin kho nhập | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Thông tin đầu mối giao hàng | User | Input | Đầu mối | M | Text | N | 50 | | = Đầu mối giao hàng trong RQ điều chuyển |
| Thông tin đầu mối giao hàng | User | Input | Số điện thoại | M | Number | N | 52 | | |
| Thông tin đầu mối giao hàng | User | Input | Thời gian bàn giao | O | Date | N | 50 | | |

**Quy trình tự động (4 bước):**

| Bước | Operator | Action | Đối tượng | Giá trị |
|------|----------|---------|-----------|---------|
| 2 | System | Update | Trạng thái RQ điều chuyển | Đã xác nhận |
| 2 | System | Update | Trạng thái RQ nhập kho | Chờ phê duyệt |
| 3 | System | Update | Tasklist AMP | "Đã xử lý" |
| 3 | System | Update | Tasklist WM | "Cần xử lý" |
| 4 | System | Send | Email notification | Notification |

Sau khi hoàn thành, quy trình chuyển sang [phê duyệt yêu cầu nhập kho](#54-điều-chuyển-về-kho-phê-duyệt-yêu-cầu-nhập-kho).

---

### 5.4. Điều chuyển về kho - Phê duyệt yêu cầu nhập kho

Quy trình phê duyệt yêu cầu nhập kho được khởi tạo từ [tạo yêu cầu nhập kho](#53-điều-chuyển-về-kho-tạo-yêu-cầu-nhập-kho), cho phép Warehouse Manager xem xét và phê duyệt các yêu cầu nhập tài sản vào kho.

#### 5.4.1. Thông số kỹ thuật giao diện người dùng

![5.1.2a B6](images/5_1_2a_B6_image2.png)

**Các bước thực hiện quy trình:**

*Luồng chính (Phê duyệt):*
1. **Nhập thông tin tìm kiếm yêu cầu** - Form tìm kiếm với nhiều tiêu chí
2. **Hiển thị kết quả tìm kiếm** - Danh sách yêu cầu phù hợp  
3. **Chọn và xem yêu cầu** - Lựa chọn yêu cầu cụ thể để xem chi tiết
4. **Điểm quyết định "Phê duyệt"** - Gateway với hai lựa chọn
5. **Cập nhật trạng thái yêu cầu** - Hệ thống cập nhật status
6. **Cập nhật tasklist** - Phân công công việc cho các role
7. **Gửi email thông báo** - Thông báo kết quả cho các bên liên quan
8. **Chuyển đến xác nhận nhập kho** - Liên kết đến [quy trình xác nhận](#55-nhập-kho-từ-quy-trình-điều-chuyển-về-kho)

*Luồng phụ (Từ chối):*
1. **Nhập lý do từ chối** - Bắt buộc nhập lý do cụ thể
2. **Xác nhận đồng ý** - Confirmation step
3. **Unlock tài sản** - Giải phóng tài sản đã được lock
4. **Cập nhật trạng thái** và **tasklist** - Cập nhật tương ứng
5. **Gửi email thông báo** - Thông báo từ chối

#### 5.4.2. Thông số kỹ thuật chi tiết

Giao diện được thiết kế để Warehouse Manager có thể tìm kiếm, xem chi tiết và ra quyết định về các yêu cầu nhập kho.

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

**Thông tin tài sản được hiển thị** bao gồm các trường chính:

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
| Tên người sử dụng | M | Hiển thị mặc định |
| Tên đơn vị | M | Hiển thị mặc định |
| Đơn vị sử dụng cha | M | Hiển thị mặc định |

**Cập nhật trạng thái tự động:**

| Action | Object | Status/Rule |
|--------|--------|-------------|
| System Update | Trạng thái RQ nhập kho | Từ chối (khi từ chối) / Chờ nhập kho (khi phê duyệt) |
| System Update | Trạng thái RQ Điều chuyển | Từ chối (khi từ chối) / Không update (khi phê duyệt) |
| System Update | Tasklist WM | Đã xử lý |
| System Update | Tasklist WK | Cần xử lý (khi phê duyệt) |
| System Update | Tasklist BU | Cần xử lý (khi từ chối) / Không update (khi phê duyệt) |
| System Update | Tasklist AMP | Cần xử lý (khi từ chối) / Không update (khi phê duyệt) |

Sau khi phê duyệt thành công, quy trình chuyển sang [xác nhận nhập kho](#55-nhập-kho-từ-quy-trình-điều-chuyển-về-kho).

---

### 5.5. Nhập kho từ quy trình điều chuyển về kho

Đây là bước cuối cùng trong quy trình điều chuyển về kho, cho phép Warehouse Keeper xác nhận việc nhập tài sản vào kho sau khi đã được [phê duyệt](#54-điều-chuyển-về-kho-phê-duyệt-yêu-cầu-nhập-kho).

#### 5.5.1. Thông số kỹ thuật giao diện người dùng

![5.1.3a B5](images/5_1_3a_B5_image3.png)

**Các bước thực hiện quy trình:**

**Luồng chung (3 bước đầu):**
1. **Nhập thông tin tìm kiếm yêu cầu** - Tìm kiếm yêu cầu cần xử lý
2. **Hiển thị kết quả tìm kiếm** - Danh sách yêu cầu phù hợp
3. **Chọn và xem yêu cầu** - Lựa chọn yêu cầu cụ thể để xem chi tiết

**Điểm quyết định "Xác nhận"** với hai hướng xử lý:

**Luồng đồng ý:**
4. **Nhập thông tin nhận hàng** - Ghi nhận chi tiết nhận hàng
5. **Xác nhận thực hiện** - Gateway confirmation
6. **Unlock và cập nhật thông tin tài sản** - Cập nhật thông tin kho cho tài sản
7. **Cập nhật trạng thái yêu cầu** - Chuyển sang "Đã nhập kho"
8. **Cập nhật tasklist** - Phân công công việc tiếp theo
9. **Gửi email thông báo** - Thông báo hoàn thành

**Luồng từ chối:**
4. **Nhập lý do từ chối** - Bắt buộc nhập lý do cụ thể
5. **Xác nhận từ chối** - Gateway confirmation  
6. **Unlock tài sản** - Giải phóng tài sản
7. **Cập nhật trạng thái yêu cầu** - Chuyển sang "Từ chối"
8. **Cập nhật tasklist** - Thông báo cho các bên liên quan
9. **Gửi email thông báo** - Thông báo từ chối

#### 5.5.2. Thông số kỹ thuật chi tiết

**Form tìm kiếm yêu cầu:**

| Field Name VN | M/O | Field Type | Editable | Max Length | Operator | Action |
|---------------|-----|------------|----------|------------|----------|--------|
| Số yêu cầu | O | Text | Y | 20 | User | Input |
| Ngày tạo | O | Date | Y | 20 | User | Input |
| Tiêu đề | O | Text | Y | 150 | User | Input |
| Người tạo | O | List | Y | 20 | User | Select |
| Trạng thái yêu cầu | O | List | Y | 20 | User | Select |
| Người xử lý | O | List | Y | 20 | User | Select |
| Ngày xác nhận | O | Date | Y | 20 | User | Input |

**Thông tin kho nhập:**

| Field Name VN | M/O | Field Type | Max Length | Data Source | Data Rule |
|---------------|-----|------------|------------|-------------|-----------|
| Tên kho | M | List | 50 | | |
| Địa chỉ kho | M | Text | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Quản lý kho | M | Text | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

**Logic nghiệp vụ quan trọng:**
- Hệ thống tự động cập nhật "Ngày bắt đầu sử dụng" khi xác nhận nhập kho nếu trường này có giá trị N/A
- Unlock tài sản khi từ chối hoặc xác nhận để tài sản có thể được sử dụng cho yêu cầu khác
- Tự động cập nhật trạng thái yêu cầu điều chuyển liên quan khi từ chối
- Gửi thông báo email tự động cho AMP và BU khi có thay đổi trạng thái

---

### 5.6. Nhập kho thủ công - Tạo yêu cầu

Chức năng này cho phép tạo yêu cầu nhập kho tài sản một cách thủ công, khác với quy trình tự động từ [điều chuyển về kho](#53-điều-chuyển-về-kho-tạo-yêu-cầu-nhập-kho). Đây là một phần quan trọng của [Module Quản lý Kho](#52-module-quản-lý-kho).

#### 5.6.1. Thông số kỹ thuật giao diện người dùng

![5.2.1a B5](images/5_2_1a_B5_image4.png)

**Các bước thực hiện quy trình:**
1. **Tạo yêu cầu nhập kho và định nghĩa danh sách** - Khởi tạo yêu cầu với thông tin cơ bản
2. **Lock tài sản** - Khóa tài sản để tránh xung đột với các yêu cầu khác
3. **Điểm quyết định** với hai lựa chọn:
   - **"Gửi"** - Tiếp tục quy trình với các bước sau:
     - Cập nhật trạng thái yêu cầu thành "Chờ phê duyệt"
     - Cập nhật tasklist người nhận
     - Gửi email thông báo cho Warehouse Manager
     - Chuyển sang [quy trình phê duyệt](#57-nhập-kho-thủ-công-phê-duyệt-yêu-cầu)
   - **"Thoát"** - Kết thúc quy trình ngay lập tức

#### 5.6.2. Thông số kỹ thuật chi tiết

**Thông tin chung yêu cầu:**

| Tab/Section | Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Format | Default Value | Data Rule |
|-------------|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| Thông tin chung | | | | | | | | | | |
| | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| | User | Input | Tiêu đề | O | Text | Y | 150 | | | |
| | User | Select | Thêm tài sản | M | Button | N | | | | |

**Form tìm kiếm tài sản:**

| Field name VN | M/O | Field type | Editable | Max length | Operator |
|---------------|-----|------------|----------|------------|----------|
| Mã tài sản | O | Text | N | 20 | User Input |
| Tên tài sản | O | Text | Y | 20 | User Input |
| Phân loại tài sản | O | List | N | 20 | User Select |
| Nhóm tài sản | O | List | N | 20 | User Select |
| PO number | O | Text | Y | 20 | User Input |
| Trạng thái TS | O | List | N | 50 | User Select |
| Tên nhà cung cấp | O | List | N | 50 | User Select |
| Tên kho | O | List | Y | 50 | User Input |
| Vị trí đặt tài sản | O | Text | N | 100 | User Select |

**Thông tin kho nhập:**

| Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|---------------|-----|------------|----------|------------|-------------|-----------|
| Tên kho | M | List | N | 50 | | System/User Display/Search/Select |
| Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện (Tên \| Phòng ban \| Email) |

**Thông tin đầu mối giao hàng:**

| Field name VN | M/O | Field type | Editable | Max length |
|---------------|-----|------------|----------|------------|
| Đầu mối | M | Text | Y | 50 |
| Số điện thoại | M | Number | Y | 52 |
| Thời gian bàn giao | O | Date | Y | 50 |
| Ghi chú | M | Text | Y | 150 |

**Yêu cầu nghiệp vụ:**
- Có thể chọn nhiều tài sản cho một yêu cầu
- Cảnh báo khi tài sản đã bị lock trong request khác đang xử lý
- Tài sản bị lock không thể sử dụng cho request khác cho đến khi request hiện tại hoàn thành
- Bắt buộc có đầu mối giao hàng và số điện thoại liên lạc

Sau khi gửi thành công, quy trình chuyển sang [phê duyệt yêu cầu nhập kho thủ công](#57-nhập-kho-thủ-công-phê-duyệt-yêu-cầu).

---

### 5.7. Nhập kho thủ công - Phê duyệt yêu cầu

Quy trình phê duyệt cho các yêu cầu nhập kho thủ công được tạo từ [nhập kho thủ công](#56-nhập-kho-thủ-công-tạo-yêu-cầu), cho phép Warehouse Manager xem xét và quyết định phê duyệt.

#### 5.7.1. Thông số kỹ thuật giao diện người dùng

![5.2.2a B5](images/5_2_2a_B5_image5.png)

**Các bước thực hiện quy trình:**

**Luồng chung (3 bước đầu):**
1. **Nhập thông tin tìm kiếm yêu cầu** - Form tìm kiếm với nhiều tiêu chí
2. **Hiển thị kết quả tìm kiếm** - Danh sách yêu cầu phù hợp
3. **Chọn và xem yêu cầu** - Lựa chọn yêu cầu cụ thể để xem chi tiết

**Điểm quyết định "Phê duyệt"** với hai hướng xử lý:

**Luồng phê duyệt:**
4. **Cập nhật trạng thái yêu cầu** - Chuyển sang "Chờ xác nhận"
5. **Cập nhật tasklist** - Phân công cho Warehouse Keeper
6. **Gửi email thông báo** - Thông báo cho người yêu cầu
7. **Chuyển đến xác nhận nhập kho** - Liên kết đến [quy trình xác nhận](#58-nhập-kho-thủ-công-xác-nhận-nhập-kho)

**Luồng từ chối:**
4. **Nhập lý do từ chối** - Bắt buộc nhập lý do cụ thể
5. **Xác nhận đồng ý từ chối** - Gateway confirmation
6. **Unlock tài sản** - Giải phóng tài sản đã được lock
7. **Cập nhật trạng thái yêu cầu** - Chuyển sang "Từ chối"
8. **Cập nhật tasklist** - Thông báo cho các bên liên quan
9. **Gửi email thông báo** - Thông báo từ chối

#### 5.7.2. Thông số kỹ thuật chi tiết

**Form tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Thông tin tài sản hiển thị:**

| Trường | M/O | Hiển thị | Mô tả |
|--------|-----|----------|-------|
| Mã tài sản | M | Hiển thị mặc định | |
| Tên Tài sản | M | Hiển thị mặc định | |
| Mô tả TS | M | Hiển thị mặc định | |
| Trạng thái TS | M | Hiển thị mặc định | |
| Phân nhóm TS (group name) | M | Hiển thị mặc định | |
| Nhóm TS (CAT1) | M | Hiển thị mặc định | |
| Số PO | M | Hiển thị mặc định | |
| Nguyên giá TS (VAT incl) | M | Ẩn hiện tùy biến | |
| Tên người sử dụng | M | Hiển thị mặc định | |
| Tên đơn vị | M | Hiển thị mặc định | |
| Đơn vị sử dụng cha | M | Hiển thị mặc định | |

**Thông tin kho:**

| Trường | M/O | Kiểu | Editable | Độ dài | Nguồn dữ liệu | Quy tắc |
|--------|-----|------|----------|--------|---------------|---------|
| Tên kho | M | List | N | 50 | | |
| Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện theo Tên kho |
| Quản lý kho | M | Text | N | 50 | OMS | Hiển thị: Tên \| Phòng ban \| Email |

**Yêu cầu nghiệp vụ:**
- Bắt buộc nhập lý do khi từ chối yêu cầu (max 150 ký tự)
- Cho phép nhập ghi chú khi phê duyệt (max 150 ký tự)
- Tự động unlock tài sản khi yêu cầu bị từ chối
- Cập nhật tasklist và gửi email thông báo cho các bên liên quan

---

### 5.8. Nhập kho thủ công - Xác nhận nhập kho

Bước cuối cùng trong quy trình nhập kho thủ công, được thực hiện sau khi yêu cầu đã được [phê duyệt](#57-nhập-kho-thủ-công-phê-duyệt-yêu-cầu).

#### 5.8.1. Thông số kỹ thuật giao diện người dùng

![5.2.3a B6](images/5_2_3a_B6_image6.png)

**Các bước thực hiện quy trình:**

**Luồng chung (3 bước đầu):**
1. **Nhập thông tin tìm kiếm yêu cầu** - Tìm kiếm yêu cầu cần xử lý
2. **Hiển thị kết quả tìm kiếm** - Danh sách yêu cầu đã được phê duyệt
3. **Chọn và xem yêu cầu** - Lựa chọn yêu cầu cụ thể để xử lý

**Điểm quyết định "Xác nhận"** với hai hướng xử lý:

**Luồng đồng ý:**
4. **Nhập thông tin nhận hàng** - Ghi nhận chi tiết thực tế nhận hàng
5. **Gateway kiểm tra "Đồng ý"** - Xác nhận cuối cùng
6. **Unlock và cập nhật thông tin tài sản** - Cập nhật thông tin kho
7. **Cập nhật trạng thái yêu cầu** - Chuyển sang "Đã nhập kho"
8. **Cập nhật tasklist** - Hoàn thành công việc
9. **Gửi email thông báo** - Thông báo hoàn thành

**Luồng từ chối:**
4. **Nhập lý do từ chối** - Bắt buộc nhập lý do cụ thể
5. **Gateway kiểm tra "Đồng ý"** - Xác nhận từ chối
6. **Unlock tài sản** - Giải phóng tài sản
7. **Cập nhật trạng thái yêu cầu** - Chuyển sang "Từ chối"
8. **Cập nhật tasklist** - Thông báo các bên liên quan
9. **Gửi email thông báo** - Thông báo từ chối

#### 5.8.2. Thông số kỹ thuật chi tiết

**Form tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Thông tin kho nhập:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| System | Display | Tên kho | M | List | N | 50 | | |
| System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

**Thông tin đầu mối giao hàng:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| System | Display | Đầu mối | M | Text | Y | 50 |
| System | Display | Số điện thoại | M | Number | Y | 52 |
| System | Display | Thời gian bàn giao | O | Date | Y | 50 |
| System | Display | Ghi chú | M | Text | Y | 150 |

**Yêu cầu nghiệp vụ:**
- Chỉ được xác nhận yêu cầu có trạng thái "Chờ xác nhận"
- Tự động cập nhật "Ngày bắt đầu sử dụng" khi xác nhận nếu trường này = N/A
- Unlock tài sản khi từ chối để asset có thể được pickup cho request khác
- Cập nhật tasklist cho các role khác nhau và gửi email notification
- Hỗ trợ đính kèm hồ sơ tài liệu với thông tin chi tiết về file

---

### 5.9. Hủy Yêu Cầu Nhập Kho

Chức năng cho phép hủy các yêu cầu nhập kho đã được tạo nhưng chưa hoàn thành, áp dụng cho cả [nhập kho từ điều chuyển](#53-điều-chuyển-về-kho-tạo-yêu-cầu-nhập-kho) và [nhập kho thủ công](#56-nhập-kho-thủ-công-tạo-yêu-cầu).

#### 5.9.1. Thông số kỹ thuật giao diện người dùng

![5.3.1a B5](images/5_3_1a_B5_image7.png)

**Các bước thực hiện quy trình:**
1. **Nhập thông tin tìm kiếm yêu cầu** - Form tìm kiếm yêu cầu cần hủy
2. **Hiển thị kết quả tìm kiếm** - Danh sách yêu cầu phù hợp
3. **Chọn yêu cầu cần xử lý** - Lựa chọn yêu cầu cụ thể từ danh sách
4. **Điểm quyết định** với hai lựa chọn:
   - **"Hủy"** - Tiếp tục với các bước:
     - Nhập lý do hủy (bắt buộc)
     - Cập nhật trạng thái yêu cầu thành "Đã hủy"
     - Unlock tài sản để có thể sử dụng cho yêu cầu khác
     - Cập nhật tasklist cho các bên liên quan
     - Thông báo cho BU user
   - **"Thoát"** - Quay về bước 3 hoặc kết thúc quy trình

#### 5.9.2. Thông số kỹ thuật chi tiết

**Điều kiện hủy yêu cầu:**
- Yêu cầu nhập kho phải được gửi thành công
- Yêu cầu phải có trạng thái khác "Đã nhập kho"

**Form tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Thông tin yêu cầu - Thông tin chung:**

| Trường | Operator | Action | Bắt buộc | Max Length | Format | Default | Data Rule |
|--------|----------|--------|----------|------------|--------|---------|-----------|
| Số yêu cầu | System | Display | M | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 |
| Ngày tạo | System | Display | M | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | System | Input | O | 150 | | | |

**Thông tin kho xuất:**

| Trường | Operator | Action | Bắt buộc | Max Length | Data Source | Data Rule |
|--------|----------|--------|----------|------------|-------------|-----------|
| Tên kho | System/User | Display/Search/Select | M | 50 | | Thông tin kho trên RQ cấp tài sản |
| Địa chỉ kho | System | Display | M | 50 | OMS | |
| Quản lý kho | System | Display | M | 50 | OMS | |

**Logic nghiệp vụ:**
- Bắt buộc nhập lý do hủy khi thực hiện hủy yêu cầu
- Tự động unlock tài sản khi yêu cầu bị hủy để asset có thể được pickup cho request khác
- Cập nhật trạng thái yêu cầu thành "Đã hủy"
- Cập nhật tasklist: WM thành "Đã xử lý", AMP/BU user thành "Cần xử lý"
- Gửi thông báo email cho các bên liên quan

---

### 5.10. Phê duyệt yêu cầu cấp tài sản

Quy trình phê duyệt yêu cầu cấp tài sản là điểm khởi đầu cho việc tạo [yêu cầu xuất kho](#511-tạo-yêu-cầu-xuất-kho) trong [Module Quản lý Kho](#52-module-quản-lý-kho).

#### 5.10.1. Thông số kỹ thuật giao diện người dùng

![5.4.0a A4](images/5_4_0a_A4_image8.png)

**Các bước thực hiện quy trình:**

**Luồng chung (3 bước đầu):**
1. **Nhập thông tin tìm kiếm yêu cầu** - Form tìm kiếm với nhiều tiêu chí
2. **Hiển thị kết quả tìm kiếm** - Danh sách yêu cầu cấp tài sản
3. **Chọn yêu cầu cần xử lý** - Lựa chọn yêu cầu cụ thể để xem chi tiết

**Điểm quyết định** với hai hướng xử lý:

**Luồng từ chối:**
- Dẫn trực tiếp đến End Event và chuyển sang "Bước 3"

**Luồng phê duyệt:**
4. **Nhập lý do từ chối** (nếu cần)
5. **Cập nhật trạng thái yêu cầu** - Chuyển sang "Đã phê duyệt"
6. **Unlock tài sản** - Chuẩn bị cho việc xuất kho
7. **Cập nhật tasklist** - Phân công công việc tiếp theo
8. **Thông báo cho AMP** - Gửi notification
9. **Chuyển sang tạo yêu cầu xuất kho** - Liên kết đến [quy trình 5.4.1a](#511-tạo-yêu-cầu-xuất-kho)

#### 5.10.2. Thông số kỹ thuật chi tiết

**Form tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Mã yêu cầu | M | Text | Y | 20 |
| User | Input | Tiêu đề | M | Text | Y | 150 |
| User | Select | Người tạo | M | List | Y | 20 |
| User | Select | Trạng thái | M | List | Y | 20 |
| User | Input | Ngày tạo | M | Date | Y | 20 |
| User | Select | Loại cấp tài sản | M | List | Y | 100 |
| User | Select | Người xử lý | M | List | Y | 20 |
| User | Input | Ngày xác nhận | M | Date | Y | 20 |

**Thông tin tài sản được cấp** (hiển thị 25+ trường):

| Operator | Action | Field name VN | M/O | Data rule |
|----------|--------|---------------|-----|-----------|
| System | Display | Mã tài sản | M | Hiển thị mặc định |
| System | Display | Tên Tài sản | M | Hiển thị mặc định |
| System | Display | Mô tả TS | M | Hiển thị mặc định |
| System | Display | Trạng thái TS | M | Hiển thị mặc định |
| System | Display | Phân nhóm TS (group name) | M | Hiển thị mặc định |
| System | Display | Nhóm TS (CAT1) | M | Hiển thị mặc định |
| System | Display | Số PO | M | Hiển thị mặc định |
| System | Display | Tên nhà cung cấp | O | Ẩn hiện tùy biến |
| System | Display | Nguyên giá TS (VAT incl) | M | Ẩn hiện tùy biến |
| System | Display | Tên người sử dụng | M | Hiển thị mặc định |
| System | Display | Tên đơn vị | M | Hiển thị mặc định |
| System | Display | Đơn vị sử dụng cha | M | Hiển thị mặc định |

**Thông tin đơn vị nhận:**

| Operator | Action | Field name VN | M/O | Max length | Default value | Data source | Data rule |
|----------|--------|---------------|-----|------------|---------------|-------------|-----------|
| System/User | Display/Search/Select | Tên Người nhận | M | 50 | = Người khởi tạo | OMS | |
| System | Display | Tên ĐVKD/ Phòng ban HO | M | 50 | | OMS | Tự động nhận diện, hiển thị tên đơn vị Người khởi tạo |
| System | Display | Địa chỉ nhận | M | 150 | | OMS | Tự động nhận diện, hiển thị Khối theo Người khởi tạo |
| System/User | Display/Input | Điện thoại di động | M | 50 | | OMS | Tự động nhận diện, hiển thị số điện thoại của Người khởi tạo |

**Yêu cầu nghiệp vụ:**
- Bắt buộc nhập lý do khi từ chối yêu cầu (max 150 ký tự)
- Tự động unlock tài sản khi yêu cầu bị từ chối
- Tự động cập nhật tasklist và gửi thông báo email cho AMP
- AM có thể thêm/xóa file đính kèm nhưng không được xóa file do người khởi tạo đính kèm
- Lưu trữ đầy đủ lịch sử xử lý với thông tin người xử lý, hành động, thời gian và ghi chú

Sau khi phê duyệt thành công, hệ thống tự động chuyển sang [tạo yêu cầu xuất kho](#511-tạo-yêu-cầu-xuất-kho).

---

### 5.11. Tạo yêu cầu xuất kho

Quy trình này được khởi tạo tự động sau khi [yêu cầu cấp tài sản được phê duyệt](#510-phê-duyệt-yêu-cầu-cấp-tài-sản), tạo ra yêu cầu xuất kho tương ứng để chuyển tài sản từ kho đến người sử dụng cuối cùng.

#### 5.11.1. Thông số kỹ thuật giao diện người dùng

![5.4.1a. B5](images/5_4_1a__B5_image9.png)

**Các bước thực hiện quy trình:**
1. **Tạo yêu cầu xuất kho** - Hệ thống tự động khởi tạo yêu cầu dựa trên thông tin phiếu cấp
2. **Cập nhật trạng thái yêu cầu** - Hệ thống cập nhật status của yêu cầu
3. **Cập nhật tasklist** - Cập nhật danh sách công việc cho các role liên quan
4. **Thông báo cho WK** - Gửi thông báo đến Warehouse Keeper
5. **Chuyển sang tiếp nhận yêu cầu** - Liên kết đến [quy trình 5.4.2a](#512-xuất-kho-từ-cấp-tài-sản-tiếp-nhận-yêu-cầu-xuất-kho)

#### 5.11.2. Thông số kỹ thuật chi tiết

Hệ thống tự động tạo yêu cầu xuất kho dựa trên thông tin từ phiếu cấp tài sản đã được phê duyệt.

**Thông tin chung yêu cầu:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max Length | Format | Default | Data Rule |
|--------|----------|---------|------------|-----|------|----------|------------|---------|---------|-----------|
| Số yêu cầu | System | Display | Số yêu cầu | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Ngày tạo | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | System | Input | Tiêu đề | O | Text | Y | 150 | | | =Tiêu đề RQ Cấp/Thanh lý |

**Thông tin kho xuất:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max Length | Data Source | Data Rule |
|--------|----------|---------|------------|-----|------|----------|------------|-------------|-----------|
| Tên kho | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | = Thông tin kho trên RQ cấp/Thanh lý |
| Địa chỉ kho | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | |
| Quản lý kho | System | Display | Quản lý kho | M | Text | N | 50 | OMS | |

**Thông tin đầu mối nhận hàng:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max Length |
|--------|----------|---------|------------|-----|------|----------|------------|
| Đầu mối | User | Input | Đầu mối | M | Text | Y | 50 |
| Số điện thoại | User | Input | Số điện thoại | M | Number | Y | 52 |
| Thời gian bàn giao | User | Input | Thời gian bàn giao | O | Date | Y | 50 |

**Quy trình cập nhật tự động:**

| Đối tượng | Action | Trạng thái mới |
|-----------|---------|----------------|
| RQ Cấp tài sản/RQ Thanh lý | Update | Đã xác nhận/Đã cập nhật kết quả thanh lý/Đã phê duyệt kết quả thanh lý |
| RQ Xuất kho | Update | Chờ xuất kho |
| Tasklist AM | Update | Đã xử lý |
| Tasklist WK | Update | Cần xử lý |
| Tasklist AMP | Update | Đã xử lý |

**Yêu cầu nghiệp vụ:**
- Danh sách tài sản phải kế thừa hoàn toàn từ phiếu cấp/thanh lý gốc
- Thông tin kho xuất phải khớp với thông tin kho trên RQ cấp/thanh lý
- Bắt buộc nhập thông tin đầu mối và số điện thoại người nhận
- Ghi chú mặc định phải chứa mã RQ cấp/thanh lý gốc

Sau khi tạo thành công, quy trình chuyển sang [tiếp nhận yêu cầu xuất kho](#512-xuất-kho-từ-cấp-tài-sản-tiếp-nhận-yêu-cầu-xuất-kho).

---

### 5.12. Xuất kho từ cấp tài sản - Tiếp nhận yêu cầu xuất kho

Quy trình tiếp nhận và xử lý các yêu cầu xuất kho được tạo từ [tạo yêu cầu xuất kho](#511-tạo-yêu-cầu-xuất-kho), cho phép Warehouse Keeper xem xét và quyết định về yêu cầu.

#### 5.12.1. Thông số kỹ thuật giao diện người dùng

![5.4.2a. B5](images/5_4_2a__B5_image10.png)

**Các bước thực hiện quy trình:**

**Luồng chung (3 bước đầu):**
1. **Nhập thông tin tìm kiếm yêu cầu** - Form tìm kiếm yêu cầu xuất kho
2. **Hiển thị kết quả tìm kiếm** - Danh sách yêu cầu phù hợp
3. **Chọn yêu cầu cần xử lý** - Lựa chọn yêu cầu cụ thể để xem chi tiết

**Điểm quyết định** với hai hướng xử lý:

**Luồng từ chối:**
4. **Cập nhật trạng thái yêu cầu** - Chuyển sang "Từ chối"
5. **Unlock tài sản** - Giải phóng tài sản đã được lock
6. **Cập nhật tasklist** - Thông báo cho các bên liên quan
7. **Thông báo cho AMP** - Gửi notification về việc từ chối

**Luồng đồng ý:**
4. **Cập nhật trạng thái yêu cầu** - Chuyển sang "Chờ phê duyệt"
5. **Cập nhật tasklist** - Phân công cho Warehouse Manager
6. **Thông báo cho Warehouse Manager** - Gửi notification
7. **Chuyển sang phê duyệt xuất kho** - Liên kết đến [quy trình 5.4.3a](#513-xuất-kho-từ-cấp-tài-sản-phê-duyệt-yêu-cầu-xuất-kho)

#### 5.12.2. Thông số kỹ thuật chi tiết

**Form tìm kiếm yêu cầu:**

| Operator | Field name VN | M/O | Field type | Editable | Max length |
|----------|---------------|-----|------------|----------|------------|
| User Input | Mã yêu cầu | M | Text | Y | 20 |
| User Input | Tiêu đề | M | Text | Y | 150 |
| User Select | Người tạo | M | List | Y | 20 |
| User Select | Trạng thái | M | List | Y | 20 |
| User Input | Ngày tạo | M | Date | Y | 20 |
| User Select | Nghiệp vụ kho | M | List | Y | 100 |
| User Select | Người xử lý | M | List | Y | 20 |
| User Input | Ngày xác nhận | M | Date | Y | 20 |

**Thông tin chi tiết tài sản** (Display Only):

| Field name VN | M/O | Editable | Hiển thị |
|---------------|-----|----------|----------|
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
| Đơn vị sử dụng cha | M | N | Hiển thị mặc định |

**Thông tin đầu mối nhận hàng:**

| Field name VN | M/O | Field type | Editable | Max length |
|---------------|-----|------------|----------|------------|
| Đầu mối | M | Text | Y | 50 |
| Số điện thoại | M | Number | Y | 52 |
| Thời gian bàn giao | O | Date | Y | 50 |
| Ghi chú | M | Text | Y | 150 |

**Yêu cầu nghiệp vụ:**
- Ẩn nút "Từ chối" nếu yêu cầu xuất kho xuất phát từ yêu cầu thanh lý
- Hệ thống phải tự động lock/unlock tài sản khi từ chối yêu cầu
- Cập nhật multiple tasklist và gửi email notification theo workflow
- Số yêu cầu phải theo format "XK.YY.xxxx" (YY = năm, xxxx = số chạy 1-9999)

---

### 5.13. Xuất kho từ cấp tài sản - Phê duyệt yêu cầu xuất kho

Quy trình phê duyệt yêu cầu xuất kho được thực hiện bởi Warehouse Manager sau khi yêu cầu đã được [tiếp nhận](#512-xuất-kho-từ-cấp-tài-sản-tiếp-nhận-yêu-cầu-xuất-kho).

#### 5.13.1. Thông số kỹ thuật giao diện người dùng

![5.4.3a. B5](images/5_4_3a__B5_image11.png)

**Các bước thực hiện quy trình:**

**Luồng chung (3 bước đầu):**
1. **Nhập thông tin tìm kiếm yêu cầu** - Form tìm kiếm với các tiêu chí
2. **Hiển thị kết quả tìm kiếm** - Danh sách yêu cầu chờ phê duyệt
3. **Chọn yêu cầu cần xử lý** - Lựa chọn yêu cầu cụ thể

**Điểm quyết định "Phê duyệt"** với hai hướng:

**Luồng từ chối:**
4. **Cập nhật trạng thái yêu cầu** - Chuyển sang "Từ chối"
5. **Thông báo BU user, WK** - Gửi notification từ chối

**Luồng phê duyệt:**
4. **Thực hiện song song 4 task:**
   - Cập nhật trạng thái yêu cầu
   - Mở khóa tài sản
   - Cập nhật tasklist  
   - Thông báo AMP/WK
5. **Xuất báo cáo** - Tạo báo cáo xuất kho
6. **Chuyển đến màn hình nhận tài sản** - Liên kết đến [quy trình 5.4.4a](#514-xuất-kho-từ-cấp-tài-sản-nhận-tài-sản)

#### 5.13.2. Thông số kỹ thuật chi tiết

**Tiêu chí tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Mã yêu cầu | M | Text | Y | 20 |
| User | Input | Tiêu đề | M | Text | Y | 150 |
| User | Select | Người tạo | M | List | Y | 20 |
| User | Select | Trạng thái | M | List | Y | 20 |
| User | Input | Ngày tạo | M | Date | Y | 20 |
| User | Select | Loại cấp tài sản | M | List | Y | 100 |
| User | Select | Người xử lý | M | List | Y | 20 |
| User | Input | Ngày xác nhận | M | Date | Y | 20 |

**Thông tin tài sản xuất kho** (26 trường):

| Operator | Action | Field name VN | M/O | Hiển thị | Data rule |
|----------|--------|---------------|-----|----------|-----------|
| System | Display | Mã tài sản | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Tên Tài sản | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Mô tả TS | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Trạng thái TS | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Phân nhóm TS (group name) | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Nhóm TS (CAT1) | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Số PO | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Tên nhà cung cấp | O | Ẩn hiện tùy biến | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Nguyên giá TS (VAT incl) | M | Ẩn hiện tùy biến | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Tên người sử dụng | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Tên đơn vị | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |
| System | Display | Đơn vị sử dụng cha | M | Hiển thị mặc định | Từ danh mục tài sản trong phiếu cấp |

**Quy trình cập nhật trạng thái:**

| Bước | Thực hiện | Hành động | Đối tượng | Trạng thái mới |
|------|-----------|-----------|-----------|---------------|
| 5 | Hệ thống | Update | RQ Cấp tài sản | Từ chối |
| 5 | Hệ thống | Update | RQ Xuất kho | Từ chối |
| 9 | Hệ thống | Update | RQ Cấp tài sản | Đã xác nhận |
| 9 | Hệ thống | Update | RQ Xuất kho | Chờ xác nhận |

**Yêu cầu nghiệp vụ:**
- Tìm kiếm yêu cầu xuất kho với 8 tiêu chí
- Hiển thị chi tiết 26 trường thông tin tài sản với tùy chọn ẩn/hiện
- Xử lý phê duyệt/từ chối với cập nhật trạng thái tự động
- Quản lý lock/unlock tài sản trong quá trình xử lý
- Gửi email thông báo tự động cho các bên liên quan
- Cập nhật tasklist cho các vai trò tương ứng

Sau khi phê duyệt, quy trình chuyển sang [nhận tài sản](#514-xuất-kho-từ-cấp-tài-sản-nhận-tài-sản).

---

### 5.14. Xuất kho từ cấp tài sản - Nhận tài sản

Bước cuối cùng trong quy trình xuất kho, cho phép Business User xác nhận nhận tài sản từ kho sau khi yêu cầu đã được [phê duyệt](#513-xuất-kho-từ-cấp-tài-sản-phê-duyệt-yêu-cầu-xuất-kho).

#### 5.14.1. Thông số kỹ thuật giao diện người dùng

![5.4.4a B6](images/5_4_4a_B6_image12.png)

**Các bước thực hiện quy trình:**

**Luồng chung (4 bước đầu):**
1. **Nhập thông tin tìm kiếm yêu cầu** - Form tìm kiếm yêu cầu
2. **Hiển thị kết quả tìm kiếm** - Danh sách yêu cầu chờ xác nhận
3. **Chọn yêu cầu cần xử lý** - Lựa chọn yêu cầu cụ thể
4. **Điểm quyết định "Xác nhận yêu cầu"** - Gateway với hai lựa chọn

**Luồng từ chối:**
5. **Cập nhật trạng thái yêu cầu** - Chuyển sang "Từ chối"
6. **Unlock tài sản** - Giải phóng tài sản
7. **Cập nhật tasklist** - Thông báo các bên liên quan
8. **Thông báo cho WK và AMP** - Gửi notification từ chối

**Luồng xác nhận:**
5. **Cập nhật trạng thái yêu cầu** - Chuyển sang "Đã nhận"
6. **Unlock tài sản** - Giải phóng tài sản
7. **Cập nhật tasklist** - Hoàn thành quy trình
8. **Thông báo cho WK và AMP** - Gửi notification hoàn thành

#### 5.14.2. Thông số kỹ thuật chi tiết

**Form tìm kiếm yêu cầu (Tasklist):**

| Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| Mã yêu cầu | M | Text | N | 20 | | | |
| Tiêu đề | M | Text | N | 150 | | | |
| Người tạo | M | List | N | 20 | | | |
| Trạng thái | M | List | N | 20 | | | |
| Ngày tạo | M | Date | N | 20 | | | |
| Nghiệp vụ kho | M | List | N | 100 | | | |
| Người xử lý | O | List | N | 20 | | | |
| Ngày xác nhận | O | Date | N | 20 | | | |

**Form tìm kiếm yêu cầu (User Input):**

| Operator | Field name VN | M/O | Field type | Editable | Max length |
|----------|---------------|-----|------------|----------|------------|
| User/Input | Mã yêu cầu | M | Text | Y | 20 |
| User/Input | Tiêu đề | M | Text | Y | 150 |
| User/Select | Người tạo | M | List | Y | 20 |
| User/Select | Trạng thái | M | List | Y | 20 |
| User/Input | Ngày tạo | M | Date | Y | 20 |
| User/Select | Nghiệp vụ kho | M | List | Y | 100 |
| User/Select | Người xử lý | M | List | Y | 20 |
| User/Input | Ngày xác nhận | M | Date | Y | 20 |

**Thông tin chung yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| System | Display | Số yêu cầu | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| System | Input | Tiêu đề | O | Text | Y | 150 | | | |

**Thông tin kho xuất:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | = Thông tin kho trên RQ cấp tài sản |
| System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | |
| System | Display | Quản lý kho | M | Text | N | 50 | OMS | |

**Thông tin đầu mối nhận hàng:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Đầu mối | M | Text | Y | 50 |
| User | Input | Số điện thoại | M | Number | Y | 52 |
| User | Input | Thời gian bàn giao | O | Date | Y | 50 |
| User | Input | Ghi chú | M | Text | Y | 150 |

**Yêu cầu nghiệp vụ:**
- Danh sách tài sản xuất kho phải bằng danh mục tài sản trong phiếu cấp/thanh lý
- Bắt buộc nhập lý do khi từ chối yêu cầu
- Tự động unlock tài sản khi từ chối để cho phép request khác sử dụng
- Cập nhật đơn vị sử dụng và clear thông tin kho khi xác nhận nhận tài sản
- Hỗ trợ hiển thị tùy biến cho một số trường thông tin (ẩn/hiện theo cấu hình)

---

### 5.15. Hủy Yêu Cầu Xuất Kho

Chức năng cho phép AMP (Asset Management Personnel) hủy các yêu cầu xuất kho chưa được xác nhận, áp dụng cho các yêu cầu được tạo từ [quy trình cấp tài sản](#511-tạo-yêu-cầu-xuất-kho).

#### 5.15.1. Thông số kỹ thuật giao diện người dùng

![5.5.1a B5](images/5_5_1a_B5_image13.png)

**Các bước thực hiện quy trình:**
1. **Nhập thông tin tìm kiếm yêu cầu** - Form tìm kiếm yêu cầu cần hủy
2. **Hiển thị kết quả tìm kiếm** - Danh sách yêu cầu phù hợp
3. **Chọn yêu cầu cần xử lý** - Lựa chọn yêu cầu cụ thể
4. **Điểm quyết định "Hủy"** với hai lựa chọn:
   - **"Thoát"** - Quay lại bước 3 hoặc kết thúc
   - **"Hủy"** - Tiếp tục với các bước:
     - Nhập lý do hủy (bắt buộc)
     - Cập nhật trạng thái yêu cầu thành "Đã hủy"
     - Unlock tài sản để có thể sử dụng cho yêu cầu khác
     - Cập nhật tasklist cho các bên liên quan
     - Thông báo cho WK về việc hủy yêu cầu

#### 5.15.2. Thông số kỹ thuật chi tiết

**Điều kiện hủy yêu cầu:**
- Yêu cầu xuất kho đã được tạo
- Yêu cầu có trạng thái khác "Đã xác nhận"

**Bảng tìm kiếm yêu cầu:**

| Trường | Loại | Bắt buộc | Max Length | Editable | Kiểu |
|--------|------|----------|------------|----------|------|
| Mã yêu cầu | User Input | M | 20 | Y | Text |
| Tiêu đề | User Input | M | 150 | Y | Text |
| Người tạo | User Select | M | 20 | Y | List |
| Trạng thái | User Select | M | 20 | Y | List |
| Ngày tạo | User Input | M | 20 | Y | Date |
| Nghiệp vụ kho | User Select | M | 100 | Y | List |
| Người xử lý | User Select | M | 20 | Y | List |
| Ngày xác nhận | User Input | M | 20 | Y | Date |

**Thông tin yêu cầu - Thông tin chung:**

| Trường | Operator | Action | Bắt buộc | Max Length | Format | Default | Data Rule |
|--------|----------|--------|----------|------------|--------|---------|-----------|
| Số yêu cầu | System | Display | M | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 |
| Ngày tạo | System | Display | M | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | System | Input | O | 150 | | | |

**Thông tin kho xuất:**

| Trường | Operator | Action | Bắt buộc | Max Length | Data Source | Data Rule |
|--------|----------|--------|----------|------------|-------------|-----------|
| Tên kho | System/User | Display/Search/Select | M | 50 | | Thông tin kho trên RQ cấp tài sản |
| Địa chỉ kho | System | Display | M | 50 | OMS | |
| Quản lý kho | System | Display | M | 50 | OMS | |

**Thông tin đầu mối nhận hàng:**

| Trường | Operator | Action | Bắt buộc | Max Length | Kiểu |
|--------|----------|--------|----------|------------|------|
| Đầu mối | User | Input | M | 50 | Text |
| Số điện thoại | User | Input | M | 52 | Number |
| Thời gian bàn giao | User | Input | O | 50 | Date |

**Logic nghiệp vụ:**
- Bắt buộc nhập lý do hủy (tối đa 150 ký tự)
- Hệ thống phải tự động unlock tài sản khi hủy yêu cầu
- Cập nhật trạng thái tài sản về trạng thái trước khi thanh lý
- Gửi email thông báo cho WK sau khi hủy
- Ẩn nút "Từ chối" đối với RQ xuất kho liên kết với RQ thanh lý

---

### 5.16. Điều chuyển tài sản giữa các kho - Tạo yêu cầu điều chuyển kho

Chức năng cho phép tạo yêu cầu điều chuyển tài sản từ kho này sang kho khác trong [Module Quản lý Kho](#52-module-quản-lý-kho).

#### 5.16.1. Thông số kỹ thuật giao diện người dùng

![5.6.1a B6](images/5_6_1a_B6_image14.png)

**Các bước thực hiện quy trình:**

**Bước khởi tạo:**
1. **Tạo yêu cầu điều chuyển** - Người dùng khởi tạo yêu cầu với thông tin tài sản và kho đích

**Điểm quyết định** với hai lựa chọn:
- **"Thoát"** - Kết thúc quy trình
- **"Gửi"** - Tiếp tục với chuỗi các bước tự động:

**Các bước xử lý tự động:**
2. **Lock tài sản** - Khóa tài sản để tránh xung đột
3. **Cập nhật trạng thái yêu cầu** - Chuyển sang "Chờ phê duyệt"
4. **Tìm và gán người phê duyệt** - Xác định approver theo quy tắc
5. **Cập nhật tasklist** - Phân công công việc cho các role
6. **Thông báo Warehouse Mgr.** - Gửi notification
7. **Chuyển sang phê duyệt** - Liên kết đến [quy trình 5.6.2a](#517-điều-chuyển-tài-sản-giữa-các-kho-phê-duyệt-yêu-cầu-điều-chuyển-kho)

#### 5.16.2. Thông số kỹ thuật chi tiết

**Thông tin chung yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| User | Select | Tạo | M | Button | N | | | | |
| System | Display | Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| User | Input | Tiêu đề | O | Text | Y | 150 | | | |
| User | Select | Thêm tài sản | M | Button | N | | | | |

**Form tìm kiếm tài sản:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Mã tài sản | O | Text | N | 20 |
| User | Input | Tên tài sản | O | Text | Y | 20 |
| User | Select | Phân loại tài sản | O | List | N | 20 |
| User | Select | Nhóm tài sản | O | List | N | 20 |
| User | Input | PO number | O | Text | Y | 20 |
| User | Select | Trạng thái TS | O | List | N | 50 |
| User | Select | Tên nhà cung cấp | O | List | N | 50 |
| User | Input | Tên kho | O | List | Y | 50 |
| User | Select | Vị trí đặt tài sản | O | Text | N | 100 |

**Thông tin kho:**

| Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|---------|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| Kho đi | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | |
| Kho đi | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Kho đi | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Kho nhập | User | Select | Tên kho | M | List | N | 50 | | |
| Kho nhập | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Kho nhập | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

**Thông tin đầu mối và quyết định:**

| Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|---------|----------|--------|---------------|-----|------------|----------|------------|
| Đầu mối giao hàng | User | Input | Đầu mối | M | Text | Y | 50 |
| Đầu mối giao hàng | User | Input | Số điện thoại | M | Number | Y | 52 |
| Đầu mối giao hàng | User | Input | Thời gian bàn giao | O | Date | Y | 50 |
| Ghi chú | User | Input | Ghi chú | M | Text | Y | 150 |
| Quyết định | User | Select | Gửi | M | Button | N | |
| Quyết định | User | Select | Hủy | M | Button | N | |

**Yêu cầu nghiệp vụ:**
- Tự động tạo số yêu cầu theo format CK.YY.xxxx
- Lock tài sản khi có yêu cầu để tránh xung đột
- Tích hợp với OMS để lấy thông tin kho và quản lý kho
- Hỗ trợ tùy biến hiển thị các trường thông tin
- Workflow tự động: lock asset → update status → assign approver → update tasklist → send notification

Sau khi gửi thành công, quy trình chuyển sang [phê duyệt yêu cầu điều chuyển kho](#517-điều-chuyển-tài-sản-giữa-các-kho-phê-duyệt-yêu-cầu-điều-chuyển-kho).

---

### 5.17. Điều chuyển tài sản giữa các kho - Phê duyệt yêu cầu điều chuyển kho

Quy trình phê duyệt yêu cầu điều chuyển tài sản giữa các kho được thực hiện sau khi [yêu cầu được tạo](#516-điều-chuyển-tài-sản-giữa-các-kho-tạo-yêu-cầu-điều-chuyển-kho).

#### 5.17.1. Thông số kỹ thuật giao diện người dùng

![5.6.2a B5](images/5_6_2a_B5_image15.png)

**Các bước thực hiện quy trình:**

**Luồng chung (3 bước đầu):**
1. **Nhập thông tin tìm kiếm yêu cầu** - Form tìm kiếm yêu cầu điều chuyển
2. **Hiển thị kết quả tìm kiếm** - Danh sách yêu cầu chờ phê duyệt
3. **Chọn yêu cầu cần xử lý** - Lựa chọn yêu cầu cụ thể để xem chi tiết

**Điểm quyết định phê duyệt** với hai hướng:

**Luồng từ chối:**
4. **Cập nhật trạng thái** - Chuyển sang "Từ chối"
5. **Thông báo cho WK khối đi và kho đến** - Gửi notification từ chối

**Luồng phê duyệt:**
4. **Cập nhật trạng thái yêu cầu** - Chuyển sang "Đã phê duyệt"
5. **Unlock tài sản** - Chuẩn bị cho việc điều chuyển
6. **Cập nhật tasklist** - Phân công công việc tiếp theo
7. **Thông báo cho WK** - Gửi notification
8. **Bàn giao tài sản** - Thực hiện điều chuyển vật lý
9. **Tạo biên bản xuất kho, nhập kho** - Tự động tạo documentation
10. **Cập nhật thông tin kho cho tài sản** - Cập nhật database
11. **Bàn giao tại sân** - Hoàn thành việc điều chuyển

#### 5.17.2. Thông số kỹ thuật chi tiết

**Form tìm kiếm yêu cầu:**

| Field name VN | M/O | Field type | Editable | Max length | Operator | Action |
|---------------|-----|------------|----------|------------|----------|---------|
| Số yêu cầu | O | Text | Y | 20 | User | Input |
| Ngày tạo | O | Date | Y | 20 | User | Input |
| Tiêu đề | O | Text | Y | 150 | User | Input |
| Người tạo | O | List | Y | 20 | User | Select |
| Trạng thái yêu cầu | O | List | Y | 20 | User | Select |
| Người xử lý | O | List | Y | 20 | User | Select |
| Ngày xác nhận | O | Date | Y | 20 | User | Input |

**Thông tin chung yêu cầu:**

| Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | O | Text | Y | 150 | | | |
| Thêm tài sản | M | Button | N | | | | |

**Form tìm kiếm tài sản:**

| Field name VN | M/O | Field type | Editable | Max length |
|---------------|-----|------------|----------|------------|
| Mã tài sản | O | Text | N | 20 |
| Tên tài sản | O | Text | Y | 20 |
| Phân loại tài sản | O | List | N | 20 |
| Nhóm tài sản | O | List | N | 20 |
| PO number | O | Text | Y | 20 |
| Trạng thái TS | O | List | N | 50 |
| Tên nhà cung cấp | O | List | N | 50 |
| Vị trí đặt tài sản | O | Text | N | 100 |

**Thông tin kho điều chuyển:**

| Loại kho | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|----------|---------------|-----|------------|----------|------------|-------------|-----------|
| Kho đi | Tên kho | M | List | N | 50 | | |
| Kho đi | Địa chỉ kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Kho đi | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Kho nhập | Tên kho | M | List | N | 50 | | |
| Kho nhập | Địa chỉ kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Kho nhập | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

**Thông tin đầu mối giao hàng:**

| Field name VN | M/O | Field type | Editable | Max length |
|---------------|-----|------------|----------|------------|
| Đầu mối | M | Text | N | 50 |
| Số điện thoại | M | Number | N | 52 |
| Thời gian bàn giao | O | Date | N | 50 |
| Ghi chú | M | Text | N | 150 |

**Yêu cầu nghiệp vụ:**
- Tìm kiếm yêu cầu điều chuyển theo nhiều tiêu chí
- Hiển thị chi tiết thông tin tài sản với khả năng cấu hình ẩn/hiện các trường
- Cho phép Approver từ chối (yêu cầu nhập lý do) hoặc phê duyệt yêu cầu
- Tự động tạo biên bản điều chuyển khi phê duyệt
- Cập nhật trạng thái lock/unlock tài sản theo từng bước xử lý
- Quản lý tasklist và thông báo email tự động
- Lưu trữ lịch sử xử lý và quá trình phê duyệt

---

## 6. System Status Matrix

Hệ thống trạng thái được thiết kế để theo dõi cả **Request Status** (trạng thái yêu cầu) và **Asset Status** (trạng thái tài sản) trong toàn bộ vòng đời từ cấp phát đến thanh lý. Bảng dưới đây định nghĩa các trạng thái và luồng chuyển đổi cho từng quy trình chính.

### 6.1. Ma trận trạng thái - Cấp tài sản không ở kho

| Sub-process | PIC | Action | Request Status | Asset Status | Note |
|-------------|-----|--------|----------------|--------------|------|
| 1 Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - |
| 1 Tạo yêu cầu | AMP | Gửi | Chờ xác nhận | - | - |
| 2. Xác nhận | BU User | Từ chối | Từ chối | - | - |
| 2. Xác nhận | BU User | Xác nhận | Đã xác nhận | Đang sử dụng | Đã xác nhận >>> Đã nhận tài sản |
| 2. Xác nhận | BU User | Bổ sung thông tin | Bổ sung thông tin | - | - |
| 3. Bổ sung TT | AMP | Bổ sung thông tin | Chờ xác nhận | - | - |

### 6.2. Ma trận trạng thái - Cấp tài sản từ kho

| Sub-process | PIC | Action | Request Status | Warehouse Status | Asset Status |
|-------------|-----|--------|----------------|------------------|--------------|
| 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - |
| 1. Tạo yêu cầu | AMP | Gửi | Chờ xác nhận | - | - |
| 2. Phê duyệt | AM | Từ chối | Từ chối | - | - |
| 2. Phê duyệt | AM | Duyệt | Đã xác nhận | - | - |
| 3. Tạo yêu cầu | System | - | Đã xác nhận | Chờ xuất kho | - |
| 4. Xuất kho | WK | Từ chối | Từ chối | Từ chối | - |
| 4. Xuất kho | WK | Đồng ý | Đã xác nhận | Chờ phê duyệt | - |
| 5. Phê duyệt | Warehouse Mgr. | Từ chối | Từ chối | Từ chối | - |
| 5. Phê duyệt | Warehouse Mgr. | Duyệt | Đã xác nhận | Chờ xác nhận | - |
| 6. Nhận hàng | BU User | Từ chối | Từ chối | Từ chối | - |
| 6. Nhận hàng | BU User | Xác nhận | Đã xác nhận | Đã nhận tài sản | Đang sử dụng |

### 6.3. Ma trận trạng thái - Thanh lý tài sản (Bán trực tiếp)

| Sub-process | PIC | Action | Request Status | Warehouse Status | Asset Status | Note |
|-------------|-----|--------|----------------|------------------|--------------|------|
| 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - | - |
| 1. Tạo yêu cầu | AMP | Gửi | Chờ kiểm soát | - | - | - |
| 2. Kiểm soát | Checker | Từ chối | Từ chối | - | - | - |
| 2. Kiểm soát | Checker | Yêu cầu bổ sung thông tin | Bổ sung thông tin | - | - | - |
| 2. Kiểm soát | Checker | Đồng ý | Chờ phê duyệt | - | - | - |
| 3. Phê duyệt | Approver | Từ chối | Đang tạo | - | - | - |
| 3. Phê duyệt | Approver | Yêu cầu bổ sung thông tin | Bổ sung thông tin | - | - | - |
| 3. Phê duyệt | Approver | Phê duyệt | Chờ cập nhật kết quả | - | - | - |
| 4. Cập nhật kết quả thanh lý | AMP | Hủy | Đã hủy | - | - | - |
| 4. Cập nhật kết quả thanh lý | AMP | Cập nhật kết quả | Đã cập nhật kết quả thanh lý | - | Đã thanh lý | - |
| 5. Tạo yêu cầu xuất kho | System | Send | Đã cập nhật kết quả thanh lý | Chờ xuất kho | Đã thanh lý | - |
| 5.1 View yêu cầu xuất kho | AMP | Hủy | Đã hủy | Đã hủy | Trả lại trạng thái ban đầu trước khi thanh lý | - |

### 6.4. Yêu cầu hệ thống

- Hệ thống phải hỗ trợ các trạng thái yêu cầu: **Đang tạo**, **Chờ xác nhận**, **Đã xác nhận**, **Từ chối**, **Bổ sung thông tin**
- Hệ thống phải theo dõi trạng thái tài sản

---

## Phụ lục: Hình ảnh bổ sung

Các hình ảnh sau được trích xuất từ tài liệu gốc nhưng chưa được đặt vào nội dung chính:

![filename](images/filename)



---

*Generated by Claude Sonnet 4.5 from 37 sheet summaries*
*Headings: 70 | Internal Links: 79 | Images: 16*

*⚠️ Link validation warnings - some links may need manual review*
*✅ All image tokens converted successfully*
