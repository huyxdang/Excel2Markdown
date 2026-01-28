# Tài Liệu Yêu Cầu Nghiệp vụ (BRD) - FAM Wave 4

---

## 1. Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Project Scope & Objectives](#2-project-scope-objectives)
3. [Stakeholders](#3-stakeholders)
4. [Business Requirements](#4-business-requirements)
   - 4.1. [Dashboard Tài Sản](#41-dashboard-tài-sản)
   - 4.2. [Module Quản lý Kho](#42-module-quản-lý-kho)
   - 4.3. [Điều chuyển về kho - Tạo yêu cầu nhập kho](#43-điều-chuyển-về-kho-tạo-yêu-cầu-nhập-kho)
   - 4.4. [Nhập kho từ quy trình điều chuyển về kho - Phê duyệt](#44-nhập-kho-từ-quy-trình-điều-chuyển-về-kho-phê-duyệt)
   - 4.5. [Nhập kho từ quy trình điều chuyển về kho - Xác nhận](#45-nhập-kho-từ-quy-trình-điều-chuyển-về-kho-xác-nhận)
   - 4.6. [NHẬP KHO THỦ CÔNG - Tạo yêu cầu](#46-nhập-kho-thủ-công-tạo-yêu-cầu)
   - 4.7. [NHẬP KHO THỦ CÔNG - Phê duyệt](#47-nhập-kho-thủ-công-phê-duyệt)
   - 4.8. [Nhập kho thủ công - Xác nhận nhập kho](#48-nhập-kho-thủ-công-xác-nhận-nhập-kho)
   - 4.9. [HỦY YÊU CẦU NHẬP KHO](#49-hủy-yêu-cầu-nhập-kho)
   - 4.10. [Cấp tài sản - Phê duyệt](#410-cấp-tài-sản-phê-duyệt)
   - 4.11. [Cấp tài sản - Tạo yêu cầu xuất kho](#411-cấp-tài-sản-tạo-yêu-cầu-xuất-kho)
   - 4.12. [Xuất kho từ cấp tài sản - Tiếp nhận](#412-xuất-kho-từ-cấp-tài-sản-tiếp-nhận)
   - 4.13. [Xuất kho từ cấp tài sản - Phê duyệt](#413-xuất-kho-từ-cấp-tài-sản-phê-duyệt)
   - 4.14. [Xuất kho từ cấp tài sản - Nhận tài sản](#414-xuất-kho-từ-cấp-tài-sản-nhận-tài-sản)
   - 4.15. [HỦY YÊU CẦU XUẤT KHO](#415-hủy-yêu-cầu-xuất-kho)
   - 4.16. [Điều chuyển kho - Tạo yêu cầu](#416-điều-chuyển-kho-tạo-yêu-cầu)
   - 4.17. [Điều chuyển kho - Phê duyệt](#417-điều-chuyển-kho-phê-duyệt)
   - 4.18. [Phê duyệt yêu cầu điều chuyển tài sản giữa các kho](#418-phê-duyệt-yêu-cầu-điều-chuyển-tài-sản-giữa-các-kho)
   - 4.19. [Status - Ma trận trạng thái](#419-status-ma-trận-trạng-thái)
   - 4.20. [Tasklist - Ma trận phân bổ công việc](#420-tasklist-ma-trận-phân-bổ-công-việc)
5. [Assumptions & Constraints](#5-assumptions-constraints)
6. [Dependencies](#6-dependencies)
7. [Acceptance Criteria](#7-acceptance-criteria)
8. [Glossary](#8-glossary)

---

## 1. Executive Summary

Dự án FAM (Fixed Asset Management) Wave 4 tập trung vào việc nâng cấp và mở rộng hệ thống quản lý tài sản cố định với 11 yêu cầu chính được phân loại theo 4 mức độ ưu tiên. Các sản phẩm chính bao gồm [4.1. Dashboard Tài Sản](#41-dashboard-tài-sản) với khả năng visualize và customize cao, [4.2. Module Quản lý Kho](#42-module-quản-lý-kho) toàn diện và module sửa chữa tài sản tích hợp với ITSM.

Dự án sẽ cải tiến đáng kể trải nghiệm người dùng thông qua dashboard tương tác với 4 KPI cốt lõi và khả năng drill-down theo nhiều góc độ. Đồng thời, hệ thống sẽ tự động hóa các quy trình nghiệp vụ như phê duyệt phiếu cấp tài sản sau 20 ngày và tối ưu hóa hiển thị danh sách tài sản.

Hai module mới quan trọng sẽ được phát triển: [4.2. Module Quản lý Kho](#42-module-quản-lý-kho) xử lý xuất-nhập kho tự động từ các yêu cầu cấp phát, thanh lý, điều chuyển với độ ưu tiên cao nhất, và module sửa chữa tài sản tích hợp với ITSM và Cổng hỗ trợ chi nhánh. Hệ thống cũng được tích hợp với OMS (tự động đồng bộ khi orgchart thay đổi) và EMS (đồng bộ tiêu đề PO, thông tin thời gian bảo hành).

---

## 2. Project Scope & Objectives

### Trong phạm vi dự án:
- Dashboard tài sản với khả năng visualize và customize theo nhiều tiêu chí
- Tối ưu hóa hiển thị danh sách tài sản với khả năng ẩn/hiện tùy chọn
- Upload phiếu cấp tài sản theo danh sách
- Tự động xác nhận phiếu cấp tài sản sau 20 ngày không phản hồi
- Module kho toàn diện xử lý xuất-nhập kho tài sản
- Module sửa chữa tài sản tích hợp với ITSM
- Tích hợp với hệ thống OMS và EMS

### Ngoài phạm vi:
- Thay đổi cấu trúc dữ liệu cơ bản của hệ thống hiện tại
- Tích hợp với các hệ thống khác ngoài OMS, EMS và ITSM

### Mục tiêu dự án:
- Nâng cao hiệu quả quản lý tài sản thông qua tự động hóa
- Cung cấp thông tin tổng quan và chi tiết về tài sản qua dashboard
- Tối ưu hóa quy trình xuất-nhập kho tài sản
- Tăng cường khả năng theo dõi và báo cáo tài sản
- Cải thiện trải nghiệm người dùng và giảm thời gian xử lý

---

## 3. Stakeholders

### Vai trò chính trong hệ thống:
- **AMP (Asset Management Personnel)**: Nhân viên quản lý tài sản, xử lý các yêu cầu và quy trình
- **BU User (Business Unit User)**: Người dùng đơn vị kinh doanh, khởi tạo yêu cầu cấp phát tài sản
- **BU Head (Business Unit Head)**: Trưởng đơn vị kinh doanh, phê duyệt yêu cầu
- **AM (Asset Manager)**: Quản lý tài sản, phê duyệt các yêu cầu cấp cao
- **WK (Warehouse Keeper)**: Thủ kho, thực hiện xuất-nhập kho thực tế
- **Warehouse Manager (WM)**: Quản lý kho, phê duyệt các yêu cầu xuất-nhập kho
- **Checker**: Kiểm soát viên trong quy trình thanh lý tài sản
- **Approver**: Người phê duyệt cuối cùng trong các quy trình quan trọng

### Hệ thống liên kết:
- **OMS (Organization Management System)**: Hệ thống quản lý tổ chức, đồng bộ dữ liệu đơn vị
- **EMS**: Hệ thống quản lý đơn hàng, đồng bộ thông tin PO và bảo hành
- **ITSM (IT Service Management)**: Hệ thống quản lý dịch vụ IT
- **Cổng hỗ trợ chi nhánh**: Hệ thống hỗ trợ trên intranet

---

## 4. Business Requirements

### 4.1. Dashboard Tài Sản

![Dashboard Tài Sản](images/dashboard_overview.png)

Dashboard tài sản được thiết kế để cung cấp giao diện tổng quan và trực quan hóa dữ liệu nhằm hỗ trợ đưa ra quyết định nhanh chóng. Hệ thống hiển thị thông tin tài sản theo nhiều chiều dimension như phòng ban theo orgchart, trạng thái tài sản, biến động theo thời gian, tỷ lệ sử dụng, và đặc biệt quan tâm đến các tài sản hết bảo hành hoặc có thời gian sử dụng trên 3-5 năm.

Dashboard bao gồm 4 KPI cốt lõi với công thức tính toán cụ thể, bộ lọc đa tiêu chí cho phép drill-down theo nhiều góc độ, và các biểu đồ tương tác đa dạng (tròn, cột, đường, scatter) với khả năng hover xem chi tiết và chuyển đổi sang các module liên quan. Hệ thống tích hợp với [OMS](#3-stakeholders) để đồng bộ dữ liệu đơn vị sử dụng và hỗ trợ xuất dữ liệu ra Excel.

#### Bảng KPI Dashboard Tổng Quan
| STT | Content | Value | Công thức tính |
|-----|---------|-------|----------------|
| 1 | Total assets | Count số lượng | All tài sản - Đã thanh lý - Vô hiệu hóa |
| 2 | Total value | Sum nguyên giá | All tài sản - Đã thanh lý - Vô hiệu hóa |
| 3 | Warranty status | Tỷ lệ phần trăm | Số lượng tài sản còn hạn bảo hành/(All tài sản - Vô hiệu hóa - Đã thanh lý) |
| 4 | Utilization rate | Tỷ lệ phần trăm | Số lượng tài sản đang sử dụng/(All tài sản - Vô hiệu hóa - Đã thanh lý) |

#### Bảng Bộ Lọc Dùng Chung
| STT | Tiêu chí lọc | Kiểu dữ liệu | Nguồn dữ liệu |
|-----|--------------|--------------|---------------|
| 1 | Vùng | LOV | - |
| 2 | Đơn vị sử dụng | LOV | Đồng bộ từ OMS |
| 3 | CAT 1 | LOV | - |
| 4 | Group name | LOV | - |
| 5 | Asset status | LOV | Không bao gồm Đã thanh lý, Vô hiệu hóa |

#### Bảng Đặc Tả Biểu Đồ
| STT | Tên biểu đồ | Dữ liệu hiển thị | Loại biểu đồ | Ghi chú |
|-----|-------------|------------------|--------------|---------|
| 1 | Asset Distribution - Cơ cấu theo trạng thái | Nguyên giá | Sunburst | Vòng trong: Nhóm IT/ADM/CMD, Vòng ngoài: Trạng thái. Hover hiện số lượng và giá trị |
| 2 | Asset Distribution - Cơ cấu theo Vùng/Đơn vị | Nguyên giá | Stacked Column | - |
| 3 | Asset Value by Group Name | Nguyên giá | Column | - |
| 4 | Asset Fluctuation Over Time | Nguyên giá | Line | Theo Month/Year |
| 5 | Asset by Time in Use | Số lượng | Scatter | - |

---

### 4.2. Module Quản lý Kho

Module này là trọng tâm của dự án FAM Wave 4, bao gồm các quy trình nghiệp vụ chính được so sánh giữa trạng thái hiện tại (As-is) và trạng thái mong muốn (To-be). Hệ thống được thiết kế với sự tự động hóa cao trong phiên bản To-be, tự động tạo các yêu cầu nhập/xuất kho sau khi có sự duyệt từ các bước trước, giảm thiểu can thiệp thủ công và tăng tính nhất quán.

Các quy trình chính bao gồm:
- [4.3. Điều chuyển nội bộ và chéo về kho](#43-điều-chuyển-về-kho-tạo-yêu-cầu-nhập-kho)
- [4.6. Nhập kho (tự động và thủ công)](#46-nhập-kho-thủ-công-tạo-yêu-cầu)
- [4.9. Hủy nhập kho](#49-hủy-yêu-cầu-nhập-kho)
- [4.11. Cấp tài sản và xuất kho](#411-cấp-tài-sản-tạo-yêu-cầu-xuất-kho)
- [4.15. Thanh lý tài sản và hủy xuất kho](#415-hủy-yêu-cầu-xuất-kho)
- [4.16. Điều chuyển giữa các kho](#416-điều-chuyển-kho-tạo-yêu-cầu)

Mỗi quy trình được thiết kế với các checkpoint duyệt/từ chối rõ ràng, cho phép quay lại bước trước khi cần thiết. Hệ thống tích hợp chặt chẽ giữa các module, khi hủy một yêu cầu sẽ tự động ảnh hưởng đến các yêu cầu liên quan, đảm bảo tính toàn vẹn dữ liệu và quy trình nghiệp vụ.

**Yêu cầu chính:**
- Tự động tạo yêu cầu nhập kho sau khi xác nhận điều chuyển về kho
- Tự động tạo yêu cầu xuất kho sau khi duyệt cấp tài sản hoặc thanh lý tài sản
- Tự động hủy các yêu cầu liên quan khi hủy yêu cầu chính
- Tự động tạo biên bản và bút toán cho các giao dịch xuất/nhập kho
- AMP có thể xem và thao tác các yêu cầu như người khởi tạo khi yêu cầu bị từ chối

---

### 4.3. Điều chuyển về kho - Tạo yêu cầu nhập kho

![Giao diện tạo yêu cầu nhập kho](images/5_1_1a_B5_image1.png)

#### 4.3.1. Thông số kỹ thuật giao diện người dùng

Quy trình tự động tạo yêu cầu nhập kho khi có điều chuyển tài sản về kho. Hệ thống sẽ tự động sinh ra yêu cầu nhập kho với đầy đủ thông tin tài sản từ request điều chuyển ban đầu, bao gồm thông tin cơ bản về tài sản, thông tin kho đích và đầu mối giao nhận.

Giao diện cho phép AMP (Asset Management Personnel) tìm kiếm và chọn yêu cầu điều chuyển, sau đó có thể thực hiện các hành động như từ chối, xác nhận hoặc yêu cầu bổ sung thông tin. Khi AMP xác nhận yêu cầu, hệ thống sẽ tự động tạo yêu cầu nhập kho theo [4.4. quy trình phê duyệt](#44-nhập-kho-từ-quy-trình-điều-chuyển-về-kho-phê-duyệt).

#### 4.3.2. Thông số kỹ thuật chi tiết

Quy trình bao gồm 4 bước chính: (1) Tạo yêu cầu nhập kho với các trường thông tin được map tự động, (2) Cập nhật trạng thái các yêu cầu liên quan, (3) Cập nhật tasklist cho AMP và WM, và (4) Gửi thông báo email cho Warehouse Manager.

Hệ thống có cơ chế lock/unlock tài sản để đảm bảo tính nhất quán dữ liệu: tài sản được unlock khỏi RQ điều chuyển khi hoàn thành và lock bởi RQ nhập kho mới tạo. Thông tin tài sản chỉ được cập nhật khi RQ nhập kho hoàn thành thông qua [4.5. quy trình xác nhận](#45-nhập-kho-từ-quy-trình-điều-chuyển-về-kho-xác-nhận).

### Bảng field specifications cho form tạo yêu cầu nhập kho:

| Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|-------------|----------|---------|---------------|-----|------------|----------|------------|---------|---------------|-----------|
| Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| | System | Display | Tiêu đề | M | Text | N | 150 | | | =Tiêu đề RQ điều chuyển |
| DS tài sản nhập kho | System | Display | Mã tài sản | M | | N | | | | Hiển thị mặc định |
| | System | Display | Tên Tài sản | M | | N | | | | Hiển thị mặc định |
| | System | Display | Mô tả TS | M | | N | | | | Hiển thị mặc định |
| | System | Display | Trạng thái TS | M | | N | | | | Hiển thị mặc định |
| | System | Display | Phân nhóm TS (group name) | M | | N | | | | Hiển thị mặc định |
| | System | Display | Nhóm TS (CAT1) | M | | N | | | | Hiển thị mặc định |
| | System | Display | Số PO | M | | N | | | | Hiển thị mặc định |
| | System | Display | Tên nhà cung cấp | O | | N | | | | Ẩn hiện tùy biến |
| | System | Display | Nguyên giá TS (VAT incl) | M | | N | | | | Ẩn hiện tùy biến |
| | System | Display | Tên người sử dụng | M | | N | | | | Hiển thị mặc định |
| | System | Display | Tên đơn vị | M | | N | | | | Hiển thị mặc định |
| Thông tin kho nhập | System | Display | Tên kho | M | List | N | 50 | | | = Kho trong RQ điều chuyển |
| | System | Display | Địa chỉ kho | M | Text | N | 50 | | | Tự động nhận diện, hiển thị theo Tên kho |
| | System | Display | Quản lý kho | M | Text | N | 50 | | | Tự động nhận diện (Tên \| Phòng ban \| Email) |
| Thông tin đầu mối giao hàng | User | Input | Đầu mối | M | Text | N | 50 | | | = Đầu mối giao hàng trong RQ điều chuyển |
| | User | Input | Số điện thoại | M | Number | N | 52 | | | |
| | User | Input | Thời gian bàn giao | O | Date | N | 50 | | | |

---

### 4.4. Nhập kho từ quy trình điều chuyển về kho - Phê duyệt

![Giao diện phê duyệt yêu cầu nhập kho](images/5.1.2a_B6_image2.png)

#### 4.4.1. Thông số kỹ thuật giao diện người dùng

Giao diện này cho phép Warehouse Manager xem xét và phê duyệt các yêu cầu nhập kho được tạo từ [4.3. quy trình điều chuyển về kho](#43-điều-chuyển-về-kho-tạo-yêu-cầu-nhập-kho). Quy trình bao gồm việc tìm kiếm yêu cầu thông qua các tiêu chí như số yêu cầu, ngày tạo, tiêu đề, người tạo và trạng thái, sau đó hiển thị danh sách kết quả để lựa chọn và xem xét.

Sau khi phê duyệt, quy trình sẽ chuyển sang [4.5. bước xác nhận nhập kho](#45-nhập-kho-từ-quy-trình-điều-chuyển-về-kho-xác-nhận) bởi Warehouse Keeper. Nếu từ chối, hệ thống sẽ tự động unlock tài sản và thông báo cho các bên liên quan.

#### 4.4.2. Thông số kỹ thuật chi tiết

Giao diện chi tiết yêu cầu hiển thị đầy đủ thông tin tài sản bao gồm thông tin cơ bản, thông tin người sử dụng, vị trí đặt tài sản, thông tin bảo hành, thông tin kho nhập và đầu mối giao hàng. Ngoài ra còn có các phần hiển thị hồ sơ đính kèm, quá trình xử lý và lịch sử thao tác.

### Bảng thông tin tìm kiếm yêu cầu
| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

### Bảng thông tin kho và giao hàng
| Section | Field name VN | M/O | Field type | Max length | Data source | Data rule |
|---------|---------------|-----|------------|------------|-------------|-----------|
| Thông tin kho nhập | Tên kho | M | List | 50 | - | - |
| | Địa chỉ kho | M | Text | 50 | OMS | Tự động nhận diện theo Tên kho |
| | Quản lý kho | M | Text | 50 | OMS | Hiển thị: Tên \| Phòng ban \| Email |
| Thông tin đầu mối giao hàng | Đầu mối | M | Text | 50 | - | - |
| | Số điện thoại | M | Number | 52 | - | - |
| | Thời gian bàn giao | O | Date | 50 | - | - |

---

### 4.5. Nhập kho từ quy trình điều chuyển về kho - Xác nhận

![Giao diện xác nhận nhập kho](images/warehouse_confirmation.png)

#### 4.5.1. Thông số kỹ thuật giao diện người dùng

Màn hình xác nhận nhập kho là bước cuối cùng trong [4.3. quy trình điều chuyển về kho](#43-điều-chuyển-về-kho-tạo-yêu-cầu-nhập-kho), được thực hiện bởi Warehouse Keeper sau khi [4.4. Warehouse Manager đã phê duyệt](#44-nhập-kho-từ-quy-trình-điều-chuyển-về-kho-phê-duyệt). Giao diện cho phép xem xét thông tin hàng hóa được điều chuyển và thực hiện xác nhận để hoàn tất việc nhập kho.

#### 4.5.2. Thông số kỹ thuật chi tiết

Giao diện được thiết kế với các phần chính: form tìm kiếm yêu cầu, danh sách kết quả, thông tin chi tiết yêu cầu bao gồm danh sách tài sản, thông tin kho nhập, đầu mối giao hàng, hồ sơ đính kèm, và lịch sử xử lý. Khi xác nhận nhập kho, hệ thống tự động cập nhật "Ngày bắt đầu sử dụng" nếu trường này = N/A, unlock tài sản, cập nhật thông tin kho và gửi thông báo cho AMP và BU.

### Bảng thông tin tìm kiếm yêu cầu
| Trường | Operator | Action | Kiểu dữ liệu | Bắt buộc | Có thể chỉnh sửa | Độ dài tối đa |
|--------|----------|--------|--------------|----------|------------------|----------------|
| Số yêu cầu | User | Input | Text | O | Y | 20 |
| Ngày tạo | User | Input | Date | O | Y | 20 |
| Tiêu đề | User | Input | Text | O | Y | 150 |
| Người tạo | User | Select | List | O | Y | 20 |
| Trạng thái yêu cầu | User | Select | List | O | Y | 20 |
| Người xử lý | User | Select | List | O | Y | 20 |
| Ngày xác nhận | User | Input | Date | O | Y | 20 |

### Bảng thông tin kho và đầu mối
| Trường | Operator | Action | Kiểu dữ liệu | Bắt buộc | Có thể chỉnh sửa | Độ dài | Nguồn dữ liệu/Quy tắc |
|--------|----------|--------|--------------|----------|------------------|--------|----------------------|
| Tên kho | System | Display | List | M | N | 50 | - |
| Địa chỉ kho | System | Display | Text | M | Y | 50 | OMS - Tự động nhận diện theo Tên kho |
| Quản lý kho | System | Display | Text | M | N | 50 | OMS - Hiển thị: Tên \| Phòng ban \| Email |
| Đầu mối | System | Display | Text | M | Y | 50 | - |
| Số điện thoại | System | Display | Number | M | Y | 52 | - |
| Thời gian bàn giao | System | Display | Date | O | Y | 50 | - |

---

### 4.6. NHẬP KHO THỦ CÔNG - Tạo yêu cầu

![Giao diện nhập kho thủ công](images/5.2.1a_B5.png)

#### 4.6.1. Thông số kỹ thuật giao diện người dùng

Chức năng nhập kho thủ công cho phép người dùng khởi tạo các yêu cầu nhập kho một cách thủ công thay vì tự động như trong [4.3. quy trình điều chuyển về kho](#43-điều-chuyển-về-kho-tạo-yêu-cầu-nhập-kho). Giao diện hỗ trợ tìm kiếm tài sản theo nhiều tiêu chí và cho phép người dùng tự chọn tài sản cần nhập kho.

#### 4.6.2. Thông số kỹ thuật chi tiết

Giao diện được chia thành các phần chính: thông tin chung (số yêu cầu, ngày tạo, tiêu đề), phần tìm kiếm và chọn tài sản với nhiều tiêu chí lọc, danh sách kết quả hiển thị thông tin chi tiết của tài sản. Hệ thống hỗ trợ tìm kiếm tài sản theo mã, tên, phân loại, nhóm, PO number, trạng thái, nhà cung cấp, kho và vị trí.

Sau khi chọn tài sản, người dùng cần nhập thông tin kho nhập, thông tin đầu mối giao hàng, ghi chú và đính kèm hồ sơ. Hệ thống thực hiện lock tài sản, cập nhật trạng thái yêu cầu và gửi thông báo cho [4.7. Warehouse Manager để phê duyệt](#47-nhập-kho-thủ-công-phê-duyệt).

### Bảng thông tin các trường trong form tạo yêu cầu:

| STT | Tab/Section | Operator | Action | Field Name | M/O | Field Type | Editable | Max Length | Format | Default | Data Rule |
|-----|-------------|----------|--------|------------|-----|------------|----------|------------|--------|---------|-----------|
| 1 | Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| 2 | Thông tin chung | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| 3 | Thông tin chung | User | Input | Tiêu đề | O | Text | Y | 150 | | | |
| 4 | Tìm kiếm tài sản | User | Input | Mã tài sản | O | Text | N | 20 | | | |
| 5 | Tìm kiếm tài sản | User | Input | Tên tài sản | O | Text | Y | 20 | | | |
| 6 | Tìm kiếm tài sản | User | Select | Phân loại tài sản | O | List | N | 20 | | | |
| 7 | Tìm kiếm tài sản | User | Select | Nhóm tài sản | O | List | N | 20 | | | |
| 8 | Tìm kiếm tài sản | User | Input | PO number | O | Text | Y | 20 | | | |
| 9 | Tìm kiếm tài sản | User | Select | Trạng thái TS | O | List | N | 50 | | | |
| 10 | Tìm kiếm tài sản | User | Select | Tên nhà cung cấp | O | List | N | 50 | | | |
| 11 | Tìm kiếm tài sản | User | Input | Tên kho | O | List | Y | 50 | | | |
| 12 | Tìm kiếm tài sản | User | Select | Vị trí đặt tài sản | O | Text | N | 100 | | | |

### Bảng thông tin kho nhập và đầu mối:

| Tab/Section | Operator | Action | Field Name | M/O | Field Type | Editable | Max Length | Data Source | Data Rule |
|-------------|----------|--------|------------|-----|------------|----------|------------|-------------|-----------|
| Thông tin kho nhập | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | |
| Thông tin kho nhập | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Thông tin kho nhập | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện (Tên \| Phòng ban \| Email) |
| Thông tin đầu mối | User | Input | Đầu mối | M | Text | Y | 50 | | |
| Thông tin đầu mối | User | Input | Số điện thoại | M | Number | Y | 52 | | |
| Thông tin đầu mối | User | Input | Thời gian bàn giao | O | Date | Y | 50 | | |

---

### 4.7. NHẬP KHO THỦ CÔNG - Phê duyệt

![Giao diện phê duyệt nhập kho thủ công](images/5.2.2a_B5.png)

#### 4.7.1. Thông số kỹ thuật giao diện người dùng

Màn hình này cho phép Warehouse Manager xem xét và phê duyệt các yêu cầu nhập kho thủ công được tạo từ [4.6. quy trình tạo yêu cầu](#46-nhập-kho-thủ-công-tạo-yêu-cầu). Giao diện cung cấp đầy đủ thông tin để hỗ trợ việc ra quyết định phê duyệt.

#### 4.7.2. Thông số kỹ thuật chi tiết

Quy trình phê duyệt bắt đầu với việc tìm kiếm yêu cầu theo nhiều tiêu chí, sau đó hiển thị danh sách kết quả để chọn và xem chi tiết. Warehouse Manager có thể thực hiện hai hành động chính là "Từ chối" (kèm lý do) hoặc "Phê duyệt" (kèm ghi chú). Sau quyết định, hệ thống cập nhật trạng thái yêu cầu, unlock tài sản nếu từ chối, cập nhật tasklist và gửi thông báo email.

Khi được phê duyệt, yêu cầu sẽ chuyển sang [4.8. bước xác nhận nhập kho](#48-nhập-kho-thủ-công-xác-nhận-nhập-kho) bởi Warehouse Keeper.

### Bảng tìm kiếm yêu cầu
| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max length |
|--------|----------|--------|------------|-----|------|----------|------------|
| Tìm kiếm yêu cầu | User | Input | Số yêu cầu | O | Text | Y | 20 |
| | User | Input | Ngày tạo | O | Date | Y | 20 |
| | User | Input | Tiêu đề | O | Text | Y | 150 |
| | User | Select | Người tạo | O | List | Y | 20 |
| | User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| | User | Select | Người xử lý | O | List | Y | 20 |
| | User | Input | Ngày xác nhận | O | Date | Y | 20 |

### Bảng thông tin kho và giao hàng
| Section | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max length | Data rule |
|---------|----------|--------|------------|-----|------|----------|------------|-----------|
| Thông tin kho nhập | System | Display | Tên kho | M | List | N | 50 | |
| | System | Display | Địa chỉ kho | M | Text | Y | 50 | Tự động nhận diện theo Tên kho |
| | System | Display | Quản lý kho | M | Text | N | 50 | Hiển thị: Tên \| Phòng ban \| Email |
| Thông tin đầu mối giao hàng | System | Display | Đầu mối | M | Text | Y | 50 | |
| | System | Display | Số điện thoại | M | Number | Y | 52 | |
| | System | Display | Thời gian bàn giao | O | Date | Y | 50 | |

---

### 4.8. Nhập kho thủ công - Xác nhận nhập kho

![Giao diện xác nhận nhập kho thủ công](images/5.2.3a_B6_image6.png)

#### 4.8.1. Thông số kỹ thuật giao diện người dùng

Màn hình xác nhận nhập kho thủ công là bước cuối trong quy trình [4.6. nhập kho thủ công](#46-nhập-kho-thủ-công-tạo-yêu-cầu), được thực hiện bởi Warehouse Keeper sau khi [4.7. Warehouse Manager phê duyệt](#47-nhập-kho-thủ-công-phê-duyệt). Giao diện đảm bảo tính chính xác và kiểm soát trong quá trình nhập hàng.

#### 4.8.2. Thông số kỹ thuật chi tiết

Quy trình xác nhận bao gồm 3 phần chính: tìm kiếm yêu cầu, xem chi tiết yêu cầu và đưa ra quyết định. Giao diện hiển thị thông tin chi tiết tài sản với hơn 20 thuộc tính, thông tin kho nhập, đầu mối giao hàng, hồ sơ đính kèm và lịch sử xử lý.

Nhân viên kho có thể đưa ra quyết định từ chối hoặc xác nhận nhập kho, kèm theo các cập nhật tự động về trạng thái và thông báo. Khi xác nhận, hệ thống tự động cập nhật "Ngày bắt đầu sử dụng" nếu trường này = N/A và unlock tài sản khi từ chối.

### Bảng tìm kiếm yêu cầu
| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|---------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

### Bảng thông tin kho và đầu mối
| Section | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|---------|---------------|-----|------------|----------|------------|-------------|-----------|
| Thông tin kho nhập | Tên kho | M | List | N | 50 | - | - |
| | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Thông tin đầu mối giao hàng | Đầu mối | M | Text | Y | 50 | - | - |
| | Số điện thoại | M | Number | Y | 52 | - | - |
| | Thời gian bàn giao | O | Date | Y | 50 | - | - |

---

### 4.9. HỦY YÊU CẦU NHẬP KHO

![Giao diện hủy yêu cầu nhập kho](images/5_3_1a_B5_image7.png)

#### 4.9.1. Thông số kỹ thuật giao diện người dùng

Chức năng hủy yêu cầu nhập kho cho phép linh hoạt trong việc xử lý các yêu cầu khi có thay đổi về kế hoạch hoặc khi phát hiện lỗi trong yêu cầu ban đầu. Giao diện có nút điều hướng để quay lại màn hình trước và tiêu đề rõ ràng.

#### 4.9.2. Thông số kỹ thuật chi tiết

Quy trình hủy yêu cầu nhập kho gồm 8 bước chính, từ việc tìm kiếm và chọn yêu cầu cần hủy đến việc cập nhật trạng thái cuối cùng. Điều kiện tiên quyết là yêu cầu nhập kho phải đã được tạo thành công và có trạng thái khác "Đã nhập kho".

Hệ thống tự động unlock các tài sản để có thể sử dụng cho yêu cầu khác, cập nhật trạng thái thành "Đã hủy", và thông báo cho các bên liên quan thông qua email và cập nhật tasklist. Bắt buộc nhập lý do hủy với độ dài tối đa 150 ký tự.

### Bảng tìm kiếm yêu cầu
| Trường | Operator | Action | Loại | Bắt buộc | Độ dài tối đa |
|--------|----------|--------|------|----------|---------------|
| Số yêu cầu | User | Input | Text | Optional | 20 |
| Ngày tạo | User | Input | Date | Optional | 20 |
| Tiêu đề | User | Input | Text | Optional | 150 |
| Người tạo | User | Select | List | Optional | 20 |
| Trạng thái yêu cầu | User | Select | List | Optional | 20 |
| Người xử lý | User | Select | List | Optional | 20 |
| Ngày xác nhận | User | Input | Date | Optional | 20 |

### Bảng thông tin kho
| Trường | Loại | Bắt buộc | Độ dài | Nguồn dữ liệu | Quy tắc |
|--------|------|----------|--------|---------------|---------|
| Tên kho | List | Mandatory | 50 | - | - |
| Địa chỉ kho | Text | Mandatory | 50 | OMS | Tự động hiển thị theo Tên kho |
| Quản lý kho | Text | Mandatory | 50 | OMS | Tự động hiển thị (Tên \| Phòng ban \| Email) |

---

### 4.10. Cấp tài sản - Phê duyệt

![Giao diện phê duyệt yêu cầu cấp tài sản](images/5_4_0a_A4_image8.png)

#### 4.10.1. Thông số kỹ thuật giao diện người dùng

Giao diện phê duyệt yêu cầu cấp tài sản cho phép Asset Manager xem xét và phê duyệt các yêu cầu cấp phát tài sản từ người dùng. Đây là một màn hình quan trọng trong module quản lý cấp phát tài sản, có navigation để quay lại menu chính.

#### 4.10.2. Thông số kỹ thuật chi tiết

Quy trình bắt đầu với việc AM tìm kiếm và xem danh sách các yêu cầu cấp tài sản, sau đó chọn yêu cầu cụ thể để xem chi tiết và đưa ra quyết định phê duyệt hoặc từ chối. Giao diện hiển thị đầy đủ thông tin tài sản cần cấp với 24 thuộc tính chi tiết, trong đó một số trường có thể được cấu hình "ẩn hiện tùy biến".

Khi AM từ chối yêu cầu, hệ thống sẽ tự động cập nhật trạng thái, unlock các tài sản đã được lock, cập nhật tasklist và gửi thông báo cho AMP để xử lý tiếp theo. Khi phê duyệt, hệ thống sẽ tự động khởi tạo [4.11. yêu cầu xuất kho](#411-cấp-tài-sản-tạo-yêu-cầu-xuất-kho).

### Bảng tìm kiếm yêu cầu
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

### Bảng thông tin tài sản cấp
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
| System | Display | Mã nhân viên | M | N | Ẩn hiện tùy biến |
| System | Display | Đơn vị sử dụng cha | M | N | Hiển thị mặc định |

---

### 4.11. Cấp tài sản - Tạo yêu cầu xuất kho

![Giao diện tạo yêu cầu xuất kho](images/warehouse_export_request.png)

#### 4.11.1. Thông số kỹ thuật giao diện người dùng

Chức năng tạo yêu cầu xuất kho được kích hoạt tự động sau khi [4.10. Asset Manager phê duyệt yêu cầu cấp tài sản](#410-cấp-tài-sản-phê-duyệt). Giao diện cho phép khởi tạo quy trình xuất kho tài sản từ kho để cung cấp cho người dùng.

#### 4.11.2. Thông số kỹ thuật chi tiết

Chức năng này cho phép hệ thống tự động tạo yêu cầu xuất kho dựa trên thông tin từ phiếu cấp tài sản đã được phê duyệt. Yêu cầu xuất kho sẽ bao gồm đầy đủ thông tin về tài sản cần xuất, thông tin người sử dụng, đơn vị sử dụng, và vị trí đặt tài sản.

Sau khi tạo yêu cầu xuất kho thành công, hệ thống sẽ tự động cập nhật trạng thái các yêu cầu liên quan, cập nhật tasklist cho các vai trò AM, WK, AMP và gửi thông báo email cho [4.12. Warehouse Keeper để tiếp nhận](#412-xuất-kho-từ-cấp-tài-sản-tiếp-nhận).

### Thông tin chung
| Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Format | Default Value | Data Rule |
|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| System | Display | Số yêu cầu | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| System | Input | Tiêu đề | O | Text | Y | 150 | | | =Tiêu đề RQ Cấp/Thanh lý |

### Thông tin kho xuất
| Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length | Data Source | Data Rule |
|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | = Thông tin kho trên RQ cấp/Thanh lý |
| System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | |
| System | Display | Quản lý kho | M | Text | N | 50 | OMS | |

### Thông tin đầu mối nhận hàng
| Operator | Action | Field Name VN | M/O | Field Type | Editable | Max Length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Đầu mối | M | Text | Y | 50 |
| User | Input | Số điện thoại | M | Number | Y | 52 |
| User | Input | Thời gian bàn giao | O | Date | Y | 50 |

---

### 4.12. Xuất kho từ cấp tài sản - Tiếp nhận

![Giao diện tiếp nhận yêu cầu xuất kho](images/5_4_2a__B5_image10.png)

#### 4.12.1. Thông số kỹ thuật giao diện người dùng

Giai đoạn tiếp nhận yêu cầu xuất kho là bước khởi đầu trong quy trình xuất kho tài sản từ [4.11. yêu cầu cấp tài sản](#411-cấp-tài-sản-tạo-yêu-cầu-xuất-kho). Giao diện cho phép nhân viên kho tiếp nhận và xử lý các yêu cầu xuất kho.

#### 4.12.2. Thông số kỹ thuật chi tiết

Quy trình xử lý yêu cầu xuất kho với 11 bước chính, từ tìm kiếm yêu cầu đến thông báo cho các bên liên quan. Warehouse Keeper tìm kiếm và chọn yêu cầu xuất kho từ danh sách, sau đó xem thông tin chi tiết bao gồm thông tin tài sản, kho xuất, đầu mối nhận hàng và hồ sơ đính kèm.

Nhân viên kho có thể đưa ra quyết định "Đồng ý" hoặc "Từ chối" yêu cầu, trong đó nút "Từ chối" sẽ bị ẩn nếu yêu cầu xuất phát từ thanh lý tài sản. Sau mỗi quyết định, hệ thống tự động cập nhật trạng thái yêu cầu, tasklist và gửi thông báo email. Nếu đồng ý, quy trình chuyển sang [4.13. Warehouse Manager để phê duyệt](#413-xuất-kho-từ-cấp-tài-sản-phê-duyệt).

### Bảng thông tin tìm kiếm yêu cầu:
| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value |
|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|
| User | Input | Mã yêu cầu | M | Text | Y | 20 | | |
| User | Input | Tiêu đề | M | Text | Y | 150 | | |
| User | Select | Người tạo | M | List | Y | 20 | | |
| User | Select | Trạng thái | M | List | Y | 20 | | |
| User | Input | Ngày tạo | M | Date | Y | 20 | | |
| User | Select | Nghiệp vụ kho | M | List | Y | 100 | | |
| User | Select | Người xử lý | M | List | Y | 20 | | |
| User | Input | Ngày xác nhận | M | Date | Y | 20 | | |

### Bảng thông tin tài sản chi tiết:
| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|-----------|
| System | Display | Mã tài sản | M | | N | | Hiển thị mặc định |
| System | Display | Tên Tài sản | M | | N | | Hiển thị mặc định |
| System | Display | Mô tả TS | M | | N | | Hiển thị mặc định |
| System | Display | Trạng thái TS | M | | N | | Hiển thị mặc định |
| System | Display | Phân nhóm TS (group name) | M | | N | | Hiển thị mặc định |
| System | Display | Nhóm TS (CAT1) | M | | N | | Hiển thị mặc định |
| System | Display | Số PO | M | | N | | Hiển thị mặc định |
| System | Display | Tên nhà cung cấp | O | | N | | Ẩn hiện tùy biến |
| System | Display | Nguyên giá TS (VAT incl) | M | | N | | Ẩn hiện tùy biến |

---

### 4.13. Xuất kho từ cấp tài sản - Phê duyệt

![Giao diện phê duyệt yêu cầu xuất kho](images/5_4_3a__B5_image11.png)

#### 4.13.1. Thông số kỹ thuật giao diện người dùng

Màn hình phê duyệt yêu cầu xuất kho cho phép Warehouse Manager xem xét và phê duyệt các yêu cầu được [4.12. Warehouse Keeper đồng ý tiếp nhận](#412-xuất-kho-từ-cấp-tài-sản-tiếp-nhận). Giao diện hỗ trợ quy trình phê duyệt trong luồng xuất kho tài sản với khả năng điều hướng về menu chính.

#### 4.13.2. Thông số kỹ thuật chi tiết

Quy trình phê duyệt bao gồm 12 bước chính từ tìm kiếm yêu cầu, xem thông tin chi tiết, đưa ra quyết định phê duyệt/từ chối, đến cập nhật trạng thái và thông báo cho các bên liên quan. Hệ thống có cơ chế phân quyền rõ ràng giữa System và User, với khả năng hiển thị/ẩn các trường thông tin tùy theo cấu hình.

Nút "Từ chối" bị ẩn nếu yêu cầu xuất kho xuất phát từ yêu cầu thanh lý. Sau khi phê duyệt hoặc từ chối, hệ thống tự động cập nhật trạng thái, gửi thông báo và cập nhật tasklist. Khi được phê duyệt, quy trình chuyển sang [4.14. bước nhận tài sản](#414-xuất-kho-từ-cấp-tài-sản-nhận-tài-sản).

### Bảng tìm kiếm yêu cầu
| STT | Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|-----|----------|--------|---------------|-----|------------|----------|------------|
| 1 | User | Input | Mã yêu cầu | M | Text | Y | 20 |
| 2 | User | Input | Tiêu đề | M | Text | Y | 150 |
| 3 | User | Select | Người tạo | M | List | Y | 20 |
| 4 | User | Select | Trạng thái | M | List | Y | 20 |
| 5 | User | Input | Ngày tạo | M | Date | Y | 20 |
| 6 | User | Select | Loại cấp tài sản | M | List | Y | 100 |
| 7 | User | Select | Người xử lý | M | List | Y | 20 |
| 8 | User | Input | Ngày xác nhận | M | Date | Y | 20 |

### Bảng thông tin chung
| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| System | Display | Số yêu cầu | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| System | Input | Tiêu đề | O | Text | Y | 150 | | | |

### Bảng thông tin đầu mối nhận hàng
| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Đầu mối | M | Text | Y | 50 |
| User | Input | Số điện thoại | M | Number | Y | 52 |
| User | Input | Thời gian bàn giao | O | Date | Y | 50 |

---

### 4.14. Xuất kho từ cấp tài sản - Nhận tài sản

![Giao diện nhận tài sản](images/5.4.4a_B6_image12.png)

#### 4.14.1. Thông số kỹ thuật giao diện người dụng

Màn hình nhận tài sản là bước cuối cùng trong quy trình xuất kho, cho phép Business Unit User thực hiện việc nhận tài sản từ kho sau khi [4.13. Warehouse Manager đã phê duyệt](#413-xuất-kho-từ-cấp-tài-sản-phê-duyệt). Giao diện hỗ trợ quy trình nhận tài sản với các chức năng xác nhận thông tin và cập nhật trạng thái kho.

#### 4.14.2. Thông số kỹ thuật chi tiết

Giao diện được thiết kế phức tạp với 11 bước xử lý từ tìm kiếm yêu cầu đến cập nhật trạng thái cuối cùng. Người dùng có thể xem thông tin chi tiết về tài sản cần nhận với 26+ trường thông tin từ mã tài sản đến thông tin bảo hành, thông tin kho xuất và đầu mối nhận hàng.

Quy trình xử lý bao gồm hai luồng chính: từ chối yêu cầu (với nhập lý do) hoặc xác nhận nhận tài sản. Khi xác nhận, hệ thống clear thông tin kho và cập nhật đơn vị sử dụng cho tài sản. Khi từ chối, hệ thống unlock tài sản để có thể pickup cho request khác và gửi thông báo cho các bên liên quan.

### Bảng tìm kiếm yêu cầu
| Field Name | Operator | Field Type | Editable | Max Length | M/O | Mô tả |
|------------|----------|------------|----------|------------|-----|-------|
| Mã yêu cầu | User Input | Text | Y | 20 | M | |
| Tiêu đề | User Input | Text | Y | 150 | M | |
| Người tạo | User Select | List | Y | 20 | M | |
| Trạng thái | User Select | List | Y | 20 | M | |
| Ngày tạo | User Input | Date | Y | 20 | M | |
| Nghiệp vụ kho | User Select | List | Y | 100 | M | |
| Người xử lý | User Select | List | Y | 20 | M | |
| Ngày xác nhận | User Input | Date | Y | 20 | M | |

### Bảng thông tin chung yêu cầu
| Field Name | Operator | Field Type | Editable | Max Length | Format | Default | M/O | Data Rule |
|------------|----------|------------|----------|------------|--------|---------|-----|-----------|
| Số yêu cầu | System Display | Text | N | 50 | XK.YY.xxxx | | M | YY = Year, xxxx = số chạy từ 1-9999 |
| Ngày tạo | System Display | Date | N | 50 | MM.DD.YYYY | Today | M | |
| Tiêu đề | System Input | Text | Y | 150 | | | O | |

### Bảng thông tin kho và đầu mối
| Field Name | Operator | Field Type | Editable | Max Length | M/O | Data Source |
|------------|----------|------------|----------|------------|-----|-------------|
| Tên kho | System/User Display/Search/Select | List | N | 50 | M | Thông tin kho trên RQ cấp tài sản |
| Địa chỉ kho | System Display | Text | Y | 50 | M | OMS |
| Quản lý kho | System Display | Text | N | 50 | M | OMS - Format: Tên \| Phòng ban \| Email |
| Đầu mối | User Input | Text | Y | 50 | M | |
| Số điện thoại | User Input | Number | Y | 52 | M | |
| Thời gian bàn giao | User Input | Date | Y | 50 | O | |

---

### 4.15. HỦY YÊU CẦU XUẤT KHO

![Giao diện hủy yêu cầu xuất kho](images/5.5.1a_B5.png)

#### 4.15.1. Thông số kỹ thuật giao diện người dùng

Chức năng hủy yêu cầu xuất kho là một phần của module quản lý xuất nhập kho, cho phép người dùng thực hiện việc hủy các yêu cầu xuất kho đã được tạo từ [4.11. quy trình cấp tài sản](#411-cấp-tài-sản-tạo-yêu-cầu-xuất-kho) hoặc thanh lý tài sản. Giao diện có khả năng điều hướng trong hệ thống và tiêu đề rõ ràng.

#### 4.15.2. Thông số kỹ thuật chi tiết

Quy trình hủy yêu cầu xuất kho gồm 8 bước chính, từ việc tìm kiếm và chọn yêu cầu cần hủy đến việc cập nhật trạng thái cuối cùng. Điều kiện tiên quyết là yêu cầu xuất kho phải đã được tạo thành công và có trạng thái khác "Đã xác nhận".

Quy trình đặc biệt lưu ý đến việc xử lý tài sản bị lock/unlock và khôi phục trạng thái tài sản về trước khi thanh lý, đảm bảo tính nhất quán dữ liệu trong hệ thống. Hệ thống tự động thực hiện các tác vụ như unlock tài sản, cập nhật trạng thái và gửi thông báo email cho Warehouse Keeper.

### Bảng tìm kiếm yêu cầu xuất kho:
| STT | Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|-----|----------|--------|---------------|-----|------------|----------|------------|
| 1 | User | Input | Mã yêu cầu | M | Text | Y | 20 |
| 2 | User | Input | Tiêu đề | M | Text | Y | 150 |
| 3 | User | Select | Người tạo | M | List | Y | 20 |
| 4 | User | Select | Trạng thái | M | List | Y | 20 |
| 5 | User | Input | Ngày tạo | M | Date | Y | 20 |
| 6 | User | Select | Nghiệp vụ kho | M | List | Y | 100 |
| 7 | User | Select | Người xử lý | M | List | Y | 20 |
| 8 | User | Input | Ngày xác nhận | M | Date | Y | 20 |

### Bảng thông tin kho và đầu mối nhận hàng:
| STT | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source |
|-----|----------|--------|---------------|-----|------------|----------|------------|-------------|
| 1 | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | Thông tin kho trên RQ cấp tài sản |
| 2 | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS |
| 3 | System | Display | Quản lý kho | M | Text | N | 50 | OMS - Format: Tên \| Phòng ban \| Email |
| 4 | User | Input | Đầu mối | M | Text | Y | 50 | |
| 5 | User | Input | Số điện thoại | M | Number | Y | 52 | |
| 6 | User | Input | Thời gian bàn giao | O | Date | Y | 50 | |

---

### 4.16. Điều chuyển kho - Tạo yêu cầu

![Giao diện tạo yêu cầu điều chuyển kho](images/warehouse_transfer_request.png)

#### 4.16.1. Thông số kỹ thuật giao diện người dùng

Chức năng điều chuyển tài sản giữa các kho cho phép người dùng tạo yêu cầu để di chuyển tài sản từ kho này sang kho khác một cách có kiểm soát và theo dõi được. Giao diện hỗ trợ việc tạo yêu cầu điều chuyển kho thông qua form nhập liệu.

#### 4.16.2. Thông số kỹ thuật chi tiết

Giao diện bao gồm các phần chính: thông tin chung của yêu cầu (số yêu cầu tự động, ngày tạo, tiêu đề), chức năng tìm kiếm và chọn tài sản với nhiều tiêu chí lọc, hiển thị danh sách tài sản được chọn để điều chuyển. Phần thông tin kho bao gồm kho đi (hiển thị tự động từ tài sản được chọn) và kho nhập (người dùng chọn), cùng với thông tin đầu mối giao hàng.

Sau khi gửi yêu cầu, hệ thống sẽ tự động thực hiện các bước: khóa tài sản, cập nhật trạng thái, tìm người duyệt, cập nhật tasklist và gửi thông báo cho [4.17. Asset Manager và Warehouse Manager để phê duyệt](#417-điều-chuyển-kho-phê-duyệt).

### Bảng thông tin chung yêu cầu
| Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|-------------|----------|--------|---------------|-----|------------|----------|------------|---------|---------------|-----------|
| Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| | User | Input | Tiêu đề | O | Text | Y | 150 | | | |

### Bảng tìm kiếm tài sản
| Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data rule |
|-------------|----------|--------|---------------|-----|------------|----------|------------|-----------|
| Tìm kiếm tài sản | User | Input | Mã tài sản | O | Text | N | 20 | |
| | User | Input | Tên tài sản | O | Text | Y | 20 | |
| | User | Select | Phân loại tài sản | O | List | N | 20 | |
| | User | Select | Nhóm tài sản | O | List | N | 20 | |
| | User | Input | PO number | O | Text | Y | 20 | |
| | User | Select | Trạng thái TS | O | List | N | 50 | |
| | User | Select | Tên nhà cung cấp | O | List | N | 50 | |
| | User | Input | Tên kho | O | List | Y | 50 | |
| | User | Select | Vị trí đặt tài sản | O | Text | N | 100 | |

### Bảng thông tin kho
| Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|-------------|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| Thông tin kho đi | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | |
| | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Thông tin kho nhập | User | Select | Tên kho | M | List | N | 50 | | |
| | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

---

### 4.17. Điều chuyển kho - Phê duyệt

![Giao diện phê duyệt điều chuyển kho](images/warehouse_transfer_approval.png)

#### 4.17.1. Thông số kỹ thuật giao diện người dùng

Giao diện phê duyệt yêu cầu điều chuyển tài sản giữa các kho cho phép người có thẩm quyền xem xét và phê duyệt các yêu cầu được tạo từ [4.16. quy trình tạo yêu cầu](#416-điều-chuyển-kho-tạo-yêu-cầu). Đây là một phần quan trọng trong việc kiểm soát việc điều chuyển tài sản giữa các đơn vị lưu trữ.

#### 4.17.2. Thông số kỹ thuật chi tiết

Quy trình phê duyệt bao gồm 14 bước chính, từ việc tìm kiếm và xem yêu cầu, phê duyệt hoặc từ chối, đến việc tạo biên bản điều chuyển và bàn giao tài sản thực tế. Giao diện được thiết kế cho người phê duyệt với các chức năng tìm kiếm yêu cầu theo nhiều tiêu chí, xem chi tiết thông tin tài sản cần điều chuyển, thông tin kho đi và kho nhận.

Hệ thống tự động xử lý các thông báo, cập nhật trạng thái, tạo biên bản và cập nhật thông tin kho cho tài sản sau khi được phê duyệt. Khi từ chối, bắt buộc nhập lý do và hệ thống unlock tài sản để có thể sử dụng cho yêu cầu khác.

### Bảng tìm kiếm yêu cầu:
| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|---------|---------------|-----|-------------|-----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

### Bảng thông tin chung yêu cầu:
| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|----------|---------|---------------|-----|-------------|-----------|------------|---------|---------------|-----------|
| System | Display | Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| User | Input | Tiêu đề | O | Text | Y | 150 | | | |
| User | Select | Thêm tài sản | M | Button | N | | | | |

### Bảng thông tin đầu mối giao hàng:
| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|---------|---------------|-----|-------------|-----------|------------|
| User | Input | Đầu mối | M | Text | N | 50 |
| User | Input | Số điện thoại | M | Number | N | 52 |
| User | Input | Thời gian bàn giao | O | Date | N | 50 |
| User | Input | Ghi chú | M | Text | N | 150 |

---

### 4.18. Phê duyệt yêu cầu điều chuyển tài sản giữa các kho

#### 4.18.1. Thông số kỹ thuật giao diện người dùng

Giao diện phê duyệt này là phần mở rộng của [4.17. quy trình phê duyệt điều chuyển kho](#417-điều-chuyển-kho-phê-duyệt), cung cấp thêm các chức năng chi tiết cho việc xử lý yêu cầu điều chuyển tài sản. Approver có thể tìm kiếm, xem xét và phê duyệt/từ chối các yêu cầu điều chuyển.

#### 4.18.2. Thông số kỹ thuật chi tiết

Quy trình bắt đầu với việc người phê duyệt tìm kiếm yêu cầu theo các tiêu chí như số yêu cầu, ngày tạo, tiêu đề, người tạo, trạng thái và người xử lý. Khi xem chi tiết yêu cầu, người phê duyệt có thể thấy đầy đủ thông tin về tài sản cần điều chuyển, thông tin kho đi và kho đến, đầu mối giao nhận, và các hồ sơ đính kèm.

Sau khi quyết định, hệ thống sẽ tự động cập nhật trạng thái yêu cầu, unlock tài sản (nếu từ chối), cập nhật tasklist cho các bên liên quan, gửi thông báo email, và tạo các biên bản xuất/nhập kho (nếu phê duyệt) theo [4.19. ma trận trạng thái](#419-status-ma-trận-trạng-thái).

### Bảng tìm kiếm yêu cầu
| Field name VN | M/O | Field type | Editable | Max length | Operator | Action |
|---------------|-----|------------|----------|------------|----------|--------|
| Số yêu cầu | O | Text | Y | 20 | User | Input |
| Ngày tạo | O | Date | Y | 20 | User | Input |
| Tiêu đề | O | Text | Y | 150 | User | Input |
| Người tạo | O | List | Y | 20 | User | Select |
| Trạng thái yêu cầu | O | List | Y | 20 | User | Select |
| Người xử lý | O | List | Y | 20 | User | Select |
| Ngày xác nhận | O | Date | Y | 20 | User | Input |

### Bảng cập nhật trạng thái hệ thống
| Hành động | Đối tượng | Trạng thái/Nội dung |
|-----------|-----------|-------------------|
| Update | RQ điều chuyển kho | "Từ chối" hoặc "Đã phê duyệt" |
| Update | Trạng thái lock tài sản | Unlock (khi từ chối) |
| Update | Tasklist Approver | "Đã xử lý" |
| Update | Tasklist AMP | "Cần xử lý" |
| Send | Email notification | Thông báo cho AMP, WK, AM, Warehouse Mgr |

---

### 4.19. Status - Ma trận trạng thái

#### 4.19.1. Thông số kỹ thuật quy trình nghiệp vụ

Ma trận trạng thái định nghĩa toàn bộ các trạng thái, hành động và luồng nghiệp vụ trong hệ thống quản lý tài sản. Hệ thống được thiết kế với 2 loại trạng thái song song: **Request Status** (trạng thái yêu cầu) và **Asset Status** (trạng thái tài sản), cho phép theo dõi chi tiết tiến trình xử lý và vị trí tài sản trong từng thời điểm.

#### 4.19.2. Thông số kỹ thuật chi tiết

Ma trận mô tả 4 quy trình chính: **Cấp tài sản**, **Thanh lý tài sản**, và **Điều chuyển tài sản**. Quy trình **Cấp tài sản** có 2 luồng chính: cấp tài sản không ở kho (3 bước) được xử lý qua [4.10. phê duyệt cấp tài sản](#410-cấp-tài-sản-phê-duyệt) và cấp tài sản từ kho (6 bước) thông qua [4.11. tạo yêu cầu xuất kho](#411-cấp-tài-sản-tạo-yêu-cầu-xuất-kho).

Quy trình **Thanh lý tài sản** phân chia thành 2 hình thức: bán trực tiếp (8 bước) và bán đấu giá (10 bước), với các khâu kiểm soát và phê duyệt nghiêm ngặt bởi Checker và Approver. **Điều chuyển tài sản** được xử lý qua [4.16. tạo yêu cầu](#416-điều-chuyển-kho-tạo-yêu-cầu) và [4.17. phê duyệt](#417-điều-chuyển-kho-phê-duyệt).

### Ma trận trạng thái - Cấp tài sản

| Process | Sub-process | PIC | Action | Request Status | Asset Status | Note |
|---------|-------------|-----|--------|----------------|--------------|------|
| Cấp tài sản không ở kho | 1 Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - |
| | | | Gửi | Chờ xác nhận | - | - |
| | 2. Xác nhận | BU User | Từ chối | Từ chối | - | - |
| | | | Xác nhận | Đã xác nhận | Đang sử dụng | Đã xác nhận >>> Đã nhận tài sản |
| | | | Bổ sung thông tin | Bổ sung thông tin | - | - |
| | 3. Bổ sung TT | AMP | Bổ sung thông tin | Chờ xác nhận | - | - |
| Cấp tài sản từ kho | 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - |
| | | | Gửi | Chờ xác nhận | - | - |
| | 2. Phê duyệt | AM | Từ chối | Từ chối | - | - |
| | | | Duyệt | Đã xác nhận | - | - |
| | 3. Tạo yêu cầu | System | - | Đã xác nhận | Chờ xuất kho | - |
| | 4. Xuất kho | WK | Từ chối | Từ chối | Từ chối | - |
| | | | Đồng ý | Đã xác nhận | Chờ phê duyệt | - |
| | 5. Phê duyệt | Warehouse Mgr. | Từ chối | Từ chối | Từ chối | - |
| | | | Duyệt | Đã xác nhận | Chờ xác nhận | - |
| | 6. Nhận hàng | BU User | Từ chối | Từ chối | Từ chối | - |
| | | | Xác nhận | Đã xác nhận | Đã nhận tài sản | Đang sử dụng |

### Ma trận trạng thái - Thanh lý tài sản (Bán trực tiếp)

| Sub-process | PIC | Action | Request Status | Note |
|-------------|-----|--------|----------------|------|
| 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | - |
| | | Gửi | Chờ kiểm soát | - |
| 2. Kiểm soát | Checker | Từ chối | Từ chối | - |
| | | Yêu cầu bổ sung thông tin | Bổ sung thông tin | - |
| | | Đồng ý | Chờ phê duyệt | - |
| 3. Phê duyệt | Approver | Từ chối | Đang tạo | - |
| | | Yêu cầu bổ sung thông tin | Bổ sung thông tin | - |
| | | Duyệt | Chờ cập nhật kết quả thanh lý | - |

---

### 4.20. Tasklist - Ma trận phân bổ công việc

#### 4.20.1. Thông số kỹ thuật quy trình công việc

Ma trận phân bổ công việc định nghĩa luồng xử lý và phân bổ công việc trong quy trình điều chuyển kho, xác định ai làm gì, khi nào và ở trạng thái nào trong luồng xử lý. Hệ thống tasklist được chia thành hai loại: "Tasklist Điều chuyển" và "Tasklist Kho", mỗi loại có hai trạng thái "Cần xử lý" và "Đã xử lý".

#### 4.20.2. Thông số kỹ thuật chi tiết

Ma trận này cho thấy luồng công việc tuần tự từ Initiator khởi tạo thông qua [4.16. tạo yêu cầu điều chuyển](#416-điều-chuyển-kho-tạo-yêu-cầu), qua BUH phê duyệt trong [4.17. quy trình phê duyệt](#417-điều-chuyển-kho-phê-duyệt), đến AMP xử lý, và cuối cùng WM (Warehouse Manager) xác nhận nhập kho.

Quy trình bao gồm ba giai đoạn chính với nhiều hành động khác nhau (Lưu, Gửi, Từ chối, Duyệt, Bổ sung thông tin, Xác nhận) được thực hiện bởi các vai trò khác nhau. Có cơ chế xử lý các trường hợp từ chối và yêu cầu bổ sung thông tin, đảm bảo tính linh hoạt trong quy trình.

| Quy trình con | Hành động | Vai trò | Tasklist Điều chuyển - Cần xử lý | Tasklist Điều chuyển - Đã xử lý | Tasklist Kho - Cần xử lý | Tasklist Kho - Đã xử lý | Ghi chú |
|---------------|-----------|---------|----------------------------------|--------------------------------|---------------------------|-------------------------|---------|
| 2.3.1a Tạo yêu cầu điều chuyển | Lưu | Initiator | x | | | | |
| | Gửi | | | x | | | |
| 2.3.3a Phê duyệt yêu cầu điều chuyển | Từ chối | Initiator | x | | | | |
| | | BUH | | x | | | |
| | Duyệt | Initiator | | x | | | |
| | | BUH | | x | | | |
| | | AMP | x | | | | |
| | Bổ sung thông tin | Initiator | x | | | | |
| | | BUH | | x | | | |
| 5.2.2a Xác nhận yêu cầu điều chuyển | Từ chối | Initiator | x | | | | |
| | | BUH | | x | | | |
| | | AMP | | x | | | |
| | Bổ sung thông tin | Initiator | x | | | | |
| | | BUH | | x | | | |
| | | AMP | | x | | | |
| | Xác nhận & Yêu cầu nhập kho | Initiator | x | | | | |
| | | BUH | | x | | | |
| | | AMP | | x | x | | |
| | | WM | | | x | | |
| | Phê duyệt yêu cầu nhập kho - Từ chối | Initiator | x | | x | | Vấn đề về quy trình xử lý |

---

## 5. Assumptions & Constraints

### Giả định:
- Hệ thống hiện tại đã có sẵn cơ sở dữ liệu tài sản và người dùng
- Các hệ thống OMS, EMS và ITSM sẵn sàng tích hợp
- Người dùng đã được đào tạo cơ bản về hệ thống hiện tại
- Môi trường mạng và cơ sở hạ tầng IT đảm bảo hoạt động ổn định

### Ràng buộc:
- Không thay đổi cấu trúc dữ liệu cốt lõi của hệ thống hiện tại
- Tuân thủ quy trình phê duyệt hiện có của tổ chức
- Đảm bảo tính bảo mật trong quản lý thông tin tài sản
- Hỗ trợ tối đa 10,000 giao dịch đồng thời
- Thời gian phản hồi tối đa 3 giây cho các thao tác cơ bản

---

## 6. Dependencies

### Phụ thuộc nội bộ:
- [4.1. Dashboard Tài Sản](#41-dashboard-tài-sản) phụ thuộc vào tích hợp OMS
- [4.2. Module Quản lý Kho](#42-module-quản-lý-kho) là tiền đề cho tất cả các quy trình xuất-nhập kho
- [4.10. Phê duyệt cấp tài sản](#410-cấp-tài-sản-phê-duyệt) là điều kiện để kích hoạt [4.11. tạo yêu cầu xuất kho](#411-cấp-tài-sản-tạo-yêu-cầu-xuất-kho)

### Phụ thuộc hệ thống bên ngoài:
- **OMS (Organization Management System)**: Cung cấp cấu trúc tổ chức, thông tin nhân viên và đơn vị
- **EMS**: Đồng bộ thông tin PO, thời gian bảo hành
- **ITSM (IT Service Management)**: Tích hợp module sửa chữa tài sản
- **Cổng hỗ trợ chi nhánh**: Kết nối với hệ thống intranet

### Phụ thuộc quy trình:
- Quy trình [4.19. ma trận trạng thái](#419-status-ma-trận-trạng-thái) phải được triển khai trước
- [4.20. Ma trận phân bổ công việc](#420-tasklist-ma-trận-phân-bổ-công-việc) cần được cấu hình cho từng vai trò

---

## 7. Acceptance Criteria

### Tiêu chí chức năng:
1. **Dashboard**: [4.1. Dashboard Tài Sản](#41-dashboard-tài-sản) hiển thị chính xác 4 KPI với công thức tính đã định nghĩa
2. **Tích hợp**: Đồng bộ thành công với OMS, EMS theo đúng lịch trình
3. **Quy trình kho**: Tất cả luồng trong [4.2. Module Quản lý Kho](#42-module-quản-lý-kho) hoạt động end-to-end
4. **Tự động hóa**: Phiếu cấp tài sản tự động phê duyệt sau 20 ngày
5. **Truy vết**: Mọi thay đổi trạng thái tài sản được ghi log theo [4.19. ma trận trạng thái](#419-status-ma-trận-trạng-thái)

### Tiêu chí hiệu năng:
- Thời gian tải [4.1. dashboard](#41-dashboard-tài-sản) < 5 giây
- Xử lý đồng thời tối thiểu 1000 user
- Uptime 99.9% trong giờ làm việc
- Backup tự động hàng ngày

### Tiêu chí bảo mật:
- Phân quyền theo [4.20. ma trận phân bổ công việc](#420-tasklist-ma-trận-phân-bổ-công-việc)
- Mã hóa dữ liệu nhạy cảm
- Audit trail cho tất cả thao tác quan trọng
- Single Sign-On (SSO) với hệ thống hiện tại

---

## 8. Glossary

| Thuật ngữ | Định nghĩa |
|-----------|------------|
| **AMP** | Asset Management Personnel - Nhân viên quản lý tài sản |
| **AM** | Asset Manager - Quản lý tài sản |
| **BU** | Business Unit - Đơn vị kinh doanh |
| **BUH** | Business Unit Head - Trưởng đơn vị kinh doanh |
| **WK** | Warehouse Keeper - Thủ kho |
| **WM** | Warehouse Manager - Quản lý kho |
| **OMS** | Organization Management System - Hệ thống quản lý tổ chức |
| **EMS** | Enterprise Management System - Hệ thống quản lý doanh nghiệp |
| **ITSM** | IT Service Management - Quản lý dịch vụ IT |
| **Dashboard KPI** | 4 chỉ số chính: Total assets, Total value, Warranty status, Utilization rate |
| **Request Status** | Trạng thái xử lý yêu cầu trong hệ thống |
| **Asset Status** | Trạng thái thực tế của tài sản |
| **Lock/Unlock** | Cơ chế khóa tài sản để tránh xung đột trong xử lý |
| **Tasklist** | Danh sách công việc được phân bổ cho từng vai trò |

---

*Tài liệu này được tạo từ 37 sheet Excel với đầy đủ thông tin chi tiết về yêu cầu nghiệp vụ FAM Wave 4. Mọi tham chiếu nội bộ đều được liên kết để hỗ trợ điều hướng dễ dàng.*

---

*Generated by Claude Sonnet 4.5 from 37 sheet summaries*
*Headings: 119 | Internal Links: 80*

*✅ All internal links validated successfully*
