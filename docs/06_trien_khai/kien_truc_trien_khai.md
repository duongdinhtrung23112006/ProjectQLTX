# Kiến trúc triển khai

## 1. Mục đích

Mô tả cách các thành phần của hệ thống được tổ chức khi triển khai và cách chúng giao tiếp với nhau.

Kiến trúc triển khai phải phù hợp với kiến trúc hệ thống và công nghệ thực tế của dự án.

---

## 2. Thành phần triển khai

Hệ thống gồm các thành phần chính:

- Người dùng.
- Trình duyệt web.
- Ứng dụng Flask.
- Các route xử lý nghiệp vụ.
- Các service xử lý nghiệp vụ và kết nối dữ liệu.
- Cơ sở dữ liệu MySQL.
- Thành phần AI.
- Tệp cấu hình môi trường.

---

## 3. Luồng giao tiếp

Luồng xử lý cơ bản:

`Người dùng → Trình duyệt → Flask → Route → Service → MySQL`

Đối với chức năng AI:

`Người dùng → Flask → Route → Service → Dữ liệu nghiệp vụ → AI Service → Kết quả → Người dùng`

AI sử dụng dữ liệu do hệ thống cung cấp và không thay thế cơ sở dữ liệu nguồn.

---

## 4. Ứng dụng Flask

Ứng dụng Flask là thành phần xử lý chính của hệ thống.

Nhiệm vụ:

- Tiếp nhận HTTP request.
- Xác thực người dùng.
- Kiểm tra quyền.
- Gọi route tương ứng.
- Gọi service xử lý nghiệp vụ.
- Đọc và ghi dữ liệu.
- Trả kết quả về giao diện.

Tệp khởi động hiện tại:

`app.py`

---

## 5. Route

Các route được tổ chức theo nhóm chức năng và vai trò:

- `routes/auth/`
- `routes/quanly/`
- `routes/nhanvien/`
- `routes/ketoan/`

Route chịu trách nhiệm tiếp nhận yêu cầu và điều phối xử lý, không nên chứa toàn bộ logic nghiệp vụ phức tạp.

---

## 6. Service

Thư mục:

`services/`

Các service chịu trách nhiệm xử lý logic dùng chung hoặc nghiệp vụ.

Ví dụ hiện tại:

- `database.py`: kết nối MySQL.
- `auth_service.py`: xác thực và kiểm tra vai trò.
- `quan_ly_ca.py`: xử lý nghiệp vụ liên quan đến ca.

Khi hệ thống phát triển, logic nghiệp vụ phức tạp nên được tách khỏi route và đưa vào service phù hợp.

---

## 7. Cơ sở dữ liệu

Hệ thống sử dụng MySQL với cơ sở dữ liệu:

`tram_xang`

Cơ sở dữ liệu lưu dữ liệu nghiệp vụ như:

- Tài khoản.
- Nhân viên.
- Ca làm việc.
- Nhiên liệu.
- Bồn chứa.
- Nhập hàng.
- Các dữ liệu bán hàng khi chức năng được triển khai.

Thông tin kết nối không được ghi trực tiếp trong mã nguồn.

Các biến môi trường hiện tại:

- `DB_HOST`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`

---

## 8. Giao diện

Giao diện sử dụng:

- HTML.
- Jinja Template.
- CSS.
- JavaScript.

Thư mục:

`templates/`

và:

`static/`

Giao diện được tổ chức theo các khu vực:

- `auth/`
- `quanly/`
- `nhanvien/`
- `ketoan/`

---

## 9. Thành phần AI

AI được tích hợp như một thành phần hỗ trợ phân tích.

AI nhận dữ liệu đã được hệ thống chuẩn bị và có thể thực hiện:

- Sinh báo cáo.
- Tóm tắt biến động tồn bồn.
- Phân tích và cảnh báo số liệu bất thường.

AI không được phép:

- Tự sửa dữ liệu CSDL.
- Tự phê duyệt nhập hàng.
- Tự thay đổi tồn bồn.
- Tự thực hiện quyết định nghiệp vụ.

---

## 10. Cấu hình môi trường

Môi trường triển khai phải tách khỏi mã nguồn.

Các thông tin như:

- Mật khẩu CSDL.
- API key.
- Secret key.
- Thông tin kết nối dịch vụ.

phải được quản lý bằng biến môi trường hoặc cơ chế quản lý secret phù hợp.

Không commit thông tin bí mật vào Git.

---

## 11. Môi trường triển khai

Có thể triển khai theo các môi trường:

### Development

Dùng để phát triển và kiểm thử.

### Testing

Dùng để kiểm thử phiên bản trước khi đưa vào sử dụng.

### Production

Dùng cho hệ thống thực tế.

Dữ liệu và cấu hình giữa các môi trường phải được quản lý riêng.

---

## 12. Khả năng mở rộng

Kiến trúc cần cho phép mở rộng:

- Thêm route.
- Thêm service.
- Thêm chức năng nghiệp vụ.
- Thêm chức năng AI.
- Thay đổi hoặc mở rộng cơ sở dữ liệu.
- Đóng gói bằng Docker khi cần.

Việc mở rộng không được phá vỡ các chức năng và dữ liệu hiện có.

---

## 13. Giám sát và xử lý sự cố

Môi trường triển khai cần có khả năng theo dõi:

- Trạng thái ứng dụng.
- Kết nối CSDL.
- Lỗi ứng dụng.
- Lỗi AI.
- Tài nguyên hệ thống.
- Các thao tác quan trọng.

Khi xảy ra sự cố phải có khả năng xác định thành phần gây lỗi và khôi phục hệ thống.

---

## 14. Nguyên tắc triển khai

- Cấu hình tách khỏi mã nguồn.
- Không đưa secret vào Git.
- Phân tách môi trường phát triển, kiểm thử và thực tế.
- Dữ liệu CSDL phải được sao lưu.
- Thay đổi triển khai phải có khả năng quay lui.
- Chỉ triển khai phiên bản đã được kiểm thử.
- Mọi thay đổi quan trọng phải có khả năng truy vết về mã nguồn và tài liệu liên quan.