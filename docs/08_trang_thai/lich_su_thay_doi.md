# Lịch sử thay đổi

## 1. Mục đích

Ghi nhận các thay đổi quan trọng của hệ thống trong quá trình phát triển, giúp theo dõi phiên bản và truy vết nguyên nhân thay đổi.

## 2. Nội dung cần ghi nhận

Mỗi thay đổi quan trọng cần có:

- Thời gian.
- Người thực hiện.
- Phiên bản hoặc commit.
- Nội dung thay đổi.
- Lý do thay đổi.
- Tài liệu hoặc yêu cầu liên quan.
- Kết quả kiểm tra.

## 3. Nhật ký thay đổi

| ID | Thời gian | Phiên bản / Commit | Nội dung | Lý do | Người thực hiện | Kết quả |
|---|---|---|---|---|---|---|
| CHG-001 | | | | | | |
| CHG-002 | | | | | | |
| CHG-003 | | | | | | |

## 4. Phân loại thay đổi

- **Thêm mới:** bổ sung chức năng hoặc tài liệu.
- **Sửa đổi:** thay đổi chức năng hoặc thiết kế hiện có.
- **Loại bỏ:** loại bỏ chức năng hoặc thành phần.
- **Sửa lỗi:** khắc phục lỗi.
- **Cập nhật tài liệu:** thay đổi tài liệu nhưng không thay đổi hệ thống.
- **Thay đổi AI:** thay đổi prompt, mô hình hoặc quy trình AI.

## 5. Truy vết

Mỗi thay đổi quan trọng nên liên kết với các thành phần liên quan:

`Yêu cầu → Tài liệu → Prompt → Mã nguồn → Kiểm thử → Commit`

Khi thay đổi ảnh hưởng đến dữ liệu hoặc chức năng đã có, cần kiểm tra các thành phần liên quan trước khi xác nhận thay đổi.

## 6. Nguyên tắc

- Ghi nhận thay đổi ngay sau khi hoàn thành.
- Không ghi thông tin bí mật vào lịch sử.
- Không xóa lịch sử thay đổi quan trọng.
- Commit cần có nội dung mô tả rõ ràng.
- Thay đổi lớn phải được kiểm thử trước khi đánh dấu hoàn thành.