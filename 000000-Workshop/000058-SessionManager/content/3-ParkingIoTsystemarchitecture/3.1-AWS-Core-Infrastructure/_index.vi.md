---
title : "AWS Core Infrastructure"
date: 2026-05-13
weight : 1
chapter : false
pre : " <b> 3.1. </b> "
---

Phần này trình bày toàn bộ kiến trúc và thiết lập cơ sở hạ tầng cốt lõi AWS đã được nhóm nghiên cứu, triển khai và đưa vào vận hành thực tế phục vụ **Nền tảng Web App Smart Parking IoT** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)). 

Cơ sở hạ tầng của hệ thống được xây dựng hoàn toàn theo mô hình **AWS Serverless**, tận dụng sức mạnh kết hợp của **Amazon S3, Amazon DynamoDB, AWS Lambda, Amazon API Gateway, AWS AppSync (GraphQL & WebSockets Chatbox), AWS IoT Core, IAM, Amazon CloudFront, AWS WAF** và **Amazon CloudWatch**. Mô hình này cho phép Web App duy trì độ sẵn sàng cao, loại bỏ hoàn toàn gánh nặng quản lý máy chủ vật lý và tự động mở rộng (Auto-scaling) mượt mà khi lượng truy cập từ người dùng Web hoặc số lượng xe ra vào bãi tăng cao.

### 3.1.1. Mục tiêu & Vai trò Hạ tầng Đã Triển khai
Hạ tầng đám mây AWS cốt lõi đã hoàn thành tốt các nhiệm vụ chiến lược:

* **Phân phối Web App:** Phục vụ ứng dụng Web tĩnh lưu trữ trên Amazon S3, phân phối toàn cầu trực tiếp qua Amazon CloudFront CDN và bảo mật bằng AWS WAF.
* **Tích hợp Dữ liệu Biên:** Nhận ảnh xe ra/vào từ ESP32-CAM thông qua cơ chế S3 Presigned URL và tiếp nhận dữ liệu trạng thái chỗ đỗ qua giao thức MQTT gửi tới AWS IoT Core.
* **Truyền thông Socket Thời gian thực (AWS AppSync):** Thiết lập kết nối WebSockets hai chiều thông qua AWS AppSync cho khung **Chatbox Socket** tương tác thời gian thực và GraphQL Subscriptions đẩy cập nhật vị trí đỗ.
* **Xử lý Không Máy chủ & Dịch vụ AI (AWS Lambda):**
  - **Lambda ANPR:** Nhận diện biển số xe tự động qua Amazon Rekognition.
  - **Lambda AI Chatbot:** Trợ lý ảo Chatbot thông minh xử lý câu hỏi & tư vấn tự động cho người dùng.
  - **Lambda AI Forecast (Dự báo Lưu lượng Xe 7 Ngày Tới):** Mô hình AI phân tích dữ liệu lịch sử chuỗi thời gian (Time-series) để dự báo mật độ phương tiện ra vào bãi trong 7 ngày tới, hỗ trợ công tác quản lý trên Admin Dashboard.
* **Lưu trữ Dữ liệu Tốc độ Cao:** Lưu trữ toàn bộ nhật ký phương tiện, thông tin vị trí đỗ, dữ liệu dự báo AI và thông tin người dùng trên Amazon DynamoDB với độ trễ phản hồi sub-millisecond.
* **Cung cấp API cho Web Frontend:** Mở các RESTful API endpoints qua Amazon API Gateway và GraphQL APIs qua AWS AppSync tích hợp với Cognito Authorizer.
* **Bảo mật & Kiểm soát Vận hành:** Đảm bảo an toàn thông tin theo nguyên tắc Least Privilege thông qua IAM và theo dõi log/metric thời gian thực với Amazon CloudWatch.

### 3.1.2. Triển khai Hạ tầng bằng AWS CDK (Infrastructure as Code)
Toàn bộ tài nguyên trên AWS của hệ thống đã được định nghĩa và triển khai tự động bằng **AWS CDK (TypeScript)**. 

**Cấu trúc dự án CDK đã triển khai:**
```text
parking-iot-cdk/
├── bin/
│   └── parking-iot.ts            # Entry point khởi tạo các Stacks
├── lib/
│   ├── storage-stack.ts          # Định nghĩa S3 Buckets & DynamoDB Tables
│   ├── api-stack.ts              # Định nghĩa API Gateway & Lambda Backend
│   ├── appsync-stack.ts          # Định nghĩa AWS AppSync GraphQL Schema & WebSockets Chatbox
│   ├── iot-stack.ts              # Định nghĩa AWS IoT Core Rules & MQTT Topics
│   ├── auth-stack.ts             # Định nghĩa Cognito User Pools & Authorizers
│   ├── ai-chatbot-stack.ts       # Định nghĩa AWS Lambda AI Chatbot Assistant
│   ├── ai-forecast-stack.ts      # Định nghĩa AWS Lambda AI Dự báo Lưu lượng Xe 7 ngày tới
│   └── monitoring-stack.ts       # Định nghĩa CloudWatch Dashboards & Alarms
├── package.json
└── cdk.json
```

**Chi tiết các Stack tài nguyên chính:**

| CDK Stack | Dịch vụ AWS Triển khai | Vai trò đối với Hệ thống Web |
|---|---|---|
| **Storage Stack** | Amazon S3, DynamoDB | Lưu trữ tài nguyên Web, ảnh xe, dữ liệu dự báo và bảng dữ liệu DynamoDB |
| **API Stack** | API Gateway, AWS Lambda | Cung cấp backend REST APIs và logic nghiệp vụ cho Web App |
| **AppSync Stack** | AWS AppSync (GraphQL & WebSockets) | Cung cấp kết nối Socket thời gian thực cho Chatbox và Subscriptions |
| **IoT Stack** | AWS IoT Core, IoT Rules | Tiếp nhận kết nối MQTT từ ESP32 cảm biến đỗ xe |
| **Auth Stack** | Amazon Cognito, IAM Roles | Quản lý đăng ký/đăng nhập và xác thực token API cho Web User |
| **AI Chatbot Stack** | AWS Lambda | Cung cấp Trợ lý AI Chatbot tương tác tự động trên giao diện Web |
| **AI Forecast Stack** | AWS Lambda, DynamoDB | Chạy mô hình AI dự báo lưu lượng xe ra vào bãi trong 7 ngày tới |
| **Monitoring Stack** | CloudWatch, AWS Budgets | Giám sát trạng thái hoạt động, ghi log và quản lý ngân sách |

### 3.1.3. Dịch vụ AWS AppSync & WebSockets Chatbox Socket
AWS AppSync quản lý hạ tầng GraphQL API và kết nối WebSockets hai chiều cho khung Chatbox Socket:
* **Chatbox WebSockets Connection:** Kết nối Socket trực tiếp giữa giao diện Web Chatbox và AWS AppSync.
* **GraphQL Subscriptions:** Tự động phát tin nhắn hội thoại và đồng bộ trạng thái ô đỗ về trình duyệt người dùng theo thời gian thực mà không cần polling.

### 3.1.4. Hệ thống Lưu trữ Amazon S3 & CloudFront CDN
* **S3 Static Website Hosting:** Phân phối ứng dụng Web tĩnh qua Amazon CloudFront CDN (`https://d3imp0j8sdburp.cloudfront.net`).
* **S3 Vehicle Image Storage:** Lưu trữ ảnh xe chụp từ thiết bị ESP32-CAM tại cổng vào/ra qua Presigned URL.

### 3.1.5. Cơ sở Dữ liệu Amazon DynamoDB
Amazon DynamoDB là cơ sở dữ liệu NoSQL chính, lưu trữ các bảng dữ liệu:

| Tên Bảng DynamoDB | Partition Key | Sort Key | Chức năng trên Web Dashboard |
|---|---|---|---|
| `ParkingSlots` | `slot_id` (String) | - | Lưu trạng thái hiện tại (`available`/`occupied`) của từng chỗ đỗ xe |
| `VehicleLogs` | `log_id` (String) | `timestamp` (String) | Lưu nhật ký xe ra vào, biển số nhận diện và URL ảnh S3 |
| `TrafficForecasts` | `forecast_date` (String) | `slot_zone` (String) | Lưu dữ liệu mô hình AI dự báo lưu lượng xe trong 7 ngày tới |
| `ChatMessages` | `chat_id` (String) | `timestamp` (String) | Lưu nhật ký hội thoại Chatbox giữa người dùng và AI Chatbot |
| `Users` | `user_id` (String) | - | Lưu thông tin hồ sơ người dùng và cài đặt cá nhân |

### 3.1.6. Lớp Xử lý Serverless AWS Lambda Microservices
Hệ thống sử dụng các hàm AWS Lambda chuyên biệt:

| Hàm Lambda | Trigger (Sự kiện kích hoạt) | Chức năng nghiệp vụ |
|---|---|---|
| **Lambda API Backend** | Amazon API Gateway / AppSync Resolver | Phản hồi các truy vấn REST/GraphQL API từ giao diện Web App |
| **Lambda Presigned URL** | API Gateway (`GET /upload-url`) | Cấp presigned URL có thời hạn cho ESP32-CAM tải ảnh lên S3 |
| **Lambda Image Processing** | S3 `ObjectCreated` Event | Đọc ảnh từ S3, gọi Amazon Rekognition trích xuất biển số và lưu log |
| **Lambda Sensor Processing** | AWS IoT Core Rule (MQTT) | Tiếp nhận tin nhắn cảm biến đỗ xe, cập nhật DynamoDB và kích hoạt AppSync |
| **Lambda AI Chatbot** | AWS AppSync / API Gateway (`POST /chat`) | Trợ lý ảo Chatbot xử lý ngôn ngữ tự nhiên & trả lời thắc mắc |
| **Lambda AI 7-Day Forecast** | EventBridge Cron Scheduled / API Gateway | Phân tích chuỗi thời gian & dự báo lưu lượng xe 7 ngày tới cho Admin Dashboard |

### 3.1.7. Cổng Giao tiếp REST API Gateway & AppSync GraphQL
Hệ thống kết hợp song song API Gateway (cho REST APIs & Presigned URLs) và **AWS AppSync** (cho WebSockets Chatbox & GraphQL Subscriptions):
* **REST API Endpoint `/api/ai/forecast-7days`:** Trả về chuỗi dữ liệu dự báo mật độ xe 7 ngày tới cho biểu đồ trên Admin Dashboard.
* **AppSync GraphQL WebSockets Chatbox:** Phản hồi tin nhắn và phát sự kiện hội thoại qua Socket thời gian thực.

### 3.1.8. Quản lý Thiết bị AWS IoT Core
AWS IoT Core tiếp nhận mTLS MQTT telemetry từ ESP32 sensors, tự động cập nhật bảng `ParkingSlots` và đẩy tín hiệu tới AppSync Subscriptions.

### 3.1.9. Cấu hình Mạng & Bảo mật IAM
* Toàn bộ kênh kết nối CloudFront, API Gateway và AppSync WebSockets được mã hóa chuẩn TLS 1.3/HTTPS.
* Phân quyền IAM Least Privilege nghiêm ngặt cho từng hàm Lambda (ANPR, AI Chatbot, AI Forecast).

### 3.1.10. Kết luận
Hạ tầng cốt lõi AWS Serverless tích hợp **AWS AppSync WebSockets Chatbox**, **Lambda AI Chatbot** và **Lambda AI Dự báo Lưu lượng Xe 7 Ngày Tới** đã mang lại giải pháp Smart Parking IoT toàn diện, thông minh và tiên tiến.
