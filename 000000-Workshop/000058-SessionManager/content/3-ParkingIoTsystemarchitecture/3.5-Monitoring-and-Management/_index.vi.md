---
title : "Monitoring and Management"
date: 2026-05-13
weight : 5
chapter : false
pre : " <b> 3.5. </b> "
---

Phần này mô tả chi tiết các giải pháp giám sát vận hành, theo dõi hiệu năng và quản trị chi phí cho **Nền tảng Web App Smart Parking IoT** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)) sau khi triển khai thực tế trên hạ tầng AWS Serverless.

Hệ thống kết hợp các công cụ giám sát chuyên sâu từ AWS (Lambda, API Gateway, IoT Core, S3, DynamoDB, Rekognition, Lambda AI Service) nhằm duy trì thời gian hoạt động liên tục (Uptime 99.9%), đảm bảo độ trễ thấp cho Web App và tối ưu hóa ngân sách vận hành:
* **Amazon CloudWatch:** Quản lý tập trung CloudWatch Dashboards, Log Groups của API Gateway/Lambda, và thiết lập CloudWatch Alarms cảnh báo lỗi tự động.
* **AWS Budgets & Cost Explorer:** Theo dõi chi phí từng dịch vụ hàng ngày và phát cảnh báo qua Email khi chi phí đạt ngưỡng 80% ngân sách đề ra.
* **AWS CloudTrail:** Ghi vết (Audit Logs) toàn bộ các thao tác quản trị tài nguyên AWS nhằm đáp ứng tiêu chuẩn an toàn thông tin.
* **IAM Security Governance:** Định kỳ rà soát các chính sách phân quyền (Least Privilege) của Lambda microservices và API Authorizers.

### 3.5.1. Mục tiêu Giám sát Vận hành Nền tảng Web App
Quy trình giám sát hệ thống được thiết lập nhằm đảm bảo Web App hoạt động mượt mà 24/7 và hỗ trợ quản trị viên nhanh chóng khắc phục sự cố phần cứng/phần mềm.

**Mục tiêu Giám sát Chính:**
* **Theo dõi Hiệu năng Lambda Backend:** Đảm bảo thời gian thực thi (Duration) của các hàm Lambda dưới 500ms và tỷ lệ lỗi (Error Rate) dưới 0.1%.
* **Giám sát Lưu lượng API Gateway:** Đếm tổng số lượng request HTTPS từ Web App, theo dõi các mã lỗi 4xx/5xx.
* **Kiểm tra Kết nối IoT Core:** Theo dõi số lượng thiết bị ESP32 gửi thông điệp MQTT thành công.
* **Giám sát Quá trình Nhận diện ANPR:** Phát hiện sớm các trường hợp Lambda Image Processing không trích xuất được biển số từ ảnh S3.
* **Kiểm soát Ngân sách Đám mây:** Đảm bảo chi phí sử dụng AWS hàng tháng nằm trong ngân sách dự kiến.

### 3.5.2. Quản lý Tập trung với Amazon CloudWatch Dashboards
Nhóm đã xây dựng một **CloudWatch Operational Dashboard** tổng hợp các chỉ số theo thời gian thực:

**Các Widget Chỉ số Chính trên CloudWatch Dashboard:**
1. **API Gateway Invocations & Latency:** Biểu đồ lượng truy cập Web App theo phút và độ trễ phản hồi API.
2. **Lambda Duration & Errors:** Biểu đồ theo dõi thời gian thực thi và số lần gặp exception của các hàm Lambda (bao gồm Lambda Backend, Image Processing và Lambda AI Service).
3. **DynamoDB Consumed Read/Write Units:** Đo lường đơn vị Capacity Units đã tiêu thụ trên bảng `ParkingSlots` và `VehicleLogs`.
4. **AWS IoT Core Message Ingestion:** Số lượng tin nhắn MQTT nhận được từ cảm biến đỗ xe.

### 3.5.3. Cấu hình CloudWatch Log Groups & Insights
Toàn bộ log vận hành từ API Gateway, Lambda Backend và IoT Core Rules được tự động đẩy về **CloudWatch Logs Groups**:

* **Thời gian lưu trữ log (Retention Policy):** Cấu hình tự động xóa log sau 30 ngày để tiết kiệm chi phí lưu trữ.
* **CloudWatch Logs Insights:** Sử dụng ngôn ngữ truy vấn log để chủ động tìm kiếm các lỗi hệ thống:
  ```sql
  fields @timestamp, @message
  | filter @message like /ERROR/ or @message like /Exception/
  | sort @timestamp desc
  | limit 20
  ```

### 3.5.4. Thiết lập Cảnh báo Tự động với CloudWatch Alarms & Amazon SNS
Hệ thống cấu hình các quy tắc cảnh báo tự động gửi thông báo qua Email/SMS tới Quản trị viên hệ thống qua **Amazon SNS (Simple Notification Service)**:

| Tên Cảnh báo Alarm | Điều kiện Kích hoạt | Hành động |
|---|---|---|
| `High-Lambda-Error-Alarm` | Hàm Lambda có số lỗi > 5 trong vòng 5 phút | Gửi Email cảnh báo sự cố khẩn cấp cho DevSecOps |
| `API-Gateway-5xx-Alarm` | Tỷ lệ lỗi 5xx trên API Gateway > 1% | Thông báo sự cố nghẽn backend Web App |
| `ESP32-Offline-Alarm` | Không nhận được heartbeat MQTT trong 3 phút | Cảnh báo thiết bị cảm biến mất kết nối Wi-Fi |

### 3.5.5. Quản trị Chi phí với AWS Budgets & Cost Explorer
Hệ thống sử dụng **AWS Budgets** để giám sát và kiểm soát chi phí vận hành nền tảng Web App trên AWS:
* **Ngân sách Dự kiến (Monthly Budget):** Đặt ngưỡng chi phí $20.00 USD/tháng cho toàn bộ môi trường thử nghiệm & sản xuất.
* **Cảnh báo Chi phí:** Gửi Email thông báo tự động khi chi phí thực tế đạt **80% ($16.00)** và **100% ($20.00)** của ngân sách thiết lập.
* **Cost Explorer Breakdown:** Theo dõi chi tiết chi phí phát sinh theo từng dịch vụ (DynamoDB, Lambda, Rekognition, CloudFront).

### 3.5.6. Ghi vết Nhật ký An toàn Thông tin với AWS CloudTrail
AWS CloudTrail ghi lại toàn bộ nhật ký API và thao tác quản trị trên tài khoản AWS:
* Kiểm vết ai đã thay đổi cấu hình Lambda, sửa đổi rule AWS WAF hoặc thay đổi chính sách Cognito User Pool.
* Đáp ứng các tiêu chuẩn an toàn thông tin và hỗ trợ điều tra sự cố bảo mật khi cần thiết.

### 3.5.7. Quy trình Xử lý Sự cố & Quản lý Bảo trì
1. **Phát hiện Sự cố:** CloudWatch Alarm kích hoạt SNS gửi thông báo tới nhóm vận hành.
2. **Truy vết Root Cause:** Nhóm dev mở CloudWatch Logs Insights tra cứu theo `RequestId` của hàm Lambda bị lỗi.
3. **Sửa lỗi & Re-deploy:** Cập nhật mã nguồn Lambda bằng CDK CLI và xác nhận lại chỉ số metric trên CloudWatch Dashboard.

### 3.5.8. Kết luận
Hệ thống giám sát vận hành CloudWatch kết hợp cùng quản trị chi phí AWS Budgets đã mang lại khả năng quản lý toàn diện cho **Nền tảng Web App Smart Parking IoT**. Quản trị viên hoàn toàn chủ động trong việc duy trì hiệu năng cao, đảm bảo tính sẵn sàng và kiểm soát chặt chẽ ngân sách đám mây.
