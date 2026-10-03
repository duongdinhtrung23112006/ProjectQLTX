# SƠ ĐỒ USE CASE

## 1. Mục đích

Sơ đồ mô tả các chức năng chính của hệ thống và mối quan hệ giữa người dùng với hệ thống.

## 2. Actor

- Quản lý.
- Nhân viên ca.
- Kế toán.

AI không được biểu diễn như một actor nghiệp vụ độc lập.

## 3. Sơ đồ

```mermaid
flowchart LR
    QL[Quản lý]
    NV[Nhân viên ca]
    KT[Kế toán]

    subgraph HT[Hệ thống quản lý trạm xăng]
        UC01((UC01<br/>Đăng nhập))
        UC02((UC02<br/>Phân quyền))

        UC03((UC03<br/>Quản lý bồn chứa))
        UC04((UC04<br/>Xem bồn chứa))
        UC05((UC05<br/>Quản lý nhiên liệu))
        UC06((UC06<br/>Xem nhiên liệu))

        UC07((UC07<br/>Ghi nhận nhập hàng))
        UC08((UC08<br/>Phê duyệt / từ chối nhập hàng))
        UC09((UC09<br/>Ghi nhận bán hàng theo ngày))
        UC10((UC10<br/>Theo dõi tồn bồn))

        UC11((UC11<br/>Quản lý nhân viên))
        UC12((UC12<br/>Quản lý ca làm việc))
        UC13((UC13<br/>Xem ca làm việc))

        UC14((UC14<br/>Tra cứu doanh thu))
        UC15((UC15<br/>Tra cứu nhập - xuất - tồn))
        UC16((UC16<br/>Thống kê hoạt động))

        UC17((UC17<br/>Sinh báo cáo bằng AI))
        UC18((UC18<br/>Tóm tắt biến động tồn bồn))
        UC19((UC19<br/>Cảnh báo số liệu bất thường))
    end

    QL --- UC01
    QL --- UC02
    QL --- UC03
    QL --- UC04
    QL --- UC05
    QL --- UC06
    QL --- UC07
    QL --- UC08
    QL --- UC09
    QL --- UC10
    QL --- UC11
    QL --- UC12
    QL --- UC13
    QL --- UC14
    QL --- UC15
    QL --- UC16
    QL --- UC17
    QL --- UC18
    QL --- UC19

    NV --- UC01
    NV --- UC04
    NV --- UC06
    NV --- UC07
    NV --- UC09
    NV --- UC10
    NV --- UC13

    KT --- UC01
    KT --- UC14
    KT --- UC15
    KT --- UC16
4. Phân nhóm chức năng
Xác thực
├── UC01 Đăng nhập
└── UC02 Phân quyền

Nhiên liệu và bồn
├── UC03 Quản lý bồn chứa
├── UC04 Xem bồn chứa
├── UC05 Quản lý nhiên liệu
└── UC06 Xem nhiên liệu

Nhập và bán
├── UC07 Ghi nhận nhập hàng
├── UC08 Phê duyệt / từ chối nhập hàng
├── UC09 Ghi nhận bán hàng theo ngày
└── UC10 Theo dõi tồn bồn

Nhân sự
├── UC11 Quản lý nhân viên
├── UC12 Quản lý ca làm việc
└── UC13 Xem ca làm việc

Báo cáo và thống kê
├── UC14 Tra cứu doanh thu
├── UC15 Tra cứu nhập - xuất - tồn
└── UC16 Thống kê hoạt động

AI
├── UC17 Sinh báo cáo bằng AI
├── UC18 Tóm tắt biến động tồn bồn
└── UC19 Cảnh báo số liệu bất thường
5. Quy tắc
Mỗi actor chỉ liên kết với các UC mà vai trò đó được phép thực hiện.
UC phải phù hợp với yêu cầu chức năng và ma trận phân quyền.
Khi thêm hoặc thay đổi UC phải cập nhật danh_sach_use_case.md, user_story.md và ma_tran_truy_vet.md.