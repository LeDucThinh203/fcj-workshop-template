---
title : "User Interface and Security"
date: 2026-05-13
weight : 4
chapter : false
pre : " <b> 3.4. </b> "
---

Phần này trình bày chi tiết về **Giao diện Nền tảng Web App Smart Parking IoT** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)) và **Hệ thống Bảo mật Đa lớp** đã được triển khai thành công trên hạ tầng AWS Serverless.

Nền tảng Web App đóng vai trò là trung tâm điều hành trực quan (Operational Control Center) cho nhà quản lý và cổng tiện ích tự phục vụ (Self-service Portal) cho khách đỗ xe, tích hợp trợ lý ảo AI phát triển trên AWS Lambda và cơ chế bảo mật điện toán đám mây toàn diện.

### 3.4.1. Tổng quan Giao diện Web App Đã Triển khai
Giao diện Web App được phát triển bằng ngôn ngữ HTML5/CSS3/JavaScript hiện đại, tối ưu hóa giao diện responsive hiển thị tốt trên cả máy tính bàn (Desktop) và thiết bị di động (Mobile).

**Các tính năng cốt lõi đã hoàn thiện trên Web App:**
* 🔑 **Hệ thống Xác thực Người dùng:** Đăng ký, đăng nhập tài khoản an toàn qua Amazon Cognito User Pool.
* 📊 **Sơ đồ Vị trí Đỗ xe Thời gian thực (Real-time Slot Map):** Trực quan hóa danh sách các ô đỗ xe với màu xanh (Còn trống) và màu đỏ (Đã có xe).
* 🚗 **Nhật ký Xe Ra/Vào & ANPR Log:** Xem danh sách toàn bộ lượt xe vào/ra bãi, hiển thị hình ảnh chụp từ ESP32-CAM và kết quả biển số xe tự động.
* 🔍 **Bộ máy Tra cứu Biển số Xe:** Tìm kiếm tức thời lịch sử gửi xe theo chuỗi ký tự biển số.
* 🤖 **Trợ lý Virtual AI Assistant (AWS Lambda AI Service):** Khung chat AI hỗ trợ người dùng tra cứu thông tin và hỗ trợ Admin phân tích mật độ đỗ xe.
* 📈 **Thống kê & Báo cáo Mật độ:** Biểu đồ trực quan về tỷ lệ lấp đầy bãi xe và lưu lượng xe theo khung giờ.

{{% notice tip "Thông Tin Trải Nghiệm Trực Tuyến" %}}
🌐 **Web CloudFront Live Deploy:** [https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)  
🔑 **Tài khoản Admin trải nghiệm:** `leducthinh203` | **Mật khẩu:** `Admin123@`  
🎬 Xem video và bộ ảnh chụp chi tiết giao diện Web tại [Folder Google Drive Demo FE](https://drive.google.com/drive/folders/1RLwMvlmJNH05ot-FZzCE_2U7c10_8zqz?usp=sharing).
{{% /notice %}}

### 3.4.2. Phân phối Website Tốc độ Cao với Amazon S3 & CloudFront CDN
Ứng dụng Web tĩnh được build và lưu trữ trên Amazon S3 Static Website Hosting, sau đó được phân phối trực tiếp toàn cầu qua mạng lưới CDN **Amazon CloudFront** (`https://d3imp0j8sdburp.cloudfront.net`).

**Lợi ích của Kiến trúc CloudFront + S3:**
* **Tốc độ Tải trang Sub-second:** Nội dung tĩnh được lưu đệm (Caching) tại các Edge Location của CloudFront giúp giảm độ trễ truy cập xuống dưới 100ms.
* **Tự động Mã hóa HTTPS:** Tích hợp chứng chỉ SSL/TLS từ AWS Certificate Manager (ACM) đảm bảo mọi giao tiếp giữa trình duyệt web và hạ tầng AWS được mã hóa an toàn.
* **Giảm tải cho Backend S3:** CloudFront xử lý đến 95% lượng request tĩnh mà không làm tăng chi phí đọc trên S3 Bucket.

### 3.4.3. Định tuyến & Phân phối Trực tiếp qua Amazon CloudFront CDN
Hệ thống sử dụng đường dẫn trực tiếp của Amazon CloudFront CDN phân phối giao diện tới người dùng cuối mà không cần cấu hình DNS Route 53 phức tạp:
`Người dùng Web → CloudFront Distribution Domain (https://d3imp0j8sdburp.cloudfront.net) → Amazon S3 Bucket`.

### 3.4.4. Bảo vệ Nền tảng Web với AWS WAF (Web Application Firewall)
AWS WAF được đặt ở lớp đầu tiên phía trước CloudFront Distribution để ngăn chặn các mối đe dọa an ninh mạng:
* **Chống Tấn công Web Phổ biến:** Lọc các truy vấn có dấu hiệu SQL Injection (SQLi), Cross-Site Scripting (XSS).
* **Giới hạn Tần suất (Rate Limiting Rules):** Tự động chặn tạm thời các IP gửi quá 100 request/phút để phòng chống tấn công từ chối dịch vụ (DDoS / Brute Force).
* **IP Reputation Lists:** Sử dụng AWS Managed Rulesets để chặn các IP nằm trong danh sách đen độc hại.

### 3.4.5. Xác thực Người dùng với Amazon Cognito User Pool
Hệ thống quản lý định danh người dùng thông qua **Amazon Cognito User Pool**:

**Quy trình Đăng nhập & Xác thực API:**
1. Người dùng nhập Tài khoản/Mật khẩu trên giao diện Web App.
2. Web App gửi request authentication tới Cognito User Pool Endpoint.
3. Cognito xác thực và trả về bộ mã token mã hóa chuẩn **JWT (JSON Web Token)** bao gồm: `ID Token`, `Access Token` và `Refresh Token`.
4. Trong các request tiếp theo tới API Gateway, Web App đính kèm token trong Header `Authorization: Bearer <JWT_Token>`.
5. API Gateway Cognito Authorizer kiểm tra chữ ký và quyền hạn token trước khi cho phép kích hoạt hàm Lambda backend.

### 3.4.6. Phân quyền Người dùng (Role-Based Access Control - RBAC)
Nền tảng phân chia rõ ràng hai cấp độ quyền truy cập:

| Cấp độ Quyền | Đối tượng | Các tính năng được phép trên Web App |
|---|---|---|
| **Role: User (Khách đỗ xe)** | Khách hàng đăng ký tự do | Tra cứu vị trí đỗ trống, quản lý thông tin xe cá nhân, chat với Trợ lý AI |
| **Role: Admin (Quản trị viên)** | Tài khoản `leducthinh203` | Xem sơ đồ bãi xe toàn cảnh, truy cập toàn bộ nhật ký xe ra vào, tra cứu biển số, xem báo cáo thống kê |

### 3.4.7. Tích hợp Trợ lý Virtual AI Assistant trên AWS Lambda
Khung chat AI thông minh được nhúng trực tiếp ở góc dưới giao diện Web App:
* **Công nghệ tích hợp:** Xây dựng trên nền tảng **AWS Lambda AI Service**, kết nối trực tiếp với cơ sở dữ liệu DynamoDB và các giải thuật AI xử lý ngôn ngữ tự nhiên.
* **Khả năng Trợ lý AI:**
  - Trả lời tự nhiên các câu hỏi của khách hàng: *"Bãi xe hiện tại còn chỗ trống ở khu A không?"*, *"Phí gửi xe được tính như thế nào?"*.
  - Hỗ trợ Admin truy vấn dữ liệu theo ngôn ngữ tự nhiên: *"Tổng hợp số lượt xe vào bãi trong khung giờ từ 8h đến 10h sáng nay"*.

### 3.4.8. An toàn Dữ liệu & Tuân thủ Bảo mật IAM
* Toàn bộ dữ liệu nhạy cảm (như mật khẩu) được Cognito mã hóa với thuật toán mã hóa mạnh Salted SHA-256.
* Các hàm Lambda backend vận hành với IAM Execution Roles được cấp quyền tối thiểu (Least Privilege), đảm bảo một hàm xử lý ảnh không thể truy cập trái phép bảng dữ liệu người dùng.

### 3.4.9. Kết luận
Giải pháp giao diện người dùng Web App kết hợp cùng kiến trúc bảo mật đám mây AWS đã mang lại một nền tảng quản lý đỗ xe thông minh hiện đại, an toàn và dễ sử dụng. Hệ thống sẵn sàng phục vụ lượng lớn người dùng đồng thời trên môi trường sản xuất Internet.
