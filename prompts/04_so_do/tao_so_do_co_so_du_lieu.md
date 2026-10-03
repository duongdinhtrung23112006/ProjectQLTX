# Prompt tạo sơ đồ cơ sở dữ liệu

## 1. Mục đích

Tạo đặc tả sơ đồ cơ sở dữ liệu dựa trên thiết kế và cấu trúc database thực tế của hệ thống.

## 2. Context

Đọc:

- `docs/03_thiet_ke/thiet_ke_co_so_du_lieu.md`
- `docs/03_thiet_ke/tu_dien_du_lieu.md`
- Các script SQL nếu có.
- Cấu trúc database hiện tại nếu được cung cấp.

## 3. Nhiệm vụ

AI Agent phải:

1. Xác định các bảng cần thể hiện.
2. Xác định khóa chính.
3. Xác định khóa ngoại.
4. Xác định quan hệ giữa các bảng.
5. Xác định lực lượng quan hệ nếu có đủ thông tin.
6. Đối chiếu với database thực tế.
7. Phát hiện điểm không thống nhất giữa thiết kế và database.

## 4. Ràng buộc

- Không tự thêm bảng.
- Không tự thêm khóa ngoại.
- Không tự tạo quan hệ không tồn tại.
- Không thay đổi cấu trúc database.
- Không biến chức năng tra cứu hoặc thống kê thành bảng dữ liệu.
- Nếu cấu trúc chưa được xác định, ghi rõ `Chưa xác định`.

## 5. Output

### Danh sách bảng

| Bảng | Khóa chính | Khóa ngoại | Mục đích |
|---|---|---|---|

### Quan hệ

Mô tả quan hệ giữa các bảng dựa trên khóa ngoại thực tế.

### Kiểm tra

Đối chiếu:

`Thiết kế CSDL → SQL → Database thực tế`

Nêu rõ mọi điểm không thống nhất.

### Đặc tả sơ đồ

Mô tả các bảng, khóa và quan hệ cần xuất hiện.

Chỉ tạo mã Mermaid hoặc PlantUML khi người dùng yêu cầu tạo sơ đồ thực tế.

### Truy vết

`Bảng → Từ điển dữ liệu → Chức năng → FR/UC`