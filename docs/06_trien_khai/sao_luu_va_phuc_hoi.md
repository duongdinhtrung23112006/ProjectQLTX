# Sao lưu và phục hồi

## 1. Mục đích

Đảm bảo dữ liệu của hệ thống có thể được sao lưu và phục hồi khi xảy ra lỗi, mất dữ liệu hoặc sự cố triển khai.

---

## 2. Dữ liệu cần sao lưu

Dữ liệu chính cần sao lưu:

- Database `tram_xang`.
- Cấu hình cần thiết để phục hồi hệ thống.
- Các tệp dữ liệu nghiệp vụ nếu có.
- Các tài liệu quan trọng của dự án.

Không sao lưu secret theo cách làm lộ mật khẩu hoặc API key.

---

## 3. Phương pháp sao lưu

Có thể sử dụng công cụ của MySQL để xuất database.

Ví dụ:

```bash
mysqldump -u root -p tram_xang > tram_xang_backup.sql

Hệ thống yêu cầu nhập mật khẩu khi thực hiện lệnh.

File backup cần được lưu tại vị trí an toàn, không đưa thông tin nhạy cảm lên repository công khai.

4. Nội dung backup

Một bản backup cần có khả năng khôi phục:

Cấu trúc bảng.
Khóa chính.
Khóa ngoại.
Dữ liệu nghiệp vụ.
Các ràng buộc cần thiết.

Cần kiểm tra backup có thể sử dụng được thay vì chỉ kiểm tra file có tồn tại.

5. Phục hồi database

Tạo database nếu chưa tồn tại:

CREATE DATABASE tram_xang;

Sau đó phục hồi:

mysql -u root -p tram_xang < tram_xang_backup.sql

Kiểm tra sau phục hồi:

Các bảng tồn tại.
Dữ liệu tồn tại.
Quan hệ giữa các bảng hoạt động.
Ứng dụng kết nối được database.
Các chức năng chính hoạt động.
6. Kiểm tra backup

Định kỳ kiểm tra:

Tạo backup.
Phục hồi trên môi trường kiểm thử.
Kiểm tra cấu trúc database.
Kiểm tra dữ liệu.
Chạy các ca kiểm thử liên quan.
Ghi nhận kết quả.

Một backup chưa được kiểm tra khả năng phục hồi không được xem là đã xác nhận sử dụng được.

7. Khi xảy ra sự cố

Quy trình:

Xác định nguyên nhân.
Ngăn các thao tác có thể làm dữ liệu hỏng thêm.
Xác định bản backup phù hợp.
Phục hồi trên môi trường an toàn nếu có thể.
Kiểm tra dữ liệu.
Kiểm tra ứng dụng.
Đưa hệ thống hoạt động trở lại.
Ghi nhận sự cố và quá trình phục hồi.
8. Lịch sử backup

Theo dõi:

Thời điểm	Phiên bản	Phạm vi	Vị trí	Kết quả kiểm tra
				

Không ghi mật khẩu hoặc secret vào bảng này.

9. Nguyên tắc
Backup phải được lưu tách khỏi môi trường đang chạy.
Không chỉ lưu một bản backup duy nhất.
Không ghi đè backup quan trọng mà không có phương án dự phòng.
Backup phải được kiểm tra khả năng phục hồi.
Khi phục hồi phải kiểm tra tính toàn vẹn dữ liệu.
Mọi sự cố phục hồi phải được ghi nhận để có thể truy vết.