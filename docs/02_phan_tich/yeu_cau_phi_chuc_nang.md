# YÊU CẦU PHI CHỨC NĂNG

## 1. Bảo mật

- Mật khẩu không lưu dạng văn bản thuần.
- API key và thông tin bí mật không được ghi trực tiếp vào source code.
- Sử dụng biến môi trường cho thông tin cấu hình nhạy cảm.
- Kiểm soát truy cập theo vai trò.
- Kiểm tra và xử lý dữ liệu đầu vào.
- Không đưa dữ liệu nhạy cảm vào AI công cộng.

## 2. Tính toàn vẹn dữ liệu

- Khóa chính và khóa ngoại phải được đảm bảo.
- Không cho phép tham chiếu dữ liệu không tồn tại.
- Không để tồn bồn âm.
- Không để tồn bồn vượt sức chứa.
- Số liệu nhập - bán - tồn phải nhất quán.

## 3. Khả năng kiểm thử

Các chức năng quan trọng phải có thể kiểm thử.

Kiểm thử tối thiểu gồm:

- Luồng chính.
- Trường hợp biên.
- Dữ liệu không hợp lệ.
- Phân quyền.
- Xử lý lỗi.
- Regression khi thay đổi chức năng.

## 4. Khả năng bảo trì

- Tách giao diện, route, service và xử lý dữ liệu hợp lý.
- Không gom toàn bộ logic vào một file.
- Hạn chế thay đổi lan sang chức năng không liên quan.
- Code phải dễ đọc và có cấu trúc rõ ràng.

## 5. Khả năng triển khai

Hệ thống phải có:

- Cấu hình môi trường.
- Hướng dẫn cài đặt.
- Hướng dẫn chạy.
- Sao lưu và khôi phục dữ liệu.
- Phương án quay lui khi triển khai lỗi.

## 6. Khả năng giám sát

Hệ thống cần có khả năng:

- Ghi log lỗi và hoạt động quan trọng.
- Theo dõi trạng thái hệ thống.
- Phát hiện sự cố.
- Tạo cảnh báo khi cần thiết.

## 7. AI

Kết quả AI phải:

- Dựa trên dữ liệu được cung cấp.
- Không tự tạo số liệu nghiệp vụ.
- Thể hiện giới hạn khi thiếu dữ liệu.
- Có thể được con người kiểm tra.
- Được đánh giá về độ chính xác, tính phù hợp và nguy cơ hallucination.

## 8. Nguyên tắc chung

Các yêu cầu phi chức năng phải được xem xét khi:

- Thiết kế.
- Lập trình.
- Kiểm thử.
- Triển khai.
- Tích hợp AI.

Không được đánh đổi yêu cầu bảo mật hoặc toàn vẹn dữ liệu chỉ để hoàn thành nhanh một chức năng.