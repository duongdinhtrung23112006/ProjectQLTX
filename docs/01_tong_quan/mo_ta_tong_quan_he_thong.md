# Mô tả tổng quan hệ thống

## 1. Tên hệ thống

Hệ thống quản lý trạm xăng có tích hợp AI.

Tên dự án kỹ thuật: ProjectQLTX.

---

## 2. Mục đích hệ thống

Hệ thống được xây dựng nhằm hỗ trợ quản lý các hoạt động nghiệp vụ chính
của một trạm xăng, bao gồm quản lý nhiên liệu, bồn chứa, nhập hàng,
bán hàng, tồn bồn, nhân viên, ca làm việc, doanh thu và các số liệu
nhập - xuất - tồn.

Hệ thống đồng thời tích hợp các chức năng AI nhằm hỗ trợ người dùng
tổng hợp, phân tích và phát hiện các dấu hiệu bất thường trong dữ liệu
hoạt động của trạm xăng.

AI chỉ đóng vai trò hỗ trợ phân tích và tổng hợp dữ liệu. Quyết định
nghiệp vụ cuối cùng thuộc về người dùng có thẩm quyền.

---

## 3. Người sử dụng hệ thống

Hệ thống hiện có ba vai trò chính:

- Quản lý
- Nhân viên ca
- Kế toán

Mỗi vai trò được cấp quyền truy cập và thực hiện các chức năng phù hợp
với trách nhiệm nghiệp vụ.

Chi tiết về vai trò và quyền hạn được mô tả trong:

`docs/02_phan_tich/vai_tro_nguoi_dung.md`

---

## 4. Các nhóm chức năng chính

### 4.1. Xác thực và phân quyền

- Đăng nhập hệ thống.
- Xác định vai trò người dùng.
- Kiểm soát quyền truy cập chức năng.

### 4.2. Quản lý nhiên liệu

- Quản lý thông tin mặt hàng nhiên liệu.
- Quản lý tên nhiên liệu
- Quản lý mã nhiên liệu.
- Quản lý đơn vị tính.
- Quản lý đơn giá.
- Quản lý trạng thái nhiên liệu.
- Quản lý các chức năng CRUD

### 4.3. Quản lý bồn chứa

- Quản lý thông tin bồn chứa (mã bồn, tên bồn, loại nhiên liệu).
- Liên kết bồn chứa với mặt hàng nhiên liệu (nhiên liệu được chọn ở bồn chứa liên kết tới nhiên liệu được tạo ở chức năng quản lý nhiên liệu).
- Theo dõi sức chứa.
- Theo dõi lượng tồn.
- Theo dõi trạng thái bồn.
- Quản lý các chức năng CRUD

### 4.4. Quản lý nhập hàng

- Ghi nhận lần nhập hàng.
- Xác định nhiên liệu và bồn nhận hàng.
- Ghi nhận số lượng nhập.
- Theo dõi trạng thái phiếu nhập.
- Duyệt hoặc từ chối phiếu nhập.
- Cập nhật tồn bồn khi phiếu nhập được duyệt.

### 4.5. Quản lý nhân viên

- Quản lý thông tin nhân viên.
- Theo dõi trạng thái nhân viên.
- Liên kết tài khoản với nhân viên.

### 4.6. Quản lý ca làm việc

- Quản lý ca làm việc.
- Phân công nhân viên vào ca.
- Theo dõi trạng thái ca.

### 4.7. Bán hàng và tồn bồn

Hệ thống có phạm vi quản lý hoạt động bán hàng và theo dõi tồn bồn
theo phạm vi nghiệp vụ được xác định trong tài liệu yêu cầu.

Cách ghi nhận bán hàng, cách tính tồn và các quy tắc liên quan phải
tuân theo tài liệu yêu cầu và trạng thái triển khai hiện tại của hệ thống.

Không tự suy đoán hoặc bổ sung nghiệp vụ chưa được xác định.

### 4.8. Tra cứu và thống kê

- Tra cứu doanh thu.
- Tra cứu số liệu nhập - xuất - tồn.
- Thống kê sản lượng bán.
- Thống kê chênh lệch tồn.
- Thống kê doanh thu.

### 4.9. Chức năng AI

Hệ thống định hướng tích hợp AI cho các nhóm chức năng:

- Sinh báo cáo từ dữ liệu hoạt động.
- Tóm tắt biến động tồn bồn.
- Phân tích số liệu.
- Phát hiện và cảnh báo các dấu hiệu bất thường.
- Hỗ trợ kiểm tra và giải thích dữ liệu.

Các chức năng AI phải sử dụng dữ liệu được hệ thống cung cấp và không
được tự tạo ra dữ liệu nghiệp vụ không tồn tại.

---

## 5. Công nghệ hiện tại

### Backend

- Python
- Flask

### Cơ sở dữ liệu

- MySQL

### Giao diện

- HTML
- CSS
- JavaScript
- Jinja Template

### Quản lý mã nguồn

- Git
- GitHub

### AI

Hệ thống có khả năng tích hợp LLM thông qua API hoặc các cơ chế tích hợp
AI phù hợp với kiến trúc được xác định trong tài liệu thiết kế.

Công nghệ AI cụ thể phải được xác định trong tài liệu thiết kế AI và
cấu hình dự án, không được Agent tự ý thay đổi nếu chưa có yêu cầu.

---

## 6. Kiến trúc tổng quát

Hệ thống được tổ chức theo mô hình ứng dụng web:

Người dùng
→ Giao diện web
→ Flask Backend
→ Các route xử lý nghiệp vụ
→ Service
→ MySQL

Đối với chức năng AI:

Người dùng hoặc chức năng nghiệp vụ
→ Flask Backend
→ AI Service
→ LLM/API AI
→ Kết quả AI
→ Backend kiểm tra và xử lý
→ Giao diện người dùng

AI không được phép tự ý thay đổi dữ liệu nghiệp vụ trong cơ sở dữ liệu
nếu chưa có cơ chế kiểm soát và xác nhận phù hợp.

---

## 7. Nguyên tắc phát triển

### 7.1. Không tự suy đoán

Agent phải dựa trên tài liệu trong thư mục `docs/` và mã nguồn thực tế.

Nếu thông tin cần thiết chưa được xác định, Agent phải nêu rõ phần
thiếu thay vì tự tạo giả định.

### 7.2. Không thay đổi ngoài phạm vi

Khi thực hiện một nhiệm vụ, Agent chỉ được thay đổi các file và chức năng
cần thiết cho nhiệm vụ đó.

Không tự ý tái cấu trúc toàn bộ hệ thống nếu không được yêu cầu.

### 7.3. Bảo mật

Không đưa mật khẩu, API key, token, dữ liệu cá nhân hoặc dữ liệu nhạy cảm
vào prompt gửi đến AI công cộng.

Thông tin bí mật phải được quản lý bằng biến môi trường hoặc cơ chế quản lý
secret phù hợp.

### 7.4. Human-in-the-loop

Mọi kết quả quan trọng do AI tạo ra phải được con người kiểm tra.

AI không thay thế quyết định nghiệp vụ của người quản lý.

### 7.5. Kiểm thử

Mọi chức năng do AI hỗ trợ xây dựng hoặc sửa đổi phải được kiểm thử trước
khi xác nhận hoàn thành.

---

## 8. Nguyên tắc dành cho AI Agent

Khi làm việc với ProjectQLTX, AI Agent phải:

1. Đọc tài liệu trong `docs/` liên quan đến nhiệm vụ.
2. Đọc mã nguồn hiện tại trước khi sửa.
3. Kiểm tra trạng thái hiện tại của chức năng.
4. Xác định các file cần thay đổi.
5. Nêu các rủi ro hoặc điểm chưa rõ nếu có.
6. Thực hiện thay đổi trong phạm vi nhiệm vụ.
7. Kiểm thử thay đổi.
8. Không tự tạo dữ liệu hoặc yêu cầu nghiệp vụ chưa được xác định.
9. Cập nhật tài liệu liên quan nếu thay đổi làm ảnh hưởng đến thiết kế
   hoặc yêu cầu.
10. Ghi nhận việc sử dụng AI vào nhật ký AI của dự án.

---

## 9. Các tài liệu nguồn liên quan

Các tài liệu chi tiết của hệ thống được tổ chức trong thư mục:

- `docs/01_tong_quan/`
- `docs/02_phan_tich/`
- `docs/03_thiet_ke/`
- `docs/04_so_do/`
- `docs/05_kiem_thu/`
- `docs/06_trien_khai/`
- `docs/07_ai/`
- `docs/08_trang_thai/`

Khi có mâu thuẫn giữa mô tả tổng quan và tài liệu chi tiết hơn, Agent phải
báo cáo mâu thuẫn và ưu tiên tài liệu có phạm vi chuyên biệt hơn sau khi
được người phát triển xác nhận.

---

## 10. Trạng thái tài liệu

Tài liệu này mô tả kiến trúc và phạm vi tổng quan của ProjectQLTX.

Trạng thái triển khai thực tế của từng chức năng được quản lý riêng trong:

`docs/08_trang_thai/`

Không sử dụng tài liệu này để suy luận rằng mọi chức năng được mô tả ở trên
đã hoàn thành.