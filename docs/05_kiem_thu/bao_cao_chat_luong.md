# Báo cáo chất lượng

## 1. Mục đích

Tổng hợp tình trạng chất lượng của hệ thống dựa trên kết quả kiểm thử thực tế.

Báo cáo không tự tạo số liệu. Các chỉ số chỉ được cập nhật sau khi có kết quả kiểm thử.

---

## 2. Phạm vi đánh giá

Đánh giá các nhóm:

- Đăng nhập và phân quyền.
- Quản lý nhiên liệu.
- Quản lý bồn chứa.
- Nhập hàng.
- Bán hàng.
- Tồn bồn.
- Nhân viên và ca làm việc.
- Tra cứu và thống kê.
- Chức năng AI.
- Xử lý lỗi và bảo mật.

---

## 3. Chỉ số kiểm thử

| Chỉ số | Giá trị |
|---|---:|
| Tổng số ca kiểm thử | Chưa cập nhật |
| Đã thực hiện | Chưa cập nhật |
| Đạt | Chưa cập nhật |
| Không đạt | Chưa cập nhật |
| Chưa thực hiện | Chưa cập nhật |
| Không áp dụng | Chưa cập nhật |
| Tổng số lỗi | Chưa cập nhật |
| Lỗi nghiêm trọng | Chưa cập nhật |
| Lỗi cao | Chưa cập nhật |
| Lỗi trung bình | Chưa cập nhật |
| Lỗi thấp | Chưa cập nhật |

Không thay thế `Chưa cập nhật` bằng số liệu khi chưa có kết quả thực tế.

---

## 4. Đánh giá theo nhóm chức năng

### 4.1. Đăng nhập và phân quyền

Đánh giá:
- Đăng nhập đúng và sai.
- Kiểm tra phiên đăng nhập.
- Phân quyền theo vai trò.
- Ngăn truy cập trái phép.

Kết quả: Chưa cập nhật.

### 4.2. Nhiên liệu và bồn chứa

Đánh giá:
- Tính hợp lệ của dữ liệu.
- Quan hệ giữa nhiên liệu và bồn.
- Sức chứa.
- Tồn hiện tại.
- Các trường hợp biên.

Kết quả: Chưa cập nhật.

### 4.3. Nhập hàng

Đánh giá:
- Tạo phiếu.
- Phê duyệt.
- Từ chối.
- Xóa phiếu chờ duyệt.
- Cập nhật tồn sau khi phê duyệt.
- Không cập nhật tồn khi từ chối.

Kết quả: Chưa cập nhật.

### 4.4. Bán hàng và tồn bồn

Đánh giá:
- Ghi nhận bán hàng theo ngày.
- Tính thành tiền.
- Kiểm tra tồn trước khi bán.
- Tính tồn cuối.
- Tra cứu nhập - xuất - tồn.

Kết quả: Chưa cập nhật.

### 4.5. Tra cứu và thống kê

Đánh giá:
- Doanh thu.
- Tổng nhập.
- Tổng bán.
- Tồn.
- Chênh lệch tồn.
- Thống kê theo khoảng thời gian.

Kết quả: Chưa cập nhật.

### 4.6. AI

Đánh giá:

- Độ chính xác số liệu.
- Tính phù hợp của nội dung.
- Tính nhất quán.
- Khả năng chống hallucination.
- Khả năng phát hiện bất thường.
- Tuân thủ giới hạn quyền.
- Khả năng truy vết về dữ liệu nguồn.

Kết quả: Chưa cập nhật.

---

## 5. Chất lượng dữ liệu

Kiểm tra:

- Tính đúng đắn.
- Tính đầy đủ.
- Tính nhất quán.
- Tính hợp lệ.
- Quan hệ giữa các bảng.
- Tính chính xác của các phép tính nghiệp vụ.

Các công thức chính:

`Thành tiền = Số lượng bán × Đơn giá`

`Tồn cuối = Tồn đầu + Tổng nhập - Tổng bán`

`Chênh lệch = Tồn thực tế - Tồn theo hệ thống`

---

## 6. Chất lượng AI

Kết quả AI phải được đánh giá dựa trên dữ liệu nguồn.

Các tiêu chí:

| Tiêu chí | Nội dung |
|---|---|
| Độ chính xác | Số liệu và nội dung phù hợp dữ liệu nguồn |
| Tính liên quan | Đúng yêu cầu được giao |
| Tính nhất quán | Kết quả hợp lý giữa các lần xử lý |
| Hallucination | Không tự tạo dữ liệu |
| An toàn | Không thực hiện hành động ngoài quyền |
| Truy vết | Có thể xác định nguồn dữ liệu sử dụng |

AI chỉ đóng vai trò phân tích và hỗ trợ. Quyết định nghiệp vụ cuối cùng thuộc người dùng có thẩm quyền.

---

## 7. Chất lượng bảo mật

Kiểm tra:

- Xác thực người dùng.
- Phân quyền.
- Bảo vệ các route.
- Không để lộ mật khẩu.
- Không để lộ API key.
- Xử lý lỗi CSDL an toàn.
- Ngăn thao tác vượt quyền.

---

## 8. Lỗi còn tồn tại

Liệt kê các lỗi chưa đóng từ:

`docs/05_kiem_thu/danh_sach_loi.md`

| Mã lỗi | Mức độ | Chức năng | Trạng thái | Ảnh hưởng |
|---|---|---|---|---|
|  |  |  |  |  |

---

## 9. Đánh giá phiên bản

Mỗi phiên bản cần ghi:

- Phiên bản.
- Ngày đánh giá.
- Số ca kiểm thử.
- Số ca đạt.
- Số ca không đạt.
- Lỗi còn tồn tại.
- Chức năng chưa kiểm thử.
- Thay đổi kể từ phiên bản trước.
- Kết luận phạm vi chất lượng.

---

## 10. Kết luận

Kết luận chất lượng chỉ được đưa ra sau khi có dữ liệu kiểm thử thực tế.

Kết luận phải nêu rõ:

- Những chức năng đã kiểm thử.
- Những chức năng đạt.
- Những chức năng chưa đạt.
- Các lỗi còn tồn tại.
- Các chức năng chưa kiểm thử.
- Các vấn đề cần xử lý trước phiên bản tiếp theo.

Không sử dụng kết quả kiểm thử để khẳng định hệ thống hoàn toàn không có lỗi.