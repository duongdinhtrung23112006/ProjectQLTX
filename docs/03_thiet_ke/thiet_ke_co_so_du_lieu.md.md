# THIẾT KẾ CƠ SỞ DỮ LIỆU

## 1. Tổng quan

Hệ thống sử dụng MySQL để lưu trữ dữ liệu nghiệp vụ của trạm xăng.

Cơ sở dữ liệu phải đảm bảo:

- Tính toàn vẹn dữ liệu.
- Quan hệ giữa các thực thể rõ ràng.
- Không tạo dữ liệu tham chiếu không tồn tại.
- Kiểm soát số lượng tồn bồn.
- Hỗ trợ truy vấn, thống kê và báo cáo.

## 2. Các bảng chính

```text
nhien_lieu
    │
    └──< bon_chua

nhan_vien
    ├──< tai_khoan
    ├──< ca_lam_viec
    └──< nhap_hang

bon_chua
    └──< nhap_hang

nhien_lieu
    └──< nhap_hang

Các bảng nghiệp vụ bán hàng và các bảng phục vụ thống kê/AI sẽ được bổ sung theo thiết kế và phạm vi triển khai thực tế.

3. Bảng nhiên liệu

nhien_lieu lưu danh mục các loại nhiên liệu.

Khóa chính:

nhien_lieu.id

Mã nhiên liệu là duy nhất.

4. Bảng bồn chứa

bon_chua lưu thông tin các bồn chứa.

Quan hệ:

nhien_lieu.id 1 ───── N bon_chua.nhien_lieu_id

Mỗi bồn phải tham chiếu đến một nhiên liệu tồn tại.

Các dữ liệu quan trọng:

Sức chứa.
Tồn hiện tại.
Trạng thái.
5. Bảng nhân viên

nhan_vien lưu thông tin nhân viên làm việc tại trạm.

Khóa chính:

nhan_vien.id

Mã nhân viên là duy nhất.

6. Bảng tài khoản

tai_khoan lưu thông tin đăng nhập và vai trò.

Quan hệ:

nhan_vien.id 1 ───── 1 tai_khoan.nhan_vien_id

Mỗi nhân viên chỉ được liên kết với một tài khoản.

7. Bảng ca làm việc

ca_lam_viec lưu thông tin phân công nhân viên theo ngày.

Quan hệ:

nhan_vien.id 1 ───── N ca_lam_viec.nhan_vien_id

Ca làm việc được quản lý độc lập với dữ liệu bán hàng theo ngày.

8. Bảng nhập hàng

nhap_hang lưu các phiếu nhập nhiên liệu vào bồn.

Quan hệ:

nhien_lieu.id 1 ───── N nhap_hang.nhien_lieu_id
bon_chua.id   1 ───── N nhap_hang.bon_id
nhan_vien.id  1 ───── N nhap_hang.nhan_vien_id

Phiếu nhập có trạng thái để kiểm soát quá trình chờ duyệt, duyệt hoặc từ chối.

Chỉ phiếu được phê duyệt mới làm thay đổi tồn bồn.

9. Dữ liệu bán hàng

Dữ liệu bán hàng được thiết kế theo ngày, không bắt buộc ghi nhận từng giao dịch hoặc từng ca.

Thông tin nghiệp vụ dự kiến gồm:

Ngày bán.
Nhân viên lập.
Nhiên liệu.
Bồn chứa.
Số lượng bán.
Đơn giá.
Thành tiền.

Dữ liệu bán hàng phải liên kết được với nhiên liệu và bồn chứa tương ứng.

10. Tính toàn vẹn dữ liệu
Khóa chính phải duy nhất.
Khóa ngoại phải tham chiếu bản ghi tồn tại.
Mã nghiệp vụ cần duy nhất khi được quy định.
Không cho phép tồn bồn âm.
Không cho phép tồn vượt sức chứa.
Cập nhật tồn khi duyệt nhập phải thực hiện trong transaction.
Các nghiệp vụ liên quan đến tồn phải đảm bảo dữ liệu nhất quán.
11. Nguyên tắc cập nhật

Dữ liệu gốc được lưu tại MySQL.

Các chức năng thống kê và AI lấy dữ liệu từ cơ sở dữ liệu thay vì tự tạo dữ liệu mới.

AI không được trực tiếp sửa dữ liệu trong các bảng nghiệp vụ.