# Prompt phân tích kết quả kiểm thử

## 1. Mục đích

Phân tích kết quả kiểm thử để xác định chức năng đạt, không đạt và các vấn đề cần xử lý.

## 2. Context

Đọc:

- `docs/05_kiem_thu/ke_hoach_kiem_thu.md`
- `docs/05_kiem_thu/danh_sach_ca_kiem_thu.md`
- `docs/05_kiem_thu/ket_qua_kiem_thu.md`
- `docs/05_kiem_thu/danh_sach_loi.md`
- Mã nguồn liên quan nếu cần.

## 3. Nhiệm vụ

AI Agent phải:

1. Phân loại kết quả Pass / Fail / Blocked / Not Run.
2. Đối chiếu kết quả với yêu cầu.
3. Xác định lỗi liên quan.
4. Phân tích nguyên nhân nếu có đủ bằng chứng.
5. Kiểm tra ảnh hưởng đến các chức năng khác.
6. Xác định ca kiểm thử cần chạy lại.
7. Đánh giá riêng các chức năng AI.

## 4. Ràng buộc

- Không tự tạo kết quả kiểm thử.
- Không chuyển Fail thành Pass nếu chưa có bằng chứng.
- Không kết luận nguyên nhân khi dữ liệu chưa đủ.
- Không bỏ qua lỗi ảnh hưởng đến dữ liệu hoặc bảo mật.
- Phân biệt rõ kết quả thực tế với nhận định của AI.

## 5. Output

### Tổng quan

| Trạng thái | Số lượng |
|---|---:|
| Pass | |
| Fail | |
| Blocked | |
| Not Run | |

### Kết quả cần xử lý

| TC | FR/UC | Kết quả | Lỗi | Mức độ | Đề xuất |
|---|---|---|---|---|---|

### Phân tích lỗi

Mô tả nguyên nhân và bằng chứng nếu xác định được.

### Kiểm thử lại

Liệt kê các Test Case cần chạy lại sau khi sửa.

### Chất lượng AI

Đánh giá độ chính xác, tính liên quan, tính nhất quán và khả năng bịa dữ liệu nếu có chức năng AI.

### Truy vết

`FR/UC → TC → Kết quả → BUG → Sửa lỗi → Kiểm thử lại`