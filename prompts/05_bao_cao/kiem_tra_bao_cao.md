# Prompt kiểm tra báo cáo

## 1. Mục đích

Kiểm tra báo cáo trước khi hoàn thiện nhằm phát hiện thiếu sót, mâu thuẫn và nội dung không phù hợp với hệ thống thực tế.

## 2. Context

Đọc:

- `bao_cao/cau_truc_bao_cao.md`
- `bao_cao/quy_dinh_trinh_bay.md`
- Toàn bộ tài liệu trong `docs/`
- Nội dung báo cáo hiện tại nếu đã có.
- Mã nguồn khi cần đối chiếu chức năng thực tế.

## 3. Nhiệm vụ

Kiểm tra các nhóm sau:

### Nội dung

- Đủ các chương và mục theo cấu trúc.
- Nội dung đúng phạm vi hệ thống.
- Mô tả đúng chức năng thực tế.
- Phân biệt rõ đã hoàn thành, đang phát triển và chưa thực hiện.

### Tính nhất quán

- Tên chức năng, vai trò và Use Case thống nhất.
- Nội dung giữa các chương không mâu thuẫn.
- Cơ sở dữ liệu, API, giao diện và chức năng được mô tả phù hợp.
- Nội dung AI phù hợp với thiết kế và chiến lược sử dụng AI.

### Tính chính xác

- Không có số liệu hoặc kết quả kiểm thử được tự tạo.
- Không có chức năng chưa thực hiện được mô tả như đã hoàn thành.
- Không có thông tin trái với mã nguồn hoặc tài liệu nguồn.

### Truy vết

Kiểm tra khả năng truy vết:

`Yêu cầu → Use Case/User Story → Thiết kế → Mã nguồn → Kiểm thử → Báo cáo`

## 4. Ràng buộc

- Không tự sửa nội dung nếu chưa xác định nguyên nhân.
- Không tự bổ sung dữ liệu còn thiếu.
- Không thay đổi phạm vi hoặc yêu cầu của hệ thống.
- Các vấn đề chưa đủ thông tin phải được đánh dấu để người dùng xác nhận.

## 5. Output

### Danh sách vấn đề

| Mức độ | Vị trí | Vấn đề | Nguồn đối chiếu | Đề xuất xử lý |
|---|---|---|---|---|

Mức độ:

- `Cao`: sai nội dung hoặc ảnh hưởng nghiêm trọng đến tính chính xác.
- `Trung bình`: thiếu hoặc không nhất quán.
- `Thấp`: lỗi trình bày hoặc chi tiết nhỏ.

### Kết luận kiểm tra

- Nội dung đạt.
- Nội dung cần sửa.
- Nội dung cần người dùng xác nhận.

## 6. Nguyên tắc

Báo cáo phải phản ánh đúng hệ thống thực tế, không phải mô tả một hệ thống được giả định là đã hoàn thành.