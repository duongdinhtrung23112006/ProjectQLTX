Hãy triển khai CHỨC NĂNG CUỐI CÙNG: DASHBOARD TỔNG QUAN HỆ THỐNG cho dự án quản lý trạm xăng có tích hợp AI tại:

D:\ProjectQLTX

Đây là màn hình tổng hợp toàn hệ thống, có giao diện chuyên nghiệp, hiện đại, trực quan và tạo cảm giác như một phần mềm quản lý trạm xăng thực tế đang được vận hành.

Chức năng dành chung cho hai vai trò:
- Quản lý
- Kế toán

Hãy chủ động khảo sát code và triển khai trực tiếp, không chỉ đưa ra hướng dẫn.

==================================================
I. KHẢO SÁT VÀ TỔNG HỢP TOÀN HỆ THỐNG
==================================================

Trước khi triển khai, hãy đọc cấu trúc dự án, các route, service, template, cơ chế đăng nhập, phân quyền và database schema thực tế.

Rà soát các chức năng đã có, dự kiến gồm:
- Đăng nhập và phân quyền.
- Quản lý nhân viên.
- Quản lý ca làm việc.
- Quản lý nhiên liệu.
- Quản lý bồn chứa và tồn bồn.
- Nhập hàng.
- Bán hàng.
- Duyệt và từ chối giao dịch.
- Tra cứu số liệu.
- Thống kê số liệu.
- Các chức năng AI nếu đã được triển khai.

Chỉ tổng hợp những chức năng thực sự tồn tại trong dự án. Không tự tuyên bố một chức năng đã hoàn thành nếu code chưa có.

Mục tiêu là tạo một trang tổng quan thống nhất, giúp người dùng nắm bắt tình hình hoạt động của trạm xăng ngay sau khi đăng nhập.

Không viết lại các chức năng hiện có. Tận dụng các route, service, truy vấn và component đã có khi phù hợp.

==================================================
II. GIAO DIỆN VÀ PHONG CÁCH THIẾT KẾ
==================================================

Đây là yêu cầu rất quan trọng.

1. Phải giữ nguyên ngôn ngữ thiết kế chung của hệ thống:
   - Màu chủ đạo.
   - Màu nền.
   - Font chữ.
   - Sidebar và thanh điều hướng.
   - Kiểu nút bấm.
   - Kiểu bảng dữ liệu.
   - Khoảng cách, đường viền, bo góc.
   - Phong cách icon và các thành phần giao diện.

2. Trước khi thiết kế, hãy kiểm tra CSS, layout base, sidebar, header và những trang đang có để xác định chính xác bộ màu của hệ thống.

3. Không tự ý đổi màu toàn bộ hệ thống hoặc tạo một giao diện có bảng màu khác biệt.

4. Được phép nâng cấp cách bố trí, phân cấp thông tin, biểu đồ, thẻ thống kê và các chi tiết trực quan để trang tổng quan trông chuyên nghiệp hơn, nhưng vẫn phải đồng nhất với giao diện hiện có.

5. Phong cách hướng tới:
   - Chuyên nghiệp.
   - Hiện đại.
   - Gọn gàng.
   - Dễ đọc.
   - Trực quan.
   - Có phân cấp thông tin rõ ràng.
   - Phù hợp với phần mềm quản lý doanh nghiệp.

6. Không lạm dụng gradient, hiệu ứng phát sáng, hoạt ảnh, màu sắc rực rỡ hoặc quá nhiều thẻ lồng nhau.

7. Không dùng emoji thay thế icon giao diện nếu hệ thống đang sử dụng thư viện icon.

8. Responsive tốt trên máy tính, máy tính bảng và màn hình nhỏ.

==================================================
III. BỐ CỤC DASHBOARD
==================================================

Thiết kế một trang tổng quan hoàn chỉnh với các khu vực sau.

1. Phần tiêu đề

Hiển thị:
- Tiêu đề: Tổng quan hệ thống.
- Mô tả ngắn về tình hình hoạt động của trạm xăng.
- Ngày hiện tại theo thời gian hệ thống.
- Thông tin tài khoản đang đăng nhập nếu layout hiện tại đã hỗ trợ.
- Nút làm mới số liệu nếu phù hợp.

Không tạo các nút trang trí không có chức năng.

2. Bộ lọc thời gian

Cung cấp các lựa chọn phù hợp:
- Hôm nay.
- 7 ngày gần nhất.
- 30 ngày gần nhất.
- Tháng này.
- Khoảng thời gian tùy chọn.

Khi thay đổi khoảng thời gian, những chỉ số và biểu đồ liên quan phải được cập nhật theo dữ liệu thực tế.

Các thống kê về giao dịch phải sử dụng cùng quy tắc lọc thời gian để bảo đảm nhất quán.

Những chỉ số trạng thái hiện tại như số bồn chứa hoặc tình trạng tồn bồn cần được xác định rõ là số liệu tại thời điểm truy vấn, không được hiểu nhầm thành số liệu lịch sử của khoảng thời gian đã chọn.

3. Các thẻ KPI tổng quan

Thiết kế các thẻ thống kê nổi bật:
- Tổng tiền bán hàng đã duyệt trong khoảng thời gian.
- Tổng lượng xăng dầu đã bán.
- Tổng lượng xăng dầu đã nhập.
- Số giao dịch bán hàng đã duyệt.
- Số giao dịch nhập hàng đã duyệt.
- Số giao dịch đang chờ duyệt.
- Số bồn chứa đang hoạt động hoặc tổng số bồn chứa theo trạng thái thực tế.
- Tỷ lệ sử dụng dung tích bồn chứa nếu dữ liệu hợp lệ.

Không bắt buộc phải đặt tất cả KPI ở cùng một hàng. Hãy bố trí theo mức độ quan trọng, ưu tiên những chỉ số giúp người dùng hiểu nhanh tình hình hoạt động.

Nếu có thể so sánh với kỳ trước, hãy hiển thị mức tăng hoặc giảm kèm giá trị và tỷ lệ phần trăm. Chỉ thực hiện so sánh khi hai kỳ có phạm vi rõ ràng và dữ liệu đủ điều kiện.

Không tự tạo giá trị tăng trưởng, dữ liệu giả hoặc các con số cố định để làm đẹp giao diện.

4. Khu vực biểu đồ hoạt động

Tạo khu vực biểu đồ trực quan, có bố cục hợp lý.

Biểu đồ A — Hoạt động bán hàng:
- Thể hiện doanh thu bán hàng đã duyệt theo ngày hoặc theo tháng.
- Cho phép xem xu hướng lượng bán nếu dữ liệu hỗ trợ.
- Ưu tiên biểu đồ đường hoặc cột phù hợp với loại dữ liệu.

Biểu đồ B — Cơ cấu nhiên liệu:
- So sánh lượng bán theo từng loại nhiên liệu.
- Có thể sử dụng biểu đồ cột hoặc biểu đồ tròn nếu số nhóm phù hợp.
- Phải ghi rõ đơn vị và tên nhiên liệu.

Biểu đồ C — Nhập hàng và bán hàng:
- So sánh lượng nhập và lượng bán theo thời gian.
- Chỉ đặt hai đại lượng trên cùng biểu đồ khi đơn vị và cách nhóm dữ liệu tương thích.
- Nếu không tương thích, hãy tách biểu đồ hoặc trình bày bằng phương án dễ hiểu hơn.

Không bắt buộc phải sử dụng mọi biểu đồ nếu dữ liệu không đủ. Hãy ưu tiên ít biểu đồ nhưng có ý nghĩa.

5. Khu vực tình trạng bồn chứa

Tận dụng bảng bon_chua và nhien_lieu hiện có.

Hiển thị danh sách hoặc các thẻ bồn chứa với:
- Mã bồn.
- Tên bồn.
- Loại nhiên liệu.
- Sức chứa tối đa.
- Tồn hiện tại.
- Tỷ lệ đầy bồn.
- Trạng thái bồn.

Dùng thanh tiến trình để biểu diễn tỷ lệ đầy bồn.

Có thể sử dụng màu cảnh báo theo trạng thái và ngưỡng nghiệp vụ hợp lý:
- Tồn thấp.
- Tồn ở mức bình thường.
- Tồn gần đầy.

Không tự sửa số liệu tồn bồn và không tạo dữ liệu bồn giả.

Tỷ lệ đầy bồn chỉ được tính khi sức chứa hợp lệ và lớn hơn 0.

Có liên kết đến trang quản lý hoặc xem chi tiết bồn chứa hiện có nếu route thực sự tồn tại.

6. Khu vực giao dịch gần đây

Hiển thị một danh sách giao dịch gần đây, bao gồm bán hàng và nhập hàng nếu phù hợp.

Các cột có thể gồm:
- Mã giao dịch.
- Loại giao dịch.
- Ngày giờ.
- Nhân viên.
- Nhiên liệu.
- Số lượng.
- Thành tiền nếu có.
- Trạng thái duyệt.

Ưu tiên các giao dịch mới nhất.

Hiển thị trạng thái rõ ràng:
- Chờ duyệt.
- Đã duyệt.
- Đã từ chối.

Có nút xem chi tiết hoặc xem tất cả nếu chức năng tương ứng đã tồn tại.

Không đưa chức năng sửa, xóa hoặc duyệt giao dịch trực tiếp vào khu vực này. Đây chỉ là khu vực tổng quan và điều hướng.

7. Khu vực cần chú ý

Tổng hợp các thông tin thực sự cần người dùng quan tâm, chẳng hạn:
- Giao dịch đang chờ duyệt.
- Bồn chứa có tồn thấp.
- Dữ liệu bồn chứa không hợp lệ nếu có.
- Những cảnh báo bất thường đã được hệ thống phát hiện.
- Cảnh báo từ chức năng AI nếu đã triển khai và có dữ liệu thực.

Mỗi cảnh báo cần có:
- Nội dung ngắn gọn.
- Mức độ ưu tiên.
- Thông tin đối tượng liên quan nếu có.
- Liên kết đến chức năng xử lý hoặc xem chi tiết nếu route tồn tại.

Không tự phát minh cảnh báo. Nếu không có cảnh báo, hiển thị trạng thái bình thường phù hợp.

Không đưa các tình huống dữ liệu lỗi vào trạng thái vận hành bình thường. Các điều kiện như tồn âm hoặc tồn vượt sức chứa chỉ nên được báo cáo khi thực sự phát hiện dữ liệu không hợp lệ.

==================================================
IV. QUY TẮC TÍNH TOÁN
==================================================

Đây là phần bắt buộc phải chính xác.

1. Tổng tiền bán hàng phải được tính từ các giao dịch bán hàng đã duyệt.

2. Tổng lượng bán phải lấy từ các giao dịch bán hàng đã duyệt.

3. Tổng lượng nhập phải lấy từ các giao dịch nhập hàng đã duyệt.

4. Giao dịch Chờ duyệt và Đã từ chối không được cộng vào số liệu bán hàng hoặc nhập hàng thực tế.

5. Nếu hiển thị số giao dịch đang chờ duyệt, phải đếm riêng các giao dịch theo trạng thái thực tế.

6. Không JOIN nhiều bảng giao dịch theo cách làm nhân bản bản ghi và khiến tổng tiền hoặc số lượng bị cộng nhiều lần.

7. Không cộng các đơn vị đo khác nhau vào một tổng lượng nếu không có quy đổi hợp lệ.

8. Không gọi doanh thu là lợi nhuận. Không tính lợi nhuận nếu database không có đủ dữ liệu chi phí.

9. Không tự giả định tên cột, quan hệ hoặc trạng thái trong database. Hãy kiểm tra schema thực tế.

10. Những số liệu trạng thái hiện tại của bồn chứa phải được lấy từ database tại thời điểm truy vấn.

11. Không để dashboard tự thay đổi dữ liệu nghiệp vụ.

12. Các KPI, biểu đồ và bảng giao dịch phải nhất quán với nhau về phạm vi thời gian và điều kiện tính toán.

==================================================
V. PHÂN QUYỀN
==================================================

Dashboard dùng chung cho Quản lý và Kế toán.

1. Cả hai vai trò đều được truy cập dashboard.
2. Kiểm tra quyền truy cập ở backend.
3. Người chưa đăng nhập không được truy cập trái phép.
4. Nhân viên ca không được truy cập nếu chính sách phân quyền hiện tại không cho phép.
5. Không chỉ ẩn menu trên giao diện mà phải bảo vệ endpoint tương ứng.
6. Không thay đổi cơ chế phân quyền hiện có nếu không cần thiết.
7. Các liên kết điều hướng phải phù hợp với quyền của tài khoản đang đăng nhập.

==================================================
VI. HIỆU NĂNG VÀ XỬ LÝ LỖI
==================================================

1. Tổng hợp số liệu tại backend bằng SQL hoặc service phù hợp.
2. Tránh tải toàn bộ dữ liệu giao dịch về frontend rồi mới tính toán.
3. Tận dụng service hiện có để tránh lặp lại logic tính doanh thu, lượng bán và lượng nhập.
4. Xử lý đúng trường hợp không có dữ liệu, giá trị NULL hoặc mẫu số bằng 0.
5. Hiển thị trạng thái đang tải, lỗi truy vấn hoặc không có dữ liệu phù hợp.
6. Không để một biểu đồ lỗi làm hỏng toàn bộ dashboard nếu có thể xử lý độc lập.
7. Không hardcode dữ liệu KPI hoặc dữ liệu biểu đồ.
8. Có thể sử dụng cache nếu thực sự cần thiết, nhưng không được khiến số liệu hiển thị sai lệch hoặc quá cũ mà không có cơ chế làm mới hợp lý.

==================================================
VII. TÍCH HỢP VỚI HỆ THỐNG
==================================================

1. Giữ nguyên các chức năng đang hoạt động.
2. Tái sử dụng layout, sidebar, header, CSS và thư viện biểu đồ hiện có.
3. Không tạo một giao diện tách biệt với phần còn lại của hệ thống.
4. Không tạo bảng database mới.
5. Không tự ý đổi bộ màu chung của hệ thống.
6. Không sửa các chức năng bán hàng, nhập hàng, duyệt giao dịch hoặc quản lý bồn chứa ngoài phạm vi cần thiết.
7. Không ghi đè những thay đổi hiện có của người dùng.
8. Không tạo nút hoặc liên kết dẫn đến route không tồn tại.
9. Không sử dụng dữ liệu giả để làm dashboard trông đầy đủ hơn.

==================================================
VIII. KIỂM THỬ
==================================================

Kiểm tra tối thiểu:
- Quản lý truy cập được dashboard.
- Kế toán truy cập được dashboard.
- Người không có quyền không thể truy cập.
- Bộ lọc thời gian hoạt động chính xác.
- KPI khớp với dữ liệu thực tế.
- Biểu đồ và bảng giao dịch khớp nhau.
- Giao dịch chờ duyệt và bị từ chối không bị cộng vào số liệu thực tế.
- Không xảy ra đếm trùng khi tổng hợp nhiều bảng.
- Bồn chứa hiển thị đúng số liệu hiện tại.
- Không có dữ liệu vẫn hiển thị bình thường.
- Các liên kết điều hướng hoạt động đúng.
- Giao diện không bị vỡ trên màn hình nhỏ.
- Dashboard không làm thay đổi dữ liệu database.
- Những chức năng hiện có vẫn hoạt động sau khi triển khai.

==================================================
IX. CÁCH THỰC HIỆN
==================================================

Hãy chủ động đọc code, lập kế hoạch và triển khai trực tiếp.

Thực hiện theo thứ tự:
1. Khảo sát toàn bộ cấu trúc và giao diện hiện có.
2. Xác định bộ màu và các component dùng chung.
3. Kiểm tra schema và các chức năng nghiệp vụ hiện có.
4. Xác định các chỉ số có thể tổng hợp chính xác.
5. Thiết kế dashboard chuyên nghiệp nhưng đồng nhất với giao diện chung.
6. Triển khai backend, truy vấn, biểu đồ, KPI, danh sách giao dịch và cảnh báo.
7. Kiểm tra phân quyền.
8. Chạy các kiểm thử phù hợp và sửa lỗi phát sinh.
9. Tổng kết các file đã tạo hoặc sửa, cách truy cập, các chỉ số đã hoàn thành và kết quả kiểm thử.

Nếu một chỉ số không thể tính chính xác vì thiếu dữ liệu, hãy bỏ chỉ số đó hoặc nêu rõ giới hạn. Không bịa dữ liệu để lấp chỗ trống.

KẾT QUẢ MONG MUỐN:

Một dashboard tổng quan hệ thống có giao diện chuyên nghiệp, phối màu thống nhất với toàn bộ phần mềm, giúp Quản lý và Kế toán nhanh chóng nắm được tình hình bán hàng, nhập hàng, tồn bồn, giao dịch chờ duyệt và những vấn đề cần chú ý.

Dashboard phải sử dụng dữ liệu thật, tính toán chính xác, hoạt động ổn định và tích hợp trực tiếp vào hệ thống hiện tại.