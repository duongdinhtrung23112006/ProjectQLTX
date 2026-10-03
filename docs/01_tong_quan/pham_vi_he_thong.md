# Mô tả phạm vi hệ thống

> **Tên hệ thống:** Hệ thống quản lý trạm xăng có tích hợp AI
> **Mã dự án:** ProjectQLTX
> **Loại tài liệu:** System Scope / Scope Prompt
> **Mục đích:** Xác định phạm vi nghiệp vụ và giới hạn của hệ thống để AI Agent sử dụng làm nguồn tham chiếu khi phân tích, thiết kế, lập trình, kiểm thử và tạo tài liệu.

---

# 1. MỤC ĐÍCH

Tài liệu này xác định phạm vi của **Hệ thống quản lý trạm xăng có tích hợp AI**.

Phạm vi được sử dụng làm căn cứ để:

* Xác định các chức năng cần phát triển.
* Xác định các chức năng không thuộc hệ thống.
* Kiểm soát phạm vi khi phát triển.
* Phân tích yêu cầu.
* Thiết kế cơ sở dữ liệu.
* Thiết kế kiến trúc hệ thống.
* Xây dựng Use Case.
* Xây dựng kiểm thử.
* Tích hợp AI.
* Xây dựng tài liệu và báo cáo.

## Quy tắc đối với AI Agent

AI Agent phải sử dụng tài liệu này để kiểm tra xem một yêu cầu mới có nằm trong phạm vi hệ thống hay không.

Nếu yêu cầu mới không được xác định trong tài liệu này, AI Agent **không được tự động coi yêu cầu đó là yêu cầu chính thức**.

---

# 2. PHẠM VI TỔNG QUÁT

Hệ thống tập trung vào việc **quản lý và phân tích dữ liệu hoạt động của một trạm xăng**.

Các nhóm nghiệp vụ chính bao gồm:

1. Đăng nhập và phân quyền.
2. Quản lý mặt hàng nhiên liệu.
3. Quản lý bồn chứa.
4. Quản lý nhập hàng.
5. Quản lý bán hàng.
6. Theo dõi tồn bồn.
7. Quản lý nhân viên.
8. Quản lý ca làm việc.
9. Tra cứu doanh thu và số liệu nhập - xuất - tồn.
10. Thống kê hoạt động.
11. Tích hợp AI để hỗ trợ tổng hợp và phân tích dữ liệu.

---

# 3. ĐỐI TƯỢNG SỬ DỤNG

Hệ thống phục vụ ba nhóm người dùng chính:

* Quản lý
* Nhân viên ca
* Kế toán

---

## 3.1. Quản lý

Quản lý sử dụng hệ thống để:

* Quản lý nhiên liệu.
* Quản lý bồn chứa.
* Quản lý nhân viên.
* Quản lý ca làm việc.
* Theo dõi nhập hàng.
* Phê duyệt hoặc từ chối nhập hàng.
* Theo dõi bán hàng.
* Theo dõi tồn bồn.
* Tra cứu doanh thu.
* Xem thống kê.
* Sử dụng các chức năng AI.

---

## 3.2. Nhân viên ca

Nhân viên ca sử dụng hệ thống để:

* Đăng nhập.
* Xem thông tin bồn chứa.
* Xem thông tin nhiên liệu.
* Thực hiện các nghiệp vụ được phân quyền.
* Ghi nhận hoạt động nhập hàng.
* Ghi nhận hoạt động bán hàng.
* Theo dõi dữ liệu liên quan đến công việc.
* Xem thông tin ca làm việc của mình.

---

## 3.3. Kế toán

Kế toán sử dụng hệ thống chủ yếu để:

* Tra cứu doanh thu.
* Tra cứu số liệu nhập.
* Tra cứu số liệu bán.
* Tra cứu tồn bồn.
* Xem thống kê.
* Đối chiếu các số liệu phục vụ công tác kế toán.

---

# 4. PHẠM VI CHỨC NĂNG

## 4.1. Đăng nhập và phân quyền

Hệ thống bao gồm:

* Đăng nhập.
* Kiểm tra thông tin tài khoản.
* Xác định vai trò.
* Quản lý phiên đăng nhập.
* Kiểm soát quyền truy cập.

### Các vai trò

* Quản lý.
* Nhân viên ca.
* Kế toán.

---

## 4.2. Quản lý mặt hàng nhiên liệu

Hệ thống cho phép quản lý:

* Mã nhiên liệu.
* Tên nhiên liệu.
* Đơn vị.
* Đơn giá.
* Trạng thái.

### Các thao tác chính

* Thêm.
* Xem.
* Chỉnh sửa.
* Cập nhật trạng thái.

---

## 4.3. Quản lý bồn chứa

Hệ thống cho phép quản lý:

* Mã bồn.
* Tên bồn.
* Nhiên liệu được chứa.
* Sức chứa.
* Tồn hiện tại.
* Trạng thái.

### Quy tắc dữ liệu

Mỗi bồn phải tham chiếu đến **một mặt hàng nhiên liệu đã tồn tại trong hệ thống**.

Không sử dụng tên nhiên liệu nhập tự do để thay thế quan hệ dữ liệu giữa bồn và nhiên liệu.

Quan hệ dữ liệu phải được thể hiện rõ ràng trong thiết kế cơ sở dữ liệu.

---

## 4.4. Quản lý nhập hàng

Hệ thống hỗ trợ:

* Tạo phiếu nhập.
* Xem phiếu nhập.
* Theo dõi trạng thái phiếu.
* Phê duyệt phiếu nhập.
* Từ chối phiếu nhập.
* Xóa phiếu nhập khi thỏa mãn điều kiện nghiệp vụ.
* Lưu lịch sử phiếu đã xử lý.

### Quy tắc nghiệp vụ

Khi phiếu nhập được phê duyệt, hệ thống phải:

1. Kiểm tra sức chứa của bồn.
2. Kiểm tra điều kiện cập nhật tồn.
3. Chỉ cập nhật tồn khi nghiệp vụ hợp lệ.

Không được để việc phê duyệt phiếu nhập làm cho tồn bồn vượt quá sức chứa.

---

## 4.5. Quản lý bán hàng

Hệ thống hỗ trợ ghi nhận **lượng nhiên liệu bán ra theo ngày**.

Thông tin bán hàng tối thiểu gồm:

* Ngày bán.
* Nhân viên thực hiện.
* Nhiên liệu.
* Bồn chứa.
* Số lượng bán.
* Đơn giá.
* Thành tiền.

Dữ liệu bán hàng được sử dụng cho:

* Tính doanh thu.
* Tính sản lượng bán.
* Theo dõi tồn bồn.
* Thống kê.
* Phân tích AI.

### Quy tắc quan trọng

Mô hình hiện tại **không mặc định yêu cầu ghi nhận doanh số thành từng giao dịch khách hàng**.

Mô hình hiện tại cũng **không mặc định yêu cầu ghi nhận doanh số theo từng ca**.

---

## 4.6. Theo dõi tồn bồn

Hệ thống hỗ trợ theo dõi:

* Tồn đầu.
* Tổng nhập.
* Tổng bán.
* Tồn cuối.
* Chênh lệch tồn khi có dữ liệu đối chiếu.

### Công thức

```text
Tồn cuối = Tồn đầu + Tổng nhập - Tổng bán
```

### Ràng buộc

Hệ thống không được để tồn bồn:

```text
Tồn bồn > Sức chứa
```

hoặc:

```text
Tồn bồn < 0
```

Các quy tắc trên phải được kiểm tra trong logic nghiệp vụ và/hoặc các ràng buộc phù hợp của hệ thống.

---

## 4.7. Quản lý nhân viên

Hệ thống quản lý:

* Mã nhân viên.
* Họ tên.
* Số điện thoại.
* Địa chỉ.
* Chức vụ.
* Ngày vào làm.
* Trạng thái.

### Các thao tác chính

* Thêm.
* Xem.
* Chỉnh sửa.
* Cập nhật trạng thái.

---

## 4.8. Quản lý ca làm việc

Hệ thống quản lý:

* Mã ca.
* Tên ca.
* Ngày làm việc.
* Nhân viên được phân công.
* Trạng thái ca.

Chức năng ca làm việc phục vụ việc:

* Quản lý ca.
* Phân công nhân viên.
* Xác định nhân viên thực hiện công việc.

### Quy tắc quan trọng

**Quản lý ca làm việc không đồng nghĩa với việc bắt buộc phải ghi nhận doanh số theo từng ca.**

Cụ thể:

```text
Ca làm việc
    ≠
Doanh số theo ca
```

Hệ thống hiện tại quản lý ca làm việc nhưng dữ liệu bán hàng được xác định theo **ngày**.

Không tự ý tạo nghiệp vụ:

```text
Doanh số ca 1
Doanh số ca 2
Doanh số ca 3
```

nếu chưa có yêu cầu chính thức.

---

## 4.9. Tra cứu và thống kê

Hệ thống hỗ trợ tra cứu:

* Doanh thu.
* Lượng nhập.
* Lượng bán.
* Tồn bồn.
* Sản lượng bán.
* Chênh lệch tồn.

Có thể tra cứu theo các tiêu chí phù hợp với dữ liệu hệ thống, chẳng hạn:

* Thời gian.
* Nhiên liệu.
* Bồn chứa.

Các bộ lọc cụ thể chỉ được triển khai khi phù hợp với thiết kế và yêu cầu đã được xác định.

---

# 5. PHẠM VI TÍCH HỢP AI

AI được tích hợp như một **thành phần hỗ trợ tổng hợp và phân tích dữ liệu**.

AI không thay thế các nghiệp vụ quản lý cốt lõi của hệ thống.

---

## 5.1. Sinh báo cáo

AI có thể sử dụng dữ liệu nghiệp vụ được hệ thống cung cấp để tạo báo cáo tổng hợp.

Nguồn dữ liệu có thể bao gồm:

* Bán hàng.
* Nhập hàng.
* Tồn bồn.
* Doanh thu.
* Sản lượng bán.
* Chênh lệch tồn.

### Quy tắc

AI không được tự tạo số liệu nghiệp vụ.

Mọi số liệu được AI sử dụng phải có nguồn từ dữ liệu mà hệ thống cung cấp.

---

## 5.2. Tóm tắt biến động tồn bồn

AI hỗ trợ:

* Tóm tắt biến động.
* So sánh các giá trị được cung cấp.
* Chỉ ra thay đổi đáng chú ý.
* Đề xuất nội dung cần kiểm tra.

AI không được tự xác định nguyên nhân nếu dữ liệu không đủ để chứng minh nguyên nhân đó.

Ví dụ:

```text
Dữ liệu:
Tồn bồn giảm mạnh trong ngày X.

AI có thể:
→ Phát hiện mức giảm.
→ Tóm tắt mức giảm.
→ Đề xuất kiểm tra dữ liệu bán hàng.

AI không được tự kết luận:
→ "Nguyên nhân chắc chắn là thất thoát nhiên liệu."

nếu dữ liệu không đủ chứng minh kết luận đó.
```

---

## 5.3. Cảnh báo số liệu bất thường

AI hỗ trợ phát hiện các trường hợp có dấu hiệu cần kiểm tra.

Ví dụ:

* Lượng bán thay đổi bất thường.
* Tồn bồn có biến động lớn.
* Chênh lệch giữa số liệu tính toán và số liệu đối chiếu.

### Nguyên tắc

Đây là **cảnh báo hỗ trợ kiểm tra**, không phải quyết định nghiệp vụ tự động.

AI không được tự động thực hiện hành động nghiệp vụ chỉ dựa trên cảnh báo.

---

# 6. DỮ LIỆU THUỘC PHẠM VI

Các nhóm dữ liệu chính thuộc hệ thống:

```text
Tài khoản
    │
    └── Nhân viên
            │
            └── Ca làm việc


Nhiên liệu
    │
    └── Bồn chứa


Nhân viên
    │
    ├── Nhập hàng
    │
    └── Bán hàng


Nhập hàng
    │
    └── Tồn bồn


Bán hàng
    │
    └── Tồn bồn


Nhập hàng + Bán hàng + Tồn bồn
    │
    ├── Doanh thu
    ├── Thống kê
    └── Phân tích AI
```

Các dữ liệu trên là cơ sở cho các chức năng quản lý và phân tích của hệ thống.

---

# 7. NHỮNG NỘI DUNG NẰM NGOÀI PHẠM VI

Các nội dung dưới đây **không thuộc phạm vi hiện tại**, trừ khi có yêu cầu được phê duyệt và tài liệu phạm vi được cập nhật.

---

## 7.1. Quản lý khách hàng

Hệ thống hiện tại không tập trung vào:

* Hồ sơ khách hàng.
* Lịch sử mua hàng của từng khách hàng.
* Chương trình khách hàng thân thiết.
* Điểm thưởng.

---

## 7.2. Thanh toán điện tử

Hệ thống không triển khai trực tiếp:

* Ví điện tử.
* Cổng thanh toán.
* Thanh toán ngân hàng.
* QR Payment.

---

## 7.3. Quản lý nhà cung cấp chuyên sâu

Hệ thống hiện tại tập trung vào việc ghi nhận nhập hàng.

Các nghiệp vụ quản lý nhà cung cấp chuyên sâu như:

* Hợp đồng.
* Công nợ.
* Đánh giá nhà cung cấp.
* Quản lý đơn đặt hàng.

không thuộc phạm vi hiện tại nếu chưa được xác định trong yêu cầu.

---

## 7.4. Quản lý tài chính - kế toán chuyên sâu

Hệ thống cung cấp các số liệu:

* Doanh thu.
* Nhập.
* Xuất / bán.
* Tồn.

nhằm phục vụ:

* Tra cứu.
* Thống kê.
* Đối chiếu.

Hệ thống **không thay thế phần mềm kế toán chuyên nghiệp**.

---

## 7.5. Điều khiển thiết bị vật lý

Hệ thống không trực tiếp điều khiển:

* Máy bơm.
* Van.
* Cảm biến bồn.
* Thiết bị đo nhiên liệu.
* Hệ thống thanh toán tại cột bơm.

Nếu trong tương lai tích hợp thiết bị IoT, phạm vi phải được cập nhật riêng.

---

## 7.6. AI tự động ra quyết định

AI không được tự động:

* Phê duyệt nhập hàng.
* Từ chối nhập hàng.
* Thay đổi tồn kho.
* Thay đổi giá bán.
* Khóa tài khoản.
* Xử lý nhân viên.
* Thực hiện quyết định nghiệp vụ thay người quản lý.

AI chỉ cung cấp thông tin hỗ trợ trong phạm vi được hệ thống xác định.

---

# 8. GIỚI HẠN DỮ LIỆU AI

AI chỉ được phân tích dữ liệu được hệ thống cung cấp cho nó.

AI không được:

* Tự bịa số liệu.
* Tự bổ sung dữ liệu không có nguồn.
* Tự suy đoán dữ liệu bị thiếu thành dữ liệu thực tế.
* Thay đổi dữ liệu gốc trong cơ sở dữ liệu.
* Sử dụng dữ liệu nhạy cảm không cần thiết.
* Tiết lộ thông tin bí mật.

Khi dữ liệu không đủ để đưa ra kết luận, AI phải thể hiện rõ giới hạn của dữ liệu.

Ví dụ:

```text
Dữ liệu hiện tại không đủ để xác định nguyên nhân.
Cần bổ sung dữ liệu liên quan trước khi đưa ra kết luận.
```

---

# 9. RANH GIỚI GIỮA HỆ THỐNG VÀ AI

Có thể xác định ranh giới như sau:

```text
┌───────────────────────────────────────────────┐
│              HỆ THỐNG QUẢN LÝ                │
│                                               │
│  Tài khoản                                    │
│  Nhân viên                                    │
│  Nhiên liệu                                   │
│  Bồn chứa                                     │
│  Nhập hàng                                    │
│  Bán hàng                                     │
│  Ca làm việc                                  │
│  Tồn bồn                                      │
│  Doanh thu                                    │
│                                               │
│          ↓ Dữ liệu được kiểm soát             │
├───────────────────────────────────────────────┤
│                     AI                        │
│                                               │
│  • Tổng hợp                                   │
│  • Tóm tắt                                    │
│  • Phân tích                                  │
│  • Cảnh báo                                   │
│                                               │
│          ↓ Kết quả hỗ trợ                     │
├───────────────────────────────────────────────┤
│                  NGƯỜI DÙNG                   │
│                                               │
│       Kiểm tra → Đánh giá → Quyết định        │
└───────────────────────────────────────────────┘
```

## Nguyên tắc

> **AI không có quyền vượt qua ranh giới nghiệp vụ của hệ thống.**

AI chỉ xử lý dữ liệu trong phạm vi được hệ thống cung cấp và không tự động thay thế quyết định nghiệp vụ của con người.

---

# 10. QUY TẮC KIỂM SOÁT PHẠM VI

Khi phát sinh yêu cầu mới, AI Agent phải kiểm tra:

1. Yêu cầu có thuộc phạm vi hiện tại không?
2. Yêu cầu có làm thay đổi nghiệp vụ hiện tại không?
3. Yêu cầu có cần thêm dữ liệu mới không?
4. Yêu cầu có ảnh hưởng đến vai trò và phân quyền không?
5. Yêu cầu có ảnh hưởng đến cơ sở dữ liệu không?
6. Yêu cầu có ảnh hưởng đến Use Case không?
7. Yêu cầu có ảnh hưởng đến kiểm thử không?
8. Yêu cầu có ảnh hưởng đến báo cáo hoặc sơ đồ không?
9. Yêu cầu có ảnh hưởng đến chức năng AI không?
10. Yêu cầu có làm thay đổi ranh giới giữa hệ thống và AI không?

---

## 10.1. Nếu yêu cầu thuộc phạm vi

AI có thể tiếp tục phân tích và thực hiện theo quy trình phát triển của ProjectQLTX.

---

## 10.2. Nếu yêu cầu chưa được xác định

AI phải đánh dấu:

```text
[CẦN XÁC NHẬN]
```

Không được tự động coi yêu cầu là chính thức.

---

## 10.3. Nếu yêu cầu nằm ngoài phạm vi

AI không được tự ý triển khai.

Phải xác định yêu cầu đó thuộc một trong các trường hợp:

```text
Thay đổi phạm vi
        hoặc
Mở rộng phạm vi
        hoặc
Không thuộc hệ thống
```

Nếu đề xuất mở rộng phạm vi, phải tách riêng thành:

```text
ĐỀ XUẤT MỞ RỘNG PHẠM VI
```

và không coi đó là yêu cầu chính thức.

---

# 11. TRẠNG THÁI PHẠM VI

Phạm vi trong tài liệu này được xem là **phạm vi cơ sở của phiên bản hiện tại**.

Mọi thay đổi phạm vi phải được:

1. Ghi nhận.
2. Phân tích ảnh hưởng.
3. Cập nhật tài liệu.
4. Cập nhật Use Case.
5. Cập nhật thiết kế nếu cần.
6. Cập nhật kiểm thử.
7. Cập nhật ma trận truy vết.
8. Ghi nhận trong lịch sử thay đổi.

> **Không được thay đổi phạm vi chỉ bằng cách sửa code.**

---

# 12. QUY TẮC ĐẶC BIỆT VỀ CA LÀM VIỆC VÀ BÁN HÀNG

Đây là một quy tắc nghiệp vụ quan trọng của ProjectQLTX.

## 12.1. Ca làm việc

Ca làm việc được sử dụng để:

* Quản lý ca.
* Phân công nhân viên.
* Xác định nhân viên thực hiện công việc.

## 12.2. Bán hàng

Dữ liệu bán hàng hiện tại được xác định theo **ngày**.

Thông tin bán hàng tối thiểu:

```text
Ngày bán
Nhân viên
Nhiên liệu
Bồn chứa
Số lượng bán
Đơn giá
Thành tiền
```

## 12.3. Không suy diễn doanh số theo ca

AI Agent **không được suy diễn** rằng:

```text
Có ca làm việc
        ↓
Phải có doanh số theo ca
```

Quy tắc chính thức là:

```text
Có ca làm việc
        ≠
Bắt buộc có doanh số theo ca
```

Do đó, AI Agent không được tự ý:

* Thêm trường doanh số theo ca.
* Thêm bảng doanh số theo ca.
* Thêm Use Case bán hàng theo ca.
* Thêm báo cáo doanh thu theo ca.
* Thêm API doanh số theo ca.

trừ khi yêu cầu này được xác định và phê duyệt trong tài liệu phạm vi mới.

---

# 13. NGUYÊN TẮC ƯU TIÊN KHI CÓ XUNG ĐỘT

Khi xử lý một yêu cầu mới, AI Agent phải ưu tiên:

```text
Tài liệu phạm vi hiện tại
        ↓
Các tài liệu yêu cầu chính thức
        ↓
Thiết kế đã được phê duyệt
        ↓
Code hiện tại
        ↓
Đề xuất kỹ thuật của AI
```

Đề xuất kỹ thuật của AI **không được tự động trở thành yêu cầu của hệ thống**.

Nếu các tài liệu chính thức có mâu thuẫn, AI Agent phải:

1. Phát hiện mâu thuẫn.
2. Chỉ ra nguồn liên quan.
3. Mô tả điểm mâu thuẫn.
4. Không tự ý chọn phương án.
5. Yêu cầu xác nhận nếu mâu thuẫn ảnh hưởng đến kết quả.

---

# 14. CHECKLIST KIỂM TRA PHẠM VI

Trước khi triển khai một yêu cầu mới, AI Agent có thể sử dụng checklist:

```text
[ ] Yêu cầu có thuộc phạm vi hệ thống?
[ ] Có thuộc nhóm nghiệp vụ hiện tại?
[ ] Có actor tương ứng?
[ ] Có Use Case tương ứng?
[ ] Có dữ liệu cần thiết?
[ ] Có ảnh hưởng database?
[ ] Có ảnh hưởng API?
[ ] Có ảnh hưởng phân quyền?
[ ] Có ảnh hưởng AI?
[ ] Có ảnh hưởng security?
[ ] Có ảnh hưởng testing?
[ ] Có ảnh hưởng documentation?
[ ] Có ảnh hưởng traceability?
[ ] Có cần cập nhật phạm vi?
[ ] Có cần người dùng xác nhận?
```

Nếu có mục quan trọng chưa xác định, AI Agent phải dừng ở bước phân tích và yêu cầu bổ sung hoặc xác nhận thay vì tự bịa thông tin.

---

# 15. NGUYÊN TẮC CUỐI CÙNG

ProjectQLTX tập trung vào:

```text
Quản lý trạm xăng
        +
Quản lý dữ liệu nghiệp vụ
        +
Tra cứu và thống kê
        +
Phân tích dữ liệu
        +
AI hỗ trợ
```

AI là thành phần hỗ trợ:

```text
Dữ liệu hệ thống
        ↓
      AI
        ↓
Tổng hợp / Tóm tắt / Phân tích / Cảnh báo
        ↓
    Người dùng
        ↓
Kiểm tra / Đánh giá / Quyết định
```

AI không được:

```text
Tự tạo dữ liệu
Tự thay đổi dữ liệu gốc
Tự quyết định nghiệp vụ
Tự mở rộng phạm vi
Tự tạo yêu cầu chính thức
```

### Quy tắc quan trọng nhất

> **Phạm vi được xác định bởi tài liệu chính thức và quyết định của con người, không được xác định ngược lại từ những gì AI cho rằng hệ thống nên có.**

> **Mọi chức năng chưa được xác định phải được coi là chưa thuộc phạm vi cho đến khi được xác nhận hoặc cập nhật chính thức.**
