---
title : "ESP32 Edge Devices"
date: 2026-05-13
weight : 2
chapter : false
pre : " <b> 3.2. </b> "
---

Phần này mô tả chi tiết giải pháp tích hợp các thiết bị biên phần cứng (ESP32 Edge Devices) đã được cài đặt và vận hành thực tế tại bãi đỗ xe để liên tục cung cấp dữ liệu thời gian thực cho **Giao diện Web App Smart Parking IoT** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)).

Các thiết bị biên đóng vai trò là "mắt thần" và "cảm biến đầu nguồn" của toàn bộ hệ thống Web App, bao gồm hai dòng thiết bị chính:
* **ESP32-CAM (Cổng vào / Cổng ra):** Tự động chụp hình ảnh xe khi phát hiện chuyển động, xin Presigned URL và tải ảnh trực tiếp lên Amazon S3 để kích hoạt quy trình nhận diện biển số (ANPR).
* **Thiết bị Cảm biến ESP32 (Ultrasonic / IR Sensor):** Lắp đặt tại từng vị trí đỗ xe, liên tục đo khoảng cách để xác định trạng thái đỗ (`available` hoặc `occupied`) và gửi thông điệp MQTT trực tiếp lên AWS IoT Core.

Mọi dữ liệu từ các thiết bị ESP32 được AWS Serverless tự động đồng bộ hóa lên **Web Dashboard**, giúp quản trị viên và người dùng theo dõi sơ đồ chỗ đỗ xe theo thời gian thực mà không bị độ trễ.

### 3.2.1. Vai trò của Thiết bị Biên trong Hệ thống Web App
Các thiết bị biên ESP32 đã triển khai đóng vai trò là lớp thu thập dữ liệu tự động tại bãi đỗ xe, chịu trách nhiệm tương tác trực tiếp với môi trường vật lý và đẩy thông tin lên đám mây AWS.

**Nhiệm vụ cốt lõi của Lớp Thiết bị Biên:**
* **Giám sát Cổng ra/vào:** Tự động phát hiện phương tiện, chụp ảnh độ phân giải cao và truyền tải ảnh lên Amazon S3 qua Presigned URL.
* **Cập nhật Trạng thái Chỗ đỗ:** Đo khoảng cách chính xác tại từng vị trí đỗ xe và phát tín hiệu MQTT cập nhật trạng thái lên AWS IoT Core.
* **Đồng bộ hóa Thời gian thực:** Đảm bảo độ trễ truyền dữ liệu từ phần cứng lên giao diện Web Dashboard dưới 1.5 giây.
* **Tự động hóa Kiểm soát Bãi xe:** Giảm thiểu 100% thao tác ghi chép thủ công của nhân viên bảo vệ.

### 3.2.2. Phân hệ ESP32-CAM (Chụp ảnh & Nhận diện Cổng)
Thiết bị ESP32-CAM được lắp đặt cố định tại cổng vào (Entrance Gate) và cổng ra (Exit Gate), được tối ưu hóa góc chụp và dải sáng để ghi lại biển số xe rõ nét nhất.

**Các thông số & Luồng hoạt động chính:**
* **Thiết bị phần cứng:** Module ESP32-CAM tích hợp cảm biến ảnh OV2640, đèn Flash LED trợ sáng và module kết nối Wi-Fi 2.4GHz.
* **Quy trình truyền tải ảnh:**
  `Xe tới cổng → Cảm biến phát hiện → ESP32-CAM chụp ảnh → Gọi API Gateway xin Presigned URL → Tải ảnh JPEG trực tiếp lên S3 Bucket`.

**Cấu trúc dữ liệu hình ảnh gửi từ ESP32-CAM:**
```json
{
  "device_id": "esp32_cam_entrance_01",
  "gate_type": "entrance",
  "image_name": "cam01_20260513_091528.jpg",
  "timestamp": "2026-05-13T09:15:28Z",
  "upload_status": "success"
}
```

### 3.2.3. Phân hệ Thiết bị Cảm biến ESP32 (Phát hiện Vị trí Đỗ)
Mỗi khu vực đỗ xe được trang bị các nút cảm biến ESP32 kết nối với cảm biến siêu âm (HC-SR04) hoặc cảm biến hồng ngoại.

**Cơ chế đo khoảng cách & Quyết định trạng thái:**
* Khoảng cách đo được `< 50 cm`: Xác định trạng thái đỗ là `occupied` (Đã có xe).
* Khoảng cách đo được `>= 50 cm`: Xác định trạng thái đỗ là `available` (Còn trống).

**Trạng thái Vị trí Đỗ trên Web Dashboard:**

| Trạng thái | Giá trị Payload | Hiển thị trên Web Dashboard |
|---|---|---|
| Chỗ đỗ trống | `available` | Ô màu xanh lục (Green) - Cho phép đặt chỗ / đỗ xe |
| Chỗ đã có xe | `occupied` | Ô màu đỏ (Red) - Phản ánh biển số xe đang đỗ |

**Luồng dữ liệu Cảm biến:**
`Cảm biến ESP32 → AWS IoT Core (MQTT over mTLS) → AWS IoT Rule → Lambda Sensor Processing → DynamoDB → Web App UI`.

### 3.2.4. Mã nguồn Firmware ESP32 & Kết nối AWS IoT Core
Firmware chạy trên ESP32 được lập trình bằng C++/Arduino Framework, sử dụng thư viện `PubSubClient` và `WiFiClientSecure` để thiết lập kết nối mã hóa mTLS an toàn với AWS IoT Core.

**Cấu trúc Firmware triển khai:**
- **Chứng chỉ Bảo mật:** Lưu giữ AWS Root CA, Device Certificate và Private Key trong bộ nhớ Flash mã hóa của ESP32.
- **Vòng lặp đo đạc (Loop Routine):** Đọc cảm biến định kỳ mỗi 2 giây, nếu phát hiện sự thay đổi trạng thái chỗ đỗ sẽ lập tức đóng gói payload JSON và `publish` tới topic MQTT `parking/slots/{slot_id}/status`.

### 3.2.5. Cơ chế Xử lý Presigned URL cho ESP32-CAM
Để tránh tình trạng nghẽn cổ chai tại các hàm Lambda khi tải các tập tin ảnh có dung lượng lớn, ESP32-CAM áp dụng cơ chế **Presigned URL**:
1. ESP32-CAM gửi một HTTP GET Request tới API Gateway endpoint `/api/camera/presigned-url`.
2. API Gateway kích hoạt hàm `Lambda Presigned URL` để khởi tạo một đường dẫn S3 Upload URL có thời hạn hiệu lực trong 5 phút.
3. ESP32-CAM nhận URL và phát lệnh HTTP PUT trực tiếp tải ảnh lên Amazon S3 Bucket mà không thông qua bất kỳ máy chủ trung gian nào.

### 3.2.6. Đồng bộ hóa Trạng thái Thiết bị trên Web Dashboard
Nhằm phục vụ công tác quản trị bãi xe, hệ thống Web App hiển thị bảng theo dõi sức khỏe và kết nối của từng thiết bị biên (Edge Device Health Monitoring):
* **Heartbeat Ping:** Mỗi thiết bị ESP32 gửi thông điệp heartbeat 60 giây/lần lên topic `parking/devices/heartbeat`.
* **Trạng thái Kết nối:** Web Dashboard đánh dấu màu Xanh (Online) hoặc Màu Xám (Offline) giúp quản trị viên kịp thời phát hiện sự cố phần cứng hoặc đứt gãy mạng Wi-Fi tại bãi xe.

### 3.2.7. Tối ưu hóa Năng lượng & Độ tin cậy Phần cứng
* **Cơ chế Lọc Nhiễu Cảm biến (Debouncing):** Thực hiện thuật toán lấy trung bình 5 lần đo liên tiếp trước khi quyết định thay đổi trạng thái, giúp loại bỏ tín hiệu nhiễu do người đi bộ qua lại.
* **Tự động Khôi phục Kết nối (Auto-Reconnect):** Tự động phát hiện mất mạng Wi-Fi/MQTT và thực hiện quy trình thử lại (Exponential Backoff) mà không làm treo thiết bị.

### 3.2.8. Kết luận
Các thiết bị biên ESP32-CAM và ESP32 Sensor đã chứng minh tính hiệu quả cao trong vận hành thực tế. Nhờ khả năng kết nối bảo mật trực tiếp với AWS IoT Core và S3, lớp phần cứng biên đã cung cấp dòng dữ liệu chuẩn xác, liên tục cho **Nền tảng Web App Smart Parking IoT**, làm cơ sở cho tính năng hiển thị sơ đồ chỗ đỗ thời gian thực và nhận diện biển số tự động.
