# TỪ ĐIỂN THUẬT NGỮ

## 1. Mục đích

Tài liệu này quy định cách hiểu và cách sử dụng các thuật ngữ trong Hệ thống quản lý trạm xăng có tích hợp AI.

Tài liệu được sử dụng làm nguồn tham chiếu thống nhất cho:

- Phân tích yêu cầu.
- Thiết kế hệ thống.
- Thiết kế cơ sở dữ liệu.
- Thiết kế API.
- Viết mã nguồn.
- Xây dựng Use Case.
- Xây dựng sơ đồ.
- Viết kiểm thử.
- Tích hợp AI.
- Viết báo cáo.
- Tạo tài liệu DOCX.

AI Agent phải ưu tiên sử dụng các thuật ngữ trong tài liệu này khi tạo hoặc chỉnh sửa nội dung của project.

---

# 2. Thuật ngữ nghiệp vụ

| Thuật ngữ | Định nghĩa | Cách sử dụng |
|---|---|---|
| Trạm xăng | Đơn vị kinh doanh và cung cấp nhiên liệu cho phương tiện | Thuật ngữ tổng quát của hệ thống |
| Nhiên liệu | Mặt hàng nhiên liệu được lưu trữ và bán tại trạm | Dùng khi nói về loại sản phẩm |
| Mặt hàng nhiên liệu | Một loại nhiên liệu được quản lý trong hệ thống | Tương ứng với dữ liệu `nhien_lieu` |
| Bồn chứa | Thiết bị dùng để lưu trữ nhiên liệu | Dùng thống nhất thay cho "bể chứa" hoặc "tank" trong tài liệu tiếng Việt |
| Tồn bồn | Lượng nhiên liệu hiện có trong một bồn chứa | Dùng trong nghiệp vụ nhập - bán - tồn |
| Tồn đầu | Lượng nhiên liệu có trong bồn tại thời điểm bắt đầu kỳ theo dõi | Dùng để tính tồn cuối |
| Tồn cuối | Lượng nhiên liệu còn lại trong bồn tại thời điểm kết thúc kỳ theo dõi | Được tính từ tồn đầu, nhập và bán |
| Nhập hàng | Hoạt động đưa nhiên liệu từ nguồn cung cấp vào bồn chứa | Được ghi nhận bằng phiếu nhập |
| Phiếu nhập | Bản ghi mô tả một lần nhập nhiên liệu | Có trạng thái xử lý |
| Bán hàng | Hoạt động ghi nhận lượng nhiên liệu bán ra | Trong phạm vi hiện tại được tổng hợp theo ngày |
| Doanh thu | Giá trị tiền thu được từ hoạt động bán hàng được ghi nhận trong hệ thống | Dùng cho tra cứu và thống kê |
| Sản lượng bán | Tổng số lượng nhiên liệu đã bán trong một khoảng thời gian | Đơn vị phụ thuộc vào dữ liệu nhiên liệu |
| Chênh lệch tồn | Phần chênh lệch giữa số liệu tồn tính toán và số liệu đối chiếu | Dùng để hỗ trợ kiểm tra |
| Ca làm việc | Khoảng thời gian hoặc phân công làm việc của nhân viên tại trạm | Dùng để quản lý nhân viên và công việc |
| Nhân viên ca | Nhân viên thực hiện công việc trong ca được phân công | Một trong các vai trò người dùng |
| Quản lý | Người có quyền quản lý và kiểm soát các nghiệp vụ chính của hệ thống | Vai trò có quyền cao nhất trong phạm vi hiện tại |
| Kế toán | Người sử dụng dữ liệu doanh thu và nhập - xuất - tồn phục vụ công tác đối chiếu, thống kê | Một trong các vai trò người dùng |

---

# 3. Thuật ngữ hệ thống

| Thuật ngữ | Định nghĩa |
|---|---|
| Hệ thống | Hệ thống quản lý trạm xăng có tích hợp AI |
| Người dùng | Người sử dụng hệ thống thông qua tài khoản được cấp |
| Tài khoản | Thông tin dùng để xác thực và xác định người dùng |
| Vai trò | Nhóm quyền xác định những chức năng người dùng được phép truy cập |
| Phiên đăng nhập | Trạng thái xác định người dùng đã đăng nhập vào hệ thống |
| Phân quyền | Cơ chế giới hạn quyền truy cập chức năng theo vai trò |
| Cơ sở dữ liệu | Nơi lưu trữ dữ liệu nghiệp vụ của hệ thống |
| Dữ liệu nghiệp vụ | Dữ liệu phát sinh từ hoạt động thực tế của hệ thống |
| Trạng thái | Thông tin biểu thị tình trạng hiện tại của một đối tượng nghiệp vụ |
| Tra cứu | Hoạt động tìm kiếm và xem dữ liệu đã được lưu trong hệ thống |
| Thống kê | Hoạt động tổng hợp dữ liệu theo các tiêu chí xác định |
| Báo cáo | Nội dung tổng hợp dữ liệu nhằm cung cấp thông tin cho người dùng |
| Dashboard | Giao diện tổng hợp các chỉ số và thông tin quan trọng của hệ thống |

---

# 4. Thuật ngữ phát triển phần mềm

| Thuật ngữ | Định nghĩa |
|---|---|
| CRUD | Create, Read, Update, Delete — các thao tác tạo, xem, sửa và xóa dữ liệu |
| API | Giao diện cho phép các thành phần phần mềm trao đổi dữ liệu và chức năng |
| Route | Điểm truy cập URL được backend xử lý |
| Service | Thành phần chứa hoặc hỗ trợ xử lý logic nghiệp vụ |
| Template | Thành phần giao diện được server sử dụng để tạo HTML |
| Frontend | Phần giao diện mà người dùng tương tác |
| Backend | Phần xử lý nghiệp vụ, dữ liệu và yêu cầu từ frontend |
| Database | Cơ sở dữ liệu của hệ thống |
| SQL | Ngôn ngữ được sử dụng để truy vấn và thao tác với cơ sở dữ liệu quan hệ |
| Git | Hệ thống quản lý phiên bản mã nguồn |
| Repository | Kho lưu trữ mã nguồn và lịch sử thay đổi được quản lý bằng Git |
| Commit | Một mốc ghi nhận thay đổi trong Git |
| Branch | Nhánh phát triển độc lập trong Git |
| CI/CD | Quy trình tự động hóa kiểm thử, xây dựng và triển khai phần mềm |
| Docker | Công nghệ đóng gói và chạy ứng dụng trong container |
| Docker Compose | Công cụ định nghĩa và điều phối nhiều container bằng cấu hình |
| Health Check | Cơ chế kiểm tra trạng thái hoạt động của một thành phần hệ thống |
| Rollback | Đưa hệ thống hoặc phiên bản về trạng thái trước đó khi xảy ra sự cố |

---

# 5. Thuật ngữ phân tích và thiết kế

| Thuật ngữ | Định nghĩa |
|---|---|
| Yêu cầu chức năng | Chức năng hoặc hành vi hệ thống phải cung cấp |
| Yêu cầu phi chức năng | Các yêu cầu về chất lượng, bảo mật, hiệu năng, khả năng bảo trì và các đặc tính khác |
| Quy tắc nghiệp vụ | Quy định mà hệ thống phải tuân thủ khi xử lý nghiệp vụ |
| Quy trình nghiệp vụ | Chuỗi các bước thực hiện một nghiệp vụ |
| Actor | Đối tượng bên ngoài tương tác với hệ thống |
| Use Case | Mô tả một mục tiêu hoặc chức năng mà Actor thực hiện thông qua hệ thống |
| User Story | Mô tả nhu cầu của người dùng dưới góc nhìn người sử dụng hệ thống |
| Acceptance Criteria | Các điều kiện dùng để xác định User Story đã được thực hiện đúng |
| Ma trận truy vết | Bảng liên kết các yêu cầu với Use Case, User Story, thiết kế và kiểm thử |
| Kiến trúc hệ thống | Cấu trúc tổng thể và mối quan hệ giữa các thành phần hệ thống |
| Thành phần hệ thống | Một đơn vị có trách nhiệm xác định trong kiến trúc |
| ERD | Entity Relationship Diagram — sơ đồ thực thể liên kết |
| Entity | Đối tượng dữ liệu được quản lý trong hệ thống |
| Attribute | Thuộc tính mô tả một Entity |
| Primary Key | Khóa chính dùng để xác định duy nhất một bản ghi |
| Foreign Key | Khóa ngoại dùng để liên kết dữ liệu giữa các bảng |
| Relationship | Mối quan hệ giữa các Entity |
| Data Dictionary | Tài liệu mô tả các bảng, trường dữ liệu, kiểu dữ liệu và ràng buộc |

---

# 6. Thuật ngữ AI

| Thuật ngữ | Định nghĩa |
|---|---|
| AI | Artificial Intelligence — trí tuệ nhân tạo |
| GenAI | Generative Artificial Intelligence — AI tạo sinh |
| LLM | Large Language Model — mô hình ngôn ngữ lớn |
| Prompt | Nội dung chỉ dẫn được cung cấp cho AI để thực hiện một nhiệm vụ |
| System Prompt | Chỉ dẫn cấp hệ thống quy định vai trò, nguyên tắc và giới hạn của AI |
| Prompt Engineering | Kỹ thuật thiết kế và cải thiện prompt để đạt đầu ra phù hợp |
| RAG | Retrieval-Augmented Generation — phương pháp cung cấp dữ liệu liên quan cho LLM trước khi sinh câu trả lời |
| Embedding | Biểu diễn dữ liệu dưới dạng vector số để phục vụ tìm kiếm ngữ nghĩa |
| Vector Database | Cơ sở dữ liệu hỗ trợ lưu trữ và tìm kiếm vector |
| Context | Thông tin được cung cấp cho AI để AI hiểu nhiệm vụ và dữ liệu liên quan |
| Hallucination | Trường hợp AI tạo ra thông tin không có căn cứ hoặc không được dữ liệu hỗ trợ |
| Grounding | Việc ràng buộc câu trả lời AI vào dữ liệu hoặc nguồn thông tin xác định |
| HITL | Human-in-the-Loop — con người tham gia kiểm tra hoặc quyết định trong quy trình có AI |
| Function Calling | Cơ chế cho phép LLM yêu cầu hệ thống thực hiện một hàm hoặc thao tác được định nghĩa |
| Agent | Thành phần AI có khả năng sử dụng context, công cụ và quy trình để thực hiện nhiệm vụ |
| AI Agent | Agent được sử dụng để hỗ trợ phân tích, lập trình, kiểm thử, tạo tài liệu hoặc các nhiệm vụ khác của project |
| AI Output | Kết quả do AI sinh ra |
| AI Evaluation | Hoạt động đánh giá chất lượng đầu ra của AI |
| AI Safety | Các biện pháp nhằm giảm rủi ro khi sử dụng AI |
| Guardrail | Cơ chế giới hạn và kiểm soát đầu vào, quá trình xử lý hoặc đầu ra của AI |

---

# 7. Thuật ngữ kiểm thử

| Thuật ngữ | Định nghĩa |
|---|---|
| Kiểm thử | Hoạt động kiểm tra hệ thống nhằm xác định hệ thống có hoạt động đúng theo yêu cầu hay không |
| Test Case | Một trường hợp kiểm thử cụ thể |
| Test Data | Dữ liệu được sử dụng trong kiểm thử |
| Expected Result | Kết quả mong đợi của một Test Case |
| Actual Result | Kết quả thực tế khi chạy Test Case |
| Happy Path | Luồng sử dụng hợp lệ và bình thường |
| Edge Case | Trường hợp nằm ở biên hoặc điều kiện đặc biệt |
| Error Case | Trường hợp hệ thống nhận dữ liệu hoặc thao tác không hợp lệ |
| Regression Test | Kiểm thử lại các chức năng đã tồn tại sau khi hệ thống thay đổi |
| Smoke Test | Kiểm tra nhanh các chức năng quan trọng để xác định hệ thống có thể tiếp tục kiểm thử |
| Integration Test | Kiểm thử sự phối hợp giữa nhiều thành phần |
| Unit Test | Kiểm thử một đơn vị logic nhỏ của hệ thống |
| Bug | Lỗi khiến hệ thống hoạt động khác với yêu cầu hoặc hành vi mong đợi |
| Root Cause | Nguyên nhân gốc gây ra lỗi |
| Retest | Chạy lại kiểm thử sau khi lỗi đã được sửa |

---

# 8. Thuật ngữ triển khai và vận hành

| Thuật ngữ | Định nghĩa |
|---|---|
| Môi trường phát triển | Môi trường được sử dụng để lập trình và kiểm thử trong quá trình phát triển |
| Môi trường kiểm thử | Môi trường dành cho hoạt động kiểm thử hệ thống |
| Môi trường production | Môi trường chạy hệ thống phục vụ người dùng thực tế |
| Deployment | Quá trình đưa hệ thống lên một môi trường chạy |
| Monitoring | Hoạt động theo dõi trạng thái và chỉ số của hệ thống |
| Logging | Hoạt động ghi nhận các sự kiện và thông tin xử lý của hệ thống |
| Alert | Cảnh báo được tạo khi một điều kiện cần chú ý xảy ra |
| Backup | Bản sao dữ liệu được tạo để phục vụ khôi phục |
| Restore | Quá trình khôi phục dữ liệu từ bản sao lưu |
| Incident | Sự cố ảnh hưởng đến hoạt động hoặc chất lượng hệ thống |
| Recovery | Quá trình đưa hệ thống trở lại trạng thái hoạt động sau sự cố |
| MTTR | Mean Time To Recovery/Repair — thời gian trung bình để khôi phục hoặc sửa chữa sau sự cố |
| DORA | Nhóm chỉ số đánh giá hiệu quả phân phối phần mềm |
| SPACE | Khung đánh giá năng suất phát triển phần mềm dựa trên nhiều khía cạnh |

---

# 9. Quy ước viết tắt

| Viết tắt | Nghĩa đầy đủ |
|---|---|
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| CRUD | Create, Read, Update, Delete |
| DB | Database |
| ERD | Entity Relationship Diagram |
| FR | Functional Requirement |
| NFR | Non-Functional Requirement |
| GenAI | Generative Artificial Intelligence |
| HITL | Human-in-the-Loop |
| LLM | Large Language Model |
| RAG | Retrieval-Augmented Generation |
| SQL | Structured Query Language |
| UI | User Interface |
| UX | User Experience |
| UC | Use Case |
| US | User Story |
| TC | Test Case |
| CI/CD | Continuous Integration / Continuous Delivery hoặc Deployment |
| DORA | DevOps Research and Assessment |
| MTTR | Mean Time To Recovery/Repair |
| MLOps | Machine Learning Operations |
| RBAC | Role-Based Access Control |
| PoLP | Principle of Least Privilege |

---

# 10. Quy ước thuật ngữ trong ProjectQLTX

Để tránh không thống nhất giữa tài liệu, mã nguồn và báo cáo, ProjectQLTX sử dụng các quy ước sau:

| Không ưu tiên | Thuật ngữ chuẩn |
|---|---|
| Bể xăng | Bồn chứa |
| Tank | Bồn chứa |
| Loại xăng | Nhiên liệu |
| Sản phẩm | Mặt hàng nhiên liệu khi nói trong phạm vi nghiệp vụ |
| Nhập xăng | Nhập hàng |
| Phiếu nhập xăng | Phiếu nhập |
| Tồn kho bồn | Tồn bồn |
| Nhân viên bán | Nhân viên ca nếu đang nói về vai trò hệ thống |
| Ca bán hàng | Ca làm việc khi nói về phân công nhân viên |
| AI tự quyết định | AI hỗ trợ quyết định |
| AI đoán nguyên nhân | AI phân tích dựa trên dữ liệu được cung cấp |
| AI tạo số liệu | AI tổng hợp dữ liệu nguồn |

Các thuật ngữ chuẩn phải được ưu tiên trong:

- Tên tài liệu.
- Nội dung báo cáo.
- Tên Use Case.
- Tên User Story.
- Sơ đồ.
- Prompt.
- Nội dung AI sinh ra.
- Tên biến hoặc hàm khi phù hợp.
- Tên hiển thị trên giao diện.

---

# 11. Quy tắc sử dụng thuật ngữ

AI Agent phải tuân thủ các nguyên tắc:

1. Không tự tạo thêm định nghĩa nghiệp vụ nếu thuật ngữ đã được xác định trong tài liệu.
2. Không sử dụng nhiều thuật ngữ khác nhau để chỉ cùng một đối tượng nếu không có lý do rõ ràng.
3. Khi phát hiện hai tài liệu sử dụng thuật ngữ không thống nhất, phải xác định sự khác biệt trước khi sửa.
4. Không tự đổi tên bảng hoặc trường dữ liệu chỉ vì muốn thuật ngữ đẹp hơn.
5. Khi thuật ngữ nghiệp vụ và tên kỹ thuật khác nhau, phải giữ cả hai và thể hiện rõ mối quan hệ.

Ví dụ:

```text
Thuật ngữ nghiệp vụ:
Bồn chứa

Tên bảng:
bon_chua

Tên biến có thể sử dụng:
bon_chua

Tên tiếng Anh trong sơ đồ kỹ thuật:
Tank

12. Quy tắc cập nhật từ điển

Khi phát sinh thuật ngữ mới:

Kiểm tra xem thuật ngữ đã tồn tại hay chưa.
Xác định ý nghĩa nghiệp vụ.
Xác định tên kỹ thuật nếu cần.
Kiểm tra xung đột với thuật ngữ hiện có.
Cập nhật tài liệu này.
Kiểm tra các tài liệu có sử dụng thuật ngữ.
Cập nhật sơ đồ hoặc code nếu cần.
Ghi nhận thay đổi trong lịch sử thay đổi.

Không tự ý tạo thuật ngữ mới chỉ để giải quyết một lỗi đặt tên trong code.

13. Nguyên tắc ưu tiên

Khi có sự khác biệt giữa cách gọi trong tài liệu và cách gọi trong mã nguồn:

Thuật ngữ nghiệp vụ
        ↓
Tài liệu yêu cầu
        ↓
Thiết kế hệ thống
        ↓
Tên kỹ thuật trong code/database

Tên kỹ thuật có thể khác thuật ngữ nghiệp vụ, nhưng mối quan hệ giữa chúng phải được xác định rõ.

Mục tiêu là đảm bảo người đọc báo cáo, người phát triển hệ thống và AI Agent đều hiểu cùng một khái niệm.