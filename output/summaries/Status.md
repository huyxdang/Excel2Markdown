# Phân tích Sheet Status

## 1. Loại sheet
**quy-trình**

## 2. Mức độ chi tiết
**chi-tiết-cao** - Sheet chứa bảng mapping chi tiết về status transitions, actions, và roles cụ thể cho từng bước trong quy trình nghiệp vụ.

## 3. Chủ đề/tiêu đề chính
Định nghĩa trạng thái (status) và luồng chuyển đổi trạng thái cho các quy trình quản lý tài sản, bao gồm cấp tài sản, thanh lý tài sản và điều chuyển tài sản.

## 4. Tóm tắt thông tin chính
Sheet này định nghĩa chi tiết các trạng thái trong hệ thống quản lý tài sản với ba quy trình chính: cấp tài sản (từ kho và không từ kho), thanh lý tài sản (bán trực tiếp và đấu giá), và điều chuyển tài sản (về kho và giữa các kho). Mỗi quy trình được chia thành các bước con với người chịu trách nhiệm (PIC) cụ thể và các hành động có thể thực hiện.

Hệ thống trạng thái được thiết kế với các luồng phê duyệt nhiều cấp, cho phép từ chối, yêu cầu bổ sung thông tin, và theo dõi trạng thái tài sản từ lúc tạo yêu cầu đến khi hoàn thành. Đặc biệt, quy trình thanh lý có sự phân biệt rõ ràng giữa Request Status (trạng thái yêu cầu) và Asset Status (trạng thái tài sản).

## 5. Các bên liên quan/vai trò được đề cập
- **AMP** (Asset Management Personnel): Quản lý tài sản
- **BU User**: Người dùng nghiệp vụ
- **BU Head**: Trưởng phòng nghiệp vụ
- **AM**: Asset Manager
- **WK**: Warehouse Keeper (Thủ kho)
- **Warehouse Mgr.**: Quản lý kho
- **Checker**: Người kiểm soát
- **Approver**: Người phê duyệt
- **System**: Hệ thống tự động

## 6. Các yêu cầu tìm thấy
- Hệ thống phải hỗ trợ lưu tạm yêu cầu trước khi gửi chính thức
- Cần có cơ chế phê duyệt nhiều cấp cho các quy trình
- Phải có khả năng từ chối và yêu cầu bổ sung thông tin tại mỗi bước
- Hệ thống tự động tạo yêu cầu xuất kho/nhập kho sau khi được phê duyệt
- Trạng thái tài sản phải được cập nhật đồng bộ với trạng thái yêu cầu
- Có cơ chế khôi phục trạng thái ban đầu khi hủy yêu cầu

## 7. Các sheet liên quan
Không có tham chiếu trực tiếp đến sheet khác, nhưng liên quan đến các sheet định nghĩa quy trình cụ thể cho từng module.

## 8. Bảng cần giữ nguyên

### Bảng trạng thái quy trình Cấp tài sản không ở kho

| Sub-process | PIC | Action | Rq Status | Asset Status | Note |
|-------------|-----|--------|-----------|--------------|------|
| 1 Tạo yêu cầu | AMP | Lưu | Đang tạo | | |
| | | Gửi | Chờ xác nhận | | |
| 2. Xác nhận | BU User | Từ chối | Từ chối | | |
| | | Xác nhận | Đã xác nhận | Đang sử dụng | Đã xác nhận >>> Đã nhận tài sản |
| | | Bổ sung thông tin | Bổ sung thông tin | | |
| 3. Bổ sung TT | AMP | Bổ sung thông tin | Chờ xác nhận | | |

### Bảng trạng thái quy trình Cấp tài sản từ kho

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

### Bảng trạng thái quy trình Thanh lý - Bán trực tiếp

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

## 9. Hình ảnh trong sheet
Không có hình ảnh.

---
*Source: Status.csv | Rows: 87 | Images analyzed: 0*
