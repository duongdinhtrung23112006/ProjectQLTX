# Prompt tái cấu trúc

## 1. Mục đích

Hướng dẫn AI Agent cải thiện cấu trúc mã nguồn mà không thay đổi hành vi nghiệp vụ của hệ thống.

## 2. Context

Trước khi tái cấu trúc, đọc:

- Mã nguồn liên quan.
- `docs/03_thiet_ke/`.
- `docs/08_trang_thai/`.
- Các test hiện có.

## 3. Nhiệm vụ

AI Agent phải:

1. Xác định vấn đề trong cấu trúc hiện tại.
2. Xác định nguyên nhân cần tái cấu trúc.
3. Xác định phạm vi ảnh hưởng.
4. Đề xuất cấu trúc mới.
5. Thực hiện thay đổi từng bước.
6. Giữ nguyên hành vi nghiệp vụ.
7. Chạy các test liên quan.
8. Kiểm tra hồi quy sau thay đổi.

## 4. Ràng buộc

- Không thay đổi yêu cầu nghiệp vụ.
- Không tự thêm chức năng.
- Không thay đổi công nghệ nếu chưa được yêu cầu.
- Không xóa code đang được sử dụng khi chưa xác định phụ thuộc.
- Không thay đổi database chỉ vì mục đích làm code đẹp hơn nếu chưa cần thiết.
- Ưu tiên thay đổi nhỏ, dễ kiểm tra và có thể quay lui.

## 5. Output

### Vấn đề hiện tại
Mô tả cấu trúc cần cải thiện.

### Phương án
Mô tả cấu trúc sau khi tái cấu trúc.

### File thay đổi

| File | Thao tác | Mục đích |
|---|---|---|
| | | |

### Kiểm thử

- Kiểm tra chức năng trước và sau.
- Chạy test liên quan.
- Kiểm tra hồi quy.
- Kiểm tra lỗi phát sinh.

### Truy vết

`Vấn đề → Phương án → Code → Test`

### Kết luận

Xác nhận hành vi nghiệp vụ được giữ nguyên hoặc nêu rõ phần bị ảnh hưởng.