# Prompt định dạng báo cáo DOCX

## 1. Mục đích

Định dạng file DOCX theo đúng quy định trình bày của báo cáo mà không thay đổi nội dung.

## 2. Context

Đọc:

- `bao_cao/quy_dinh_trinh_bay.md`
- `bao_cao/cau_truc_bao_cao.md`
- File DOCX hiện tại.
- Các quy định về tiêu đề, đoạn văn, bảng, hình, chú thích, mục lục và đánh số.

## 3. Nhiệm vụ

Thiết lập và kiểm tra:

- Khổ giấy và lề trang.
- Phông chữ và cỡ chữ.
- Tiêu đề chương, mục và tiểu mục.
- Khoảng cách đoạn và dòng.
- Căn lề và thụt đầu dòng.
- Đánh số chương, mục.
- Đánh số hình và bảng.
- Chú thích hình và bảng.
- Header, footer và số trang nếu được yêu cầu.
- Mục lục, danh sách hình và danh sách bảng nếu có.

## 4. Ràng buộc

- Chỉ thay đổi định dạng, không thay đổi nội dung.
- Không tự thêm hoặc xóa đoạn văn.
- Không thay đổi số liệu, bảng, hình và chú thích.
- Không tự đặt quy định trình bày nếu `quy_dinh_trinh_bay.md` đã quy định.
- Không làm thay đổi thứ tự nội dung.
- Không làm mất định dạng cần thiết của bảng hoặc hình.

## 5. Công cụ

Sử dụng `python-docx` để xử lý file DOCX.

Ưu tiên tạo các style dùng chung thay vì định dạng thủ công từng đoạn.

## 6. Output

Tạo file DOCX đã định dạng tại:

`bao_cao/phien_ban/`

Ghi lại:

- File nguồn.
- Phiên bản đầu ra.
- Các quy định đã áp dụng.
- Các vấn đề không thể tự xử lý.

## 7. Kiểm tra

Sau khi định dạng, kiểm tra:

- Nội dung không thay đổi.
- Style được áp dụng nhất quán.
- Tiêu đề đúng cấp.
- Số trang hoạt động đúng.
- Hình và bảng không bị lệch hoặc mất.
- Chú thích và đánh số không bị sai.
- Mục lục và danh sách liên quan phù hợp với nội dung.