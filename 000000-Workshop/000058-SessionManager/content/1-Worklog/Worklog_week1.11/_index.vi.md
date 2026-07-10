
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

