# Prompt xem xét mã nguồn

## 1. Mục đích

Đánh giá mã nguồn hiện tại về tính đúng đắn, bảo mật, khả năng bảo trì và mức độ phù hợp với thiết kế của hệ thống.

## 2. Context

AI Agent phải đọc:

- Mã nguồn cần xem xét.
- `docs/02_phan_tich/`.
- `docs/03_thiet_ke/`.
- `docs/05_kiem_thu/`.
- `docs/08_trang_thai/`.

## 3. Nội dung xem xét

Kiểm tra:

- Logic nghiệp vụ.
- Xử lý dữ liệu đầu vào.
- Xử lý lỗi và ngoại lệ.
- Phân quyền.
- Truy vấn database.
- Quản lý transaction.
- Bảo mật.
- Quản lý secret và biến môi trường.
- Cấu trúc và khả năng bảo trì.
- Hiệu năng ở mức phù hợp.
- Khả năng kiểm thử.
- Sự phù hợp với tài liệu thiết kế.

## 4. Ràng buộc

- Không tự sửa mã nguồn khi chỉ được yêu cầu review.
- Không đánh giá dựa trên giả định chưa có căn cứ.
- Phân biệt lỗi thực tế với đề xuất cải thiện.
- Không yêu cầu tối ưu hóa không cần thiết.
- Không tự thay đổi nghiệp vụ.

## 5. Output

### Tổng quan

Đánh giá ngắn gọn tình trạng mã nguồn.

### Vấn đề phát hiện

| ID | File | Vấn đề | Mức độ | Loại |
|---|---|---|---|---|
| CODE-001 | | | | |
| CODE-002 | | | | |

Loại vấn đề có thể gồm:

- Logic.
- Bảo mật.
- Dữ liệu.
- Hiệu năng.
- Cấu trúc.
- Khả năng bảo trì.
- Kiểm thử.

### Đề xuất

Nêu cách cải thiện tương ứng với từng vấn đề.

### Kiểm tra bổ sung

Liệt kê các test cần thực hiện để xác nhận vấn đề.

### Truy vết

`Code → FR/UC → Test → Vấn đề`

### Kết luận

Phân biệt rõ vấn đề cần sửa với các cải tiến tùy chọn.