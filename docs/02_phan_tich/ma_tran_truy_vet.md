# MA TRẬN TRUY VẾT

## 1. Mục tiêu → Yêu cầu → Use Case → User Story

| Mục tiêu | Yêu cầu | Use Case | User Story |
|---|---|---|---|
| Quản lý người dùng an toàn | FR01, FR02, NFR01 | UC01, UC02 | US01, US02 |
| Quản lý nhiên liệu | FR03, FR04 | UC05, UC06 | US05, US06 |
| Quản lý bồn chứa | FR05, FR06, NFR02 | UC03, UC04 | US03, US04 |
| Quản lý nhập hàng | FR07, FR08, NFR02 | UC07, UC08 | US07, US08 |
| Quản lý bán hàng | FR09, NFR02 | UC09 | US09 |
| Kiểm soát tồn bồn | FR10, NFR02 | UC10 | US10 |
| Quản lý nhân sự | FR11 | UC11 | US11 |
| Quản lý ca làm việc | FR12, FR13 | UC12, UC13 | US12, US13 |
| Theo dõi doanh thu | FR14 | UC14 | US14 |
| Theo dõi nhập - xuất - tồn | FR15 | UC15 | US15 |
| Thống kê hoạt động | FR16 | UC16 | US16 |
| Hỗ trợ phân tích bằng AI | FR17, FR18, FR19, NFR06, NFR07 | UC17, UC18, UC19 | US17, US18, US19 |

## 2. Truy vết yêu cầu chức năng

| Yêu cầu | Use Case | User Story |
|---|---|---|
| FR01 | UC01 | US01 |
| FR02 | UC02 | US02 |
| FR03 | UC05 | US05 |
| FR04 | UC06 | US06 |
| FR05 | UC03 | US03 |
| FR06 | UC04 | US04 |
| FR07 | UC07 | US07 |
| FR08 | UC08 | US08 |
| FR09 | UC09 | US09 |
| FR10 | UC10 | US10 |
| FR11 | UC11 | US11 |
| FR12 | UC12 | US12 |
| FR13 | UC13 | US13 |
| FR14 | UC14 | US14 |
| FR15 | UC15 | US15 |
| FR16 | UC16 | US16 |
| FR17 | UC17 | US17 |
| FR18 | UC18 | US18 |
| FR19 | UC19 | US19 |

## 3. Truy vết yêu cầu phi chức năng

| Yêu cầu | Thành phần liên quan |
|---|---|
| NFR01 | Đăng nhập, phân quyền, bảo mật |
| NFR02 | Cơ sở dữ liệu, nhập hàng, bán hàng, tồn bồn |
| NFR03 | Kiểm thử chức năng và phân quyền |
| NFR04 | Kiến trúc code và bảo trì |
| NFR05 | Cấu hình và triển khai |
| NFR06 | Các chức năng AI |
| NFR07 | Prompt, dữ liệu đầu vào và kết quả AI |
| NFR08 | Logging, monitoring, AI usage log |

## 4. Nguyên tắc truy vết

Mỗi yêu cầu chức năng phải có ít nhất một Use Case và User Story tương ứng.

Khi thay đổi một yêu cầu, cần kiểm tra và cập nhật các thành phần liên quan:

```text
Mục tiêu
   ↓
Yêu cầu
   ↓
Use Case
   ↓
User Story
   ↓
Thiết kế
   ↓
Code
   ↓
Kiểm thử

Không tự ý thêm hoặc loại bỏ chức năng mà không cập nhật tài liệu truy vết.