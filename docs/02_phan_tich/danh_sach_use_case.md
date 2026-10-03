# DANH SÁCH USE CASE

## 1. Tổng quan

| Mã UC | Tên Use Case | Actor chính |
|---|---|---|
| UC01 | Đăng nhập | Quản lý, Nhân viên ca, Kế toán |
| UC02 | Phân quyền | Quản lý |
| UC03 | Quản lý bồn chứa | Quản lý |
| UC04 | Xem bồn chứa | Quản lý, Nhân viên ca |
| UC05 | Quản lý nhiên liệu | Quản lý |
| UC06 | Xem nhiên liệu | Quản lý, Nhân viên ca |
| UC07 | Ghi nhận nhập hàng | Quản lý, Nhân viên ca |
| UC08 | Phê duyệt / từ chối nhập hàng | Quản lý |
| UC09 | Ghi nhận bán hàng theo ngày | Quản lý, Nhân viên ca |
| UC10 | Theo dõi tồn bồn | Quản lý, Nhân viên ca |
| UC11 | Quản lý nhân viên | Quản lý |
| UC12 | Quản lý ca làm việc | Quản lý |
| UC13 | Xem ca làm việc | Quản lý, Nhân viên ca |
| UC14 | Tra cứu doanh thu | Quản lý, Kế toán |
| UC15 | Tra cứu nhập - xuất - tồn | Quản lý, Kế toán |
| UC16 | Thống kê hoạt động | Quản lý, Kế toán |
| UC17 | Sinh báo cáo bằng AI | Quản lý |
| UC18 | Tóm tắt biến động tồn bồn bằng AI | Quản lý |
| UC19 | Cảnh báo số liệu bất thường bằng AI | Quản lý |

## 2. Nhóm Use Case xác thực và phân quyền

### UC01 - Đăng nhập
Người dùng nhập tài khoản và mật khẩu để truy cập hệ thống.

### UC02 - Phân quyền
Hệ thống xác định vai trò và kiểm soát quyền truy cập chức năng.

## 3. Nhóm quản lý nhiên liệu và bồn chứa

### UC03 - Quản lý bồn chứa
Quản lý thêm, xem, sửa và cập nhật trạng thái bồn.

### UC04 - Xem bồn chứa
Quản lý và nhân viên ca xem thông tin bồn, nhiên liệu và tồn hiện tại.

### UC05 - Quản lý nhiên liệu
Quản lý thêm, xem, sửa và cập nhật trạng thái nhiên liệu.

### UC06 - Xem nhiên liệu
Quản lý và nhân viên ca xem thông tin nhiên liệu.

## 4. Nhóm nhập và bán hàng

### UC07 - Ghi nhận nhập hàng
Quản lý hoặc nhân viên ca tạo phiếu nhập nhiên liệu vào bồn.

### UC08 - Phê duyệt / từ chối nhập hàng
Quản lý kiểm tra phiếu nhập và quyết định phê duyệt hoặc từ chối.

### UC09 - Ghi nhận bán hàng theo ngày
Quản lý hoặc nhân viên ca ghi nhận số lượng nhiên liệu bán trong ngày.

## 5. Nhóm tồn kho và nhân sự

### UC10 - Theo dõi tồn bồn
Theo dõi tồn đầu, nhập, bán, tồn cuối và chênh lệch nếu có dữ liệu đối chiếu.

### UC11 - Quản lý nhân viên
Quản lý thêm, xem, sửa và cập nhật trạng thái nhân viên.

### UC12 - Quản lý ca làm việc
Quản lý tạo ca, phân công nhân viên và cập nhật trạng thái ca.

### UC13 - Xem ca làm việc
Quản lý và nhân viên ca xem thông tin ca được phân công.

## 6. Nhóm báo cáo và thống kê

### UC14 - Tra cứu doanh thu
Quản lý và kế toán tra cứu doanh thu từ dữ liệu bán hàng.

### UC15 - Tra cứu nhập - xuất - tồn
Quản lý và kế toán tra cứu dữ liệu nhập, bán và tồn theo điều kiện phù hợp.

### UC16 - Thống kê hoạt động
Quản lý và kế toán xem các số liệu thống kê về doanh thu, sản lượng bán, nhập, bán, tồn và chênh lệch.

## 7. Nhóm tích hợp AI

### UC17 - Sinh báo cáo bằng AI
Quản lý yêu cầu AI tổng hợp dữ liệu nghiệp vụ thành báo cáo.

### UC18 - Tóm tắt biến động tồn bồn bằng AI
Quản lý yêu cầu AI phân tích và tóm tắt biến động nhập, bán và tồn.

### UC19 - Cảnh báo số liệu bất thường bằng AI
Quản lý yêu cầu AI phân tích dữ liệu và đưa ra cảnh báo đối với các dấu hiệu bất thường.

## 8. Quy tắc chung

- UC chỉ được thực hiện bởi actor có quyền.
- UC phải tuân thủ các quy tắc nghiệp vụ đã xác định.
- AI không phải là actor nghiệp vụ độc lập.
- Kết quả AI phải dựa trên dữ liệu hệ thống được cung cấp.
- Các UC quan trọng phải có thể truy vết tới yêu cầu chức năng tương ứng.