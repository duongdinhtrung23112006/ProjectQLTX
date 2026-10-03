# Prompt tạo báo cáo DOCX

## 1. Mục đích

Tạo file báo cáo DOCX từ nội dung đã được kiểm tra, giữ đúng cấu trúc và quy định trình bày của báo cáo.

## 2. Context

Đọc:

- `bao_cao/cau_truc_bao_cao.md`
- `bao_cao/quy_dinh_trinh_bay.md`
- Nội dung báo cáo đã hoàn thiện.
- `bao_cao/danh_sach_hinh.md`
- `bao_cao/danh_sach_bang.md`
- `bao_cao/danh_sach_tai_lieu_tham_khao.md`
- Các hình ảnh trong `bao_cao/hinh_anh/`
- Các biểu đồ trong `bao_cao/bieu_do/`

## 3. Nhiệm vụ

- Tạo file DOCX từ nội dung báo cáo.
- Giữ đúng thứ tự chương, mục và tiểu mục.
- Định dạng tiêu đề theo cấp.
- Định dạng đoạn văn, bảng và danh sách.
- Chèn hình đúng vị trí.
- Chèn chú thích và đánh số hình, bảng.
- Tạo mục lục nếu cấu trúc báo cáo yêu cầu.
- Tạo danh sách hình và danh sách bảng nếu có.
- Tạo phần tài liệu tham khảo.
- Lưu phiên bản DOCX vào `bao_cao/phien_ban/`.

## 4. Ràng buộc

- Không tự viết thêm nội dung báo cáo.
- Không thay đổi ý nghĩa nội dung nguồn.
- Không tự tạo số liệu, hình ảnh hoặc kết quả kiểm thử.
- Không làm mất bảng, hình hoặc chú thích.
- Không thay đổi tên chức năng, Use Case và thuật ngữ kỹ thuật.
- Không đưa thông tin bí mật hoặc API key vào báo cáo.
- Chỉ tạo DOCX khi nội dung nguồn đã đủ để tạo báo cáo.

## 5. Công cụ

Sử dụng thư viện `python-docx` để tạo file DOCX.

Nếu cần xử lý hình ảnh hoặc bảng, phải giữ đúng nội dung nguồn.

## 6. Output

Tạo:

`bao_cao/phien_ban/bao_cao_<phien_ban>.docx`

Kèm thông tin:

- Phiên bản.
- Ngày tạo.
- Nguồn nội dung.
- Các thành phần đã chèn.
- Các thành phần còn thiếu nếu có.

## 7. Kiểm tra sau khi tạo

Kiểm tra:

- File DOCX mở được.
- Đủ chương và mục.
- Không mất nội dung.
- Bảng hiển thị đúng.
- Hình hiển thị đúng.
- Chú thích hình và bảng đúng.
- Thứ tự đánh số nhất quán.
- Không có nội dung tự sinh ngoài nguồn.