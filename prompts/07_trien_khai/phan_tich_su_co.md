# Prompt phân tích sự cố

## 1. Mục đích

Phân tích sự cố trong quá trình phát triển, triển khai hoặc vận hành để xác định nguyên nhân, ảnh hưởng và hướng xử lý.

## 2. Context

Đọc:

- `docs/06_trien_khai/giam_sat_va_van_hanh.md`
- `docs/06_trien_khai/phuong_an_quay_lui.md`
- `docs/05_kiem_thu/danh_sach_loi.md`
- `docs/08_trang_thai/loi_va_no_ky_thuat.md`
- `docs/08_trang_thai/lich_su_thay_doi.md`
- Log, cấu hình và mã nguồn liên quan đến sự cố.

## 3. Nhiệm vụ

Phân tích theo trình tự:

1. Xác định sự cố.
2. Xác định thời điểm và môi trường xảy ra.
3. Thu thập bằng chứng.
4. Xác định thành phần bị ảnh hưởng.
5. Xác định nguyên nhân trực tiếp.
6. Xác định nguyên nhân gốc nếu có đủ bằng chứng.
7. Đánh giá phạm vi ảnh hưởng.
8. Xác định biện pháp khắc phục.
9. Kiểm tra lại sau khi khắc phục.
10. Xác định biện pháp phòng ngừa tái diễn.

## 4. Ràng buộc

- Không suy đoán nguyên nhân khi chưa có bằng chứng.
- Phân biệt rõ nguyên nhân đã xác định và giả thuyết.
- Không xóa hoặc thay đổi bằng chứng sự cố.
- Không tự sửa dữ liệu nghiệp vụ để che giấu lỗi.
- Không coi sự cố đã xử lý nếu chưa kiểm tra lại.
- Nếu cần quay lui, tham chiếu `phuong_an_quay_lui.md`.

## 5. Output

### Thông tin sự cố

| Trường | Nội dung |
|---|---|
| Mã sự cố | |
| Thời điểm | |
| Môi trường | |
| Thành phần ảnh hưởng | |
| Mức độ | |
| Triệu chứng | |

### Phân tích

- Bằng chứng.
- Nguyên nhân trực tiếp.
- Nguyên nhân gốc.
- Giả thuyết chưa xác nhận.
- Phạm vi ảnh hưởng.

### Xử lý

- Biện pháp tạm thời.
- Biện pháp khắc phục.
- Kết quả kiểm tra lại.
- Biện pháp phòng ngừa.

### Truy vết

`Sự cố → Bằng chứng → Nguyên nhân → Xử lý → Kiểm tra lại → Cập nhật tài liệu`

## 6. Kết quả

Phân loại sự cố:

- Đã xác định nguyên nhân.
- Đã khắc phục.
- Đang điều tra.
- Cần thêm dữ liệu.
- Cần quay lui.