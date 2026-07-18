---
title : "User Interface and Security"
date: 2026-05-13
weight : 4
chapter : false
pre : " <b> 3.4. </b> "
---

Phần này mô tả cách triển khai giao diện người dùng và các cơ chế bảo mật cho Hệ thống IoT Bãi đỗ xe Thông minh. Giao diện Web/App cho phép người dùng giám sát trạng thái chỗ đỗ xe, xem lịch sử xe ra vào, kiểm tra thông tin biển số xe và truy cập dữ liệu hệ thống.

Ngoài ra, hệ thống sử dụng các dịch vụ bảo mật như Amazon Cognito, AWS WAF, IAM, API Gateway Authorizer và CloudFront HTTPS để đảm bảo người dùng được xác thực, dữ liệu được bảo vệ và các dịch vụ AWS chỉ được cấp các quyền cần thiết.

### 3.4.1. Tổng quan về Giao diện Web/App
Giao diện Web/App là nơi chính để người dùng tương tác với hệ thống Parking IoT. Thông qua giao diện này, người dùng có thể xem dữ liệu đỗ xe theo thời gian thực, kiểm tra trạng thái của từng chỗ đỗ và giám sát lịch sử xe ra vào.

Các tính năng chính của giao diện bao gồm:
* Đăng nhập người dùng.
* Xem tổng số chỗ đỗ xe.
* Xem số chỗ trống và chỗ đã có xe.
* Xem trạng thái của từng chỗ đỗ xe.
* Xem lịch sử xe ra vào.
* Xem hình ảnh xe được lưu trữ trong Amazon S3.
* Xem thông tin biển số xe đã được nhận diện.
* Tìm kiếm xe theo biển số.
* Xem thống kê hoạt động của bãi đỗ xe.
* Gửi câu hỏi đến AI Service nếu tích hợp Amazon Bedrock.

Giao diện có thể được phát triển bằng HTML/CSS/JavaScript hoặc các framework như React và Next.js. Sau khi build, các tệp tĩnh được lưu trữ trong Amazon S3 và phân phối đến người dùng thông qua Amazon CloudFront.

### 3.4.2. Triển khai Giao diện với Amazon S3 Static Website
Amazon S3 được sử dụng để lưu trữ các tệp tĩnh của giao diện Web/App, bao gồm:
* Tệp HTML.
* Tệp CSS.
* Tệp JavaScript.
* Hình ảnh, biểu tượng (icons) và các tài nguyên giao diện khác.

**Luồng triển khai giao diện:**
`Mã nguồn Web/App → Build Project → Tải tệp tĩnh lên Amazon S3 → CloudFront phân phối nội dung đến người dùng`

**Cấu trúc thư mục build mẫu:**
```text
web-app-build/
├── index.html
├── assets/
│   ├── style.css
│   ├── app.js
│   └── logo.png
└── dashboard/
    └── index.html
```

Amazon S3 cung cấp một giải pháp lưu trữ giao diện web đơn giản và tiết kiệm chi phí, rất phù hợp với kiến trúc serverless.

### 3.4.3. Phân phối Website với Amazon CloudFront
Amazon CloudFront được sử dụng để phân phối giao diện Web/App đến người dùng với tốc độ truy cập nhanh hơn. CloudFront đóng vai trò là một lớp trung gian giữa người dùng và Amazon S3.

**Luồng truy cập website:**
`Người dùng → Route 53 → CloudFront → Amazon S3 Static Website`

**Vai trò của CloudFront:**
* Cải thiện tốc độ truy cập trang web.
* Giảm độ trễ cho người dùng.
* Hỗ trợ HTTPS cho kết nối an toàn.
* Giảm tải trực tiếp lên Amazon S3.
* Tích hợp với AWS WAF để bảo vệ trang web.

Khi người dùng truy cập website, CloudFront sẽ lấy nội dung từ S3 và lưu vào bộ đệm (cache) tại các edge location. Điều này giúp trang web phản hồi nhanh hơn, đặc biệt khi có nhiều người dùng truy cập cùng lúc.

### 3.4.4. Quản lý Tên miền với Amazon Route 53
Amazon Route 53 được sử dụng để quản lý tên miền của hệ thống. Thay vì truy cập vào một URL CloudFront dài dòng, người dùng có thể truy cập hệ thống qua một tên miền thân thiện.

**Ví dụ:**
`parking.example.com → CloudFront Distribution`

**Vai trò của Route 53:**
* Quản lý DNS cho hệ thống.
* Định tuyến người dùng đến CloudFront.
* Cung cấp một địa chỉ trang web thân thiện với người dùng.
* Hỗ trợ cấu hình tên miền cho môi trường demo hoặc production.

**Luồng truy cập với Route 53:**
`Người dùng nhập tên miền → Route 53 → CloudFront → S3 Static Website`

### 3.4.5. Bảo vệ Website với AWS WAF
AWS WAF được đặt trước CloudFront để bảo vệ trang web khỏi các yêu cầu bất thường hoặc độc hại. WAF giúp tăng cường bảo mật hệ thống khi trang web được công khai trên Internet.

**Luồng bảo vệ website:**
`Người dùng → Route 53 → CloudFront + AWS WAF → Amazon S3 Static Website`

**AWS WAF có thể giúp:**
* Chặn các địa chỉ IP đáng ngờ.
* Chặn các yêu cầu có định dạng bất thường.
* Giới hạn số lượng yêu cầu từ một nguồn (rate limiting).
* Bảo vệ trang web khỏi các cuộc tấn công web phổ biến.
* Tạo các quy tắc (rules) để lọc các yêu cầu không hợp lệ.

Trong hệ thống Parking IoT, WAF bảo vệ lớp giao diện người dùng trước khi các yêu cầu được chuyển tiếp đến Web/App hoặc API.

### 3.4.6. Xác thực Người dùng với Amazon Cognito
Amazon Cognito được sử dụng để xác thực người dùng trước khi cho phép họ truy cập vào các tính năng quản lý bãi đỗ xe. Người dùng phải đăng nhập bằng tài khoản được cấp.

**Luồng xác thực:**
`Người dùng → Web/App → Amazon Cognito → Nhận Token → API Gateway → Lambda Backend`

**Các bước xử lý:**
1. Người dùng mở Web/App.
2. Người dùng nhập tên đăng nhập và mật khẩu.
3. Web/App gửi thông tin đăng nhập đến Amazon Cognito.
4. Cognito xác minh thông tin người dùng.
5. Nếu đăng nhập thành công, Cognito trả về một token.
6. Web/App gửi token kèm theo các yêu cầu đến API Gateway.
7. API Gateway xác thực token bằng Cognito Authorizer.
8. Nếu token hợp lệ, yêu cầu được chuyển tiếp đến Lambda Backend.

Amazon Cognito giúp hệ thống quản lý quá trình đăng nhập một cách an toàn và dễ dàng tích hợp với API Gateway.

### 3.4.7. Phân quyền Người dùng (Authorization)
Hệ thống có thể chia người dùng thành nhiều vai trò (roles) khác nhau để kiểm soát quyền truy cập. Mỗi vai trò được phép sử dụng các chức năng khác nhau trong Web/App.

**Ví dụ về kiểm soát truy cập dựa trên vai trò:**

| Vai trò | Quyền truy cập |
|------|-------------------|
| User | Xem trạng thái đỗ xe và số chỗ trống |
| Manager | Xem lịch sử xe, thống kê và dữ liệu biển số |
| Admin | Quản lý người dùng, cấu hình hệ thống và truy cập tất cả dữ liệu |

Việc phân quyền giúp ngăn chặn người dùng truy cập vào các chức năng không phù hợp với vai trò của họ. Ví dụ: người dùng bình thường chỉ có thể xem trạng thái đỗ xe, trong khi Admin có thể quản lý tài khoản và cài đặt hệ thống.

### 3.4.8. Bảo mật API với API Gateway Authorizer
API Gateway là cổng giao tiếp giữa Web/App và Lambda Backend. Để bảo vệ các API, hệ thống sử dụng Cognito Authorizer để xác minh token của người dùng trước khi cho phép truy cập API.

**Luồng bảo mật API:**
`Web/App → API Gateway → Cognito Authorizer → Lambda Backend → DynamoDB`

**Cách hoạt động:**
1. Web/App gửi yêu cầu đến API Gateway.
2. Yêu cầu bao gồm một token từ Amazon Cognito.
3. API Gateway xác thực token bằng Cognito Authorizer.
4. Nếu token hợp lệ, yêu cầu được chuyển tiếp đến Lambda.
5. Nếu token không hợp lệ, API Gateway từ chối yêu cầu.

**Các API cần được bảo vệ:**

| API Endpoint | Mục đích |
|--------------|---------|
| `/parking/slots` | Lấy trạng thái chỗ đỗ xe |
| `/vehicle/logs` | Xem lịch sử xe ra vào |
| `/vehicle/search` | Tìm kiếm xe theo biển số |
| `/ai/query` | Gửi câu hỏi đến AI Service |
| `/admin/users` | Quản lý người dùng |

Cách tiếp cận này giúp ngăn chặn các truy cập trái phép vào dữ liệu đỗ xe.

### 3.4.9. Kiểm soát Truy cập với IAM
IAM được sử dụng để kiểm soát quyền giữa các dịch vụ AWS. Mỗi dịch vụ chỉ được cấp các quyền cần thiết theo nguyên tắc Đặc quyền Tối thiểu (Least Privilege).

**Ví dụ về các quyền IAM:**

| Thành phần | Quyền cần thiết |
|-----------|---------------------|
| Lambda Backend | Đọc và ghi dữ liệu DynamoDB |
| Lambda Image Processing | Đọc hình ảnh từ S3, gọi Rekognition và ghi vào DynamoDB |
| Lambda Presigned URL | Tạo Presigned URL cho S3 |
| Lambda Sensor Processing | Ghi dữ liệu cảm biến vào DynamoDB |
| Lambda AI Service | Đọc DynamoDB và gọi Amazon Bedrock |
| API Gateway | Gọi Lambda (Invoke) |
| IoT Rule | Kích hoạt (Trigger) Lambda Sensor Processing |

**Các nguyên tắc quan trọng:**
* Không cấp các quyền quá rộng.
* Mỗi hàm Lambda chỉ nên có các quyền cần thiết cho tác vụ của nó.
* Các thiết bị ESP32 không được lưu trữ trực tiếp AWS Access Keys hoặc Secret Keys.

IAM giúp giảm thiểu rủi ro bảo mật nếu một thành phần bị lỗi hoặc bị truy cập trái phép.

### 3.4.10. Tải Hình ảnh An toàn với Presigned URL
ESP32 Camera không được cấp quyền AWS trực tiếp để tải hình ảnh lên S3. Thay vào đó, hệ thống sử dụng Presigned URLs.

**Luồng tải hình ảnh an toàn:**
`ESP32 Camera → API Gateway → Lambda tạo Presigned URL → ESP32 Camera tải hình ảnh lên S3`

**Lợi ích của Presigned URLs:**
* Không cần lưu trữ AWS Access Keys trên ESP32 Camera.
* URL chỉ có hiệu lực trong một khoảng thời gian ngắn.
* Việc tải lên bị giới hạn ở một tệp hoặc một bucket cụ thể.
* Giảm thiểu rủi ro nếu thiết bị bị truy cập trái phép.

**Ví dụ:**
* Presigned URL có hiệu lực trong 5 phút.
* ESP32 Camera chỉ có thể tải hình ảnh vào thư mục `entrance/` hoặc `exit/`.

Phương pháp này rất phù hợp cho các hệ thống IoT vì các thiết bị biên thường có tài nguyên hạn chế và không nên lưu trữ thông tin xác thực nhạy cảm.

### 3.4.11. Bảo mật Kết nối Thiết bị IoT
Đối với các cảm biến ESP32, dữ liệu được gửi đến AWS IoT Core thông qua MQTT. Để bảo mật kết nối, mỗi thiết bị cần có một chứng chỉ riêng và một IoT Policy.

**Các thành phần bảo mật bao gồm:**
* IoT Thing đại diện cho thiết bị.
* Chứng chỉ Thiết bị (Device Certificate).
* Khóa riêng tư (Private Key).
* IoT Policy.
* Một topic MQTT riêng biệt cho mỗi thiết bị.

**Topic mẫu:**
`parking/slot/A01/status`

**Nguyên tắc cấp quyền mẫu:**
* Cảm biến ESP32 A01 chỉ có thể gửi dữ liệu đến topic `parking/slot/A01/status`.
* Cảm biến ESP32 B03 chỉ có thể gửi dữ liệu đến topic `parking/slot/B03/status`.

Việc giới hạn các topic MQTT giúp giảm rủi ro thiết bị gửi dữ liệu sai hoặc bị truy cập trái phép.

### 3.4.12. Luồng Bảo mật Tổng thể
**Luồng truy cập của người dùng:**
`Người dùng → Route 53 → CloudFront → AWS WAF → S3 Static Website → Cognito → API Gateway → Lambda → DynamoDB`

**Luồng tải hình ảnh từ ESP32 Camera:**
`ESP32 Camera → API Gateway → Lambda Presigned URL → Amazon S3 → Lambda Image Processing`

**Luồng dữ liệu cảm biến:**
`Cảm biến ESP32 → AWS IoT Core → IoT Rule → Lambda Sensor Processing → DynamoDB`

**Các lớp bảo mật chính:**

| Lớp Bảo mật | Dịch vụ AWS |
|----------------|--------------|
| Bảo vệ website | CloudFront, AWS WAF, HTTPS |
| Xác thực người dùng | Amazon Cognito |
| Bảo vệ API | API Gateway Authorizer |
| Kiểm soát quyền dịch vụ | IAM |
| Tải hình ảnh an toàn | Presigned URL |
| Bảo mật thiết bị IoT | IoT Certificate và IoT Policy |
| Giám sát log bảo mật | CloudWatch Logs |

### 3.4.13. Kết luận
Lớp giao diện người dùng và bảo mật cho phép hệ thống Parking IoT phục vụ người dùng một cách rõ ràng, an toàn và dễ quản lý. Giao diện Web/App được lưu trữ trên Amazon S3 và phân phối qua CloudFront, giúp người dùng truy cập hệ thống nhanh chóng và đáng tin cậy.

Các dịch vụ như Amazon Cognito, AWS WAF, IAM, API Gateway Authorizer và Presigned URLs giúp bảo vệ hệ thống khỏi các truy cập trái phép, đảm bảo an toàn dữ liệu đỗ xe và kiểm soát quyền giữa các thành phần. Với thiết kế này, hệ thống có thể hoạt động an toàn, dễ dàng mở rộng và phù hợp với kiến trúc AWS Serverless.
