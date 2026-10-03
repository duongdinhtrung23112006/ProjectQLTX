# Prompt sinh mã kiểm thử

## 1. Mục đích

Hướng dẫn AI Agent sinh mã kiểm thử dựa trên ca kiểm thử và mã nguồn hiện tại.

## 2. Context

Đọc:

- `docs/02_phan_tich/`
- `docs/05_kiem_thu/`
- Mã nguồn liên quan.
- Cấu hình và thư viện kiểm thử hiện tại.

## 3. Nhiệm vụ

AI Agent phải:

1. Xác định chức năng cần kiểm thử.
2. Đối chiếu với các Test Case.
3. Kiểm tra cấu trúc mã nguồn hiện tại.
4. Xác định framework kiểm thử đang sử dụng.
5. Sinh test cho các trường hợp hợp lệ và không hợp lệ.
6. Kiểm tra các quy tắc nghiệp vụ quan trọng.
7. Bổ sung test cho lỗi đã phát hiện nếu phù hợp.
8. Chạy hoặc hướng dẫn chạy test.
9. Báo cáo kết quả thực tế.

## 4. Ràng buộc

- Không tự tạo kết quả test.
- Không sửa mã nguồn nghiệp vụ chỉ để test đạt.
- Không bỏ qua test lỗi hoặc trường hợp biên.
- Không tạo dữ liệu giả gây hiểu nhầm là dữ liệu thực tế.
- Tuân thủ cấu trúc test hiện có.
- Không thêm thư viện mới nếu chưa cần thiết.

## 5. Output

### Phân tích

Xác định chức năng và các Test Case cần triển khai.

### File kiểm thử

| File | Thao tác | Mục đích |
|---|---|---|
| | Tạo/Sửa | |

### Mã kiểm thử

Cung cấp code hoàn chỉnh cho từng file.

### Cách chạy

Nêu lệnh chạy test và điều kiện cần thiết.

### Kết quả

Chỉ ghi kết quả thực tế sau khi test được thực thi.

### Truy vết

`FR/UC → TC → Test Code → Kết quả`