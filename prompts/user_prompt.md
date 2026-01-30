# User Prompt Template for BRD Synthesis

Dưới đây là các bản tóm tắt của {num_sheets} sheet từ file Excel Tài liệu Yêu cầu Nghiệp vụ.

Vui lòng tổng hợp những bản tóm tắt này thành một Tài liệu Yêu cầu Nghiệp vụ toàn diện theo hướng dẫn của bạn.

**LƯU Ý QUAN TRỌNG VỀ HÌNH ẢNH:**

⚠️ **SỬ DỤNG TOKEN `<<IMAGE:filename>>` - KHÔNG dùng markdown image syntax**

- Khi muốn nhúng hình ảnh, viết: `<<IMAGE:5_2_1a_B5_image1.png>>`
- KHÔNG viết: `![...](images/...)`
- Copy CHÍNH XÁC tên file từ Section 10
- Hệ thống sẽ tự động chuyển token thành markdown sau

**CÁC LƯU Ý KHÁC:**
1. **GIỮ NGUYÊN TÊN SHEET GỐC** làm tiêu đề section (tiếng Anh hoặc tiếng Việt - KHÔNG dịch)
2. Thêm số thứ tự trước tiêu đề (1., 2.1., 5.2.3., v.v.)
3. Kết hợp các sheet thành cặp (a/b) thành section duy nhất
4. **GIỮ NGUYÊN MARKDOWN TABLES** từ bản tóm tắt cho các sheet có mức độ chi tiết = `chi-tiết-cao`
5. **DÙNG PROSE** cho các sheet có mức độ chi tiết = `tổng-quan`
6. Bảo toàn NỘI DUNG ĐẦY ĐỦ từ mỗi sheet
7. **THÊM THAM CHIẾU CHÉO:** Nhắm đến 20+ liên kết nội bộ

---

## Các Bản tóm tắt Sheet

{summaries}

---

Vui lòng cung cấp BRD hoàn chỉnh ở định dạng Markdown với:
- Tiêu đề section giữ nguyên từ tên sheet gốc
- Tables được giữ nguyên khi cần
- Tham chiếu chéo nội bộ phong phú
- **Hình ảnh sử dụng TOKEN `<<IMAGE:filename>>`**