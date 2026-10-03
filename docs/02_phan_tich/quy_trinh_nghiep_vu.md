# QUY TRÌNH NGHIỆP VỤ

## 1. Quy trình đăng nhập

1. Người dùng mở hệ thống.
2. Nhập tên đăng nhập và mật khẩu.
3. Hệ thống kiểm tra thông tin tài khoản.
4. Nếu hợp lệ, hệ thống xác định vai trò và cho phép truy cập chức năng tương ứng.
5. Nếu không hợp lệ, hệ thống thông báo lỗi và không cho phép đăng nhập.

## 2. Quy trình quản lý nhiên liệu

1. Quản lý tạo thông tin nhiên liệu.
2. Hệ thống kiểm tra dữ liệu bắt buộc và mã nhiên liệu.
3. Hệ thống lưu nhiên liệu.
4. Quản lý có thể xem, sửa hoặc cập nhật trạng thái nhiên liệu.

## 3. Quy trình quản lý bồn chứa

1. Quản lý chọn chức năng quản lý bồn.
2. Nhập thông tin bồn và chọn nhiên liệu đã tồn tại.
3. Hệ thống kiểm tra nhiên liệu được tham chiếu.
4. Hệ thống lưu thông tin bồn.
5. Quản lý có thể xem, sửa hoặc cập nhật trạng thái bồn.

## 4. Quy trình nhập hàng

1. Quản lý hoặc nhân viên ca tạo phiếu nhập.
2. Chọn nhiên liệu và bồn chứa.
3. Nhập số lượng cần nhập.
4. Hệ thống kiểm tra dữ liệu và tạo phiếu ở trạng thái `Chờ duyệt`.
5. Quản lý xem phiếu nhập.
6. Nếu phê duyệt, hệ thống khóa bồn, kiểm tra sức chứa và cập nhật tồn.
7. Nếu từ chối, phiếu chuyển sang `Từ chối` và tồn bồn không thay đổi.
8. Phiếu đã xử lý được lưu để tra cứu lịch sử.

## 5. Quy trình bán hàng

1. Quản lý hoặc nhân viên ca ghi nhận hoạt động bán hàng trong ngày.
2. Chọn ngày, nhiên liệu và bồn chứa.
3. Nhập số lượng bán và đơn giá.
4. Hệ thống kiểm tra số lượng bán không vượt tồn.
5. Hệ thống ghi nhận doanh số và cập nhật số liệu bán hàng.
6. Tồn bồn sau bán không được nhỏ hơn 0.

## 6. Quy trình theo dõi tồn bồn

1. Hệ thống xác định tồn đầu ngày.
2. Tổng hợp lượng nhập đã được duyệt trong ngày.
3. Tổng hợp lượng bán trong ngày.
4. Tính tồn cuối ngày.
5. Hiển thị các số liệu nhập, bán, tồn và chênh lệch nếu có dữ liệu đối chiếu.

## 7. Quy trình quản lý ca

1. Quản lý tạo ca làm việc.
2. Chọn ngày làm việc và nhân viên được phân công.
3. Hệ thống lưu thông tin ca.
4. Nhân viên được phân công có thể xem ca của mình.
5. Quản lý có thể cập nhật trạng thái ca.

## 8. Quy trình tra cứu và thống kê

1. Quản lý hoặc kế toán chọn loại dữ liệu cần xem.
2. Chọn khoảng thời gian hoặc điều kiện lọc nếu có.
3. Hệ thống truy vấn dữ liệu.
4. Hệ thống tổng hợp và hiển thị doanh thu, nhập, bán, tồn hoặc các chỉ số thống kê.

## 9. Quy trình sử dụng AI

1. Người dùng có quyền chọn chức năng AI.
2. Hệ thống lấy dữ liệu nghiệp vụ phù hợp.
3. Dữ liệu được đưa vào quy trình xử lý AI.
4. AI tạo báo cáo, tóm tắt biến động hoặc cảnh báo bất thường.
5. Hệ thống hiển thị kết quả và nguồn dữ liệu liên quan khi có thể.
6. Người dùng kiểm tra kết quả.
7. Người có thẩm quyền quyết định hành động nghiệp vụ nếu cần.

AI chỉ hỗ trợ phân tích và tổng hợp; không tự thay đổi dữ liệu nghiệp vụ hoặc tự thực hiện quyết định quan trọng.