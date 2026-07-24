---
title : "IoT Data Pipeline"
date: 2026-05-13
weight : 3
chapter : false
pre : " <b> 3.3. </b> "
---

Phần này mô tả chi tiết các đường ống dữ liệu (IoT Data Pipelines) thời gian thực và phân tích dự báo AI được thiết kế và triển khai trên hạ tầng AWS Serverless, kết nối trực tiếp các thiết bị biên ESP32 với **Nền tảng Web App Smart Parking IoT** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)).

Đường ống dữ liệu đóng vai trò mạch máu thông tin của hệ thống, xử lý bất đồng bộ các luồng dữ liệu lớn: **Dữ liệu Hình ảnh phương tiện** (ANPR), **Dữ liệu Cảm biến vị trí đỗ**, **Truyền thông Socket Chatbox qua AWS AppSync**, **Trợ lý AI Chatbot** và **Mô hình Lambda AI Dự báo Lưu lượng Xe 7 Ngày Tới**.

### 3.3.1. Tổng quan Kiến trúc Đường ống Dữ liệu
Dữ liệu thu thập từ bãi đỗ xe trải qua chuỗi xử lý tự động hóa từ phần cứng biên đến giao diện người dùng trên Web App.

**Sơ đồ tổng quát Luồng dữ liệu:**
`ESP32 Edge Devices → AWS IoT Core / Amazon S3 → AWS Lambda Microservices (ANPR, AI Chatbot, AI Forecast) → Amazon Rekognition / DynamoDB → AWS AppSync (WebSockets) / API Gateway → Web App UI`.

**Các Luồng Dữ liệu Chính trên Hệ thống:**

| Luồng Dữ liệu | Đầu vào (Input) | Các Dịch vụ AWS Xử lý | Đầu ra trên Web App (Output) |
|---|---|---|---|
| **Image ANPR Pipeline** | Ảnh chụp từ ESP32-CAM | S3 Bucket, Lambda, Amazon Rekognition | Nhật ký xe ra/vào, biển số trích xuất & Ảnh hiển thị |
| **Sensor Status Pipeline** | Payload MQTT từ ESP32 | AWS IoT Core, IoT Rule, Lambda, DynamoDB, AppSync Subscription | Sơ đồ vị trí đỗ xanh/đỏ cập nhật thời gian thực qua WebSockets |
| **AppSync WebSockets Chatbox** | Tin nhắn Socket từ Web Chatbox | AWS AppSync WebSockets, Lambda AI Chatbot, DynamoDB | Phản hồi trò chuyện thời gian thực cho khung Chatbox Web |
| **AI 7-Day Traffic Forecast** | Lịch sử đỗ xe từ `VehicleLogs` | EventBridge Cron, Lambda AI Forecast, DynamoDB | Biểu đồ dự báo mật độ & lưu lượng xe 7 ngày tới trên Admin Dashboard |

### 3.3.2. Đường ống Xử lý Dữ liệu Hình ảnh (Image ANPR Pipeline)
Luồng xử lý hình ảnh xe vào/ra bãi đỗ xe được tối ưu hóa để đạt tốc độ trích xuất biển số xe ngắn nhất:

1. **Khởi tạo:** Xe tiến vào vùng quét của cổng vào/ra, ESP32-CAM phát hiện và chụp ảnh.
2. **Xin Presigned URL:** ESP32-CAM gửi request HTTP GET tới API Gateway `/api/camera/presigned-url`.
3. **Cấp URL ngắn hạn:** Hàm `Lambda Presigned URL` khởi tạo link upload S3 có hiệu lực trong 5 phút.
4. **Tải ảnh lên S3:** ESP32-CAM đẩy tập tin ảnh JPEG trực tiếp vào bucket `s3://smart-parking-vehicle-images/entrance/`.
5. **Kích hoạt Sự kiện:** S3 tạo ra sự kiện `s3:ObjectCreated:Put` lập tức kích hoạt hàm `Lambda Image Processing`.
6. **Nhận diện Biển số (ANPR):** Lambda truyền buffer ảnh sang **Amazon Rekognition** thông qua API `DetectText`.
7. **Lưu trữ & Phản hồi:** Kết quả trích xuất chuỗi biển số (ví dụ `51H-98765`, confidence `98.2%`) được ghi vào DynamoDB table `VehicleLogs` và đồng bộ qua API đẩy tới Web Dashboard.

### 3.3.3. Cấu hình Thư mục & Metadata trong Amazon S3
Hình ảnh được tổ chức có hệ thống trong S3 Bucket để phục vụ tra cứu hình ảnh trên Web App:

**Cấu trúc thư mục Bucket S3:**
```text
smart-parking-vehicle-images/
├── entrance/
│   ├── cam_ent_01_20260513_091528.jpg
│   └── cam_ent_01_20260513_093000.jpg
└── exit/
    ├── cam_ext_01_20260513_101500.jpg
    └── cam_ext_01_20260513_104520.jpg
```

### 3.3.4. Xử lý Trực quan với Amazon Rekognition
Hàm `Lambda Image Processing` gửi ảnh tới **Amazon Rekognition** để phát hiện các khối văn bản (Bounding Boxes) nằm trong vùng biển số xe:

```python
import boto3

rekognition = boto3.client('rekognition')

def detect_license_plate(bucket, key):
    response = rekognition.detect_text(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}}
    )
    text_detections = response['TextDetections']
    for text in text_detections:
        if text['Type'] == 'LINE' and text['Confidence'] > 90.0:
            return text['DetectedText'], text['Confidence']
    return "UNKNOWN", 0.0
```

### 3.3.5. Đường ống Xử lý Dữ liệu Cảm biến & AWS AppSync Subscriptions
Luồng dữ liệu trạng thái chỗ đỗ xe hoạt động liên tục theo thời gian thực:

1. **Đọc Cảm biến:** ESP32 Cảm biến siêu âm đo khoảng cách tại ô đỗ `A01`.
2. **Gửi tin nhắn MQTT:** Nếu trạng thái chuyển đổi từ `available` sang `occupied`, ESP32 publish payload JSON tới topic MQTT `parking/slots/A01/status`.
3. **Chuyển hướng bởi AWS IoT Rule:** SQL Rule trên AWS IoT Core lọc tin nhắn và kích hoạt `Lambda Sensor Processing`.
4. **Cập nhật CSDL & Đẩy WebSockets:** Lambda cập nhật bảng DynamoDB `ParkingSlots` và gửi một **AWS AppSync Mutation**, tự động kích hoạt **GraphQL Subscription** (`onUpdateParkingSlot`).
5. **Đồng bộ Web Dashboard:** Mọi trình duyệt Web đang mở sơ đồ đỗ xe sẽ tự động đổi màu ô đỗ `A01` qua kênh truyền WebSockets mà không cần F5 reload trang.

### 3.3.6. Đường ống Chatbox WebSockets qua AWS AppSync & Lambda AI Chatbot
Đối với phân hệ Chatbox tương tác thời gian thực:

1. **Gửi tin nhắn Socket:** Trình duyệt Web gửi GraphQL Mutation `sendMessage` qua kết nối **AWS AppSync WebSockets**.
2. **Xử lý AI Backend:** AppSync định tuyến tin nhắn tới `Lambda AI Chatbot`, kích hoạt thuật toán phân tích intent và truy vấn dữ liệu từ DynamoDB.
3. **Lưu nhật ký:** Tin nhắn hội thoại được ghi vào bảng DynamoDB `ChatMessages`.
4. **Đẩy phản hồi tức thì:** AWS AppSync phát sự kiện Subscription `onNewChatMessage` truyền dữ liệu phản hồi ngược lại cho khung Chatbox trên Web App trong vài miligiây.

### 3.3.7. Đường ống Dữ liệu Mô hình AI Dự báo Lưu lượng Xe 7 Ngày Tới
Phân hệ phân tích và dự báo xu hướng đỗ xe:

1. **Thu thập Dữ liệu Lịch sử:** Hàm `Lambda AI 7-Day Forecast` chạy định kỳ (hoặc kích hoạt qua API) quét toàn bộ nhật ký xe ra vào trong 30 ngày từ bảng DynamoDB `VehicleLogs`.
2. **Phân tích Chuỗi Thời gian (Time-series Forecasting):** Mô hình AI thực hiện thuật toán dự báo tính toán số lượng lượt xe dự kiến cho 7 ngày tiếp theo (Day +1 đến Day +7) theo từng khung giờ và khu vực đỗ.
3. **Lưu trữ Kết quả Dự báo:** Kết quả được lưu vào bảng DynamoDB `TrafficForecasts`.
4. **Trực quan hóa trên Admin Dashboard:** Giao diện Web App gọi API Gateway `GET /api/ai/forecast-7days` để lấy dữ liệu và hiển thị biểu đồ đường (Line Chart) xu hướng lưu lượng xe 7 ngày tới, giúp nhà quản lý chủ động điều phối nhân sự và vị trí đỗ.

### 3.3.8. Cơ chế Xử lý Lỗi & Dead Letter Queue (DLQ)
Đường ống dữ liệu tích hợp sẵn các cơ chế chịu lỗi (Fault Tolerance) với Amazon SQS Dead Letter Queues (DLQ) và DynamoDB exponential backoff.

### 3.3.9. Kết luận
Đường ống dữ liệu IoT Data Pipeline kết hợp cùng **AWS AppSync WebSockets Chatbox**, **Lambda AI Chatbot** và **Mô hình Lambda AI Dự báo Lưu lượng Xe 7 Ngày Tới** đã kiến tạo nên một hệ thống truyền tải và phân tích dữ liệu đỗ xe thông minh hàng đầu.
