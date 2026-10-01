# ProjectQLTX - AI Instructions

## 1. Project overview

ProjectQLTX là hệ thống quản lý trạm xăng được xây dựng bằng Flask và MySQL.

Hệ thống hỗ trợ quản lý:

* Bồn chứa.
* Mặt hàng/nhiên liệu.
* Nhân viên.
* Ca làm việc.
* Tài khoản và phân quyền.
* Nhập hàng.
* Bán hàng.
* Tồn bồn.
* Thống kê và tra cứu.

Hệ thống có tích hợp AI ở giai đoạn phát triển để hỗ trợ phân tích, xây dựng, kiểm thử và cải tiến phần mềm.

---

## 2. Technology stack

### Backend

* Python
* Flask
* Flask Blueprint

### Database

* MySQL
* Database hiện tại: `tram_xang`

### Frontend

* HTML
* Jinja2
* CSS
* JavaScript

### Development

* Visual Studio Code
* Git

---

## 3. Current architecture

Project sử dụng kiến trúc phân chia theo các nhóm:

* `routes/`: xử lý HTTP request và điều hướng chức năng.
* `services/`: xử lý nghiệp vụ dùng chung và kết nối dữ liệu.
* `templates/`: giao diện HTML/Jinja2.
* `static/`: CSS, JavaScript và hình ảnh.
* `tests/`: kiểm thử.
* `docs/`: tài liệu dự án.

Không tự ý thay đổi kiến trúc hiện tại nếu chưa có lý do rõ ràng.

---

## 4. Rules when modifying code

Trước khi sửa code:

1. Đọc và phân tích code liên quan.
2. Xác định module, route, service và template bị ảnh hưởng.
3. Kiểm tra các chức năng hiện tại có phụ thuộc vào phần cần sửa hay không.
4. Nếu yêu cầu chưa rõ hoặc mâu thuẫn với code hiện tại, phải báo lại.

Khi sửa code:

* Không tự ý viết lại toàn bộ module.
* Không tự ý xóa code cũ.
* Không tự ý xóa file.
* Không tự ý đổi tên route.
* Không tự ý đổi tên bảng hoặc cột database.
* Không tự ý thay đổi kiến trúc.
* Không sửa các module không liên quan.
* Ưu tiên tái sử dụng code và service hiện có.
* Chỉ sửa code cũ khi việc sửa là cần thiết cho yêu cầu hiện tại.

Sau khi sửa:

* Kiểm tra lỗi cú pháp.
* Kiểm tra các chức năng liên quan.
* Kiểm tra khả năng ảnh hưởng đến chức năng cũ.
* Báo rõ những file đã thay đổi và lý do thay đổi.

---

## 5. Business requirements

Không tự ý bổ sung yêu cầu nghiệp vụ.

Các yêu cầu nghiệp vụ chính thức được lưu trong:

`docs/requirements.md`

Các quy tắc nghiệp vụ được lưu trong:

`docs/business-rules.md`

Nếu yêu cầu mới chưa có trong tài liệu, phải phân biệt rõ:

* Yêu cầu đã tồn tại.
* Yêu cầu mới được đề xuất.
* Giả định của AI.

Không được biến giả định thành yêu cầu chính thức.

---

## 6. Database rules

Database hiện tại được mô tả trong:

`docs/database.md`

Không tự ý:

* Xóa bảng.
* Đổi tên bảng.
* Đổi tên cột.
* Thay đổi khóa chính/khóa ngoại.
* Thay đổi quan hệ dữ liệu.

Nếu cần thay đổi database, phải nêu:

* Lý do.
* Bảng/cột bị ảnh hưởng.
* Quan hệ bị ảnh hưởng.
* Chức năng bị ảnh hưởng.

---

## 7. Security rules

* Không lưu mật khẩu dạng plaintext.
* Sử dụng cơ chế hash mật khẩu hiện có.
* Không đưa mật khẩu hoặc thông tin nhạy cảm vào tài liệu.
* Không đưa thông tin xác thực thật vào source code nếu không cần thiết.
* Phân quyền phải được kiểm tra ở backend.
* Không coi việc ẩn menu giao diện là cơ chế bảo mật.

---

## 8. Coding conventions

* Ưu tiên tên biến và hàm bằng tiếng Việt theo quy ước hiện tại của project.
* Giữ phong cách code nhất quán với code hiện có.
* Không thay đổi cách tổ chức module chỉ vì sở thích cá nhân.
* Ưu tiên code dễ đọc và dễ bảo trì.
* Không thêm thư viện mới nếu chưa thực sự cần thiết.

---

## 9. AI working principle

AI là công cụ hỗ trợ phát triển phần mềm, không thay thế quyết định của người phát triển.

Khi thực hiện một task lớn:

1. Phân tích yêu cầu.
2. Phân tích code hiện tại.
3. Xác định các file liên quan.
4. Lập kế hoạch thay đổi.
5. Thực hiện thay đổi từng phần.
6. Kiểm thử.
7. Báo cáo kết quả và các vấn đề còn tồn tại.

Không được tự ý mở rộng phạm vi task.

---

## 10. Important principle

Ưu tiên:

> Hiểu hệ thống hiện tại trước khi thay đổi hệ thống.

Nếu code hiện tại đã hoạt động đúng thì giữ nguyên và tích hợp chức năng mới vào nền hiện có.
