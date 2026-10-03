# Prompt sinh chức năng

## 1. Mục đích

Hướng dẫn AI Agent triển khai một chức năng mới dựa trên yêu cầu và cấu trúc hiện có của dự án.

## 2. Context

Trước khi lập trình, đọc:

- Yêu cầu trong `docs/02_phan_tich/`.
- Thiết kế liên quan trong `docs/03_thiet_ke/`.
- Sơ đồ đặc tả trong `docs/04_so_do/`.
- Trạng thái hiện tại trong `docs/08_trang_thai/`.
- Mã nguồn và database liên quan.

## 3. Input

Người dùng cung cấp:

- Mã FR/UC/User Story.
- Mô tả chức năng.
- Điều kiện hoặc quy tắc nghiệp vụ bổ sung nếu có.

## 4. Nhiệm vụ

AI Agent phải:

1. Phân tích yêu cầu trước khi viết code.
2. Xác định file cần tạo hoặc sửa.
3. Kiểm tra các module và hàm đang tồn tại.
4. Triển khai theo kiến trúc hiện tại.
5. Không tạo file hoặc cấu trúc trùng lặp.
6. Cập nhật database/API/UI khi chức năng yêu cầu.
7. Xử lý lỗi và kiểm tra dữ liệu đầu vào.
8. Tạo hoặc cập nhật test liên quan.
9. Cập nhật tài liệu nếu thay đổi ảnh hưởng đến thiết kế.

## 5. Ràng buộc

- Không thay đổi công nghệ nếu chưa được yêu cầu.
- Không tự thêm nghiệp vụ.
- Không phá vỡ chức năng hiện có.
- Không hard-code mật khẩu, API key hoặc secret.
- Tuân thủ phân quyền hiện tại.
- Dữ liệu nghiệp vụ phải được kiểm tra trước khi ghi.
- Nếu yêu cầu chưa rõ, dừng tại phần phân tích và nêu vấn đề.

## 6. Output

Trả kết quả theo thứ tự:

### Phân tích
Mô tả cách triển khai.

### File thay đổi
| File | Thao tác | Mục đích |
|---|---|---|
| | Tạo/Sửa | |

### Code
Cung cấp nội dung hoặc phần thay đổi của từng file.

### Kiểm thử
Nêu các trường hợp cần kiểm tra.

### Truy vết
`FR → UC → User Story → Code → Test`

### Ghi chú
Nêu các điểm cần người dùng kiểm tra hoặc phê duyệt.