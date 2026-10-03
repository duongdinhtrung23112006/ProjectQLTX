# TỪ ĐIỂN DỮ LIỆU

## 1. nhien_lieu

| Trường | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
|---|---|---|---|
| id | INT | PK, AUTO_INCREMENT | Mã định danh |
| ma_nhien_lieu | VARCHAR(20) | NOT NULL, UNIQUE | Mã nhiên liệu |
| ten_nhien_lieu | VARCHAR(100) | NOT NULL | Tên nhiên liệu |
| don_vi | VARCHAR(20) | NOT NULL | Đơn vị tính |
| don_gia | DECIMAL(12,2) | NOT NULL | Đơn giá |
| trang_thai | VARCHAR(30) | NOT NULL | Trạng thái |

## 2. bon_chua

| Trường | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
|---|---|---|---|
| id | INT | PK, AUTO_INCREMENT | Mã định danh |
| ma_bon | VARCHAR(20) | NOT NULL, UNIQUE | Mã bồn |
| ten_bon | VARCHAR(100) | NOT NULL | Tên bồn |
| nhien_lieu_id | INT | FK, NOT NULL | Nhiên liệu chứa |
| suc_chua | INT | NOT NULL | Sức chứa |
| ton_hien_tai | INT | NOT NULL | Tồn hiện tại |
| trang_thai | VARCHAR(30) | NOT NULL | Trạng thái |

Quan hệ: `bon_chua.nhien_lieu_id → nhien_lieu.id`

## 3. nhan_vien

| Trường | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
|---|---|---|---|
| id | INT | PK, AUTO_INCREMENT | Mã định danh |
| ma_nv | VARCHAR(20) | NOT NULL, UNIQUE | Mã nhân viên |
| ho_ten | VARCHAR(100) | NOT NULL | Họ tên |
| so_dien_thoai | VARCHAR(20) | NULL | Số điện thoại |
| dia_chi | VARCHAR(255) | NULL | Địa chỉ |
| chuc_vu | VARCHAR(50) | NOT NULL | Chức vụ |
| ngay_vao_lam | DATE | NULL | Ngày vào làm |
| trang_thai | VARCHAR(30) | NOT NULL | Trạng thái |

## 4. tai_khoan

| Trường | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
|---|---|---|---|
| id | INT | PK, AUTO_INCREMENT | Mã định danh |
| ten_dang_nhap | VARCHAR(50) | NOT NULL, UNIQUE | Tên đăng nhập |
| mat_khau | VARCHAR(255) | NOT NULL | Mật khẩu đã được xử lý bảo mật |
| vai_tro | VARCHAR(30) | NOT NULL | Vai trò |
| nhan_vien_id | INT | FK, UNIQUE, NOT NULL | Nhân viên sở hữu tài khoản |

Quan hệ: `tai_khoan.nhan_vien_id → nhan_vien.id`

Vai trò hiện tại:

- Quản lý.
- Nhân viên ca.
- Kế toán.

## 5. ca_lam_viec

| Trường | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
|---|---|---|---|
| id | INT | PK, AUTO_INCREMENT | Mã định danh |
| ma_ca | VARCHAR(20) | NOT NULL | Mã ca |
| ten_ca | VARCHAR(100) | NOT NULL | Tên ca |
| ngay_lam_viec | DATE | NOT NULL | Ngày làm việc |
| nhan_vien_id | INT | FK, NOT NULL | Nhân viên được phân công |
| trang_thai | VARCHAR(30) | NOT NULL | Trạng thái |

Quan hệ: `ca_lam_viec.nhan_vien_id → nhan_vien.id`

## 6. nhap_hang

| Trường | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
|---|---|---|---|
| id | INT | PK, AUTO_INCREMENT | Mã định danh |
| ma_nhap | VARCHAR(20) | NOT NULL, UNIQUE | Mã phiếu nhập |
| ngay_tao | DATE | NOT NULL | Ngày tạo phiếu |
| nhien_lieu_id | INT | FK, NOT NULL | Nhiên liệu nhập |
| bon_id | INT | FK, NOT NULL | Bồn nhận nhiên liệu |
| so_luong | INT | NOT NULL | Số lượng nhập |
| nhan_vien_id | INT | FK, NOT NULL | Nhân viên lập phiếu |
| trang_thai | VARCHAR(30) | NOT NULL | Trạng thái phiếu |

Quan hệ:

```text
nhap_hang.nhien_lieu_id → nhien_lieu.id
nhap_hang.bon_id         → bon_chua.id
nhap_hang.nhan_vien_id   → nhan_vien.id

Trạng thái nghiệp vụ hiện tại:

Chờ duyệt.
Đã duyệt.
Từ chối.
7. Dữ liệu bán hàng

Dữ liệu bán hàng dự kiến lưu:

Trường	Ý nghĩa
Ngày bán	Ngày phát sinh bán hàng
Nhân viên	Người lập dữ liệu
Nhiên liệu	Loại nhiên liệu bán
Bồn chứa	Bồn xuất nhiên liệu
Số lượng bán	Lượng nhiên liệu bán
Đơn giá	Giá bán
Thành tiền	Giá trị bán

Bảng bán hàng chính thức sẽ được cập nhật vào từ điển dữ liệu khi được triển khai trong CSDL.

8. Quy tắc dữ liệu quan trọng
PK xác định duy nhất mỗi bản ghi.
FK đảm bảo quan hệ giữa các bảng.
Mã nhiên liệu, mã bồn, mã nhân viên và mã phiếu nhập không được trùng.
ton_hien_tai không được âm.
ton_hien_tai không được vượt suc_chua.
Số lượng nhập và bán không được âm.
Dữ liệu AI không thay thế dữ liệu nghiệp vụ trong CSDL.