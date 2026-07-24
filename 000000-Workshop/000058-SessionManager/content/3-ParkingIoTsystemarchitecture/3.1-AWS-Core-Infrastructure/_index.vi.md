---
title : "AWS Core Infrastructure"
date: 2026-05-13
weight : 1
chapter : false
pre : " <b> 3.1. </b> "
---

Phần này trình bày toàn bộ kiến trúc và thiết lập cơ sở hạ tầng cốt lõi AWS đã được nhóm nghiên cứu, triển khai và đưa vào vận hành thực tế phục vụ **Nền tảng Web App Smart Parking IoT** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)). 

Cơ sở hạ tầng của hệ thống được xây dựng hoàn toàn theo mô hình **AWS Serverless**, tận dụng sức mạnh kết hợp của **Amazon S3, Amazon DynamoDB, AWS Lambda, Amazon API Gateway, AWS IoT Core, IAM, Amazon CloudFront, AWS WAF** và **Amazon CloudWatch**. Mô hình này cho phép Web App duy trì độ sẵn sàng cao, loại bỏ hoàn toàn gánh nặng quản lý máy chủ vật lý và tự động mở rộng (Auto-scaling) mượt mà khi lượng truy cập từ người dùng Web hoặc số lượng xe ra vào bãi tăng cao.

### 3.1.1. Mục tiêu & Vai trò Hạ tầng Đã Triển khai
Hạ tầng đám mây AWS cốt lõi đã hoàn thành tốt các nhiệm vụ chiến lược:

* **Phân phối Web App:** Phục vụ ứng dụng Web tĩnh lưu trữ trên Amazon S3, phân phối toàn cầu trực tiếp qua Amazon CloudFront CDN và bảo mật bằng AWS WAF.
* **Tích hợp Dữ liệu Biên:** Nhận ảnh xe ra/vào từ ESP32-CAM thông qua cơ chế S3 Presigned URL và tiếp nhận dữ liệu trạng thái chỗ đỗ qua giao thức MQTT gửi tới AWS IoT Core.
* **Xử lý Bất đồng bộ Không Máy chủ:** Kích hoạt chuỗi các hàm AWS Lambda để tự động hóa quy trình nhận diện biển số xe (ANPR với Amazon Rekognition), cập nhật trạng thái bãi xe và xử lý dịch vụ AI trên Lambda (Lambda AI Service).
* **Lưu trữ Dữ liệu Tốc độ Cao:** Lưu trữ toàn bộ nhật ký phương tiện, thông tin vị trí đỗ và dữ liệu người dùng trên Amazon DynamoDB với độ trễ phản hồi sub-millisecond.
* **Cung cấp RESTful API:** Mở các endpoint API bảo mật qua Amazon API Gateway tích hợp với Cognito Authorizer phục vụ giao diện Web App.
* **Bảo mật & Kiểm soát Vận hành:** Đảm bảo an toàn thông tin theo nguyên tắc Least Privilege thông qua IAM và theo dõi log/metric thời gian thực với Amazon CloudWatch.

### 3.1.2. Triển khai Hạ tầng bằng AWS CDK (Infrastructure as Code)
Toàn bộ tài nguyên trên AWS của hệ thống đã được định nghĩa và triển khai tự động bằng **AWS CDK (TypeScript)**. Phương pháp này đảm bảo tính nhất quán, khả năng tái triển khai và quản lý phiên bản hạ tầng chặt chẽ.

**Cấu trúc dự án CDK đã triển khai:**
```text
parking-iot-cdk/
├── bin/
│   └── parking-iot.ts            # Entry point khởi tạo các Stacks
├── lib/
│   ├── storage-stack.ts          # Định nghĩa S3 Buckets & DynamoDB Tables
│   ├── api-stack.ts              # Định nghĩa API Gateway & Lambda Backend
│   ├── iot-stack.ts              # Định nghĩa AWS IoT Core Rules & MQTT Topics
│   ├── auth-stack.ts             # Định nghĩa Cognito User Pools & Authorizers
│   ├── ai-stack.ts               # Định nghĩa AWS Lambda AI Service
│   └── monitoring-stack.ts       # Định nghĩa CloudWatch Dashboards & Alarms
├── package.json
└── cdk.json
```

**Chi tiết các Stack tài nguyên chính:**

| CDK Stack | Dịch vụ AWS Triển khai | Vai trò đối với Hệ thống Web |
|---|---|---|
| **Storage Stack** | Amazon S3, DynamoDB | Lưu trữ tài nguyên Web, ảnh xe và các bảng dữ liệu DynamoDB |
| **API Stack** | API Gateway, AWS Lambda | Cung cấp backend REST APIs và logic nghiệp vụ cho Web App |
| **IoT Stack** | AWS IoT Core, IoT Rules | Tiếp nhận kết nối MQTT từ ESP32 cảm biến đỗ xe |
| **Auth Stack** | Amazon Cognito, IAM Roles | Quản lý đăng ký/đăng nhập và xác thực token API cho Web User |
| **AI Stack** | AWS Lambda | Cung cấp dịch vụ Trợ lý AI tương tác trực tiếp trên giao diện Web |
| **Monitoring Stack** | CloudWatch, AWS Budgets | Giám sát trạng thái hoạt động, ghi log và quản lý ngân sách |

### 3.1.3. Hệ thống Lưu trữ Amazon S3 & CloudFront CDN
Amazon S3 được triển khai thực tế với hai phân hệ chính:

1. **S3 Static Website Hosting (Lưu trữ Giao diện Web App):**
   - Chứa toàn bộ mã nguồn Frontend đã build (HTML, CSS, JS, Assets).
   - Phân phối trực tiếp qua Amazon CloudFront CDN (URL `https://d3imp0j8sdburp.cloudfront.net`), hỗ trợ chứng chỉ HTTPS an toàn.
   - **Luồng truy cập Web:** `Người dùng → CloudFront CDN (AWS WAF) → Amazon S3 Bucket`.

2. **S3 Image Storage (Lưu trữ Hình ảnh Phương tiện):**
   - Lưu trữ trực tiếp ảnh xe chụp từ thiết bị ESP32-CAM đặt tại cổng vào/ra.
   - Sử dụng Presigned URL để thiết bị biên tải ảnh trực tiếp lên S3 mà không cần thông qua máy chủ trung gian.
   - **Luồng tải ảnh:** `ESP32-CAM → API Gateway → Lambda Presigned URL → Amazon S3 Bucket → Triggers S3 ObjectCreated Event`.

### 3.1.4. Cơ sở Dữ liệu Amazon DynamoDB
Amazon DynamoDB đóng vai trò là cơ sở dữ liệu NoSQL chính, được thiết kế tối ưu với chế độ On-Demand Capacity giúp đáp ứng mọi lưu lượng truy xuất thời gian thực từ Web App và IoT.

**Cấu trúc các Bảng dữ liệu chính:**

| Tên Bảng DynamoDB | Partition Key | Sort Key | Chức năng trên Web Dashboard |
|---|---|---|---|
| `ParkingSlots` | `slot_id` (String) | - | Lưu trạng thái hiện tại (`available`/`occupied`) của từng chỗ đỗ xe |
| `VehicleLogs` | `log_id` (String) | `timestamp` (String) | Lưu nhật ký xe ra vào, biển số nhận diện và URL ảnh S3 |
| `SensorData` | `device_id` (String) | `timestamp` (String) | Lưu dữ liệu thô (khoảng cách, dung lượng pin) từ các thiết bị cảm biến |
| `Users` | `user_id` (String) | - | Lưu thông tin hồ sơ người dùng và cài đặt cá nhân |

### 3.1.5. Lớp Xử lý Serverless AWS Lambda
Hệ thống sử dụng kiến trúc Microservices dựa trên các hàm AWS Lambda độc lập, đảm nhận từng công việc chuyên biệt:

| Hàm Lambda | Trigger (Sự kiện kích hoạt) | Chức năng nghiệp vụ |
|---|---|---|
| **Lambda API Backend** | Amazon API Gateway | Phản hồi các truy vấn REST API từ giao diện Web App |
| **Lambda Presigned URL** | API Gateway (`GET /upload-url`) | Cấp presigned URL có thời hạn cho ESP32-CAM tải ảnh lên S3 |
| **Lambda Image Processing** | S3 `ObjectCreated` Event | Đọc ảnh từ S3, gọi Amazon Rekognition trích xuất biển số và lưu log |
| **Lambda Sensor Processing** | AWS IoT Core Rule (MQTT) | Tiếp nhận tin nhắn cảm biến đỗ xe và cập nhật bảng `ParkingSlots` |
| **Lambda AI Service** | API Gateway (`POST /ai/chat`) | Thực thi mô hình AI xử lý ngôn ngữ tự nhiên & truy vấn đỗ xe thông minh |

### 3.1.6. Cổng Giao tiếp Amazon API Gateway
Amazon API Gateway được cấu hình làm cổng tiếp nhận mọi yêu cầu HTTPS từ Web App Frontend và thiết bị ESP32-CAM, tích hợp sẵn Amazon Cognito Authorizer để bảo mật API.

**Danh sách các API Endpoints chính trên hệ thống:**

| Phương thức | Endpoint Path | Quyền truy cập | Chức năng |
|---|---|---|---|
| `GET` | `/api/parking/slots` | Public / Authorized | Lấy sơ đồ và trạng thái tất cả vị trí đỗ xe |
| `GET` | `/api/vehicle/logs` | Cognito Authorized | Lấy danh sách lịch sử xe ra vào bãi |
| `GET` | `/api/vehicle/search` | Cognito Authorized | Tìm kiếm lịch sử theo biển số xe |
| `POST` | `/api/camera/presigned-url` | Device Authenticated | Tạo Presigned URL cho ESP32-CAM |
| `POST` | `/api/ai/chat` | Cognito Authorized | Gửi yêu cầu truy vấn đến Lambda AI Service |

### 3.1.7. Quản lý Thiết bị AWS IoT Core
AWS IoT Core quản lý toàn bộ kết nối và chứng chỉ bảo mật (X.509 Certificates) cho các thiết bị cảm biến ESP32 thông qua giao thức mỏng MQTT over TLS.

* **MQTT Topic trạng thái đỗ xe:** `parking/slots/{slot_id}/status`
* **Payload tin nhắn gửi từ ESP32:**
```json
{
  "device_id": "esp32_sensor_a01",
  "slot_id": "A01",
  "distance_cm": 25.4,
  "status": "occupied",
  "timestamp": "2026-05-13T09:15:30Z"
}
```
* **AWS IoT Rule:** Tự động lắng nghe trên topic `parking/slots/+/status` và kích hoạt hàm **Lambda Sensor Processing** để đồng bộ trạng thái lên Web Dashboard trong vòng vài miligiây.

### 3.1.8. Cấu hình Mạng & Bảo mật Mạng (Networking & Security)
Trong kiến trúc Serverless đã triển khai:
* Các dịch vụ managed như S3, DynamoDB, IoT Core, Rekognition, Lambda AI và CloudWatch được AWS quản lý theo vùng (Regional Services).
* Nhóm đã cấu hình **VPC Security Endpoints** và **Subnets riêng** cho các hàm Lambda đòi hỏi truy cập tài nguyên nội bộ nâng cao.
* **AWS WAF (Web Application Firewall):** Được gắn trực tiếp trước CloudFront distribution để lọc các truy vấn xấu, chống tấn công SQL Injection, XSS và giới hạn tần suất yêu cầu (Rate Limiting).

### 3.1.9. Phân quyền IAM (Identity & Access Management)
Mọi tài nguyên AWS trong hệ thống đều tuân thủ nghiêm ngặt nguyên tắc **Đặc quyền Tối thiểu (Least Privilege)**:
* **Role Lambda Image Processing:** Chỉ có quyền `s3:GetObject` trên bucket ảnh, `rekognition:DetectText` và `dynamodb:PutItem` trên bảng `VehicleLogs`.
* **Role Lambda Sensor Processing:** Chỉ có quyền `dynamodb:UpdateItem` trên bảng `ParkingSlots`.
* **Role Lambda AI Service:** Được cấp quyền đọc bảng DynamoDB để tổng hợp dữ liệu đỗ xe và trả lời truy vấn.
* **Role API Gateway:** Chỉ có quyền `lambda:InvokeFunction` tới các hàm Lambda backend tương ứng.

### 3.1.10. Kết luận
Hạ tầng cốt lõi AWS Serverless là xương sống vững chắc giúp **Nền tảng Web App Smart Parking IoT** vận hành ổn định, mượt mà và an toàn trên môi trường thực tế. Sự kết hợp nhuần nhuyễn giữa hạ tầng IaC (AWS CDK), lưu trữ đám mây (S3, DynamoDB), xử lý không máy chủ (Lambda, Rekognition, Lambda AI Service) và phân phối CDN (CloudFront, WAF) đã tạo nên một giải pháp đỗ xe thông minh toàn diện, sẵn sàng mở rộng quy mô sản xuất.
