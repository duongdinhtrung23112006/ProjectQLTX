# QUY TẮC NGHIỆP VỤ

## BR01 - Đăng nhập

- Người dùng phải đăng nhập trước khi sử dụng chức năng yêu cầu xác thực.
- Tài khoản phải xác định được vai trò.
- Người dùng không được truy cập chức năng ngoài quyền.

## BR02 - Vai trò

Hệ thống có 3 vai trò:

- Quản lý.
- Nhân viên ca.
- Kế toán.

Quyền truy cập được kiểm soát theo vai trò.

## BR03 - Nhiên liệu và bồn chứa

- Nhiên liệu phải được tạo trước khi tạo bồn.
- Mỗi bồn tham chiếu đến một nhiên liệu đã tồn tại.
- Không nhập tự do tên nhiên liệu thay cho khóa ngoại.
- Một loại nhiên liệu có thể được gắn với nhiều bồn.

nhien_lieu 1 ───── N bon_chua
BR04 - Sức chứa bồn
ton_hien_tai >= 0
ton_hien_tai <= suc_chua
Không được nhập hàng nếu số lượng sau nhập vượt sức chứa.
Tồn sau nhập = Tồn hiện tại + Số lượng nhập
BR05 - Nhập hàng

Phiếu nhập có các trạng thái tối thiểu:

Chờ duyệt.
Đã duyệt.
Từ chối.

Quy tắc:

Chỉ phiếu Chờ duyệt mới được duyệt hoặc từ chối.
Chỉ cập nhật tồn khi phiếu được duyệt.
Phiếu đã duyệt phải được giữ lại để tra cứu.
Phiếu đã từ chối không làm thay đổi tồn.
Không được xóa phiếu đã xử lý nếu nghiệp vụ yêu cầu lưu lịch sử.
BR06 - Bán hàng
Bán hàng được ghi nhận theo ngày.
Số lượng bán không được âm.
Không được bán vượt lượng tồn.
Sau khi bán, tồn bồn không được âm.
Tồn sau bán = Tồn trước bán - Số lượng bán
BR07 - Tồn bồn
Tồn cuối = Tồn đầu + Tổng nhập - Tổng bán

Tồn bồn phải nhất quán với các nghiệp vụ nhập và bán đã được ghi nhận.

BR08 - Ca làm việc
Ca làm việc dùng để phân công và quản lý nhân viên.
Ca làm việc không đồng nghĩa với việc bán hàng phải được ghi nhận thành từng ca.
Dữ liệu bán hàng hiện tại được tổng hợp theo ngày.
BR09 - Doanh thu

Doanh thu được tính từ dữ liệu bán hàng thực tế.

Không được tạo số liệu doanh thu giả để thay thế dữ liệu nghiệp vụ.

BR10 - Thống kê
Thống kê phải sử dụng dữ liệu thực tế trong hệ thống.
Các phép tổng hợp phải nhất quán với dữ liệu gốc.
Không tự suy diễn dữ liệu còn thiếu thành dữ liệu thực tế.
BR11 - AI

AI:

Chỉ phân tích dữ liệu được cung cấp.
Không tự tạo số liệu.
Không tự sửa dữ liệu nghiệp vụ.
Không tự phê duyệt hoặc từ chối nghiệp vụ.
Không tự thay đổi tồn bồn.
Không tự đưa ra quyết định thay người có thẩm quyền.

Khi dữ liệu không đủ, AI phải nêu rõ giới hạn.

BR12 - Human-in-the-loop

Kết quả AI chỉ có tính chất hỗ trợ.

Người có thẩm quyền phải kiểm tra và quyết định trước các hành động nghiệp vụ quan trọng.

BR13 - Tính toàn vẹn dữ liệu
Khóa chính phải duy nhất.
Khóa ngoại phải tham chiếu bản ghi tồn tại.
Không được tạo bản ghi tham chiếu sai.
Các thao tác cập nhật tồn quan trọng phải đảm bảo tính nhất quán dữ liệu.
BR14 - Thay đổi nghiệp vụ

Không được tự ý thay đổi quy tắc nghiệp vụ bằng code.

Nếu cần thay đổi:

Cập nhật tài liệu.
Phân tích ảnh hưởng.
Cập nhật Use Case.
Cập nhật thiết kế.
Cập nhật code.
Cập nhật kiểm thử.
