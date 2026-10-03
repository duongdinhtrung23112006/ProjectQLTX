# Cấu hình mẫu

## 1. Mục đích

Cung cấp cấu hình mẫu để thiết lập môi trường mà không chứa thông tin bí mật.

Cấu hình thực tế được lưu bằng biến môi trường hoặc cơ chế quản lý secret phù hợp.

---

## 2. Cấu hình môi trường

Tạo tệp `.env` tại thư mục gốc dự án:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=<mat_khau>
DB_NAME=tram_xang

Trong đó:

DB_HOST: máy chủ MySQL.
DB_USER: tài khoản MySQL.
DB_PASSWORD: mật khẩu MySQL.
DB_NAME: tên cơ sở dữ liệu.

Không thay <mat_khau> bằng mật khẩu thật trong tài liệu hoặc Git.

3. Cấu hình Flask

Các cấu hình liên quan đến Flask phải được quản lý riêng theo môi trường.

Có thể bao gồm:

Chế độ phát triển.
Địa chỉ máy chủ.
Cổng chạy ứng dụng.
Secret key.
Cấu hình log.

Secret key không được ghi trực tiếp vào tài liệu công khai.

4. Cấu hình AI

Khi tích hợp AI, các thông tin cần quản lý bằng biến môi trường gồm:

AI_API_KEY=<api_key>
AI_MODEL=<model_name>

Tên biến có thể được điều chỉnh theo dịch vụ AI thực tế.

Không lưu API key trực tiếp trong mã nguồn, prompt hoặc Git.

5. Cấu hình cơ sở dữ liệu

Cấu hình phải đảm bảo ứng dụng kết nối đúng:

Ứng dụng Flask
      ↓
Biến môi trường
      ↓
MySQL
      ↓
Database tram_xang

Thông tin kết nối phải được kiểm tra trước khi chạy hệ thống.

6. Cấu hình theo môi trường
Development

Dùng cho phát triển.

Có thể sử dụng:

MySQL cục bộ.
Dữ liệu kiểm thử.
Log chi tiết.
Testing

Dùng cho kiểm thử.

Nên sử dụng:

Database riêng.
Dữ liệu kiểm thử.
Cấu hình AI kiểm thử nếu cần.
Production

Dùng cho hệ thống thực tế.

Cần:

Secret riêng.
Database riêng.
Cấu hình bảo mật phù hợp.
Logging và giám sát.
Sao lưu dữ liệu.

Không dùng trực tiếp cấu hình production trong môi trường phát triển.

7. .gitignore

Các tệp chứa thông tin hoặc dữ liệu môi trường không nên commit:

.env
venv/
.venv/
__pycache__/
*.pyc

Các thư mục hoặc tệp dữ liệu khác chỉ được thêm vào .gitignore khi xác định rõ lý do.

8. Kiểm tra cấu hình

Trước khi chạy hệ thống:

Kiểm tra .env tồn tại.
Kiểm tra tên database.
Kiểm tra kết nối MySQL.
Kiểm tra các biến AI nếu AI được sử dụng.
Kiểm tra secret không xuất hiện trong Git.
Khởi động ứng dụng.
Kiểm tra chức năng cần thiết.
9. Nguyên tắc bảo mật
Không ghi mật khẩu thật vào tài liệu.
Không commit .env.
Không đưa API key vào prompt mẫu.
Không ghi secret vào log.
Mỗi môi trường sử dụng secret riêng.
Khi secret bị lộ phải thay đổi hoặc thu hồi secret đó.