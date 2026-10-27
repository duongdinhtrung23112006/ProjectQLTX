# NHIỆM VỤ: XÂY DỰNG CHỨC NĂNG QUẢN LÝ TỒN BỒN CHO QUẢN LÝ VÀ XEM TỒN BỒN CHO NHÂN VIÊN CA

## 1. Phạm vi

Triển khai hai giao diện:
1. Quản lý tồn bồn dành cho vai trò Quản lý.
2. Xem tồn bồn dành cho vai trò Nhân viên ca.

Đây là chức năng tổng hợp và trực quan hóa dữ liệu tồn bồn hiện có, không phải chức năng nhập/xuất kho hay điều chỉnh tồn.

Trước khi triển khai, hãy đọc cấu trúc repository, cơ chế đăng nhập và phân quyền, cách đăng ký Blueprint, cách kết nối database và các giao diện hiện có của dự án. Tái sử dụng phong cách UI, CSS, JavaScript và quy ước code hiện tại.

## 2. Ràng buộc database

- Database hiện tại là tram_xang.
- Tận dụng bảng bon_chua và nhien_lieu.
- Không tạo bảng mới.
- Không thêm, xóa hoặc sửa cột.
- Không thay đổi schema hoặc dữ liệu hiện có.
- Không tự ý cập nhật bon_chua.ton_hien_tai trong chức năng này.
- Không tạo dữ liệu giả để hiển thị.

Trước khi viết truy vấn, kiểm tra schema thực tế để xác định chính xác các cột và quan hệ.

## 3. Chức năng quản lý tồn bồn

Xây dựng trang tổng quan trực quan dành cho Quản lý.

### Thẻ thống kê
Hiển thị các số liệu được tính từ database:
- Tổng số bồn chứa.
- Tổng sức chứa của các bồn.
- Tổng lượng nhiên liệu đang tồn.
- Tỷ lệ lấp đầy tổng thể, tính bằng tổng tồn hiện tại chia tổng sức chứa, nhân 100.

Phải xử lý trường hợp tổng sức chứa bằng 0 để tránh lỗi chia cho 0. Chỉ tính trên những bồn phù hợp với quy tắc trạng thái hiện có; nếu loại trừ bồn ngừng hoạt động thì phải thể hiện quy tắc đó nhất quán.

### Danh sách bồn
Hiển thị:
- Mã bồn.
- Tên bồn.
- Tên loại nhiên liệu.
- Sức chứa tối đa.
- Tồn hiện tại.
- Dung tích còn trống.
- Tỷ lệ lấp đầy.
- Trạng thái bồn.

Công thức:
- Dung tích còn trống = sức chứa - tồn hiện tại.
- Tỷ lệ lấp đầy (%) = tồn hiện tại / sức chứa * 100.

Không tự ý ép số liệu âm hoặc vượt sức chứa về giá trị hợp lệ để che giấu dữ liệu bất thường. Nếu dữ liệu không hợp lý, cần hiển thị cảnh báo để quản lý kiểm tra.

### Trực quan hóa
- Dùng thẻ thống kê và thanh tiến trình biểu thị tỷ lệ lấp đầy từng bồn.
- Màu sắc cảnh báo phải nhất quán và có chú giải.
- Có thể đánh dấu bồn gần hết hoặc bồn có dữ liệu bất thường.
- Ngưỡng cảnh báo cần được xác định từ cấu hình hoặc quy ước sẵn có. Nếu dự án chưa có ngưỡng, hãy chọn một ngưỡng mặc định hợp lý trong code và ghi rõ để có thể thay đổi; không cần thêm cột database.

### Tìm kiếm và lọc
- Tìm kiếm theo mã bồn hoặc tên bồn.
- Lọc theo loại nhiên liệu.
- Lọc theo trạng thái bồn.
- Hiển thị trạng thái không có kết quả khi danh sách rỗng.

Chức năng này chỉ tổng hợp và hiển thị dữ liệu, không có nút thêm, sửa, xóa bồn hoặc điều chỉnh tồn.

## 4. Chức năng xem tồn bồn cho Nhân viên ca

Tạo trang xem tồn bồn riêng cho Nhân viên ca, tận dụng nguồn dữ liệu và logic tính toán từ chức năng quản lý khi phù hợp.

Hiển thị:
- Mã và tên bồn.
- Loại nhiên liệu.
- Sức chứa.
- Tồn hiện tại.
- Dung tích còn trống.
- Tỷ lệ lấp đầy.
- Trạng thái bồn.

Cho phép tìm kiếm và lọc dữ liệu tương tự trang quản lý nếu phù hợp.

Đây là chức năng chỉ đọc:
- Không có thao tác thêm, sửa, xóa hoặc điều chỉnh tồn.
- Backend không được cung cấp endpoint thay đổi tồn cho Nhân viên ca.
- Không được trừ tồn từ phiếu bán đang Chờ duyệt.
- Không tự cộng tồn từ phiếu nhập đang Chờ duyệt.
- Hiển thị số liệu thực tế đang được lưu trong bon_chua.ton_hien_tai.

## 5. Phân quyền

- Trang quản lý tồn bồn chỉ dành cho vai trò Quản lý.
- Trang xem tồn bồn chỉ dành cho vai trò Nhân viên ca, theo cơ chế phân quyền hiện tại.
- Sử dụng cơ chế xác thực và decorator hiện có trong dự án.
- Kiểm tra quyền ở backend, không chỉ ẩn menu hoặc nút trên giao diện.
- Không làm ảnh hưởng đến các vai trò khác.

## 6. Giao diện và chất lượng code

- Khảo sát các trang quản lý và nhân viên hiện có trước khi tạo template.
- Tái sử dụng layout chung, menu, CSS và cách hiển thị thông báo hiện có.
- Giao diện rõ ràng, trực quan, responsive.
- Dùng truy vấn tham số, không ghép dữ liệu người dùng trực tiếp vào SQL.
- Dùng đúng cách kết nối và đóng kết nối database hiện tại.
- Không sửa nghiệp vụ nhập hàng, bán hàng hoặc cập nhật tồn.
- Bảo toàn mọi thay đổi chưa commit của người dùng.
- Không tự ý commit hoặc push Git.

## 7. Kiểm thử

Kiểm tra tối thiểu:
1. Quản lý truy cập được trang tổng quan tồn bồn.
2. Nhân viên ca truy cập được trang xem tồn bồn.
3. Người chưa đăng nhập hoặc sai vai trò bị từ chối.
4. Các số liệu tổng hợp và tỷ lệ lấp đầy được tính chính xác.
5. Tìm kiếm và lọc hoạt động đúng.
6. Dữ liệu bồn có sức chứa bằng 0 hoặc tồn bất thường không làm trang lỗi.
7. Chức năng chỉ đọc không thay đổi database.
8. Phiếu Chờ duyệt không làm thay đổi số tồn hiển thị.
9. Các chức năng hiện có vẫn hoạt động bình thường.

Không tuyên bố kiểm thử thành công nếu chưa thực sự chạy.

## 8. Thực hiện và báo cáo

Trực tiếp khảo sát và chỉnh sửa code trong workspace, không chỉ đưa ra kế hoạch hoặc code minh họa.

Sau khi hoàn thành, báo cáo:
- Các file đã tạo/sửa.
- Các route đã triển khai.
- Cách phân quyền.
- Các công thức thống kê đã sử dụng.
- Kết quả kiểm thử thực tế.
- Các vấn đề còn tồn tại.

Điều kiện hoàn thành: Hai vai trò có giao diện tồn bồn phù hợp quyền hạn, dữ liệu lấy từ database thật, hiển thị trực quan và không có bất kỳ thay đổi schema hay cập nhật tồn nào từ chức năng này.

## BỔ SUNG: CHỨC NĂNG XEM CHI TIẾT BỒN CHỨA

Cả giao diện Quản lý tồn bồn và giao diện Nhân viên ca xem tồn bồn đều phải có nút "Xem chi tiết" ở mỗi dòng bồn trong danh sách.

Khi nhấn nút, mở trang chi tiết bồn chứa với các thông tin:
- Mã bồn, tên bồn và trạng thái.
- Loại nhiên liệu đang chứa.
- Sức chứa tối đa.
- Tồn hiện tại.
- Dung tích còn trống.
- Tỷ lệ lấp đầy, thể hiện bằng thanh tiến trình trực quan.
- Cảnh báo nếu tồn bất thường, tồn âm hoặc vượt sức chứa.

Yêu cầu:
1. Lấy dữ liệu trực tiếp từ database hiện có, không tạo dữ liệu giả.
2. Dùng chung logic truy vấn và tính toán giữa hai vai trò khi phù hợp.
3. Giao diện chi tiết phải đồng bộ với phong cách thiết kế hiện tại của dự án.
4. Có nút quay lại danh sách tồn bồn.
5. Kiểm tra quyền truy cập ở backend; không được truy cập trái phép chỉ bằng cách nhập URL trực tiếp.
6. Nhân viên ca chỉ được xem, tuyệt đối không có chức năng sửa, xóa hoặc điều chỉnh tồn.
7. Quản lý cũng chỉ xem và theo dõi trong phạm vi chức năng này; không thêm thao tác sửa tồn hoặc cập nhật database.
8. Không tạo bảng mới, không thay đổi schema và không cập nhật bon_chua.ton_hien_tai.
9. Nếu bồn không tồn tại, hiển thị thông báo phù hợp thay vì lỗi máy chủ.

Bổ sung kiểm thử cho chức năng xem chi tiết, quyền truy cập trực tiếp bằng URL và trường hợp bồn không tồn tại.