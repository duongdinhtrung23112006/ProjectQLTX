# THIẾT KẾ AI

## 1. Mục đích

AI được tích hợp để hỗ trợ Quản lý trong việc:

- Sinh báo cáo từ dữ liệu hệ thống.
- Tóm tắt biến động tồn bồn.
- Phát hiện và cảnh báo số liệu có dấu hiệu bất thường.

AI chỉ đóng vai trò hỗ trợ phân tích, không thay thế quyết định của người dùng.

## 2. Kiến trúc tích hợp

```text
MySQL
  ↓
Business Service
  ↓
AI Service
  ↓
Prompt + Dữ liệu nghiệp vụ
  ↓
LLM
  ↓
Kiểm tra kết quả
  ↓
Giao diện
  ↓
Quản lý
3. Dữ liệu đầu vào

AI chỉ nhận dữ liệu cần thiết cho từng tác vụ.

Ví dụ:

Sinh báo cáo
Ngày.
Tổng nhập.
Tổng bán.
Doanh thu.
Tồn bồn.
Chênh lệch nếu có.
Tóm tắt tồn bồn
Tồn đầu.
Tổng nhập.
Tổng bán.
Tồn cuối.
Lịch sử biến động phù hợp.
Cảnh báo bất thường
Số liệu nhập.
Số liệu bán.
Tồn bồn.
Các dữ liệu đối chiếu được cung cấp.
4. Quy trình xử lý
Người dùng chọn chức năng AI.
Hệ thống kiểm tra quyền.
Hệ thống lấy dữ liệu từ CSDL.
AI Service chuẩn bị prompt.
Gửi dữ liệu và prompt đến mô hình AI.
Nhận kết quả.
Kiểm tra kết quả.
Hiển thị cho người dùng.
Người dùng kiểm tra và quyết định.
5. Nguyên tắc prompt

Prompt AI phải xác định:

Vai trò của AI.
Mục tiêu xử lý.
Dữ liệu được phép sử dụng.
Ràng buộc.
Định dạng đầu ra.

AI phải được yêu cầu:

Không tự tạo số liệu.
Không suy diễn dữ liệu thiếu thành dữ liệu thực tế.
Nêu rõ khi dữ liệu không đủ.
Phân biệt dữ liệu thực tế và nhận định phân tích.
6. Kiểm soát hallucination

Hệ thống áp dụng các nguyên tắc:

Grounding vào dữ liệu hệ thống.
Chỉ cung cấp dữ liệu liên quan cho AI.
Kiểm tra kết quả trước khi hiển thị khi cần.
Cho phép người dùng đối chiếu với dữ liệu gốc.
Không coi kết quả AI là dữ liệu nghiệp vụ chính thức.
7. Human-in-the-loop

Kết quả AI phải được con người kiểm tra đối với các nội dung quan trọng.

Dữ liệu hệ thống
      ↓
      AI
      ↓
Kết quả phân tích
      ↓
Người dùng kiểm tra
      ↓
Quyết định nghiệp vụ

AI không tự:

Phê duyệt nhập hàng.
Từ chối nhập hàng.
Điều chỉnh tồn.
Thay đổi dữ liệu CSDL.
Thực hiện quyết định quản lý.
8. An toàn dữ liệu
Không gửi mật khẩu, API key hoặc secret cho AI.
Không đưa dữ liệu nhạy cảm không cần thiết vào prompt.
API key phải được lưu bằng biến môi trường.
Kiểm soát dữ liệu đầu vào và đầu ra.
Ghi nhận việc sử dụng AI trong docs/07_ai/nhat_ky_su_dung_ai.md.
9. Đánh giá AI

Kết quả AI được đánh giá theo:

Độ chính xác.
Tính phù hợp với dữ liệu.
Tính nhất quán.
Khả năng phát hiện bất thường.
Mức độ hallucination.
Khả năng giải thích và kiểm tra kết quả.
10. Phạm vi AI

Phiên bản hiện tại chỉ tập trung vào:

Sinh báo cáo.
Tóm tắt biến động tồn bồn.
Cảnh báo số liệu bất thường.

Các chức năng AI khác chỉ được bổ sung khi được xác định và cập nhật vào tài liệu phạm vi, yêu cầu, thiết kế và kiểm thử.