# ProjectQLTX - Business Rules

## 1. Vai trò người dùng

Hệ thống có ba vai trò:

* `Quản lý`
* `Nhân viên ca`
* `Kế toán`

Quyền truy cập chức năng phải được kiểm tra ở backend.

---

## 2. Tài khoản

Mỗi tài khoản có:

* Tên đăng nhập.
* Mật khẩu đã được hash.
* Vai trò.
* Nhân viên tương ứng.

Một nhân viên chỉ có một tài khoản.

Tên đăng nhập phải là duy nhất.

---

## 3. Thêm nhân viên

Khi thêm nhân viên:

1. Kiểm tra dữ liệu đầu vào.
2. Tạo bản ghi trong `nhan_vien`.
3. Lấy `nhan_vien_id`.
4. Hash mật khẩu.
5. Tạo tài khoản trong `tai_khoan`.
6. Nếu cả hai thành công thì `COMMIT`.
7. Nếu xảy ra lỗi thì `ROLLBACK`.

Không được để xảy ra trường hợp có nhân viên nhưng không có tài khoản tương ứng do lỗi giữa giao dịch.

---

## 4. Xóa nhân viên

Khi xóa nhân viên:

1. Xóa các ca làm việc liên quan.
2. Xóa tài khoản liên quan.
3. Xóa nhân viên.
4. `COMMIT` nếu tất cả thành công.
5. `ROLLBACK` nếu xảy ra lỗi.

---

## 5. Ca làm việc

Mỗi bản ghi trong `ca_lam_viec` đại diện cho việc một nhân viên được phân công một ca vào một ngày.

Các loại ca hiện tại:

* Sáng: 06:00 - 12:00.
* Chiều: 12:00 - 18:00.
* Tối: 18:00 - 23:59.

Một ca được xem là trùng khi có cùng:

`ten_ca + ngay_lam_viec`

Quy tắc này không phụ thuộc vào nhân viên.

---

## 6. Sửa ca làm việc

Khi sửa ca:

* Nhân viên hiện tại được hiển thị.
* Không cho phép thay đổi nhân viên.
* Không cần cập nhật lại `nhan_vien_id`.

---

## 7. Trạng thái ca

Các trạng thái hiện tại:

* `Đang hoạt động`
* `Đã đóng`

---

## 8. Đăng nhập

Khi đăng nhập thành công, hệ thống lưu thông tin cần thiết vào session, bao gồm:

* ID tài khoản.
* ID nhân viên.
* Vai trò.
* Tên đăng nhập.

Khi đăng xuất, session được xóa.

Thông báo lỗi đăng nhập không được tiết lộ riêng biệt rằng tên đăng nhập có tồn tại hay không.

---

## 9. Phân quyền

Việc ẩn hoặc hiện menu trên giao diện chỉ có tác dụng hỗ trợ trải nghiệm người dùng.

Cơ chế bảo vệ thực sự phải được thực hiện ở backend.

Người dùng không có quyền không được thực hiện chức năng chỉ bằng cách truy cập trực tiếp URL.

---

## 10. Nguyên tắc dữ liệu

Không tự ý tạo dữ liệu nghiệp vụ không có trong yêu cầu.

Các số liệu doanh thu, sản lượng, tồn bồn và nhập hàng phải lấy từ dữ liệu thực tế trong hệ thống.

AI không được tự tạo số liệu để đưa vào báo cáo.

---

## 11. AI

Kết quả AI có tính chất hỗ trợ.

AI có thể:

* Tổng hợp.
* Tóm tắt.
* Phân tích.
* Cảnh báo dữ liệu cần kiểm tra.

AI không tự động thay thế quyết định của người quản lý.

Khi dữ liệu không đủ để đưa ra kết luận, hệ thống phải thể hiện rõ giới hạn của dữ liệu.
