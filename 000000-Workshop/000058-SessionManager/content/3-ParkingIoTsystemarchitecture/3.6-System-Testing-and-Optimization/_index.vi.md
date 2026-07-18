---
title : "System Testing and Optimization"
date: 2026-05-13
weight : 6
chapter : false
pre : " <b> 3.6. </b> "
---

Phần này trình bày quá trình kiểm thử và tối ưu hóa cho Hệ thống IoT Bãi đỗ xe Thông minh sau khi triển khai các thành phần chính như thiết bị ESP32, AWS IoT Core, Amazon S3, AWS Lambda, Amazon Rekognition, DynamoDB, API Gateway, Cognito, CloudFront và CloudWatch.

Mục đích của việc kiểm thử là để đảm bảo rằng hệ thống hoạt động theo đúng thiết kế, dữ liệu được truyền tải và xử lý chính xác, giao diện Web/App hiển thị thông tin đúng, và hệ thống có thể vận hành ổn định, an toàn, cũng như tiết kiệm chi phí.

### 3.6.1. Mục tiêu Kiểm thử
Quá trình kiểm thử hệ thống được dùng để xác minh xem các chức năng chính của hệ thống Parking IoT có hoạt động chính xác hay không.

Các mục tiêu kiểm thử bao gồm:
* Kiểm tra xem ESP32 Camera có thể chụp và tải ảnh lên Amazon S3 thành công không.
* Kiểm tra xem cảm biến ESP32 có gửi dữ liệu trạng thái chỗ đỗ xe đến AWS IoT Core không.
* Kiểm tra xem AWS IoT Core có kích hoạt Lambda để xử lý dữ liệu cảm biến không.
* Kiểm tra xem sự kiện S3 ObjectCreated có kích hoạt Lambda xử lý ảnh không.
* Kiểm tra xem Amazon Rekognition có phân tích được ảnh và trả về kết quả không.
* Kiểm tra xem DynamoDB có lưu trữ dữ liệu chính xác không.
* Kiểm tra xem API Gateway và Lambda Backend có trả dữ liệu về Web/App không.
* Kiểm tra xem Cognito có xác thực người dùng đúng cách không.
* Kiểm tra xem CloudWatch có ghi log và hỗ trợ phát hiện lỗi không.
* Kiểm tra xem chi phí sử dụng AWS có nằm trong ngân sách dự kiến không.

### 3.6.2. Kiểm thử ESP32 Camera
ESP32 Camera được sử dụng để chụp ảnh xe ra vào bãi đỗ. Do đó, cần phải kiểm tra khả năng chụp ảnh, yêu cầu Presigned URL và tải ảnh lên Amazon S3.

**Luồng kiểm thử:**
`ESP32 Camera → API Gateway → Lambda tạo Presigned URL → Amazon S3`

**Các bước kiểm thử:**
1. Bật nguồn ESP32 Camera và kết nối WiFi.
2. Kiểm tra xem thiết bị kết nối mạng thành công không.
3. Cho một phương tiện hoặc vật thể đi qua khu vực camera.
4. Kiểm tra xem ESP32 Camera có chụp ảnh không.
5. Kiểm tra xem ESP32 Camera có gọi API Gateway để xin Presigned URL không.
6. Kiểm tra xem Lambda tạo Presigned URL có thành công không.
7. Kiểm tra xem hình ảnh có được tải lên Amazon S3 không.
8. Kiểm tra xem hình ảnh có được lưu đúng vào thư mục `entrance/` hoặc `exit/` không.

**Kết quả mong đợi:**

| Hạng mục kiểm thử | Kết quả mong đợi |
|-----------|-----------------|
| Kết nối WiFi | ESP32 Camera kết nối thành công |
| Chụp ảnh | Hình ảnh được chụp rõ nét |
| Yêu cầu API Gateway | Yêu cầu được gửi thành công |
| Tạo Presigned URL | Lambda trả về một URL hợp lệ |
| Tải ảnh lên S3 | Hình ảnh xuất hiện trong S3 Bucket |

### 3.6.3. Kiểm thử Cảm biến ESP32
Cảm biến ESP32 được dùng để xác định trạng thái của từng chỗ đỗ xe. Thiết bị gửi dữ liệu lên AWS IoT Core bằng MQTT.

**Luồng kiểm thử:**
`ESP32 Sensor → AWS IoT Core → IoT Rule → Lambda Sensor Processing → DynamoDB`

**Các bước kiểm thử:**
1. Bật nguồn thiết bị cảm biến ESP32.
2. Kiểm tra xem thiết bị có kết nối WiFi không.
3. Kiểm tra xem thiết bị có kết nối với AWS IoT Core không.
4. Đặt một vật thể hoặc xe vào khu vực cảm biến.
5. Kiểm tra xem cảm biến có phát hiện trạng thái là đã có xe (occupied) không.
6. Lấy vật thể hoặc xe ra khỏi khu vực cảm biến.
7. Kiểm tra xem cảm biến có phát hiện trạng thái là trống (available) không.
8. Kiểm tra xem dữ liệu có được gửi (publish) đến đúng topic MQTT không.
9. Kiểm tra xem IoT Rule có kích hoạt Lambda không.
10. Kiểm tra xem DynamoDB có cập nhật trạng thái chỗ đỗ mới nhất không.

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

**Kết quả mong đợi:**

| Hạng mục kiểm thử | Kết quả mong đợi |
|-----------|-----------------|
| Kết nối WiFi | ESP32 kết nối thành công |
| Kết nối AWS IoT Core | Thiết bị gửi dữ liệu MQTT thành công |
| Dữ liệu cảm biến | Trạng thái được phát hiện đúng là available hoặc occupied |
| IoT Rule | Lambda được kích hoạt |
| DynamoDB | Dữ liệu được cập nhật chính xác |

### 3.6.4. Kiểm thử Xử lý Hình ảnh và Nhận diện Biển số
Sau khi ESP32 Camera tải ảnh lên Amazon S3, hệ thống cần kiểm tra xem Lambda có được kích hoạt không và Amazon Rekognition có xử lý ảnh chính xác không.

**Luồng kiểm thử:**
`Amazon S3 → Sự kiện S3 ObjectCreated → Lambda Image Processing → Amazon Rekognition → DynamoDB`

**Các bước kiểm thử:**
1. Tải một hình ảnh xe lên S3 bằng ESP32 Camera hoặc tải lên thủ công để kiểm thử.
2. Kiểm tra xem sự kiện S3 ObjectCreated có được kích hoạt không.
3. Kiểm tra xem hàm Lambda Image Processing có chạy thành công không.
4. Kiểm tra xem Lambda có thể đọc ảnh từ S3 không.
5. Kiểm tra xem Lambda có gọi Amazon Rekognition không.
6. Kiểm tra xem kết quả nhận diện có được trả về không.
7. Kiểm tra xem dữ liệu có được ghi vào bảng VehicleLogs trong DynamoDB không.

**Dữ liệu sau xử lý mẫu:**
```json
{
  "log_id": "LOG001",
  "plate_number": "51A-12345",
  "confidence": 92.5,
  "direction": "in",
  "image_url": "s3://parking-image-bucket/entrance/car_001.jpg",
  "timestamp": "2026-04-27T10:30:00"
}
```

**Kết quả mong đợi:**

| Hạng mục kiểm thử | Kết quả mong đợi |
|-----------|-----------------|
| Tải ảnh | Hình ảnh được lưu trong S3 |
| S3 Event | Lambda được kích hoạt |
| Rekognition | Hình ảnh được phân tích |
| DynamoDB | Kết quả được lưu vào bảng VehicleLogs |
| CloudWatch | Log xử lý thành công được ghi nhận |

### 3.6.5. Kiểm thử API Gateway và Lambda Backend
API Gateway và Lambda Backend hoạt động như một lớp trung gian giữa Web/App và dữ liệu lưu trong DynamoDB. Các API phải được kiểm tra để đảm bảo hoạt động chính xác.

**Luồng kiểm thử:**
`Web/App → API Gateway → Lambda Backend → DynamoDB`

**Các API cần kiểm thử:**

| API Endpoint | Mục đích Kiểm thử |
|--------------|-----------------|
| `GET /parking/slots` | Lấy danh sách chỗ đỗ xe |
| `GET /vehicle/logs` | Lấy lịch sử xe ra vào |
| `POST /upload-url` | Tạo Presigned URL |
| `GET /vehicle/search` | Tìm kiếm xe theo biển số |
| `POST /ai/query` | Gửi câu hỏi đến AI Service |

**Các bước kiểm thử:**
1. Gửi các yêu cầu đến từng endpoint API.
2. Kiểm tra xem API Gateway có nhận được yêu cầu không.
3. Kiểm tra xem Lambda Backend có được gọi không.
4. Kiểm tra xem Lambda có truy vấn DynamoDB đúng không.
5. Kiểm tra xem phản hồi có trả về đúng định dạng JSON không.
6. Kiểm tra xem có bất kỳ lỗi 4xx hay 5xx nào không.

**Phản hồi API mẫu:**
```json
{
  "total_slots": 50,
  "available": 18,
  "occupied": 32
}
```

**Kết quả mong đợi:**

| Hạng mục kiểm thử | Kết quả mong đợi |
|-----------|-----------------|
| API nhận yêu cầu | Yêu cầu được gửi thành công |
| Lambda Backend | Lambda xử lý yêu cầu chính xác |
| Truy vấn DynamoDB | Dữ liệu được truy vấn chuẩn xác |
| Phản hồi | Phản hồi JSON được trả về đúng định dạng |
| Xử lý lỗi | Các log lỗi được ghi lại nếu yêu cầu không hợp lệ |

### 3.6.6. Kiểm thử Giao diện Web/App
Giao diện Web/App là nơi người dùng xem dữ liệu đỗ xe. Do đó, cần kiểm tra xem giao diện có hiển thị dữ liệu từ backend một cách chính xác hay không.

**Các chức năng cần kiểm tra:**
* Đăng nhập người dùng.
* Hiển thị tổng số chỗ đỗ xe.
* Hiển thị số chỗ trống và đã có xe.
* Hiển thị trạng thái của từng chỗ đỗ xe.
* Hiển thị lịch sử xe ra vào.
* Hiển thị hình ảnh xe từ S3.
* Tìm kiếm xe theo biển số.
* Hiển thị thông báo lỗi khi có sự cố API.

**Luồng kiểm thử giao diện:**
`Người dùng → CloudFront → S3 Static Website → API Gateway → Lambda → DynamoDB`

**Kết quả mong đợi:**

| Chức năng | Kết quả mong đợi |
|----------|-----------------|
| Đăng nhập | Người dùng đăng nhập thành công |
| Bảng điều khiển (Dashboard) | Hiển thị chính xác chỗ trống và chỗ có xe |
| Chỗ đỗ xe (Parking Slots) | Trạng thái chỗ đỗ xe được cập nhật |
| Lịch sử xe (Vehicle Logs) | Lịch sử ra vào của xe được hiển thị đầy đủ |
| Tìm kiếm | Tìm kiếm biển số xe trả về kết quả đúng |
| Thông báo lỗi | Giao diện hiển thị thông báo lỗi rõ ràng |

### 3.6.7. Kiểm thử Bảo mật
Kiểm thử bảo mật đảm bảo rằng hệ thống không cho phép truy cập trái phép và các dịch vụ AWS chỉ được cấp những quyền cần thiết.

**Các hạng mục cần kiểm tra:**
* Người dùng chưa đăng nhập không thể gọi các API được bảo vệ.
* Token Cognito hết hạn sẽ bị API Gateway từ chối.
* Người dùng thông thường không thể truy cập các chức năng của Admin.
* ESP32 Camera không có quyền AWS trực tiếp.
* Presigned URLs chỉ có hiệu lực trong thời gian ngắn.
* Cảm biến ESP32 chỉ có thể gửi dữ liệu đến các topic MQTT được ủy quyền.
* Các hàm Lambda chỉ có những quyền cần thiết cho tác vụ của mình.

**Ví dụ kiểm thử không có token:**
`Web/App → API Gateway → Không có Token Cognito → Yêu cầu bị từ chối`

**Kết quả mong đợi:**

| Hạng mục kiểm thử | Kết quả mong đợi |
|-----------|-----------------|
| Gọi API không có token | Yêu cầu bị từ chối |
| Token hết hạn hoặc không hợp lệ | Yêu cầu bị từ chối |
| Người dùng gọi API Admin | Bị từ chối nếu không có quyền |
| Presigned URL hết hạn | Không cho phép tải ảnh lên |
| Sai MQTT topic | Thiết bị không được phép publish |

### 3.6.8. Kiểm thử Giám sát và Log
CloudWatch được sử dụng để kiểm tra log của các thành phần hệ thống. Kiểm thử log đảm bảo rằng khi có lỗi xảy ra, quản trị viên có thể nhanh chóng xác định được nguyên nhân.

**Các log cần kiểm tra:**

| Thành phần | Log cần kiểm tra |
|-----------|---------------|
| Lambda Backend | Yêu cầu từ Web/App và lỗi truy vấn dữ liệu |
| Lambda Image Processing | Lỗi đọc ảnh và lỗi Rekognition |
| Lambda Sensor Processing | Payload MQTT và lỗi ghi DynamoDB |
| API Gateway | Yêu cầu, phản hồi và lỗi 4xx/5xx |
| IoT Core | Dữ liệu MQTT từ các thiết bị ESP32 |
| CloudFront/WAF | Các yêu cầu bị chặn hoặc bất thường |

**Các bước kiểm thử:**
1. Tạo một yêu cầu hợp lệ và kiểm tra các log thành công.
2. Tạo một yêu cầu không hợp lệ và kiểm tra các log lỗi.
3. Gửi một payload MQTT thiếu trường dữ liệu và kiểm tra log của Lambda.
4. Tải lên một định dạng ảnh không hợp lệ và kiểm tra log của Lambda Image Processing.
5. Kiểm tra các nhóm log (Log Groups) trong CloudWatch cho từng hàm Lambda.

**Kết quả mong đợi:**
* CloudWatch ghi lại cả log thành công và log lỗi.
* Quản trị viên có thể truy vết lỗi theo từng dịch vụ và bước xử lý.

### 3.6.9. Tối ưu hóa Hiệu suất Hệ thống
Sau khi kiểm thử các chức năng, hệ thống cần được tối ưu hóa để chạy nhanh hơn, đáng tin cậy hơn và có khả năng phục vụ lượng người dùng và thiết bị lớn hơn.

**Các phương pháp tối ưu hóa bao gồm:**
* Tối ưu hóa thời gian thực thi của Lambda.
* Giảm kích thước ảnh trước khi tải lên S3.
* Sử dụng Presigned URLs để giảm tải cho Lambda.
* Thiết kế Khóa phân vùng (Partition Keys) DynamoDB phù hợp.
* Giảm các lời gọi API không cần thiết từ Web/App.
* Sử dụng bộ đệm (cache) CloudFront để tăng tốc độ truy cập trang web.
* Cấu hình thời gian timeout hợp lý cho Lambda.
* Giảm bớt các log không cần thiết để tiết kiệm chi phí CloudWatch.

**Ví dụ về tối ưu hóa hình ảnh:**
* ESP32 Camera giảm kích thước ảnh trước khi tải lên S3.
* Giúp cải thiện tốc độ tải lên và giảm chi phí lưu trữ.

**Ví dụ về tối ưu hóa API:**
* Web/App nên gọi API lấy trạng thái đỗ xe theo một khoảng thời gian phù hợp, thay vì gọi liên tục quá nhiều lần trong thời gian ngắn.

### 3.6.10. Tối ưu hóa Chi phí AWS
Do hệ thống sử dụng nhiều dịch vụ AWS, việc tối ưu hóa chi phí là cần thiết, đặc biệt trong các môi trường học tập hoặc demo.

**Các phương pháp tối ưu hóa chi phí bao gồm:**
* Xóa các hình ảnh cũ trong S3 nếu không còn cần thiết.
* Cấu hình S3 Lifecycle Rules để tự động di chuyển hoặc xóa dữ liệu cũ.
* Hạn chế số lần gọi Amazon Rekognition.
* Hạn chế số lần gọi Amazon Bedrock nếu sử dụng AI Service.
* Giám sát chi phí bằng AWS Budgets.
* Chỉ bật các log cần thiết trong CloudWatch.
* Xóa các tài nguyên không sử dụng sau khi demo xong.
* Sử dụng chế độ On-Demand cho DynamoDB trong môi trường kiểm thử nhỏ.

**Cấu hình ngân sách mẫu:**
* Ngân sách hàng tháng: 10 USD
* Cảnh báo ở mức 50%, 80% và 100%
* Gửi cảnh báo đến email của quản trị viên

**Kết quả mong đợi:**
* Hệ thống hoạt động trong phạm vi chi phí dự kiến.
* Quản trị viên nhận được thông báo khi chi phí tăng đột biến.

### 3.6.11. Tóm tắt Kết quả Kiểm thử
Sau khi kiểm tra từng thành phần, kết quả có thể được tóm tắt trong bảng sau:

| Hạng mục kiểm thử | Kết quả mong đợi | Trạng thái |
|-----------|-----------------|--------|
| ESP32 Camera | Chụp và tải ảnh lên S3 | Đạt (Passed) |
| Cảm biến ESP32 | Gửi dữ liệu trạng thái đến AWS IoT Core | Đạt (Passed) |
| S3 Event | Kích hoạt Lambda xử lý ảnh | Đạt (Passed) |
| Rekognition | Phân tích ảnh và trả về kết quả | Đạt (Passed) |
| DynamoDB | Lưu trữ dữ liệu chính xác | Đạt (Passed) |
| API Gateway | Trả dữ liệu về Web/App | Đạt (Passed) |
| Cognito | Xác thực người dùng | Đạt (Passed) |
| CloudWatch | Ghi lại log hệ thống | Đạt (Passed) |
| AWS Budgets | Theo dõi chi phí AWS | Đạt (Passed) |

Bảng này có thể được cập nhật dựa trên kết quả thực tế trong quá trình triển khai và trình diễn.

### 3.6.12. Kết luận
Phần kiểm thử và tối ưu hóa hệ thống đảm bảo rằng hệ thống Parking IoT hoạt động đúng theo thiết kế, dữ liệu được truyền đi chính xác từ các thiết bị ESP32 lên AWS, các hàm Lambda hoàn thành đúng tác vụ, và giao diện Web/App hiển thị thông tin đầy đủ.

Thông qua quá trình kiểm thử, nhóm có thể phát hiện lỗi trong các luồng như tải ảnh lên, truyền dữ liệu cảm biến, xử lý ảnh, truy vấn API, hoặc xác thực người dùng. Thêm vào đó, việc tối ưu hóa hiệu suất và chi phí giúp hệ thống vận hành ổn định, hiệu quả và tiết kiệm trong điều kiện thực tế.

Sau khi hoàn tất kiểm thử, hệ thống Parking IoT có thể hỗ trợ các chức năng then chốt như giám sát chỗ đỗ xe theo thời gian thực, lưu trữ lịch sử ra vào, nhận diện biển số xe, hiển thị dữ liệu trực quan trên Web/App và quản trị hệ thống qua CloudWatch cùng AWS Budgets.
