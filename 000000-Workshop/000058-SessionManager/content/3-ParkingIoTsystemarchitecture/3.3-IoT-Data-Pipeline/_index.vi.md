---
title : "IoT Data Pipeline"
date: 2026-05-13
weight : 3
chapter : false
pre : " <b> 3.3. </b> "
---

Phần này mô tả cách thu thập, truyền tải, xử lý và lưu trữ dữ liệu trong Hệ thống IoT Bãi đỗ xe Thông minh. Luồng dữ liệu IoT kết nối các thiết bị ESP32 tại bãi đỗ xe với các dịch vụ AWS được sử dụng để xử lý, lưu trữ, nhận diện biển số, giám sát và hiển thị dữ liệu.

Trong hệ thống Parking IoT, dữ liệu được chia thành hai nhóm chính:
* **Dữ liệu hình ảnh:** được thu thập từ ESP32 Camera khi có xe ra hoặc vào bãi đỗ.
* **Dữ liệu cảm biến:** được thu thập từ các thiết bị cảm biến ESP32 để phát hiện trạng thái của từng chỗ đỗ xe.

Sau khi dữ liệu được gửi đến AWS, nó sẽ được xử lý bởi AWS Lambda, lưu trữ trong Amazon S3 và Amazon DynamoDB, rồi hiển thị trên giao diện Web/App. Dữ liệu cũng có thể được sử dụng cho các tính năng dựa trên AI trong tương lai.

### 3.3.1. Tổng quan về Data Pipeline
Luồng dữ liệu của hệ thống Parking IoT bao gồm nhiều bước xử lý, bắt đầu từ các thiết bị biên và kết thúc tại các dịch vụ AWS Cloud.

**Luồng dữ liệu tổng quát:**
`ESP32 Camera / Cảm biến ESP32 → Dịch vụ AWS → Xử lý bằng Lambda → DynamoDB / S3 → Web/App`

Hệ thống có ba luồng dữ liệu chính:

| Luồng dữ liệu | Mô tả |
|-----------|-------------|
| Luồng dữ liệu hình ảnh | ESP32 Camera chụp ảnh xe và tải lên Amazon S3 |
| Luồng dữ liệu cảm biến | Cảm biến ESP32 gửi trạng thái chỗ đỗ xe đến AWS IoT Core |
| Luồng truy vấn Web/App | Người dùng truy cập dữ liệu hệ thống thông qua API Gateway và Lambda |

Mỗi luồng dữ liệu được xử lý riêng biệt, nhưng kết quả sau cùng được lưu trữ tập trung tại DynamoDB để quản lý và hiển thị.

### 3.3.2. Luồng Dữ liệu Hình ảnh từ ESP32 Camera
Luồng dữ liệu hình ảnh được sử dụng để ghi nhận xe ra vào bãi đỗ và hỗ trợ nhận diện biển số xe.

Thay vì gửi hình ảnh trực tiếp qua Lambda, ESP32 Camera sẽ yêu cầu một Presigned URL từ API Gateway. Sau đó, thiết bị sẽ tải hình ảnh trực tiếp lên Amazon S3. Cách tiếp cận này giúp giảm tải cho Lambda và phù hợp hơn với các tệp hình ảnh có kích thước lớn.

**Luồng tải hình ảnh:**
`ESP32 Camera → API Gateway → Lambda tạo Presigned URL → Amazon S3`

Sau khi hình ảnh được tải lên S3, hệ thống tiếp tục xử lý qua luồng sau:
`Amazon S3 → Sự kiện S3 ObjectCreated → Lambda Image Processing → Amazon Rekognition → DynamoDB`

**Các bước xử lý chi tiết:**
1. ESP32 Camera phát hiện có xe tại cổng ra hoặc vào.
2. Thiết bị chụp ảnh xe.
3. ESP32 Camera gửi yêu cầu đến API Gateway để lấy Presigned URL.
4. API Gateway gọi hàm Lambda tạo Presigned URL.
5. Lambda tạo Presigned URL và trả về cho ESP32 Camera.
6. ESP32 Camera tải hình ảnh JPEG trực tiếp lên Amazon S3.
7. Amazon S3 tạo ra một sự kiện ObjectCreated sau khi hình ảnh được tải lên thành công.
8. Sự kiện S3 này sẽ kích hoạt hàm Lambda xử lý hình ảnh (Lambda Image Processing).
9. Lambda gọi Amazon Rekognition để phân tích hình ảnh.
10. Kết quả nhận diện được lưu vào DynamoDB.

### 3.3.3. Lưu trữ Hình ảnh trong Amazon S3
Amazon S3 được dùng để lưu trữ hình ảnh xe. Mỗi hình ảnh có thể được đặt tên dựa trên ID thiết bị, timestamp, vị trí cổng, hoặc ID xe để dễ dàng quản lý.

**Cấu trúc lưu trữ S3 mẫu:**
```text
parking-image-bucket/
├── entrance/
│   ├── esp32_cam_01_20260427_103000.jpg
│   └── esp32_cam_01_20260427_104500.jpg
├── exit/
│   ├── esp32_cam_02_20260427_110000.jpg
│   └── esp32_cam_02_20260427_111500.jpg
```

Cấu trúc thư mục này giúp phân biệt rõ ràng giữa hình ảnh xe vào và xe ra.

**Siêu dữ liệu (metadata) hình ảnh mẫu:**
```json
{
  "image_id": "esp32_cam_01_20260427_103000.jpg",
  "device_id": "esp32_cam_01",
  "gate": "entrance",
  "direction": "in",
  "timestamp": "2026-04-27T10:30:00",
  "s3_url": "s3://parking-image-bucket/entrance/esp32_cam_01_20260427_103000.jpg"
}
```

### 3.3.4. Xử lý Hình ảnh với Lambda và Rekognition
Sau khi hình ảnh được tải lên Amazon S3, sự kiện ObjectCreated sẽ kích hoạt một hàm Lambda để xử lý hình ảnh. Lambda nhận thông tin hình ảnh từ sự kiện S3 và gọi Amazon Rekognition để phân tích.

**Luồng xử lý:**
`S3 ObjectCreated → Lambda Image Processing → Amazon Rekognition → DynamoDB`

**Vai trò của từng thành phần:**

| Thành phần | Vai trò |
|-----------|------|
| Amazon S3 | Lưu trữ hình ảnh xe |
| S3 ObjectCreated | Kích hoạt Lambda khi có hình ảnh mới tải lên |
| Lambda Image Processing | Xử lý hình ảnh và gọi Rekognition |
| Amazon Rekognition | Phân tích hình ảnh và hỗ trợ nhận diện biển số |
| DynamoDB | Lưu trữ kết quả nhận diện |

Kết quả sau xử lý có thể bao gồm:
* ID hình ảnh.
* Biển số xe.
* Độ tin cậy của nhận diện (confidence score).
* Hướng di chuyển (vào/ra).
* Thời gian ghi nhận (timestamp).
* Đường dẫn hình ảnh trên S3.

**Dữ liệu xử lý mẫu:**
```json
{
  "log_id": "LOG001",
  "plate_number": "51A-12345",
  "confidence": 92.5,
  "direction": "in",
  "image_url": "s3://parking-image-bucket/entrance/esp32_cam_01_20260427_103000.jpg",
  "timestamp": "2026-04-27T10:30:00"
}
```

### 3.3.5. Luồng Dữ liệu Cảm biến qua AWS IoT Core
Luồng dữ liệu cảm biến được dùng để cập nhật trạng thái của từng chỗ đỗ xe theo thời gian thực. Cảm biến ESP32 gửi dữ liệu đến AWS IoT Core bằng giao thức MQTT.

**Luồng dữ liệu cảm biến:**
`Cảm biến ESP32 → AWS IoT Core → IoT Rule → Lambda Sensor Processing → DynamoDB`

**Các bước xử lý chi tiết:**
1. Cảm biến ESP32 đọc dữ liệu từ cảm biến tại một chỗ đỗ xe.
2. Thiết bị xác định chỗ đỗ là trống hay đã có xe.
3. ESP32 gửi dữ liệu đến AWS IoT Core qua MQTT.
4. AWS IoT Core nhận dữ liệu từ thiết bị.
5. IoT Rule kiểm tra topic MQTT và chuyển tiếp dữ liệu đến Lambda.
6. Lambda Sensor Processing xác thực và chuẩn hóa dữ liệu.
7. Dữ liệu đã xử lý được lưu vào DynamoDB.
8. Web/App truy vấn DynamoDB để hiển thị trạng thái chỗ đỗ mới nhất.

**Topic MQTT mẫu:**
`parking/slot/A01/status`

**Payload mẫu:**
```json
{
  "device_id": "esp32_sensor_01",
  "slot_id": "A01",
  "status": "occupied",
  "timestamp": "2026-04-27T10:30:00"
}
```

### 3.3.6. Xử lý và Chuẩn hóa Dữ liệu Cảm biến
Trước khi lưu trữ vào DynamoDB, dữ liệu cảm biến cần được xác thực để đảm bảo đúng định dạng và giảm thiểu các bản ghi không chính xác.

Lambda Sensor Processing thực hiện các nhiệm vụ sau:
* Kiểm tra xem `device_id` có tồn tại không.
* Kiểm tra xem `slot_id` có đúng định dạng không.
* Kiểm tra xem `status` có phải là `available` hoặc `occupied` không.
* Thêm timestamp xử lý nếu thiết bị không gửi kèm.
* Loại bỏ dữ liệu không hợp lệ hoặc thiếu thông tin.
* Ghi trạng thái chỗ đỗ xe mới nhất vào DynamoDB.

**Dữ liệu hợp lệ mẫu:**
```json
{
  "slot_id": "A01",
  "status": "available",
  "updated_at": "2026-04-27T10:30:00"
}
```

**Dữ liệu không hợp lệ mẫu:**
```json
{
  "slot_id": "",
  "status": "unknown"
}
```

Dữ liệu không hợp lệ sẽ không được ghi vào DynamoDB hoặc có thể được log vào CloudWatch để kiểm tra sau.

### 3.3.7. Lưu trữ Dữ liệu trong Amazon DynamoDB
Amazon DynamoDB được dùng để lưu trữ dữ liệu sau khi xử lý. Hệ thống có thể dùng nhiều bảng để tách biệt dữ liệu xe, dữ liệu cảm biến và trạng thái chỗ đỗ.

**Các bảng chính:**

| Bảng | Chức năng |
|-------|----------|
| ParkingSlots | Lưu trạng thái mới nhất của từng chỗ đỗ xe |
| VehicleLogs | Lưu lịch sử xe ra vào |
| SensorData | Lưu dữ liệu cảm biến theo thời gian |
| DeviceStatus | Lưu trạng thái hoạt động của thiết bị (nếu cần) |

**Dữ liệu bảng ParkingSlots mẫu:**
```json
{
  "slot_id": "A01",
  "status": "occupied",
  "updated_at": "2026-04-27T10:30:00",
  "device_id": "esp32_sensor_01"
}
```

**Dữ liệu bảng VehicleLogs mẫu:**
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

DynamoDB cho phép hệ thống truy vấn dữ liệu nhanh chóng phục vụ các tính năng như hiển thị trạng thái chỗ đỗ, tìm kiếm lịch sử xe và báo cáo tổng quan (dashboard).

### 3.3.8. Luồng Truy vấn Dữ liệu từ Web/App
Người dùng truy cập Web/App để xem trạng thái chỗ đỗ xe, lịch sử ra vào và thông tin biển số xe. Web/App không truy cập trực tiếp vào DynamoDB. Thay vào đó, nó sẽ gọi API Gateway, và API Gateway chuyển yêu cầu đến Lambda Backend.

**Luồng truy vấn:**
`Web/App → API Gateway → Lambda Backend → DynamoDB → Lambda Backend → Web/App`

Các chức năng truy vấn chính bao gồm:
* Lấy danh sách chỗ đỗ xe.
* Xem trạng thái của từng chỗ đỗ xe.
* Xem số lượng chỗ trống và chỗ đã có xe.
* Xem lịch sử xe ra vào.
* Tìm kiếm xe theo biển số.
* Xem hình ảnh xe đã lưu trong S3.
* Xem thống kê bãi đỗ xe.

**API endpoint mẫu:**
`GET /parking/slots`

**Phản hồi (response) mẫu:**
```json
{
  "total_slots": 50,
  "available": 18,
  "occupied": 32,
  "slots": [
    {
      "slot_id": "A01",
      "status": "occupied"
    },
    {
      "slot_id": "A02",
      "status": "available"
    }
  ]
}
```

### 3.3.9. Luồng Dữ liệu AI Service
Ngoài các tính năng quản lý bãi đỗ xe tiêu chuẩn, hệ thống có thể tích hợp Amazon Bedrock để hỗ trợ các truy vấn bằng ngôn ngữ tự nhiên. Người dùng có thể đặt câu hỏi qua Web/App, và hệ thống xử lý yêu cầu thông qua Lambda AI Service.

**Luồng AI service:**
`Web/App → API Gateway → Lambda AI Service → DynamoDB → Amazon Bedrock → Web/App`

**Các bước xử lý:**
1. Người dùng nhập câu hỏi vào Web/App.
2. Web/App gửi câu hỏi đến API Gateway.
3. API Gateway gọi hàm Lambda AI Service.
4. Lambda AI Service truy vấn dữ liệu cần thiết từ DynamoDB.
5. Lambda gửi ngữ cảnh dữ liệu đến Amazon Bedrock.
6. Amazon Bedrock tạo câu trả lời bằng ngôn ngữ tự nhiên.
7. Kết quả được trả về cho Web/App.

**Câu hỏi mẫu:**
`Hiện tại bãi đỗ xe còn bao nhiêu chỗ trống?`

**Câu trả lời mẫu:**
`Hiện tại bãi đỗ xe còn 18 chỗ trống trên tổng số 50 chỗ.`

### 3.3.10. Logging và Xử lý Lỗi trong Luồng Dữ liệu
Trong quá trình truyền tải và xử lý dữ liệu, hệ thống có thể gặp các lỗi như mất kết nối thiết bị, tải ảnh thất bại, payload cảm biến không hợp lệ hoặc lỗi xử lý Lambda. Do đó, CloudWatch được sử dụng để thu thập log và hỗ trợ kiểm tra lỗi.

**Các lỗi thường gặp và cách xử lý:**

| Lỗi | Cách xử lý |
|-------|-----------------|
| ESP32 mất kết nối WiFi | Thiết bị tự tự động kết nối lại và gửi lại dữ liệu |
| Tải ảnh thất bại | ESP32 yêu cầu Presigned URL mới và tải lại |
| Payload MQTT sai định dạng | Lambda log lỗi vào CloudWatch |
| Rekognition không nhận ra biển số | Lưu kết quả dưới dạng cần xem xét thủ công |
| Lỗi ghi DynamoDB | Lambda thử ghi lại (retry) hoặc log lỗi |
| API Gateway trả về lỗi 4xx/5xx | Kiểm tra định dạng yêu cầu và log Lambda |

**Luồng logging:**
`API Gateway / Lambda / IoT Core / Rekognition / DynamoDB → CloudWatch`

CloudWatch giúp đội ngũ phát hiện sớm các sự cố và đảm bảo data pipeline hoạt động ổn định.

### 3.3.11. Kết luận
Data pipeline của hệ thống IoT là một thành phần quan trọng giúp hệ thống Parking IoT hoạt động tự động và theo thời gian thực. Dữ liệu từ ESP32 Camera và các cảm biến ESP32 được gửi lên AWS thông qua hai luồng chính: hình ảnh xe được tải lên Amazon S3 bằng Presigned URLs, trong khi dữ liệu cảm biến được gửi đến AWS IoT Core bằng MQTT.

Sau khi nhận dữ liệu, AWS Lambda sẽ đảm nhiệm các tác vụ xử lý, Amazon Rekognition hỗ trợ nhận diện biển số xe, DynamoDB lưu trữ kết quả và Web/App hiển thị dữ liệu đến người dùng. CloudWatch cũng được tận dụng để log và giám sát lỗi xuyên suốt quá trình này.

Với thiết kế này, hệ thống có thể theo dõi bãi đỗ xe theo thời gian thực, lưu trữ dữ liệu tập trung, hỗ trợ nhận diện biển số xe và cung cấp nền tảng vững chắc cho các tính năng nâng cao như thống kê, cảnh báo và AI Service.
