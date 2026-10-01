# ProjectQLTX - System Requirements

## 1. Tổng quan

ProjectQLTX là hệ thống quản lý hoạt động của một trạm xăng.

Hệ thống hỗ trợ quản lý dữ liệu vận hành, nhân viên, ca làm việc, bồn chứa, nhiên liệu, nhập hàng, bán hàng, tồn bồn, thống kê và tra cứu.

Hệ thống có ba vai trò chính:

* Quản lý.
* Nhân viên ca.
* Kế toán.

---

## 2. Quản lý tài khoản

### Đăng nhập

Người dùng có thể đăng nhập bằng:

* Tên đăng nhập.
* Mật khẩu.

Hệ thống xác thực thông tin tài khoản trước khi cho phép truy cập các chức năng yêu cầu đăng nhập.

### Đăng xuất

Người dùng có thể đăng xuất khỏi hệ thống.

### Phân quyền

Hệ thống xác định quyền truy cập dựa trên vai trò của tài khoản.

---

## 3. Quản lý bồn chứa

Quản lý có thể:

* Xem danh sách bồn chứa.
* Thêm bồn chứa.
* Xem thông tin chi tiết bồn chứa.
* Sửa thông tin bồn chứa.
* Xóa bồn chứa.

Thông tin bồn chứa gồm:

* Mã bồn.
* Tên bồn.
* Nhiên liệu.
* Sức chứa.
* Tồn hiện tại.
* Trạng thái.

---

## 4. Quản lý nhiên liệu

Hệ thống quản lý thông tin các loại nhiên liệu được sử dụng tại trạm.

---

## 5. Quản lý nhân viên

Quản lý có thể:

* Xem danh sách nhân viên.
* Thêm nhân viên.
* Xem thông tin chi tiết.
* Sửa thông tin.
* Xóa nhân viên.

Thông tin nhân viên gồm:

* Mã nhân viên.
* Họ tên.
* Số điện thoại.
* Địa chỉ.
* Chức vụ.
* Ngày vào làm.
* Trạng thái.

Khi thêm nhân viên, hệ thống đồng thời tạo tài khoản tương ứng cho nhân viên.

---

## 6. Quản lý ca làm việc

Quản lý có thể:

* Xem danh sách ca.
* Thêm ca.
* Xem chi tiết ca.
* Sửa ca.
* Xóa ca.

Thông tin ca gồm:

* Mã ca.
* Tên ca.
* Ngày làm việc.
* Nhân viên.
* Trạng thái.

---

## 7. Bán hàng

Nhân viên ca thực hiện nghiệp vụ bán hàng theo ca.

Hệ thống ghi nhận dữ liệu bán hàng phục vụ cho việc theo dõi doanh thu và tồn bồn.

---

## 8. Nhập hàng

Hệ thống ghi nhận các lần nhập nhiên liệu vào bồn chứa.

Dữ liệu nhập hàng được sử dụng để theo dõi lượng nhập và tồn bồn.

---

## 9. Quản lý tồn bồn

Hệ thống theo dõi số lượng tồn bồn.

Có thể theo dõi:

* Tồn đầu ca.
* Tồn cuối ca.
* Biến động tồn.

---

## 10. Thống kê

Hệ thống hỗ trợ thống kê các số liệu hoạt động của trạm, bao gồm:

* Doanh thu.
* Sản lượng bán.
* Chênh lệch tồn.
* Số liệu nhập - xuất - tồn.

---

## 11. Tra cứu

Người dùng có quyền phù hợp có thể tra cứu các số liệu hoạt động của hệ thống theo thời gian và các tiêu chí phù hợp.

---

## 12. AI hỗ trợ

AI được định hướng hỗ trợ:

* Sinh báo cáo ca dựa trên dữ liệu hệ thống.
* Tóm tắt tình hình biến động tồn bồn.
* Phân tích và cảnh báo các số liệu có dấu hiệu bất thường cần kiểm tra.

AI chỉ có vai trò hỗ trợ tổng hợp và phân tích dữ liệu.

AI không thay thế quyết định của người quản lý.
