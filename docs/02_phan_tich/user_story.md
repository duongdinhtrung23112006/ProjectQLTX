# USER STORY

## 1. Xác thực và phân quyền

| Mã | User Story | Acceptance Criteria |
|---|---|---|
| US01 | Là người dùng, tôi muốn đăng nhập để truy cập hệ thống. | Đúng tài khoản thì đăng nhập thành công; sai thông tin thì bị từ chối. |
| US02 | Là quản lý, tôi muốn phân quyền để mỗi vai trò chỉ truy cập chức năng được phép. | Truy cập đúng quyền được phép; truy cập trái quyền bị từ chối. |

## 2. Nhiên liệu và bồn chứa

| Mã | User Story | Acceptance Criteria |
|---|---|---|
| US03 | Là quản lý, tôi muốn quản lý bồn chứa để kiểm soát các bồn trong trạm. | Có thể thêm, xem, sửa và cập nhật trạng thái bồn. |
| US04 | Là nhân viên ca, tôi muốn xem bồn chứa để biết tình trạng tồn hiện tại. | Xem được thông tin bồn và tồn hiện tại. |
| US05 | Là quản lý, tôi muốn quản lý nhiên liệu để duy trì danh mục nhiên liệu. | Có thể thêm, xem, sửa và cập nhật trạng thái nhiên liệu. |
| US06 | Là nhân viên ca, tôi muốn xem nhiên liệu để lựa chọn đúng loại khi thực hiện nghiệp vụ. | Chỉ hiển thị nhiên liệu tồn tại trong hệ thống. |

## 3. Nhập và bán hàng

| Mã | User Story | Acceptance Criteria |
|---|---|---|
| US07 | Là nhân viên ca hoặc quản lý, tôi muốn ghi nhận nhập hàng để cập nhật lượng nhiên liệu nhập vào. | Phiếu được tạo ở trạng thái chờ duyệt và chứa đủ dữ liệu cần thiết. |
| US08 | Là quản lý, tôi muốn phê duyệt hoặc từ chối phiếu nhập để kiểm soát việc cập nhật tồn. | Chỉ phiếu chờ duyệt được xử lý; duyệt hợp lệ mới cập nhật tồn. |
| US09 | Là nhân viên ca hoặc quản lý, tôi muốn ghi nhận bán hàng theo ngày để theo dõi lượng nhiên liệu đã bán. | Không cho phép số lượng bán âm hoặc vượt tồn. |

## 4. Tồn bồn và nhân sự

| Mã | User Story | Acceptance Criteria |
|---|---|---|
| US10 | Là quản lý hoặc nhân viên ca, tôi muốn theo dõi tồn bồn để kiểm soát lượng nhiên liệu. | Hiển thị được tồn đầu, nhập, bán và tồn cuối. |
| US11 | Là quản lý, tôi muốn quản lý nhân viên để duy trì thông tin nhân sự. | Có thể thêm, xem, sửa và cập nhật trạng thái nhân viên. |
| US12 | Là quản lý, tôi muốn quản lý ca làm việc để phân công nhân viên. | Có thể tạo ca, phân công nhân viên và cập nhật trạng thái. |
| US13 | Là nhân viên ca, tôi muốn xem ca được phân công để biết lịch làm việc của mình. | Chỉ hiển thị thông tin ca phù hợp với người dùng. |

## 5. Báo cáo và thống kê

| Mã | User Story | Acceptance Criteria |
|---|---|---|
| US14 | Là quản lý hoặc kế toán, tôi muốn tra cứu doanh thu để theo dõi kết quả bán hàng. | Doanh thu được tính từ dữ liệu bán hàng thực tế. |
| US15 | Là quản lý hoặc kế toán, tôi muốn tra cứu nhập - xuất - tồn để đối chiếu số liệu. | Hiển thị đúng dữ liệu nhập, bán và tồn theo điều kiện tra cứu. |
| US16 | Là quản lý hoặc kế toán, tôi muốn xem thống kê để đánh giá hoạt động của trạm. | Thống kê dựa trên dữ liệu thực tế và nhất quán với dữ liệu gốc. |

## 6. Tích hợp AI

| Mã | User Story | Acceptance Criteria |
|---|---|---|
| US17 | Là quản lý, tôi muốn AI sinh báo cáo để giảm thời gian tổng hợp dữ liệu. | Báo cáo dựa trên dữ liệu được cung cấp và không tự tạo số liệu. |
| US18 | Là quản lý, tôi muốn AI tóm tắt biến động tồn bồn để nhanh chóng nắm tình hình. | Kết quả phản ánh dữ liệu nhập, bán và tồn được cung cấp. |
| US19 | Là quản lý, tôi muốn AI cảnh báo số liệu bất thường để hỗ trợ kiểm tra dữ liệu. | AI chỉ đưa ra cảnh báo; người dùng quyết định hành động tiếp theo. |

## 7. Quy tắc chung

- Mỗi User Story phải truy vết được tới Use Case tương ứng.
- Acceptance Criteria phải kiểm thử được.
- Không thêm chức năng ngoài phạm vi hệ thống.
- AI chỉ đóng vai trò hỗ trợ, không thay thế quyết định nghiệp vụ.