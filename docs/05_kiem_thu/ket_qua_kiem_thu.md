# Kết quả kiểm thử

## 1. Mục đích

Ghi nhận kết quả thực tế của các ca kiểm thử trong hệ thống.

Kết quả phải phản ánh đúng trạng thái kiểm thử, không tự đánh dấu `Đạt` khi chưa thực hiện.

---

## 2. Quy ước trạng thái

- `Chưa thực hiện`: Chưa chạy ca kiểm thử.
- `Đạt`: Kết quả thực tế phù hợp với kết quả mong đợi.
- `Không đạt`: Kết quả thực tế khác kết quả mong đợi.
- `Không áp dụng`: Ca kiểm thử không còn phù hợp với phiên bản hiện tại.

---

## 3. Bảng kết quả kiểm thử

| Mã TC | Chức năng | Kết quả mong đợi | Kết quả thực tế | Trạng thái | Ngày kiểm thử | Người kiểm thử | Mã lỗi |
|---|---|---|---|---|---|---|---|
| TC01 | Đăng nhập |  |  | Chưa thực hiện |  |  |  |
| TC02 | Đăng nhập |  |  | Chưa thực hiện |  |  |  |
| TC03 | Đăng nhập |  |  | Chưa thực hiện |  |  |  |
| TC04 | Phân quyền |  |  | Chưa thực hiện |  |  |  |
| TC05 | Phân quyền |  |  | Chưa thực hiện |  |  |  |
| TC06 | Phân quyền |  |  | Chưa thực hiện |  |  |  |
| TC07 | Phiên đăng nhập |  |  | Chưa thực hiện |  |  |  |
| TC08–TC20 | Nhiên liệu và bồn |  |  | Chưa thực hiện |  |  |  |
| TC21–TC33 | Nhập hàng |  |  | Chưa thực hiện |  |  |  |
| TC34–TC38 | Bán hàng |  |  | Chưa thực hiện |  |  |  |
| TC39–TC44 | Tồn và tra cứu |  |  | Chưa thực hiện |  |  |  |
| TC45–TC49 | Nhân viên và ca |  |  | Chưa thực hiện |  |  |  |
| TC50–TC58 | AI |  |  | Chưa thực hiện |  |  |  |
| TC59–TC63 | Lỗi và bảo mật |  |  | Chưa thực hiện |  |  |  |

Khi thực hiện kiểm thử, các nhóm TC có thể được tách thành từng dòng riêng để ghi nhận chính xác.

---

## 4. Tổng hợp kết quả

Sau mỗi lần kiểm thử, cập nhật:

- Tổng số ca kiểm thử.
- Số ca đã thực hiện.
- Số ca đạt.
- Số ca không đạt.
- Số ca chưa thực hiện.
- Số ca không áp dụng.
- Số lỗi phát hiện.

Không sử dụng tỷ lệ hoặc số liệu tổng hợp khi chưa có dữ liệu kiểm thử thực tế.

---

## 5. Kết quả kiểm thử theo nhóm

### 5.1. Đăng nhập và phân quyền

Theo dõi TC01–TC07.

Kiểm tra:
- Đăng nhập.
- Phiên đăng nhập.
- Quyền của từng vai trò.
- Truy cập trái phép.

### 5.2. Nhiên liệu và bồn

Theo dõi TC08–TC20.

Kiểm tra:
- Dữ liệu nhiên liệu.
- Liên kết nhiên liệu với bồn.
- Sức chứa.
- Tồn hiện tại.
- Các giá trị biên.

### 5.3. Nhập hàng

Theo dõi TC21–TC33.

Kiểm tra:
- Tạo phiếu.
- Phê duyệt.
- Từ chối.
- Xóa phiếu.
- Cập nhật tồn.
- Trạng thái phiếu.

### 5.4. Bán hàng

Theo dõi TC34–TC38.

Kiểm tra:
- Tạo giao dịch.
- Số lượng bán.
- Thành tiền.
- Kiểm tra tồn trước khi bán.

### 5.5. Tồn và thống kê

Theo dõi TC39–TC44.

Kiểm tra:
- Tồn cuối.
- Tổng nhập.
- Tổng bán.
- Doanh thu.
- Nhập - xuất - tồn.
- Thống kê hoạt động.

### 5.6. Nhân viên và ca

Theo dõi TC45–TC49.

Kiểm tra:
- Thông tin nhân viên.
- Mã nhân viên.
- Tạo ca.
- Phân công ca.
- Tra cứu ca.

### 5.7. AI

Theo dõi TC50–TC58.

Kiểm tra:
- Báo cáo AI.
- Tóm tắt tồn.
- Cảnh báo bất thường.
- Tính chính xác số liệu.
- Khả năng chống bịa dữ liệu.
- Giới hạn quyền của AI.

Các chức năng AI chưa được triển khai chỉ được đánh dấu `Chưa thực hiện`, không đánh dấu `Đạt`.

---

## 6. Ghi nhận kết quả không đạt

Khi một ca kiểm thử không đạt, phải ghi:

- Mã TC.
- Mô tả lỗi.
- Dữ liệu đầu vào.
- Các bước thực hiện.
- Kết quả mong đợi.
- Kết quả thực tế.
- Mức độ nghiêm trọng.
- Mã lỗi.
- Trạng thái xử lý.

Thông tin chi tiết được lưu trong:

`docs/05_kiem_thu/danh_sach_loi.md`

---

## 7. Kiểm thử lại sau khi sửa lỗi

Sau khi lỗi được sửa:

1. Chạy lại ca kiểm thử đã thất bại.
2. Ghi nhận kết quả mới.
3. Cập nhật trạng thái lỗi.
4. Kiểm thử hồi quy các chức năng liên quan.

Không xóa kết quả kiểm thử cũ; cần giữ lịch sử để truy vết thay đổi.

---

## 8. Đánh giá kết quả AI

Kết quả AI được kiểm tra theo các tiêu chí:

- Đúng số liệu nguồn.
- Đúng phạm vi dữ liệu được cung cấp.
- Không tự tạo dữ liệu.
- Nội dung phù hợp với yêu cầu.
- Không thực hiện hành động nghiệp vụ trái quyền.
- Có thể truy ngược kết quả về dữ liệu nguồn.

Nếu AI đưa ra thông tin không có căn cứ, phải ghi nhận là lỗi hoặc kết quả không đạt tùy trường hợp.

---

## 9. Kết luận kiểm thử

Chỉ đưa ra kết luận tổng thể sau khi có kết quả kiểm thử thực tế.

Kết luận phải dựa trên:
- Các ca đã thực hiện.
- Số ca đạt và không đạt.
- Các lỗi còn tồn tại.
- Mức độ ảnh hưởng của lỗi.
- Các chức năng chưa được kiểm thử.

Không kết luận hệ thống đạt yêu cầu khi vẫn còn dữ liệu kiểm thử chưa được thực hiện hoặc còn lỗi nghiêm trọng chưa được xử lý.