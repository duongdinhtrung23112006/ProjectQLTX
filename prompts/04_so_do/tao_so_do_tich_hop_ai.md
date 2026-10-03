# Prompt tạo sơ đồ tích hợp AI

## 1. Mục đích

Tạo đặc tả sơ đồ mô tả cách hệ thống trao đổi dữ liệu với thành phần AI và cách kết quả AI được đưa về cho người dùng.

## 2. Context

Đọc:

- `docs/03_thiet_ke/thiet_ke_ai.md`
- `docs/03_thiet_ke/kien_truc_he_thong.md`
- `docs/07_ai/chien_luoc_su_dung_ai.md`
- `docs/07_ai/an_toan_ai.md`
- Mã nguồn liên quan đến AI nếu đã có.

## 3. Nhiệm vụ

AI Agent phải xác định:

1. Người dùng khởi tạo chức năng AI.
2. Dữ liệu nguồn được lấy từ hệ thống.
3. Thành phần chuẩn bị dữ liệu và prompt.
4. API hoặc thành phần kết nối AI.
5. Dữ liệu được gửi đến AI.
6. Kết quả AI trả về.
7. Bước kiểm tra và xử lý kết quả.
8. Kết quả được hiển thị cho người dùng.

Phải mô tả riêng ba chức năng:

- Sinh báo cáo.
- Tóm tắt biến động tồn bồn.
- Cảnh báo số liệu bất thường.

## 4. Ràng buộc

- AI chỉ phân tích dữ liệu do hệ thống cung cấp.
- Không cho AI tự thay đổi dữ liệu nghiệp vụ.
- Không cho AI tự phê duyệt hoặc từ chối giao dịch.
- Không coi kết quả AI là dữ liệu gốc.
- Phải có bước kiểm tra kết quả trước khi sử dụng.
- Không tự thêm mô hình, API hoặc dịch vụ AI chưa được xác định.
- Không đưa API key hoặc thông tin bí mật vào tài liệu.

## 5. Output

### Thành phần

| Thành phần | Vai trò |
|---|---|
| Người dùng | |
| Web UI | |
| Backend | |
| Database | |
| AI Service | |
| AI Model | |

### Luồng dữ liệu

Mô tả dữ liệu đi từ hệ thống đến AI, kết quả AI quay lại hệ thống và được hiển thị cho người dùng.

### Kiểm soát AI

Mô tả các bước kiểm tra dữ liệu đầu vào, kết quả đầu ra và quyền quyết định của người dùng.

### Đặc tả sơ đồ

Mô tả các thành phần, kết nối và hướng dữ liệu cần thể hiện.

### Truy vết

`Chức năng AI → Dữ liệu nguồn → Backend → AI → Kết quả → Người dùng`