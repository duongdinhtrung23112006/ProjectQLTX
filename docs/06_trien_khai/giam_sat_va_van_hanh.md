# Giám sát và vận hành

## 1. Mục đích

Theo dõi trạng thái hệ thống trong quá trình chạy, phát hiện sự cố và duy trì hoạt động ổn định.

---

## 2. Thành phần cần giám sát

### Ứng dụng

Theo dõi:

- Trạng thái Flask.
- Lỗi HTTP.
- Lỗi xử lý nghiệp vụ.
- Thời gian phản hồi.
- Số lượng request lỗi.

### Cơ sở dữ liệu

Theo dõi:

- Khả năng kết nối.
- Trạng thái MySQL.
- Lỗi truy vấn.
- Tài nguyên database.
- Các vấn đề về dữ liệu.

### AI

Theo dõi:

- Số lần gọi AI.
- Lỗi kết nối AI.
- Thời gian phản hồi.
- Kết quả không hợp lệ.
- Nội dung có dấu hiệu hallucination.
- Chi phí sử dụng nếu dịch vụ AI có tính phí.

---

## 3. Logging

Log cần hỗ trợ xác định:

- Thời điểm xảy ra sự kiện.
- Thành phần gây ra sự kiện.
- Loại lỗi.
- Request hoặc thao tác liên quan.
- Kết quả xử lý.

Không ghi vào log:

- Mật khẩu.
- API key.
- Secret.
- Dữ liệu nhạy cảm không cần thiết.

---

## 4. Health Check

Hệ thống nên có cơ chế kiểm tra tối thiểu:

- Ứng dụng có đang chạy.
- Kết nối database có hoạt động.
- Các thành phần phụ thuộc quan trọng có hoạt động.

Health check chỉ phản ánh trạng thái hệ thống, không tự sửa dữ liệu nghiệp vụ.

---

## 5. Giám sát dữ liệu nghiệp vụ

Theo dõi các dấu hiệu cần kiểm tra:

- Tồn bồn âm.
- Tồn vượt sức chứa.
- Số liệu nhập - bán không hợp lý.
- Giao dịch có dữ liệu bất thường.
- Chênh lệch tồn.

Các cảnh báo không tự động thay đổi dữ liệu.

---

## 6. Giám sát AI

Kết quả AI phải có khả năng truy ngược về:

`Dữ liệu nguồn → Dữ liệu đầu vào AI → Prompt → Kết quả AI`

Nếu phát hiện kết quả AI không phù hợp:

1. Ghi nhận kết quả.
2. Kiểm tra dữ liệu đầu vào.
3. Kiểm tra prompt.
4. Kiểm tra xử lý dữ liệu.
5. Kiểm tra kết quả AI.
6. Đánh giá và điều chỉnh nếu cần.

---

## 7. Xử lý sự cố

Khi phát hiện sự cố:

1. Xác định thành phần bị ảnh hưởng.
2. Đánh giá mức độ.
3. Ghi nhận thời điểm và triệu chứng.
4. Kiểm tra log.
5. Kiểm tra database.
6. Khắc phục.
7. Kiểm thử lại.
8. Theo dõi sau khi khắc phục.
9. Ghi nhận nguyên nhân và cách xử lý.

---

## 8. Vận hành định kỳ

Các công việc cần thực hiện:

- Kiểm tra log.
- Kiểm tra trạng thái ứng dụng.
- Kiểm tra database.
- Kiểm tra backup.
- Kiểm tra dung lượng lưu trữ.
- Kiểm tra lỗi còn tồn tại.
- Kiểm tra cấu hình.
- Kiểm tra hoạt động của AI nếu đã tích hợp.

---

## 9. Bảo trì

Khi cập nhật hệ thống:

1. Xác định thay đổi.
2. Cập nhật tài liệu liên quan.
3. Kiểm thử.
4. Backup dữ liệu nếu cần.
5. Triển khai.
6. Kiểm tra sau triển khai.
7. Theo dõi log.
8. Có phương án quay lui nếu phát sinh lỗi.

---

## 10. Nguyên tắc vận hành

- Không sửa trực tiếp dữ liệu nghiệp vụ nếu không có quy trình phù hợp.
- Không bỏ qua cảnh báo dữ liệu.
- Không để secret xuất hiện trong log.
- Không triển khai thay đổi chưa được kiểm thử.
- Mọi sự cố quan trọng phải được ghi nhận và truy vết.