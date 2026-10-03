# Phương án quay lui

## 1. Mục đích

Xác định cách đưa hệ thống về phiên bản ổn định trước đó khi phiên bản mới gây lỗi hoặc ảnh hưởng đến dữ liệu và chức năng.

---

## 2. Khi nào cần quay lui

Có thể thực hiện quay lui khi:

- Ứng dụng không thể khởi động.
- Chức năng chính bị lỗi nghiêm trọng.
- Phân quyền hoạt động sai.
- Kết nối database bị lỗi sau triển khai.
- Dữ liệu bị ảnh hưởng do thay đổi.
- Chức năng AI gây lỗi nghiêm trọng.
- Lỗi mới ảnh hưởng đến các chức năng đã hoạt động ổn định.

Quyết định quay lui phải dựa trên mức độ ảnh hưởng thực tế.

---

## 3. Chuẩn bị trước triển khai

Trước khi triển khai phiên bản mới cần:

- Ghi nhận mã commit hoặc phiên bản hiện tại.
- Backup database.
- Kiểm tra phiên bản đang chạy.
- Kiểm thử phiên bản mới.
- Xác định phiên bản có thể quay lui.
- Ghi nhận các thay đổi về database.

---

## 4. Quay lui mã nguồn

Xác định phiên bản ổn định trước đó:

```bash
git log --oneline

Có thể chuyển về commit cần thiết:

git checkout <commit_id>

Hoặc sử dụng quy trình Git phù hợp với chiến lược triển khai của dự án.

Không thực hiện thao tác Git trên môi trường production khi chưa xác định rõ ảnh hưởng.

5. Quay lui cơ sở dữ liệu

Nếu phiên bản mới đã thay đổi dữ liệu hoặc cấu trúc database:

Dừng các thao tác có thể làm dữ liệu thay đổi thêm.
Xác định backup phù hợp.
Phục hồi database trên môi trường an toàn.
Kiểm tra tính toàn vẹn dữ liệu.
Kiểm tra ứng dụng.
Đưa hệ thống hoạt động trở lại.

Không tự động phục hồi database nếu chưa xác định nguyên nhân và phạm vi ảnh hưởng.

6. Quay lui cấu hình

Nếu lỗi liên quan đến cấu hình:

Khôi phục cấu hình phiên bản trước.
Kiểm tra biến môi trường.
Kiểm tra kết nối database.
Kiểm tra cấu hình AI.
Khởi động lại ứng dụng.
Kiểm tra chức năng.

Secret phải được quản lý riêng và không ghi trực tiếp vào Git.

7. Quay lui chức năng AI

Nếu lỗi xuất phát từ AI:

Tạm ngừng chức năng AI bị lỗi nếu cần.
Giữ nguyên dữ liệu nghiệp vụ.
Kiểm tra prompt và dữ liệu đầu vào.
Kiểm tra phiên bản mô hình hoặc cấu hình AI.
Khôi phục cấu hình ổn định trước đó.
Kiểm thử lại.
Chỉ kích hoạt lại sau khi kết quả đạt yêu cầu.

AI không được phép tự thực hiện thao tác quay lui dữ liệu nghiệp vụ.

8. Kiểm tra sau quay lui

Sau khi quay lui phải kiểm tra:

Ứng dụng khởi động.
Đăng nhập.
Phân quyền.
Kết nối database.
Dữ liệu nghiệp vụ.
Các chức năng chính.
Các ca kiểm thử liên quan.
Log và lỗi hệ thống.
9. Ghi nhận sự cố

Mỗi lần quay lui cần ghi:

Thông tin	Nội dung
Thời điểm	
Phiên bản lỗi	
Phiên bản quay lui	
Nguyên nhân	
Phạm vi ảnh hưởng	
Backup sử dụng	
Người thực hiện	
Kết quả	
10. Sau khi quay lui

Sau khi hệ thống ổn định:

Phân tích nguyên nhân.
Xác định thay đổi gây lỗi.
Tạo hoặc cập nhật lỗi.
Sửa nguyên nhân.
Kiểm thử lại.
Cập nhật tài liệu.
Chỉ triển khai lại sau khi phiên bản mới đạt yêu cầu.
11. Nguyên tắc
Luôn có phiên bản ổn định để quay lui.
Backup trước thay đổi quan trọng.
Không quay lui một cách tùy tiện.
Không làm mất dữ liệu mới hợp lệ khi chưa đánh giá ảnh hưởng.
Sau quay lui phải kiểm thử xác nhận.
Mọi lần quay lui phải được ghi nhận để truy vết.