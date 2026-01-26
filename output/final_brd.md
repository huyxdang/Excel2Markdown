# Tài liệu Yêu cầu Nghiệp vụ - FAM Wave 4

## Mục lục

1. [Executive Summary](#1-executive-summary)
2. [Project Scope & Objectives](#2-project-scope-objectives)
3. [Stakeholders](#3-stakeholders)
4. [Business Requirements](#4-business-requirements)
   - 4.1. [Asset Dashboard Module](#41-asset-dashboard-module)
   - 4.2. [Warehouse Management Module](#42-warehouse-management-module)
     - 4.2.1. [Create Warehouse Intake Request](#421-create-warehouse-intake-request)
     - 4.2.2. [Approve Warehouse Intake Request](#422-approve-warehouse-intake-request)
     - 4.2.3. [Warehouse Intake Confirmation](#423-warehouse-intake-confirmation)
     - 4.2.4. [Manual Warehouse Intake Process](#424-manual-warehouse-intake-process)
     - 4.2.5. [Cancel Warehouse Intake Request](#425-cancel-warehouse-intake-request)
   - 4.3. [Asset Provisioning Module](#43-asset-provisioning-module)
   - 4.4. [Inter-Warehouse Transfer Module](#44-inter-warehouse-transfer-module)
     - 4.4.1. [Create Inter-Warehouse Transfer Request](#441-create-inter-warehouse-transfer-request)
     - 4.4.2. [Approve Inter-Warehouse Transfer Request](#442-approve-inter-warehouse-transfer-request)
   - 4.5. [Warehouse Export Module](#45-warehouse-export-module)
5. [System Integration Requirements](#5-system-integration-requirements)
6. [Workflow & Status Management](#6-workflow-status-management)
7. [Assumptions & Constraints](#7-assumptions-constraints)
8. [Dependencies](#8-dependencies)
9. [Acceptance Criteria](#9-acceptance-criteria)

---

## 1. Executive Summary

Dự án FAM Wave 4 là một chương trình nâng cấp toàn diện hệ thống quản lý tài sản cố định (Fixed Asset Management) nhằm cải thiện hiệu quả quản lý và tự động hóa quy trình nghiệp vụ. Dự án tập trung vào việc phát triển các module chức năng mới và nâng cấp các tính năng hiện có để đáp ứng nhu cầu quản lý tài sản ngày càng phức tạp của tổ chức.

Các sản phẩm chính bao gồm [module dashboard tài sản tương tác](#41-asset-dashboard-module) với khả năng trực quan hóa dữ liệu, [module quản lý kho toàn diện](#42-warehouse-management-module) hỗ trợ đầy đủ quy trình xuất nhập kho, và [module điều chuyển tài sản giữa các kho](#44-inter-warehouse-transfer-module). Hệ thống cũng được tích hợp với các hệ thống hiện có như OMS và EMS để đảm bảo đồng bộ dữ liệu và tối ưu hóa quy trình nghiệp vụ.

Dự án được thiết kế với workflow phê duyệt nhiều cấp, hỗ trợ tự động hóa các quy trình lặp lại và cung cấp khả năng theo dõi, kiểm soát chặt chẽ tất cả các hoạt động liên quan đến tài sản.

## 2. Project Scope & Objectives

### Trong phạm vi dự án

- Phát triển [dashboard tài sản](#41-asset-dashboard-module) với khả năng trực quan hóa và tùy biến theo nhiều tiêu chí
- Xây dựng [module quản lý kho](#42-warehouse-management-module) hoàn chỉnh hỗ trợ các quy trình xuất nhập kho tự động và thủ công
- Triển khai [module cấp tài sản](#43-asset-provisioning-module) với quy trình phê duyệt tối ưu
- Phát triển [module điều chuyển tài sản](#44-inter-warehouse-transfer-module) giữa các kho
- Tích hợp với hệ thống OMS để đồng bộ orgchart và thông tin kho
- Tích hợp với hệ thống EMS để đồng bộ thông tin PO và thời gian đưa vào sử dụng
- Cải tiến các tính năng hiện có: ẩn/hiện tài sản vô hiệu hóa, tùy chỉnh hiển thị cột danh sách

### Ngoài phạm vi dự án

- Module sửa chữa tài sản (được đánh dấu ưu tiên thấp - mức 4)
- Phần mềm quản lý tài liệu số
- Tích hợp với các hệ thống bên ngoài khác ngoài OMS và EMS

### Mục tiêu dự án

- Cải thiện khả năng trực quan hóa và phân tích dữ liệu tài sản
- Tự động hóa tối đa các quy trình quản lý kho và cấp phát tài sản
- Giảm thiểu thời gian xử lý và sai sót trong quy trình nghiệp vụ
- Tăng cường khả năng theo dõi và kiểm soát tài sản trong toàn tổ chức
- Đảm bảo tính nhất quán dữ liệu thông qua tích hợp hệ thống

## 3. Stakeholders

Dự án FAM Wave 4 có sự tham gia của nhiều bên liên quan với vai trò và trách nhiệm khác nhau:

### Nhóm quản lý tài sản
- **Asset Manager (AM)**: Phê duyệt các yêu cầu cấp tài sản và điều chuyển cấp cao
- **Asset Management Personnel (AMP)**: Thực hiện các nghiệp vụ quản lý tài sản hàng ngày, tạo và xử lý các yêu cầu

### Nhóm quản lý kho
- **Warehouse Manager (WM)**: Phê duyệt các yêu cầu xuất nhập kho, quản lý hoạt động kho tổng thể
- **Warehouse Keeper (WK)**: Thực hiện các hoạt động xuất nhập kho thực tế, xác nhận giao nhận hàng hóa

### Nhóm nghiệp vụ
- **Business Unit Manager (BU Mgr)**: Phê duyệt các yêu cầu từ đơn vị, quản lý tài sản của phòng ban
- **Business Unit User (BU User)**: Người dùng cuối, tạo yêu cầu và nhận tài sản

### Hệ thống tích hợp
- **OMS (Organization Management System)**: Cung cấp dữ liệu tổ chức, thông tin kho và nhân sự
- **EMS**: Đồng bộ thông tin PO và thời gian phê duyệt
- **ITSM**: Hệ thống quản lý sự cố IT (cho module sửa chữa tương lai)

## 4. Business Requirements

### 4.1. Asset Dashboard Module

Module dashboard tài sản được thiết kế để cung cấp giao diện tổng quan và trực quan hóa dữ liệu tài sản, hỗ trợ việc đưa ra quyết định nhanh chóng và hiệu quả. Dashboard hiển thị dữ liệu tài sản theo nhiều góc độ khác nhau bao gồm phòng ban, trạng thái tài sản, biến động theo thời gian và tỷ lệ sử dụng.

Hệ thống cung cấp bốn thông số tổng quan chính: tổng số lượng tài sản, tổng giá trị tài sản, tỷ lệ tài sản còn bảo hành và tỷ lệ sử dụng. Tất cả các tính toán sẽ loại trừ tài sản đã thanh lý và vô hiệu hóa để đảm bảo tính chính xác của báo cáo.

Dashboard được trang bị năm loại bộ lọc chính: theo vùng, đơn vị sử dụng (đồng bộ từ OMS), phân nhóm tài sản (CAT 1 và Group name), trạng thái tài sản (không bao gồm đã thanh lý và vô hiệu hóa), và thời gian. Hệ thống hỗ trợ xuất dữ liệu dashboard ra file Excel để phục vụ báo cáo và phân tích chi tiết.

**Yêu cầu chi tiết:**

| STT | Nội dung | Giá trị | Loại biểu đồ | Ghi chú |
|-----|----------|---------|--------------|---------|
| 1 | Tổng số tài sản | Count số lượng (All tài sản - Đã thanh lý - Vô hiệu hóa) | - | - |
| 2 | Tổng giá trị | Sum nguyên giá (All tài sản - Đã thanh lý - Vô hiệu hóa) | - | - |
| 3 | Tình trạng bảo hành | Tỷ lệ phần trăm theo số lượng tài sản còn hạn bảo hành/(All tài sản - Vô hiệu hóa - Đã thanh lý) | - | - |
| 4 | Tỷ lệ sử dụng | Tỷ lệ phần trăm theo số lượng tài sản có trạng thái đang sử dụng/(All tài sản - Vô hiệu hóa - Đã thanh lý) | - | - |

**Biểu đồ tương tác:**

| STT | Tên biểu đồ | Dữ liệu | Loại biểu đồ | Ghi chú |
|-----|-------------|---------|--------------|---------|
| 1 | Phân bổ tài sản - Cơ cấu nhóm tài sản theo trạng thái | Nguyên giá | Sunburst (Vòng trong: Nhóm IT/ADM/CMD, Vòng ngoài: Trạng thái) | Khi Hover hiển thị số lượng và giá trị |
| 2 | Phân bổ tài sản - Cơ cấu theo Vùng và Đơn vị sử dụng | Nguyên giá | Stacked Column | - |
| 3 | Giá trị tài sản theo Group Name | Nguyên giá | Column | - |
| 4 | Biến động tài sản theo thời gian (Tháng/Năm) | Nguyên giá | Line | - |
| 5 | Tài sản theo thời gian sử dụng | Số lượng | Scatter | - |

### 4.2. Warehouse Management Module

Module quản lý kho là một thành phần core của hệ thống, được thiết kế để xử lý toàn bộ quy trình xuất nhập kho tài sản một cách tự động và hiệu quả. Module này bao gồm các quy trình chính: [tạo yêu cầu nhập kho](#421-create-warehouse-intake-request), [phê duyệt yêu cầu nhập kho](#422-approve-warehouse-intake-request), [xác nhận nhập kho](#423-warehouse-intake-confirmation), và các quy trình hỗ trợ khác.

Điểm nổi bật của module là khả năng tự động tạo các yêu cầu liên quan, giúp giảm thiểu công việc thủ công và đảm bảo tính liên tục của quy trình. Hệ thống tự động tạo yêu cầu nhập kho sau khi xác nhận điều chuyển về kho, tự động tạo yêu cầu xuất kho sau khi duyệt [cấp tài sản](#43-asset-provisioning-module) hoặc thanh lý tài sản.

Tất cả các quy trình đều có cơ chế phê duyệt đa cấp với khả năng từ chối và quay lại bước trước, đồng thời có các tùy chọn hủy bỏ yêu cầu khi cần thiết. Hệ thống cũng tự động cập nhật trạng thái và tạo các biên bản, bút toán kế toán liên quan.

#### 4.2.1. Create Warehouse Intake Request

##### 4.2.1.1. Thông số kỹ thuật giao diện người dùng

![Giao diện tạo yêu cầu nhập kho](images/5_1_1a_B5_image1.png)

Quy trình tạo yêu cầu nhập kho được khởi tạo tự động khi có yêu cầu chuyển kho được xác nhận. Hệ thống sẽ kế thừa toàn bộ thông tin từ yêu cầu chuyển kho bao gồm thông tin tài sản, chi tiết kho đích và các tệp đính kèm.

Giao diện được thiết kế với cấu trúc rõ ràng bao gồm phần header hiển thị số yêu cầu và trạng thái, phần thông tin chung cho phép nhập tiêu đề và ghi chú, phần chi tiết tài sản hiển thị danh sách tài sản được chuyển với thông tin đầy đủ, và phần tệp đính kèm cho phép upload thêm tài liệu hỗ trợ.

Quy trình xử lý bao gồm các bước tìm kiếm yêu cầu điều chuyển, xem chi tiết thông tin, và đưa ra quyết định. AMP có thể từ chối yêu cầu (với việc nhập lý do bắt buộc), xác nhận để tạo yêu cầu nhập kho tự động, hoặc yêu cầu bổ sung thông tin. Hệ thống tự động cập nhật trạng thái, tasklist và gửi thông báo email cho các bên liên quan sau mỗi hành động.

##### 4.2.1.2. Thông số kỹ thuật chi tiết

Dưới đây là đặc tả chi tiết các trường dữ liệu và quy tắc validation cho chức năng tạo yêu cầu nhập kho:

**Thông tin chung yêu cầu nhập kho:**

| Trường | Operator | Action | Tên trường | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|--------|----------|--------|------------|-----|------------|----------|------------|--------|---------------|-----------|
| Số yêu cầu | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| Ngày tạo | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | System | Display | Tiêu đề | M | Text | N | 150 | | | =Tiêu đề RQ điều chuyển |

**Danh sách tài sản nhập kho (hiển thị mặc định):**

| Trường | Operator | Action | Tên trường | M/O | Editable | Data rule |
|--------|----------|--------|------------|-----|----------|-----------|
| Mã tài sản | System | Display | Mã tài sản | M | N | Hiển thị mặc định |
| Tên Tài sản | System | Display | Tên Tài sản | M | N | Hiển thị mặc định |
| Mô tả TS | System | Display | Mô tả TS | M | N | Hiển thị mặc định |
| Trạng thái TS | System | Display | Trạng thái TS | M | N | Hiển thị mặc định |
| Phân nhóm TS | System | Display | Phân nhóm TS (group name) | M | N | Hiển thị mặc định |
| Nhóm TS | System | Display | Nhóm TS (CAT1) | M | N | Hiển thị mặc định |
| Số PO | System | Display | Số PO | M | N | Hiển thị mặc định |
| Tên người sử dụng | System | Display | Tên người sử dụng | M | N | Hiển thị mặc định |
| Tên đơn vị | System | Display | Tên đơn vị | M | N | Hiển thị mặc định |
| Đơn vị sử dụng cha | System | Display | Đơn vị sử dụng cha | M | N | Hiển thị mặc định |

**Thông tin kho nhập:**

| Trường | Operator | Action | Tên trường | M/O | Field type | Max length | Data source | Data rule |
|--------|----------|--------|------------|-----|------------|------------|-------------|-----------|
| Tên kho | System | Display | Tên kho | M | List | 50 | | = Kho trong RQ điều chuyển |
| Địa chỉ kho | System | Display | Địa chỉ kho | M | Text | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| Quản lý kho | System | Display | Quản lý kho | M | Text | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

Sau khi tạo yêu cầu nhập kho, hệ thống tự động cập nhật trạng thái RQ điều chuyển thành "Đã xác nhận", RQ nhập kho thành "Chờ phê duyệt", cập nhật tasklist AMP thành "Đã xử lý" và WM thành "Cần xử lý", đồng thời gửi email thông báo cho Warehouse Manager để xử lý tiếp.

#### 4.2.2. Approve Warehouse Intake Request

##### 4.2.2.1. Thông số kỹ thuật giao diện người dùng

![Giao diện phê duyệt yêu cầu nhập kho](images/5_1_2a_B6_image2.png)

Giao diện phê duyệt yêu cầu nhập kho được thiết kế để Warehouse Manager có thể xem xét và đưa ra quyết định phê duyệt các yêu cầu nhập kho tài sản. Màn hình bao gồm phần tìm kiếm yêu cầu với các tiêu chí lọc đa dạng, phần hiển thị kết quả tìm kiếm và phần chi tiết yêu cầu với thông tin đầy đủ về tài sản.

Giao diện hiển thị thông tin tài sản toàn diện với hơn 20 trường thông tin bao gồm thông tin cơ bản, thông tin người sử dụng, thông tin bảo hành và các thông tin khác. Hệ thống hỗ trợ tùy biến hiển thị các trường thông tin theo nhu cầu của người dùng.

Warehouse Manager có hai lựa chọn chính: từ chối yêu cầu (yêu cầu nhập lý do bắt buộc) hoặc phê duyệt. Khi từ chối, hệ thống sẽ unlock tài sản và cập nhật trạng thái về "Từ chối". Khi phê duyệt, hệ thống chuyển trạng thái thành "Chờ nhập kho" và tạo task cho Warehouse Keeper.

##### 4.2.2.2. Thông số kỹ thuật chi tiết

**Bảng tìm kiếm yêu cầu:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Chỉnh sửa | Độ dài |
|--------|----------|---------|------------|-----|------|-----------|---------|
| Tìm kiếm yêu cầu | User | Input | Số yêu cầu | O | Text | Y | 20 |
| | User | Input | Ngày tạo | O | Date | Y | 20 |
| | User | Input | Tiêu đề | O | Text | Y | 150 |
| | User | Select | Người tạo | O | List | Y | 20 |
| | User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| | User | Select | Người xử lý | O | List | Y | 20 |
| | User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Bảng hiển thị danh sách yêu cầu:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Chỉnh sửa | Độ dài |
|--------|----------|---------|------------|-----|------|-----------|---------|
| Kết quả | System | Display | Số yêu cầu | M | Text | N | 20 |
| | System | Display | Ngày tạo | M | Date | N | 20 |
| | System | Display | Tiêu đề | M | Text | N | 150 |
| | System | Display | Người tạo | M | Text | N | 20 |
| | System | Display | Trạng thái yêu cầu | M | Text | N | 20 |
| | System | Display | Người xử lý | O | Text | N | 20 |
| | System | Display | Ngày xác nhận | O | Date | N | 20 |

Quy trình phê duyệt được thiết kế với workflow tự động: khi Warehouse Manager từ chối yêu cầu, hệ thống tự động unlock tài sản để có thể sử dụng cho các yêu cầu khác, cập nhật tasklist cho AMP và BU user, và gửi email thông báo. Khi phê duyệt, hệ thống cập nhật trạng thái yêu cầu, tạo task cho WK và gửi thông báo tương ứng.

#### 4.2.3. Warehouse Intake Confirmation

##### 4.2.3.1. Thông số kỹ thuật giao diện người dùng

![Giao diện xác nhận nhập kho](images/5_1_3a_B5_image3.png)

Chức năng xác nhận nhập kho là bước cuối cùng trong quy trình nhập kho, được thực hiện bởi Warehouse Keeper. Giao diện cho phép WK tìm kiếm các yêu cầu nhập kho đã được phê duyệt, xem chi tiết thông tin tài sản và thực hiện xác nhận nhập kho thực tế.

Màn hình hiển thị đầy đủ thông tin về yêu cầu bao gồm thông tin chung, danh sách tài sản với hơn 25 trường thông tin chi tiết, thông tin kho nhập, đầu mối giao hàng và lịch sử xử lý. WK có thể từ chối (yêu cầu nhập lý do) hoặc xác nhận nhập kho.

Hệ thống có workflow tự động để cập nhật trạng thái yêu cầu, unlock tài sản, cập nhật thông tin tài sản (đặc biệt là trường "Ngày bắt đầu sử dụng" nếu đang là N/A) và gửi thông báo cho các bên liên quan.

##### 4.2.3.2. Thông số kỹ thuật chi tiết

**Bảng thông tin tìm kiếm yêu cầu:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Bảng danh sách tài sản nhập kho (các trường chính):**

| Operator | Action | Field name VN | M/O | Field type | Editable | Data rule |
|----------|--------|---------------|-----|------------|----------|-----------|
| System | Display | Mã tài sản | M | - | N | Hiển thị mặc định |
| System | Display | Tên Tài sản | M | - | N | Hiển thị mặc định |
| System | Display | Mô tả TS | M | - | N | Hiển thị mặc định |
| System | Display | Trạng thái TS | M | - | N | Hiển thị mặc định |
| System | Display | Phân nhóm TS (group name) | M | - | N | Hiển thị mặc định |
| System | Display | Nhóm TS (CAT1) | M | - | N | Hiển thị mặc định |
| System | Display | Số PO | M | - | N | Hiển thị mặc định |
| System | Display | Tên nhà cung cấp | O | - | N | Ẩn hiện tùy biến |
| System | Display | Nguyên giá TS (VAT incl) | M | - | N | Ẩn hiện tùy biến |

Khi WK xác nhận nhập kho, hệ thống tự động cập nhật trường "Ngày bắt đầu sử dụng" thành ngày xác nhận nếu trường này đang có giá trị N/A, unlock tài sản để có thể sử dụng cho các yêu cầu khác, và hoàn tất quy trình nhập kho.

#### 4.2.4. Manual Warehouse Intake Process

Module nhập kho thủ công cung cấp khả năng tạo yêu cầu nhập kho độc lập, không thông qua quy trình tự động từ [điều chuyển về kho](#421-create-warehouse-intake-request). Quy trình này hữu ích cho các trường hợp nhập kho đặc biệt hoặc tài sản mới không thông qua quy trình điều chuyển.

##### 4.2.4.1. Thông số kỹ thuật giao diện người dùng

![Giao diện tạo yêu cầu nhập kho thủ công](images/5_2_1a_B5_image4.png)

Giao diện tạo yêu cầu nhập kho thủ công cho phép người dùng tạo mới yêu cầu nhập kho với đầy đủ thông tin. Màn hình bao gồm các phần: thông tin chung, chức năng tìm kiếm tài sản với nhiều tiêu chí lọc, danh sách tài sản được chọn và thông tin kho nhập.

Hệ thống hỗ trợ tìm kiếm tài sản theo các tiêu chí như mã tài sản, tên, phân loại, nhóm, PO number, trạng thái, nhà cung cấp và vị trí. Người dùng có thể chọn nhiều tài sản cùng lúc và hệ thống sẽ cảnh báo nếu tài sản đang bị lock trong request khác.

##### 4.2.4.2. Thông số kỹ thuật chi tiết

**Bảng thông tin chung yêu cầu:**

| STT | Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data rule |
|-----|-------------|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-----------|
| 1 | Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | NK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 không dùng lại |
| 2 | Thông tin chung | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | |
| 3 | Thông tin chung | User | Input | Tiêu đề | O | Text | Y | 150 | | | |
| 4 | Thông tin chung | User | Select | Thêm tài sản | M | Button | N | | | | |

**Bảng thông tin kho và giao hàng:**

| STT | Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule |
|-----|-------------|----------|--------|---------------|-----|------------|----------|------------|-------------|-----------|
| 1 | Thông tin kho nhập | System/User | Display/Search/Select | Tên kho | M | List | N | 50 | | |
| 2 | Thông tin kho nhập | System | Display | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho |
| 3 | Thông tin kho nhập | System | Display | Quản lý kho | M | Text | N | 50 | OMS | Tự động nhận diện, hiển thị theo Tên kho (Tên \| Phòng ban \| Email) |

Sau khi tạo yêu cầu, hệ thống tự động lock các tài sản được chọn, cập nhật trạng thái yêu cầu thành "Chờ phê duyệt", cập nhật tasklist và gửi email thông báo cho Warehouse Manager để tiến hành [phê duyệt yêu cầu](#422-approve-warehouse-intake-request).

Quy trình phê duyệt và xác nhận nhập kho thủ công tương tự như quy trình tự động, đều thông qua các bước [phê duyệt](#422-approve-warehouse-intake-request) và [xác nhận nhập kho](#423-warehouse-intake-confirmation).

#### 4.2.5. Cancel Warehouse Intake Request

##### 4.2.5.1. Thông số kỹ thuật giao diện người dùng

![Giao diện hủy yêu cầu nhập kho](images/5_3_1a_B5_image7.png)

Chức năng hủy yêu cầu nhập kho cho phép AMP hủy bỏ các yêu cầu nhập kho đã được tạo nhưng chưa hoàn thành. Điều kiện áp dụng là yêu cầu nhập kho phải có trạng thái khác "Đã nhập kho".

Giao diện cho phép tìm kiếm yêu cầu theo nhiều tiêu chí, xem chi tiết thông tin và thực hiện hủy yêu cầu với việc nhập lý do bắt buộc. Hệ thống sẽ tự động unlock tài sản để có thể sử dụng cho các yêu cầu khác.

##### 4.2.5.2. Thông số kỹ thuật chi tiết

**Form tìm kiếm yêu cầu:**

| Trường | Operator | Action | Tên trường | M/O | Kiểu | Editable | Max length |
|---------|-----------|---------|------------|-----|------|----------|------------|
| User | Input | Số yêu cầu | O | Text | Y | 20 |
| User | Input | Ngày tạo | O | Date | Y | 20 |
| User | Input | Tiêu đề | O | Text | Y | 150 |
| User | Select | Người tạo | O | List | Y | 20 |
| User | Select | Trạng thái yêu cầu | O | List | Y | 20 |
| User | Select | Người xử lý | O | List | Y | 20 |
| User | Input | Ngày xác nhận | O | Date | Y | 20 |

**Lý do hủy:**

| Trường | Operator | Action | M/O | Kiểu | Editable | Max length |
|---------|-----------|---------|-----|------|----------|------------|
| User | Nhập | Lý do hủy | M | Text | Y | 150 |

Khi hủy yêu cầu nhập kho, hệ thống tự động cập nhật trạng thái yêu cầu thành "Đã hủy", unlock tài sản, cập nhật tasklist cho WM và AMP/BU user, và gửi email thông báo cho các bên liên quan. Đối với yêu cầu nhập kho được tạo từ [điều chuyển về kho](#421-create-warehouse-intake-request), hệ thống cũng cập nhật ngược trạng thái yêu cầu điều chuyển liên quan.

### 4.3. Asset Provisioning Module

Module cấp tài sản xử lý quy trình phân phối tài sản từ kho đến người dùng cuối thông qua workflow phê duyệt được thiết kế chặt chẽ. Module này tích hợp chặt chẽ với [module quản lý kho](#42-warehouse-management-module) để tự động tạo các yêu cầu xuất kho sau khi phê duyệt cấp tài sản.

#### 4.3.1. Thông số kỹ thuật giao diện người dùng

![Giao diện phê duyệt yêu cầu cấp tài sản](images/5_4_0a_A4_image8.png)

Giao diện phê duyệt yêu cầu cấp tài sản được thiết kế cho Asset Manager để xem xét và phê duyệt các yêu cầu cấp phát tài sản. Màn hình hiển thị thông tin chi tiết về yêu cầu, danh sách tài sản cần cấp và thông tin đơn vị nhận.

#### 4.3.2. Thông số kỹ thuật chi tiết

**Bảng tìm kiếm yêu cầu:**

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

**Bảng thông tin tài sản cấp:**

| STT | Operator | Action | Field name VN | M/O | Display Rule |
|-----|----------|--------|---------------|-----|--------------|
| 1 | System | Display | Mã tài sản | M | Hiển thị mặc định |
| 2 | System | Display | Tên Tài sản | M | Hiển thị mặc định |
| 3 | System | Display | Mô tả TS | M | Hiển thị mặc định |
| 4 | System | Display | Trạng thái TS | M | Hiển thị mặc định |
| 5 | System | Display | Phân nhóm TS (group name) | M | Hiển thị mặc định |
| 6 | System | Display | Nhóm TS (CAT1) | M | Hiển thị mặc định |
| 7 | System | Display | Số PO | M | Hiển thị mặc định |
| 8 | System | Display | Tên nhà cung cấp | O | Ẩn hiện tùy biến |
| 9 | System | Display | Nguyên giá TS (VAT incl) | M | Ẩn hiện tùy biến |
| 10 | System | Display | Tên người sử dụng | M | Hiển thị mặc định |
| 11 | System | Display | Tên đơn vị | M | Hiển thị mặc định |
| 12 | System | Display | Đơn vị sử dụng cha | M | Hiển thị mặc định |

Khi Asset Manager phê duyệt yêu cầu cấp tài sản, hệ thống tự động tạo [yêu cầu xuất kho](#45-warehouse-export-module) tương ứng và kích hoạt quy trình xuất kho. Nếu từ chối, hệ thống sẽ unlock tài sản để có thể sử dụng cho các yêu cầu khác và thông báo cho AMP.

### 4.4. Inter-Warehouse Transfer Module

Module điều chuyển tài sản giữa các kho cho phép di chuyển tài sản từ kho này sang kho khác thông qua quy trình phê duyệt có kiểm soát. Module này là một phần quan trọng trong việc tối ưu hóa phân bổ tài sản và quản lý inventory theo địa lý.

#### 4.4.1. Create Inter-Warehouse Transfer Request

##### 4.4.1.1. Thông số kỹ thuật giao diện người dùng

![Giao diện tạo yêu cầu điều chuyển kho](images/5_6_1a_B6_image14.png)

Chức năng tạo yêu cầu điều chuyển kho cho phép người dùng tạo các yêu cầu di chuyển tài sản từ kho này sang kho khác. Giao diện bao gồm các section: thông tin chung, tìm kiếm tài sản, danh sách tài sản được chọn và thông tin kho đi/kho nhận.

##### 4.4.1.2. Thông số kỹ thuật chi tiết

**Bảng đặc tả trường thông tin chung:**

| Tab/Section | Operator | Action | Field name VN | M/O | Field type | Editable | Max length | Format | Default value | Data source | Data rule |
|-------------|----------|--------|---------------|-----|------------|----------|------------|--------|---------------|-------------|-----------|
| Thông tin chung | System | Display | Số yêu cầu | M | Text | N | 50 | CK.YY.xxxx | | | YY = Year, xxxx = số chạy từ 1-9999 |
| | System | Display | Ngày tạo | M | Date | N | 50 | MM.DD.YYYY | Today | | |
| | User | Input | Tiêu đề | O | Text | Y | 150 | | | | |
| | User | Select | Thêm tài sản | M | Button | N | | | | | |

**Bảng đặc tả thông tin kho:**

| Tab/Section | Field name VN | M/O | Field type | Editable | Max length | Data source | Data rule | Operator | Action |
|-------------|---------------|-----|------------|----------|------------|-------------|-----------|----------|--------|
| Thông tin kho đi | Tên kho | M | List | N | 50 | | | System/User | Display/Search/Select |
| | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện theo Tên kho | System | Display |
| | Quản lý kho | M | Text | N | 50 | OMS | Hiển thị Tên\|Phòng ban\|Email | System | Display |
| Thông tin kho nhập | Tên kho | M | List | N | 50 | | | User | Select |
| | Địa chỉ kho | M | Text | Y | 50 | OMS | Tự động nhận diện theo Tên kho | System | Display |
| | Quản lý kho | M | Text | N | 50 | OMS | Hiển thị Tên\|Phòng ban\|Email | System | Display |

Sau khi tạo yêu cầu, hệ thống tự động khóa tài sản, cập nhật trạng thái "Chờ phê duyệt", tìm và gán người duyệt (AM/Warehouse Manager), cập nhật tasklist và gửi email thông báo đến các bên liên quan.

#### 4.4.2. Approve Inter-Warehouse Transfer Request

##### 4.4.2.1. Thông số kỹ thuật giao diện người dùng

Giao diện phê duyệt yêu cầu điều chuyển tài sản giữa các kho được thiết kế cho Approver để xem xét và đưa ra quyết định phê duyệt. Màn hình bao gồm chức năng tìm kiếm yêu cầu, hiển thị thông tin chi tiết tài sản và form quyết định phê duyệt.

##### 4.4.2.2. Thông số kỹ thuật chi tiết

**Bảng tìm kiếm yêu cầu:**

| Field name | M/O | Field type | Editable | Max length | Format |
|------------|-----|------------|----------|------------|--------|
| Số yêu cầu | O | Text | Y | 20 | |
| Ngày tạo | O | Date | Y | 20 | |
| Tiêu đề | O | Text | Y | 150 | |
| Người tạo | O | List | Y | 20 | |
| Trạng thái yêu cầu | O | List | Y | 20 | |
| Người xử lý | O | List | Y | 20 | |
| Ngày xác nhận | O | Date | Y | 20 | |

**Bảng thông tin chung yêu cầu:**

| Field name | Operator | Action | M/O | Field type | Max length | Format | Default | Data rule |
|------------|----------|--------|-----|------------|------------|--------|---------|-----------|
| Số yêu cầu | System | Display | M | Text | 50 | CK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 |
| Ngày tạo | System | Display | M | Date | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | User | Input | O | Text | 150 | | | |

Khi Approver phê duyệt yêu cầu, hệ thống tự động tạo biên bản điều chuyển, cập nhật thông tin kho của tài sản, thông báo cho các bên liên quan (AMP, WK kho đi, WK kho đến) và cập nhật tasklist tương ứng. Nếu từ chối, hệ thống unlock tài sản và thông báo cho người tạo yêu cầu.

### 4.5. Warehouse Export Module

Module xuất kho xử lý các yêu cầu xuất tài sản từ kho, thường được kích hoạt tự động sau khi [yêu cầu cấp tài sản](#43-asset-provisioning-module) được phê duyệt. Module này đảm bảo quy trình xuất kho được kiểm soát chặt chẽ với workflow phê duyệt đa cấp.

#### 4.5.1. Thông số kỹ thuật giao diện người dùng

![Giao diện tạo yêu cầu xuất kho](images/5_4_1a_B5_image9.png)

Giao diện tạo yêu cầu xuất kho thường được kích hoạt tự động bởi hệ thống sau khi yêu cầu cấp tài sản được phê duyệt. Thông tin yêu cầu được kế thừa từ phiếu cấp tài sản gốc bao gồm danh sách tài sản, thông tin kho xuất và đầu mối nhận hàng.

#### 4.5.2. Thông số kỹ thuật chi tiết

**Thông tin chung:**

| Trường | Operator | Action | Loại | M/O | Editable | Max Length | Format | Default | Quy tắc |
|--------|----------|--------|------|-----|----------|------------|---------|---------|---------|
| Số yêu cầu | System | Display | Text | M | N | 50 | XK.YY.xxxx | | YY = Year, xxxx = số chạy từ 1-9999 |
| Ngày tạo | System | Display | Date | M | N | 50 | MM.DD.YYYY | Today | |
| Tiêu đề | System | Input | Text | O | Y | 150 | | | =Tiêu đề RQ Cấp/Thanh lý |

**Thông tin đầu mối nhận hàng:**

| Operator | Action | Field name VN | M/O | Field type | Editable | Max length |
|----------|--------|---------------|-----|------------|----------|------------|
| User | Input | Đầu mối | M | Text | Y | 50 |
| User | Input | Số điện thoại | M | Number | Y | 52 |
| User | Input | Thời gian bàn giao | O | Date | Y | 50 |

Quy trình xuất kho bao gồm các bước: tiếp nhận yêu cầu từ Warehouse Keeper, [phê duyệt từ Warehouse Manager](#45-warehouse-export-module), và xác nhận nhận hàng từ BU User. Đối với yêu cầu xuất kho từ thanh lý, hệ thống sẽ ẩn nút "Từ chối" để đảm bảo quy trình thanh lý được thực hiện đầy đủ.

## 5. System Integration Requirements

Hệ thống FAM Wave 4 tích hợp với nhiều hệ thống bên ngoài để đảm bảo đồng bộ dữ liệu và tối ưu hóa quy trình nghiệp vụ:

### 5.1. OMS Integration

**Organization Management System (OMS)** cung cấp dữ liệu tổ chức quan trọng cho tất cả các module:

- Đồng bộ orgchart tự động khi có thay đổi cơ cấu tổ chức
- Cung cấp thông tin kho bao gồm tên kho, địa chỉ và quản lý kho cho [module quản lý kho](#42-warehouse-management-module)
- Cung cấp thông tin nhân sự và đơn vị sử dụng cho [dashboard tài sản](#41-asset-dashboard-module)
- Hỗ trợ dữ liệu cho các quy trình [điều chuyển kho](#44-inter-warehouse-transfer-module)

### 5.2. EMS Integration

**Enterprise Management System (EMS)** đồng bộ thông tin liên quan đến Purchase Order:

- Đồng bộ tiêu đề PO từ EMS sang FAM
- Cập nhật thông tin thời gian từ EMS dựa trên thời gian PO được phê duyệt
- Tự động cập nhật trường "Thông tin thời gian đưa vào sử dụng" và "Thời gian bắt đầu bảo hành" bằng thời gian PO được phê duyệt

### 5.3. ITSM Integration

**IT Service Management (ITSM)** sẽ được tích hợp trong tương lai cho module sửa chữa tài sản:

- Tạo yêu cầu sửa chữa tài sản trên FAM và gửi link sang ITSM
- Đồng bộ trạng thái xử lý từ ITSM về FAM
- Tích hợp với Cổng hỗ trợ chi nhánh trên intranet

## 6. Workflow & Status Management

Hệ thống FAM Wave 4 được thiết kế với workflow phức tạp và quản lý trạng thái chặt chẽ để đảm bảo tính nhất quán và kiểm soát quy trình nghiệp vụ.

### 6.1. Asset Provisioning Workflow

Quy trình cấp tài sản có hai luồng chính:

**Cấp tài sản không qua kho:**

| Sub-process | PIC | Action | Rq Status | Asset Status | Note |
|-------------|-----|--------|-----------|--------------|------|
| 1 Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - |
| - | AMP | Gửi | Chờ xác nhận | - | - |
| 2. Xác nhận | BU User | Từ chối | Từ chối | - | - |
| - | BU User | Xác nhận | Đã xác nhận | Đang sử dụng | Đã xác nhận >>> Đã nhận tài sản |
| - | BU User | Bổ sung thông tin | Bổ sung thông tin | - | - |
| 3. Bổ sung TT | AMP | Bổ sung thông tin | Chờ xác nhận | - | - |

**Cấp tài sản từ kho:**

| Sub-process | PIC | Action | Rq Status | Warehouse Status | Asset Status |
|-------------|-----|--------|-----------|------------------|--------------|
| 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - |
| - | AMP | Gửi | Chờ xác nhận | - | - |
| 2. Phê duyệt | AM | Từ chối | Từ chối | - | - |
| - | AM | Duyệt | Đã xác nhận | - | - |
| 3. Tạo yêu cầu | System | - | Đã xác nhận | Chờ xuất kho | - |
| 4. Xuất kho | WK | Từ chối | Từ chối | Từ chối | - |
| - | WK | Đồng ý | Đã xác nhận | Chờ phê duyệt | - |
| 5. Phê duyệt | Warehouse Mgr. | Từ chối | Từ chối | Từ chối | - |
| - | Warehouse Mgr. | Duyệt | Đã xác nhận | Chờ xác nhận | - |
| 6. Nhận hàng | BU User | Từ chối | Từ chối | Từ chối | - |
| - | BU User | Xác nhận | Đã xác nhận | Đã nhận tài sản | Đang sử dụng |

### 6.2. Tasklist Management

Hệ thống quản lý tasklist đảm bảo phân công công việc rõ ràng và theo dõi tiến độ xử lý:

| Sub-process | Hành động | Chi tiết | Vai trò | Điều chuyển - Cần xử lý | Điều chuyển - Đã xử lý | Kho - Cần xử lý | Kho - Đã xử lý | Ghi chú |
|-------------|-----------|----------|---------|-------------------------|------------------------|-----------------|----------------|---------|
| 2.3.1a Tạo yêu cầu điều chuyển | Lưu | | Initiator | x | | | | |
| | Gửi | | | | x | | | |
| 2.3.3a Phê duyệt yêu cầu điều chuyển | Từ chối | | Initiator | x | | | | |
| | | | BUH | | x | | | |
| | Duyệt | | Initiator | | x | | | |
| | | | BUH | | x | | | |
| | | | AMP | x | | | | |
| | Bổ sung thông tin | | Initiator | x | | | | |
| | | | BUH | | x | | | |

Hệ thống tự động cập nhật tasklist sau mỗi hành động để đảm bảo các bên liên quan được thông báo kịp thời và thực hiện công việc của mình.

## 7. Assumptions & Constraints

### Giả định

- Hệ thống OMS và EMS hoạt động ổn định và cung cấp API đáng tin cậy
- Người dùng đã được đào tạo về quy trình nghiệp vụ hiện tại và có thể thích ứng với các thay đổi
- Hạ tầng IT hiện có đủ khả năng hỗ trợ các tính năng mới
- Dữ liệu master về tài sản, kho và tổ chức đã được chuẩn hóa

### Ràng buộc

- Phải tuân thủ các quy định về kiểm toán và tuân thủ pháp luật hiện hành
- Không được gián đoạn hoạt động nghiệp vụ hiện tại trong quá trình triển khai
- Phải đảm bảo tính bảo mật thông tin theo tiêu chuẩn của tổ chức
- Ngân sách và thời gian triển khai theo kế hoạch đã được phê duyệt
- Module sửa chữa tài sản phụ thuộc vào việc làm rõ quy trình với bộ phận ITSM

## 8. Dependencies

### Phụ thuộc nội bộ

- [Dashboard tài sản](#41-asset-dashboard-module) phụ thuộc vào data từ tất cả các module khác
- [Module quản lý kho](#42-warehouse-management-module) là nền tảng cho [module cấp tài sản](#43-asset-provisioning-module)
- [Module điều chuyển kho](#44-inter-warehouse-transfer-module) phụ thuộc vào [quy trình nhập kho](#421-create-warehouse-intake-request)

### Phụ thuộc hệ thống bên ngoài

- OMS: Cung cấp dữ liệu orgchart, thông tin kho và nhân sự
- EMS: Đồng bộ thông tin PO và thời gian
- ITSM: Tích hợp module sửa chữa tài sản (tương lai)
- Email system: Gửi thông báo tự động

### Phụ thuộc dữ liệu

- Dữ liệu tài sản hiện có phải được migrate và làm sạch
- Master data về kho, đơn vị tổ chức phải được đồng bộ từ OMS
- Quyền người dùng và vai trò phải được cấu hình đúng

## 9. Acceptance Criteria

### Tiêu chí chấp nhận chung

- Tất cả các chức năng được mô tả trong [Business Requirements](#4-business-requirements) hoạt động đúng theo đặc tả
- Hiệu năng hệ thống không giảm so với phiên bản hiện tại
- Giao diện người dùng thân thiện và tuân thủ chuẩn UX của tổ chức
- Hệ thống tích hợp thành công với OMS và EMS

### Tiêu chí chấp nhận cụ thể

**[Dashboard tài sản](#41-asset-dashboard-module):**
- Hiển thị chính xác 4 KPI chính với dữ liệu real-time
- 5 loại biểu đồ tương tác hoạt động mượt mà với hover và click events
- Bộ lọc hoạt động chính xác và tốc độ phản hồi dưới 3 giây
- Xuất Excel thành công với đầy đủ dữ liệu đã lọc

**[Module quản lý kho](#42-warehouse-management-module):**
- Tự động tạo yêu cầu nhập kho sau khi xác nhận điều chuyển về kho
- Workflow phê duyệt 3 cấp hoạt động chính xác
- Lock/unlock tài sản hoạt động đúng logic nghiệp vụ
- Email notification gửi đúng người và đúng thời điểm

**[Module cấp tài sản](#43-asset-provisioning-module):**
- Tự động tạo yêu cầu xuất kho sau khi AM phê duyệt
- Quản lý trạng thái chính xác qua tất cả các bước
- Đồng bộ thông tin với EMS về thời gian đưa vào sử dụng

**[Module điều chuyển kho](#44-inter-warehouse-transfer-module):**
- Tạo yêu cầu điều chuyển với validation đầy đủ
- Phê duyệt và tự động tạo biên bản điều chuyển
- Cập nhật thông tin kho của tài sản sau khi hoàn thành

**Tích hợp hệ thống:**
- Đồng bộ orgchart từ OMS hoạt động real-time
- Đồng bộ thông tin PO từ EMS chính xác và kịp thời
- Tasklist cập nhật chính xác cho tất cả các vai trò

**Hiệu năng và độ tin cậy:**
- Thời gian phản hồi trung bình dưới 2 giây cho các thao tác thường dùng
- Uptime đạt 99.9% trong giờ làm việc
- Xử lý được đồng thời tối thiểu 100 concurrent users
- Backup và recovery hoạt động chính xác theo quy trình

Tài liệu này sẽ được review và cập nhật định kỳ theo tiến độ dự án và phản hồi từ các bên liên quan.

---

*Generated by Claude Sonnet 4.5 from 37 sheet summaries*
*Headings: 45 | Internal Links: 54*

*✅ All internal links validated successfully*
