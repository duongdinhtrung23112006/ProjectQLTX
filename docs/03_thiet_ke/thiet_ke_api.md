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

6. Theo dõi tồn bồn

Phương thức	Route	Vai trò	Chức năng
GET	/quanly/ton-bon	Quản lý	Tổng quan, tìm kiếm và lọc tồn bồn
GET	/quanly/ton-bon/xem/<id>	Quản lý	Chi tiết tồn bồn
GET	/nhanvien/ton-bon	Nhân viên ca	Xem, tìm kiếm và lọc tồn bồn
GET	/nhanvien/ton-bon/xem/<id>	Nhân viên ca	Xem chi tiết tồn bồn
GET	/ketoan/ton-bon	Kế toán	Xem tồn bồn để giữ liên kết menu hiện có

Các trang dùng chung dữ liệu và giao diện chỉ đọc từ `bon_chua` và `nhien_lieu`. Thống kê gồm cả bồn ngừng hoạt động. Ngưỡng cảnh báo bồn gần hết mặc định là mức tồn không quá 20% sức chứa. Chức năng không thay đổi số tồn hoặc schema.

Tra cứu số liệu

Phương thức	Route	Vai trò	Chức năng
GET	/quanly/tra-cuu	Quản lý	Tìm kiếm, lọc và tổng hợp bán hàng/nhập hàng
GET	/quanly/tra-cuu/xem/<loai_giao_dich>/<id>	Quản lý	Xem chi tiết giao dịch
GET	/ketoan/tra-cuu	Kế toán	Tìm kiếm, lọc và tổng hợp bán hàng/nhập hàng
GET	/ketoan/tra-cuu/xem/<loai_giao_dich>/<id>	Kế toán	Xem chi tiết giao dịch

Các endpoint chỉ đọc, dùng phân trang và truy vấn tham số. Số liệu thực tế chỉ tính giao dịch đã duyệt; lượng bán/nhập được nhóm theo đơn vị nhiên liệu. Bảng `nhap_hang` hiện không có ca làm việc, đơn giá hoặc thành tiền nên không hỗ trợ lọc nhập theo ca và không hiển thị chi phí nhập.

Thống kê và tổng quan

Phương thức	Route	Vai trò	Chức năng
GET	/quanly/thong-ke	Quản lý	Tổng quan KPI, biểu đồ, tình trạng bồn, giao dịch gần đây và cảnh báo
GET	/quanly/thong-ke/xem/<loai_giao_dich>/<id>	Quản lý	Xem chi tiết giao dịch chỉ đọc
GET	/ketoan/thong-ke	Kế toán	Tổng quan KPI, biểu đồ, tình trạng bồn, giao dịch gần đây và cảnh báo
GET	/ketoan/thong-ke/xem/<loai_giao_dich>/<id>	Kế toán	Xem chi tiết giao dịch chỉ đọc

Khoảng thống kê hỗ trợ hôm nay, 7 ngày, 30 ngày, tháng này và ngày tùy chọn. KPI/báo cáo giao dịch tính các phiếu đã duyệt; số chờ duyệt và tồn bồn là trạng thái hiện tại. Lượng nhập/bán được tách theo đơn vị đo, không tính lợi nhuận.

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

Nhân viên ca lập và quản lý phiếu của mình qua các route:

Phương thức	Route	Chức năng
GET	/nhanvien/ban-hang	Danh sách phiếu của nhân viên
GET/POST	/nhanvien/ban-hang/them	Lập phiếu chờ duyệt

Chỉ phiếu `Chờ duyệt` mới được chỉnh sửa hoặc xóa bởi nhân viên. Lập, sửa và xóa phiếu chờ duyệt không làm thay đổi tồn bồn.

Quản lý xem và xử lý phiếu trên phạm vi toàn trạm:

Phương thức	Route	Chức năng
GET	/quanly/ban-hang	Danh sách, tìm kiếm và lọc phiếu bán
GET	/quanly/ban-hang/xem/<id>	Xem chi tiết phiếu
POST	/quanly/ban-hang/duyet/<id>	Duyệt phiếu đang chờ
POST	/quanly/ban-hang/tu-choi/<id>	Từ chối phiếu đang chờ
POST	/quanly/ban-hang/xoa/<id>	Xóa phiếu theo trạng thái

Đường dẫn `/ban-hang` và các thao tác con tương ứng được giữ làm bí danh tương thích với menu quản lý hiện có.

Trạng thái sử dụng: `Chờ duyệt`, `Đã duyệt`, `Đã từ chối`. Chỉ phiếu chờ duyệt có thao tác duyệt/từ chối. Khi duyệt, hệ thống khóa phiếu và bồn, kiểm tra trạng thái nhiên liệu/bồn và tồn mới nhất, sau đó trừ tồn và đổi trạng thái trong cùng transaction. Khi xóa phiếu đã duyệt, số lượng được hoàn trả về đúng bồn trong transaction; thao tác bị từ chối nếu việc hoàn trả vượt sức chứa. Từ chối hoặc xóa phiếu chưa duyệt/đã từ chối không làm đổi tồn bồn.
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