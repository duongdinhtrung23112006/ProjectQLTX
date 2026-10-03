# Prompt kiểm tra yêu cầu

## 1. Mục đích

Kiểm tra chất lượng và tính nhất quán của các yêu cầu hệ thống trước khi sử dụng làm cơ sở thiết kế và lập trình.

## 2. Context

Đọc:

- `docs/01_tong_quan/`
- `docs/02_phan_tich/`
- `docs/03_thiet_ke/`
- `docs/08_trang_thai/`

Đối chiếu với mã nguồn hiện tại nếu cần.

## 3. Nhiệm vụ

Kiểm tra:

1. Yêu cầu có rõ ràng và có thể kiểm thử hay không.
2. Yêu cầu có mâu thuẫn với nhau hay không.
3. FR có Use Case tương ứng hay không.
4. Use Case có User Story tương ứng hay không.
5. User Story có tiêu chí chấp nhận hay không.
6. Yêu cầu có phù hợp với phạm vi hệ thống hay không.
7. Yêu cầu có thể truy vết đến kiểm thử hay không.
8. Phát hiện yêu cầu thiếu, trùng hoặc chưa xác định.

## 4. Ràng buộc

- Không tự sửa yêu cầu.
- Không tự bổ sung nghiệp vụ.
- Không thay đổi phạm vi.
- Không coi đề xuất của AI là yêu cầu chính thức.
- Khi phát hiện vấn đề phải chỉ rõ tài liệu và mã liên quan.

## 5. Output

### Yêu cầu đạt
Danh sách yêu cầu không phát hiện vấn đề.

### Yêu cầu cần xem xét
| Mã | Vấn đề | Tài liệu | Mức độ |
|---|---|---|---|

### Mâu thuẫn
Mô tả các yêu cầu mâu thuẫn và nguồn liên quan.

### Thiếu truy vết
Các FR/UC/User Story chưa có liên kết đầy đủ.

### Đề xuất
Chỉ đưa ra đề xuất khi cần và đánh dấu rõ là đề xuất.

### Kết luận
Đánh giá liệu bộ yêu cầu hiện tại có đủ cơ sở để chuyển sang bước tiếp theo hay chưa.