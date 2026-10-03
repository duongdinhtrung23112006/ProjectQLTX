# Sơ đồ thực thể liên kết (ERD)

## 1. Mục đích

Sơ đồ ERD mô tả các thực thể dữ liệu chính, thuộc tính và quan hệ giữa các thực thể trong hệ thống quản lý trạm xăng.

ERD gồm:
- Dữ liệu tài khoản và phân quyền.
- Dữ liệu nhân viên và ca làm việc.
- Dữ liệu nhiên liệu và bồn chứa.
- Dữ liệu nhập hàng.
- Dữ liệu bán hàng.
- Dữ liệu tồn kho.
- Dữ liệu phục vụ tra cứu và thống kê.

Các chức năng **tra cứu** và **thống kê** chủ yếu được thực hiện bằng truy vấn và phép tính trên dữ liệu nghiệp vụ, không tạo bảng riêng nếu không có nhu cầu lưu kết quả.

---

## 2. ERD tổng thể

```mermaid
erDiagram

    VAI_TRO ||--o{ TAI_KHOAN : "phan_quyen"
    NHAN_VIEN ||--o| TAI_KHOAN : "so_huu"

    NHAN_VIEN ||--o{ CA_LAM_VIEC : "duoc_phan_cong"

    NHIEN_LIEU ||--o{ BON_CHUA : "duoc_chua"

    NHIEN_LIEU ||--o{ NHAP_HANG : "duoc_nhap"
    BON_CHUA ||--o{ NHAP_HANG : "nhan_hang"
    NHAN_VIEN ||--o{ NHAP_HANG : "lap"

    NHIEN_LIEU ||--o{ BAN_HANG : "duoc_ban"
    BON_CHUA ||--o{ BAN_HANG : "xuat_hang"
    NHAN_VIEN ||--o{ BAN_HANG : "lap"

    BON_CHUA ||--o{ TON_BON : "co_ton"
    NHIEN_LIEU ||--o{ TON_BON : "theo_doi"

    VAI_TRO {
        INT id PK
        VARCHAR ma_vai_tro UK
        VARCHAR ten_vai_tro
        VARCHAR mo_ta
        VARCHAR trang_thai
    }

    TAI_KHOAN {
        INT id PK
        VARCHAR ten_dang_nhap UK
        VARCHAR mat_khau
        INT vai_tro_id FK
        INT nhan_vien_id FK
        VARCHAR trang_thai
    }

    NHAN_VIEN {
        INT id PK
        VARCHAR ma_nv UK
        VARCHAR ho_ten
        VARCHAR so_dien_thoai
        VARCHAR dia_chi
        VARCHAR chuc_vu
        DATE ngay_vao_lam
        VARCHAR trang_thai
    }

    CA_LAM_VIEC {
        INT id PK
        VARCHAR ma_ca
        VARCHAR ten_ca
        DATE ngay_lam_viec
        INT nhan_vien_id FK
        VARCHAR trang_thai
    }

    NHIEN_LIEU {
        INT id PK
        VARCHAR ma_nhien_lieu UK
        VARCHAR ten_nhien_lieu
        VARCHAR don_vi
        DECIMAL don_gia
        VARCHAR trang_thai
    }

    BON_CHUA {
        INT id PK
        VARCHAR ma_bon UK
        VARCHAR ten_bon
        INT nhien_lieu_id FK
        INT suc_chua
        INT ton_hien_tai
        VARCHAR trang_thai
    }

    NHAP_HANG {
        INT id PK
        VARCHAR ma_nhap UK
        DATE ngay_tao
        INT nhien_lieu_id FK
        INT bon_id FK
        INT so_luong
        INT nhan_vien_id FK
        VARCHAR trang_thai
    }

    BAN_HANG {
        INT id PK
        VARCHAR ma_ban UK
        DATE ngay_ban
        INT nhien_lieu_id FK
        INT bon_id FK
        INT so_luong
        DECIMAL don_gia
        DECIMAL thanh_tien
        INT nhan_vien_id FK
    }

    TON_BON {
        INT id PK
        DATE ngay
        INT bon_id FK
        INT nhien_lieu_id FK
        INT ton_dau
        INT tong_nhap
        INT tong_ban
        INT ton_cuoi
        INT chenh_lech
    }
3. Ý nghĩa các thực thể
3.1. VAI_TRO

Lưu các vai trò của người sử dụng hệ thống.

Các vai trò chính:

Quản lý.
Nhân viên ca.
Kế toán.

Một vai trò có thể được cấp cho nhiều tài khoản.

3.2. TAI_KHOAN

Lưu thông tin đăng nhập và vai trò của người sử dụng.

Tài khoản liên kết với:

Một nhân viên.
Một vai trò.

Không lưu thông tin nghiệp vụ của trạm xăng trong bảng tài khoản.

3.3. NHAN_VIEN

Lưu thông tin nhân viên làm việc tại trạm.

Nhân viên có thể:

Có một tài khoản.
Được phân công nhiều ca.
Lập nhiều phiếu nhập hàng.
Lập nhiều bản ghi bán hàng.
3.4. CA_LAM_VIEC

Lưu thông tin phân công ca làm việc.

Ca làm việc được gắn với nhân viên và ngày làm việc.

Lưu ý:

Ca làm việc dùng để quản lý nhân sự và lịch làm việc, không dùng làm đơn vị ghi nhận doanh số bán hàng.

Doanh số được ghi nhận theo ngày.

3.5. NHIEN_LIEU

Lưu danh mục nhiên liệu.

Ví dụ:

Xăng.
Dầu.

Mỗi loại nhiên liệu có thể được chứa trong nhiều bồn và xuất hiện trong nhiều giao dịch nhập/bán.

3.6. BON_CHUA

Lưu thông tin bồn chứa.

Mỗi bồn:

Chỉ chứa một loại nhiên liệu.
Có sức chứa tối đa.
Có lượng tồn hiện tại.
Có trạng thái hoạt động.

Ràng buộc:

0 <= ton_hien_tai <= suc_chua
3.7. NHAP_HANG

Lưu các lần nhập nhiên liệu vào bồn.

Trạng thái:

Chờ duyệt
Đã duyệt
Từ chối

Chỉ phiếu Đã duyệt mới làm tăng tồn bồn.

Công thức:

Tổng nhập trong ngày
= SUM(so_luong của các phiếu nhập đã duyệt trong ngày)
3.8. BAN_HANG

Lưu dữ liệu bán nhiên liệu theo ngày.

Một bản ghi bán hàng gồm:

Ngày bán.
Nhiên liệu.
Bồn xuất.
Số lượng.
Đơn giá.
Thành tiền.
Nhân viên lập.

Công thức:

Thành tiền
= Số lượng bán × Đơn giá

Doanh thu:

Doanh thu trong kỳ
= SUM(Thành tiền)

Số lượng bán:

Tổng bán trong kỳ
= SUM(Số lượng bán)

Bảng BAN_HANG là bảng nghiệp vụ cần triển khai để hoàn thiện chức năng bán hàng.

3.9. TON_BON

Lưu số liệu tồn bồn phục vụ theo dõi, tra cứu và thống kê.

Công thức:

Tồn cuối
= Tồn đầu + Tổng nhập - Tổng bán

Trong đó:

Tổng nhập
= Tổng số lượng phiếu nhập đã duyệt

Tổng bán
= Tổng số lượng bán trong ngày

Nếu có số liệu kiểm kê thực tế:

Chênh lệch tồn
= Tồn thực tế - Tồn theo hệ thống
4. Dữ liệu phục vụ tra cứu và thống kê

Hệ thống không tạo bắt buộc các bảng TRA_CUU hoặc THONG_KE.

Các chức năng này được thực hiện bằng truy vấn trên dữ liệu nghiệp vụ.

Tra cứu doanh thu

Nguồn:

BAN_HANG

Tính:

Doanh thu = SUM(so_luong × don_gia)

Có thể lọc theo:

Ngày.
Khoảng thời gian.
Nhiên liệu.
Bồn.
Nhân viên.
Tra cứu nhập - xuất - tồn

Nguồn:

NHAP_HANG
BAN_HANG
TON_BON
BON_CHUA

Tính:

Tồn cuối = Tồn đầu + Tổng nhập - Tổng bán
Thống kê hoạt động

Các chỉ tiêu chính:

Tổng doanh thu
= SUM(thanh_tien)

Tổng số lượng bán
= SUM(so_luong bán)

Tổng số lượng nhập
= SUM(so_luong của phiếu nhập đã duyệt)

Tồn cuối
= Tồn đầu + Tổng nhập - Tổng bán

Các kết quả thống kê có thể được nhóm theo:

Ngày.
Nhiên liệu.
Bồn chứa.
Nhân viên.
5. Dữ liệu phục vụ AI

AI không phải là một thực thể nghiệp vụ trong ERD.

AI nhận dữ liệu đã được hệ thống truy vấn và tính toán từ:

NHIEN_LIEU
BON_CHUA
NHAP_HANG
BAN_HANG
TON_BON
NHAN_VIEN

Luồng xử lý:
flowchart LR
    DB[(CSDL)]
    DB --> DATA[Dữ liệu nghiệp vụ]
    DATA --> CALC[Tính toán thống kê]
    CALC --> AI[AI phân tích]
    AI --> REPORT[Báo cáo / Tóm tắt / Cảnh báo]
    REPORT --> USER[Người dùng kiểm tra]
AI không được:

Tự tạo số liệu.
Tự sửa tồn bồn.
Tự duyệt nhập hàng.
Tự từ chối giao dịch.
Tự thay đổi dữ liệu nghiệp vụ.
Thay thế quyết định của người quản lý.
6. Trạng thái triển khai
Đã có trong CSDL hiện tại
nhien_lieu
bon_chua
nhap_hang
nhan_vien
ca_lam_viec
tai_khoan
Cần hoàn thiện / mở rộng
vai_tro: có thể tách thành bảng riêng để chuẩn hóa phân quyền thay cho lưu trực tiếp chuỗi vai trò trong tai_khoan.
ban_hang: cần triển khai để hoàn thiện nghiệp vụ bán hàng.
ton_bon: cần triển khai nếu hệ thống cần lưu lịch sử tồn theo ngày.