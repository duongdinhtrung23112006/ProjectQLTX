# Prompt tạo quy trình triển khai

## 1. Mục đích

Xây dựng quy trình triển khai hệ thống từ trạng thái mã nguồn đến khi hệ thống hoạt động và được kiểm tra sau triển khai.

## 2. Context

Đọc:

- `docs/06_trien_khai/kien_truc_trien_khai.md`
- `docs/06_trien_khai/huong_dan_cai_dat.md`
- `docs/06_trien_khai/huong_dan_chay_he_thong.md`
- `docs/06_trien_khai/cau_hinh_mau.md`
- `docs/06_trien_khai/sao_luu_va_phuc_hoi.md`
- `docs/06_trien_khai/giam_sat_va_van_hanh.md`
- `docs/06_trien_khai/phuong_an_quay_lui.md`
- Cấu trúc mã nguồn và cấu hình triển khai thực tế.

## 3. Nhiệm vụ

Xác định quy trình:

1. Kiểm tra mã nguồn và cấu hình.
2. Kiểm tra kiểm thử trước triển khai.
3. Sao lưu dữ liệu cần thiết.
4. Chuẩn bị môi trường triển khai.
5. Build ứng dụng.
6. Triển khai các thành phần.
7. Khởi động hệ thống.
8. Kiểm tra trạng thái và health check.
9. Kiểm tra các chức năng chính.
10. Theo dõi hệ thống sau triển khai.
11. Ghi nhận kết quả và vấn đề phát sinh.
12. Thực hiện quay lui nếu triển khai thất bại.

## 4. Ràng buộc

- Không tự thêm bước phụ thuộc vào công nghệ chưa được xác định.
- Không bỏ qua bước sao lưu khi thao tác có thể ảnh hưởng dữ liệu.
- Không coi triển khai thành công chỉ dựa trên việc container hoặc ứng dụng khởi động.
- Phải có bước kiểm tra sau triển khai.
- Không tự thay đổi dữ liệu nghiệp vụ trong quá trình triển khai.
- Secret phải được cung cấp qua cấu hình an toàn.

## 5. Output

### Điều kiện trước triển khai

Các yêu cầu cần đạt trước khi triển khai.

### Quy trình triển khai

`Kiểm tra → Sao lưu → Build → Triển khai → Khởi động → Kiểm tra → Giám sát`

### Kiểm tra sau triển khai

- Ứng dụng hoạt động.
- Kết nối cơ sở dữ liệu hoạt động.
- Các chức năng chính hoạt động.
- Log không xuất hiện lỗi nghiêm trọng.
- Health check đạt yêu cầu.

### Quay lui

Xác định điều kiện kích hoạt và liên kết với:

`docs/06_trien_khai/phuong_an_quay_lui.md`

### Kết quả

Ghi nhận:

- Phiên bản triển khai.
- Thời điểm triển khai.
- Người thực hiện.
- Kết quả.
- Vấn đề phát sinh.
- Hành động xử lý.

## 6. Kiểm tra

Đảm bảo quy trình có thể thực hiện tuần tự, có điểm kiểm tra rõ ràng và có phương án xử lý khi triển khai thất bại.