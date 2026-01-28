# Phân tích Sheet: Status

## 1. Loại sheet
**quy-trình** - Sheet mô tả các trạng thái và luồng xử lý trong hệ thống quản lý tài sản

## 2. Mức độ chi tiết
**chi-tiết-cao** - Sheet chứa mapping chi tiết các trạng thái, hành động và chuyển đổi trạng thái cụ thể

## 3. Chủ đề/tiêu đề chính
**Ma trận trạng thái và luồng xử lý tài sản** - Định nghĩa các trạng thái của yêu cầu (Request Status) và tài sản (Asset Status) trong các quy trình cấp phát, thanh lý và điều chuyển tài sản

## 4. Tóm tắt thông tin chính

Sheet này định nghĩa một hệ thống trạng thái phức tạp cho việc quản lý tài sản với ba quy trình chính: cấp tài sản, thanh lý tài sản và điều chuyển tài sản. Mỗi quy trình được chia thành các sub-process với các trạng thái yêu cầu và trạng thái tài sản tương ứng.

Quy trình cấp tài sản được chia thành hai luồng: cấp tài sản không ở kho (luồng đơn giản hơn) và cấp tài sản từ kho (luồng phức tạp với nhiều bước phê duyệt). Quy trình thanh lý cũng có hai hình thức: bán trực tiếp và bán đấu giá, với quy trình đấu giá có thêm các bước kiểm soát và phê duyệt kết quả thanh lý.

Hệ thống trạng thái được thiết kế để theo dõi cả trạng thái của yêu cầu (Request Status) và trạng thái của tài sản (Asset Status), cho phép kiểm soát chặt chẽ toàn bộ vòng đời của tài sản từ lúc cấp phát đến khi thanh lý.

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

- Hệ thống phải hỗ trợ các trạng thái yêu cầu: Đang tạo, Chờ xác nhận, Đã xác nhận, Từ chối, Bổ sung thông tin
- Hệ thống phải theo dõi trạng thái tài sản: Đang sử dụng, Đã nhập kho, Đã thanh lý
- Cần có cơ chế rollback trạng thái tài sản về "trạng thái ban đầu trước khi thanh lý" khi hủy yêu cầu
- Hệ thống phải tự động tạo yêu cầu xuất kho/nhập kho sau khi hoàn thành các bước phê duyệt
- Cần phân quyền rõ ràng cho từng vai trò trong từng bước của quy trình

## 7. Các sheet liên quan

Không có tham chiếu trực tiếp đến sheet khác, nhưng có thể liên quan đến các sheet định nghĩa quy trình chi tiết và giao diện người dùng.

## 8. Bảng cần giữ nguyên

### Ma trận trạng thái - Cấp tài sản không ở kho

| Sub-process | PIC | Action | Request Status | Asset Status | Note |
|-------------|-----|--------|----------------|--------------|------|
| 1 Tạo yêu cầu | AMP | Lưu | Đang tạo | - | - |
| 1 Tạo yêu cầu | AMP | Gửi | Chờ xác nhận | - | - |
| 2. Xác nhận | BU User | Từ chối | Từ chối | - | - |
| 2. Xác nhận | BU User | Xác nhận | Đã xác nhận | Đang sử dụng | Đã xác nhận >>> Đã nhận tài sản |
| 2. Xác nhận | BU User | Bổ sung thông tin | Bổ sung thông tin | - | - |
| 3. Bổ sung TT | AMP | Bổ sung thông tin | Chờ xác nhận | - | - |

### Ma trận trạng thái - Cấp tài sản từ kho

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

### Ma trận trạng thái - Thanh lý tài sản (Bán trực tiếp)

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

## 9. Hình ảnh trong sheet

Không có hình ảnh.

---
*Source: Status.csv | Rows: 87 | Images: 0 | Images analyzed: 0 | Generated by Claude Sonnet 4.5*
