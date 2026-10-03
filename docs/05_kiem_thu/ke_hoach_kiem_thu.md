# Kế hoạch kiểm thử

## 1. Mục đích

Xác định phạm vi, phương pháp và tiêu chí kiểm thử cho hệ thống quản lý trạm xăng có tích hợp AI.

Mục tiêu:
- Kiểm tra hệ thống thực hiện đúng yêu cầu chức năng.
- Kiểm tra các quy tắc nghiệp vụ.
- Kiểm tra phân quyền.
- Kiểm tra tính đúng đắn của các phép tính.
- Kiểm tra các chức năng AI.
- Phát hiện và ghi nhận lỗi.
- Đảm bảo thay đổi mã nguồn không làm hỏng chức năng đã hoàn thành.

---

## 2. Phạm vi kiểm thử

### 2.1. Chức năng được kiểm thử

- Đăng nhập.
- Phân quyền.
- Quản lý nhiên liệu.
- Quản lý bồn chứa.
- Nhập hàng.
- Phê duyệt và từ chối nhập hàng.
- Bán hàng theo ngày.
- Theo dõi tồn bồn.
- Quản lý nhân viên.
- Quản lý ca làm việc.
- Tra cứu doanh thu.
- Tra cứu nhập - xuất - tồn.
- Thống kê hoạt động.
- Sinh báo cáo bằng AI.
- Tóm tắt biến động tồn bồn bằng AI.
- Cảnh báo số liệu bất thường bằng AI.

### 2.2. Ngoài phạm vi

Không kiểm thử các chức năng chưa thuộc phạm vi hệ thống, gồm:

- Quản lý khách hàng.
- Thanh toán điện tử.
- Điều khiển thiết bị vật lý.
- Quyết định nghiệp vụ tự động bằng AI.
- Kế toán đầy đủ ngoài phạm vi thống kê doanh thu.

---

## 3. Các cấp độ kiểm thử

### 3.1. Kiểm thử đơn vị

Kiểm tra từng hàm hoặc thành phần nhỏ.

Ví dụ:
- Hàm tính thành tiền.
- Hàm tính tồn cuối.
- Hàm kiểm tra quyền.
- Hàm chuẩn hóa vai trò.
- Hàm kiểm tra sức chứa bồn.

### 3.2. Kiểm thử tích hợp

Kiểm tra sự phối hợp giữa các thành phần.

Ví dụ:

`Route → Service → CSDL`

hoặc:

`Business Service → AI Service → Kết quả AI`

### 3.3. Kiểm thử hệ thống

Kiểm tra toàn bộ chức năng từ giao diện đến CSDL.

Ví dụ:

`Đăng nhập → Phân quyền → Thực hiện nghiệp vụ → Hiển thị kết quả`

### 3.4. Kiểm thử chấp nhận

Kiểm tra hệ thống theo yêu cầu và tiêu chí chấp nhận đã xác định trong User Story.

---

## 4. Phương pháp kiểm thử

### Kiểm thử chức năng

Kiểm tra đầu vào, xử lý và đầu ra của từng chức năng.

### Kiểm thử biên

Kiểm tra các giá trị tại giới hạn.

Ví dụ:

- Số lượng bằng 0.
- Tồn bồn bằng 0.
- Tồn bồn bằng đúng sức chứa.
- Nhập hàng khiến tồn vừa bằng sức chứa.
- Nhập hàng khiến tồn vượt sức chứa.

### Kiểm thử dữ liệu không hợp lệ

Kiểm tra:
- Dữ liệu bắt buộc bị bỏ trống.
- Số lượng âm.
- Mã bị trùng.
- Nhiên liệu không tồn tại.
- Bồn không tồn tại.
- Tài khoản không hợp lệ.

### Kiểm thử phân quyền

Kiểm tra từng vai trò chỉ được thực hiện các chức năng được phép.

### Kiểm thử hồi quy

Sau khi sửa lỗi hoặc thêm chức năng, chạy lại các ca kiểm thử liên quan để đảm bảo chức năng cũ vẫn hoạt động.

---

## 5. Kiểm thử các quy tắc nghiệp vụ

### 5.1. Tồn bồn

Kiểm tra:

`Tồn cuối = Tồn đầu + Tổng nhập - Tổng bán`

### 5.2. Sức chứa

Kiểm tra:

`Tồn hiện tại <= Sức chứa`

### 5.3. Phê duyệt nhập hàng

Chỉ phiếu `Chờ duyệt` mới được phê duyệt.

Khi phê duyệt thành công:
- Tồn bồn tăng.
- Phiếu chuyển thành `Đã duyệt`.

### 5.4. Từ chối nhập hàng

Khi từ chối:
- Phiếu chuyển thành `Từ chối`.
- Tồn bồn không thay đổi.

### 5.5. Xóa phiếu nhập

Chỉ phiếu `Chờ duyệt` được xóa.

### 5.6. Doanh thu

Kiểm tra:

`Thành tiền = Số lượng bán × Đơn giá`

và:

`Doanh thu = SUM(Thành tiền)`

---

## 6. Kiểm thử phân quyền

### Quản lý

Được kiểm tra các chức năng:
- Quản lý nhiên liệu.
- Quản lý bồn.
- Quản lý nhân viên.
- Quản lý ca.
- Quản lý nhập hàng.
- Phê duyệt / từ chối nhập hàng.
- Thống kê.
- Chức năng AI.

### Nhân viên ca

Được kiểm tra:
- Xem bồn.
- Xem nhiên liệu.
- Ghi nhận nhập hàng.
- Ghi nhận bán hàng.
- Theo dõi tồn.
- Xem ca được phân công.

### Kế toán

Được kiểm tra:
- Tra cứu doanh thu.
- Tra cứu nhập - xuất - tồn.
- Thống kê hoạt động.

Người dùng không có quyền phải nhận phản hồi từ chối truy cập và không được thực hiện nghiệp vụ.

---

## 7. Kiểm thử chức năng AI

### 7.1. Độ chính xác dữ liệu

Kiểm tra các số liệu trong kết quả AI có khớp dữ liệu đầu vào hay không.

### 7.2. Tính phù hợp

Kiểm tra AI có trả lời đúng yêu cầu được giao hay không.

### 7.3. Tính nhất quán

Cùng một bộ dữ liệu và yêu cầu phải tạo ra kết quả phù hợp với nhau.

### 7.4. Hallucination

Kiểm tra AI có:
- Tự tạo số liệu.
- Tự tạo giao dịch.
- Tự thêm dữ liệu không tồn tại.
- Đưa ra kết luận không có căn cứ.

### 7.5. An toàn

Kiểm tra AI có tuân thủ giới hạn:
- Không sửa dữ liệu.
- Không phê duyệt giao dịch.
- Không thay đổi tồn.
- Không thay thế người quyết định.

---

## 8. Dữ liệu kiểm thử

Dữ liệu kiểm thử phải đủ để kiểm tra:

- Dữ liệu hợp lệ.
- Dữ liệu không hợp lệ.
- Dữ liệu biên.
- Nhiều loại nhiên liệu.
- Nhiều bồn chứa.
- Nhiều nhân viên.
- Nhiều phiếu nhập.
- Phiếu ở các trạng thái khác nhau.
- Nhiều giao dịch bán hàng.
- Dữ liệu có biến động tồn.
- Dữ liệu có khả năng tạo cảnh báo.

Không sử dụng mật khẩu thật, API key hoặc dữ liệu bí mật trong bộ dữ liệu kiểm thử.

---

## 9. Tiêu chí đạt

Một chức năng được xem là đạt khi:

- Thực hiện đúng yêu cầu.
- Kết quả đúng với dữ liệu đầu vào.
- Tuân thủ quy tắc nghiệp vụ.
- Phân quyền đúng.
- Không gây lỗi cho chức năng liên quan.
- Các trường hợp lỗi được xử lý phù hợp.

Đối với AI, ngoài các tiêu chí trên cần kiểm tra:
- Không tự tạo dữ liệu.
- Có căn cứ từ dữ liệu đầu vào.
- Đúng định dạng yêu cầu.
- Không thực hiện hành động nghiệp vụ ngoài quyền hạn.

---

## 10. Quy trình kiểm thử

1. Xác định yêu cầu cần kiểm thử.
2. Xác định điều kiện đầu vào.
3. Chuẩn bị dữ liệu.
4. Thực hiện ca kiểm thử.
5. Ghi nhận kết quả thực tế.
6. So sánh với kết quả mong đợi.
7. Đánh dấu `Đạt` hoặc `Không đạt`.
8. Nếu lỗi, tạo bản ghi trong danh sách lỗi.
9. Sửa lỗi.
10. Kiểm thử lại.
11. Thực hiện kiểm thử hồi quy đối với các chức năng liên quan.

---

## 11. Liên kết với tài liệu khác

Kế hoạch kiểm thử sử dụng các tài liệu:

- `docs/02_phan_tich/yeu_cau_chuc_nang.md`
- `docs/02_phan_tich/yeu_cau_phi_chuc_nang.md`
- `docs/02_phan_tich/quy_tac_nghiep_vu.md`
- `docs/02_phan_tich/danh_sach_use_case.md`
- `docs/02_phan_tich/user_story.md`
- `docs/02_phan_tich/ma_tran_truy_vet.md`

Kết quả kiểm thử được ghi vào:

- `docs/05_kiem_thu/danh_sach_ca_kiem_thu.md`
- `docs/05_kiem_thu/ket_qua_kiem_thu.md`
- `docs/05_kiem_thu/danh_sach_loi.md`
- `docs/05_kiem_thu/bao_cao_chat_luong.md`

---

## 12. Nguyên tắc

Kiểm thử phải dựa trên yêu cầu và dữ liệu đã được xác định, không tạo ra yêu cầu mới chỉ để làm cho kết quả kiểm thử đẹp hơn.

Mọi lỗi phát hiện phải có khả năng truy ngược về:
- Chức năng.
- Yêu cầu.
- Ca kiểm thử.
- Kết quả thực tế.
- Cách xử lý lỗi.