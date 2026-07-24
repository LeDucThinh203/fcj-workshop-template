---
title : "Monitoring and Management"
date: 2026-05-13
weight : 5
chapter : false
pre : " <b> 3.5. </b> "
---

Phần này mô tả chi tiết các giải pháp giám sát vận hành, theo dõi hiệu năng và quản trị chi phí cho **Nền tảng Web App Smart Parking IoT** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)) sau khi triển khai thực tế trên hạ tầng AWS Serverless.

Hệ thống kết hợp các công cụ giám sát chuyên sâu từ AWS (Lambda ANPR, Lambda AI Chatbot, Lambda AI Forecast 7 ngày, AppSync WebSockets, API Gateway, IoT Core, S3, DynamoDB, Rekognition) nhằm duy trì thời gian hoạt động liên tục (Uptime 99.9%), đảm bảo độ trễ thấp cho Web App và tối ưu hóa ngân sách vận hành:
* **Amazon CloudWatch:** Quản lý tập trung CloudWatch Dashboards, Log Groups của API Gateway/Lambda/AppSync, và thiết lập CloudWatch Alarms cảnh báo lỗi tự động.
* **AWS Budgets & Cost Explorer:** Theo dõi chi phí từng dịch vụ hàng ngày và phát cảnh báo qua Email khi chi phí đạt ngưỡng 80% ngân sách đề ra.
* **AWS CloudTrail:** Ghi vết (Audit Logs) toàn bộ các thao tác quản trị tài nguyên AWS nhằm đáp ứng tiêu chuẩn an toàn thông tin.
* **IAM Security Governance:** Định kỳ rà soát các chính sách phân quyền (Least Privilege) của Lambda microservices và API Authorizers.

### 3.5.1. Mục tiêu Giám sát Vận hành Nền tảng Web App
Quy trình giám sát hệ thống được thiết lập nhằm đảm bảo Web App hoạt động mượt mà 24/7 và hỗ trợ quản trị viên nhanh chóng khắc phục sự cố phần cứng/phần mềm.

**Mục tiêu Giám sát Chính:**
* **Theo dõi Hiệu năng Lambda Backend & AI:** Đảm bảo thời gian thực thi (Duration) của các hàm Lambda (ANPR, AI Chatbot, AI Forecast 7 ngày) dưới 500ms và tỷ lệ lỗi (Error Rate) dưới 0.1%.
* **Giám sát Kết nối AppSync WebSockets:** Theo dõi số lượng kết nối Chatbox Socket đồng thời và độ trễ phát GraphQL Subscriptions.
* **Giám sát Lưu lượng API Gateway:** Đếm tổng số lượng request HTTPS từ Web App, theo dõi các mã lỗi 4xx/5xx.
* **Kiểm tra Kết nối IoT Core:** Theo dõi số lượng thiết bị ESP32 gửi thông điệp MQTT thành công.
* **Giám sát Quá trình Nhận diện ANPR:** Phát hiện sớm các trường hợp Lambda Image Processing không trích xuất được biển số từ ảnh S3.
* **Kiểm soát Ngân sách Đám mây:** Đảm bảo chi phí sử dụng AWS hàng tháng nằm trong ngân sách dự kiến.

### 3.5.2. Quản lý Tập trung với Amazon CloudWatch Dashboards
Nhóm đã xây dựng một **CloudWatch Operational Dashboard** tổng hợp các chỉ số theo thời gian thực:

**Các Widget Chỉ số Chính trên CloudWatch Dashboard:**
1. **API Gateway & AppSync Invocations:** Biểu đồ lượng truy cập Web App, lượng tin nhắn Chatbox WebSockets theo phút và độ trễ phản hồi.
2. **Lambda Microservices Duration & Errors:** Biểu đồ theo dõi thời gian thực thi của Lambda Backend, Lambda ANPR, Lambda AI Chatbot và Lambda AI 7-Day Forecast.
3. **DynamoDB Consumed Capacity:** Đo lường đơn vị Read/Write Capacity Units đã tiêu thụ trên các bảng `ParkingSlots`, `VehicleLogs`, `TrafficForecasts` và `ChatMessages`.
4. **AWS IoT Core Message Ingestion:** Số lượng tin nhắn MQTT nhận được từ cảm biến đỗ xe.

### 3.5.3. Cấu hình CloudWatch Log Groups & Insights
Toàn bộ log vận hành từ API Gateway, AppSync, Lambda Microservices và IoT Core Rules được tự động đẩy về **CloudWatch Logs Groups**:
* **Retention Policy:** Cấu hình tự động xóa log sau 30 ngày để tiết kiệm chi phí lưu trữ.
* **CloudWatch Logs Insights:** Truy vấn chủ động tìm lỗi hệ thống qua cú pháp query.

### 3.5.4. Thiết lập Cảnh báo Tự động với CloudWatch Alarms & Amazon SNS
Kích hoạt thông báo Email/SMS qua Amazon SNS khi phát hiện số lỗi Lambda > 5 trong 5 phút hoặc tỷ lệ lỗi API > 1%.

### 3.5.5. Quản trị Chi phí với AWS Budgets & Cost Explorer
Đánh giá và kiểm soát chi phí điện toán đám mây với ngân sách $20.00 USD/tháng, nhận cảnh báo tự động ở mức 80% và 100%.

### 3.5.6. Ghi vết Nhật ký An toàn Thông tin với AWS CloudTrail
Ghi vết toàn bộ thao tác quản trị trên tài khoản AWS nhằm đáp ứng tiêu chuẩn bảo mật.

### 3.5.7. Kết luận
Hệ thống giám sát vận hành CloudWatch kết hợp cùng quản trị chi phí AWS Budgets đã mang lại khả năng quản lý toàn diện cho **Nền tảng Web App Smart Parking IoT**.
