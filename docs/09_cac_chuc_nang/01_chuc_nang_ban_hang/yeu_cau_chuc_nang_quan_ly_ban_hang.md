# NHIỆM VỤ: TRIỂN KHAI CHỨC NĂNG QUẢN LÝ PHIẾU BÁN HÀNG

## 1. Phạm vi

Triển khai chức năng quản lý phiếu bán hàng dành cho vai trò Quản lý trong dự án hiện có.

Trước khi làm, hãy đọc và khảo sát:
- Toàn bộ chức năng quản lý nhập hàng hiện có, đặc biệt là danh sách, xem chi tiết, duyệt, từ chối và xóa.
- Chức năng bán hàng dành cho Nhân viên ca đã triển khai.
- Cơ chế đăng nhập, phân quyền, đăng ký Blueprint, kết nối database và quy ước xử lý trạng thái.
- Schema database thực tế, đặc biệt các bảng ban_hang, bon_chua, nhien_lieu, ca_lam_viec, nhan_vien và tai_khoan.

Ưu tiên tái sử dụng cách tổ chức code, nghiệp vụ, giao diện và xử lý trạng thái của chức năng quản lý nhập hàng. Không tự tạo một quy trình khác nếu dự án đã có quy ước phù hợp.

## 2. Giao diện danh sách bán hàng

Giao diện index bán hàng của quản lý phải giống giao diện index bán hàng của nhân viên về:
- Bố cục tổng thể.
- Bảng danh sách phiếu.
- Các thông tin hiển thị.
- Thanh tìm kiếm, bộ lọc và cách phân trang nếu có.
- CSS, màu sắc, nút bấm, thông báo và responsive.

Tuy nhiên, danh sách của quản lý phải phục vụ nghiệp vụ quản lý và xét duyệt phiếu, không bị giới hạn vào các phiếu do chính quản lý tạo. Hãy đối chiếu phạm vi dữ liệu của chức năng quản lý nhập hàng để áp dụng đúng.

Không sao chép mù quáng toàn bộ template nếu có thể tái sử dụng template hoặc thành phần hiện có một cách an toàn.

## 3. Quy tắc hiển thị thao tác theo trạng thái

Mỗi phiếu có trạng thái và các nút thao tác tương ứng như sau:

### Trạng thái Chờ duyệt
Hiển thị:
- Xem
- Duyệt
- Từ chối
- Xóa

### Trạng thái Đã duyệt
Chỉ hiển thị:
- Xem
- Xóa

### Trạng thái Đã từ chối
Chỉ hiển thị:
- Xem
- Xóa

Không hiển thị nút Duyệt hoặc Từ chối đối với phiếu đã được duyệt hoặc đã bị từ chối.

Đây là quy tắc giao diện. Backend cũng phải kiểm tra trạng thái thực tế trong database để ngăn request không hợp lệ, không chỉ dựa vào việc ẩn nút trên HTML.

## 4. Xem chi tiết phiếu

Xây dựng hoặc tái sử dụng trang xem chi tiết phiếu bán, hiển thị đầy đủ thông tin cần thiết:
- Mã phiếu.
- Ngày và giờ bán.
- Nhân viên lập phiếu.
- Ca làm việc.
- Nhiên liệu và bồn chứa.
- Số lượng.
- Đơn giá.
- Thành tiền.
- Ghi chú.
- Trạng thái hiện tại.

Giao diện phải nhất quán với trang xem chi tiết của chức năng quản lý nhập hàng và chức năng bán hàng của nhân viên.

## 5. Chức năng duyệt phiếu

Khi quản lý chọn Duyệt:
1. Kiểm tra quyền Quản lý ở backend.
2. Xác minh phiếu tồn tại và đang ở trạng thái Chờ duyệt.
3. Kiểm tra lại dữ liệu phiếu và tính hợp lệ của bồn chứa, nhiên liệu, số lượng.
4. Kiểm tra tồn bồn hiện tại trong database.
5. Nếu tồn đủ, thực hiện trừ tồn bồn và chuyển trạng thái phiếu sang Đã duyệt trong cùng một transaction.
6. Nếu tồn không đủ hoặc xảy ra lỗi, rollback toàn bộ transaction; không trừ tồn một phần và không chuyển trạng thái.
7. Thông báo kết quả rõ ràng cho người dùng.

Phải xử lý an toàn khi hai phiếu cùng được duyệt gần như đồng thời. Sử dụng transaction và cơ chế khóa hoặc cập nhật có điều kiện phù hợp với database hiện tại để không bán vượt tồn.

Phiếu đã duyệt không được duyệt lại.

Trước khi triển khai, hãy kiểm tra xem dự án đã có service hoặc quy tắc cập nhật tồn khi duyệt nhập hàng hay chưa. Chỉ tái sử dụng khi đúng nghiệp vụ; không được áp dụng nhầm logic nhập hàng cho bán hàng.

## 6. Chức năng từ chối phiếu

Khi quản lý chọn Từ chối:
1. Chỉ cho phép từ chối phiếu đang Chờ duyệt.
2. Chuyển trạng thái sang Đã từ chối theo đúng quy ước trạng thái của dự án.
3. Không thay đổi tồn bồn.
4. Nếu chức năng quản lý nhập hàng có lưu lý do từ chối, hãy khảo sát cách triển khai và áp dụng nhất quán cho phiếu bán hàng. Không tự ý thêm cột hoặc thay đổi schema nếu chưa xác minh sự cần thiết.
5. Có xác nhận thao tác và thông báo kết quả.
6. Không cho từ chối lại phiếu đã duyệt hoặc đã bị từ chối.

Nếu cần lưu lý do từ chối mà schema hiện tại chưa hỗ trợ, hãy kiểm tra các trường sẵn có và báo cáo trước khi thực hiện thay đổi schema không cần thiết.

## 7. Chức năng xóa phiếu

Nút Xóa xuất hiện với cả ba trạng thái:
- Chờ duyệt.
- Đã duyệt.
- Đã từ chối.

Tuy nhiên, phải bảo đảm dữ liệu tồn bồn chính xác:
- Phiếu Chờ duyệt chưa trừ tồn, nên xóa không làm thay đổi tồn bồn.
- Phiếu Đã từ chối chưa trừ tồn, nên xóa không làm thay đổi tồn bồn.
- Phiếu Đã duyệt đã trừ tồn. Nếu cho phép xóa, phải hoàn trả đúng số lượng về đúng bồn trong cùng transaction với thao tác xóa để không làm sai lệch tồn.

Trước khi xóa phiếu đã duyệt, phải có hộp thoại xác nhận rõ ràng. Backend phải kiểm tra trạng thái và dữ liệu thực tế trước khi hoàn trả tồn.

Chỉ dùng phương thức POST hoặc phương thức thay đổi dữ liệu phù hợp với kiến trúc hiện có; tuyệt đối không xóa bằng GET.

Nếu dự án có quy định nghiệp vụ khác về xóa phiếu đã duyệt, hãy đối chiếu chức năng quản lý nhập hàng và báo cáo điểm khác biệt trước khi tự quyết định.

## 8. Database và trạng thái

Kiểm tra schema thực tế của bảng ban_hang trước khi sửa.

Các trạng thái nghiệp vụ cần hỗ trợ:
- Chờ duyệt.
- Đã duyệt.
- Đã từ chối.

Sử dụng đúng quy ước trạng thái đang tồn tại trong dự án. Nếu tên trạng thái thực tế khác, hãy thống nhất theo quy ước hiện có và không tạo ra nhiều cách viết khác nhau cho cùng một trạng thái.

Không chạy lại câu ALTER TABLE nếu cột trạng thái đã tồn tại. Không tạo lại bảng, xóa dữ liệu hoặc tự ý sửa schema không cần thiết.

Không triển khai trạng thái duyệt giả lập ở frontend; mọi thay đổi phải được lưu thực sự trong database.

## 9. Phân quyền và bảo toàn chức năng hiện có

- Chỉ vai trò Quản lý được truy cập các route quản lý phiếu bán hàng.
- Dùng cơ chế phân quyền hiện tại của dự án.
- Nhân viên ca không được gọi trực tiếp các endpoint duyệt hoặc từ chối.
- Kiểm tra quyền ở backend cho từng thao tác.
- Không sửa chức năng bán hàng dành cho nhân viên ngoài những thay đổi tích hợp tối thiểu và thực sự cần thiết.
- Không làm ảnh hưởng chức năng quản lý nhập hàng, đăng nhập, ca làm việc, nhiên liệu hoặc bồn chứa.
- Bảo toàn mọi thay đổi Git chưa commit. Không tự ý khôi phục, ghi đè hoặc xóa file đang được chỉnh sửa.
- Không tự ý commit hoặc push Git.

## 10. Kiểm thử

Chạy các kiểm thử phù hợp với cấu trúc dự án, tối thiểu gồm:

1. Quản lý xem được danh sách phiếu bán.
2. Danh sách có đúng các nút theo từng trạng thái.
3. Duyệt phiếu hợp lệ làm chuyển trạng thái và trừ tồn đúng một lần.
4. Duyệt phiếu khi tồn không đủ không làm thay đổi tồn hoặc trạng thái.
5. Hai yêu cầu duyệt đồng thời không làm tồn âm.
6. Không thể duyệt hoặc từ chối phiếu không ở trạng thái Chờ duyệt.
7. Từ chối phiếu không làm thay đổi tồn bồn.
8. Xóa phiếu Chờ duyệt hoặc Đã từ chối không làm thay đổi tồn.
9. Xóa phiếu Đã duyệt hoàn trả đúng lượng tồn theo transaction.
10. Người không có quyền Quản lý không thể truy cập endpoint quản lý.
11. Các chức năng bán hàng nhân viên và quản lý nhập hàng vẫn hoạt động.
12. Tìm kiếm, lọc và xem chi tiết không bị lỗi.

Không tuyên bố kiểm thử thành công nếu chưa thực sự chạy. Nếu không thể chạy do thiếu database hoặc cấu hình, nêu rõ nguyên nhân.

## 11. Cách thực hiện

Trực tiếp chỉnh sửa code trong workspace, không chỉ đưa ra kế hoạch hoặc ví dụ code.

Sau khi hoàn thành, báo cáo:
- Các file đã tạo và sửa.
- Các route đã triển khai.
- Quy tắc trạng thái và phân quyền.
- Cách xử lý transaction khi duyệt và xóa phiếu.
- Kết quả kiểm thử thực tế.
- Những vấn đề còn tồn tại.

Ưu tiên thay đổi tối thiểu, đúng kiến trúc dự án và đồng bộ với chức năng quản lý nhập hàng hiện có.