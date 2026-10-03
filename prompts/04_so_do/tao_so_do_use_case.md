# Prompt tạo sơ đồ Use Case

## 1. Mục đích

Tạo đặc tả sơ đồ Use Case dựa trên yêu cầu và danh sách Use Case của hệ thống.

## 2. Context

Đọc:

- `docs/02_phan_tich/vai_tro_nguoi_dung.md`
- `docs/02_phan_tich/yeu_cau_chuc_nang.md`
- `docs/02_phan_tich/danh_sach_use_case.md`
- `docs/02_phan_tich/user_story.md`

## 3. Nhiệm vụ

AI Agent phải:

1. Xác định các actor.
2. Xác định các Use Case.
3. Xác định quan hệ giữa actor và Use Case.
4. Xác định quan hệ `include` hoặc `extend` khi có căn cứ.
5. Kiểm tra sơ đồ không chứa chức năng ngoài phạm vi.

Các actor hiện tại:

- Quản lý.
- Nhân viên ca.
- Kế toán.

AI không phải actor nghiệp vụ.

## 4. Ràng buộc

- Không tự thêm actor.
- Không tự thêm Use Case.
- Không biến chức năng kỹ thuật thành Use Case nếu không có yêu cầu.
- Không tạo quan hệ `include` / `extend` chỉ để làm sơ đồ phức tạp.
- Phải đối chiếu với `danh_sach_use_case.md`.

## 5. Output

Trả về:

### Actor

Danh sách actor và các Use Case tương ứng.

### Use Case

Danh sách UC và mã UC.

### Quan hệ

Mô tả các quan hệ giữa actor và Use Case, bao gồm `include` / `extend` nếu có.

### Đặc tả sơ đồ

Cung cấp mã Mermaid hoặc PlantUML khi người dùng yêu cầu tạo sơ đồ thực tế.

Nếu chưa yêu cầu mã sơ đồ, chỉ trả về đặc tả dạng văn bản.

### Truy vết

`Actor → UC → FR → User Story`