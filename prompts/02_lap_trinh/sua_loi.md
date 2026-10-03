# Prompt sửa lỗi

## 1. Mục đích

Hướng dẫn AI Agent phân tích và sửa lỗi trong mã nguồn mà không làm ảnh hưởng đến các chức năng đang hoạt động.

## 2. Input

Cung cấp:

- Mô tả lỗi.
- Thông báo lỗi hoặc log nếu có.
- File hoặc chức năng xảy ra lỗi.
- Các bước tái hiện lỗi nếu có.

AI Agent phải đọc mã nguồn liên quan và tài liệu `docs/` trước khi sửa.

## 3. Nhiệm vụ

AI Agent phải:

1. Xác định cách tái hiện lỗi.
2. Phân tích nguyên nhân gốc.
3. Xác định phạm vi ảnh hưởng.
4. Đề xuất cách sửa.
5. Thực hiện sửa đúng phạm vi.
6. Kiểm tra các phần code liên quan.
7. Tạo hoặc cập nhật test để xác nhận lỗi đã được sửa.
8. Kiểm tra hồi quy các chức năng bị ảnh hưởng.

## 4. Ràng buộc

- Không chỉ sửa triệu chứng nếu có thể xác định nguyên nhân gốc.
- Không thay đổi nghiệp vụ ngoài phạm vi lỗi.
- Không xóa kiểm tra hoặc xử lý lỗi chỉ để làm lỗi biến mất.
- Không hard-code secret.
- Không tự ý thay đổi database nếu chưa xác định rõ tác động.
- Không đánh dấu lỗi đã sửa khi chưa kiểm thử.

## 5. Output

### Nguyên nhân
Mô tả nguyên nhân gốc và vị trí liên quan.

### Phạm vi ảnh hưởng
Liệt kê các file, chức năng hoặc dữ liệu có liên quan.

### Thay đổi
| File | Thay đổi | Lý do |
|---|---|---|
| | | |

### Kiểm thử
- Bước tái hiện lỗi.
- Kết quả trước khi sửa.
- Kết quả sau khi sửa.
- Kiểm thử hồi quy.

### Truy vết
`BUG → FR/UC → Code → Test`

### Kết luận
Nêu rõ lỗi đã được kiểm tra hay vẫn cần xử lý thêm.