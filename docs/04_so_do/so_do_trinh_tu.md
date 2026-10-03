# Đặc tả sơ đồ trình tự

## 1. Mục đích

Mô tả thứ tự tương tác giữa người dùng, giao diện, route, service, cơ sở dữ liệu và AI trong các nghiệp vụ chính.

Tài liệu này là nguồn dữ liệu để AI Agent sinh sơ đồ trình tự khi cần. Không chứa hình vẽ hoặc mã Mermaid.

---

## 2. Trình tự đăng nhập

### Đối tượng tham gia

- Người dùng.
- Giao diện đăng nhập.
- Route đăng nhập.
- Auth Service.
- CSDL.

### Trình tự

1. Người dùng nhập tên đăng nhập và mật khẩu.
2. Giao diện gửi thông tin đến route đăng nhập.
3. Route chuyển thông tin cho Auth Service.
4. Auth Service truy vấn tài khoản trong CSDL.
5. CSDL trả về thông tin tài khoản.
6. Auth Service kiểm tra thông tin đăng nhập.
7. Nếu hợp lệ, hệ thống tạo session gồm `tai_khoan_id` và `vai_tro`.
8. Hệ thống chuyển người dùng đến giao diện tương ứng với vai trò.
9. Nếu không hợp lệ, hệ thống trả thông báo đăng nhập thất bại.

---

## 3. Trình tự ghi nhận nhập hàng

### Đối tượng tham gia

- Nhân viên ca.
- Giao diện nhập hàng.
- Route nhập hàng.
- Database Service.
- CSDL.

### Trình tự

1. Nhân viên chọn nhiên liệu, bồn chứa và nhập số lượng.
2. Giao diện gửi dữ liệu đến route nhập hàng.
3. Route kiểm tra quyền và dữ liệu đầu vào.
4. Hệ thống kiểm tra nhiên liệu và bồn chứa có tồn tại.
5. Hệ thống tạo phiếu nhập với trạng thái `Chờ duyệt`.
6. Phiếu được lưu vào bảng `nhap_hang`.
7. Hệ thống trả kết quả cho giao diện.
8. Khi phiếu còn `Chờ duyệt`, dữ liệu tồn bồn chưa thay đổi.

---

## 4. Trình tự phê duyệt nhập hàng

### Đối tượng tham gia

- Quản lý.
- Giao diện quản lý nhập hàng.
- Route duyệt nhập hàng.
- Database Service.
- CSDL.

### Trình tự

1. Quản lý chọn một phiếu nhập đang `Chờ duyệt`.
2. Route kiểm tra quyền quản lý.
3. Hệ thống bắt đầu transaction.
4. Hệ thống khóa bản ghi bồn tương ứng để tránh cập nhật đồng thời.
5. Hệ thống kiểm tra số lượng tồn hiện tại.
6. Hệ thống kiểm tra điều kiện:

   `Tồn hiện tại + Số lượng nhập <= Sức chứa bồn`

7. Nếu không đạt, giao dịch bị hủy và phiếu vẫn ở trạng thái `Chờ duyệt`.
8. Nếu đạt, hệ thống cập nhật tồn bồn.
9. Hệ thống chuyển phiếu sang `Đã duyệt`.
10. Transaction được commit.
11. Hệ thống trả kết quả cho quản lý.

### Trường hợp từ chối

1. Quản lý chọn phiếu `Chờ duyệt`.
2. Hệ thống chuyển trạng thái thành `Từ chối`.
3. Không cập nhật tồn bồn.
4. Phiếu vẫn được lưu để phục vụ lịch sử.

---

## 5. Trình tự ghi nhận bán hàng

### Đối tượng tham gia

- Nhân viên ca.
- Giao diện bán hàng.
- Route bán hàng.
- Database Service.
- CSDL.

### Trình tự

1. Nhân viên nhập ngày bán, nhiên liệu, bồn, số lượng và đơn giá.
2. Giao diện gửi dữ liệu đến route bán hàng.
3. Route kiểm tra quyền và dữ liệu đầu vào.
4. Hệ thống kiểm tra nhiên liệu và bồn chứa.
5. Hệ thống kiểm tra số lượng bán hợp lệ.
6. Hệ thống tính:

   `Thành tiền = Số lượng bán × Đơn giá`

7. Hệ thống lưu bản ghi vào `ban_hang`.
8. Hệ thống trả kết quả cho giao diện.

Lưu ý:

- Bán hàng được ghi nhận theo ngày.
- Ca làm việc chỉ dùng để quản lý nhân sự, không phải đơn vị tổng hợp doanh thu.

---

## 6. Trình tự tính nhập - xuất - tồn

### Đối tượng tham gia

- Người dùng.
- Giao diện tra cứu.
- Route tra cứu.
- Service thống kê.
- CSDL.

### Trình tự

1. Người dùng chọn ngày hoặc khoảng thời gian.
2. Giao diện gửi yêu cầu tra cứu.
3. Route chuyển yêu cầu cho Service thống kê.
4. Service lấy dữ liệu nhập đã được duyệt từ `nhap_hang`.
5. Service lấy dữ liệu bán từ `ban_hang`.
6. Service lấy tồn đầu từ dữ liệu tồn tương ứng.
7. Service tính:

   `Tổng nhập = SUM(số lượng phiếu nhập đã duyệt)`

8. Service tính:

   `Tổng bán = SUM(số lượng bán)`

9. Service tính:

   `Tồn cuối = Tồn đầu + Tổng nhập - Tổng bán`

10. Kết quả được trả về giao diện.

---

## 7. Trình tự tra cứu doanh thu

### Đối tượng tham gia

- Kế toán.
- Giao diện tra cứu doanh thu.
- Route doanh thu.
- Service thống kê.
- CSDL.

### Trình tự

1. Kế toán chọn khoảng thời gian cần tra cứu.
2. Route nhận yêu cầu.
3. Service thống kê lấy các bản ghi `ban_hang`.
4. Hệ thống tính thành tiền của từng bản ghi:

   `Thành tiền = Số lượng × Đơn giá`

5. Hệ thống tính:

   `Doanh thu = SUM(Thành tiền)`

6. Có thể nhóm kết quả theo ngày hoặc nhiên liệu.
7. Kết quả được trả về giao diện.

---

## 8. Trình tự thống kê hoạt động

### Dữ liệu đầu vào

- Dữ liệu bán hàng.
- Dữ liệu nhập hàng đã duyệt.
- Dữ liệu tồn bồn.
- Dữ liệu nhiên liệu.
- Dữ liệu nhân viên.

### Trình tự

1. Người dùng yêu cầu thống kê.
2. Hệ thống xác định khoảng thời gian.
3. Service thống kê truy vấn dữ liệu nghiệp vụ.
4. Hệ thống tính các chỉ tiêu:
   - Tổng doanh thu.
   - Tổng số lượng bán.
   - Tổng số lượng nhập.
   - Tồn đầu.
   - Tồn cuối.
   - Chênh lệch tồn nếu có dữ liệu kiểm kê.
5. Hệ thống nhóm dữ liệu theo tiêu chí được yêu cầu.
6. Kết quả được trả về giao diện.

---

## 9. Trình tự sinh báo cáo bằng AI

### Đối tượng tham gia

- Người dùng.
- Giao diện AI.
- Route AI.
- Service thống kê.
- AI Service.
- Mô hình AI.
- CSDL.

### Trình tự

1. Người dùng yêu cầu sinh báo cáo.
2. Route kiểm tra quyền.
3. Service thống kê lấy dữ liệu trong khoảng thời gian yêu cầu.
4. Hệ thống tính toán các số liệu nghiệp vụ trước khi gửi AI.
5. AI Service nhận dữ liệu đã được kiểm tra.
6. AI tạo nội dung báo cáo dựa trên dữ liệu được cung cấp.
7. AI Service trả kết quả về hệ thống.
8. Hệ thống hiển thị báo cáo cho người dùng.
9. Người dùng kiểm tra và quyết định sử dụng báo cáo.

### Nguyên tắc

AI không tự truy cập và thay đổi dữ liệu nghiệp vụ.

AI không được:
- Tự tạo số liệu không có trong dữ liệu đầu vào.
- Tự sửa tồn bồn.
- Tự duyệt hoặc từ chối nhập hàng.
- Tự thay đổi giao dịch.
- Tự đưa ra quyết định thay người quản lý.

---

## 10. Trình tự cảnh báo số liệu bất thường

### Dữ liệu đầu vào

- Số lượng nhập.
- Số lượng bán.
- Tồn đầu.
- Tồn cuối.
- Chênh lệch tồn.
- Các chỉ tiêu thống kê liên quan.

### Trình tự

1. Hệ thống lấy dữ liệu trong khoảng thời gian yêu cầu.
2. Hệ thống tính các chỉ tiêu nghiệp vụ.
3. Hệ thống kiểm tra các điều kiện dữ liệu cơ bản.
4. Dữ liệu hợp lệ được gửi đến AI Service nếu cần phân tích.
5. AI phân tích các số liệu được cung cấp.
6. AI trả về nội dung cảnh báo hoặc nhận xét.
7. Hệ thống hiển thị cảnh báo.
8. Người dùng kiểm tra dữ liệu nguồn trước khi đưa ra quyết định.

AI chỉ đưa ra cảnh báo hỗ trợ kiểm tra, không tự xác định giao dịch sai hoặc tự sửa dữ liệu.

---

## 11. Quy tắc xử lý lỗi

### Dữ liệu đầu vào không hợp lệ

- Không ghi dữ liệu vào CSDL.
- Trả thông báo lỗi cho người dùng.

### Không tìm thấy dữ liệu

- Không thực hiện phép tính trên dữ liệu không tồn tại.
- Trả kết quả rỗng hoặc thông báo phù hợp.

### Phê duyệt nhập hàng vượt sức chứa

- Không cập nhật tồn.
- Không chuyển trạng thái sang `Đã duyệt`.
- Transaction được rollback.

### Lỗi khi gọi AI

- Không làm thay đổi dữ liệu nghiệp vụ.
- Ghi nhận lỗi.
- Thông báo cho người dùng.
- Cho phép thực hiện lại yêu cầu nếu phù hợp.

---

## 12. Nguyên tắc tổng quát

Mọi nghiệp vụ phải tuân theo chuỗi:

`Người dùng → Giao diện → Route → Service → CSDL`

Đối với nghiệp vụ AI:

`Người dùng → Giao diện → Route → Service → Tính toán dữ liệu → AI Service → AI → Người dùng`

Dữ liệu nghiệp vụ là nguồn sự thật của hệ thống.

Các công thức và quy tắc nghiệp vụ phải được thực hiện bởi hệ thống trước khi dữ liệu được sử dụng cho thống kê hoặc AI.