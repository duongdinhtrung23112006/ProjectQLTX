# Đặc tả tích hợp AI

## 1. Mục đích

Mô tả cách AI được tích hợp vào hệ thống quản lý trạm xăng, nguồn dữ liệu AI sử dụng, quá trình xử lý và giới hạn quyền của AI.

AI đóng vai trò hỗ trợ phân tích và tổng hợp dữ liệu, không thay thế các nghiệp vụ chính của hệ thống.

---

## 2. Vị trí của AI trong hệ thống

AI nằm ở tầng dịch vụ AI và giao tiếp với hệ thống thông qua AI Service.

Luồng tổng quát:

Người dùng
→ Giao diện
→ Route
→ Business Service
→ Tính toán và kiểm tra dữ liệu
→ AI Service
→ Mô hình AI
→ AI Service
→ Business Service
→ Giao diện
→ Người dùng

AI không truy cập trực tiếp vào cơ sở dữ liệu để tự thay đổi dữ liệu.

---

## 3. Nguồn dữ liệu cung cấp cho AI

AI chỉ được sử dụng dữ liệu đã có trong hệ thống.

Các nguồn chính:

- `nhien_lieu`: thông tin nhiên liệu.
- `bon_chua`: thông tin bồn và sức chứa.
- `nhap_hang`: dữ liệu nhập hàng.
- `ban_hang`: dữ liệu bán hàng.
- `ton_bon`: dữ liệu tồn bồn nếu đã triển khai.
- `nhan_vien`: thông tin cần thiết để thống kê theo nhân viên.
- Kết quả thống kê được hệ thống tính toán.

AI không được tự bổ sung dữ liệu nghiệp vụ còn thiếu.

---

## 4. Quy trình chuẩn bị dữ liệu cho AI

Trước khi gửi dữ liệu cho AI, hệ thống phải:

1. Xác định phạm vi thời gian.
2. Truy vấn dữ liệu nguồn.
3. Lọc dữ liệu phù hợp.
4. Kiểm tra dữ liệu.
5. Tính các chỉ tiêu nghiệp vụ.
6. Chuẩn hóa dữ liệu.
7. Tạo dữ liệu đầu vào cho AI.
8. Gửi dữ liệu đến AI Service.

Các phép tính nghiệp vụ phải được thực hiện trước khi AI phân tích.

---

## 5. Các phép tính cung cấp cho AI

### 5.1. Thành tiền

`Thành tiền = Số lượng bán × Đơn giá`

### 5.2. Doanh thu

`Doanh thu = SUM(Thành tiền)`

### 5.3. Tổng nhập

`Tổng nhập = SUM(Số lượng của các phiếu nhập đã duyệt)`

### 5.4. Tổng bán

`Tổng bán = SUM(Số lượng bán)`

### 5.5. Tồn cuối

`Tồn cuối = Tồn đầu + Tổng nhập - Tổng bán`

### 5.6. Chênh lệch tồn

Nếu có số liệu kiểm kê:

`Chênh lệch = Tồn thực tế - Tồn theo hệ thống`

AI sử dụng các kết quả này để phân tích, không tự thay thế công thức nghiệp vụ.

---

## 6. Chức năng AI sinh báo cáo

### Đầu vào

- Khoảng thời gian.
- Doanh thu.
- Tổng nhập.
- Tổng bán.
- Tồn đầu.
- Tồn cuối.
- Các biến động đáng chú ý.

### Xử lý

1. Hệ thống tính toán số liệu.
2. AI nhận dữ liệu đã được chuẩn bị.
3. AI tổng hợp tình hình hoạt động.
4. AI tạo nội dung báo cáo.
5. Hệ thống trả báo cáo cho người dùng.

### Đầu ra

Báo cáo có thể gồm:

- Tổng quan hoạt động.
- Tình hình bán hàng.
- Tình hình nhập hàng.
- Tình hình tồn bồn.
- Các biến động đáng chú ý.
- Các nội dung cần người dùng kiểm tra.

---

## 7. Chức năng AI tóm tắt biến động tồn bồn

### Đầu vào

- Tồn đầu.
- Tổng nhập.
- Tổng bán.
- Tồn cuối.
- Chênh lệch tồn nếu có.
- Dữ liệu của các ngày liên quan.

### Xử lý

1. Hệ thống tính các chỉ tiêu tồn.
2. So sánh dữ liệu giữa các thời điểm.
3. Gửi kết quả cho AI.
4. AI mô tả các biến động đáng chú ý.

### Đầu ra

Nội dung tóm tắt biến động tồn bồn.

AI không được tự sửa số liệu tồn.

---

## 8. Chức năng AI cảnh báo số liệu bất thường

### Dữ liệu kiểm tra

- Số lượng nhập.
- Số lượng bán.
- Tồn bồn.
- Chênh lệch tồn.
- Biến động theo thời gian.

### Quy trình

1. Hệ thống lấy dữ liệu.
2. Hệ thống kiểm tra các ràng buộc cơ bản.
3. Hệ thống tính các chỉ tiêu.
4. AI phân tích dữ liệu.
5. AI trả về cảnh báo hoặc nhận xét.
6. Hệ thống hiển thị cảnh báo.
7. Người dùng kiểm tra lại dữ liệu nguồn.

### Nguyên tắc

Cảnh báo AI chỉ là tín hiệu hỗ trợ kiểm tra.

AI không tự kết luận giao dịch gian lận hoặc tự xử lý giao dịch.

---

## 9. Cấu trúc dữ liệu gửi cho AI

Dữ liệu gửi AI nên được cấu trúc rõ ràng, gồm:

### Thông tin yêu cầu

- Loại yêu cầu.
- Khoảng thời gian.
- Mục đích phân tích.

### Dữ liệu thống kê

- Doanh thu.
- Tổng nhập.
- Tổng bán.
- Tồn đầu.
- Tồn cuối.
- Chênh lệch tồn.

### Dữ liệu chi tiết khi cần

- Danh sách giao dịch.
- Danh sách bồn.
- Danh sách nhiên liệu.
- Các bản ghi liên quan.

Chỉ gửi những dữ liệu cần thiết cho nhiệm vụ.

---

## 10. Prompt AI

Prompt phải quy định rõ:

- Vai trò của AI.
- Nguồn dữ liệu được phép sử dụng.
- Nhiệm vụ cần thực hiện.
- Định dạng đầu ra.
- Không được tự tạo số liệu.
- Không được thay đổi dữ liệu.
- Phải nêu rõ khi dữ liệu không đủ.
- Phải phân biệt dữ liệu thực tế với nhận xét do AI tạo.

AI không được suy diễn thành số liệu thực tế nếu dữ liệu đầu vào không cung cấp.

---

## 11. Kiểm soát đầu ra AI

Sau khi AI trả kết quả, hệ thống hoặc người dùng cần kiểm tra:

- Kết quả có đúng định dạng không.
- Các số liệu có khớp dữ liệu nguồn không.
- AI có tạo số liệu không tồn tại không.
- AI có đưa ra kết luận vượt quá dữ liệu không.
- Nội dung có phù hợp với yêu cầu không.

Kết quả không đạt yêu cầu phải được đánh dấu để kiểm tra hoặc tạo lại.

---

## 12. Human-in-the-loop

Người dùng vẫn giữ quyền quyết định cuối cùng.

Quy trình:

`Dữ liệu → Tính toán → AI phân tích → Kết quả AI → Người dùng kiểm tra → Quyết định`

Đặc biệt đối với:

- Cảnh báo bất thường.
- Báo cáo hoạt động.
- Biến động tồn bồn.
- Các đề xuất cần kiểm tra.

AI không tự động thực hiện hành động nghiệp vụ sau khi phân tích.

---

## 13. Quyền của AI

### AI được phép

- Phân tích dữ liệu được cung cấp.
- Tóm tắt dữ liệu.
- Sinh báo cáo.
- Phát hiện dấu hiệu bất thường.
- Đưa ra nội dung cần kiểm tra.

### AI không được phép

- Tự sửa dữ liệu CSDL.
- Tự cập nhật tồn bồn.
- Tự tạo phiếu nhập.
- Tự ghi nhận bán hàng.
- Tự phê duyệt nhập hàng.
- Tự từ chối nhập hàng.
- Tự thay đổi tài khoản hoặc phân quyền.
- Tự đưa ra quyết định nghiệp vụ cuối cùng.

---

## 14. Xử lý lỗi khi gọi AI

### Lỗi kết nối

1. Ghi nhận lỗi.
2. Không thay đổi dữ liệu nghiệp vụ.
3. Thông báo cho người dùng.
4. Có thể thực hiện lại yêu cầu.

### AI trả dữ liệu sai định dạng

1. Kiểm tra kết quả.
2. Nếu không hợp lệ, không sử dụng trực tiếp.
3. Có thể yêu cầu AI tạo lại theo định dạng quy định.
4. Nếu tiếp tục lỗi, trả thông báo cho người dùng.

### AI không đủ dữ liệu

AI phải thông báo rằng dữ liệu không đủ để đưa ra nhận xét đáng tin cậy.

Không được tự tạo dữ liệu để hoàn thành câu trả lời.

---

## 15. Bảo mật dữ liệu AI

Không gửi các dữ liệu không cần thiết cho AI.

Không đưa vào prompt:

- Mật khẩu.
- Thông tin xác thực.
- Khóa API.
- Secret.
- Dữ liệu nhạy cảm không liên quan đến nhiệm vụ.

API key và thông tin kết nối AI phải được lưu trong biến môi trường hoặc cấu hình bảo mật.

---

## 16. Truy vết kết quả AI

Mỗi kết quả AI cần có thể xác định:

- Thời điểm yêu cầu.
- Loại yêu cầu.
- Khoảng thời gian dữ liệu.
- Dữ liệu hoặc chỉ tiêu đã cung cấp.
- Prompt được sử dụng.
- Kết quả AI.
- Người yêu cầu.
- Kết quả kiểm tra của người dùng nếu có.

Mục tiêu là bảo đảm có thể truy ngược:

`Kết quả AI → Prompt → Dữ liệu đầu vào → Dữ liệu nguồn`

---

## 17. Nguyên tắc tích hợp

AI là thành phần hỗ trợ của hệ thống, không phải nguồn dữ liệu gốc.

Nguồn dữ liệu gốc:

`Cơ sở dữ liệu nghiệp vụ`

Nguồn tính toán:

`Business Service / Service thống kê`

Nguồn phân tích:

`AI Service`

Nguồn quyết định:

`Người dùng có quyền`

Kiến trúc này giúp hạn chế việc AI tạo thông tin không có căn cứ và giữ quyền kiểm soát nghiệp vụ cho hệ thống và người dùng.