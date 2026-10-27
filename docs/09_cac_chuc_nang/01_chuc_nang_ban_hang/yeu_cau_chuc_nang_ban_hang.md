YÊU CẦU TRIỂN KHAI CHỨC NĂNG BÁN HÀNG DÀNH CHO NHÂN VIÊN CA
1. Mục tiêu và giới hạn phạm vi
Triển khai hoàn chỉnh chức năng lập và quản lý phiếu bán hàng dành cho Nhân viên ca trong dự án quản lý trạm xăng hiện có.

Phạm vi chỉ bao gồm phía Nhân viên ca. Không triển khai giao diện/quy trình duyệt dành cho quản lý trong nhiệm vụ này. Tuy nhiên, dữ liệu và nghiệp vụ phải sẵn sàng để quản lý có thể duyệt phiếu ở giai đoạn sau.

Không tự ý mở rộng sang chức năng quản lý, kế toán, báo cáo quản lý hoặc sửa các nghiệp vụ không liên quan.
2. Quy trình nghiệp vụ đã thống nhất
1. Nhân viên ca đăng nhập và mở chức năng bán hàng.
2. Nhân viên tạo phiếu bán. Sau khi tạo thành công, phiếu phải xuất hiện trong danh sách với trạng thái Chờ duyệt.
3. Với phiếu ở trạng thái Chờ duyệt, nhân viên được phép:
   - Xem danh sách và chi tiết.
   - Tìm kiếm/lọc phiếu.
   - Sửa phiếu.
   - Xóa phiếu.
4. Khi phiếu đã được quản lý duyệt và chuyển sang trạng thái Đã duyệt, nhân viên chỉ được xem; không được sửa hoặc xóa.
5. Trong nhiệm vụ hiện tại, chỉ xây dựng phía Nhân viên ca. Không tạo trang hoặc endpoint duyệt phiếu cho quản lý. Không giả lập việc duyệt.
6. Chọn phương án B cho tồn bồn: tạo, sửa hoặc xóa phiếu đang Chờ duyệt không làm thay đổi bon_chua.ton_hien_tai. Chỉ khi quản lý duyệt thành công trong giai đoạn sau mới kiểm tra tồn thực tế và trừ tồn.
7. Vì tồn chỉ bị trừ khi duyệt, ở giai đoạn nhân viên lập phiếu cần kiểm tra dữ liệu hợp lệ và có thể cảnh báo lượng tồn hiện tại tham khảo, nhưng không được coi đó là cam kết tồn sẽ còn đủ tại thời điểm duyệt.
8. Khi duyệt trong tương lai, hệ thống phải kiểm tra tồn mới nhất trong transaction; nếu tồn không đủ thì không được duyệt, không trừ tồn và không chuyển trạng thái sang Đã duyệt. Phần duyệt này chỉ là yêu cầu tương thích nghiệp vụ, không triển khai trong nhiệm vụ hiện tại.
3. Database hiện có
Database: tram_xang.

Bảng ban_hang đã được tạo với các cột:
- id INT — khóa chính, tự tăng.
- ma_ban VARCHAR(20) — mã phiếu, duy nhất, không null.
- ngay_ban DATE — không null.
- gio_ban TIME — không null.
- ca_lam_viec_id INT — khóa ngoại đến ca_lam_viec(id).
- nhan_vien_id INT — khóa ngoại đến nhan_vien(id).
- nhien_lieu_id INT — khóa ngoại đến nhien_lieu(id).
- bon_id INT — khóa ngoại đến bon_chua(id).
- so_luong INT — không null, phải lớn hơn 0.
- don_gia DECIMAL(12,2) — không null, không âm.
- thanh_tien DECIMAL(14,2) — không null, không âm.
- ghi_chu TEXT NULL.
Cần có thêm cột trạng thái cho phiếu. Trước khi thay đổi database, hãy kiểm tra schema thực tế để xác nhận cột đã tồn tại chưa. Nếu chưa có thì bổ sung tối thiểu:
ALTER TABLE ban_hang
ADD COLUMN trang_thai VARCHAR(30)
NOT NULL DEFAULT 'Chờ duyệt';
Không chạy lại câu lệnh trên nếu cột trang_thai đã tồn tại. Không tự ý tạo lại bảng, xóa dữ liệu, đổi tên cột hoặc thay đổi cấu trúc không cần thiết.

Các bảng liên quan đã được xác nhận có cấu trúc chính như sau:
nhan_vien
- id
- ma_nv
- ho_ten
- so_dien_thoai
- dia_chi
- chuc_vu
- ngay_vao_lam
- trang_thai
ca_lam_viec
- id
- ma_ca
- ten_ca
- ngay_lam_viec
- nhan_vien_id
- trang_thai
- gio_bat_dau
- gio_ket_thuc
nhien_lieu
- id
- ma_nhien_lieu
- ten_nhien_lieu
- don_vi
- don_gia
- trang_thai
bon_chua
- id
- ma_bon
- ten_bon
- nhien_lieu_id
- suc_chua
- ton_hien_tai
- trang_thai
tai_khoan
- id
- ten_dang_nhap
- mat_khau
- vai_tro
- nhan_vien_id
Đây là thông tin schema đã biết; vẫn phải khảo sát schema thực tế và các ràng buộc trong repository trước khi viết truy vấn. Không đoán tên cột hoặc quan hệ khi có thể kiểm tra trực tiếp.
4. Khảo sát repository trước khi sửa
Trước khi triển khai:
1. Đọc cấu trúc dự án và cách đăng ký Blueprint.
2. Đọc route đăng nhập, cơ chế phân quyền và cách lấy nhân viên hiện tại từ session.
3. Đọc toàn bộ chức năng nhập hàng hiện có để tái sử dụng cách tổ chức route, template, CSS, JavaScript, thông báo và giao diện.
4. Đọc services/database.py và các service liên quan để dùng đúng cách kết nối database.
5. Kiểm tra schema thực tế của các bảng liên quan, đặc biệt là ban_hang, ca_lam_viec, nhien_lieu, bon_chua, nhan_vien, tai_khoan.
6. Xác định chính xác tên trường session và các giá trị vai trò/trạng thái đang dùng trong dự án.
7. Xem các thay đổi Git đang có trước khi sửa; giữ nguyên mọi công việc dở dang không thuộc phạm vi này.
Không dừng ở việc đưa ra kế hoạch. Sau khi khảo sát, hãy trực tiếp triển khai trong workspace.
5. Phân quyền và dữ liệu nhân viên
- Các route của chức năng này chỉ dành cho vai trò Nhân viên ca, sử dụng cơ chế phân quyền hiện có, ví dụ decorator yeu_cau_vai_tro("Nhân viên ca") nếu đó là cách dự án đang dùng.
- Lấy tài khoản đang đăng nhập từ session hiện có (đã thấy chức năng nhập hàng dùng session.get("tai_khoan_id"); hãy xác minh rồi dùng nhất quán).
- Từ tài khoản đăng nhập, xác định nhan_vien_id tương ứng. Không cho người dùng tự gửi nhan_vien_id để tạo/sửa phiếu.
- Danh sách và chi tiết phiếu của nhân viên chỉ được hiển thị trong phạm vi dữ liệu mà quy tắc hiện có cho phép. Mặc định, nhân viên chỉ quản lý phiếu do chính mình lập; hãy đối chiếu nghiệp vụ và cách phân quyền hiện có trước khi chốt truy vấn.
- Không tin dữ liệu phân quyền, nhân viên, ca, giá hoặc tổng tiền do trình duyệt gửi lên. Backend phải xác minh lại.
6. Chức năng giao diện cần triển khai
Tổ chức template theo quy ước hiện có của dự án và tham khảo giao diện chức năng nhập hàng để bảo đảm đồng nhất.
6.1. Danh sách phiếu bán
Hiển thị tối thiểu:
- Mã phiếu bán.
- Ngày, giờ bán.
- Ca làm việc.
- Nhân viên lập phiếu.
- Nhiên liệu.
- Bồn chứa.
- Số lượng.
- Đơn giá.
- Thành tiền.
- Trạng thái.
- Các thao tác phù hợp với trạng thái.
Có:
- Tìm kiếm theo mã phiếu và các tiêu chí phù hợp với dữ liệu hiện có.
- Lọc theo trạng thái Chờ duyệt / Đã duyệt.
- Lọc theo ngày hoặc khoảng ngày nếu phù hợp với cấu trúc giao diện hiện tại.
- Thông báo trạng thái khi danh sách rỗng hoặc không có kết quả.
- Nút tạo phiếu mới.
Quy tắc nút thao tác:
- Chờ duyệt: có Xem, Sửa, Xóa.
- Đã duyệt: chỉ có Xem.
- Ẩn nút là chưa đủ; backend cũng phải từ chối mọi request sửa/xóa phiếu đã duyệt.
6.2. Tạo phiếu bán
Biểu mẫu cần có:
- Mã phiếu bán được sinh theo quy ước nhất quán, không trùng.
- Ngày và giờ bán theo quy tắc nghiệp vụ hiện có.
- Nhân viên hiện tại tự xác định từ session, chỉ hiển thị để biết, không cho chọn người khác.
- Ca làm việc hợp lệ của nhân viên theo lịch và quy tắc hiện có.
- Nhiên liệu đang hoạt động/được phép bán.
- Bồn chứa đang hoạt động và phải chứa đúng loại nhiên liệu đã chọn.
- Số lượng bán.
- Đơn giá lấy từ dữ liệu giá hiện có ở backend.
- Thành tiền tự tính.
- Ghi chú không bắt buộc.
Xác thực phía backend:
- Phiếu mới luôn có trạng thái Chờ duyệt.
- so_luong phải là số nguyên dương.
- Nhiên liệu và bồn phải hợp lệ, hoạt động và khớp nhau.
- Ca phải hợp lệ với nhân viên hiện tại theo nghiệp vụ hiện có.
- Không tin don_gia hoặc thanh_tien do client gửi; backend tự lấy giá và tính tổng tiền.
- Không trừ hoặc cập nhật bon_chua.ton_hien_tai khi tạo phiếu.
- Nếu tồn tham khảo không đủ, có thể cảnh báo người dùng rằng phiếu có thể không được duyệt sau này; không được âm thầm trừ tồn hay tự chuyển sang Đã duyệt.
- Xử lý mã phiếu trùng và lỗi dữ liệu rõ ràng.
6.3. Xem chi tiết phiếu
Hiển thị đầy đủ thông tin phiếu và trạng thái hiện tại.

Nếu hiển thị tồn bồn, phải ghi rõ đó là tồn hiện tại tại thời điểm xem, không phải tồn đã bị trừ bởi phiếu đang chờ duyệt. Phiếu Chờ duyệt chưa làm thay đổi tồn.
6.4. Sửa phiếu
- Chỉ cho sửa khi trạng thái là Chờ duyệt.
- Backend phải truy vấn trạng thái hiện tại từ database ngay khi xử lý request; không dựa vào trạng thái từ form.
- Xác thực lại ca, nhiên liệu, bồn, số lượng và giá.
- Tính lại thanh_tien ở backend.
- Phiếu sau khi sửa vẫn ở trạng thái Chờ duyệt.
- Không cập nhật tồn bồn khi sửa phiếu chờ duyệt.
- Không cho sửa ma_ban, nhân viên lập phiếu hoặc các trường hệ thống nếu quy ước hiện tại không cho phép.
- Nếu phiếu đã được duyệt trong lúc người dùng đang mở trang sửa, backend phải từ chối cập nhật.
6.5. Xóa phiếu
- Chỉ xóa bằng phương thức POST, có xác nhận ở giao diện.
- Chỉ cho xóa phiếu đang Chờ duyệt.
- Backend phải xác minh quyền sở hữu/phạm vi dữ liệu và trạng thái hiện tại trước khi xóa.
- Phiếu đã duyệt không được xóa.
- Vì phiếu chờ duyệt chưa trừ tồn nên xóa phiếu không được cộng/trừ tồn bồn.
- Hiển thị thông báo thành công/thất bại rõ ràng.
7. Quy tắc tồn bồn và tính nhất quán dữ liệu
Áp dụng đúng phương án B:
- Tạo phiếu Chờ duyệt: không đổi bon_chua.ton_hien_tai.
- Sửa phiếu Chờ duyệt: không đổi bon_chua.ton_hien_tai.
- Xóa phiếu Chờ duyệt: không đổi bon_chua.ton_hien_tai.
- Chức năng duyệt ở giai đoạn sau mới có quyền trừ tồn, sau khi kiểm tra tồn mới nhất trong transaction.
Trong phạm vi hiện tại, không triển khai route duyệt hoặc logic trừ tồn khi duyệt. Không tự tạo các trạng thái khác ngoài những trạng thái cần thiết đã thống nhất, trừ khi repository đang có quy ước bắt buộc.
8. Giá bán và lịch sử giao dịch
- Đơn giá phải được xác định từ backend và dữ liệu nhiên liệu hiện tại theo quy tắc dự án.
- thanh_tien được backend tính lại từ số lượng và đơn giá.
- Không tin các giá trị tính toán từ JavaScript.
- Không tự ý thay đổi nghiệp vụ giá lịch sử nếu dự án đã có quy ước lưu giá tại thời điểm lập phiếu. Nếu chưa rõ, kiểm tra cách các chức năng hiện tại lưu giá và áp dụng nhất quán.
- Không thêm trường hoặc sửa schema ngoài mức tối thiểu cần thiết nếu chưa chứng minh được lý do.
9. Giao diện và chất lượng mã nguồn
- Tái sử dụng phong cách, bố cục, thành phần và cách thông báo của chức năng nhập hàng hiện có.
- Đọc các file HTML/CSS/JS hiện có trước khi tạo mới; không sao chép mù quáng hoặc phá vỡ layout dùng chung.
- Dùng đúng quy ước đặt tên, cấu trúc Blueprint, xử lý kết nối/đóng kết nối database và xử lý lỗi của dự án.
- Không để SQL injection; dùng truy vấn tham số.
- Không dùng GET để xóa hoặc thay đổi dữ liệu.
- Không sửa các chức năng đăng nhập, nhập hàng, quản lý, kế toán hoặc file khác ngoài phạm vi, trừ thay đổi tích hợp tối thiểu có lý do rõ ràng.
- Bảo toàn các thay đổi chưa commit của người dùng. Không chạy lệnh Git làm mất dữ liệu, không tự ý commit/push.
10. Kiểm thử bắt buộc
Thực hiện các kiểm thử phù hợp với cấu trúc dự án, tối thiểu bao gồm:
1. Nhân viên ca hợp lệ tạo được phiếu và phiếu xuất hiện trong danh sách ở trạng thái Chờ duyệt.
2. Tạo phiếu không làm thay đổi tồn bồn.
3. Sửa phiếu Chờ duyệt thành công và vẫn không thay đổi tồn bồn.
4. Xóa phiếu Chờ duyệt thành công và không thay đổi tồn bồn.
5. Phiếu Đã duyệt chỉ xem được; endpoint sửa/xóa phải từ chối.
6. Người chưa đăng nhập hoặc sai vai trò không truy cập được route.
7. Không thể giả mạo nhan_vien_id, ca_lam_viec_id, don_gia, thanh_tien hoặc trạng thái từ client.
8. Từ chối số lượng bằng 0, số âm, số không nguyên hoặc dữ liệu không hợp lệ.
9. Từ chối bồn không khớp loại nhiên liệu, bồn/nguyên liệu không hoạt động hoặc ca không hợp lệ.
10. Mã phiếu không bị trùng; lỗi database được xử lý rõ ràng.
11. Tìm kiếm và lọc trạng thái/ngày trả kết quả đúng.
12. Các chức năng hiện có, đặc biệt đăng nhập và nhập hàng, không bị ảnh hưởng.
Nếu không thể chạy một kiểm thử do thiếu cấu hình/database, phải nêu chính xác kiểm thử nào chưa chạy và lý do. Không tuyên bố kiểm thử thành công nếu chưa thực sự chạy.
11. Cách thực hiện và báo cáo kết quả
- Trực tiếp chỉnh sửa và tạo các file cần thiết trong workspace.
- Không chỉ trả về kế hoạch, ví dụ code hoặc hướng dẫn để người dùng tự làm.
- Không hỏi lại những thông tin có thể xác định bằng cách đọc repository và schema thực tế.
- Không tự ý thay đổi database ngoài phần tối thiểu đã nêu. Nếu phát hiện cần thay đổi schema khác, giải thích lý do và báo trước thay vì tự ý làm thay đổi phá hủy dữ liệu.
- Sau khi hoàn thành, báo cáo:
  1. Các file đã tạo/sửa.
  2. Các route và chức năng đã triển khai.
  3. Cách phân quyền và xử lý trạng thái.
  4. Xác nhận thao tác tạo/sửa/xóa phiếu chờ duyệt không thay đổi tồn.
  5. Các kiểm thử đã chạy cùng kết quả thực tế.
  6. Các vấn đề còn tồn tại hoặc phần chưa thể kiểm thử.
Điều kiện hoàn thành: Nhân viên ca có thể lập, xem, tìm kiếm/lọc, sửa và xóa phiếu Chờ duyệt; phiếu Đã duyệt chỉ được xem; các thao tác trong phạm vi nhân viên không thay đổi tồn bồn; và không có chức năng duyệt dành cho quản lý được triển khai trong nhiệm vụ này.