# Prompt tạo hình minh họa

## 1. Mục đích

Xác định các hình minh họa cần sử dụng trong báo cáo và mô tả nội dung của từng hình dựa trên tài liệu nguồn và hệ thống thực tế.

## 2. Context

Đọc:

- `bao_cao/cau_truc_bao_cao.md`
- `bao_cao/quy_dinh_trinh_bay.md`
- Các tài liệu trong `docs/04_so_do/`
- Các tài liệu trong `docs/03_thiet_ke/`
- Các tài liệu trong `docs/05_kiem_thu/`
- Các tài liệu trong `docs/08_trang_thai/`

Khi hình minh họa liên quan đến giao diện hoặc chức năng đã triển khai, kiểm tra thêm mã nguồn và giao diện thực tế.

## 3. Nhiệm vụ

- Xác định hình cần đưa vào từng chương.
- Xác định mục đích của từng hình.
- Xác định nguồn tạo hình.
- Mô tả các thành phần cần xuất hiện trong hình.
- Xác định vị trí hình trong báo cáo.
- Đặt tên và đánh số hình nhất quán.
- Đảm bảo hình hỗ trợ trực tiếp cho nội dung được trình bày.

Các nhóm hình có thể gồm:

- Hình kiến trúc hệ thống.
- Hình Use Case.
- Hình lớp.
- Hình cơ sở dữ liệu.
- Hình trình tự.
- Hình quy trình nghiệp vụ.
- Hình tích hợp AI.
- Hình giao diện hệ thống.
- Hình kết quả kiểm thử.
- Hình triển khai và vận hành.

## 4. Ràng buộc

- Không tự tạo thành phần không có trong tài liệu hoặc hệ thống.
- Không đưa chức năng chưa thực hiện vào hình như một chức năng đã hoàn thành.
- Không thay đổi quan hệ giữa các thành phần để làm hình dễ nhìn hơn.
- Tên thành phần phải thống nhất với tài liệu và mã nguồn.
- Không sử dụng dữ liệu giả làm dữ liệu thực tế.
- Nếu thiếu thông tin, ghi rõ phần cần bổ sung.

## 5. Output

Với mỗi hình, cung cấp:

- Mã hình.
- Tên hình.
- Chương/Mục sử dụng.
- Mục đích.
- Nguồn dữ liệu.
- Các thành phần cần thể hiện.
- Quan hệ hoặc luồng cần thể hiện.
- Ghi chú nếu có.
- Vị trí lưu file dự kiến.

Định dạng:

`Hình → Vị trí → Mục đích → Nguồn → Thành phần → Quan hệ → File`

## 6. Kiểm tra

Kiểm tra:

- Hình có phục vụ nội dung báo cáo.
- Tên và số thứ tự không trùng.
- Thành phần trong hình khớp với tài liệu nguồn.
- Hình không chứa thông tin chưa được xác nhận.
- Nội dung hình và phần mô tả trong báo cáo nhất quán.