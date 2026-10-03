# Prompt sinh ca kiểm thử

## 1. Mục đích

Sinh các ca kiểm thử dựa trên yêu cầu, quy tắc nghiệp vụ và chức năng thực tế của hệ thống.

## 2. Context

AI Agent phải đọc:

- `docs/02_phan_tich/yeu_cau_chuc_nang.md`
- `docs/02_phan_tich/quy_tac_nghiep_vu.md`
- `docs/02_phan_tich/danh_sach_use_case.md`
- `docs/02_phan_tich/user_story.md`
- `docs/05_kiem_thu/ke_hoach_kiem_thu.md`

## 3. Nhiệm vụ

Sinh ca kiểm thử cho:

- Chức năng chính.
- Điều kiện hợp lệ.
- Điều kiện không hợp lệ.
- Phân quyền.
- Dữ liệu biên.
- Lỗi nhập liệu.
- Quy tắc nghiệp vụ.
- Chức năng AI.
- Xử lý lỗi và bảo mật.

Mỗi ca kiểm thử phải có thể thực hiện và kiểm tra được kết quả.

## 4. Ràng buộc

- Không tự tạo yêu cầu nghiệp vụ.
- Không tạo kết quả kiểm thử giả.
- Không bỏ qua các trường hợp lỗi quan trọng.
- Không coi kết quả AI là đúng mặc định.
- Ca kiểm thử AI phải kiểm tra khả năng bịa dữ liệu và tính phù hợp với dữ liệu đầu vào.

## 5. Output

| ID | FR/UC | Tên ca kiểm thử | Tiền điều kiện | Dữ liệu | Các bước | Kết quả mong đợi |
|---|---|---|---|---|---|---|
| TC01 | | | | | | |
| TC02 | | | | | | |

Sau bảng, bổ sung:

### Trường hợp biên
Các giá trị hoặc điều kiện cần kiểm tra đặc biệt.

### Truy vết
`FR/UC → Test Case`

### Ghi chú
Nêu các thông tin còn thiếu để thực hiện kiểm thử.