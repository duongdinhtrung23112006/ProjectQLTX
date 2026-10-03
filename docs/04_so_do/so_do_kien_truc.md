# SƠ ĐỒ KIẾN TRÚC

## 1. Mục đích

Sơ đồ mô tả các thành phần chính của hệ thống, luồng dữ liệu giữa người dùng, giao diện, backend, cơ sở dữ liệu và AI.

## 2. Sơ đồ

```mermaid
flowchart TB
    U[Người dùng]

    UI[Giao diện Web<br/>HTML / Jinja / CSS / JavaScript]

    AUTH[Authentication<br/>Authorization]

    ROUTE[Flask Routes<br/>Blueprints]

    SERVICE[Business Services]

    DB[(MySQL<br/>tram_xang)]

    AI[AI Service]

    LLM[LLM]

    U --> UI
    UI --> AUTH
    AUTH --> ROUTE
    ROUTE --> SERVICE
    SERVICE --> DB

    SERVICE --> AI
    AI --> LLM
    LLM --> AI
    AI --> SERVICE
    SERVICE --> UI
3. Các thành phần
Thành phần	Vai trò
Người dùng	Quản lý, Nhân viên ca, Kế toán
Giao diện Web	Hiển thị và nhận thao tác
Authentication / Authorization	Xác thực và kiểm soát quyền
Flask Routes	Tiếp nhận và điều phối request
Business Services	Xử lý nghiệp vụ
MySQL	Lưu trữ dữ liệu
AI Service	Chuẩn bị dữ liệu, prompt và xử lý kết quả AI
LLM	Phân tích và sinh nội dung
4. Luồng dữ liệu chính
Luồng nghiệp vụ
Người dùng
→ Giao diện
→ Flask Route
→ Business Service
→ MySQL
→ Business Service
→ Giao diện
→ Người dùng
Luồng AI
Người dùng
→ Giao diện
→ Flask Route
→ Business Service
→ MySQL
→ AI Service
→ LLM
→ AI Service
→ Business Service
→ Giao diện
→ Người dùng
5. Nguyên tắc
Người dùng không truy cập trực tiếp MySQL.
Giao diện không trực tiếp xử lý logic nghiệp vụ phức tạp.
AI không trực tiếp thay đổi dữ liệu nghiệp vụ.
Business Service là lớp điều phối dữ liệu và nghiệp vụ.
Quyền truy cập phải được kiểm tra trước khi thực hiện chức năng.