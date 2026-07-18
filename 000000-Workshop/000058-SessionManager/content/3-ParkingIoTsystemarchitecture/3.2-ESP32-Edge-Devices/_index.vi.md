---
title : "ESP32 Edge Devices"
date: 2026-05-13
weight : 2
chapter : false
pre : " <b> 3.2. </b> "
---

Phần này trình bày vai trò của các thiết bị biên (edge devices) trong Hệ thống IoT Bãi đỗ xe Thông minh. Các thiết bị biên được lắp đặt trực tiếp tại bãi đỗ xe để thu thập dữ liệu thực tế, bao gồm hình ảnh xe và trạng thái chỗ đỗ xe.

Trong hệ thống này, hai loại thiết bị ESP32 chính được sử dụng:
* **ESP32 Camera:** được sử dụng để chụp hình ảnh xe ở cổng vào và cổng ra.
* **Thiết bị Cảm biến ESP32 (ESP32 Sensor Device):** được sử dụng để phát hiện trạng thái của từng chỗ đỗ xe.

Dữ liệu thu thập từ các thiết bị ESP32 được gửi đến AWS để xử lý, lưu trữ, giám sát và hiển thị thông qua giao diện Web/App.

### 3.2.1. Vai trò của Thiết bị Biên trong Hệ thống
Các thiết bị biên đóng vai trò là lớp thu thập dữ liệu đầu tiên của hệ thống Parking IoT. Những thiết bị này được lắp đặt trong bãi đỗ xe để thu thập thông tin theo thời gian thực.

Các nhiệm vụ chính của thiết bị biên bao gồm:
* Chụp hình ảnh xe khi xe vào hoặc ra khỏi bãi đỗ xe.
* Phát hiện trạng thái của từng chỗ đỗ xe.
* Gửi dữ liệu cảm biến đến AWS IoT Core.
* Tải hình ảnh xe lên Amazon S3 bằng Presigned URLs.
* Hỗ trợ tự động hóa việc giám sát bãi đỗ xe.

Với thiết bị biên, hệ thống có thể giảm bớt các thao tác thủ công và cập nhật dữ liệu đỗ xe nhanh chóng và chính xác hơn.

### 3.2.2. ESP32 Camera
ESP32 Camera được sử dụng để chụp hình ảnh xe tại cổng vào và cổng ra của bãi đỗ xe. Khi có xe đi qua cổng, camera sẽ chụp ảnh và tải lên Amazon S3 để xử lý hình ảnh và nhận diện biển số.

**Các Chức năng chính của ESP32 Camera**
* Chụp ảnh xe khi phát hiện có xe.
* Gửi yêu cầu đến API Gateway để nhận Presigned URL.
* Tải hình ảnh trực tiếp lên Amazon S3.
* Gửi thông tin hình ảnh kèm theo dấu thời gian (timestamp).
* Hỗ trợ nhận diện biển số xe sử dụng Amazon Rekognition.

**Luồng hoạt động của ESP32 Camera**
`ESP32 Camera → API Gateway → Lambda tạo Presigned URL → Amazon S3`

Sau khi hình ảnh được tải lên S3, hệ thống tiếp tục với luồng xử lý sau:
`Amazon S3 → Sự kiện S3 ObjectCreated → Lambda Image Processing → Amazon Rekognition → DynamoDB`

**Các bước Xử lý Chi tiết**
1. ESP32 Camera được lắp đặt tại cổng vào hoặc cổng ra của bãi đỗ xe.
2. Khi xe đi qua, thiết bị chụp ảnh.
3. ESP32 Camera gửi yêu cầu đến API Gateway để lấy Presigned URL.
4. API Gateway gọi Lambda Backend để tạo Presigned URL.
5. Lambda trả về Presigned URL cho ESP32 Camera.
6. ESP32 Camera tải hình ảnh JPEG trực tiếp lên Amazon S3.
7. Sau khi tải lên thành công, S3 kích hoạt hàm Lambda xử lý hình ảnh.
8. Lambda gọi Amazon Rekognition để phân tích hình ảnh.
9. Kết quả nhận diện được lưu trữ vào DynamoDB.

**Dữ liệu Hình ảnh Mẫu**
```json
{
  "image_id": "car_001.jpg",
  "device_id": "esp32_cam_01",
  "gate": "entrance",
  "direction": "in",
  "timestamp": "2026-04-27T10:30:00",
  "s3_url": "s3://parking-image-bucket/car_001.jpg"
}
```

| Thuộc tính | Mô tả |
|-----------|-------------|
| image_id | Tên hoặc ID của hình ảnh |
| device_id | ID của thiết bị ESP32 Camera |
| gate | Vị trí camera, ví dụ như cổng vào (entrance) hoặc cổng ra (exit) |
| direction | Hướng di chuyển: vào (in) hoặc ra (out) |
| timestamp | Thời gian chụp ảnh |
| s3_url | Đường dẫn hình ảnh trên Amazon S3 |

### 3.2.3. Thiết bị Cảm biến ESP32 (ESP32 Sensor Device)
Thiết bị cảm biến ESP32 được dùng để phát hiện trạng thái của từng chỗ đỗ xe. Tùy thuộc vào thiết kế thực tế, hệ thống có thể sử dụng cảm biến siêu âm, hồng ngoại hoặc cảm biến từ tính để xác định xem chỗ đỗ xe đã có xe hay còn trống.

**Các Chức năng chính của Thiết bị Cảm biến ESP32**
* Đọc dữ liệu cảm biến từ từng chỗ đỗ xe.
* Xác định xem chỗ đỗ xe là trống (available) hay đã có xe (occupied).
* Gửi dữ liệu đến AWS IoT Core qua giao thức MQTT.
* Cập nhật trạng thái chỗ đỗ xe vào DynamoDB thông qua Lambda.
* Hỗ trợ hiển thị trạng thái chỗ đỗ xe theo thời gian thực trên Web/App.

**Trạng thái Chỗ đỗ xe**
Hệ thống chủ yếu sử dụng hai trạng thái:

| Trạng thái | Mô tả |
|--------|-------------|
| available | Chỗ đỗ xe còn trống |
| occupied | Chỗ đỗ xe đã có xe |

**Luồng hoạt động của Cảm biến ESP32**
`Cảm biến ESP32 → AWS IoT Core → IoT Rule → Lambda Sensor Processing → DynamoDB`

**Các bước Xử lý Chi tiết**
1. ESP32 đọc dữ liệu từ cảm biến lắp tại chỗ đỗ xe.
2. Thiết bị xác định trạng thái chỗ đỗ là trống hoặc đã có xe.
3. ESP32 gửi dữ liệu đến AWS IoT Core qua MQTT.
4. AWS IoT Core nhận dữ liệu từ thiết bị.
5. IoT Rule kiểm tra topic MQTT và chuyển tiếp dữ liệu đến Lambda.
6. Lambda Sensor Processing xác thực và chuẩn hóa dữ liệu.
7. Dữ liệu đã xử lý được lưu vào DynamoDB.
8. Web/App truy vấn DynamoDB để hiển thị trạng thái chỗ đỗ xe mới nhất.

**MQTT Topic Mẫu**
`parking/slot/A01/status`

**Payload Mẫu gửi từ Cảm biến ESP32**
```json
{
  "device_id": "esp32_sensor_01",
  "slot_id": "A01",
  "status": "occupied",
  "timestamp": "2026-04-27T10:30:00"
}
```

| Thuộc tính | Mô tả |
|-----------|-------------|
| device_id | ID của thiết bị cảm biến ESP32 |
| slot_id | ID của chỗ đỗ xe |
| status | Trạng thái chỗ đỗ xe |
| timestamp | Thời gian ghi nhận dữ liệu |

### 3.2.4. Kết nối Thiết bị ESP32 với Internet
Các thiết bị ESP32 cần kết nối WiFi để gửi dữ liệu lên AWS. Mỗi thiết bị được cấu hình với thông tin mạng và thông tin kết nối AWS.

Cấu hình yêu cầu bao gồm:
* Tên WiFi (SSID).
* Mật khẩu WiFi.
* API Gateway endpoint cho ESP32 Camera.
* AWS IoT Core endpoint cho Cảm biến ESP32.
* Chứng chỉ bảo mật và khóa riêng tư (private keys) cho kết nối MQTT.
* Device ID để định danh từng thiết bị ESP32 trong hệ thống.

**Cấu hình thiết bị mẫu:**
* WiFi SSID: `Parking_WiFi`
* Device ID: `esp32_sensor_01`
* MQTT Topic: `parking/slot/A01/status`
* AWS IoT Endpoint: `xxxxxxxxxxxxxx-ats.iot.ap-southeast-1.amazonaws.com`

Việc định danh thiết bị giúp hệ thống dễ dàng quản lý thiết bị, khắc phục sự cố và mở rộng khi thêm các cảm biến hoặc camera mới.

### 3.2.5. Kết nối ESP32 Camera với Amazon S3
ESP32 Camera không tải hình ảnh trực tiếp thông qua Lambda vì các tệp hình ảnh có thể có dung lượng lớn. Thay vào đó, nó sử dụng một Presigned URL để tải trực tiếp lên Amazon S3.

Quá trình tải hình ảnh diễn ra như sau:
`ESP32 Camera → API Gateway → Lambda tạo Presigned URL → ESP32 Camera → Amazon S3`

Các bước bao gồm:
1. ESP32 Camera chụp hình ảnh xe.
2. ESP32 Camera gửi yêu cầu đến API Gateway.
3. Lambda tạo một Presigned URL để tải hình ảnh.
4. ESP32 Camera nhận Presigned URL.
5. ESP32 Camera tải hình ảnh JPEG lên Amazon S3.
6. S3 kích hoạt Lambda sau khi hình ảnh được tải lên thành công.

Cách tiếp cận này mang lại nhiều lợi ích:
* Giảm tải cho Lambda.
* Cải thiện hiệu suất tải hình ảnh.
* Sử dụng Amazon S3 để lưu trữ đối tượng đáng tin cậy.
* Dễ dàng kích hoạt xử lý hình ảnh sử dụng sự kiện S3.

### 3.2.6. Kết nối Cảm biến ESP32 với AWS IoT Core
Thiết bị cảm biến ESP32 gửi dữ liệu đến AWS IoT Core sử dụng giao thức MQTT. MQTT rất phù hợp cho các hệ thống IoT vì tính nhẹ, hiệu quả và hoạt động tốt với các thiết bị bị hạn chế tài nguyên.

Luồng truyền dữ liệu là:
`Cảm biến ESP32 → MQTT → AWS IoT Core → IoT Rule → Lambda → DynamoDB`

Các bước triển khai bao gồm:
1. Tạo một IoT Thing để đại diện cho thiết bị ESP32 trong AWS IoT Core.
2. Tạo chứng chỉ bảo mật cho thiết bị.
3. Đính kèm một IoT Policy vào chứng chỉ.
4. Cấu hình MQTT endpoint trên thiết bị ESP32.
5. ESP32 gửi (publish) dữ liệu đến MQTT topic đã xác định.
6. IoT Rule chuyển dữ liệu đến Lambda để xử lý.
7. Lambda ghi dữ liệu đã xử lý vào DynamoDB.

**Dữ liệu cảm biến định kỳ mẫu:**
```json
{
  "device_id": "esp32_sensor_02",
  "slot_id": "B03",
  "status": "available",
  "timestamp": "2026-04-27T10:35:00"
}
```

### 3.2.7. Bảo mật Thiết bị Biên
Bảo mật thiết bị biên rất quan trọng vì các thiết bị ESP32 kết nối trực tiếp với Internet và gửi dữ liệu lên AWS.

Các biện pháp bảo mật bao gồm:
* Không lưu trữ công khai thông tin nhạy cảm trong mã nguồn (source code).
* Sử dụng chứng chỉ khi kết nối thiết bị ESP32 với AWS IoT Core.
* Gán một Device ID duy nhất cho mỗi thiết bị.
* Cấu hình IoT Policy sao cho mỗi thiết bị chỉ có thể gửi dữ liệu đến topic của riêng nó.
* Xác thực các yêu cầu của ESP32 Camera thông qua API Gateway.
* Sử dụng Presigned URLs với thời gian hết hạn ngắn.
* Không cung cấp trực tiếp thông tin xác thực AWS (credentials) cho các thiết bị ESP32.

**Nguyên tắc bảo mật mẫu:**
* Mỗi thiết bị ESP32 chỉ có thể gửi dữ liệu đến MQTT topic riêng của nó.
* ESP32 Camera chỉ có thể tải hình ảnh lên bằng Presigned URL có thời hạn ngắn.

Việc giới hạn quyền giúp giảm thiểu rủi ro khi một thiết bị bị lỗi hoặc bị truy cập trái phép.

### 3.2.8. Xử lý Lỗi tại Thiết bị Biên
Trong quá trình hoạt động, các thiết bị ESP32 có thể gặp sự cố như mất kết nối WiFi, gửi dữ liệu thất bại hoặc tải hình ảnh không thành công. Do đó, cần triển khai xử lý lỗi cơ bản ở phía thiết bị.

**Các lỗi thường gặp và cách xử lý:**

| Lỗi | Cách xử lý |
|-------|-----------------|
| Mất kết nối WiFi | Tự động kết nối lại sau một độ trễ ngắn |
| Gửi MQTT thất bại | Thử gửi lại dữ liệu khi kết nối được khôi phục |
| Tải hình ảnh thất bại | Yêu cầu Presigned URL mới và tải lại |
| Lỗi đọc cảm biến | Lọc dữ liệu hoặc kiểm tra nhiều lần trước khi gửi |
| Hình ảnh camera bị mờ | Điều chỉnh góc camera và điều kiện ánh sáng |

Thiết bị có thể tạm thời lưu trữ dữ liệu vào bộ nhớ cục bộ nếu mất kết nối mạng và gửi lại dữ liệu khi kết nối Internet được khôi phục.

### 3.2.9. Kiểm thử Thiết bị Biên
Trước khi tích hợp hoàn toàn với AWS, mỗi thiết bị ESP32 nên được kiểm tra để đảm bảo hoạt động chính xác.

**Kiểm thử ESP32 Camera**
* Kiểm tra xem camera có thể chụp ảnh không.
* Kiểm tra xem hình ảnh có hiển thị rõ biển số xe không.
* Kiểm tra xem ESP32 có thể gọi API Gateway không.
* Kiểm tra xem Presigned URL có được tạo thành công không.
* Kiểm tra xem hình ảnh có được tải lên S3 thành công không.
* Kiểm tra xem S3 có kích hoạt hàm Lambda xử lý hình ảnh không.

**Kiểm thử Cảm biến ESP32**
* Kiểm tra xem cảm biến có đọc đúng trạng thái không.
* Kiểm tra xem ESP32 kết nối với WiFi có thành công không.
* Kiểm tra xem ESP32 kết nối với AWS IoT Core không.
* Kiểm tra xem dữ liệu có được gửi đến đúng topic MQTT không.
* Kiểm tra xem IoT Rule có kích hoạt Lambda chính xác không.
* Kiểm tra xem DynamoDB có lưu trạng thái chỗ đỗ xe mới nhất không.

### 3.2.10. Kết luận
Lớp thiết bị biên ESP32 là một lớp thu thập dữ liệu quan trọng của hệ thống Parking IoT. ESP32 Camera chịu trách nhiệm chụp hình ảnh xe ra vào, trong khi các thiết bị cảm biến ESP32 ghi nhận trạng thái của từng chỗ đỗ xe.

Dữ liệu từ thiết bị biên được gửi đến AWS thông qua hai luồng chính: hình ảnh xe được tải lên Amazon S3 sử dụng Presigned URLs, trong khi dữ liệu cảm biến được gửi đến AWS IoT Core thông qua MQTT. Sau đó, AWS Lambda sẽ xử lý dữ liệu và lưu kết quả vào DynamoDB.

Việc triển khai các thiết bị biên cho phép hệ thống Parking IoT giám sát bãi đỗ xe theo thời gian thực, giảm thiểu các thao tác thủ công và cung cấp nền tảng dữ liệu cho các tính năng nâng cao như nhận diện biển số xe, thống kê bãi đỗ xe và quản lý bằng AI.
