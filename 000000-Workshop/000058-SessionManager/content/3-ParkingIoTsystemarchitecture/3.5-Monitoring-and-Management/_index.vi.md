---
title : "Monitoring and Management"
date: 2026-05-13
weight : 5
chapter : false
pre : " <b> 3.5. </b> "
---

Phần này mô tả cách giám sát, ghi log, phát hiện lỗi và quản lý Hệ thống IoT Bãi đỗ xe Thông minh sau khi triển khai. Vì hệ thống sử dụng nhiều dịch vụ AWS như Lambda, API Gateway, AWS IoT Core, Amazon S3, Amazon DynamoDB, Amazon Rekognition và Amazon Bedrock, việc giám sát là rất quan trọng để đảm bảo hoạt động ổn định, phát hiện lỗi kịp thời và kiểm soát chi phí.

Các dịch vụ chính được sử dụng cho giám sát và quản lý bao gồm:
* Amazon CloudWatch: ghi nhận logs, giám sát lỗi và theo dõi hiệu suất hệ thống.
* AWS Budgets: giám sát chi phí AWS và gửi cảnh báo chi phí.
* AWS CloudTrail: ghi lại các hoạt động và thao tác trong tài khoản AWS.
* IAM: quản lý quyền truy cập và quản trị bảo mật.
* DynamoDB Console / S3 Console: kiểm tra dữ liệu lưu trữ và tài nguyên lưu trữ.

### 3.5.1. Mục tiêu Giám sát Hệ thống
Việc giám sát hệ thống đảm bảo rằng tất cả các thành phần trong kiến trúc Parking IoT hoạt động đúng cách, dữ liệu được xử lý chính xác và quản trị viên có thể phát hiện sự cố kịp thời.

Các mục tiêu chính bao gồm:
* Giám sát trạng thái hoạt động của các hàm Lambda.
* Kiểm tra các yêu cầu từ Web/App đến API Gateway.
* Giám sát dữ liệu gửi từ cảm biến ESP32 đến AWS IoT Core.
* Kiểm tra quá trình tải hình ảnh từ ESP32 Camera lên Amazon S3.
* Giám sát quá trình xử lý hình ảnh và nhận diện biển số xe.
* Kiểm tra xem dữ liệu có được ghi vào DynamoDB chính xác không.
* Phát hiện lỗi trong quá trình xử lý dữ liệu.
* Giám sát chi phí AWS để tránh vượt quá ngân sách.
* Theo dõi các hoạt động của người dùng và dịch vụ trong tài khoản AWS.

### 3.5.2. Giám sát với Amazon CloudWatch
Amazon CloudWatch là dịch vụ chính được sử dụng để ghi log và giám sát các hoạt động của hệ thống. Các dịch vụ như Lambda, API Gateway, AWS IoT Core và DynamoDB có thể gửi log hoặc metrics (chỉ số) đến CloudWatch.

**Luồng giám sát tổng quát:**
`API Gateway / Lambda / AWS IoT Core / DynamoDB / Rekognition → Amazon CloudWatch`

CloudWatch hỗ trợ:
* Ghi log các lần thực thi Lambda.
* Ghi log các yêu cầu từ API Gateway.
* Giám sát các lỗi xử lý của Lambda.
* Theo dõi thời gian thực thi (duration) của Lambda.
* Giám sát số lượng yêu cầu API.
* Kiểm tra lỗi khi ghi dữ liệu vào DynamoDB.
* Tạo cảnh báo (alarms) khi hệ thống có hành vi bất thường.

**Ví dụ về các log cần giám sát:**

| Thành phần | Thông tin cần giám sát |
|-----------|------------------------|
| Lambda Backend | Yêu cầu từ Web/App và lỗi xử lý API |
| Lambda Image Processing | Lỗi đọc ảnh S3 và lỗi Rekognition |
| Lambda Sensor Processing | Payload MQTT và lỗi ghi DynamoDB |
| API Gateway | Yêu cầu, phản hồi và lỗi 4xx/5xx |
| AWS IoT Core | Dữ liệu MQTT từ các thiết bị ESP32 |
| DynamoDB | Lỗi truy vấn hoặc ghi dữ liệu |

### 3.5.3. Giám sát AWS Lambda
AWS Lambda là thành phần xử lý chính của hệ thống, vì vậy các hàm Lambda phải được giám sát cẩn thận để đảm bảo hoạt động ổn định.

Các hàm Lambda cần được giám sát bao gồm:

| Hàm Lambda | Chức năng |
|-----------------|----------|
| Lambda API Backend | Xử lý các yêu cầu từ Web/App |
| Lambda Presigned URL | Tạo URL tải lên cho ESP32 Camera |
| Lambda Image Processing | Xử lý hình ảnh và gọi Rekognition |
| Lambda Sensor Processing | Xử lý dữ liệu cảm biến từ AWS IoT Core |
| Lambda AI Service | Kết nối đến Amazon Bedrock cho các truy vấn AI |

**Các chỉ số (metrics) quan trọng cần giám sát:**
* Invocations: số lần Lambda được gọi.
* Errors: số lỗi thực thi Lambda.
* Duration: thời gian thực thi Lambda.
* Throttles: số lần Lambda bị giới hạn (throttle).
* Memory Usage: mức sử dụng bộ nhớ.
* Timeout: lỗi do Lambda chạy lâu hơn thời gian timeout đã cấu hình.

**Luồng kiểm tra lỗi Lambda mẫu:**
`CloudWatch → Log Groups → Chọn Hàm Lambda → Xem Log Stream → Kiểm tra lỗi`

Khi phát hiện lỗi, quản trị viên nên kiểm tra chi tiết log để xác định nguyên nhân, chẳng hạn như lỗi quyền IAM, dữ liệu đầu vào không hợp lệ, sự cố kết nối DynamoDB hoặc lỗi gọi Rekognition.

### 3.5.4. Giám sát Amazon API Gateway
Amazon API Gateway là cổng giao tiếp giữa Web/App, ESP32 Camera và Lambda Backend. Nếu API Gateway gặp sự cố, người dùng hoặc thiết bị IoT có thể không gửi được yêu cầu đến hệ thống.

**Các thành phần cần giám sát bao gồm:**
* Số lượng yêu cầu đến API.
* Tỷ lệ yêu cầu thành công.
* Lỗi 4xx do yêu cầu không hợp lệ hoặc thiếu quyền.
* Lỗi 5xx do lỗi từ Lambda Backend.
* Thời gian phản hồi của API.
* Các yêu cầu từ Web/App và ESP32 Camera.

**Các lỗi API phổ biến:**

| Mã lỗi | Ý nghĩa |
|------------|---------|
| 400 | Định dạng yêu cầu không hợp lệ |
| 401 | Yêu cầu chưa được xác thực |
| 403 | Truy cập bị từ chối |
| 404 | Sai endpoint |
| 500 | Lỗi Lambda Backend |
| 504 | Hết thời gian yêu cầu (Request timeout) |

**Luồng giám sát API:**
`API Gateway → CloudWatch Logs → Kiểm tra Yêu cầu và Phản hồi`

Giám sát API Gateway giúp phát hiện các vấn đề kết nối giữa giao diện Web/App và hệ thống backend.

### 3.5.5. Giám sát AWS IoT Core
AWS IoT Core được sử dụng để nhận dữ liệu từ cảm biến ESP32 thông qua MQTT. Do đó, quá trình gửi dữ liệu từ thiết bị lên AWS phải được giám sát.

**Các mục cần kiểm tra bao gồm:**
* ESP32 có thể kết nối với AWS IoT Core hay không.
* Topic MQTT có đúng định dạng không.
* Payload có chứa đầy đủ dữ liệu không.
* IoT Rule có kích hoạt Lambda chính xác không.
* Lambda có ghi dữ liệu vào DynamoDB thành công không.

**Topic MQTT mẫu:**
`parking/slot/A01/status`

**Payload hợp lệ mẫu:**
```json
{
  "device_id": "esp32_sensor_01",
  "slot_id": "A01",
  "status": "occupied",
  "timestamp": "2026-04-27T10:30:00"
}
```

**Các lỗi phổ biến trong luồng IoT:**

| Lỗi | Nguyên nhân có thể |
|-------|----------------|
| Thiết bị không thể kết nối | Sai endpoint, lỗi chứng chỉ hoặc mất kết nối WiFi |
| Không nhận được dữ liệu | Sai topic MQTT hoặc thiết bị không gửi dữ liệu |
| IoT Rule không kích hoạt | Điều kiện rule sai hoặc thiếu quyền gọi Lambda |
| Lambda không ghi được vào DynamoDB | Thiếu quyền IAM hoặc định dạng dữ liệu không hợp lệ |

**Luồng giám sát dữ liệu cảm biến:**
`ESP32 Sensor → AWS IoT Core → IoT Rule → Lambda → CloudWatch Logs`

### 3.5.6. Giám sát Amazon S3 và Xử lý Hình ảnh
Amazon S3 được sử dụng để lưu trữ hình ảnh xe từ ESP32 Camera. Khi có hình ảnh mới được tải lên, S3 tạo ra sự kiện ObjectCreated để kích hoạt hàm Lambda xử lý hình ảnh.

**Luồng xử lý hình ảnh:**
`ESP32 Camera → Amazon S3 → Sự kiện S3 ObjectCreated → Lambda Image Processing → Rekognition → DynamoDB`

**Các mục cần kiểm tra bao gồm:**
* Hình ảnh có được tải lên S3 thành công không.
* Hình ảnh có được lưu đúng vào thư mục `entrance/` hoặc `exit/` không.
* Sự kiện S3 ObjectCreated có kích hoạt Lambda không.
* Lambda có đọc được hình ảnh từ S3 không.
* Lambda có gọi Rekognition thành công không.
* Kết quả nhận diện có được ghi vào DynamoDB không.

**Cấu trúc thư mục hình ảnh S3 mẫu:**
```text
parking-image-bucket/
├── entrance/
│   └── esp32_cam_01_20260427_103000.jpg
└── exit/
    └── esp32_cam_02_20260427_110000.jpg
```

**Các lỗi phổ biến:**

| Lỗi | Cách kiểm tra |
|-------|--------------|
| Tải ảnh thất bại | Kiểm tra Presigned URL và quyền S3 |
| S3 không kích hoạt Lambda | Kiểm tra S3 Event Notification |
| Lambda không thể đọc ảnh | Kiểm tra quyền IAM của Lambda Role |
| Lỗi Rekognition | Kiểm tra định dạng ảnh và quyền Rekognition |
| Kết quả không được lưu | Kiểm tra quyền ghi DynamoDB |

### 3.5.7. Giám sát Amazon DynamoDB
Amazon DynamoDB là dịch vụ lưu trữ dữ liệu chính của hệ thống. Các dữ liệu như trạng thái chỗ đỗ xe, lịch sử xe ra vào và kết quả nhận diện biển số đều được lưu trữ tại đây.

**Các bảng cần giám sát:**

| Bảng | Dữ liệu lưu trữ |
|-------|-------------|
| ParkingSlots | Trạng thái mới nhất của từng chỗ đỗ xe |
| VehicleLogs | Lịch sử xe ra vào |
| SensorData | Dữ liệu cảm biến theo thời gian |
| DeviceStatus | Trạng thái hoạt động của thiết bị (nếu có) |

**Các mục cần kiểm tra bao gồm:**
* Dữ liệu có được ghi vào đúng bảng không.
* Trạng thái chỗ đỗ xe có được cập nhật giá trị mới nhất không.
* Dữ liệu xe ra vào có chứa biển số, thời gian và thông tin ảnh không.
* Lambda có bị lỗi khi ghi dữ liệu không.
* Thiết kế khóa chính (primary key) và truy vấn có cần tối ưu không.

**Dữ liệu mẫu trong bảng ParkingSlots:**
```json
{
  "slot_id": "A01",
  "status": "occupied",
  "updated_at": "2026-04-27T10:30:00",
  "device_id": "esp32_sensor_01"
}
```

**Dữ liệu mẫu trong bảng VehicleLogs:**
```json
{
  "log_id": "LOG001",
  "plate_number": "51A-12345",
  "direction": "in",
  "image_url": "s3://parking-image-bucket/entrance/car_001.jpg",
  "timestamp": "2026-04-27T10:30:00",
  "confidence": 92.5
}
```

### 3.5.8. Giám sát Amazon Rekognition và AI Service
Amazon Rekognition được dùng để phân tích hình ảnh xe và hỗ trợ nhận diện biển số. Amazon Bedrock có thể được dùng cho AI Service, cho phép người dùng truy vấn dữ liệu đỗ xe bằng ngôn ngữ tự nhiên.

**Giám sát Rekognition**
Các mục cần kiểm tra bao gồm:
* Rekognition có được gọi thành công bởi Lambda không.
* Hình ảnh đầu vào có đúng định dạng không.
* Kết quả nhận diện có độ tin cậy (confidence score) cao không.
* Các trường hợp nhận diện lỗi có được log lại không.

**Kết quả nhận diện mẫu:**
```json
{
  "plate_number": "51A-12345",
  "confidence": 92.5,
  "status": "recognized"
}
```

**Giám sát AI Service**
Luồng AI Service:
`Web/App → API Gateway → Lambda AI Service → DynamoDB → Amazon Bedrock → Web/App`

Các mục cần kiểm tra bao gồm:
* Người dùng có gửi được câu hỏi thành công không.
* Lambda AI Service có lấy được dữ liệu từ DynamoDB không.
* Amazon Bedrock có trả về câu trả lời hợp lý không.
* Thời gian phản hồi có quá lâu không.
* Chi phí có bị đội lên do có quá nhiều yêu cầu AI không.

### 3.5.9. Cảnh báo Lỗi với CloudWatch Alarm
CloudWatch Alarm được sử dụng để gửi cảnh báo khi hệ thống có dấu hiệu bất thường. Cảnh báo giúp quản trị viên phát hiện sớm các sự cố và phản hồi nhanh chóng.

**Các cảnh báo (alarms) đề xuất:**

| Dịch vụ | Điều kiện Cảnh báo |
|---------|-----------------|
| Lambda | Lỗi (Errors) lớn hơn 0 trong vòng 5 phút |
| API Gateway | Tỷ lệ lỗi 5xx cao |
| IoT Core | Không nhận được dữ liệu từ thiết bị trong thời gian dài |
| DynamoDB | Lỗi ghi dữ liệu |
| CloudWatch Logs | Xuất hiện các log lỗi nghiêm trọng (critical) |
| AWS Budgets | Chi phí vượt ngưỡng cho phép |

**Cảnh báo Lambda mẫu:**
* Nếu `Lambda Image Processing` có `Errors > 0` trong vòng 5 phút → gửi cảnh báo cho quản trị viên.

Cảnh báo có thể được gửi qua:
* Email.
* Amazon SNS.
* Bảng điều khiển quản trị (Admin dashboard).
* Thông báo CloudWatch Alarm.

### 3.5.10. Quản lý Chi phí với AWS Budgets
AWS Budgets được sử dụng để theo dõi chi phí AWS và gửi cảnh báo khi chi phí vượt quá mức xác định. Điều này rất quan trọng vì các dịch vụ như Rekognition, Bedrock, S3, API Gateway và CloudWatch có thể phát sinh phí khi sử dụng thường xuyên.

**Các dịch vụ cần được giám sát chi phí:**
* Amazon S3.
* AWS Lambda.
* Amazon API Gateway.
* AWS IoT Core.
* Amazon DynamoDB.
* Amazon Rekognition.
* Amazon Bedrock.
* Amazon CloudWatch.
* Amazon CloudFront.

**Cấu hình ngân sách mẫu:**
* Ngân sách hàng tháng: 10 USD
* Cảnh báo 1: Khi chi phí đạt 50%
* Cảnh báo 2: Khi chi phí đạt 80%
* Cảnh báo 3: Khi chi phí đạt 100%

**Lợi ích của AWS Budgets:**
* Tránh các chi phí ngoài dự kiến.
* Theo dõi mức chi tiêu hàng tháng.
* Phát hiện các dịch vụ đang bị lạm dụng hoặc dùng quá nhiều.
* Hỗ trợ quản lý ngân sách cho các môi trường demo hoặc học tập.

### 3.5.11. Quản lý Bảo mật với IAM và CloudTrail
IAM và CloudTrail giúp quản trị viên kiểm soát quyền truy cập và theo dõi các hoạt động trong tài khoản AWS.

**IAM**
IAM được dùng để quản lý quyền truy cập giữa các dịch vụ AWS. Hệ thống nên áp dụng nguyên tắc Đặc quyền Tối thiểu (Least Privilege), nghĩa là mỗi thành phần chỉ có các quyền mà nó thực sự cần.

**Quyền truy cập mẫu:**

| Thành phần | Quyền cần thiết |
|-----------|---------------------|
| Lambda Image Processing | Đọc S3, gọi Rekognition, ghi DynamoDB |
| Lambda Sensor Processing | Ghi DynamoDB |
| Lambda AI Service | Đọc DynamoDB, gọi Bedrock |
| API Gateway | Gọi (Invoke) Lambda |
| IoT Rule | Kích hoạt (Trigger) Lambda |

**CloudTrail**
AWS CloudTrail ghi lại các hoạt động trong tài khoản AWS, chẳng hạn như:
* Ai đã tạo hoặc xóa một hàm Lambda.
* Ai đã thay đổi IAM Policy.
* Ai đã tạo một S3 Bucket.
* Ai đã đổi cấu hình API Gateway.
* Ai đã truy cập hoặc chỉnh sửa các tài nguyên quan trọng.

CloudTrail tăng cường tính minh bạch và hỗ trợ điều tra khi có sự cố bảo mật xảy ra.

### 3.5.12. Bảng điều khiển (Dashboard) Quản trị Hệ thống
Quản trị viên có thể xây dựng một dashboard để giám sát toàn bộ hệ thống Parking IoT.

Thông tin cần hiển thị trên dashboard bao gồm:
* Tổng số chỗ đỗ xe.
* Số chỗ còn trống.
* Số chỗ đã có xe.
* Số lượt xe vào hôm nay.
* Số lượt xe ra hôm nay.
* Danh sách các lỗi gần đây.
* Trạng thái các thiết bị ESP32.
* Số lượng ảnh đã tải lên S3.
* Số lượng lỗi Lambda.
* Chi phí AWS hiện tại.

**Các chỉ số trên dashboard mẫu:**

| Chỉ số | Ý nghĩa |
|--------|---------|
| Total Slots | Tổng số chỗ đỗ xe |
| Available Slots | Số chỗ đỗ trống |
| Occupied Slots | Số chỗ đã có xe |
| Today Entries | Số lượt xe vào trong ngày |
| Today Exits | Số lượt xe ra trong ngày |
| Active Devices | Số lượng thiết bị đang hoạt động |
| Lambda Errors | Số lỗi Lambda |
| Current AWS Cost | Chi phí sử dụng AWS hiện tại |

Dashboard giúp quản trị viên giám sát hệ thống nhanh chóng mà không cần phải vào kiểm tra từng dịch vụ AWS riêng lẻ.

### 3.5.13. Quy trình Xử lý Sự cố (Troubleshooting)
Khi hệ thống gặp lỗi, quản trị viên nên tuân theo quy trình kiểm tra từng lớp (layer-by-layer) để tìm ra nguyên nhân.

**Quy trình xử lý sự cố mẫu khi Web/App không hiển thị dữ liệu:**
`Web/App → API Gateway → Lambda Backend → DynamoDB → CloudWatch Logs`

**Các bước kiểm tra:**
1. Kiểm tra xem Web/App có gọi đúng API không.
2. Kiểm tra xem API Gateway có nhận được yêu cầu không.
3. Kiểm tra xem Lambda Backend có được kích hoạt không.
4. Kiểm tra xem Lambda có lỗi trong CloudWatch không.
5. Kiểm tra xem DynamoDB có chứa dữ liệu không.
6. Kiểm tra quyền IAM của Lambda.
7. Kiểm tra kết quả phản hồi trả về cho Web/App.

**Quy trình xử lý sự cố mẫu khi Cảm biến ESP32 không cập nhật trạng thái:**
`ESP32 Sensor → AWS IoT Core → IoT Rule → Lambda Sensor Processing → DynamoDB`

**Các bước kiểm tra:**
1. Kiểm tra xem ESP32 có kết nối WiFi không.
2. Kiểm tra xem thiết bị có kết nối AWS IoT Core không.
3. Kiểm tra topic MQTT có đúng không.
4. Kiểm tra IoT Rule có được kích hoạt không.
5. Kiểm tra Lambda Sensor Processing có log lỗi không.
6. Kiểm tra DynamoDB có được cập nhật không.

### 3.5.14. Kết luận
Phần giám sát và quản lý giúp hệ thống Parking IoT hoạt động ổn định, dễ dàng phát hiện lỗi và kiểm soát chi phí AWS. Amazon CloudWatch được sử dụng để thu thập logs và giám sát các thành phần quan trọng như Lambda, API Gateway, IoT Core, DynamoDB và Rekognition.

Ngoài ra, AWS Budgets giúp kiểm soát chi phí, IAM quản lý quyền truy cập và CloudTrail ghi lại các hoạt động trong tài khoản AWS. Việc xây dựng một dashboard và quy trình xử lý sự cố cho phép quản trị viên theo dõi, kiểm tra và bảo trì hệ thống hiệu quả trong quá trình vận hành thực tế.
