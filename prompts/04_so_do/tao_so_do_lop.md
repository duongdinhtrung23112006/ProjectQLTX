# Prompt tạo sơ đồ lớp

## 1. Mục đích

Tạo đặc tả sơ đồ lớp dựa trên thiết kế, database và mã nguồn hiện tại.

## 2. Context

Đọc:

- `docs/03_thiet_ke/kien_truc_he_thong.md`
- `docs/03_thiet_ke/thiet_ke_co_so_du_lieu.md`
- `docs/03_thiet_ke/tu_dien_du_lieu.md`
- Mã nguồn liên quan.

## 3. Nhiệm vụ

AI Agent phải:

1. Xác định các lớp chính.
2. Xác định thuộc tính quan trọng.
3. Xác định phương thức chính nếu có trong mã nguồn.
4. Xác định quan hệ giữa các lớp.
5. Xác định quan hệ kế thừa, kết hợp hoặc phụ thuộc khi có căn cứ.
6. Đối chiếu với database và mã nguồn.

## 4. Ràng buộc

- Không tự tạo lớp không có cơ sở.
- Không biến mọi bảng database thành lớp nếu kiến trúc không sử dụng cách này.
- Không thêm thuộc tính hoặc phương thức chỉ để làm sơ đồ đầy đủ hơn.
- Không thay đổi thiết kế hệ thống.
- Nếu thông tin chưa đủ, ghi rõ `Chưa xác định`.

## 5. Output

### Danh sách lớp

| Lớp | Trách nhiệm | Thuộc tính chính | Phương thức chính |
|---|---|---|---|

### Quan hệ

Mô tả quan hệ giữa các lớp và lý do xác định quan hệ đó.

### Đặc tả sơ đồ

Mô tả bố cục và thành phần cần thể hiện.

Chỉ tạo mã Mermaid hoặc PlantUML khi người dùng yêu cầu tạo sơ đồ thực tế.

### Kiểm tra

Đối chiếu sơ đồ với:

`Thiết kế → Database → Code`

### Truy vết

Liên kết mỗi lớp với thành phần thiết kế hoặc mã nguồn tương ứng.