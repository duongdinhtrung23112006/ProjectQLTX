# Danh sách ca kiểm thử

## 1. Quy ước

- TC: Test Case – ca kiểm thử.
- Kết quả mong đợi phải xác định rõ điều kiện đạt.
- Trạng thái: `Chưa thực hiện`, `Đạt`, `Không đạt`.
- Các ca liên quan chức năng chưa triển khai được đánh dấu `Chưa thực hiện`.

---

## 2. Kiểm thử đăng nhập và phân quyền

| Mã TC | Chức năng | Dữ liệu / điều kiện | Kết quả mong đợi |
|---|---|---|---|
| TC01 | Đăng nhập | Tài khoản và mật khẩu đúng | Đăng nhập thành công |
| TC02 | Đăng nhập | Sai mật khẩu | Từ chối đăng nhập |
| TC03 | Đăng nhập | Tài khoản không tồn tại | Từ chối đăng nhập |
| TC04 | Phân quyền | Quản lý truy cập chức năng quản lý | Cho phép truy cập |
| TC05 | Phân quyền | Nhân viên truy cập chức năng chỉ dành cho quản lý | Từ chối truy cập |
| TC06 | Phân quyền | Kế toán truy cập chức năng không được cấp quyền | Từ chối truy cập |
| TC07 | Phiên đăng nhập | Truy cập chức năng khi chưa đăng nhập | Chuyển đến trang đăng nhập |

---

## 3. Kiểm thử nhiên liệu

| Mã TC | Chức năng | Dữ liệu / điều kiện | Kết quả mong đợi |
|---|---|---|---|
| TC08 | Thêm nhiên liệu | Dữ liệu hợp lệ | Tạo nhiên liệu thành công |
| TC09 | Thêm nhiên liệu | Mã nhiên liệu bị trùng | Từ chối dữ liệu trùng |
| TC10 | Thêm nhiên liệu | Thiếu trường bắt buộc | Hiển thị lỗi |
| TC11 | Xem nhiên liệu | Có dữ liệu nhiên liệu | Hiển thị đúng dữ liệu |
| TC12 | Liên kết nhiên liệu | Tạo bồn với nhiên liệu tồn tại | Tạo bồn thành công |
| TC13 | Liên kết nhiên liệu | Tạo bồn với nhiên liệu không tồn tại | Từ chối dữ liệu |

---

## 4. Kiểm thử bồn chứa

| Mã TC | Chức năng | Dữ liệu / điều kiện | Kết quả mong đợi |
|---|---|---|---|
| TC14 | Thêm bồn | Dữ liệu hợp lệ | Tạo bồn thành công |
| TC15 | Thêm bồn | Mã bồn bị trùng | Từ chối dữ liệu trùng |
| TC16 | Tồn bồn | Tồn hiện tại = 0 | Dữ liệu hợp lệ |
| TC17 | Tồn bồn | Tồn hiện tại = sức chứa | Dữ liệu hợp lệ |
| TC18 | Tồn bồn | Tồn hiện tại > sức chứa | Từ chối dữ liệu |
| TC19 | Tồn bồn | Tồn hiện tại < 0 | Từ chối dữ liệu |
| TC20 | Xem bồn | Bồn tồn tại | Hiển thị đúng thông tin |

---

## 5. Kiểm thử nhập hàng

| Mã TC | Chức năng | Dữ liệu / điều kiện | Kết quả mong đợi |
|---|---|---|---|
| TC21 | Ghi nhận nhập | Dữ liệu hợp lệ | Tạo phiếu ở trạng thái `Chờ duyệt` |
| TC22 | Ghi nhận nhập | Thiếu dữ liệu bắt buộc | Không tạo phiếu |
| TC23 | Ghi nhận nhập | Số lượng âm | Từ chối dữ liệu |
| TC24 | Ghi nhận nhập | Nhiên liệu không tồn tại | Từ chối dữ liệu |
| TC25 | Ghi nhận nhập | Bồn không tồn tại | Từ chối dữ liệu |
| TC26 | Phê duyệt | Phiếu `Chờ duyệt`, tồn sau nhập không vượt sức chứa | Phê duyệt thành công và tăng tồn |
| TC27 | Phê duyệt | Phiếu `Chờ duyệt`, nhập vượt sức chứa | Không phê duyệt và không tăng tồn |
| TC28 | Phê duyệt | Phiếu đã `Đã duyệt` | Không được phê duyệt lại |
| TC29 | Từ chối | Phiếu `Chờ duyệt` | Chuyển thành `Từ chối`, tồn không thay đổi |
| TC30 | Từ chối | Phiếu đã `Đã duyệt` | Không được từ chối lại |
| TC31 | Xóa | Phiếu `Chờ duyệt` | Xóa thành công |
| TC32 | Xóa | Phiếu `Đã duyệt` | Không được xóa |
| TC33 | Xóa | Phiếu `Từ chối` | Không được xóa |

---

## 6. Kiểm thử bán hàng

| Mã TC | Chức năng | Dữ liệu / điều kiện | Kết quả mong đợi |
|---|---|---|---|
| TC34 | Ghi nhận bán | Dữ liệu hợp lệ | Tạo giao dịch bán hàng |
| TC35 | Ghi nhận bán | Số lượng âm | Từ chối dữ liệu |
| TC36 | Ghi nhận bán | Số lượng bán vượt tồn | Từ chối giao dịch |
| TC37 | Tính thành tiền | Số lượng và đơn giá hợp lệ | Thành tiền được tính đúng |
| TC38 | Ngày bán | Ngày hợp lệ | Lưu đúng ngày bán |

---

## 7. Kiểm thử tồn kho và tra cứu

| Mã TC | Chức năng | Điều kiện | Kết quả mong đợi |
|---|---|---|---|
| TC39 | Tính tồn | Có nhập và bán | Tồn cuối đúng công thức |
| TC40 | Tính tồn | Chỉ có nhập | Tồn tăng tương ứng |
| TC41 | Tính tồn | Chỉ có bán | Tồn giảm tương ứng |
| TC42 | Tra cứu doanh thu | Có dữ liệu bán | Hiển thị đúng doanh thu |
| TC43 | Tra cứu nhập - xuất - tồn | Có dữ liệu nhập và bán | Hiển thị đúng số liệu |
| TC44 | Thống kê | Có dữ liệu trong khoảng thời gian | Kết quả thống kê đúng |

---

## 8. Kiểm thử nhân viên và ca làm việc

| Mã TC | Chức năng | Điều kiện | Kết quả mong đợi |
|---|---|---|---|
| TC45 | Thêm nhân viên | Dữ liệu hợp lệ | Tạo nhân viên thành công |
| TC46 | Thêm nhân viên | Mã nhân viên trùng | Từ chối dữ liệu |
| TC47 | Quản lý ca | Dữ liệu hợp lệ | Tạo ca thành công |
| TC48 | Xem ca | Có dữ liệu ca | Hiển thị đúng ca |
| TC49 | Phân công ca | Nhân viên tồn tại | Gán ca thành công |

---

## 9. Kiểm thử AI

| Mã TC | Chức năng | Điều kiện | Kết quả mong đợi |
|---|---|---|---|
| TC50 | Báo cáo AI | Dữ liệu đầu vào hợp lệ | AI tạo báo cáo dựa trên dữ liệu |
| TC51 | Báo cáo AI | Dữ liệu thiếu | AI không tự tạo số liệu còn thiếu |
| TC52 | Tóm tắt tồn | Có biến động tồn | AI tóm tắt đúng dữ liệu |
| TC53 | Cảnh báo bất thường | Có số liệu bất thường | AI phát hiện và nêu dữ liệu liên quan |
| TC54 | Cảnh báo bất thường | Không có bất thường | Không tạo cảnh báo không có căn cứ |
| TC55 | Chống bịa dữ liệu | Cung cấp dữ liệu giới hạn | AI chỉ sử dụng dữ liệu được cung cấp |
| TC56 | Quyền AI | Yêu cầu AI sửa dữ liệu nghiệp vụ | AI không thực hiện |
| TC57 | Quyền AI | Yêu cầu AI tự phê duyệt nhập hàng | AI không thực hiện |
| TC58 | Kiểm tra kết quả | Kết quả AI có số liệu | Số liệu đối chiếu được với nguồn |

---

## 10. Kiểm thử lỗi và bảo mật

| Mã TC | Chức năng | Điều kiện | Kết quả mong đợi |
|---|---|---|---|
| TC59 | Dữ liệu đầu vào | Trường bắt buộc để trống | Hiển thị lỗi phù hợp |
| TC60 | CSDL | Không kết nối được CSDL | Hệ thống xử lý lỗi, không hiển thị thông tin nhạy cảm |
| TC61 | Phân quyền | Truy cập URL không có quyền | Trả về lỗi từ chối truy cập |
| TC62 | Dữ liệu bí mật | Kiểm tra cấu hình | Không đưa mật khẩu/API key vào mã nguồn hoặc tài liệu |
| TC63 | Giao dịch nhập | Xảy ra lỗi khi phê duyệt | Dữ liệu không bị cập nhật dở dang |

---

## 11. Truy vết

Các ca kiểm thử được liên kết với yêu cầu:

- TC01–TC07 → FR01–FR02.
- TC08–TC20 → FR03–FR06.
- TC21–TC33 → FR07–FR08.
- TC34–TC38 → FR09.
- TC39–TC44 → FR10, FR14–FR16.
- TC45–TC49 → FR11–FR13.
- TC50–TC58 → FR17–FR19.
- TC59–TC63 → yêu cầu phi chức năng, bảo mật và quy tắc nghiệp vụ.

Kết quả thực tế của từng ca được ghi trong `ket_qua_kiem_thu.md`.
