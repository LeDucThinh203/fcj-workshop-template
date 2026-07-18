
---
title: "Nhật ký công việc Tuần 11"
date: 2026-06-29
weight: 11
chapter: false
pre: " <b> 1.11 </b> "
---

## Mục tiêu Tuần 11:
- Tìm hiểu các khái niệm về dịch vụ AWS Storage Gateway và mô hình lưu trữ lai (Hybrid Cloud Storage).
- Thực hành triển khai và cấu hình AWS File Storage Gateway để kết nối hạ tầng lưu trữ tại chỗ (On-premises) với dịch vụ lưu trữ đám mây Amazon S3.
- Thực hành kết nối (mount) File Share (NFS/SMB) từ Storage Gateway lên hệ điều hành Linux (giả lập máy chủ On-premises).

## Công việc cần thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học lý thuyết về AWS Storage Gateway, phân loại các dòng Gateway và mô hình Hybrid Cloud Storage | 29/06/2026 | 29/06/2026 | [AWS Storage Gateway Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/WhatIsStorageGateway.html) |
| 3 | - **Thực hành (Phần 1)**: Khởi tạo S3 bucket trên AWS để đóng vai trò làm backend storage cho Storage Gateway | 30/06/2026 | 30/06/2026 | [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/) |
| 4 | - **Thực hành (Phần 2)**: Khởi chạy một EC2 instance chạy Linux để giả lập môi trường máy chủ nội bộ (On-premises machine) | 01/07/2026 | 01/07/2026 | [Amazon EC2 User Guide](https://docs.aws.amazon.com/ec2/) |
| 5 | - **Thực hành (Phần 3)**: Tạo và cấu hình AWS File Storage Gateway thông qua giao diện quản trị AWS Console | 02/07/2026 | 02/07/2026 | [Creating a File Gateway](https://docs.aws.amazon.com/storagegateway/latest/userguide/CreatingAnAppliance.html) |
| 6 | - **Thực hành (Phần 4)**: Tạo File Share trên Storage Gateway và liên kết trực tiếp với S3 bucket đã chuẩn bị ở bước trước | 03/07/2026 | 03/07/2026 | [Creating a File Share](https://docs.aws.amazon.com/storagegateway/latest/userguide/CreatingAFileShare.html) |
| 7 - Chủ nhật | - **Thực hành (Phần 5)**: Thực hiện kết nối (mount) File Share NFS lên máy chủ EC2 giả lập, kiểm tra đồng bộ ghi dữ liệu chéo lên S3<br>- Tiến hành dọn dẹp sạch sẽ tài nguyên để tránh phát sinh chi phí | 04/07/2026 | 05/07/2026 | [Mounting a File Share](https://docs.aws.amazon.com/storagegateway/latest/userguide/mounting-file-share.html) |

## Thành tựu Tuần 11:
- **Cấu hình AWS Storage Gateway**: Hiểu rõ nguyên lý hoạt động của kiến trúc lưu trữ lai (Hybrid Cloud Storage) và cấu hình thành công AWS File Storage Gateway để kết nối bộ nhớ on-premises với AWS S3 thông qua các giao thức chia sẻ tệp tiêu chuẩn.
- **Tích hợp hạ tầng lai**: Thực hành thành công quy trình mount File Share NFS và xác minh khả năng đồng bộ hóa tệp dữ liệu tự động giữa môi trường tại chỗ và cloud.
- **Tối ưu hóa chi phí**: Chủ động dọn dẹp hoàn toàn các tài nguyên thực hành (Storage Gateway, File Share, S3 Bucket, EC2 Instance) để tránh phát sinh chi phí duy trì dịch vụ Storage Gateway.

### Hình ảnh minh chứng:

1. **Khởi tạo S3 Bucket (Create s3 bucket)**
   ![Create s3 bucket](../../../images/1-Worklog/Worklog_week1.11/Create%20s3%20bucket.png)
   *Mô tả chi tiết: Quá trình tạo Amazon S3 Bucket để làm nơi lưu trữ dữ liệu cho Storage Gateway. S3 cung cấp kho lưu trữ đối tượng an toàn, bền bỉ và có khả năng mở rộng, đóng vai trò là điểm đến (backend storage) cho các file được chia sẻ qua File Gateway.*

2. **Khởi chạy EC2 (Create EC2)**
   ![Create EC2](../../../images/1-Worklog/Worklog_week1.11/Create%20EC2.png)
   *Mô tả chi tiết: Triển khai một máy ảo (EC2 instance) đóng vai trò như một máy chủ on-premises mô phỏng. Máy ảo này sẽ được cấu hình để mount (kết nối) vào File Share mà Storage Gateway cung cấp, nhằm kiểm tra khả năng lưu trữ file lên S3 từ môi trường mạng nội bộ.*

3. **Tạo Storage Gateway (Create Storage GateWay)**
   ![Create Storage GateWay](../../../images/1-Worklog/Worklog_week1.11/Create%20Storage%20GateWay.png)
   *Mô tả chi tiết: Giao diện cấu hình và khởi tạo AWS File Storage Gateway. Storage Gateway đóng vai trò làm cầu nối (bridge) giữa ứng dụng on-premises và hệ sinh thái lưu trữ đám mây của AWS. Nó cung cấp giao thức SMB/NFS tiêu chuẩn để các ứng dụng cũ có thể dễ dàng lưu file lên S3 mà không cần thay đổi kiến trúc.*

4. **Tạo File Share (Create File Share)**
   ![Create File Share](../../../images/1-Worklog/Worklog_week1.11/Create%20File%20Share.png)
   *Mô tả chi tiết: Quá trình thiết lập một File Share trên Storage Gateway vừa tạo. File share này được liên kết trực tiếp với S3 bucket. Bất kỳ file nào được ghi vào file share này thông qua NFS/SMB sẽ được Gateway tự động đẩy lên S3 dưới dạng các object.*

5. **Kết nối File Share vào máy On-premises (Mount File shares on On-premises machine)**
   ![Mount File shares on On-premises machine](../../../images/1-Worklog/Worklog_week1.11/Mount%20File%20shares%20on%20On-premises%20machine.png)
   *Mô tả chi tiết: Thực hiện lệnh mount thư mục được chia sẻ từ Storage Gateway lên máy ảo EC2 (mô phỏng máy chủ on-premises). Hình ảnh cho thấy việc kết nối thành công, cho phép người dùng hoặc ứng dụng có thể đọc/ghi dữ liệu vào S3 thông qua một thư mục mạng cục bộ một cách hoàn toàn trong suốt.*

6. **Dọn dẹp tài nguyên (Clean)**
   ![Clean](../../../images/1-Worklog/Worklog_week1.11/Clean.png)
   *Mô tả chi tiết: Thao tác xóa bỏ các tài nguyên đã tạo (Storage Gateway, File Share, S3 Bucket, EC2 Instance) sau khi hoàn thành bài thực hành. Đây là nguyên tắc quan trọng nhằm tối ưu hóa chi phí (Cost Optimization) và đảm bảo không có tài nguyên dư thừa bị bỏ quên.*
