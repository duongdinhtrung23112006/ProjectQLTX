# Hướng dẫn cài đặt

## 1. Mục đích

Hướng dẫn chuẩn bị môi trường và cài đặt hệ thống quản lý trạm xăng.

Tài liệu này áp dụng cho môi trường phát triển và là cơ sở để xây dựng quy trình triển khai thực tế.

---

## 2. Yêu cầu môi trường

Các thành phần cần chuẩn bị:

- Python.
- Git.
- MySQL.
- Trình duyệt web.
- Visual Studio Code hoặc IDE tương đương.

Các phiên bản cụ thể phải được ghi nhận theo môi trường thực tế tại thời điểm triển khai.

---

## 3. Lấy mã nguồn

Clone repository:

```bash
git clone https://github.com/duongdinhtrung23112006/ProjectQLTX.git
cd ProjectQLTX

Kiểm tra mã nguồn:

git status
4. Tạo môi trường Python

Tạo virtual environment:

python -m venv venv

Kích hoạt trên Windows:

.\venv\Scripts\Activate.ps1

Sau khi kích hoạt, kiểm tra:

python --version
5. Cài đặt thư viện

Cài đặt các thư viện từ:

requirements.txt

Lệnh:

pip install -r requirements.txt

Nếu có lỗi cài đặt, ghi nhận lỗi và phiên bản môi trường trước khi xử lý.

6. Chuẩn bị MySQL

Tạo cơ sở dữ liệu:

CREATE DATABASE tram_xang;

Sau đó tạo các bảng theo thiết kế CSDL của dự án.

Các bảng hiện có gồm:

nhien_lieu
bon_chua
nhap_hang
nhan_vien
ca_lam_viec
tai_khoan

Các bảng hoặc chức năng chưa triển khai không được tự coi là đã tồn tại.

7. Cấu hình kết nối CSDL

Tạo tệp .env ở thư mục gốc của dự án.

Các biến:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=<mat_khau>
DB_NAME=tram_xang

Không đưa mật khẩu thật vào tài liệu hoặc Git.

Tệp .env phải được loại khỏi phạm vi commit thông qua .gitignore.

8. Kiểm tra kết nối CSDL

Chạy ứng dụng hoặc chương trình kiểm tra kết nối hiện có.

Nếu kết nối thất bại, kiểm tra:

MySQL đã chạy chưa.
Host có đúng không.
User có đúng không.
Mật khẩu có đúng không.
Tên database có đúng không.
Quyền truy cập database.
9. Kiểm tra cấu trúc dự án

Sau khi cài đặt, kiểm tra các thành phần chính:

ProjectQLTX/
├── app.py
├── routes/
├── services/
├── static/
├── templates/
├── docs/
├── prompts/
├── requirements.txt
└── .gitignore

Cấu trúc thực tế có thể thay đổi theo phiên bản, nhưng phải được cập nhật trong tài liệu khi có thay đổi.

10. Kiểm tra sau cài đặt

Kiểm tra tối thiểu:

Python hoạt động.
Virtual environment hoạt động.
Thư viện đã cài đặt.
MySQL đang chạy.
Database tram_xang tồn tại.
Kết nối CSDL thành công.
Ứng dụng Flask khởi động được.
Trang đăng nhập có thể truy cập.
11. Xử lý lỗi cài đặt

Khi cài đặt thất bại cần ghi nhận:

Lệnh đã thực hiện.
Thông báo lỗi.
Phiên bản Python.
Phiên bản thư viện liên quan.
Môi trường hệ điều hành.
Cách xử lý.
Kết quả sau khi xử lý.

Lỗi quan trọng được ghi vào:

docs/05_kiem_thu/danh_sach_loi.md

12. Nguyên tắc
Không sử dụng secret thật trong tài liệu.
Không commit .env.
Không tự bỏ qua lỗi cài đặt.
Không xác nhận cài đặt thành công nếu chưa kiểm tra ứng dụng.
Mọi thay đổi môi trường có ảnh hưởng đến hệ thống phải được ghi nhận.