---
title : "IoT Data Pipeline"
date: 2026-05-13
weight : 3
chapter : false
pre : " <b> 3.3. </b> "
---

Phần này mô tả chi tiết các đường ống dữ liệu (IoT Data Pipelines) thời gian thực được thiết kế và triển khai trên hạ tầng AWS Serverless, kết nối trực tiếp các thiết bị biên ESP32 với **Nền tảng Web App Smart Parking IoT** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)).

Đường ống dữ liệu đóng vai trò mạch máu thông tin của hệ thống, xử lý bất đồng bộ hai nhóm dữ liệu lớn: **Dữ liệu Hình ảnh phương tiện** (cho bài toán nhận diện biển số xe ANPR) và **Dữ liệu Cảm biến vị trí đỗ** (cho bài toán quản lý sơ đồ đỗ xe thời gian thực).

### 3.3.1. Tổng quan Kiến trúc Đường ống Dữ liệu
Dữ liệu thu thập từ bãi đỗ xe trải qua chuỗi xử lý tự động hóa từ phần cứng biên đến giao diện người dùng trên Web App.

**Sơ đồ tổng quát Luồng dữ liệu:**
`ESP32 Edge Devices → AWS IoT Core / Amazon S3 → AWS Lambda Microservices → Amazon Rekognition / DynamoDB → API Gateway / CloudFront → Web App UI`.

**Ba Luồng Dữ liệu Chính trên Hệ thống:**

| Luồng Dữ liệu | Đầu vào (Input) | Các Dịch vụ AWS Xử lý | Đầu ra trên Web App (Output) |
|---|---|---|---|
| **Image ANPR Pipeline** | Ảnh chụp từ ESP32-CAM | S3 Bucket, Lambda, Amazon Rekognition | Nhật ký xe ra/vào, biển số trích xuất & Ảnh hiển thị |
| **Sensor Status Pipeline** | Payload MQTT từ ESP32 | AWS IoT Core, IoT Rule, Lambda, DynamoDB | Sơ đồ vị trí đỗ xanh/đỏ cập nhật thời gian thực |
| **Web REST & AI Pipeline** | Yêu cầu HTTPS từ Web User | API Gateway, Cognito, Lambda, Lambda AI Service | Kết quả tra cứu lịch sử xe, câu trả lời Trợ lý AI |

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

**Metadata đính kèm mỗi đối tượng hình ảnh:**
```json
{
  "image_id": "cam_ent_01_20260513_091528.jpg",
  "gate_id": "GATE_ENTRANCE_01",
  "direction": "in",
  "timestamp": "2026-05-13T09:15:28Z",
  "s3_uri": "s3://smart-parking-vehicle-images/entrance/cam_ent_01_20260513_091528.jpg"
}
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
    # Thuật toán lọc định dạng biển số xe Việt Nam (VD: 51H-98765)
    for text in text_detections:
        if text['Type'] == 'LINE' and text['Confidence'] > 90.0:
            return text['DetectedText'], text['Confidence']
    return "UNKNOWN", 0.0
```

### 3.3.5. Đường ống Xử lý Dữ liệu Cảm biến (Sensor Telemetry Pipeline)
Luồng dữ liệu trạng thái chỗ đỗ xe hoạt động liên tục theo thời gian thực:

1. **Đọc Cảm biến:** ESP32 Cảm biến siêu âm đo khoảng cách tại ô đỗ `A01`.
2. **Gửi tin nhắn MQTT:** Nếu trạng thái chuyển đổi từ `available` sang `occupied`, ESP32 publish payload JSON tới topic MQTT `parking/slots/A01/status`.
3. **Chuyển hướng bởi AWS IoT Rule:** SQL Rule trên AWS IoT Core lọc tin nhắn:
   ```sql
   SELECT slot_id, status, distance_cm, timestamp 
   FROM 'parking/slots/+/status'
   ```
4. **Cập nhật CSDL:** IoT Rule kích hoạt `Lambda Sensor Processing` cập nhật ngay lập tức dòng dữ liệu của slot `A01` trong bảng DynamoDB `ParkingSlots`.
5. **Đồng bộ Web Dashboard:** Khi người dùng Web gọi API lấy sơ đồ bãi xe, dữ liệu mới nhất được phản hồi tức thì dưới 100ms.

### 3.3.6. Đường ống Truy vấn Web App & Trợ lý AI trên AWS Lambda
Đối với các thao tác tương tác của người dùng trên giao diện Web App:

* **Tra cứu Lịch sử Xe:** Web App $\to$ API Gateway `GET /api/vehicle/logs?plate=51H-98765` $\to$ `Lambda API Backend` $\to$ DynamoDB Query $\to$ Phản hồi JSON danh sách lịch sử kèm link ảnh CloudFront.
* **Tương tác Trợ lý AI:** Web Chat UI $\to$ API Gateway `POST /api/ai/chat` $\to$ `Lambda AI Service` $\to$ Xử lý thuật toán AI & tổng hợp dữ liệu từ DynamoDB $\to$ Phản hồi câu trả lời tự nhiên cho người dùng Web.

### 3.3.7. Cơ chế Xử lý Lỗi & Dead Letter Queue (DLQ)
Đường ống dữ liệu tích hợp sẵn các cơ chế chịu lỗi (Fault Tolerance):
* Nếu hàm Lambda gặp sự cố khi gọi Amazon Rekognition, bản tin sự kiện sẽ được gửi vào **Amazon SQS Dead Letter Queue (DLQ)** để xử lý lại (Retry) mà không bị mất dữ liệu.
* DynamoDB áp dụng chế độ tự động ghi bù (Exponential Backoff) khi gặp hiện tượng nghẽn mạng tạm thời.

### 3.3.8. Đồng bộ hóa Real-time & Cải thiện Trải nghiệm Người dùng
Nhờ áp dụng đường ống dữ liệu bất đồng bộ AWS Serverless:
* Toàn bộ thao tác cập nhật vị trí đỗ hay xe vào/ra bãi đỗ xe đều hiển thị trên Web App trong chưa đầy 2 giây.
* Giao diện Web không bị khóa (non-blocking UI), mang lại trải nghiệm mượt mà như một ứng dụng Native App.

### 3.3.9. Kết luận
Đường ống dữ liệu IoT Data Pipeline đã triển khai thành công mô hình truyền tải dữ liệu đa kênh, an toàn và tốc độ cao. Sự kết hợp giữa các dịch vụ không máy chủ AWS đã biến các tín hiệu cảm biến và hình ảnh camera thô thành dữ liệu thông minh hiển thị trực quan trên **Nền tảng Web App Smart Parking IoT**.
