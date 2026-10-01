# ProjectQLTX - Database

## 1. Thông tin chung

DBMS:

`MySQL`

Database:

`tram_xang`

---

## 2. Bảng `bon_chua`

Lưu thông tin các bồn chứa.

| Cột          | Kiểu         | Ràng buộc          | Ý nghĩa         |
| ------------ | ------------ | ------------------ | --------------- |
| id           | INT          | PK, AUTO_INCREMENT | ID bồn          |
| ma_bon       | VARCHAR(20)  | NOT NULL, UNIQUE   | Mã bồn          |
| ten_bon      | VARCHAR(100) | NOT NULL           | Tên bồn         |
| nhien_lieu   | VARCHAR(50)  | NOT NULL           | Loại nhiên liệu |
| suc_chua     | INT          | NOT NULL           | Sức chứa        |
| ton_hien_tai | INT          | NOT NULL           | Tồn hiện tại    |
| trang_thai   | VARCHAR(30)  | NOT NULL           | Trạng thái      |

---

## 3. Bảng `nhan_vien`

Lưu thông tin nhân viên.

| Cột           | Kiểu         | Ràng buộc          | Ý nghĩa       |
| ------------- | ------------ | ------------------ | ------------- |
| id            | INT          | PK, AUTO_INCREMENT | ID nhân viên  |
| ma_nv         | VARCHAR(20)  | NOT NULL, UNIQUE   | Mã nhân viên  |
| ho_ten        | VARCHAR(100) | NOT NULL           | Họ tên        |
| so_dien_thoai | VARCHAR(20)  | NULL               | Số điện thoại |
| dia_chi       | VARCHAR(255) | NULL               | Địa chỉ       |
| chuc_vu       | VARCHAR(50)  | NOT NULL           | Chức vụ       |
| ngay_vao_lam  | DATE         | NULL               | Ngày vào làm  |
| trang_thai    | VARCHAR(30)  | NOT NULL           | Trạng thái    |

---

## 4. Bảng `ca_lam_viec`

Lưu thông tin phân công ca.

| Cột           | Kiểu         | Ràng buộc          | Ý nghĩa    |
| ------------- | ------------ | ------------------ | ---------- |
| id            | INT          | PK, AUTO_INCREMENT | ID ca      |
| ma_ca         | VARCHAR(20)  | NOT NULL           | Mã ca      |
| ten_ca        | VARCHAR(100) | NOT NULL           | Tên ca     |
| ngay_lam_viec | DATE         | NOT NULL           | Ngày làm   |
| nhan_vien_id  | INT          | NOT NULL, FK       | Nhân viên  |
| trang_thai    | VARCHAR(30)  | NOT NULL           | Trạng thái |

Foreign key:

```text
ca_lam_viec.nhan_vien_id
        ↓
nhan_vien.id
```

---

## 5. Bảng `tai_khoan`

Lưu tài khoản đăng nhập.

| Cột           | Kiểu         | Ràng buộc            | Ý nghĩa          |
| ------------- | ------------ | -------------------- | ---------------- |
| id            | INT          | PK, AUTO_INCREMENT   | ID tài khoản     |
| ten_dang_nhap | VARCHAR(50)  | NOT NULL, UNIQUE     | Tên đăng nhập    |
| mat_khau      | VARCHAR(255) | NOT NULL             | Mật khẩu đã hash |
| vai_tro       | VARCHAR(30)  | NOT NULL             | Vai trò          |
| nhan_vien_id  | INT          | NOT NULL, UNIQUE, FK | Nhân viên        |

Foreign key:

```text
tai_khoan.nhan_vien_id
        ↓
nhan_vien.id
```

Quan hệ:

```text
nhan_vien 1 ───────── 1 tai_khoan
```

---

## 6. Quan hệ hiện tại

```text
nhan_vien
    │
    ├────────────── 1 : 1 ────────────── tai_khoan
    │
    └────────────── 1 : N ────────────── ca_lam_viec
```

---

## 7. Quy tắc database

* Không tự ý đổi tên bảng.
* Không tự ý đổi tên cột.
* Không tự ý xóa khóa ngoại.
* Không tự ý thay đổi kiểu dữ liệu.
* Khi thay đổi database phải đánh giá ảnh hưởng đến backend và frontend.
* Dữ liệu nhạy cảm không được ghi trực tiếp vào tài liệu.

---

## 8. Nguyên tắc truy cập database

Kết nối database hiện được quản lý thông qua:

`services/database.py`

Các route không nên tự tạo nhiều cách kết nối database khác nhau nếu không có lý do rõ ràng.
