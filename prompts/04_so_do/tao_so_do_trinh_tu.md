# Prompt tạo sơ đồ trình tự

## 1. Mục đích

Tạo đặc tả sơ đồ trình tự để mô tả thứ tự tương tác giữa người dùng, giao diện, backend, database và các thành phần AI.

## 2. Context

Đọc:

- `docs/02_phan_tich/danh_sach_use_case.md`
- `docs/02_phan_tich/quy_trinh_nghiep_vu.md`
- `docs/03_thiet_ke/kien_truc_he_thong.md`
- `docs/03_thiet_ke/thiet_ke_api.md`
- `docs/03_thiet_ke/thiet_ke_ai.md`

## 3. Nhiệm vụ

AI Agent phải:

1. Xác định actor khởi tạo thao tác.
2. Xác định các thành phần tham gia.
3. Mô tả thứ tự gửi và nhận dữ liệu.
4. Thể hiện xử lý thành công.
5. Thể hiện các nhánh lỗi hoặc ngoại lệ quan trọng.
6. Với chức năng AI, thể hiện luồng dữ liệu từ hệ thống đến AI và kết quả quay về hệ thống.
7. Đối chiếu trình tự với Use Case và kiến trúc thực tế.

## 4. Ràng buộc

- Không tự thêm thành phần chưa có trong kiến trúc.
- Không tự tạo API chưa được thiết kế.
- Không cho AI thực hiện thao tác nghiệp vụ trái với phạm vi.
- Không bỏ qua kiểm tra phân quyền và dữ liệu khi chúng là một phần của luồng.
- Không mô tả AI như actor nghiệp vụ.

## 5. Output

### Thành phần tham gia

| Thành phần | Vai trò |
|---|---|
| Người dùng | |
| Giao diện | |
| Backend | |
| Database | |
| AI | |

### Luồng chính

Mô tả tuần tự từng bước.

### Luồng ngoại lệ

Mô tả các trường hợp lỗi hoặc dữ liệu không hợp lệ.

### Đặc tả sơ đồ

Mô tả các thành phần, mũi tên và thứ tự tương tác cần thể hiện.

Chỉ tạo mã Mermaid hoặc PlantUML khi người dùng yêu cầu tạo sơ đồ thực tế.

### Truy vết

`UC → Quy trình → API/Code → Database/AI`