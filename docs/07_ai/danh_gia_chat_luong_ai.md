# Đánh giá chất lượng AI

## 1. Mục đích

Đánh giá chất lượng các kết quả do AI tạo ra trong hệ thống, bảo đảm kết quả có cơ sở dữ liệu rõ ràng và phù hợp với mục đích sử dụng.

## 2. Tiêu chí đánh giá

### 2.1. Độ chính xác

Kết quả AI phải phản ánh đúng dữ liệu được cung cấp và không tự thay đổi các giá trị nghiệp vụ.

### 2.2. Tính liên quan

Nội dung trả về phải phù hợp với yêu cầu, không đưa thêm thông tin không cần thiết.

### 2.3. Tính nhất quán

Với cùng dữ liệu và yêu cầu tương đương, kết quả cần có nội dung và kết luận hợp lý, không mâu thuẫn.

### 2.4. Hiện tượng bịa thông tin

Kiểm tra AI có tạo ra:

- Số liệu không tồn tại.
- Giao dịch không có trong hệ thống.
- Nguyên nhân không có căn cứ.
- Thông tin ngoài dữ liệu đầu vào nhưng được trình bày như sự thật.

### 2.5. Tính an toàn

AI không được:

- Tiết lộ thông tin bí mật.
- Tiết lộ API key hoặc mật khẩu.
- Tự thực hiện thao tác nghiệp vụ.
- Đưa ra hướng dẫn làm thay đổi dữ liệu ngoài phạm vi được phép.

## 3. Đánh giá theo chức năng

| Chức năng | Tiêu chí chính |
|---|---|
| Báo cáo AI | Đúng dữ liệu, đầy đủ, dễ hiểu |
| Tóm tắt tồn bồn | Phản ánh đúng biến động |
| Cảnh báo bất thường | Có căn cứ từ số liệu |
| Các chức năng AI khác | Đúng yêu cầu và không bịa dữ liệu |

## 4. Phương pháp đánh giá

Có thể kết hợp:

- Bộ dữ liệu kiểm thử đã biết kết quả.
- So sánh kết quả AI với dữ liệu nguồn.
- Kiểm tra thủ công bởi người dùng.
- Lặp lại cùng một yêu cầu để kiểm tra tính nhất quán.
- Kiểm tra các trường hợp dữ liệu thiếu, sai hoặc bất thường.

## 5. Đánh giá kết quả

Mỗi kết quả có thể được ghi nhận:

| ID | Chức năng | Độ chính xác | Liên quan | Nhất quán | Bịa thông tin | An toàn | Kết luận |
|---|---|---|---|---|---|---|---|
| AI-E01 | | | | | | | |
| AI-E02 | | | | | | | |

Không tự tạo số liệu đánh giá khi chưa thực hiện kiểm thử thực tế.

## 6. Xử lý kết quả không đạt

Khi AI tạo kết quả không phù hợp:

1. Xác định dữ liệu đầu vào.
2. Kiểm tra prompt.
3. Kiểm tra logic xử lý dữ liệu.
4. Điều chỉnh prompt hoặc quy trình.
5. Thực hiện lại kiểm thử.
6. Ghi nhận kết quả mới trong nhật ký AI.

## 7. Nguyên tắc

AI chỉ được xem là đạt yêu cầu khi kết quả được kiểm tra và có thể truy vết về dữ liệu nguồn.

Kết quả AI không được sử dụng để tự động thay thế quyết định nghiệp vụ của người dùng.