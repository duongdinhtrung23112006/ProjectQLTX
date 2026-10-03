# Prompt phân tích thay đổi

## 1. Mục đích

Phân tích tác động của một yêu cầu hoặc thay đổi mới đối với tài liệu, mã nguồn, database, kiểm thử và triển khai.

## 2. Input

Cung cấp:

- Nội dung thay đổi.
- Lý do thay đổi.
- Phiên bản hoặc commit hiện tại nếu có.
- Các tài liệu liên quan nếu đã xác định.

AI Agent phải đọc thêm các tài liệu trong `docs/` và mã nguồn liên quan trước khi phân tích.

## 3. Nhiệm vụ

Xác định:

1. Yêu cầu nào bị ảnh hưởng.
2. Use Case và User Story bị ảnh hưởng.
3. Database và cấu trúc dữ liệu bị ảnh hưởng.
4. API và mã nguồn bị ảnh hưởng.
5. Giao diện bị ảnh hưởng.
6. Ca kiểm thử cần bổ sung hoặc cập nhật.
7. Tài liệu cần cập nhật.
8. Ảnh hưởng đến AI nếu có.
9. Ảnh hưởng đến triển khai và cấu hình nếu có.

## 4. Ràng buộc

- Không tự thực hiện thay đổi mã nguồn.
- Không tự thay đổi database.
- Không tự chấp nhận yêu cầu mới.
- Không bỏ qua các phụ thuộc hiện có.
- Nếu chưa đủ thông tin phải ghi rõ phần còn thiếu.
- Không tạo chức năng ngoài yêu cầu thay đổi.

## 5. Output

### Tóm tắt thay đổi
Mô tả ngắn gọn thay đổi cần thực hiện.

### Phạm vi ảnh hưởng
| Thành phần | Ảnh hưởng | Mức độ |
|---|---|---|
| Tài liệu | | |
| Database | | |
| Backend | | |
| Frontend | | |
| API | | |
| Kiểm thử | | |
| AI | | |
| Triển khai | | |

### Công việc cần thực hiện
Liệt kê theo thứ tự ưu tiên.

### Truy vết
Liên kết thay đổi với FR, UC, User Story, file và ca kiểm thử liên quan.

### Rủi ro
Nêu các rủi ro có căn cứ từ hệ thống hiện tại.

### Xác nhận
Chỉ thực hiện thay đổi sau khi người dùng xem xét và chấp nhận kết quả phân tích.