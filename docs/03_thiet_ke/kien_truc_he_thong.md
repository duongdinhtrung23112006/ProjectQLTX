# KIẾN TRÚC HỆ THỐNG

## 1. Tổng quan

Hệ thống quản lý trạm xăng được xây dựng theo kiến trúc phân lớp, tách giao diện, xử lý nghiệp vụ và truy cập dữ liệu. AI được tích hợp như một thành phần hỗ trợ phân tích và sinh nội dung.

```text
Người dùng
    ↓
Giao diện Web
    ↓
Route / Controller
    ↓
Service / Business Logic
    ↓
Database
    ↓
MySQL

AI được kết nối với lớp nghiệp vụ thông qua một thành phần tích hợp riêng:

Database
    ↓
Business Logic
    ↓
AI Service
    ↓
LLM
    ↓
Kết quả AI
    ↓
Người dùng kiểm tra
2. Các lớp chính
2.1. Presentation Layer

Chịu trách nhiệm:

Giao diện HTML/Jinja.
CSS và JavaScript.
Hiển thị dữ liệu.
Nhận thao tác từ người dùng.
2.2. Application Layer

Bao gồm các route và xử lý luồng chức năng.

Nhiệm vụ:

Tiếp nhận request.
Kiểm tra quyền truy cập.
Gọi service tương ứng.
Trả kết quả về giao diện.
2.3. Business Layer

Chứa logic nghiệp vụ của hệ thống.

Nhiệm vụ:

Kiểm tra quy tắc nghiệp vụ.
Xử lý nhập hàng.
Xử lý bán hàng.
Tính và kiểm soát tồn bồn.
Xử lý ca làm việc.
Xử lý doanh thu và thống kê.
Điều phối chức năng AI.
2.4. Data Access Layer

Chịu trách nhiệm:

Kết nối MySQL.
Truy vấn dữ liệu.
Thực hiện thêm, sửa, xóa và đọc dữ liệu.
Đảm bảo transaction đối với nghiệp vụ cần tính nhất quán.
2.5. AI Layer

Chịu trách nhiệm:

Chuẩn bị dữ liệu đầu vào cho AI.
Gửi prompt và dữ liệu đến mô hình AI.
Nhận và xử lý kết quả.
Kiểm tra kết quả trước khi hiển thị.

AI không trực tiếp thay đổi dữ liệu nghiệp vụ.

3. Các module chính
Hệ thống quản lý trạm xăng
├── Authentication
├── Quản lý nhiên liệu
├── Quản lý bồn chứa
├── Quản lý nhập hàng
├── Quản lý bán hàng
├── Quản lý tồn bồn
├── Quản lý nhân viên
├── Quản lý ca làm việc
├── Doanh thu và thống kê
└── Tích hợp AI
4. Công nghệ hiện tại
Backend: Flask.
Database: MySQL.
Giao diện: HTML/Jinja, CSS, JavaScript.
Quản lý mã nguồn: Git.
AI: mô hình ngôn ngữ thông qua API hoặc nền tảng được cấu hình.
5. Nguyên tắc kiến trúc
Không đưa logic nghiệp vụ phức tạp trực tiếp vào template.
Không để thông tin bí mật trong source code.
Route chịu trách nhiệm điều phối, service chịu trách nhiệm xử lý nghiệp vụ.
Dữ liệu phải được kiểm tra trước khi ghi vào cơ sở dữ liệu.
Các thao tác cập nhật tồn quan trọng phải đảm bảo tính nhất quán.
AI chỉ nhận dữ liệu cần thiết và không tự quyết định nghiệp vụ.
Thay đổi kiến trúc phải được cập nhật trong tài liệu và kiểm thử lại các thành phần liên quan.