# Đặc tả sơ đồ quy trình nghiệp vụ

## 1. Mục đích

Mô tả các quy trình nghiệp vụ chính của hệ thống dưới dạng văn bản.

Tài liệu là nguồn dữ liệu để AI Agent sinh sơ đồ quy trình khi cần.

---

## 2. Quy trình đăng nhập và phân quyền

### Đầu vào

- Tên đăng nhập.
- Mật khẩu.

### Quy trình

1. Người dùng mở chức năng đăng nhập.
2. Nhập tên đăng nhập và mật khẩu.
3. Hệ thống kiểm tra tài khoản.
4. Nếu thông tin không hợp lệ, trả thông báo lỗi và kết thúc.
5. Nếu hợp lệ, hệ thống xác định vai trò.
6. Hệ thống tạo phiên đăng nhập.
7. Người dùng được chuyển đến giao diện phù hợp với vai trò.

### Vai trò

- Quản lý.
- Nhân viên ca.
- Kế toán.

---

## 3. Quy trình quản lý nhiên liệu

### Đầu vào

- Mã nhiên liệu.
- Tên nhiên liệu.
- Đơn vị.
- Đơn giá.
- Trạng thái.

### Quy trình

1. Quản lý mở chức năng quản lý nhiên liệu.
2. Thêm, sửa, xem hoặc thay đổi trạng thái nhiên liệu.
3. Hệ thống kiểm tra dữ liệu.
4. Nếu dữ liệu không hợp lệ, yêu cầu nhập lại.
5. Nếu hợp lệ, hệ thống lưu thay đổi.
6. Nhiên liệu sau khi tạo có thể được sử dụng để tạo hoặc liên kết với bồn chứa.

### Quy tắc

- `ma_nhien_lieu` không được trùng.
- Nhiên liệu phải tồn tại trước khi bồn chứa tham chiếu đến nhiên liệu đó.

---

## 4. Quy trình quản lý bồn chứa

### Đầu vào

- Mã bồn.
- Tên bồn.
- Nhiên liệu.
- Sức chứa.
- Tồn hiện tại.
- Trạng thái.

### Quy trình

1. Quản lý mở chức năng quản lý bồn.
2. Hệ thống hiển thị danh sách bồn.
3. Quản lý thêm hoặc chỉnh sửa thông tin.
4. Hệ thống kiểm tra nhiên liệu được chọn có tồn tại.
5. Hệ thống kiểm tra sức chứa và tồn hiện tại.
6. Nếu hợp lệ, lưu dữ liệu.
7. Bồn được sử dụng trong các nghiệp vụ nhập, bán và theo dõi tồn.

### Ràng buộc

`0 <= Tồn hiện tại <= Sức chứa`

---

## 5. Quy trình nhập hàng

### Đầu vào

- Nhiên liệu.
- Bồn chứa.
- Số lượng nhập.
- Nhân viên lập phiếu.
- Ngày tạo.

### Quy trình

1. Nhân viên chọn nhiên liệu.
2. Chọn bồn chứa tương ứng.
3. Nhập số lượng.
4. Hệ thống kiểm tra dữ liệu.
5. Hệ thống tạo phiếu nhập với trạng thái `Chờ duyệt`.
6. Phiếu được lưu vào CSDL.
7. Quản lý xem danh sách phiếu chờ duyệt.
8. Quản lý lựa chọn:
   - Phê duyệt.
   - Từ chối.

### Khi phê duyệt

1. Hệ thống bắt đầu transaction.
2. Khóa bồn cần cập nhật.
3. Kiểm tra sức chứa.
4. Tính tồn mới:

`Tồn mới = Tồn hiện tại + Số lượng nhập`

5. Nếu tồn mới vượt sức chứa:
   - Không cập nhật bồn.
   - Không phê duyệt phiếu.
6. Nếu hợp lệ:
   - Cập nhật tồn bồn.
   - Chuyển phiếu thành `Đã duyệt`.
   - Commit transaction.

### Khi từ chối

1. Chuyển phiếu thành `Từ chối`.
2. Không thay đổi tồn bồn.
3. Giữ phiếu trong lịch sử.

### Khi xóa

Chỉ phiếu `Chờ duyệt` mới được phép xóa.

---

## 6. Quy trình bán hàng

### Đầu vào

- Ngày bán.
- Nhiên liệu.
- Bồn chứa.
- Số lượng bán.
- Đơn giá.
- Nhân viên lập.

### Quy trình

1. Nhân viên nhập thông tin bán hàng.
2. Hệ thống kiểm tra nhiên liệu và bồn.
3. Kiểm tra số lượng bán hợp lệ.
4. Tính thành tiền:

`Thành tiền = Số lượng bán × Đơn giá`

5. Lưu giao dịch bán hàng.
6. Giao dịch được sử dụng cho thống kê doanh thu và tồn kho.

### Quy tắc

Bán hàng được ghi nhận theo ngày, không tổng hợp doanh thu theo ca làm việc.

---

## 7. Quy trình theo dõi tồn bồn

### Dữ liệu đầu vào

- Tồn đầu.
- Phiếu nhập đã duyệt.
- Giao dịch bán hàng.

### Quy trình

1. Xác định ngày hoặc khoảng thời gian cần theo dõi.
2. Lấy tồn đầu.
3. Tính tổng nhập.
4. Tính tổng bán.
5. Tính tồn cuối.
6. Lưu hoặc hiển thị kết quả.

### Công thức

`Tổng nhập = SUM(Số lượng phiếu nhập đã duyệt)`

`Tổng bán = SUM(Số lượng bán)`

`Tồn cuối = Tồn đầu + Tổng nhập - Tổng bán`

### Kiểm tra

Nếu:

`Tồn cuối < 0`

hoặc

`Tồn cuối > Sức chứa`

thì dữ liệu cần được kiểm tra.

---

## 8. Quy trình tra cứu doanh thu

### Đầu vào

- Ngày hoặc khoảng thời gian.
- Có thể chọn nhiên liệu.
- Có thể chọn bồn.
- Có thể chọn nhân viên.

### Quy trình

1. Người dùng nhập điều kiện tra cứu.
2. Hệ thống truy vấn dữ liệu bán hàng.
3. Tính thành tiền của từng giao dịch.
4. Tổng hợp doanh thu.
5. Nhóm kết quả theo điều kiện được chọn.
6. Hiển thị kết quả.

### Công thức

`Thành tiền = Số lượng × Đơn giá`

`Doanh thu = SUM(Thành tiền)`

---

## 9. Quy trình tra cứu nhập - xuất - tồn

### Đầu vào

- Ngày hoặc khoảng thời gian.
- Nhiên liệu.
- Bồn chứa.

### Quy trình

1. Người dùng chọn điều kiện tra cứu.
2. Hệ thống lấy các phiếu nhập đã duyệt.
3. Hệ thống lấy các giao dịch bán.
4. Hệ thống xác định tồn đầu.
5. Tính tổng nhập.
6. Tính tổng bán.
7. Tính tồn cuối.
8. Hiển thị kết quả.

### Kết quả

Mỗi dòng thống kê có thể gồm:

- Nhiên liệu.
- Bồn.
- Tồn đầu.
- Tổng nhập.
- Tổng bán.
- Tồn cuối.
- Chênh lệch nếu có dữ liệu kiểm kê.

---

## 10. Quy trình thống kê hoạt động

### Dữ liệu sử dụng

- `nhap_hang`.
- `ban_hang`.
- `bon_chua`.
- `nhien_lieu`.
- `ton_bon` nếu đã triển khai.
- `nhan_vien` khi cần thống kê theo nhân viên.

### Các chỉ tiêu

#### Doanh thu

`Doanh thu = SUM(Số lượng bán × Đơn giá)`

#### Tổng số lượng bán

`Tổng bán = SUM(Số lượng bán)`

#### Tổng số lượng nhập

`Tổng nhập = SUM(Số lượng phiếu nhập đã duyệt)`

#### Tồn cuối

`Tồn cuối = Tồn đầu + Tổng nhập - Tổng bán`

#### Chênh lệch tồn

Nếu có số liệu kiểm kê:

`Chênh lệch = Tồn thực tế - Tồn theo hệ thống`

### Quy trình

1. Xác định khoảng thời gian.
2. Truy vấn dữ liệu.
3. Lọc dữ liệu hợp lệ.
4. Tính các chỉ tiêu.
5. Nhóm dữ liệu.
6. Trả kết quả thống kê.
7. Hiển thị cho người dùng.

---

## 11. Quy trình sinh báo cáo bằng AI

### Đầu vào

- Khoảng thời gian.
- Các số liệu thống kê.
- Dữ liệu tồn bồn.
- Dữ liệu nhập - bán.
- Các kết quả kiểm tra dữ liệu.

### Quy trình

1. Người dùng yêu cầu tạo báo cáo.
2. Hệ thống xác định phạm vi dữ liệu.
3. Hệ thống truy vấn dữ liệu nguồn.
4. Hệ thống tính toán các chỉ tiêu.
5. Hệ thống kiểm tra dữ liệu.
6. Dữ liệu được gửi đến AI Service.
7. AI phân tích và tạo nội dung báo cáo.
8. Hệ thống hiển thị kết quả.
9. Người dùng kiểm tra và quyết định sử dụng.

### Nguyên tắc

AI chỉ sử dụng dữ liệu được cung cấp.

AI không được:
- Tự tạo số liệu.
- Tự thay đổi dữ liệu.
- Tự điều chỉnh tồn.
- Tự phê duyệt giao dịch.
- Tự thay thế quyết định của người quản lý.

---

## 12. Quy trình tóm tắt biến động tồn bồn bằng AI

### Dữ liệu đầu vào

- Tồn đầu.
- Tổng nhập.
- Tổng bán.
- Tồn cuối.
- Chênh lệch tồn nếu có.

### Quy trình

1. Hệ thống tính các chỉ tiêu tồn.
2. So sánh dữ liệu giữa các ngày hoặc khoảng thời gian.
3. Chuẩn bị dữ liệu cho AI.
4. AI nhận diện các biến động đáng chú ý.
5. AI tạo nội dung tóm tắt.
6. Hệ thống hiển thị kết quả.
7. Người dùng kiểm tra lại số liệu nguồn.

---

## 13. Quy trình cảnh báo số liệu bất thường

### Dữ liệu kiểm tra

- Số lượng nhập.
- Số lượng bán.
- Tồn bồn.
- Chênh lệch tồn.
- Các biến động theo thời gian.

### Quy trình

1. Hệ thống lấy dữ liệu cần kiểm tra.
2. Hệ thống thực hiện các phép tính cơ bản.
3. Hệ thống kiểm tra các ràng buộc dữ liệu.
4. Dữ liệu được gửi đến AI nếu cần phân tích.
5. AI đưa ra cảnh báo hoặc nhận xét.
6. Hệ thống hiển thị cảnh báo.
7. Người dùng kiểm tra dữ liệu gốc.
8. Người có thẩm quyền quyết định cách xử lý.

### Nguyên tắc

Cảnh báo của AI là thông tin hỗ trợ kiểm tra, không phải quyết định xử lý tự động.

---

## 14. Quy trình cập nhật dữ liệu

Mọi dữ liệu nghiệp vụ phải đi qua quy trình:

`Nhập dữ liệu → Kiểm tra → Xử lý nghiệp vụ → Lưu CSDL → Cập nhật kết quả`

Không cho phép giao diện hoặc AI tự ý thay đổi dữ liệu mà không thông qua logic nghiệp vụ.

---

## 15. Quy trình xử lý lỗi

### Lỗi dữ liệu

1. Phát hiện dữ liệu không hợp lệ.
2. Không ghi dữ liệu.
3. Hiển thị nguyên nhân.
4. Người dùng sửa và gửi lại.

### Lỗi nghiệp vụ

Ví dụ nhập vượt sức chứa:

1. Phát hiện vi phạm.
2. Dừng xử lý.
3. Không cập nhật tồn.
4. Thông báo cho người dùng.

### Lỗi CSDL

1. Ghi nhận lỗi.
2. Rollback transaction nếu đang thực hiện giao dịch.
3. Không để dữ liệu ở trạng thái cập nhật dở dang.
4. Thông báo lỗi.

### Lỗi AI

1. Ghi nhận lỗi.
2. Không thay đổi dữ liệu nghiệp vụ.
3. Thông báo cho người dùng.
4. Cho phép thực hiện lại khi phù hợp.

---

## 16. Nguyên tắc truy vết

Mỗi kết quả thống kê hoặc báo cáo AI phải có thể truy ngược về dữ liệu nguồn.

Chuỗi truy vết:

`Dữ liệu nguồn → Phép tính → Kết quả thống kê → AI phân tích → Kết quả hiển thị`

Mục tiêu là bảo đảm người dùng có thể kiểm tra được cơ sở của các số liệu và nội dung do hệ thống sinh ra.