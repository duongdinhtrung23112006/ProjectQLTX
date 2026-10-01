# ProjectQLTX - Architecture

## 1. Tổng quan

ProjectQLTX hiện sử dụng kiến trúc Flask được tổ chức theo các nhóm:

```text
Browser
   ↓
Routes / Blueprint
   ↓
Services
   ↓
MySQL
```

Giao diện:

```text
Routes
   ↓
Templates
   ↓
Static CSS / JavaScript / Images
```

---

## 2. `app.py`

`app.py` là điểm khởi động của ứng dụng Flask.

Nhiệm vụ chính:

* Khởi tạo Flask application.
* Cấu hình ứng dụng.
* Đăng ký các Blueprint.
* Khởi động server.

Không đưa toàn bộ nghiệp vụ của hệ thống vào `app.py`.

---

## 3. `routes/`

`routes/` chứa các Flask Blueprint và xử lý HTTP request.

### `routes/auth/`

Chứa các chức năng xác thực.

Hiện có:

* `dang_nhap.py`

### `routes/quanly/`

Chứa các chức năng dành cho quản lý.

Hiện có:

* `bon_chua.py`
* `ca_lam_viec.py`
* `nhan_vien.py`
* `nhien_lieu.py`
* `trang_chu.py`

### `routes/nhanvien/`

Dành cho các chức năng của nhân viên ca.

### `routes/ketoan/`

Dành cho các chức năng của kế toán.

---

## 4. `services/`

Chứa các logic dùng chung và nghiệp vụ cần tách khỏi route.

Hiện có:

### `database.py`

Quản lý kết nối MySQL.

### `auth_service.py`

Chứa logic hỗ trợ xác thực và bảo vệ route.

### `quan_ly_ca.py`

Xử lý các nghiệp vụ liên quan đến ca làm việc.

---

## 5. `templates/`

Chứa giao diện HTML/Jinja2.

Cấu trúc template được tổ chức theo nhóm chức năng:

* `auth/`
* `quanly/`
* `nhanvien/`
* `ketoan/`

---

## 6. `static/`

Chứa tài nguyên frontend:

* CSS.
* JavaScript.
* Images.

CSS được tổ chức theo từng nhóm chức năng để hạn chế ảnh hưởng lẫn nhau.

---

## 7. `tests/`

Chứa các bài kiểm thử của hệ thống.

Các chức năng mới nên được kiểm tra sau khi triển khai.

---

## 8. `docs/`

Chứa tài liệu mô tả dự án:

* `requirements.md`: yêu cầu.
* `business-rules.md`: luật nghiệp vụ.
* `architecture.md`: kiến trúc.
* `database.md`: cơ sở dữ liệu.
* `prompts/`: các prompt/task dành cho AI.

---

## 9. Nguyên tắc mở rộng

Khi thêm chức năng:

1. Xác định nhóm chức năng.
2. Thêm hoặc cập nhật route phù hợp.
3. Tách nghiệp vụ dùng chung vào service khi cần.
4. Thêm template.
5. Thêm CSS/JavaScript nếu cần.
6. Cập nhật tài liệu.
7. Kiểm thử chức năng.

Không tạo module mới nếu chức năng có thể tích hợp hợp lý vào module hiện có.
