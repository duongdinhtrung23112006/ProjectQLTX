# Prompt kiểm tra triển khai

## 1. Mục đích

Kiểm tra hệ thống sau khi triển khai để xác định hệ thống hoạt động đúng, ổn định và phù hợp với cấu hình đã xác định.

## 2. Context

Đọc:

- `docs/06_trien_khai/kien_truc_trien_khai.md`
- `docs/06_trien_khai/huong_dan_cai_dat.md`
- `docs/06_trien_khai/huong_dan_chay_he_thong.md`
- `docs/06_trien_khai/cau_hinh_mau.md`
- `docs/06_trien_khai/giam_sat_va_van_hanh.md`
- `docs/05_kiem_thu/ke_hoach_kiem_thu.md`
- `docs/05_kiem_thu/danh_sach_ca_kiem_thu.md`
- Cấu hình và mã nguồn triển khai thực tế.

## 3. Nhiệm vụ

Kiểm tra:

### Môi trường

- Ứng dụng khởi động thành công.
- Các thành phần cần thiết đang hoạt động.
- Port và kết nối mạng đúng.
- Biến môi trường đầy đủ.
- Kết nối cơ sở dữ liệu hoạt động.

### Chức năng

- Đăng nhập và phân quyền.
- Các chức năng quản lý chính.
- Nhập hàng và cập nhật tồn.
- Các chức năng tra cứu và thống kê.
- Các chức năng AI nếu đã triển khai.

### Dữ liệu

- Dữ liệu không bị mất hoặc thay đổi ngoài dự kiến.
- Kết nối cơ sở dữ liệu đúng.
- Các ràng buộc dữ liệu vẫn hoạt động.

### Vận hành

- Log hoạt động bình thường.
- Health check hoạt động nếu có.
- Lỗi nghiêm trọng được phát hiện.
- Sao lưu và khôi phục có thể thực hiện theo thiết kế.

## 4. Ràng buộc

- Không tự đánh dấu đạt nếu chưa có bằng chứng kiểm tra.
- Không tạo kết quả kiểm thử giả.
- Phân biệt `Đạt`, `Không đạt`, `Chưa kiểm tra` và `Không áp dụng`.
- Không thay đổi dữ liệu nghiệp vụ chỉ để làm kiểm tra đạt.
- Nếu phát hiện lỗi, ghi nhận vào danh sách lỗi tương ứng.

## 5. Output

| Hạng mục | Kiểm tra | Kết quả | Bằng chứng | Ghi chú |
|---|---|---|---|---|

### Tổng hợp

- Số hạng mục đạt.
- Số hạng mục không đạt.
- Số hạng mục chưa kiểm tra.
- Lỗi cần xử lý.
- Rủi ro sau triển khai.

## 6. Truy vết

Liên kết kết quả với:

`Triển khai → Kiểm tra → Ca kiểm thử → Lỗi → Xử lý → Kiểm tra lại`

## 7. Nguyên tắc

Chỉ xác nhận triển khai đạt khi có bằng chứng kiểm tra tương ứng.