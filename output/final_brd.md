# Tài liệu Yêu cầu Nghiệp vụ - FAM UPGRADE WAVE 4

## Mục lục

1. [Executive Summary](#1-executive-summary)
2. [Project Scope & Objectives](#2-project-scope-objectives)
3. [Stakeholders](#3-stakeholders)
4. [Business Requirements](#4-business-requirements)
   - 4.1. [Asset Dashboard Module](#41-asset-dashboard-module)
   - 4.2. [Warehouse Management Module](#42-warehouse-management-module)
     - 4.2.1. [Create Warehouse Intake Request](#421-create-warehouse-intake-request)
     - 4.2.2. [Approve Warehouse Entry Request](#422-approve-warehouse-entry-request)
     - 4.2.3. [Warehouse Receipt Confirmation](#423-warehouse-receipt-confirmation)
     - 4.2.4. [Manual Warehouse Entry](#424-manual-warehouse-entry)
     - 4.2.5. [Cancel Warehouse Entry Request](#425-cancel-warehouse-entry-request)
     - 4.2.6. [Asset Allocation Process](#426-asset-allocation-process)
     - 4.2.7. [Cancel Asset Allocation Request](#427-cancel-asset-allocation-request)
     - 4.2.8. [Warehouse Transfer Management](#428-warehouse-transfer-management)
5. [Assumptions & Constraints](#5-assumptions-constraints)
6. [Dependencies](#6-dependencies)
7. [Acceptance Criteria](#7-acceptance-criteria)
8. [Glossary](#8-glossary)

## 1. Executive Summary

Dự án FAM (Fixed Asset Management) System Upgrade - Wave 4 tập trung vào việc nâng cấp và phát triển các tính năng mới cho hệ thống quản lý tài sản cố định. Giai đoạn này bao gồm 11 yêu cầu chính được phân loại theo độ ưu tiên từ 1-4, trong đó Priority 1 là cao nhất.

Hai sản phẩm chính của Wave 4 là [Dashboard tài sản](#41-asset-dashboard-module) với khả năng trực quan hóa và tùy biến dữ liệu, cùng với [Module quản lý kho toàn diện](#42-warehouse-management-module) hỗ trợ quy trình xuất-nhập kho tài sản. Hệ thống tập trung vào tự động hóa các quy trình nghiệp vụ như auto-confirm phiếu cấp tài sản và đồng bộ dữ liệu với các hệ thống liên quan (OMS, EMS, ITSM).

Ngoài ra, dự án còn bao gồm các tính năng mới như Module sửa chữa tài sản tích hợp với ITSM, Cổng hỗ trợ chi nhánh, và các cải tiến UI/UX để nâng cao trải nghiệm người dùng.

## 2. Project Scope & Objectives

### Trong phạm vi dự án

- Phát triển [Dashboard tài sản](#41-asset-dashboard-module) với tính năng visualization và customization
- Xây dựng [Module quản lý kho](#42-warehouse-management-module) hoàn chỉnh cho việc xuất-nhập kho tài sản
- Tự động hóa quy trình auto-confirm phiếu cấp tài sản sau 20 ngày
- Tích hợp đồng bộ dữ liệu với OMS khi có thay đổi orgchart
- Đồng bộ tiêu đề PO từ EMS và thông tin bảo hành
- Bổ sung workflow phê duyệt ATM trong module thanh lý
- Phát triển Module sửa chữa tài sản tích hợp ITSM
- Xây dựng Cổng hỗ trợ chi nhánh trên intranet

### Ngoài phạm vi dự án

- Thay đổi cấu trúc cơ sở dữ liệu hiện tại của các module khác
- Tích hợp với các hệ thống bên ngoài không được liệt kê
- Migration dữ liệu từ phiên bản cũ (sẽ được xử lý trong phase riêng)

### Mục tiêu dự án

- Nâng cao hiệu quả quản lý tài sản thông qua tự động hóa
- Cải thiện khả năng báo cáo và phân tích thông qua dashboard
- Tối ưu hóa quy trình xuất-nhập kho tài sản
- Tăng cường tích hợp với các hệ thống nội bộ
- Nâng cao trải nghiệm người dùng

## 3. Stakeholders

### Vai trò nội bộ
- **AMP (Asset Management Personnel)**: Nhân viên quản lý tài sản
- **AM (Asset Manager)**: Quản lý tài sản cấp cao
- **BU User**: Người dùng đơn vị kinh doanh
- **BU Manager**: Quản lý đơn vị kinh doanh
- **WK (Warehouse Keeper)**: Thủ kho
- **Warehouse Manager**: Quản lý kho
- **Checker**: Người kiểm soát
- **Approver**: Người phê duyệt

### Hệ thống liên quan
- **OMS (Organization Management System)**: Cung cấp thông tin tổ chức và nhân sự
- **EMS**: Hệ thống quản lý và đồng bộ thông tin PO
- **ITSM**: Hệ thống quản lý dịch vụ IT tích hợp với module sửa chữa
- **Cổng hỗ trợ chi nhánh**: Nền tảng intranet hỗ trợ chi nhánh

## 4. Business Requirements

### 4.1. Asset Dashboard Module

Dashboard tổng quan quản lý tài sản cung cấp khả năng trực quan hóa dữ liệu tài sản và hỗ trợ ra quyết định nhanh chóng. Module này hiển thị ngay khi người dùng đăng nhập vào hệ thống, cung cấp cái nhìn tổng quan về tình trạng tài sản trong toàn tổ chức.

![Dashboard tài sản](images/1_B5_image1.png)

#### Thông số tổng quan

Dashboard cung cấp bốn chỉ số quan trọng: tổng số lượng tài sản (loại trừ tài sản đã thanh lý và vô hiệu hóa), tổng giá trị tài sản theo nguyên giá, tỷ lệ phần trăm tài sản còn trong thời hạn bảo hành, và tỷ lệ tài sản đang được sử dụng so với tổng tài sản có hiệu lực.

| STT | Nội dung | Giá trị | Loại biểu đồ | Ghi chú |
|-----|----------|---------|--------------|---------|
| 1 | Total assets | Count số lượng (All tài sản - Đã thanh lý - Vô hiệu hóa) | - | - |
| 2 | Total value | Sum nguyên giá (All tài sản - Đã thanh lý - Vô hiệu hóa) | - | - |
| 3 | Warranty status | Tỷ lệ % tài sản còn hạn bảo hành/(All tài sản - Vô hiệu hóa - Đã thanh lý) | - | - |
| 4 | Utilization rate | Tỷ lệ % tài sản đang sử dụng/(All tài sản - Vô hiệu hóa - Đã thanh lý) | - | - |

#### Biểu đồ tương tác

Hệ thống cung cấp năm loại biểu đồ khác nhau để phân tích dữ liệu tài sản. Mỗi biểu đồ hỗ trợ tính năng hover để xem chi tiết và click để chuyển sang module liên quan.

| STT | Tên biểu đồ | Dữ liệu | Loại biểu đồ | Ghi chú |
|-----|-------------|---------|--------------|---------|
| 1 | Asset Distribution - Cơ cấu theo trạng thái | Nguyên giá | Sunburst (Vòng trong: IT/ADM/CMD, Vòng ngoài: Trạng thái) | Hover hiện số lượng và giá trị |
| 2 | Asset Distribution - Cơ cấu theo Vùng/Đơn vị | Nguyên giá | Stacked Column | - |
| 3 | Asset Value by Group Name | Nguyên giá | Column | - |
| 4 | Asset Fluctuation Over Time | Nguyên giá | Line | Theo Month/Year |
| 5 | Asset by Time in Use | Số lượng | Scatter | - |

#### Bộ lọc đa tiêu chí

Dashboard tích hợp bộ lọc linh hoạt cho phép người dùng phân tích dữ liệu theo nhiều góc độ khác nhau. Tất cả bộ lọc được đồng bộ từ các hệ thống liên quan như OMS.

| STT | Tiêu chí | Loại dữ liệu | Ghi chú |
|-----|----------|--------------|---------|
| 1 | Vùng | LOV | - |
| 2 | Đơn vị sử dụng | LOV đồng bộ từ OMS | - |
| 3 | CAT 1 | LOV | - |
| 4 | Group name | LOV | - |
| 5 | Asset status | LOV asset status | Không bao gồm Đã thanh lý, Vô hiệu hóa |

Dashboard hỗ trợ xuất dữ liệu ra Excel và tích hợp hoàn toàn với hệ thống OMS để đảm bảo thông tin đơn vị sử dụng luôn được cập nhật chính xác.

### 4.2. Warehouse Management Module

Module quản lý kho toàn diện hỗ trợ các quy trình xuất-nhập kho, điều chuyển tài sản và thanh lý tài sản. Hệ thống được thiết kế với nhiều mức độ tự động hóa để giảm thiểu thao tác thủ công và đảm bảo tính chính xác trong quá trình quản lý.

Module bao gồm các quy trình chính sau:
- [Tạo yêu cầu nhập kho](#421-create-warehouse-intake-request) (tự động từ điều chuyển về kho)
- [Phê duyệt yêu cầu nhập kho](#422-approve-warehouse-entry-request) 
- [Xác nhận nhập kho](#423-warehouse-receipt-confirmation)
- [Nhập kho thủ công](#424-manual-warehouse-entry)
- [Hủy yêu cầu nhập kho](#425-cancel-warehouse-entry-request)
- [Quy trình cấp tài sản](#426-asset-allocation-process)
- [Hủy yêu cầu xuất kho](#427-cancel-asset-allocation-request)
- [Quản lý điều chuyển kho](#428-warehouse-transfer-management)

Điểm nổi bật của hệ thống là khả năng tự động hóa: khi yêu cầu điều chuyển về kho được xác nhận, hệ thống tự động tạo yêu cầu nhập kho. Tương tự, khi yêu cầu cấp tài sản hoặc thanh lý được duyệt, hệ thống tự động tạo yêu cầu xuất kho tương ứng.

#### 4.2.1. Create Warehouse Intake Request

##### 4.2.1.1. Thông số kỹ thuật giao diện người dùng

Quy trình tạo yêu cầu nhập kho được khởi tạo tự động khi có yêu cầu điều chuyển tài sản về kho được xác nhận. Hệ thống sẽ kế thừa toàn bộ thông tin từ yêu cầu điều chuyển bao gồm thông tin tài sản, chi tiết kho đích và các tệp đính kèm.

![Giao diện tạo yêu cầu nhập kho](images/5_1_1a_B5_image1.png)

**Cấu trúc màn hình:**
- Phần header hiển thị số yêu cầu và trạng thái
- Phần thông tin chung cho phép nhập tiêu đề và ghi chú
- Phần chi tiết tài sản hiển thị danh sách tài sản được chuyển
- Phần tệp đính kèm cho phép upload thêm tài liệu

**Các bên liên quan:** Hệ thống (tự động tạo), Quản lý kho (phê duyệt), AMP (theo dõi)

**Quy trình xử lý:**
1. Hệ thống tự động khởi tạo yêu cầu khi RQ điều chuyển được xác nhận
2. Cập nhật trạng thái RQ điều chuyển thành "Đã xác nhận"
3. Lock tài sản để tránh xung đột với các yêu cầu khác
4. Gửi thông báo cho Warehouse Manager để xử lý tiếp
5. Cập nhật tasklist cho các bên liên quan

##### 4.2.1.2. Thông số kỹ thuật chi tiết

Hệ thống tự động tạo yêu cầu nhập kho với mã số theo định dạng NK.YY.xxxx và kế thừa đầy đủ thông tin từ yêu cầu điều chuyển gốc.

**Đặc tả fields - Thông tin chung yêu cầu nhập kho:**

| Field name VN | Operator | Action | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|---------------|----------|--------|-----|------------|----------|------------|---------|---------------|-----------|
| Số yêu cầu | System | Display | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Ngày tạo | System | Display | M | Date | N | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | System | Display | M | Text | N | 150 | | | =Tiêu đề RQ điều chuyển |

**Đặc tả fields - Danh sách tài sản nhập kho:**

| Field name VN | Operator | Action | M/O | Data rule |
|---------------|----------|--------|-----|-----------|
| Mã tài sản | System | Display | M | Hiển thị mặc định |
| Tên Tài sản | System | Display | M | Hiển thị mặc định |
| Mô tả TS | System | Display | M | Hiển thị mặc định |
| Trạng thái TS | System | Display | M | Hiển thị mặc định |
| Phân nhóm TS (group name) | System | Display | M | Hiển thị mặc định |
| Nhóm TS (CAT1) | System | Display | M | Hiển thị mặc định |
| Số PO | System | Display | M | Hiển thị mặc định |
| Tên nhà cung cấp | System | Display | O | Ẩn hiện tùy biến |
| Nguyên giá TS (VAT incl) | System | Display | M | Ẩn hiện tùy biến |
| Mã TS liên quan | System | Display | O | Ẩn hiện tùy biến |
| Mô tả TS liên quan | System | Display | O | Ẩn hiện tùy biến |
| Tên người sử dụng | System | Display | M | Hiển thị mặc định |
| Tên đơn vị | System | Display | M | Hiển thị mặc định |
| Mã nhân viên | System | Display | M | Ẩn hiện tùy biến |
| Đơn vị sử dụng cha | System | Display | M | Hiển thị mặc định |
| Email nhân viên | System | Display | M | Ẩn hiện tùy biến |
| Địa chỉ đặt TS | System | Display | O | Ẩn hiện tùy biến |
| Tầng đặt TS | System | Display | O | Ẩn hiện tùy biến |
| Phòng đặt TS | System | Display | O | Ẩn hiện tùy biến |
| Ngày bắt đầu bảo hành | System | Display | O | Ẩn hiện tùy biến |
| Thời hạn bảo hành | System | Display | O | Ẩn hiện tùy biến |
| Ngày kết thúc bảo hành | System | Display | O | Ẩn hiện tùy biến |
| Công ty bảo hành | System | Display | O | Ẩn hiện tùy biến |
| Tên người liên hệ bảo hành | System | Display | O | Ẩn hiện tùy biến |
| Điện thoại người liên hệ | System | Display | O | Ẩn hiện tùy biến |

**Quy trình cập nhật:**
- RQ điều chuyển: Trạng thái chuyển từ "Chờ xác nhận" → "Đã xác nhận"
- RQ nhập kho: Trạng thái khởi tạo "Chờ phê duyệt"
- Tasklist AMP: Cập nhật thành "Đã xử lý"
- Tasklist WM: Cập nhật thành "Cần xử lý"
- Tài sản: Unlock từ RQ điều chuyển, Lock cho RQ nhập kho

#### 4.2.2. Approve Warehouse Entry Request

##### 4.2.2.1. Thông số kỹ thuật giao diện người dùng

Giao diện phê duyệt yêu cầu nhập kho cho phép Warehouse Manager xem xét và quyết định về các yêu cầu nhập kho đã được tạo. Màn hình được thiết kế với ba phần chính: tìm kiếm yêu cầu, hiển thị chi tiết, và thực hiện quyết định.

![Giao diện phê duyệt yêu cầu nhập kho](images/5.1.2a_B5_image4.png)

**Luồng xử lý:**
1. Warehouse Manager tìm kiếm yêu cầu theo các tiêu chí
2. Xem chi tiết thông tin tài sản và thông tin liên quan
3. Đưa ra quyết định phê duyệt hoặc từ chối
4. Hệ thống cập nhật trạng thái và thông báo cho các bên liên quan

**Các bên liên quan:** Warehouse Manager (phê duyệt), Warehouse Keeper (nhận thông báo sau phê duyệt), AMP (nhận thông báo khi từ chối)

##### 4.2.2.2. Thông số kỹ thuật chi tiết

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

**Bảng hiển thị kết quả tìm kiếm:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| System | Display | Số yêu cầu | M | Text | N | 20 |
| System | Display | Ngày tạo | M | Date | N | 20 |
| System | Display | Tiêu đề | M | Text | N | 150 |
| System | Display | Người tạo | M | Text | N | 20 |
| System | Display | Trạng thái yêu cầu | M | Text | N | 20 |
| System | Display | Người xử lý | O | Text | N | 20 |
| System | Display | Ngày xác nhận | O | Date | N | 20 |

**Quy trình quyết định:**
- **Phê duyệt:** Cập nhật trạng thái RQ nhập kho thành "Chờ nhập kho", thông báo cho WK
- **Từ chối:** Cập nhật cả RQ nhập kho và RQ điều chuyển thành "Từ chối", unlock tài sản, thông báo cho AMP và BU

#### 4.2.3. Warehouse Receipt Confirmation

##### 4.2.3.1. Thông số kỹ thuật giao diện người dùng  

Chức năng xác nhận nhập kho cho phép Warehouse Keeper thực hiện việc tiếp nhận tài sản vào kho sau khi yêu cầu đã được phê duyệt. Đây là bước cuối cùng trong quy trình nhập kho từ điều chuyển tài sản.

![Giao diện xác nhận nhập kho](images/5_1_3a_B5_image3.png)

**Cấu trúc giao diện:**
- Phần tìm kiếm và danh sách yêu cầu cần xử lý
- Phần chi tiết thông tin tài sản với đầy đủ 26 trường thông tin
- Phần thông tin kho nhập, đầu mối giao hàng
- Phần hồ sơ đính kèm và lịch sử xử lý
- Các nút chức năng: Từ chối (với lý do) và Xác nhận

##### 4.2.3.2. Thông số kỹ thuật chi tiết

**Bảng thông tin tìm kiếm yêu cầu:**

| Field name VN | M/O | Field type | Editable | Max length | Operator | Action |
|---------------|-----|------------|----------|------------|-----------|---------|
| Số yêu cầu | O | Text | Y | 20 | User | Input |
| Ngày tạo | O | Date | Y | 20 | User | Input |
| Tiêu đề | O | Text | Y | 150 | User | Input |
| Người tạo | O | List | Y | 20 | User | Select |
| Trạng thái yêu cầu | O | List | Y | 20 | User | Select |
| Người xử lý | O | List | Y | 20 | User | Select |
| Ngày xác nhận | O | Date | Y | 20 | User | Input |

**Bảng thông tin tài sản chi tiết (một phần quan trọng):**

| Field name VN | M/O | Field type | Editable | Data rule |
|---------------|-----|------------|----------|-----------|
| Mã tài sản | M | - | N | Hiển thị mặc định |
| Tên Tài sản | M | - | N | Hiển thị mặc định |
| Mô tả TS | M | - | N | Hiển thị mặc định |
| Trạng thái TS | M | - | N | Hiển thị mặc định |
| Phân nhóm TS (group name) | M | - | N | Hiển thị mặc định |
| Nhóm TS (CAT1) | M | - | N | Hiển thị mặc định |
| Số PO | M | - | N | Hiển thị mặc định |
| Tên nhà cung cấp | O | - | N | Ẩn hiện tùy biến |
| Nguyên giá TS (VAT incl) | M | - | N | Ẩn hiện tùy biến |
| Tên người sử dụng | M | - | N | Hiển thị mặc định |
| Tên đơn vị | M | - | N | Hiển thị mặc định |
| Mã nhân viên | M | - | N | Ẩn hiện tùy biến |
| Email nhân viên | M | - | N | Ẩn hiện tùy biến |

**Quy trình xử lý:**
1. **Từ chối:** Bắt buộc nhập lý do → unlock tài sản → cập nhật trạng thái "Từ chối" → thông báo AMP và BU
2. **Xác nhận:** Cập nhật trạng thái "Đã nhập kho" → cập nhật thông tin tài sản → unlock tài sản → hoàn tất quy trình

Sau khi xác nhận thành công, quy trình nhập kho từ điều chuyển về kho được hoàn tất và có thể chuyển sang [quy trình nhập kho thủ công](#424-manual-warehouse-entry) nếu cần.

#### 4.2.4. Manual Warehouse Entry  

##### 4.2.4.1. Thông số kỹ thuật giao diện người dùng

Quy trình nhập kho thủ công cho phép người dùng tạo yêu cầu nhập kho một cách chủ động thay vì thông qua quy trình điều chuyển tự động. Điều này phù hợp với các trường hợp nhập kho đặc biệt hoặc bổ sung.

![Giao diện tạo yêu cầu nhập kho thủ công](images/5_2_1a_B5_image4.png)

**Quy trình gồm ba bước chính:**
1. [Tạo yêu cầu](#421-create-warehouse-intake-request) với thông tin chi tiết
2. [Phê duyệt yêu cầu](#422-approve-warehouse-entry-request) bởi Warehouse Manager 
3. [Xác nhận nhập kho](#423-warehouse-receipt-confirmation) bởi Warehouse Keeper

**Đặc điểm khác biệt:** Khác với nhập kho từ điều chuyển, quy trình thủ công yêu cầu người dùng tự chọn tài sản và nhập đầy đủ thông tin kho nhập, đầu mối giao hàng.

##### 4.2.4.2. Thông số kỹ thuật chi tiết

**Tạo yêu cầu nhập kho thủ công:**

| Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|-------------|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx |  | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Thông tin chung | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today |  |
| Thông tin chung | User | Input | Tiêu đề | O | Text | Y | 150 |  |  |  |
| Tìm kiếm tài sản | User | Input | Mã tài sản | O | Text | N | 20 |  |  |  |
| Tìm kiếm tài sản | User | Input | Tên tài sản | O | Text | Y | 20 |  |  |  |
| Tìm kiếm tài sản | User | Select | Phân loại tài sản | O | List | N | 20 |  |  |  |
| Tìm kiếm tài sản | User | Select | Nhóm tài sản | O | List | N | 20 |  |  |  |
| Tìm kiếm tài sản | User | Input | PO number | O | Text | Y | 20 |  |  |  |
| Tìm kiếm tài sản | User | Select | Trạng thái TS | O | List | N | 50 |  |  |  |
| Tìm kiếm tài sản | User | Select | Tên nhà cung cấp | O | List | N | 50 |  |  |  |
| Tìm kiếm tài sản | User | Input | Tên kho | O | List | Y | 50 |  |  |  |
| Tìm kiếm tài sản | User | Select | Vị trí đặt tài sản | O | Text | N | 100 |  |  |  |

**Thông tin kho và đầu mối:**

| Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|-------------|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| Thông tin kho nhập | System/User | Display/Search/Select | Tên kho | M | List | N | 50 |  |  |
| Thông tin kho nhập | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Thông tin kho nhập | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Thông tin đầu mối giao hàng | User | Input | Đầu mối | M | Text | Y | 50 |  |  |
| Thông tin đầu mối giao hàng | User | Input | Số điện thoại | M | Number | Y | 52 |  |  |
| Thông tin đầu mối giao hàng | User | Input | Thời gian bàn giao | O | Date | Y | 50 |  |  |

**Quy trình phê duyệt nhập kho thủ công:**

Quy trình phê duyệt cho nhập kho thủ công tương tự như [quy trình phê duyệt yêu cầu nhập kho](#422-approve-warehouse-entry-request) từ điều chuyển, với các điểm khác biệt:

- Warehouse Manager có thể từ chối với lý do bắt buộc (150 ký tự)
- Khi từ chối: unlock tài sản và thông báo cho AMP
- Khi phê duyệt: chuyển trạng thái thành "Chờ nhập kho" và thông báo cho WK

**Bảng cập nhật trạng thái:**

| Hành động | Trạng thái mới | Tasklist WM | Tasklist AMP | Tasklist WK |
|-----------|----------------|-------------|--------------|-------------|
| Từ chối | Từ chối | Đã xử lý | Cần xử lý | - |
| Phê duyệt | Chờ nhập kho | Đã xử lý | Không update | Cần xử lý |

**Xác nhận nhập kho thủ công:**

![Giao diện xác nhận nhập kho thủ công](images/5_2_3a_B6_image6.png)

Bước cuối cùng trong quy trình nhập kho thủ công được thực hiện bởi Warehouse Keeper với các yêu cầu tương tự như [xác nhận nhập kho từ điều chuyển](#423-warehouse-receipt-confirmation):

- Tìm kiếm yêu cầu theo 7 tiêu chí
- Hiển thị 25+ trường thông tin tài sản
- Hỗ trợ từ chối với lý do hoặc xác nhận
- Tự động cập nhật ngày bắt đầu sử dụng khi xác nhận
- Gửi thông báo cho AMP sau khi hoàn thành

#### 4.2.5. Cancel Warehouse Entry Request

##### 4.2.5.1. Thông số kỹ thuật giao diện người dùng

Chức năng hủy yêu cầu nhập kho cho phép người dùng có thẩm quyền hủy bỏ các yêu cầu nhập kho đã được tạo nhưng chưa hoàn thành. Điều kiện để thực hiện hủy là yêu cầu nhập kho phải đã gửi đi thành công nhưng chưa có trạng thái "Đã nhập kho".

![Giao diện hủy yêu cầu nhập kho](images/5_3_1a_B5_image7.png)

**Quy trình hủy yêu cầu:**
1. Tìm kiếm yêu cầu nhập kho theo các tiêu chí
2. Chọn và xem chi tiết yêu cầu
3. Nhập lý do hủy (bắt buộc)
4. Hệ thống unlock tài sản và cập nhật trạng thái
5. Thông báo cho các bên liên quan

**Các bên liên quan:** AMP (thực hiện hủy), WM (quản lý), BU user (nhận thông báo)

##### 4.2.5.2. Thông số kỹ thuật chi tiết

**Điều kiện hủy yêu cầu:**
- Yêu cầu nhập kho đã được gửi thành công
- Trạng thái yêu cầu ≠ "Đã nhập kho"

**Bảng trường tìm kiếm yêu cầu:**

| Trường | Operator | Action | M/O | Field Type | Editable | Max Length |
|--------|----------|--------|-----|------------|----------|------------|
| Số yêu cầu | User | Input | O | Text | Y | 20 |
| Ngày tạo | User | Input | O | Date | Y | 20 |
| Tiêu đề | User | Input | O | Text | Y | 150 |
| Người tạo | User | Select | O | List | Y | 20 |
| Trạng thái yêu cầu | User | Select | O | List | Y | 20 |
| Người xử lý | User | Select | O | List | Y | 20 |
| Ngày xác nhận | User | Input | O | Date | Y | 20 |

**Bảng thông tin tài sản với cấu hình hiển thị:**

| Trường | M/O | Editable | Quy tắc hiển thị |
|--------|-----|----------|------------------|
| Mã tài sản | M | N | Hiển thị mặc định |
| Tên Tài sản | M | N | Hiển thị mặc định |
| Mô tả TS | M | N | Hiển thị mặc định |
| Trạng thái TS | M | N | Hiển thị mặc định |
| Phân nhóm TS | M | N | Hiển thị mặc định |
| Nhóm TS (CAT1) | M | N | Hiển thị mặc định |
| Số PO | M | N | Hiển thị mặc định |
| Tên nhà cung cấp | O | N | Ẩn hiện tùy biến |
| Nguyên giá TS (VAT incl) | M | N | Ẩn hiện tùy biến |
| Mã TS liên quan | O | N | Ẩn hiện tùy biến |
| Tên người sử dụng | M | N | Hiển thị mặc định |
| Tên đơn vị | M | N | Hiển thị mặc định |
| Mã nhân viên | M | N | Ẩn hiện tùy biến |
| Email nhân viên | M | N | Ẩn hiện tùy biến |

**Quy trình xử lý hủy:**
1. **Nhập lý do hủy:** Bắt buộc, tối đa 150 ký tự
2. **Unlock tài sản:** Cho phép tài sản được sử dụng trong yêu cầu khác
3. **Cập nhật trạng thái:** RQ nhập kho và RQ điều chuyển liên quan → "Đã hủy"
4. **Cập nhật tasklist:** WM → "Đã xử lý", AMP/BU user → "Cần xử lý"
5. **Thông báo:** Gửi email cho BU/user về việc hủy yêu cầu

Sau khi hủy yêu cầu nhập kho, người dùng có thể tạo [yêu cầu nhập kho mới](#424-manual-warehouse-entry) hoặc chuyển sang [quy trình cấp tài sản](#426-asset-allocation-process).

#### 4.2.6. Asset Allocation Process

##### 4.2.6.1. Thông số kỹ thuật giao diện người dùng

Quy trình cấp tài sản bao gồm hai luồng chính: cấp tài sản không ở kho (luồng đơn giản) và cấp tài sản từ kho (luồng phức tạp). Module này xử lý quy trình cấp tài sản từ kho với workflow phê duyệt đa cấp và tự động tạo yêu cầu xuất kho.

![Giao diện phê duyệt yêu cầu cấp tài sản](images/5_4_0a_B5_image8.png)

**Luồng cấp tài sản từ kho:**
1. AMP tạo yêu cầu cấp tài sản
2. AM phê duyệt yêu cầu
3. Hệ thống tự động tạo yêu cầu xuất kho
4. WK tiếp nhận và xử lý xuất kho
5. Warehouse Manager phê duyệt xuất kho
6. BU User nhận tài sản

**Các bên liên quan:** Asset Manager (phê duyệt), Asset Management Partner (xử lý), BU User (nhận tài sản), Warehouse Keeper (xuất kho)

##### 4.2.6.2. Thông số kỹ thuật chi tiết

**Phê duyệt yêu cầu cấp tài sản:**

**Bảng thông tin tìm kiếm yêu cầu:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max Length |
|--------|----------|--------|------------|-----|------|----------|------------|
| User | Input | Mã yêu cầu | M | Text | Y | 20 |
| User | Input | Tiêu đề | M | Text | Y | 150 |
| User | Select | Người tạo | M | List | Y | 20 |
| User | Select | Trạng thái | M | List | Y | 20 |
| User | Input | Ngày tạo | M | Date | Y | 20 |
| User | Select | Loại cấp tài sản | M | List | Y | 100 |
| User | Select | Người xử lý | M | List | Y | 20 |
| User | Input | Ngày xác nhận | M | Date | Y | 20 |

**Bảng thông tin tài sản chi tiết:**

| Trường | Operator | Action | Tên trường | M/O | Editable | Quy tắc hiển thị |
|--------|----------|--------|------------|-----|----------|------------------|
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

**Bảng thông tin người nhận:**

| Trường | Operator | Action | Tên trường | M/O | Max Length | Default | Data Source | Quy tắc |
|--------|----------|--------|------------|-----|------------|---------|-------------|---------|
| System/User | Display/Search/Select | Tên Người nhận | M | 50 | = Người khởi tạo | OMS | |
| System | Display | Tên ĐVKD/ Phòng ban HO | M | 50 | | OMS | Tự động nhận diện, hiển thị tên đơn vị Người khởi tạo |
| System | Display | Địa chỉ nhận | M | 150 | | OMS | Tự động nhận diện, hiển thị Khối theo Người khởi tạo |
| System/User | Display/Input | Điện thoại di động | M | 50 | | OMS | Tự động nhận diện, hiển thị số điện thoại của Người khởi tạo |

**Tạo yêu cầu xuất kho:**

![Giao diện tạo yêu cầu xuất kho](images/5_4_1a_B6_image9.png)

Sau khi AM phê duyệt yêu cầu cấp tài sản, hệ thống tự động tạo yêu cầu xuất kho với các thông tin kế thừa:

**Bảng thông tin chung yêu cầu xuất kho:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Độ dài | Format | Default | Data rule |
|--------|----------|--------|------------|-----|------|----------|--------|--------|---------|-----------|
| Số yêu cầu | System | Display | Số yêu cầu | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 |
| Ngày tạo | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | System | Input | Tiêu đề | O | Text | Y | 150 | | | =Tiêu đề RQ Cấp/Thanh lý |

**Bảng thông tin kho xuất:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Độ dài | Data source |
|--------|----------|--------|------------|-----|------|----------|--------|-------------|
| Tên kho | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | = Thông tin kho trên RQ cấp/Thanh lý |
| Địa chỉ kho | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS |
| Quản lý kho | System | Display | Quản lý kho | M | Text | N | 50 | OMS |

**Bảng thông tin đầu mối nhận hàng:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Độ dài |
|--------|----------|--------|------------|-----|------|----------|--------|
| Đầu mối | User | Input | Đầu mối | M | Text | Y | 50 |
| Số điện thoại | User | Input | Số điện thoại | M | Number | Y | 52 |
| Thời gian bàn giao | User | Input | Thời gian bàn giao | O | Date | Y | 50 |

**Tiếp nhận yêu cầu xuất kho:**

![Giao diện tiếp nhận yêu cầu xuất kho](images/5_4_2a_B6_image10.png)

WK tiếp nhận và xử lý yêu cầu xuất kho với khả năng chấp thuận hoặc từ chối. Đặc biệt, hệ thống ẩn nút "Từ chối" nếu yêu cầu xuất kho xuất phát từ yêu cầu thanh lý.

**Bảng cập nhật trạng thái:**

| Bước | Thực hiện bởi | Action | Đối tượng | Trạng thái mới |
|------|---------------|--------|-----------|----------------|
| 5 | System | Update | RQ Cấp tài sản | Từ chối |
| 5 | System | Update | RQ Xuất kho | Từ chối |
| 9 | System | Update | RQ Cấp tài sản | Đã xác nhận |
| 9 | System | Update | RQ Xuất kho | Chờ xác nhận |

**Phê duyệt yêu cầu xuất kho:**

![Giao diện phê duyệt yêu cầu xuất kho](images/5_4_3a_B5_image11.png)

Warehouse Manager thực hiện phê duyệt cuối cùng cho yêu cầu xuất kho với logic tương tự như [phê duyệt yêu cầu nhập kho](#422-approve-warehouse-entry-request).

**Nhận tài sản:**

![Giao diện nhận tài sản](images/5_4_4a_B6_image12.png)

Bước cuối cùng là BU User xác nhận nhận tài sản, hoàn tất quy trình cấp tài sản từ kho. Sau khi xác nhận, trạng thái tài sản chuyển thành "Đã nhận tài sản" và thông tin sử dụng tài sản được cập nhật.

#### 4.2.7. Cancel Asset Allocation Request

##### 4.2.7.1. Thông số kỹ thuật giao diện người dùng

Chức năng hủy yêu cầu xuất kho cho phép AMP hủy bỏ các yêu cầu xuất kho đã được tạo nhưng chưa hoàn thành. Điều kiện để thực hiện hủy là yêu cầu xuất kho phải có trạng thái khác "Đã xác nhận".

![Giao diện hủy yêu cầu xuất kho](images/5_5_1a_B5_image13.png)

**Quy trình hủy yêu cầu xuất kho:**
1. Tìm kiếm yêu cầu xuất kho cần hủy
2. Chọn và xem chi tiết yêu cầu
3. Nhập lý do hủy (bắt buộc)
4. Hệ thống unlock tài sản và trả về trạng thái trước thanh lý
5. Cập nhật trạng thái và thông báo cho WK

**Lưu ý đặc biệt:** Ẩn nút "Từ chối" đối với RQ xuất kho liên kết với RQ thanh lý. Có câu hỏi mở về trường hợp AMP muốn hủy yêu cầu xuất kho từ request thanh lý.

##### 4.2.7.2. Thông số kỹ thuật chi tiết

**Điều kiện hủy yêu cầu:**
- Yêu cầu xuất kho đã tạo thành công
- Trạng thái ≠ "Đã xác nhận"

**Bảng tìm kiếm yêu cầu xuất kho:**

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

**Bảng thông tin chung yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| System | Display | Số yêu cầu | M | Text | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 |
| System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| System | Input | Tiêu đề | O | Text | Y | 150 | | | |

**Bảng danh sách tài sản xuất kho (các trường chính):**

| Field name VN | M/O | Editable | Data rule |
|---------------|-----|----------|-----------|
| Mã tài sản | M | N | Hiển thị mặc định |
| Tên Tài sản | M | N | Hiển thị mặc định |
| Mô tả TS | M | N | Hiển thị mặc định |
| Trạng thái TS | M | N | Hiển thị mặc định |
| Phân nhóm TS (group name) | M | N | Hiển thị mặc định |
| Nhóm TS (CAT1) | M | N | Hiển thị mặc định |
| Số PO | M | N | Hiển thị mặc định |
| Tên người sử dụng | M | N | Hiển thị mặc định |
| Tên đơn vị | M | N | Hiển thị mặc định |

**Quy trình xử lý hủy:**
1. **Điều kiện tiên quyết:** Trạng thái ≠ "Đã xác nhận"
2. **Nhập lý do hủy:** Bắt buộc (mandatory), editable, max 150 ký tự
3. **Unlock asset:** Cho phép asset được pickup cho request khác
4. **Trả về trạng thái:** Asset trở về trạng thái trước khi thanh lý
5. **Cập nhật RQ:** Cấp/Thanh lý → "Đã hủy"
6. **Thông báo:** Gửi email notification cho WK

Sau khi hủy yêu cầu xuất kho, người dùng có thể quay lại [quy trình cấp tài sản](#426-asset-allocation-process) hoặc chuyển sang [quản lý điều chuyển kho](#428-warehouse-transfer-management).

#### 4.2.8. Warehouse Transfer Management

##### 4.2.8.1. Thông số kỹ thuật giao diện người dùng

Module quản lý điều chuyển kho hỗ trợ việc di chuyển tài sản giữa các kho khác nhau trong hệ thống. Quy trình bao gồm tạo yêu cầu điều chuyển và phê duyệt yêu cầu với workflow tự động.

![Giao diện tạo yêu cầu điều chuyển kho](images/5_6_1a_B6_image14.png)

**Quy trình điều chuyển kho:**
1. Tạo yêu cầu điều chuyển với thông tin kho đi và kho đến
2. Hệ thống tự động lock tài sản và gán người duyệt
3. Asset Manager và Warehouse Manager phê duyệt yêu cầu
4. Tự động tạo phiếu xuất kho và phiếu nhập kho
5. Thực hiện điều chuyển và cập nhật vị trí tài sản

**Các bên liên quan:** User (tạo yêu cầu), Asset Manager (phê duyệt), Warehouse Manager (quản lý), WK (thực hiện điều chuyển)

##### 4.2.8.2. Thông số kỹ thuật chi tiết

**Tạo yêu cầu điều chuyển kho:**

**Bảng thông tin chung:**

| Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|-------------|----------|---------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| | User | Input | Tiêu đề | O | Text | Y | 150 | | | |
| | User | Select | Thêm tài sản | M | Button | N | | | | |

**Bảng tìm kiếm tài sản:**

| Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|-------------|----------|---------|---------------|-----|------------|----------|------------|
| Tìm kiếm tài sản | User | Input | Mã tài sản | O | Text | N | 20 |
| | User | Input | Tên tài sản | O | Text | Y | 20 |
| | User | Select | Phân loại tài sản | O | List | N | 20 |
| | User | Select | Nhóm tài sản | O | List | N | 20 |
| | User | Input | PO number | O | Text | Y | 20 |
| | User | Select | Trạng thái TS | O | List | N | 50 |
| | User | Select | Tên nhà cung cấp | O | List | N | 50 |
| | User | Input | Tên kho | O | List | Y | 50 |
| | User | Select | Vị trí đặt tài sản | O | Text | N | 100 |

**Bảng thông tin kho:**

| Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|---------|----------|---------|---------------|-----|------------|----------|------------|-------------|-----------|
| Kho đi | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | |
| | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |
| Kho nhập | User | Select | Tên kho | M | List | N | 50 | | |
| | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

**Bảng thông tin đầu mối giao hàng:**

| Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|-------------|----------|---------|---------------|-----|------------|----------|------------|
| Thông tin đầu mối giao hàng | User | Input | Đầu mối | M | Text | Y | 50 |
| | User | Input | Số điện thoại | M | Number | Y | 52 |
| | User | Input | Thời gian bàn giao | O | Date | Y | 50 |
| | User | Input | Ghi chú | M | Text | Y | 150 |

**Quy trình tự động:**
1. **Tạo yêu cầu:** Mã số CK.YY.xxxx, lock tài sản
2. **Gán người duyệt:** Tự động tìm và gán AM và WM phù hợp  
3. **Cập nhật trạng thái:** "Chờ phê duyệt"
4. **Tasklist:** AM và WM → "Cần xử lý"
5. **Thông báo:** Email cho AM và Warehouse Manager

**Phê duyệt yêu cầu điều chuyển kho:**

![Giao diện phê duyệt yêu cầu điều chuyển kho](images/5_6_2a_B5_image15.png)

Approver thực hiện phê duyệt yêu cầu điều chuyển kho với các tùy chọn phê duyệt hoặc từ chối:

**Bảng tìm kiếm yêu cầu:**

| Toán tử | Hành động | Tên trường | M/O | Loại dữ liệu | Có thể chỉnh sửa | Độ dài tối đa |
|---------|-----------|------------|-----|--------------|------------------|---------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Xử lý phê duyệt:**
- **Phê duyệt:** Tự động tạo biên bản điều chuyển, cập nhật thông tin kho của tài sản, thông báo cho WK kho đi và kho đến
- **Từ chối:** Unlock tài sản, thông báo cho AMP, cập nhật tasklist

Quy trình điều chuyển kho được tích hợp chặt chẽ với [quy trình nhập kho](#421-create-warehouse-intake-request) để đảm bảo tính liên tục và chính xác trong quản lý tài sản.

## 5. Assumptions & Constraints

### Giả định

- Tất cả người dùng đã được đào tạo về quy trình nghiệp vụ hiện tại
- Hệ thống OMS, EMS, ITSM hoạt động ổn định và có API tích hợp
- Dữ liệu master data (tài sản, kho, người dùng) đã được chuẩn hóa
- Network infrastructure hỗ trợ đủ băng thông cho việc truyền tải dữ liệu
- Quy trình phê duyệt hiện tại được duy trì trong hệ thống mới

### Ràng buộc

- **Thời gian:** Dự án phải hoàn thành trong Q2 2024
- **Ngân sách:** Không vượt quá ngân sách đã được phê duyệt
- **Công nghệ:** Sử dụng platform hiện tại, không thay đổi kiến trúc tổng thể
- **Bảo mật:** Tuân thủ các quy định về bảo mật thông tin nội bộ
- **Tương thích:** Phải tương thích với các module FAM hiện có

### Ràng buộc kỹ thuật

- Dashboard phải load trong thời gian < 3 giây
- Hỗ trợ đồng thời tối thiểu 100 concurrent users
- Database backup hàng ngày, recovery time < 4 giờ
- API response time < 2 giây cho 95% requests
- Uptime tối thiểu 99.5%

## 6. Dependencies

### Hệ thống nội bộ

- **OMS (Organization Management System):** Cung cấp thông tin tổ chức, nhân sự và cấu trúc phòng ban
- **EMS:** Đồng bộ thông tin PO và tiêu đề, cung cấp thông tin thời gian phê duyệt PO
- **ITSM:** Tích hợp với Module sửa chữa tài sản cho việc quản lý ticket
- **Email Server:** Gửi thông báo tự động cho các quy trình nghiệp vụ

### Dependencies kỹ thuật

- **Database Server:** SQL Server phiên bản tối thiểu 2019
- **Application Server:** IIS với .NET Framework 4.8 trở lên
- **Web Browser:** Hỗ trợ Chrome 90+, Firefox 85+, Edge 90+
- **Network:** Kết nối stable giữa các hệ thống

### Dependencies nghiệp vụ

- Hoàn thiện quy định về phân quyền người dùng
- Cập nhật SOP cho các quy trình mới
- Đào tạo end-users trước khi go-live
- Backup và migration plan cho dữ liệu hiện có

## 7. Acceptance Criteria

### Functional Acceptance Criteria

#### Dashboard tài sản
- ✅ Hiển thị 4 thông số tổng quan chính xác 
- ✅ 5 loại biểu đồ hoạt động với tính năng hover và click
- ✅ Bộ lọc đa tiêu chí hoạt động chính xác
- ✅ Tính năng xuất Excel thành công
- ✅ Đồng bộ dữ liệu từ OMS real-time

#### Module quản lý kho
- ✅ Tất cả 8 quy trình con hoạt động đúng logic nghiệp vụ
- ✅ Workflow phê duyệt đa cấp chính xác
- ✅ Tự động tạo yêu cầu liên quan (nhập/xuất kho)
- ✅ Lock/unlock tài sản hoạt động chính xác
- ✅ Email notification gửi đúng người và đúng thời điểm
- ✅ Cập nhật trạng thái và tasklist tự động

### Performance Acceptance Criteria
- ✅ Dashboard load time < 3 giây
- ✅ Form submission response < 2 giây  
- ✅ Hỗ trợ 100+ concurrent users
- ✅ Uptime ≥ 99.5%
- ✅ Database query optimization với index phù hợp

### Security Acceptance Criteria
- ✅ Authentication qua Active Directory
- ✅ Role-based access control chính xác
- ✅ Audit trail cho tất cả transactions
- ✅ Data encryption cho sensitive information
- ✅ Session timeout sau 30 phút inactive

### Integration Acceptance Criteria
- ✅ Tích hợp OMS: Đồng bộ orgchart và thông tin nhân sự
- ✅ Tích hợp EMS: Lấy tiêu đề PO và thời gian phê duyệt
- ✅ Tích hợp ITSM: Module sửa chữa tài sản
- ✅ Email integration: Gửi notification tự động
- ✅ API endpoints hoạt động stable

## 8. Glossary

### Thuật ngữ nghiệp vụ

- **AMP (Asset Management Personnel):** Nhân viên quản lý tài sản, thực hiện các tác vụ điều hành hàng ngày
- **AM (Asset Manager):** Quản lý tài sản cấp cao, có quyền phê duyệt các yêu cầu quan trọng
- **BU User:** Người dùng thuộc đơn vị kinh doanh, người yêu cầu và sử dụng tài sản
- **WK (Warehouse Keeper):** Thủ kho, thực hiện các tác vụ xuất nhập kho thực tế
- **Warehouse Manager:** Quản lý kho, phê duyệt các yêu cầu liên quan đến kho

### Thuật ngữ kỹ thuật

- **Dashboard:** Bảng điều khiển tổng quan hiển thị các thông số quan trọng
- **Workflow:** Luồng công việc được định nghĩa với các bước và điều kiện cụ thể
- **Lock/Unlock:** Cơ chế khóa tài sản để tránh xung đột khi có nhiều yêu cầu đồng thời
- **Tasklist:** Danh sách công việc được gán cho từng vai trò người dùng
- **Real-time sync:** Đồng bộ dữ liệu theo thời gian thực

### Thuật ngữ hệ thống

- **OMS (Organization Management System):** Hệ thống quản lý tổ chức và nhân sự
- **EMS:** Hệ thống quản lý và đồng bộ thông tin Purchase Order
- **ITSM:** Hệ thống quản lý dịch vụ CNTT
- **API:** Application Programming Interface, giao diện lập trình ứng dụng
- **SOP:** Standard Operating Procedure, quy trình vận hành chuẩn

### Trạng thái và mã số

- **NK.YY.xxxx:** Format mã yêu cầu nhập kho (NK = Nhập Kho, YY = năm, xxxx = số thứ tự)
- **XK.YY.xxxx:** Format mã yêu cầu xuất kho (XK = Xuất Kho, YY = năm, xxxx = số thứ tự)  
- **CK.YY.xxxx:** Format mã yêu cầu chuyển kho (CK = Chuyển Kho, YY = năm, xxxx = số thứ tự)
- **Chờ phê duyệt:** Trạng thái yêu cầu đang chờ người có thẩm quyền xem xét
- **Đã xác nhận:** Trạng thái yêu cầu đã được phê duyệt và thực hiện thành công

---

*Tài liệu này được tạo bởi nhóm phát triển FAM Wave 4 và sẽ được cập nhật theo tiến độ dự án.*

---

*Generated by Claude Sonnet 4.5 from 37 sheet summaries*
*Headings: 43 | Internal Links: 42*

*✅ All internal links validated successfully*
