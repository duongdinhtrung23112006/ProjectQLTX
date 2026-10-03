# YÊU CẦU CHỨC NĂNG

| Mã | Chức năng | Vai trò |
|---|---|---|
| FR01 | Đăng nhập | Quản lý, Nhân viên ca, Kế toán |
| FR02 | Phân quyền | Quản lý |
| FR03 | Quản lý nhiên liệu | Quản lý |
| FR04 | Xem nhiên liệu | Quản lý, Nhân viên ca |
| FR05 | Quản lý bồn chứa | Quản lý |
| FR06 | Xem bồn chứa | Quản lý, Nhân viên ca |
| FR07 | Ghi nhận nhập hàng | Quản lý, Nhân viên ca |
| FR08 | Phê duyệt / từ chối nhập hàng | Quản lý |
| FR09 | Ghi nhận bán hàng theo ngày | Quản lý, Nhân viên ca |
| FR10 | Theo dõi tồn bồn | Quản lý, Nhân viên ca |
| FR11 | Quản lý nhân viên | Quản lý |
| FR12 | Quản lý ca làm việc | Quản lý |
| FR13 | Xem ca làm việc | Quản lý, Nhân viên ca |
| FR14 | Tra cứu doanh thu | Quản lý, Kế toán |
| FR15 | Tra cứu nhập - xuất - tồn | Quản lý, Kế toán |
| FR16 | Thống kê hoạt động | Quản lý, Kế toán |
| FR17 | Sinh báo cáo bằng AI | Quản lý |
| FR18 | Tóm tắt biến động tồn bồn bằng AI | Quản lý |
| FR19 | Cảnh báo số liệu bất thường bằng AI | Quản lý |

---

## FR01 - Đăng nhập

- Người dùng nhập tài khoản và mật khẩu.
- Hệ thống kiểm tra thông tin.
- Đăng nhập thành công tạo phiên làm việc.
- Thông tin không hợp lệ thì từ chối đăng nhập.

## FR02 - Phân quyền

- Xác định vai trò sau khi đăng nhập.
- Chỉ cho phép truy cập chức năng thuộc quyền.
- Từ chối truy cập trái quyền.

## FR03 - Quản lý nhiên liệu

Quản lý có thể:

- Thêm.
- Xem.
- Sửa.
- Cập nhật trạng thái.

## FR04 - Xem nhiên liệu

Người dùng được phép xem:

- Mã nhiên liệu.
- Tên nhiên liệu.
- Đơn vị.
- Đơn giá.
- Trạng thái.

## FR05 - Quản lý bồn chứa

Quản lý có thể:

- Thêm.
- Xem.
- Sửa.
- Cập nhật trạng thái.

Bồn phải tham chiếu đến nhiên liệu đã tồn tại.

## FR06 - Xem bồn chứa

Cho phép xem:

- Mã bồn.
- Tên bồn.
- Nhiên liệu.
- Sức chứa.
- Tồn hiện tại.
- Trạng thái.

## FR07 - Ghi nhận nhập hàng

Ghi nhận:

- Mã nhập.
- Ngày.
- Nhiên liệu.
- Bồn.
- Số lượng.
- Nhân viên.
- Trạng thái.

## FR08 - Phê duyệt / từ chối nhập hàng

Quản lý có thể:

- Xem phiếu chờ duyệt.
- Phê duyệt.
- Từ chối.

Khi duyệt phải kiểm tra sức chứa trước khi cập nhật tồn.

## FR09 - Ghi nhận bán hàng theo ngày

Ghi nhận:

- Ngày bán.
- Nhân viên.
- Nhiên liệu.
- Bồn.
- Số lượng bán.
- Đơn giá.
- Thành tiền.

Không cho phép tồn bồn âm.

## FR10 - Theo dõi tồn bồn

Theo dõi:

- Tồn đầu.
- Tổng nhập.
- Tổng bán.
- Tồn cuối.
- Chênh lệch tồn nếu có dữ liệu đối chiếu.

## FR11 - Quản lý nhân viên

Quản lý có thể:

- Thêm.
- Xem.
- Sửa.
- Cập nhật trạng thái.

## FR12 - Quản lý ca làm việc

Quản lý có thể:

- Tạo ca.
- Xem ca.
- Phân công nhân viên.
- Cập nhật trạng thái.

## FR13 - Xem ca làm việc

Nhân viên có thể xem thông tin ca được phân công.

## FR14 - Tra cứu doanh thu

Cho phép quản lý và kế toán tra cứu doanh thu theo dữ liệu hệ thống.

## FR15 - Tra cứu nhập - xuất - tồn

Cho phép tra cứu số liệu:

- Nhập.
- Bán.
- Tồn.

Theo thời gian, nhiên liệu hoặc bồn khi dữ liệu hỗ trợ.

## FR16 - Thống kê hoạt động

Thống kê:

- Doanh thu.
- Sản lượng bán.
- Tổng nhập.
- Tổng bán.
- Tồn bồn.
- Chênh lệch tồn.

## FR17 - Sinh báo cáo bằng AI

AI tạo báo cáo từ dữ liệu hệ thống được cung cấp.

AI không được tự tạo số liệu.

## FR18 - Tóm tắt biến động tồn bồn bằng AI

AI phân tích dữ liệu nhập - bán - tồn và tạo phần tóm tắt.

## FR19 - Cảnh báo số liệu bất thường bằng AI

AI phát hiện các dấu hiệu bất thường dựa trên dữ liệu được cung cấp.

Kết quả chỉ là cảnh báo hỗ trợ kiểm tra.