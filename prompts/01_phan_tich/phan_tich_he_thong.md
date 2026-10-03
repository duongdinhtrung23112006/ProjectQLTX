# Prompt phân tích hệ thống

## 1. Mục đích

Phân tích tổng thể hệ thống dựa trên tài liệu trong thư mục `docs/`, không tự suy đoán hoặc bổ sung yêu cầu chưa được xác nhận.

## 2. Context

Đọc các tài liệu liên quan trước khi phân tích:

- `docs/01_tong_quan/`
- `docs/02_phan_tich/`
- `docs/03_thiet_ke/`
- `docs/04_so_do/`
- `docs/08_trang_thai/`

Ưu tiên thông tin trong tài liệu dự án và mã nguồn hiện tại.

## 3. Nhiệm vụ

AI Agent thực hiện:

1. Xác định mục đích và phạm vi hệ thống.
2. Xác định các vai trò người dùng.
3. Liệt kê các chức năng chính.
4. Đối chiếu yêu cầu với Use Case và User Story.
5. Kiểm tra quan hệ giữa các chức năng.
6. Phát hiện yêu cầu thiếu, mâu thuẫn hoặc chưa rõ.
7. Đối chiếu với trạng thái triển khai hiện tại.
8. Xác định các thành phần cần phân tích thêm.

## 4. Ràng buộc

- Không tự tạo yêu cầu nghiệp vụ mới.
- Không thay đổi phạm vi hệ thống nếu chưa được yêu cầu.
- Không coi AI là một actor nghiệp vụ.
- Không thay đổi quyết định đã được xác nhận trong tài liệu.
- Nếu thiếu thông tin, phải ghi rõ `Chưa xác định`.
- Phân biệt rõ thông tin từ tài liệu với đề xuất của AI.

## 5. Output

Trả kết quả theo cấu trúc:

### Tổng quan
Tóm tắt hệ thống và mục đích.

### Vai trò
Danh sách vai trò và trách nhiệm.

### Chức năng
Danh sách chức năng và mã FR/UC liên quan.

### Phân tích
Các quan hệ, phụ thuộc và điểm cần chú ý.

### Vấn đề phát hiện
Các yêu cầu thiếu, mâu thuẫn hoặc chưa rõ.

### Đề xuất
Chỉ đưa ra đề xuất khi cần thiết và phải đánh dấu rõ là đề xuất.

### Truy vết
Liên kết kết quả với tài liệu, FR, UC hoặc User Story tương ứng.