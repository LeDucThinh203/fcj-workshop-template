---
title : "AWS Core Infrastructure"
date: 2026-05-13
weight : 1
chapter : false
pre : " <b> 3.1. </b> "
---

Phần này trình bày quá trình thiết lập cơ sở hạ tầng cốt lõi của AWS cho Hệ thống IoT Bãi đỗ xe Thông minh. Cơ sở hạ tầng cốt lõi bao gồm các dịch vụ chính như Amazon S3, Amazon DynamoDB, AWS Lambda, Amazon API Gateway, AWS IoT Core, IAM, CloudFront, WAF và CloudWatch.

Hệ thống được xây dựng theo mô hình AWS Serverless, giúp giảm bớt nhu cầu quản lý máy chủ và cho phép hệ thống mở rộng dễ dàng khi số lượng thiết bị ESP32, camera, cảm biến hoặc người dùng Web/App tăng lên.

### 3.1.1. Mục tiêu của Cơ sở hạ tầng cốt lõi
Cơ sở hạ tầng cốt lõi AWS được thiết kế để đạt được các mục tiêu sau:

* Cung cấp môi trường lưu trữ dữ liệu tập trung cho hệ thống Parking IoT.
* Cho phép ESP32 Camera tải hình ảnh xe lên Amazon S3.
* Cho phép cảm biến ESP32 gửi dữ liệu trạng thái chỗ đỗ xe đến AWS IoT Core.
* Xử lý dữ liệu bằng AWS Lambda mà không cần quản lý máy chủ.
* Lưu trữ thông tin xe, dữ liệu biển số và trạng thái chỗ đỗ xe trong DynamoDB.
* Cung cấp các API cho Web/App thông qua Amazon API Gateway.
* Đảm bảo an ninh sử dụng IAM, Cognito và WAF.
* Theo dõi logs, lỗi và hiệu suất hệ thống bằng Amazon CloudWatch.

### 3.1.2. Khởi tạo dự án AWS CDK
AWS CDK được sử dụng để quản lý cơ sở hạ tầng dưới dạng mã (Infrastructure as Code - IaC). Thay vì tạo thủ công từng dịch vụ trên AWS Console, nhóm có thể định nghĩa các tài nguyên AWS bằng code và triển khai chúng tự động.

Các nhiệm vụ chính bao gồm:

* Cài đặt Node.js và AWS CDK CLI.
* Cấu hình AWS CLI với tài khoản AWS.
* Khởi tạo dự án CDK bằng TypeScript hoặc Python.
* Tạo các stack cho các nhóm tài nguyên khác nhau.
* Triển khai cơ sở hạ tầng lên AWS bằng các lệnh CDK.

**Cấu trúc dự án mẫu:**
```text
parking-iot-cdk/
├── bin/
│   └── parking-iot.ts
├── lib/
│   ├── storage-stack.ts
│   ├── api-stack.ts
│   ├── iot-stack.ts
│   ├── auth-stack.ts
│   └── monitoring-stack.ts
├── package.json
└── cdk.json
```

**Các stack chính có thể được tổ chức như sau:**

| Stack | Chức năng |
|-------|----------|
| Storage Stack | Tạo S3 Bucket và các bảng DynamoDB |
| API Stack | Tạo API Gateway và Lambda Backend |
| IoT Stack | Tạo IoT Core Rule và Lambda xử lý cảm biến |
| Auth Stack | Tạo Cognito User Pool |
| Monitoring Stack | Tạo CloudWatch Logs và cảnh báo |

Việc sử dụng AWS CDK giúp quá trình triển khai có thể lặp lại, dễ dàng sửa đổi và quản lý thông qua quản lý phiên bản (version control).

### 3.1.3. Thiết lập Amazon S3
Amazon S3 được sử dụng cho hai mục đích chính trong hệ thống Parking IoT:
* Lưu trữ giao diện tĩnh của Web/App (Static Website Hosting).
* Lưu trữ hình ảnh xe gửi từ ESP32 Camera.

**S3 Static Website**
Giao diện Web/App có thể được build thành các tệp HTML, CSS và JavaScript và tải lên S3 Bucket. Sau đó, CloudFront sẽ phân phối nội dung trang web đến người dùng.

Luồng truy cập trang web:
`Người dùng → Route 53 → CloudFront → S3 Static Website`

**S3 để lưu trữ hình ảnh xe**
Khi ESP32 Camera chụp ảnh một chiếc xe đi vào hoặc đi ra khỏi bãi đỗ xe, thiết bị sẽ yêu cầu một Presigned URL từ API Gateway. Sau đó, ESP32 Camera tải hình ảnh trực tiếp lên Amazon S3.

Luồng tải hình ảnh:
`ESP32 Camera → API Gateway → Lambda tạo Presigned URL → Amazon S3`

Sau khi hình ảnh được tải lên thành công, S3 sẽ tạo ra một sự kiện ObjectCreated để kích hoạt hàm Lambda xử lý hình ảnh.
`Amazon S3 → Sự kiện S3 ObjectCreated → Lambda xử lý hình ảnh`

### 3.1.4. Thiết lập Amazon DynamoDB
Amazon DynamoDB được sử dụng làm cơ sở dữ liệu chính của hệ thống. Dữ liệu được lưu trữ dưới định dạng NoSQL, phù hợp với các hệ thống IoT yêu cầu ghi nhanh và truy vấn theo thời gian thực.

Các bảng dữ liệu chính bao gồm:

| Tên Bảng | Chức năng |
|------------|----------|
| ParkingSlots | Lưu trạng thái của từng chỗ đỗ xe |
| VehicleLogs | Lưu lịch sử xe ra vào |
| SensorData | Lưu dữ liệu cảm biến |
| Users | Lưu thông tin người dùng nếu cần |

**Dữ liệu mẫu cho bảng ParkingSlots:**
```json
{
  "slot_id": "A01",
  "status": "occupied",
  "updated_at": "2026-04-27T10:30:00"
}
```

**Dữ liệu mẫu cho bảng VehicleLogs:**
```json
{
  "log_id": "LOG001",
  "plate_number": "51A-12345",
  "direction": "in",
  "image_url": "s3://parking-image-bucket/car_001.jpg",
  "timestamp": "2026-04-27T10:30:00"
}
```

DynamoDB giúp hệ thống truy xuất nhanh chóng trạng thái chỗ đỗ xe, lịch sử ra vào và kết quả nhận dạng biển số xe.

### 3.1.5. Thiết lập AWS Lambda
AWS Lambda là thành phần xử lý chính của hệ thống. Lambda cho phép code chạy khi có sự kiện xảy ra mà không cần triển khai hoặc quản lý máy chủ riêng.

Các hàm Lambda chính bao gồm:

| Hàm Lambda | Chức năng |
|-----------------|----------|
| Lambda API Backend | Xử lý các yêu cầu từ Web/App |
| Lambda Presigned URL | Tạo Presigned URL cho ESP32 Camera tải hình ảnh lên |
| Lambda Image Processing | Xử lý hình ảnh khi có hình ảnh mới tải lên S3 |
| Lambda Sensor Processing | Xử lý dữ liệu cảm biến từ AWS IoT Core |
| Lambda AI Service | Kết nối với Amazon Bedrock cho các tính năng AI |

**Luồng Lambda xử lý hình ảnh:**
`S3 ObjectCreated → Lambda Image Processing → Amazon Rekognition → DynamoDB`

**Luồng Lambda xử lý cảm biến:**
`AWS IoT Core → IoT Rule → Lambda Sensor Processing → DynamoDB`

Lambda cho phép hệ thống hoạt động linh hoạt, chỉ chạy khi có sự kiện và tự động mở rộng (scale) dựa trên số lượng yêu cầu.

### 3.1.6. Thiết lập Amazon API Gateway
Amazon API Gateway được sử dụng làm cổng giao tiếp giữa Web/App, ESP32 Camera và các hàm Lambda.

Các API chính có thể bao gồm:

| API Endpoint | Chức năng |
|--------------|----------|
| `/parking/slots` | Lấy trạng thái chỗ đỗ xe |
| `/vehicle/logs` | Lấy lịch sử xe ra vào |
| `/upload-url` | Tạo Presigned URL cho ESP32 Camera |
| `/ai/query` | Gửi câu hỏi đến AI Service |

**Luồng yêu cầu API từ Web/App:**
`Web/App → API Gateway → Lambda Backend → DynamoDB`

**Luồng yêu cầu Presigned URL từ ESP32 Camera:**
`ESP32 Camera → API Gateway → Lambda Presigned URL → Amazon S3`

API Gateway giúp hệ thống quản lý các yêu cầu một cách tập trung, kiểm soát truy cập dễ dàng hơn và tích hợp với Cognito Authorizer.

### 3.1.7. Thiết lập AWS IoT Core
AWS IoT Core được sử dụng để nhận dữ liệu từ cảm biến ESP32 thông qua giao thức MQTT.

Cảm biến ESP32 gửi dữ liệu trạng thái chỗ đỗ xe đến một MQTT topic, ví dụ:
`parking/slot/A01/status`

**Payload mẫu:**
```json
{
  "slot_id": "A01",
  "status": "available",
  "timestamp": "2026-04-27T10:30:00"
}
```

**Luồng dữ liệu cảm biến:**
`Cảm biến ESP32 → AWS IoT Core → IoT Rule → Lambda Sensor Processing → DynamoDB`

AWS IoT Core giúp quản lý kết nối thiết bị, chứng chỉ bảo mật và dữ liệu MQTT từ các thiết bị IoT.

### 3.1.8. Thiết lập VPC và Mạng (Networking)
Trong hệ thống Parking IoT sử dụng kiến trúc serverless, hầu hết các dịch vụ như S3, DynamoDB, IoT Core, Rekognition, Bedrock và CloudWatch đều là các dịch vụ AWS quản lý (managed services) và không được đặt trực tiếp bên trong VPC.

Tuy nhiên, có thể cấu hình một VPC nếu hệ thống cần:
* Chạy các hàm Lambda bên trong một mạng riêng (private network).
* Kết nối với một cơ sở dữ liệu nội bộ.
* Cô lập các thành phần backend.
* Cải thiện kiểm soát lưu lượng mạng.

Một VPC cơ bản có thể bao gồm:

| Thành phần | Chức năng |
|-----------|----------|
| Public Subnet | Sử dụng cho các tài nguyên cần truy cập Internet |
| Private Subnet | Sử dụng cho Lambda hoặc tài nguyên nội bộ |
| Internet Gateway | Cho phép truy cập Internet từ Public Subnet |
| NAT Gateway | Cho phép tài nguyên trong Private Subnet truy cập Internet |
| Security Group | Kiểm soát lưu lượng mạng vào/ra (inbound/outbound) |

> **Lưu ý:** Trong sơ đồ kiến trúc, các dịch vụ như S3, DynamoDB, CloudWatch, Rekognition và Bedrock không nên được đặt bên trong VPC vì chúng là các dịch vụ khu vực (regional services) do AWS quản lý.

### 3.1.9. Cấu hình IAM Roles và Policies
IAM được sử dụng để quản lý quyền truy cập cho các dịch vụ AWS. Hệ thống áp dụng nguyên tắc Đặc quyền Tối thiểu (Least Privilege), nghĩa là mỗi dịch vụ chỉ được cấp những quyền tối thiểu cần thiết để thực hiện nhiệm vụ của nó.

Một số quyền (permissions) cần thiết bao gồm:

| Thành phần | Quyền cần thiết |
|-----------|---------------------|
| Lambda API Backend | Đọc và ghi dữ liệu trong DynamoDB |
| Lambda Presigned URL | Tạo Presigned URL để tải hình ảnh lên S3 |
| Lambda Image Processing | Đọc hình ảnh từ S3, gọi Rekognition và ghi dữ liệu vào DynamoDB |
| Lambda Sensor Processing | Ghi dữ liệu cảm biến vào DynamoDB |
| Lambda AI Service | Gọi Bedrock và đọc dữ liệu từ DynamoDB |
| API Gateway | Gọi (Invoke) các hàm Lambda |
| IoT Rule | Kích hoạt (Trigger) hàm Lambda xử lý cảm biến |

Việc quản lý quyền rõ ràng giúp cải thiện bảo mật hệ thống, tránh cấp quyền quá rộng và giảm thiểu rủi ro bảo mật.

### 3.1.10. Kết luận
Cơ sở hạ tầng cốt lõi AWS là nền tảng quan trọng cho sự vận hành ổn định của hệ thống Parking IoT. Các dịch vụ như S3, DynamoDB, Lambda, API Gateway và IoT Core xử lý việc lưu trữ, xử lý dữ liệu và giao tiếp giữa các thiết bị ESP32 và Web/App.

Bên cạnh đó, IAM kiểm soát quyền truy cập, CloudWatch hỗ trợ giám sát hệ thống và CDK giúp triển khai cơ sở hạ tầng tự động, quản lý dễ dàng hơn. Với kiến trúc serverless, hệ thống có thể mở rộng linh hoạt, tối ưu hóa chi phí và đáp ứng các yêu cầu của mô hình Smart Parking IoT.
