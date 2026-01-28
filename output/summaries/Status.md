# Phân tích Sheet Status - BRD

## 1. Loại sheet
**quy-trình** - Mô tả các trạng thái và luồng xử lý trong hệ thống quản lý tài sản

## 2. Mức độ chi tiết
**chi-tiết-cao** - Sheet chứa thông tin chi tiết về state transitions, mapping giữa các trạng thái request và asset, cùng với các actors và actions cụ thể trong từng bước xử lý

## 3. Chủ đề/tiêu đề chính
Định nghĩa trạng thái (status) và luồng xử lý cho các quy trình quản lý tài sản bao gồm cấp tài sản, thanh lý tài sản và điều chuyển tài sản

## 4. Tóm tắt thông tin chính

Sheet này mô tả chi tiết workflow và state management cho hệ thống quản lý tài sản với ba quy trình chính. Quy trình **cấp tài sản** được chia thành hai nhánh: cấp tài sản không ở kho (workflow đơn giản với 3 bước: tạo yêu cầu → xác nhận → bổ sung thông tin) và cấp tài sản từ kho (workflow phức tạp hơn với 6 bước bao gồm tạo yêu cầu, phê duyệt, xuất kho và nhận hàng).

Quy trình **thanh lý tài sản** có hai hình thức: bán trực tiếp (8 bước) và bán đấu giá (10 bước), cả hai đều yêu cầu kiểm soát và phê duyệt nhiều lần trước khi thực hiện xuất kho. Quy trình **điều chuyển tài sản** cũng được chia thành điều chuyển về kho (6 bước) và điều chuyển giữa các kho (5 bước), với các bước phê duyệt và xác nhận tương ứng.

Mỗi quy trình đều có hệ thống trạng thái rõ ràng cho cả yêu cầu (Request Status) và tài sản (Asset Status), cho phép theo dõi và kiểm soát toàn bộ lifecycle của tài sản từ khi tạo yêu cầu đến khi hoàn tất xử lý.

## 5. Các bên liên quan/vai trò được đề cập

- **AMP (Asset Management Personnel)**: Nhân viên quản lý tài sản
- **BU User**: Người dùng thuộc đơn vị kinh doanh  
- **BU Head**: Trưởng đơn vị kinh doanh
- **AM (Asset Manager)**: Quản lý tài sản
- **WK (Warehouse Keeper)**: Thủ kho
- **Warehouse Mgr.**: Quản lý kho
- **Checker**: Người kiểm soát
- **Approver**: Người phê duyệt
- **System**: Hệ thống tự động

## 6. Các yêu cầu tìm thấy

- Hệ thống phải hỗ trợ workflow approval với nhiều cấp độ phê duyệt
- Cần có khả năng từ chối, yêu cầu bổ sung thông tin tại các bước xử lý
- Trạng thái tài sản và yêu cầu phải được đồng bộ và cập nhật theo thời gian thực
- Hệ thống phải tự động tạo yêu cầu xuất kho/nhập kho khi cần thiết
- Cần có cơ chế rollback trạng thái tài sản khi hủy yêu cầu
- Phân quyền rõ ràng cho từng vai trò trong các bước xử lý

## 7. Các sheet liên quan

Không có tham chiếu trực tiếp đến các sheet khác, nhưng có thể liên quan đến các sheet định nghĩa user roles, asset categories, và warehouse management.

## 8. Bảng cần giữ nguyên

### Bảng Trạng thái Quy trình Cấp tài sản không ở kho

| Sub-process | PIC | Action | Request Status | Asset Status | Note |
|-------------|-----|--------|----------------|--------------|------|
| 1 Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - |
| 1 Tạo yêu cầu | AMP | Gửi | Chờ xác nhận | - | - |
| 2. Xác nhận | BU User | Từ chối | Từ chối | - | - |
| 2. Xác nhận | BU User | Xác nhận | Đã xác nhận | Đang sử dụng | Đã xác nhận >>> Đã nhận tài sản |
| 2. Xác nhận | BU User | Bổ sung thông tin | Bổ sung thông tin | - | - |
| 3. Bổ sung TT | AMP | Bổ sung thông tin | Chờ xác nhận | - | - |

### Bảng Trạng thái Quy trình Cấp tài sản từ kho

| Sub-process | PIC | Action | Request Status | Asset Status |
|-------------|-----|--------|----------------|--------------|
| 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | - |
| 1. Tạo yêu cầu | AMP | Gửi | Chờ xác nhận | - |
| 2. Phê duyệt | AM | Từ chối | Từ chối | - |
| 2. Phê duyệt | AM | Duyệt | Đã xác nhận | - |
| 3. Tạo yêu cầu | System | - | Đã xác nhận | Chờ xuất kho |
| 4. Xuất kho | WK | Từ chối | Từ chối | Từ chối |
| 4. Xuất kho | WK | Đồng ý | Đã xác nhận | Chờ phê duyệt |
| 5. Phê duyệt | Warehouse Mgr. | Từ chối | Từ chối | Từ chối |
| 5. Phê duyệt | Warehouse Mgr. | Duyệt | Đã xác nhận | Chờ xác nhận |
| 6. Nhận hàng | BU User | Từ chối | Từ chối | Từ chối |
| 6. Nhận hàng | BU User | Xác nhận | Đã xác nhận | Đang sử dụng |

### Bảng Trạng thái Quy trình Thanh lý - Bán trực tiếp

| Sub-process | PIC | Action | Request Status | Asset Status | Note |
|-------------|-----|--------|----------------|--------------|------|
| 1. Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - |
| 1. Tạo yêu cầu | AMP | Gửi | Chờ kiểm soát | - | - |
| 2. Kiểm soát | Checker | Từ chối | Từ chối | - | - |
| 2. Kiểm soát | Checker | Yêu cầu bổ sung thông tin | Bổ sung thông tin | - | - |
| 2. Kiểm soát | Checker | Đồng ý | Chờ phê duyệt | - | - |
| 3. Phê duyệt | Approver | Từ chối | Đang tạo | - | - |
| 3. Phê duyệt | Approver | Yêu cầu bổ sung thông tin | Bổ sung thông tin | - | - |
| 3. Phê duyệt | Approver | Phê duyệt | Chờ cập nhật kết quả | - | - |
| 4. Cập nhật kết quả thanh lý | AMP | Hủy | Đã hủy | - | - |
| 4. Cập nhật kết quả thanh lý | AMP | Cập nhật kết quả | Đã cập nhật kết quả thanh lý | Đã thanh lý | - |
| 8. Nhận hàng | AMP | Từ chối | Từ chối | Từ chối | Trả lại trạng thái ban đầu trước khi thanh lý |
| 8. Nhận hàng | AMP | Xác nhận | Đã cập nhật kết quả thanh lý | Đã thanh lý | - |

## 9. Hình ảnh trong sheet

Không có hình ảnh.

---
*Source: Status.csv | Rows: 87 | Images: 0 | Images analyzed: 0 | Generated by Claude Sonnet 4.5*
