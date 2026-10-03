# Chiến lược sử dụng AI

## 1. Mục đích

Xác định cách sử dụng AI trong hệ thống quản lý trạm xăng, bảo đảm AI hỗ trợ phân tích dữ liệu nhưng không thay thế người quản lý.

## 2. Phạm vi sử dụng AI

AI được sử dụng cho:

- Sinh báo cáo hoạt động theo ngày.
- Tóm tắt biến động tồn bồn.
- Phân tích và cảnh báo số liệu có dấu hiệu bất thường.

AI chỉ xử lý dữ liệu được hệ thống cung cấp.

## 3. Nguyên tắc sử dụng

- AI không tự tạo dữ liệu nghiệp vụ.
- AI không tự sửa dữ liệu trong database.
- AI không tự phê duyệt hoặc từ chối nhập hàng.
- AI không tự điều chỉnh tồn bồn.
- Kết quả AI phải dựa trên dữ liệu đầu vào thực tế.
- Người dùng kiểm tra và quyết định đối với các kết quả AI đưa ra.
- Các kết quả quan trọng cần có khả năng truy vết về dữ liệu đầu vào.

## 4. Quy trình sử dụng AI

1. Hệ thống lấy dữ liệu nghiệp vụ.
2. Kiểm tra dữ liệu đầu vào.
3. Chuẩn bị dữ liệu và prompt.
4. Gửi yêu cầu đến mô hình AI.
5. Nhận và kiểm tra kết quả.
6. Hiển thị kết quả cho người dùng.
7. Người dùng xem xét và sử dụng kết quả.

## 5. Kiểm soát dữ liệu

Trước khi gửi dữ liệu cho AI cần:

- Kiểm tra dữ liệu thiếu hoặc không hợp lệ.
- Giới hạn dữ liệu đúng với mục đích phân tích.
- Không gửi thông tin không cần thiết.
- Không đưa secret, mật khẩu hoặc API key vào prompt.
- Lưu thông tin cần thiết để truy vết quá trình sử dụng AI.

## 6. Kiểm soát kết quả

Kết quả AI cần được kiểm tra về:

- Tính đúng với dữ liệu đầu vào.
- Tính đầy đủ.
- Tính nhất quán.
- Khả năng xuất hiện thông tin không có trong dữ liệu.
- Nội dung cảnh báo có phù hợp với số liệu hay không.

Nếu kết quả không đáng tin cậy, người dùng không sử dụng kết quả đó làm căn cứ quyết định.

## 7. Human-in-the-loop

Người dùng giữ quyền kiểm soát trong các bước quan trọng.

Mô hình:

`Dữ liệu hệ thống → AI phân tích → Kết quả → Người dùng kiểm tra → Quyết định`

AI đóng vai trò hỗ trợ tổng hợp và phân tích, không phải chủ thể ra quyết định nghiệp vụ.

## 8. Theo dõi và cải tiến

Quá trình sử dụng AI cần được ghi nhận để:

- Theo dõi prompt đã sử dụng.
- Theo dõi phiên bản mô hình.
- Đánh giá chất lượng kết quả.
- Phát hiện lỗi hoặc hiện tượng AI tạo thông tin không có căn cứ.
- Cải thiện prompt và quy trình kiểm tra.