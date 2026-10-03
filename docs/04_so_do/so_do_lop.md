# SƠ ĐỒ LỚP

## 1. Mục đích

Sơ đồ lớp mô tả các thực thể dữ liệu chính, thuộc tính và quan hệ giữa chúng trong hệ thống.

## 2. Sơ đồ

```mermaid
classDiagram
    class NhienLieu {
        +int id
        +string ma_nhien_lieu
        +string ten_nhien_lieu
        +string don_vi
        +decimal don_gia
        +string trang_thai
    }

    class BonChua {
        +int id
        +string ma_bon
        +string ten_bon
        +int nhien_lieu_id
        +int suc_chua
        +int ton_hien_tai
        +string trang_thai
    }

    class NhanVien {
        +int id
        +string ma_nv
        +string ho_ten
        +string so_dien_thoai
        +string dia_chi
        +string chuc_vu
        +date ngay_vao_lam
        +string trang_thai
    }

    class TaiKhoan {
        +int id
        +string ten_dang_nhap
        +string mat_khau
        +string vai_tro
        +int nhan_vien_id
    }

    class CaLamViec {
        +int id
        +string ma_ca
        +string ten_ca
        +date ngay_lam_viec
        +int nhan_vien_id
        +string trang_thai
    }

    class NhapHang {
        +int id
        +string ma_nhap
        +date ngay_tao
        +int nhien_lieu_id
        +int bon_id
        +int so_luong
        +int nhan_vien_id
        +string trang_thai
    }

    class BanHang {
        +int id
        +date ngay_ban
        +int nhan_vien_id
        +int nhien_lieu_id
        +int bon_id
        +int so_luong
        +decimal don_gia
        +decimal thanh_tien
    }

    NhienLieu "1" --> "N" BonChua : chứa
    NhienLieu "1" --> "N" NhapHang : được nhập
    BonChua "1" --> "N" NhapHang : nhận
    NhanVien "1" --> "N" NhapHang : lập
    NhanVien "1" --> "1" TaiKhoan : sở hữu
    NhanVien "1" --> "N" CaLamViec : được phân công
    NhanVien "1" --> "N" BanHang : lập
    NhienLieu "1" --> "N" BanHang : được bán
    BonChua "1" --> "N" BanHang : xuất
3. Quan hệ chính
Quan hệ	Ý nghĩa
Nhiên liệu - Bồn chứa	Một nhiên liệu có thể được chứa trong nhiều bồn
Nhiên liệu - Nhập hàng	Một nhiên liệu có nhiều phiếu nhập
Bồn chứa - Nhập hàng	Một bồn có nhiều lần nhận hàng
Nhân viên - Nhập hàng	Một nhân viên có thể lập nhiều phiếu
Nhân viên - Tài khoản	Một nhân viên có tối đa một tài khoản
Nhân viên - Ca làm việc	Một nhân viên có thể được phân công nhiều ca
Nhân viên - Bán hàng	Một nhân viên có thể lập nhiều dữ liệu bán
Nhiên liệu - Bán hàng	Một nhiên liệu có nhiều dữ liệu bán
Bồn chứa - Bán hàng	Một bồn có nhiều dữ liệu xuất bán
4. Quy tắc
Các khóa ngoại phải tham chiếu đến bản ghi tồn tại.
Bồn chứa phải gắn với nhiên liệu đã tồn tại.
BanHang sử dụng dữ liệu bán theo ngày.
BanHang chưa được xem là bảng CSDL chính thức cho đến khi được triển khai.
Khi thay đổi cấu trúc CSDL phải cập nhật đồng thời sơ đồ lớp và từ điển dữ liệu.