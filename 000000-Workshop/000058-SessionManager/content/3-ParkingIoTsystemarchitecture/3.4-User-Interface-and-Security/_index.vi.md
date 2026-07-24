---
title : "User Interface and Security"
date: 2026-05-13
weight : 4
chapter : false
pre : " <b> 3.4. </b> "
---

Phần này trình bày chi tiết về **Giao diện Nền tảng Web App Smart Parking IoT** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)) và **Hệ thống Bảo mật Đa lớp** đã được triển khai thành công trên hạ tầng AWS Serverless.

Nền tảng Web App đóng vai trò là trung tâm điều hành trực quan (Operational Control Center) cho nhà quản lý và cổng tiện ích tự phục vụ (Self-service Portal) cho khách đỗ xe, tích hợp **Trợ lý ảo AI Chatbot Assistant**, **Biểu đồ AI Dự báo Lưu lượng Xe 7 Ngày Tới**, **Khung Chatbox WebSockets qua AWS AppSync** và cơ chế bảo mật điện toán đám mây toàn diện.

### 3.4.1. Tổng quan Giao diện Web App Đã Triển khai
Giao diện Web App được phát triển bằng ngôn ngữ HTML5/CSS3/JavaScript hiện đại, tối ưu hóa giao diện responsive hiển thị tốt trên cả máy tính bàn (Desktop) và thiết bị di động (Mobile).

**Các tính năng cốt lõi đã hoàn thiện trên Web App:**
* 🔑 **Hệ thống Xác thực Người dùng:** Đăng ký, đăng nhập tài khoản an toàn qua Amazon Cognito User Pool.
* 📊 **Sơ đồ Vị trí Đỗ xe Thời gian thực (Real-time Slot Map):** Trực quan hóa danh sách các ô đỗ xe với màu xanh (Còn trống) và màu đỏ (Đã có xe), cập nhật tức thì qua **AWS AppSync Subscriptions**.
* 🚗 **Nhật ký Xe Ra/Vào & ANPR Log:** Xem danh sách toàn bộ lượt xe vào/ra bãi, hiển thị hình ảnh chụp từ ESP32-CAM và kết quả biển số xe tự động.
* 🔍 **Bộ máy Tra cứu Biển số Xe:** Tìm kiếm tức thời lịch sử gửi xe theo chuỗi ký tự biển số.
* 📈 **Biểu đồ AI Dự báo Lưu lượng Xe 7 Ngày Tới (7-Day Traffic Forecast):** Biểu đồ xu hướng trực quan do **Mô hình Lambda AI Forecast** tính toán, giúp Admin xem trước mật độ đỗ xe dự kiến từ Day +1 đến Day +7.
* 💬 **Khung Chatbox WebSockets Thời gian thực (AWS AppSync):** Giao tiếp hai chiều với độ trễ thấp thông qua GraphQL Subscriptions & WebSockets connection.
* 🤖 **Trợ lý Virtual AI Chatbot (AWS Lambda AI Chatbot):** Khung chat AI hỗ trợ người dùng tra cứu thông tin, tư vấn chính sách bãi xe và giải đáp thắc mắc tự động.
* 📊 **Thống kê Mật độ & Doanh thu:** Biểu đồ trực quan về tỷ lệ lấp đầy bãi xe và lưu lượng xe theo khung giờ.

{{% notice tip "Thông Tin Trải Nghiệm Trực Tuyến" %}}
🌐 **Web CloudFront Live Deploy:** [https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)  
🔑 **Tài khoản Admin trải nghiệm:** `leducthinh203` | **Mật khẩu:** `Admin123@`  
🎬 Xem video và bộ ảnh chụp chi tiết giao diện Web tại [Folder Google Drive Demo FE](https://drive.google.com/drive/folders/1RLwMvlmJNH05ot-FZzCE_2U7c10_8zqz?usp=sharing).
{{% /notice %}}

### 3.4.2. Phân phối Website Tốc độ Cao với Amazon S3 & CloudFront CDN
Ứng dụng Web tĩnh được build và lưu trữ trên Amazon S3 Static Website Hosting, sau đó được phân phối trực tiếp toàn cầu qua mạng lưới CDN **Amazon CloudFront** (`https://d3imp0j8sdburp.cloudfront.net`).

### 3.4.3. Định tuyến & Phân phối Trực tiếp qua Amazon CloudFront CDN
Hệ thống sử dụng đường dẫn trực tiếp của Amazon CloudFront CDN phân phối giao diện tới người dùng cuối mà không cần cấu hình DNS Route 53 phức tạp:
`Người dùng Web → CloudFront Distribution Domain (https://d3imp0j8sdburp.cloudfront.net) → Amazon S3 Bucket`.

### 3.4.4. Bảo vệ Nền tảng Web với AWS WAF (Web Application Firewall)
AWS WAF ngăn chặn các nguy cơ an ninh mạng (SQLi, XSS, Rate Limiting 100 req/min).

### 3.4.5. Xác thực Người dùng với Amazon Cognito User Pool
Xác thực người dùng qua mã JWT Token (`ID Token`, `Access Token`, `Refresh Token`).

### 3.4.6. Phân quyền Người dùng (Role-Based Access Control - RBAC)

| Cấp độ Quyền | Đối tượng | Các tính năng được phép trên Web App |
|---|---|---|
| **Role: User (Khách đỗ xe)** | Khách hàng đăng ký tự do | Tra cứu vị trí đỗ trống, quản lý thông tin xe cá nhân, chat với Trợ lý AI Chatbot qua WebSockets Chatbox |
| **Role: Admin (Quản trị viên)** | Tài khoản `leducthinh203` | Xem sơ đồ bãi xe toàn cảnh, nhật ký xe ra vào, tra cứu biển số, **xem Biểu đồ AI Dự báo Lưu lượng Xe 7 ngày tới** |

### 3.4.7. Tích hợp Trợ lý AI Chatbot, AI Dự báo 7 Ngày & AWS AppSync Chatbox
Các tính năng thông minh trên giao diện Web App bao gồm:

1. **Khung Chatbox WebSockets (AWS AppSync):**
   - **GraphQL Mutation `sendMessage`:** Người dùng gửi tin nhắn trên giao diện Chatbox qua kết nối WebSockets đến `Lambda AI Chatbot`.
   - **GraphQL Subscription `onNewChatMessage`:** AppSync tự động phát phản hồi tức thời về trình duyệt người dùng không cần reload trang.

2. **Trợ lý Virtual AI Chatbot Assistant (AWS Lambda AI Chatbot):**
   - Tự động trả lời thắc mắc của khách hàng: *"Bãi xe hiện tại còn chỗ trống ở khu A không?"*, *"Phí gửi xe được tính như thế nào?"*.

3. **Biểu đồ AI Dự báo Lưu lượng Xe 7 Ngày Tới (AWS Lambda AI Forecast):**
   - Tích hợp trực tiếp trên trang Admin Dashboard.
   - Hiển thị biểu đồ dự đoán số lượng xe ra/vào cho 7 ngày tiếp theo dựa trên mô hình phân tích chuỗi thời gian, giúp nhà quản lý tối ưu kế hoạch vận hành.

### 3.4.8. An toàn Dữ liệu & Tuân thủ Bảo mật IAM
Mật khẩu mã hóa Salted SHA-256; Phân quyền IAM Least Privilege cho các hàm Lambda backend (ANPR, AI Chatbot, AI Forecast).

### 3.4.9. Kết luận
Giao diện người dùng Web App tích hợp **Biểu đồ AI Dự báo 7 ngày**, **Trợ lý AI Chatbot** và **AWS AppSync WebSockets Chatbox** tạo nên giải pháp quản lý đỗ xe thông minh toàn diện và hiện đại.
