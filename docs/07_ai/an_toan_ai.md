# An toàn AI

## 1. Mục đích

Đảm bảo việc tích hợp và sử dụng AI không gây ảnh hưởng đến dữ liệu, bảo mật và hoạt động nghiệp vụ của hệ thống.

## 2. Nguyên tắc bảo vệ dữ liệu

- Chỉ cung cấp cho AI dữ liệu cần thiết.
- Không gửi mật khẩu, API key hoặc secret.
- Không đưa thông tin nhạy cảm vào prompt nếu không cần thiết.
- Kiểm tra dữ liệu trước khi gửi cho AI.
- Không cho AI quyền truy cập trực tiếp vào database nếu không cần thiết.

## 3. Kiểm soát đầu vào

Dữ liệu gửi đến AI phải được:

- Kiểm tra kiểu dữ liệu.
- Kiểm tra giá trị bất hợp lệ.
- Giới hạn phạm vi dữ liệu.
- Xác định rõ nguồn dữ liệu.
- Loại bỏ nội dung không cần thiết.

Prompt cũng phải được kiểm soát để tránh yêu cầu ngoài phạm vi chức năng.

## 4. Kiểm soát đầu ra

Kết quả AI phải được kiểm tra trước khi sử dụng.

Cần phát hiện:

- Số liệu không tồn tại.
- Kết luận không có căn cứ.
- Nội dung mâu thuẫn với dữ liệu.
- Nội dung vượt quá phạm vi yêu cầu.
- Thông tin có khả năng gây hiểu nhầm.

Kết quả không hợp lệ không được ghi trực tiếp vào dữ liệu nghiệp vụ.

## 5. Quyền hạn của AI

AI chỉ thực hiện vai trò hỗ trợ phân tích và tổng hợp.

AI không được tự:

- Thêm, sửa hoặc xóa dữ liệu nghiệp vụ.
- Phê duyệt hoặc từ chối nhập hàng.
- Điều chỉnh tồn bồn.
- Thay đổi quyền người dùng.
- Thực hiện quyết định nghiệp vụ.

## 6. Bảo vệ API

API key và thông tin xác thực AI phải được lưu bằng biến môi trường hoặc cơ chế quản lý secret phù hợp.

Không đưa thông tin xác thực vào:

- Mã nguồn.
- Prompt.
- Git repository.
- Tài liệu công khai.
- Log.

## 7. Xử lý lỗi

Khi dịch vụ AI lỗi hoặc không phản hồi:

1. Ghi nhận lỗi.
2. Không làm mất dữ liệu nghiệp vụ.
3. Có thể thử lại trong giới hạn phù hợp.
4. Không lặp lại vô hạn.
5. Nếu AI không khả dụng, hệ thống vẫn phải bảo toàn dữ liệu và các chức năng không phụ thuộc AI.

## 8. Human-in-the-loop

Các kết quả AI có ảnh hưởng đến nghiệp vụ phải được người dùng kiểm tra trước khi sử dụng.

Luồng kiểm soát:

`Dữ liệu → AI → Kiểm tra → Người dùng quyết định`

## 9. Nhật ký và truy vết

Cần ghi nhận các thông tin cần thiết về việc sử dụng AI:

- Prompt.
- Dữ liệu đầu vào ở mức phù hợp.
- Phiên bản mô hình.
- Kết quả.
- Lỗi phát sinh.
- Người kiểm tra.

Không ghi thông tin bí mật vào nhật ký.

## 10. Nguyên tắc cuối

AI là thành phần hỗ trợ của hệ thống. Quyền kiểm soát dữ liệu và quyết định nghiệp vụ vẫn thuộc về hệ thống và người dùng có thẩm quyền.