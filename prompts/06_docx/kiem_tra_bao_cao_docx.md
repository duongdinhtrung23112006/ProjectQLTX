# Prompt kiểm tra báo cáo DOCX

## 1. Mục đích

Kiểm tra file DOCX sau khi tạo hoặc định dạng để đảm bảo nội dung và hình thức phù hợp với báo cáo nguồn.

## 2. Context

Đọc:

- `bao_cao/cau_truc_bao_cao.md`
- `bao_cao/quy_dinh_trinh_bay.md`
- File DOCX cần kiểm tra.
- Các tài liệu nguồn trong `docs/` khi cần đối chiếu nội dung.

## 3. Nhiệm vụ

Kiểm tra:

### Nội dung

- Đủ chương, mục và tiểu mục.
- Nội dung khớp với nguồn.
- Không có nội dung bị mất hoặc lặp.
- Không có thông tin tự sinh hoặc chưa được xác nhận.

### Định dạng

- Khổ giấy và lề.
- Phông chữ và cỡ chữ.
- Tiêu đề các cấp.
- Khoảng cách dòng và đoạn.
- Căn lề và thụt đầu dòng.
- Header, footer và số trang.
- Mục lục.
- Danh sách hình và bảng.

### Hình và bảng

- Đủ hình và bảng.
- Hình hiển thị đúng.
- Bảng không bị cắt hoặc mất dữ liệu.
- Chú thích và số thứ tự chính xác.
- Vị trí hình và bảng phù hợp với nội dung.

### Tính nhất quán

Đối chiếu:

`DOCX ↔ Nội dung báo cáo ↔ Tài liệu nguồn`

## 4. Ràng buộc

- Không tự sửa lỗi nếu chưa xác định nguyên nhân.
- Không thay đổi nội dung chỉ để làm DOCX đẹp hơn.
- Không tự thêm hình, bảng hoặc số liệu.
- Nếu phát hiện thiếu nội dung nguồn, ghi rõ vị trí cần bổ sung.
- Nếu lỗi chỉ liên quan đến định dạng, phân loại riêng với lỗi nội dung.

## 5. Output

### Kết quả kiểm tra

| Mức độ | Vị trí | Nội dung kiểm tra | Kết quả | Vấn đề |
|---|---|---|---|---|

Trạng thái:

- `Đạt`
- `Cần sửa`
- `Cần xác nhận`

### Tổng hợp

- Lỗi nội dung.
- Lỗi định dạng.
- Lỗi hình/bảng.
- Lỗi đánh số hoặc mục lục.
- Các vấn đề cần người dùng xác nhận.

## 6. Nguyên tắc

File DOCX chỉ được xem là hoàn thiện khi nội dung, định dạng, hình, bảng và cấu trúc đều phù hợp với tài liệu nguồn.