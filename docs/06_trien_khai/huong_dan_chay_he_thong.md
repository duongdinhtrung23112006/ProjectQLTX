# Hướng dẫn chạy hệ thống

## 1. Mục đích

Hướng dẫn khởi động và kiểm tra hệ thống trong môi trường phát triển.

---

## 2. Kiểm tra môi trường

Mở terminal tại thư mục dự án:

```text
D:\ProjectQLTX

Kiểm tra Python:

python --version

Kiểm tra Git:

git --version

Đảm bảo MySQL đang chạy trước khi khởi động ứng dụng.

3. Kích hoạt môi trường Python

Trên Windows PowerShell:

.\venv\Scripts\Activate.ps1

Kiểm tra Python đang sử dụng:

python --version
4. Kiểm tra cấu hình

Đảm bảo .env có các biến:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=<mat_khau>
DB_NAME=tram_xang

Không đưa mật khẩu thật vào tài liệu hoặc Git.

5. Kiểm tra cơ sở dữ liệu

Đảm bảo:

MySQL đang hoạt động.
Database tram_xang tồn tại.
Các bảng cần thiết đã được tạo.
Tài khoản đăng nhập kiểm thử tồn tại.
Dữ liệu kiểm thử phù hợp với chức năng đang kiểm tra.
6. Khởi động Flask

Từ thư mục gốc dự án:

python app.py

Nếu ứng dụng khởi động thành công, terminal phải hiển thị thông tin máy chủ Flask.

Địa chỉ truy cập phụ thuộc vào cấu hình trong app.py.

Nếu ứng dụng sử dụng cấu hình mặc định, có thể truy cập:

http://127.0.0.1:5000
7. Kiểm tra đăng nhập

Mở trình duyệt và truy cập trang đăng nhập.

Thực hiện:

Nhập tài khoản hợp lệ.
Nhập mật khẩu.
Đăng nhập.
Kiểm tra trang được chuyển đến.
Kiểm tra vai trò của tài khoản.

Sau đó thử tài khoản có vai trò khác để kiểm tra phân quyền.

8. Kiểm tra các chức năng chính

Sau khi đăng nhập, kiểm tra theo vai trò:

Quản lý
Nhiên liệu.
Bồn chứa.
Nhập hàng.
Nhân viên.
Ca làm việc.
Dashboard.
Các chức năng quản lý được cấp quyền.
Nhân viên ca
Xem bồn.
Nhập hàng.
Các chức năng được cấp quyền.
Kế toán
Các chức năng tra cứu và thống kê được cấp quyền.

Các chức năng chưa triển khai phải được ghi nhận là chưa thực hiện.

9. Dừng hệ thống

Tại terminal đang chạy Flask:

Ctrl + C

Sau đó có thể thoát môi trường ảo:

deactivate
10. Xử lý lỗi khi khởi động
Không tìm thấy Python

Kiểm tra Python đã được cài đặt và PATH đã được cấu hình.

Không kết nối được MySQL

Kiểm tra:

MySQL.
.env.
Tên database.
Tài khoản.
Mật khẩu.
Quyền truy cập.
Không tìm thấy thư viện

Chạy:

pip install -r requirements.txt
Lỗi trong mã nguồn

Ghi lại:

Thông báo lỗi.
File gây lỗi.
Dòng lỗi.
Các bước tái hiện.

Nếu lỗi liên quan đến chức năng hệ thống, ghi vào:

docs/05_kiem_thu/danh_sach_loi.md

11. Kiểm tra sau khi khởi động

Trước khi sử dụng hệ thống cần xác nhận:

Flask đang chạy.
Kết nối CSDL thành công.
Trang đăng nhập hoạt động.
Phân quyền hoạt động.
Các chức năng cần kiểm thử có thể truy cập.
Không có lỗi nghiêm trọng trong terminal.
12. Nguyên tắc
Luôn chạy ứng dụng từ đúng thư mục dự án.
Sử dụng virtual environment.
Không ghi secret trực tiếp vào mã nguồn.
Không sử dụng dữ liệu thật trong môi trường kiểm thử.
Chỉ xác nhận hệ thống hoạt động sau khi kiểm tra thực tế.