# Prompt tạo bảng biểu

## 1. Mục đích

Xác định và tạo nội dung cho các bảng biểu cần sử dụng trong báo cáo dựa trên tài liệu nguồn và dữ liệu thực tế của hệ thống.

## 2. Context

Đọc:

- `bao_cao/cau_truc_bao_cao.md`
- `bao_cao/quy_dinh_trinh_bay.md`
- Các tài liệu trong `docs/01_tong_quan/`
- Các tài liệu trong `docs/02_phan_tich/`
- Các tài liệu trong `docs/03_thiet_ke/`
- `docs/05_kiem_thu/`
- `docs/08_trang_thai/`

Khi bảng liên quan đến chức năng hoặc dữ liệu đã triển khai, kiểm tra thêm mã nguồn và cơ sở dữ liệu.

## 3. Nhiệm vụ

- Xác định các bảng cần có trong từng chương.
- Xác định mục đích của từng bảng.
- Xác định nguồn dữ liệu của bảng.
- Tạo cấu trúc cột và nội dung bảng phù hợp.
- Đánh số và đặt tên bảng nhất quán.
- Kiểm tra sự liên kết giữa bảng và nội dung báo cáo.

Các nhóm bảng có thể gồm:

- Bảng vai trò và quyền.
- Bảng yêu cầu chức năng.
- Bảng yêu cầu phi chức năng.
- Bảng Use Case.
- Bảng User Story.
- Bảng ma trận truy vết.
- Bảng dữ liệu và thuộc tính.
- Bảng API.
- Bảng phân quyền.
- Bảng ca kiểm thử và kết quả kiểm thử.
- Bảng trạng thái chức năng.
- Bảng lỗi và nợ kỹ thuật.
- Các bảng khác nếu cấu trúc báo cáo yêu cầu.

## 4. Ràng buộc

- Không tự tạo số liệu hoặc dữ liệu thực tế.
- Không đưa chức năng chưa tồn tại vào bảng hoàn thành.
- Không tạo bảng trùng nội dung nếu có thể tái sử dụng bảng hiện có.
- Tên bảng phải thống nhất với nội dung báo cáo.
- Dữ liệu phải truy vết được về tài liệu nguồn hoặc hệ thống.
- Nếu thiếu dữ liệu, đánh dấu cần bổ sung thay vì tự suy đoán.

## 5. Output

Với mỗi bảng, cung cấp:

- Mã bảng.
- Tên bảng.
- Vị trí trong báo cáo.
- Mục đích.
- Nguồn dữ liệu.
- Danh sách cột.
- Nội dung cần điền.
- Thành phần liên quan để truy vết.

Định dạng:

`Bảng → Chương/Mục → Nguồn dữ liệu → Nội dung → Truy vết`

## 6. Kiểm tra

Kiểm tra:

- Tên bảng không trùng.
- Số thứ tự không bị thiếu.
- Cột và dữ liệu phù hợp với mục đích.
- Nội dung bảng nhất quán với phần văn bản.
- Không có dữ liệu được AI tự bịa.