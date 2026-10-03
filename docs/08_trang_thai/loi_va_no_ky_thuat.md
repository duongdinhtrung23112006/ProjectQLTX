# Lỗi và nợ kỹ thuật

## 1. Mục đích

Ghi nhận các lỗi, hạn chế và khoản nợ kỹ thuật còn tồn tại trong quá trình phát triển hệ thống.

## 2. Phân loại

### Lỗi

Vấn đề khiến chức năng hoạt động sai hoặc không đáp ứng yêu cầu.

### Nợ kỹ thuật

Giải pháp tạm thời, phần mã nguồn chưa tối ưu hoặc công việc cần thực hiện thêm nhưng chưa ảnh hưởng trực tiếp đến chức năng hiện tại.

## 3. Mức độ lỗi

| Mức độ | Ý nghĩa |
|---|---|
| Nghiêm trọng | Ảnh hưởng lớn đến hệ thống hoặc dữ liệu |
| Cao | Ảnh hưởng chức năng chính |
| Trung bình | Ảnh hưởng một phần chức năng |
| Thấp | Ảnh hưởng nhỏ hoặc giao diện |

## 4. Danh sách

| ID | Loại | Mức độ | Nội dung | Chức năng liên quan | Trạng thái |
|---|---|---|---|---|---|
| BUG-001 | | | | | |
| BUG-002 | | | | | |
| TECH-001 | | | | | |
| TECH-002 | | | | | |

## 5. Trạng thái xử lý

- `Mới`: đã phát hiện nhưng chưa xử lý.
- `Đang xử lý`: đang tìm nguyên nhân hoặc sửa lỗi.
- `Đã sửa`: đã có thay đổi khắc phục.
- `Đã kiểm tra`: đã kiểm thử lại.
- `Đóng`: lỗi được xác nhận đã giải quyết.

## 6. Quy trình xử lý

1. Ghi nhận lỗi hoặc nợ kỹ thuật.
2. Xác định mức độ ảnh hưởng.
3. Xác định nguyên nhân.
4. Thực hiện sửa hoặc cải thiện.
5. Kiểm thử lại.
6. Cập nhật trạng thái.
7. Ghi nhận thay đổi nếu cần.

## 7. Nguyên tắc

- Không tự tạo lỗi khi chưa phát hiện thực tế.
- Không đánh dấu đã sửa khi chưa kiểm tra.
- Lỗi liên quan đến dữ liệu phải được ưu tiên đánh giá.
- Nợ kỹ thuật cần được theo dõi để tránh tích lũy.
- Các lỗi quan trọng phải có khả năng truy vết đến chức năng và ca kiểm thử liên quan.