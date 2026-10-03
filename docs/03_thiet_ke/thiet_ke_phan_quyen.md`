# THIẾT KẾ PHÂN QUYỀN

## 1. Mô hình

Hệ thống sử dụng mô hình phân quyền theo vai trò (RBAC).

```text
Người dùng
    ↓
Tài khoản
    ↓
Vai trò
    ↓
Quyền truy cập chức năng

Hệ thống có 3 vai trò:

Quản lý.
Nhân viên ca.
Kế toán.
2. Ma trận quyền
Chức năng	                       Quản lý   	  Nhân viên ca	     Kế toán
Đăng nhập	                         ✓	                               ✓	               ✓
Quản lý nhiên liệu	                 ✓		   
Xem nhiên liệu	                     ✓	              ✓	
Quản lý bồn chứa	                 ✓		
Xem bồn chứa	                     ✓	              ✓	
Ghi nhận nhập hàng	                 ✓	              ✓	
Phê duyệt / từ chối nhập hàng	     ✓		
Ghi nhận bán hàng	                 ✓	              ✓	
Theo dõi tồn bồn	                 ✓	              ✓	
Quản lý nhân viên	                 ✓		
Quản lý ca làm việc	                 ✓		
Xem ca làm việc                      ✓	              ✓	
Tra cứu doanh thu	                 ✓		                           ✓
Tra cứu nhập - xuất - tồn	         ✓		                           ✓
Thống kê hoạt động                   ✓	                               ✓
Sử dụng chức năng AI	             ✓		

3. Kiểm tra xác thực

Các chức năng yêu cầu đăng nhập phải kiểm tra session.

Nếu chưa đăng nhập:

Request
  ↓
Có session?
 ├── Không → Chuyển đến đăng nhập
 └── Có → Tiếp tục
4. Kiểm tra vai trò

Sau khi xác thực, hệ thống kiểm tra vai trò của tài khoản.

Request
  ↓
Xác thực
  ↓
Kiểm tra vai trò
  ↓
Có quyền?
 ├── Có → Cho phép xử lý
 └── Không → HTTP 403
5. Nguyên tắc phân quyền
Người dùng chỉ được truy cập chức năng thuộc vai trò.
Không được kiểm soát quyền chỉ bằng giao diện.
Backend phải kiểm tra quyền trước khi xử lý nghiệp vụ.
Không cho phép người dùng tự thay đổi vai trò bằng request.
Quyền truy cập phải được kiểm tra ở các thao tác đọc và thay đổi dữ liệu quan trọng.
6. Bảo vệ dữ liệu
Mật khẩu phải được lưu theo cơ chế bảo mật phù hợp.
Thông tin bí mật không được ghi trực tiếp vào source code.
Không trả về mật khẩu hoặc thông tin xác thực trong response.
Dữ liệu chỉ được cung cấp cho vai trò có quyền.
7. AI và phân quyền

AI không phải là một vai trò người dùng.

AI chỉ được thực hiện xử lý khi có request hợp lệ từ người dùng có quyền.

Người dùng có quyền
        ↓
    AI Service
        ↓
Phân tích dữ liệu
        ↓
Kết quả hỗ trợ

AI không được tự cấp quyền, thay đổi quyền hoặc thực hiện nghiệp vụ ngoài phạm vi được phép.