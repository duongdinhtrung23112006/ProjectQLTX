# THIẾT KẾ API

## 1. Tổng quan

Backend sử dụng Flask để tiếp nhận request từ giao diện Web, kiểm tra xác thực và phân quyền, xử lý nghiệp vụ thông qua service và truy cập MySQL.

```text
Client
  ↓
Flask Route
  ↓
Authentication / Authorization
  ↓
Business Service
  ↓
MySQL
  ↓
Response
2. Nguyên tắc thiết kế
Mỗi nhóm chức năng được tổ chức thành Blueprint/route phù hợp.
Route không chứa quá nhiều logic nghiệp vụ.
Chức năng yêu cầu đăng nhập phải kiểm tra session.
Chức năng giới hạn vai trò phải kiểm tra quyền.
Dữ liệu đầu vào phải được kiểm tra trước khi xử lý.
Lỗi phải được xử lý rõ ràng.
Không trả về thông tin nhạy cảm.
Thay đổi dữ liệu quan trọng phải đảm bảo tính nhất quán.
3. Xác thực
Phương thức	Route	Chức năng
GET/POST	/dang-nhap	Hiển thị và xử lý đăng nhập
GET	/dang-xuat	Đăng xuất

Sau khi đăng nhập thành công, session lưu thông tin cần thiết để xác định người dùng và vai trò.

4. Quản lý nhiên liệu
Phương thức	Route	Chức năng
GET	/quanly/nhien-lieu	Danh sách nhiên liệu
POST	/quanly/nhien-lieu/...	Thêm hoặc cập nhật nhiên liệu

Chỉ Quản lý được thực hiện các thao tác thay đổi dữ liệu nhiên liệu.

5. Quản lý bồn chứa
Phương thức	Route	Chức năng
GET	/quanly/bon-chua	Danh sách bồn
POST	/quanly/bon-chua/...	Thêm hoặc cập nhật bồn
GET	/nhanvien/bon-chua	Nhân viên xem bồn

Khi tạo hoặc cập nhật bồn, nhien_lieu_id phải tham chiếu đến nhiên liệu tồn tại.

6. Nhập hàng

Các route nghiệp vụ hiện tại:

Phương thức	Route	Chức năng
GET	/quanly/nhap-hang	Danh sách phiếu
GET	/quanly/nhap-hang/xem/<id>	Xem phiếu
GET/POST	/quanly/nhap-hang/duyet/<id>	Phê duyệt
GET/POST	/quanly/nhap-hang/tu-choi/<id>	Từ chối
GET/POST	/quanly/nhap-hang/xoa/<id>	Xóa phiếu phù hợp trạng thái

Khi phê duyệt:

Kiểm tra phiếu còn ở trạng thái Chờ duyệt.
Khóa bản ghi bồn.
Kiểm tra sức chứa.
Cập nhật tồn.
Cập nhật trạng thái phiếu.
Commit transaction.

Nếu có lỗi, transaction phải được rollback.

7. Nhân viên và ca làm việc

Các nhóm API/route phục vụ:

Quản lý nhân viên.
Tạo và cập nhật ca.
Xem ca được phân công.

Các chức năng này phải kiểm tra quyền theo vai trò.

8. Bán hàng

API bán hàng phải nhận tối thiểu:

Ngày bán.
Nhân viên.
Nhiên liệu.
Bồn.
Số lượng.
Đơn giá.

Backend phải kiểm tra:

Dữ liệu bắt buộc.
Số lượng không âm.
Nhiên liệu và bồn tồn tại.
Số lượng bán không vượt tồn.
9. Báo cáo và thống kê

Các API báo cáo/thống kê cung cấp dữ liệu:

Doanh thu.
Số lượng bán.
Tổng nhập.
Tổng bán.
Tồn bồn.
Chênh lệch tồn.

Kết quả phải được tính từ dữ liệu thực tế trong CSDL.

10. API AI

Luồng xử lý:

Request
  ↓
Kiểm tra quyền
  ↓
Lấy dữ liệu nghiệp vụ
  ↓
Chuẩn bị prompt
  ↓
Gọi AI
  ↓
Kiểm tra kết quả
  ↓
Trả kết quả cho người dùng

AI API không được:

Tự thay đổi dữ liệu nghiệp vụ.
Tự phê duyệt phiếu nhập.
Tự điều chỉnh tồn bồn.
Tự tạo số liệu không có trong dữ liệu đầu vào.
11. HTTP Response

Sử dụng mã phản hồi phù hợp:

200: Thành công.
201: Tạo dữ liệu thành công khi API cần.
400: Dữ liệu đầu vào không hợp lệ.
401: Chưa xác thực.
403: Không có quyền.
404: Không tìm thấy dữ liệu.
500: Lỗi phía máy chủ.

Thiết kế API phải được cập nhật khi endpoint hoặc nghiệp vụ thay đổi.