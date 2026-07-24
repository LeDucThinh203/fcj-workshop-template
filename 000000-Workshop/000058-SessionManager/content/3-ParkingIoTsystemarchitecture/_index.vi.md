---
title : "Project: Smart Parking IoT"
date: 2026-05-13
weight : 3
chapter : false
pre : " <b> 3. </b> "
---

# Nền tảng Website Smart Parking IoT trên AWS Serverless

Hệ thống **Smart Parking IoT** là giải pháp toàn diện hỗ trợ giám sát bãi đỗ xe thông minh, tự động nhận diện biển số xe (ANPR), tích hợp **Trợ lý ảo AI Chatbot**, **Mô hình Lambda AI Dự báo Lưu lượng Xe 7 ngày tới** và **Khung Chatbox thời gian thực qua AWS AppSync WebSockets**. Hệ thống đã được nhóm nghiên cứu và triển khai thành công trên môi trường sản xuất của **AWS Serverless**.

{{% notice tip "Thông Tin Truy Cập & Trải Nghiệm Trực Tuyến" %}}
🌐 **Website CloudFront (Live Deploy):** [https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)  
🔑 **Tài khoản Admin thử nghiệm:** `leducthinh203` | **Mật khẩu:** `Admin123@`  
👤 **Tài khoản Khách (User):** Người dùng có thể đăng ký tài khoản mới trực tiếp trên trang Web.  
🎬 **Demo Frontend (FE):** Xem video và bộ ảnh chụp giao diện Web Dashboard thực tế tại [Thư mục Google Drive Demo FE](https://drive.google.com/drive/folders/1RLwMvlmJNH05ot-FZzCE_2U7c10_8zqz?usp=sharing).
{{% /notice %}}

## Tổng quan Hệ thống đã triển khai

Chương này trình bày chi tiết về kiến trúc tổng thể, hạ tầng đám mây, luồng xử lý dữ liệu IoT thời gian thực, giao diện điều khiển Web App, cùng các giải pháp bảo mật và quản trị vận hành mà nhóm đã triển khai.

### Các Phân Hệ Cốt Lõi:

* **3.1. [AWS Core Infrastructure](3.1-aws-core-infrastructure/):** Hạ tầng Serverless cốt lõi bao gồm S3, DynamoDB, Lambda (Backend, ANPR, AI Chatbot, AI Dự báo 7 ngày), API Gateway, AWS AppSync (GraphQL & WebSockets Chatbox), AWS IoT Core, CloudFront và WAF được định nghĩa bằng AWS CDK.
* **3.2. [ESP32 Edge Devices](3.2-esp32-edge-devices/):** Các thiết bị biên phần cứng (ESP32 Camera chụp ảnh xe cổng vào/ra và ESP32 cảm biến phát hiện vị trí đỗ) kết nối trực tiếp với AWS.
* **3.3. [IoT Data Pipeline](3.3-iot-data-pipeline/):** Luồng truyền tải và xử lý dữ liệu thời gian thực giữa thiết bị biên, AWS Lambda, Amazon Rekognition (ANPR), AWS AppSync Subscriptions, mô hình AI Dự báo 7 ngày và lưu trữ DynamoDB.
* **3.4. [User Interface and Security](3.4-user-interface-and-Security/):** Giao diện Web Dashboard hiện đại (Admin & User Portal), Biểu đồ AI Dự báo Lưu lượng Xe 7 ngày tới, Khung Chatbox thời gian thực qua AWS AppSync WebSockets, AI Chatbot Assistant cùng kiến trúc bảo mật đa lớp với Cognito, CloudFront HTTPS và WAF.
* **3.5. [Monitoring and Management](3.5-monitoring-and-management/):** Hệ thống giám sát vận hành, nhật ký logs, cảnh báo sự cố với Amazon CloudWatch, theo dõi nhật ký bảo mật CloudTrail và quản lý ngân sách AWS Budgets.
* **3.6. [System Testing and Optimization](3.6-system-testing-and-Optimization/):** Kết quả kiểm thử thực tế về độ trễ (<2s), độ chính xác nhận diện biển số (>95%), độ chính xác dự báo AI, cùng các giải pháp tối ưu chi phí và hiệu năng vận hành.
