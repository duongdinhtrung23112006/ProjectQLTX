# Danh sách lỗi

## 1. Mục đích

Ghi nhận, phân loại và theo dõi các lỗi phát hiện trong quá trình kiểm thử hệ thống.

Mỗi lỗi phải có khả năng truy ngược về ca kiểm thử và chức năng liên quan.

---

## 2. Quy ước mức độ lỗi

| Mức độ | Mô tả |
|---|---|
| Nghiêm trọng | Làm hệ thống không thể sử dụng hoặc gây mất/sai dữ liệu quan trọng |
| Cao | Làm một chức năng chính không thể hoạt động đúng |
| Trung bình | Làm chức năng hoạt động không đúng trong một số trường hợp |
| Thấp | Lỗi giao diện, thông báo hoặc vấn đề ít ảnh hưởng đến nghiệp vụ |

---

## 3. Trạng thái lỗi

- `Mới`: Vừa phát hiện.
- `Đã xác nhận`: Đã kiểm tra và xác nhận lỗi.
- `Đang sửa`: Đang xử lý.
- `Đã sửa`: Đã có thay đổi để sửa lỗi.
- `Đã kiểm thử lại`: Đã kiểm tra sau khi sửa.
- `Đã đóng`: Lỗi được xác nhận đã xử lý.
- `Không sửa`: Có lý do rõ ràng và được ghi nhận.

---

## 4. Danh sách lỗi

| Mã lỗi | Mã TC | Chức năng | Mô tả lỗi | Mức độ | Trạng thái | Người xử lý |
|---|---|---|---|---|---|---|
| BUG001 |  |  |  |  | Mới |  |
| BUG002 |  |  |  |  | Mới |  |
| BUG003 |  |  |  |  | Mới |  |

Chỉ thêm lỗi khi lỗi thực tế được phát hiện trong quá trình kiểm thử.

---

## 5. Thông tin chi tiết của một lỗi

Mỗi lỗi cần ghi:

### BUGxxx

- **Mã lỗi:** BUGxxx
- **Mã ca kiểm thử:** TCxxx
- **Chức năng:** 
- **Ngày phát hiện:** 
- **Người phát hiện:** 
- **Mức độ:** 
- **Môi trường:** 
- **Dữ liệu đầu vào:** 
- **Các bước tái hiện:**
  1. 
  2. 
  3. 
- **Kết quả mong đợi:** 
- **Kết quả thực tế:** 
- **Nguyên nhân:** 
- **Cách xử lý:** 
- **Phiên bản sửa lỗi:** 
- **Kết quả kiểm thử lại:** 
- **Trạng thái:** 

---

## 6. Lỗi liên quan đến dữ liệu

Đặc biệt theo dõi các lỗi:

- Tồn bồn âm.
- Tồn bồn vượt sức chứa.
- Phê duyệt nhập hàng nhưng không cập nhật tồn.
- Tồn bị cập nhật nhiều lần.
- Phiếu bị thay đổi trạng thái sai.
- Doanh thu tính sai.
- Thành tiền tính sai.
- Tổng nhập hoặc tổng bán sai.
- Dữ liệu giữa các bảng không nhất quán.

---

## 7. Lỗi phân quyền và bảo mật

Theo dõi các trường hợp:

- Người dùng truy cập chức năng không được phép.
- Người chưa đăng nhập truy cập chức năng bảo vệ.
- Người dùng có thể thực hiện thao tác vượt quyền.
- Dữ liệu nhạy cảm xuất hiện trong phản hồi không phù hợp.
- Mật khẩu hoặc API key xuất hiện trong mã nguồn.
- Lỗi CSDL làm lộ thông tin nhạy cảm.

---

## 8. Lỗi liên quan đến AI

Theo dõi:

- AI tạo số liệu không có trong dữ liệu nguồn.
- AI hiểu sai dữ liệu.
- AI đưa ra kết luận không có căn cứ.
- AI không phát hiện dữ liệu bất thường khi có đủ dữ liệu.
- AI cảnh báo khi không có dấu hiệu bất thường.
- AI trả về sai định dạng.
- AI cố thực hiện thao tác nghiệp vụ ngoài quyền hạn.
- Kết quả AI không thể truy ngược về dữ liệu nguồn.

---

## 9. Quy trình xử lý lỗi

1. Phát hiện lỗi.
2. Tạo mã lỗi.
3. Liên kết lỗi với ca kiểm thử.
4. Xác định mức độ.
5. Xác nhận và phân tích nguyên nhân.
6. Sửa lỗi.
7. Kiểm thử lại.
8. Kiểm thử hồi quy nếu cần.
9. Cập nhật trạng thái.
10. Đóng lỗi khi kết quả đạt yêu cầu.

---

## 10. Nguyên tắc

- Không xóa lỗi đã ghi nhận.
- Không tự tạo lỗi chưa phát hiện.
- Không đánh dấu `Đã sửa` nếu chưa có thay đổi tương ứng.
- Không đánh dấu `Đã đóng` nếu chưa kiểm thử lại.
- Mỗi lỗi phải có khả năng truy ngược về yêu cầu hoặc ca kiểm thử liên quan.