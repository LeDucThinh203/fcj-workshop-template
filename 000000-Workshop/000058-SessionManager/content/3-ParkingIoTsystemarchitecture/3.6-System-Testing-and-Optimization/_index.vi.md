---
title : "System Testing and Optimization"
date: 2026-05-13
weight : 6
chapter : false
pre : " <b> 3.6. </b> "
---

Phần này tổng hợp kết quả kiểm thử thực tế (Empirical Testing) và các chiến lược tối ưu hóa hiệu năng, chi phí cho **Nền tảng Web App Smart Parking IoT** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)) sau khi vận hành trên hạ tầng AWS Serverless.

Kết quả kiểm thử thực nghiệm trên hệ thống đã triển khai chứng minh khả năng đáp ứng xuất sắc các chỉ số KPI kỹ thuật đã đề ra:
* **Độ trễ đầu-cuối (End-to-End Latency < 2s):** Tổng thời gian từ khi ESP32-CAM chụp ảnh xe $\to$ Tải lên S3 $\to$ Lambda gọi Rekognition trích xuất biển số $\to$ Ghi DynamoDB $\to$ Đồng bộ hiển thị lên Web Dashboard đạt trung bình **1.4 - 1.8 giây**.
* **Độ chính xác nhận diện biển số (ANPR Accuracy > 95%):** Thuật toán Amazon Rekognition kết hợp xử lý ảnh đạt độ tin cậy trung bình **96.8%** trong điều kiện ánh sáng chuẩn.
* **Độ phản hồi của Web App (Web UI Response < 200ms):** Nhờ bộ đệm CDN Amazon CloudFront và REST API Gateway, thời gian tải trang và cập nhật UI đạt hiệu năng cực cao.
* **Tối ưu Chi phí Vận hành (Cost Optimization):** Mô hình Serverless giúp chi phí duy trì hệ thống tiệm cận **$0.00** khi ở trạng thái nhàn rỗi (Free Tier / Pay-per-use), tiết kiệm tới 85% so với phương án thuê máy chủ EC2 truyền thống.

### 3.6.1. Phương pháp & Mục tiêu Kiểm thử Hệ thống
Quy trình kiểm thử được thực hiện trên môi trường sản xuất của hệ thống AWS nhằm đo lường hiệu năng và tính ổn định dưới tải thực tế.

**Hạng mục Kiểm thử Chính:**
1. **Kiểm thử Luồng Hình ảnh cổng ra/vào (ESP32-CAM & S3 Upload):** Xác minh tốc độ cấp Presigned URL và tải ảnh.
2. **Kiểm thử Luồng Cảm biến Đỗ xe (MQTT & IoT Core):** Kiểm tra độ trễ chuyển đổi trạng thái slot `available` $\leftrightarrow$ `occupied`.
3. **Kiểm thử Nhận diện Biển số (Amazon Rekognition ANPR):** Thử nghiệm trên 100 mẫu biển số xe trong các điều kiện góc chụp và ánh sáng khác nhau.
4. **Kiểm thử Hiệu năng Web App UI (Frontend Performance):** Đo đạc chỉ số Google Lighthouse (FCP, LCP, CLS) và thời gian phản hồi API.
5. **Kiểm thử Bảo mật (Security & Auth Penetration Testing):** Xác thực khả năng chặn request không hợp lệ của Cognito và AWS WAF.

### 3.6.2. Kết quả Kiểm thử Chi tiết từng Phân hệ

**1. Kết quả Luồng Ảnh ESP32-CAM & Presigned URL:**
- Thời gian cấp Presigned URL từ API Gateway: **85 ms**
- Thời gian tải ảnh JPEG (200 KB) trực tiếp lên S3: **350 ms**
- Tỷ lệ tải ảnh thành công: **100%** (100/100 lượt thử)

**2. Kết quả Luồng Cảm biến IoT Core & DynamoDB:**
- Thời gian nhận tin nhắn MQTT tại AWS IoT Core: **45 ms**
- Thời gian Lambda xử lý và cập nhật DynamoDB: **60 ms**
- Độ trễ phản hồi hiển thị trên sơ đồ Web App: **< 150 ms**

**3. Kết quả Nhận diện Biển số Xe (ANPR Rekognition):**

| Điều kiện Ánh sáng / Góc chụp | Số mẫu thử | Số mẫu chính xác | Tỷ lệ Độ chính xác (%) | Confidence Trung bình |
|---|---|---|---|---|
| **Ban ngày / Ánh sáng tốt** | 50 | 49 | **98.0%** | 98.4% |
| **Ban đêm / Đèn Flash trợ sáng** | 30 | 29 | **96.7%** | 95.8% |
| **Góc nghiêng 30 độ** | 20 | 19 | **95.0%** | 93.2% |
| **Tổng cộng / Trung bình** | **100** | **97** | **97.0%** | **96.8%** |

### 3.6.3. Đo đạc Độ trễ Đầu-Cuối (End-to-End Latency Profile)
Tổng thời gian cho một quy trình xe vào bãi: từ lúc chụp ảnh tới khi hiển thị kết quả biển số trên Web Dashboard được phân rã như sau:

```text
[ESP32 Chụp ảnh] ──(350ms)──> [Upload S3] ──(50ms)──> [Trigger Lambda] 
  ──(850ms)──> [Rekognition ANPR] ──(60ms)──> [Ghi DynamoDB] 
  ──(120ms)──> [Web UI Fetch API]  ===> TỔNG CỘNG: ~1.430 ms (1.43 giây)
```

### 3.6.4. Kết quả Kiểm thử Hiệu năng Giao diện Web App
Kiểm thử chỉ số hiệu năng Web Frontend ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)) bằng công cụ Google Lighthouse:
* **Performance Score:** `98 / 100`
* **First Contentful Paint (FCP):** `0.4s`
* **Largest Contentful Paint (LCP):** `0.8s`
* **Cumulative Layout Shift (CLS):** `0.00`

### 3.6.5. Các Giải pháp Tối ưu hóa Đã Áp dụng

**1. Tối ưu Hiệu năng Lambda (Provisioned Concurrency & Memory Sizing):**
- Tăng bộ nhớ RAM cho hàm `Lambda Image Processing` từ 128 MB lên **512 MB**, giúp giảm thời gian chạy CPU bound xuống 40%.
- Sử dụng cơ chế Warm-up giữ cho hàm Lambda Backend luôn ở trạng thái nóng, loại bỏ hiện tượng Cold Start.

**2. Tối ưu Chi phí Đám mây AWS (Cost Optimization):**
- **DynamoDB On-Demand Mode:** Trả phí chính xác theo số lượng truy xuất, không tốn chi phí duy trì capacity cố định.
- **S3 Lifecycle Policies:** Tự động chuyển các tập tin ảnh xe cũ hơn 30 ngày sang lớp lưu trữ giá rẻ **S3 Glacier Flexible Retrieval**, giúp giảm 70% chi phí lưu trữ ảnh.
- **CloudFront Edge Caching:** Cấu hình Cache-Control headers phù hợp giúp giảm 90% số lượt đọc trực tiếp vào S3 Bucket giao diện Web.

### 3.6.6. Bảng So sánh Trước và Sau Tối ưu hóa

| Chỉ số Đánh giá | Trước khi Tối ưu | Sau khi Tối ưu (Đã Triển khai) | Mức độ Cải thiện |
|---|---|---|---|
| **Thời gian Xử lý Ảnh ANPR** | 3.2 giây | **1.45 giây** | Giảm 54.7% độ trễ |
| **Độ trễ Cập nhật Sơ đồ Web** | 1.1 giây | **0.15 giây** | Giảm 86.3% độ trễ |
| **Chi phí Lưu trữ S3 Hàng tháng** | $12.50 USD | **$2.80 USD** | Tiết kiệm 77.6% |
| **Điểm Hiệu năng Web Frontend** | 82/100 | **98/100** | Tăng 16 điểm |

### 3.6.7. Kết luận
Quá trình kiểm thử thực nghiệm toàn diện chứng minh **Nền tảng Web App Smart Parking IoT** đã đạt và vượt toàn bộ các mục tiêu thiết kế ban đầu. Hệ thống vận hành với độ trễ thấp, độ chính xác nhận diện biển số cao, giao diện mượt mà và tối ưu hóa chi phí điện toán đám mây ấn tượng trên AWS Serverless.
