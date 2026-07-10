---
title: "Worklog Tuần 8"
date: 2026-05-13
weight: 8
chapter: false
pre: " <b> 1.8 </b> "
---

## Mục tiêu Tuần 8:
- Học và thực hành di chuyển máy chủ từ On-premise lên AWS bằng VM Import/Export.
- Tạo container cho ứng dụng bằng Docker và quản lý container với Docker Compose trên Amazon EC2.
- Cấu hình các container ứng dụng kết nối với Amazon RDS và lưu trữ ảnh container trong Amazon ECR và Docker Hub.

## Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học các khái niệm VM Import/Export<br> - Lab 14: Chuẩn bị VM và xuất từ môi trường On-premise | 08/06/2026 | 08/06/2026 | [VM Import/Export Requirements](https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html) |
| 3 | - Lab 14: Tải tệp VM lên Amazon S3<br> - Chạy lệnh CLI để nhập VM làm AWS AMI và khởi chạy EC2 instance | 09/06/2026 | 09/06/2026 | [Importing a VM as an Image](https://docs.aws.amazon.com/vm-import/latest/userguide/what-is-vmimport.html) |
| 4 | - Lab 14: Cấu hình S3 Bucket ACL<br> - Xuất EC2 instance trở lại S3 dưới dạng tệp VM và dọn dẹp tài nguyên | 10/06/2026 | 10/06/2026 | [Exporting an Instance/Image](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html) |
| 5 | - Lab 15: Triển khai và kiểm tra ứng dụng trên môi trường Local<br> - Chuẩn bị AWS: Cấu hình VPC, Security Group, IAM Roles cho ECR và đăng nhập vào Docker Hub | 11/06/2026 | 11/06/2026 | [Docker Documentation](https://docs.docker.com/)<br> [Amazon ECR IAM Policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/security_iam_id-based-policy-examples.html) |
| 6 | - Lab 15: Tạo DB Subnet Group và khởi chạy RDS Instance<br> - Khởi chạy và cấu hình EC2 Instance làm máy chủ Docker và cài đặt các phụ thuộc | 12/06/2026 | 12/06/2026 | [Amazon RDS DB Instance Creation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html)<br> [Docker on AWS EC2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) |
| 7 - Chủ nhật | - Lab 15: Tạo ảnh Docker, chạy container và cấu hình Docker Compose trên EC2 để kết nối với RDS<br> - Đẩy ảnh Docker lên Amazon ECR và Docker Hub<br> - Dọn dẹp tài nguyên để tránh chi phí | 13/06/2026 | 14/06/2026 | [Docker Compose Reference](https://docs.docker.com/compose/)<br> [ECR Push Image Commands](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html) |

## Thành tựu Tuần 8:
