
---
title: "Nhật ký công việc Tuần 11"
date: 2026-06-29
weight: 11
chapter: false
pre: " <b> 1.11 </b> "
---

## Mục tiêu Tuần 11:
- Thực hành triển khai CI/CD pipeline bằng AWS CodePipeline, CodeCommit, CodeBuild và CodeDeploy.
- Hiểu và cấu hình AWS Storage Gateway để kết nối với môi trường on-premises.
- Bảo vệ ứng dụng hiệu quả bằng AWS Web Application Firewall (WAF).
- Quản lý tài nguyên AWS bằng Tags và Resource Groups.

## Công việc cần thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - **Thực hành**: Triển khai ứng dụng lên EC2 với AWS CodePipeline (Phần 1)<br>+ Chuẩn bị (S3, Git, IAM roles)<br>+ Khởi chạy EC2 và cài đặt CodeDeploy Agent | 29/06/2026 | 29/06/2026 | <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html" target="_blank">AWS CodeDeploy Guide</a> |
| 3 | - **Thực hành**: Triển khai ứng dụng lên EC2 với AWS CodePipeline (Phần 2)<br>+ Thiết lập AWS CodeCommit, CodeBuild, CodeDeploy<br>+ Cấu hình CodePipeline cho tự động hóa CI/CD | 30/06/2026 | 30/06/2026 | <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html" target="_blank">AWS CodePipeline Guide</a> |
| 4 | - **Thực hành**: AWS Storage Gateway<br>+ Tạo S3 Bucket cho Storage Gateway<br>+ Khởi tạo Storage Gateway và File Shares<br>+ Gắn File Shares lên máy On-premises | 01/07/2026 | 01/07/2026 | <a href="https://docs.aws.amazon.com/storagegateway/" target="_blank">AWS Storage Gateway</a> |
| 5 | - **Thực hành**: AWS Web Application Firewall (Phần 1)<br>+ Triển khai Web App mẫu<br>+ Sử dụng AWS WAF, cấu hình ACLs và Managed rules | 02/07/2026 | 02/07/2026 | <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html" target="_blank">AWS WAF Developer Guide</a> |
| 6 | - **Thực hành**: AWS Web Application Firewall (Phần 2)<br>+ Tạo Custom rules để chặn IP/Quốc gia<br>+ Bật Logging và Kiểm tra | 03/07/2026 | 03/07/2026 | <a href="https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups.html" target="_blank">AWS WAF Managed Rules</a> |
| 7 - Chủ nhật | - **Thực hành**: Quản lý tài nguyên bằng Tags và Resource Groups<br>+ Sử dụng Tags trên Console và CLI<br>+ Tạo và quản lý Resource Groups | 04/07/2026 | 05/07/2026 | <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html" target="_blank">Tagging AWS resources</a><br><a href="https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html" target="_blank">AWS Resource Groups</a> |

## Thành tựu Tuần 11:
- **Thành thạo CI/CD Pipeline trên AWS**: Đã tích hợp các dịch vụ như CodeCommit, CodeBuild, CodeDeploy và CodePipeline để tự động hóa hoàn toàn việc triển khai ứng dụng.
- **Cấu hình AWS Storage Gateway**: Đã hiểu và cấu hình thành công AWS File Storage Gateway để kết nối bộ nhớ on-premises với AWS S3.
- **Bảo vệ ứng dụng web với WAF**: Đã triển khai AWS WAF để bảo vệ các ứng dụng web khỏi các cuộc tấn công bằng Web ACLs và các quy tắc tuỳ chỉnh.
- **Quản lý tài nguyên với Tags & Resource Groups**: Đã học cách tổ chức và quản lý các tài nguyên AWS một cách hiệu quả bằng Tags và Resource Groups.
- **Hoàn thành tất cả bài lab**: Đã hoàn thành thành công tất cả 4 bài lab thực hành như hướng dẫn.

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
