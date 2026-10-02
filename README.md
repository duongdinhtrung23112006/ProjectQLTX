# Hệ thống quản lý trạm xăng có tích hợp AI

Hệ thống quản lý các hoạt động của một trạm xăng, được xây dựng bằng **Python Flask** và **MySQL**, có tích hợp các chức năng AI nhằm hỗ trợ tổng hợp, phân tích và phát hiện những số liệu bất thường trong quá trình vận hành.

## 📌 Giới thiệu

Project được xây dựng nhằm số hóa một số hoạt động quản lý tại trạm xăng, thay thế việc theo dõi thủ công bằng hệ thống quản lý tập trung.

Hệ thống hỗ trợ quản lý:

* Bồn chứa nhiên liệu
* Mặt hàng nhiên liệu
* Nhập hàng
* Bán hàng theo ca
* Tồn bồn
* Nhân viên
* Ca làm việc
* Doanh thu và các số liệu nhập – xuất – tồn

Ngoài các chức năng quản lý cơ bản, hệ thống định hướng tích hợp AI để hỗ trợ người dùng tổng hợp và phân tích dữ liệu.

## 🚀 Chức năng chính

### 👤 Quản lý tài khoản và phân quyền

Hệ thống hỗ trợ 3 vai trò:

* **Quản lý**
* **Nhân viên ca**
* **Kế toán**

Mỗi vai trò được giới hạn quyền truy cập vào các chức năng phù hợp.

### ⛽ Quản lý bồn chứa

* Xem danh sách bồn chứa
* Xem thông tin chi tiết bồn chứa
* Thêm bồn chứa
* Sửa thông tin bồn chứa
* Xóa bồn chứa
* Theo dõi sức chứa và lượng tồn hiện tại
* Theo dõi trạng thái bồn

### 🛢️ Quản lý nhiên liệu

* Xem danh sách nhiên liệu
* Xem thông tin nhiên liệu
* Thêm nhiên liệu
* Sửa thông tin nhiên liệu
* Xóa nhiên liệu
* Quản lý đơn vị và đơn giá

### 👨‍💼 Quản lý nhân viên

* Quản lý thông tin nhân viên
* Quản lý chức vụ
* Theo dõi trạng thái làm việc

### 🕐 Quản lý ca làm việc

* Tạo ca làm việc
* Phân công nhân viên
* Theo dõi ngày làm việc và trạng thái ca

### 📊 Thống kê và tra cứu

* Tra cứu doanh thu
* Theo dõi số liệu nhập – xuất – tồn
* Thống kê sản lượng bán
* Theo dõi chênh lệch tồn

### 🤖 Tích hợp AI

AI được định hướng sử dụng để hỗ trợ:

* Sinh báo cáo ca
* Tóm tắt biến động tồn bồn
* Phân tích và cảnh báo các số liệu có dấu hiệu bất thường

Các kết quả do AI tạo ra có tính chất **hỗ trợ tổng hợp và phân tích dữ liệu**, không thay thế quyết định của người quản lý.

## 🛠️ Công nghệ sử dụng

| Thành phần       | Công nghệ             |
| ---------------- | --------------------- |
| Backend          | Python, Flask         |
| Database         | MySQL                 |
| Frontend         | HTML, CSS, JavaScript |
| Template engine  | Jinja2                |
| Quản lý mã nguồn | Git, GitHub           |
| AI               | Đang phát triển       |

## 📂 Cấu trúc project

```text
ProjectQLTX/
├── app.py
├── routes/
│   ├── auth/
│   ├── ketoan/
│   ├── nhanvien/
│   └── quanly/
├── services/
│   ├── auth_service.py
│   ├── database.py
│   └── quan_ly_ca.py
├── static/
│   ├── auth/
│   ├── cssketoan/
│   ├── cssnhanvien/
│   ├── cssquanly/
│   ├── images/
│   └── js/
├── templates/
│   ├── auth/
│   ├── ketoan/
│   ├── nhanvien/
│   └── quanly/
├── docs/
├── requirements.txt
├── test_database.py
└── .gitignore
```

## ⚙️ Cài đặt và chạy project

### 1. Clone repository

```bash
git clone https://github.com/duongdinhtrung23112006/ProjectQLTX.git
cd ProjectQLTX
```

### 2. Tạo môi trường ảo

Windows:

```powershell
python -m venv venv
```

Kích hoạt:

```powershell
.\venv\Scripts\activate
```

### 3. Cài đặt thư viện

```powershell
pip install -r requirements.txt
```

### 4. Cấu hình database

Tạo database MySQL:

```sql
CREATE DATABASE tram_xang;
```

Sau đó cấu hình thông tin kết nối database trong file `.env`:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=tram_xang
```

> Không đưa file `.env` lên GitHub vì file này có thể chứa thông tin bảo mật.

### 5. Chạy ứng dụng

```powershell
python app.py
```

Sau đó truy cập:

```text
http://127.0.0.1:5000
```

## 🔐 Phân quyền

Hệ thống sử dụng cơ chế phân quyền dựa trên vai trò.

```text
Quản lý
├── Quản lý bồn chứa
├── Quản lý nhiên liệu
├── Quản lý nhân viên
├── Quản lý ca làm việc
├── Tra cứu
├── Thống kê
└── Chức năng AI

Nhân viên ca
├── Xem bồn chứa
├── Xem nhiên liệu
├── Nhập hàng
├── Bán hàng theo ca
├── Theo dõi tồn bồn
└── Xem ca làm việc

Kế toán
├── Tra cứu doanh thu
├── Tra cứu nhập – xuất – tồn
└── Thống kê
```

## 🤖 Trạng thái phát triển

Project đang được phát triển theo từng giai đoạn.

### Đã triển khai

* [x] Đăng nhập
* [x] Phân quyền người dùng
* [x] Quản lý bồn chứa
* [x] Xem bồn chứa cho nhân viên
* [x] Quản lý nhiên liệu
* [x] Xem nhiên liệu cho nhân viên
* [x] Quản lý nhân viên
* [x] Quản lý ca làm việc

### Đang phát triển

* [ ] Ghi nhận nhập hàng
* [ ] Ghi nhận bán hàng theo ca
* [ ] Theo dõi tồn bồn
* [ ] Tra cứu doanh thu
* [ ] Thống kê
* [ ] Sinh báo cáo bằng AI
* [ ] Tóm tắt biến động tồn bồn bằng AI
* [ ] Phân tích và cảnh báo số liệu bất thường bằng AI

## 🎯 Mục tiêu của project

Project hướng tới việc xây dựng một hệ thống quản lý trạm xăng có khả năng:

1. Quản lý tập trung dữ liệu hoạt động của trạm.
2. Phân quyền người dùng theo vai trò.
3. Hỗ trợ theo dõi nhập – xuất – tồn và doanh thu.
4. Giảm thao tác quản lý thủ công.
5. Ứng dụng AI để hỗ trợ tổng hợp và phân tích dữ liệu.

## 📄 Tài liệu

Các tài liệu liên quan đến quá trình phân tích, thiết kế và phát triển hệ thống được lưu trong thư mục [`docs`](./docs).

## 👨‍💻 Tác giả

**Duong Dinh Trung**

GitHub: [duongdinhtrung23112006](https://github.com/duongdinhtrung23112006)
