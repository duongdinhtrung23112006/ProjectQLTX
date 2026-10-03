# Prompt tạo sơ đồ kiến trúc

## 1. Mục đích

Tạo đặc tả sơ đồ kiến trúc thể hiện các thành phần chính của hệ thống và cách chúng kết nối với nhau.

## 2. Context

Đọc:

- `docs/03_thiet_ke/kien_truc_he_thong.md`
- `docs/03_thiet_ke/thiet_ke_api.md`
- `docs/03_thiet_ke/thiet_ke_ai.md`
- `docs/06_trien_khai/kien_truc_trien_khai.md`
- Cấu trúc mã nguồn hiện tại.

## 3. Nhiệm vụ

AI Agent phải xác định:

- Người dùng.
- Giao diện web.
- Flask application.
- Routes.
- Services.
- Database MySQL.
- Thành phần AI.
- Cấu hình và môi trường triển khai.
- Các luồng dữ liệu chính.

Mô tả quan hệ và hướng trao đổi dữ liệu giữa các thành phần.

## 4. Ràng buộc

- Không thêm thành phần chưa có căn cứ.
- Không thay đổi kiến trúc hiện tại.
- Phân biệt thành phần thực tế với thành phần dự kiến.
- Không coi AI là thành phần có quyền tự quyết định nghiệp vụ.
- Không đưa secret hoặc thông tin nhạy cảm vào sơ đồ.

## 5. Output

### Thành phần

| Thành phần | Trách nhiệm | Trạng thái |
|---|---|---|
| Web UI | | |
| Flask | | |
| Routes | | |
| Services | | |
| MySQL | | |
| AI | | |

### Kết nối

Mô tả các kết nối giữa các thành phần và dữ liệu được trao đổi.

### Đặc tả sơ đồ

Mô tả bố cục và các thành phần cần xuất hiện.

Chỉ tạo mã Mermaid hoặc PlantUML khi người dùng yêu cầu tạo sơ đồ thực tế.

### Kiểm tra

Đối chiếu:

`Kiến trúc tài liệu → Mã nguồn → Triển khai`

### Truy vết

`Thành phần → Tài liệu thiết kế → Code → Triển khai`