Đọc sheet này từ tài liệu Yêu cầu Nghiệp vụ (BRD) và phân tích nội dung.

Tên sheet: {sheet_name}
Nội dung sheet (định dạng CSV):
{content}

Vui lòng đưa ra:

1. **Loại sheet**: Phân loại là một trong các loại: tổng-quan/quy-trình/giao-diện/đặc-tả/mô-hình-dữ-liệu/khác

2. **Mức độ chi tiết**: Phân loại là một trong hai loại:
   - `chi-tiết-cao`: Sheet chứa nhiều thông số kỹ thuật, số liệu cụ thể, validation rules, field specifications, hoặc data mapping → CẦN GIỮ NGUYÊN DẠNG BẢNG
   - `tổng-quan`: Sheet chứa mô tả quy trình, luồng công việc, hoặc thông tin high-level → CÓ THỂ CHUYỂN THÀNH PROSE/SECTIONS

3. **Chủ đề/tiêu đề chính**: Chủ đề hoặc mục đích chính của sheet này là gì?

4. **Tóm tắt thông tin chính**: Cung cấp 2-3 đoạn văn tóm tắt các thông tin thiết yếu, logic nghiệp vụ và yêu cầu trong sheet này.

5. **Các bên liên quan/vai trò được đề cập**: Liệt kê các cá nhân, nhóm, vai trò hoặc phòng ban được đề cập.

6. **Các yêu cầu tìm thấy**: Trích xuất các yêu cầu, đặc tả hoặc ràng buộc rõ ràng (nếu có).

7. **Các sheet liên quan**: Xác định các tham chiếu đến sheet khác, tài liệu hoặc hệ thống khác.

8. **Bảng cần giữ nguyên** (CHỈ khi mức độ chi tiết = `chi-tiết-cao`):
   Nếu sheet chứa bảng với thông số kỹ thuật quan trọng, hãy chuyển đổi sang định dạng Markdown table và đưa vào đây.
   
   Các loại bảng CẦN giữ nguyên:
   - Bảng field specifications (tên trường, kiểu dữ liệu, độ dài, bắt buộc/không)
   - Bảng validation rules
   - Bảng status/state transitions
   - Bảng data mapping (source → target)
   - Bảng API specifications
   - Bảng error codes
   - Bảng permission/role matrix
   
   Định dạng Markdown table:
   ```markdown
   | Tên trường | Kiểu dữ liệu | Độ dài | Bắt buộc | Mô tả |
   |------------|--------------|--------|----------|-------|
   | ma_yeu_cau | VARCHAR      | 50     | Có       | Mã yêu cầu theo format NK.YY.xxxx |
   ```

9. **Hình ảnh trong sheet** (QUAN TRỌNG - SỬ DỤNG TOKEN):
   Tìm TẤT CẢ các tham chiếu hình ảnh trong sheet (có dạng `![...](images/...)`).
   Trích xuất TÊN FILE và liệt kê dưới dạng token.
   
   Ví dụ nếu trong CSV có: `B5: ![5.2.1a_B5](images/5_2_1a_B5_image1.png)`
   Thì ghi:
   ```
   - Cell B5: `<<IMAGE:5_2_1a_B5_image1.png>>`
   ```
   
   CHỈ lấy tên file (phần sau `images/`), KHÔNG bao gồm path.
   Nếu không có hình ảnh, ghi "Không có hình ảnh."

Trình bày phân tích của bạn dưới dạng markdown ngôn ngữ tự nhiên (KHÔNG phải JSON). Ngắn gọn nhưng đầy đủ.