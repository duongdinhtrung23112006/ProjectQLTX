# VẤN ĐỀ VÀ MỤC TIÊU HỆ THỐNG

## 1. Vấn đề đặt ra

Hoạt động của trạm xăng phát sinh nhiều loại dữ liệu liên quan đến nhiên liệu, bồn chứa, nhập hàng, bán hàng, nhân viên, ca làm việc và doanh thu.

Nếu việc quản lý và tổng hợp dữ liệu được thực hiện thủ công hoặc phân tán, người quản lý có thể gặp khó khăn trong việc:

- Theo dõi lượng nhiên liệu tồn trong các bồn chứa.
- Theo dõi lượng nhiên liệu nhập vào và bán ra.
- Đối chiếu số liệu giữa các hoạt động.
- Tổng hợp doanh thu và sản lượng bán.
- Phát hiện các số liệu có dấu hiệu bất thường.
- Lập báo cáo từ dữ liệu hoạt động.
- Theo dõi lịch sử hoạt động của nhân viên và ca làm việc.

Ngoài ra, dữ liệu vận hành của trạm xăng có thể tăng theo thời gian. Việc chỉ dựa vào thao tác thủ công để tổng hợp và phân tích dữ liệu sẽ làm tăng thời gian xử lý và gây khó khăn cho việc kiểm tra.

Vì vậy, cần xây dựng một hệ thống quản lý tập trung để lưu trữ, xử lý và tra cứu dữ liệu hoạt động của trạm xăng.

Hệ thống đồng thời tích hợp các chức năng AI nhằm hỗ trợ người dùng tổng hợp, phân tích và phát hiện những điểm cần kiểm tra trong dữ liệu.

---

# 2. Mục tiêu tổng quát

Xây dựng một hệ thống quản lý trạm xăng có khả năng quản lý tập trung các hoạt động chính của trạm, đồng thời tích hợp AI để hỗ trợ phân tích và tổng hợp dữ liệu.

Hệ thống phải giúp người dùng:

- Quản lý dữ liệu tập trung.
- Thực hiện các nghiệp vụ quản lý theo vai trò.
- Theo dõi tình trạng nhập, bán và tồn nhiên liệu.
- Tra cứu và thống kê dữ liệu.
- Hỗ trợ lập báo cáo.
- Phát hiện các số liệu có dấu hiệu bất thường.
- Giảm công việc tổng hợp dữ liệu thủ công.

---

# 3. Mục tiêu cụ thể

## 3.1. Quản lý người dùng và phân quyền

Hệ thống cung cấp cơ chế đăng nhập và phân quyền theo vai trò.

Các vai trò chính:

- Quản lý.
- Nhân viên ca.
- Kế toán.

Mỗi vai trò chỉ được truy cập những chức năng phù hợp với trách nhiệm của mình.

---

## 3.2. Quản lý nhiên liệu

Hệ thống cho phép quản lý thông tin các mặt hàng nhiên liệu được sử dụng tại trạm.

Thông tin cần quản lý gồm:

- Mã nhiên liệu.
- Tên nhiên liệu.
- Đơn vị.
- Đơn giá.
- Trạng thái.

Dữ liệu nhiên liệu được sử dụng làm cơ sở cho các nghiệp vụ liên quan đến bồn chứa, nhập hàng và bán hàng.

---

## 3.3. Quản lý bồn chứa

Hệ thống cho phép quản lý các bồn chứa nhiên liệu.

Mỗi bồn chứa phải xác định được:

- Mã bồn.
- Tên bồn.
- Loại nhiên liệu.
- Sức chứa.
- Lượng tồn hiện tại.
- Trạng thái.

Hệ thống phải đảm bảo dữ liệu tồn bồn không vượt quá sức chứa của bồn và không bị âm trong quá trình xử lý nghiệp vụ.

---

## 3.4. Quản lý nhập hàng

Hệ thống cho phép ghi nhận các lần nhập nhiên liệu vào bồn.

Thông tin nhập hàng được lưu lại để:

- Theo dõi lịch sử nhập.
- Kiểm tra số lượng nhập.
- Theo dõi trạng thái phê duyệt.
- Cập nhật tồn bồn khi nghiệp vụ được duyệt.
- Phục vụ tra cứu và thống kê.

---

## 3.5. Quản lý bán hàng

Hệ thống cho phép ghi nhận lượng nhiên liệu bán ra theo ngày.

Dữ liệu bán hàng được sử dụng để:

- Theo dõi sản lượng bán.
- Tính thành tiền.
- Cập nhật số liệu tồn.
- Tính toán doanh thu.
- Phục vụ thống kê và phân tích.

---

## 3.6. Theo dõi tồn bồn

Hệ thống hỗ trợ theo dõi sự thay đổi lượng nhiên liệu trong từng bồn.

Số liệu tồn được đối chiếu dựa trên:

- Tồn đầu.
- Tổng lượng nhập.
- Tổng lượng bán.
- Tồn cuối.

Công thức nghiệp vụ:

Tồn cuối = Tồn đầu + Tổng nhập - Tổng bán

Các số liệu này là nguồn dữ liệu quan trọng cho việc thống kê và phân tích bằng AI.

---

## 3.7. Quản lý nhân viên và ca làm việc

Hệ thống hỗ trợ quản lý:

- Thông tin nhân viên.
- Chức vụ.
- Trạng thái làm việc.
- Ca làm việc.
- Phân công nhân viên vào ca.

Thông tin này được liên kết với các hoạt động nghiệp vụ để xác định người thực hiện.

---

## 3.8. Tra cứu và thống kê

Hệ thống hỗ trợ người dùng có quyền:

- Tra cứu doanh thu.
- Tra cứu lượng nhập.
- Tra cứu lượng bán.
- Tra cứu tồn bồn.
- Thống kê sản lượng bán.
- Thống kê chênh lệch tồn.
- Theo dõi dữ liệu theo thời gian.

---

# 4. Mục tiêu tích hợp AI

AI được tích hợp nhằm hỗ trợ người dùng xử lý dữ liệu, không thay thế người dùng trong việc đưa ra quyết định nghiệp vụ.

Các mục tiêu AI chính gồm:

## 4.1. Sinh báo cáo

AI sử dụng dữ liệu đã được hệ thống cung cấp để hỗ trợ tạo báo cáo tổng hợp.

AI không được tự tạo hoặc thay đổi số liệu nguồn.

---

## 4.2. Tóm tắt biến động tồn bồn

AI phân tích dữ liệu nhập - bán - tồn để tạo phần tóm tắt về biến động của bồn chứa.

Khi dữ liệu không đủ để xác định nguyên nhân, AI phải thể hiện rõ giới hạn của kết luận thay vì tự suy đoán.

---

## 4.3. Phát hiện số liệu bất thường

AI hỗ trợ xác định các dữ liệu có dấu hiệu bất thường dựa trên dữ liệu được cung cấp.

Kết quả được sử dụng như một cảnh báo để người có trách nhiệm kiểm tra.

AI không tự động đưa ra quyết định xử lý nghiệp vụ.

---

# 5. Mục tiêu về chất lượng

Hệ thống hướng tới các mục tiêu:

- Dữ liệu được quản lý tập trung.
- Dữ liệu giữa các chức năng có tính nhất quán.
- Các chức năng được phân quyền rõ ràng.
- Có khả năng kiểm thử.
- Có khả năng bảo trì và mở rộng.
- Có thể triển khai lại từ môi trường sạch.
- Có tài liệu cài đặt và vận hành.
- Có cơ chế ghi nhận và theo dõi các thay đổi.

Đối với các chức năng AI:

- Kết quả phải dựa trên dữ liệu được cung cấp.
- Kết quả AI phải được con người kiểm tra.
- Không đưa dữ liệu nhạy cảm vào prompt công cộng.
- Có khả năng đánh giá chất lượng đầu ra.
- Có khả năng ghi nhận các lỗi hoặc trường hợp AI trả lời không chính xác.

---

# 6. Nguyên tắc thực hiện

Trong quá trình phát triển hệ thống:

1. Phạm vi nghiệp vụ phải được xác định trước khi triển khai chức năng.
2. Không tự thêm nghiệp vụ chưa được xác định.
3. Mọi thay đổi yêu cầu phải được cập nhật vào tài liệu liên quan.
4. AI chỉ đóng vai trò hỗ trợ trong quá trình phát triển và vận hành.
5. Mọi mã nguồn do AI tạo ra phải được kiểm tra và chạy thử.
6. Các số liệu nghiệp vụ phải có nguồn dữ liệu xác định.
7. Người dùng có thẩm quyền chịu trách nhiệm đối với quyết định nghiệp vụ cuối cùng.
8. Các thay đổi quan trọng phải có khả năng kiểm tra và quay lui.

---

# 7. Kết quả mong muốn

Sau khi hoàn thiện, hệ thống phải cung cấp được một nền tảng quản lý tập trung cho các hoạt động chính của trạm xăng.

Người dùng có thể thực hiện các nghiệp vụ theo vai trò được phân quyền, theo dõi dữ liệu nhập - bán - tồn, tra cứu và thống kê hoạt động.

Các chức năng AI cung cấp thêm khả năng tổng hợp báo cáo, tóm tắt biến động dữ liệu và cảnh báo các số liệu cần kiểm tra.

Toàn bộ hệ thống phải có tài liệu, kiểm thử, quy trình triển khai và cơ chế theo dõi chất lượng để có thể tiếp tục phát triển trong các phiên bản sau.