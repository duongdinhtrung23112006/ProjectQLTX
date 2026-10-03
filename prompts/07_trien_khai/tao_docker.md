# Prompt tạo cấu hình Docker

## 1. Mục đích

Phân tích hệ thống và tạo các thành phần cần thiết để đóng gói, chạy và triển khai hệ thống bằng Docker.

## 2. Context

Đọc:

- `docs/03_thiet_ke/kien_truc_he_thong.md`
- `docs/03_thiet_ke/thiet_ke_co_so_du_lieu.md`
- `docs/06_trien_khai/kien_truc_trien_khai.md`
- `docs/06_trien_khai/huong_dan_cai_dat.md`
- `docs/06_trien_khai/cau_hinh_mau.md`
- `requirements.txt`
- Cấu trúc mã nguồn hiện tại.

## 3. Nhiệm vụ

Xác định:

- Thành phần cần chạy trong container.
- Quan hệ giữa các thành phần.
- Port cần sử dụng.
- Biến môi trường cần thiết.
- Cách kết nối ứng dụng với cơ sở dữ liệu.
- Cách lưu dữ liệu cần tồn tại sau khi container dừng.
- Các file Docker cần tạo hoặc cập nhật.
- Cách build và chạy hệ thống.
- Health check nếu cần.

## 4. Ràng buộc

- Không đưa mật khẩu, API key hoặc secret vào file cấu hình.
- Không tự thay đổi kiến trúc hệ thống.
- Không thêm container hoặc dịch vụ không có căn cứ từ tài liệu.
- Không xóa dữ liệu khi khởi động lại nếu dữ liệu cần được bảo toàn.
- Phải phân biệt cấu hình phát triển và cấu hình triển khai khi cần.
- Không giả định dịch vụ bên ngoài nếu chưa được xác định.

## 5. Output

Cung cấp:

- Danh sách file Docker cần tạo hoặc sửa.
- Vai trò của từng file.
- Cấu hình cần có trong từng file.
- Biến môi trường cần thiết.
- Port và kết nối giữa các thành phần.
- Lệnh build.
- Lệnh khởi động.
- Lệnh dừng.
- Lệnh kiểm tra trạng thái.
- Các lưu ý về dữ liệu và secret.

## 6. Kiểm tra

Kiểm tra:

- Cấu hình có khớp kiến trúc hệ thống.
- Container có thể giao tiếp đúng.
- Port không xung đột.
- Biến môi trường đầy đủ.
- Secret không bị hard-code.
- Dữ liệu cần bảo toàn được xử lý đúng.
- Có thể khởi động và dừng hệ thống theo hướng dẫn.