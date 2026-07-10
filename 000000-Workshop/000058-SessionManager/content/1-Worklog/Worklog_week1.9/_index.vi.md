---
title: "Worklog Tuần 9"
date: 2026-06-15
weight: 9
chapter: false
pre: " <b> 1.9 </b> "
---

## Mục tiêu Tuần 9:
- Hiểu và thực hành triển khai ứng dụng trên Amazon ECS (Elastic Container Service) sử dụng Fargate, ALB và Cloud Map.
- Học và cấu hình CI/CD pipeline tự động sử dụng GitLab CI/CD, GitHub Actions và AWS CodeBuild.
- Cấu hình giám sát container bằng Amazon CloudWatch Container Insights và ghi log sử dụng AWS FireLens.
- Sử dụng AWS Security Hub để đánh giá posture bảo mật tổng thể (Security Score) theo các tiêu chuẩn bảo mật AWS.

## Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học các khái niệm Amazon ECS, Fargate, Task Definitions và các hoạt động ECS Cluster | 15/06/2026 | 15/06/2026 | [Amazon ECS Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) |
| 3 | - **Lab 16 (Phần 1)**: Cấu hình mạng VPC, Subnets, Security Groups và đẩy Docker images lên ECR/Docker Hub | 16/06/2026 | 16/06/2026 | [AWS ECR User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) |
| 4 | - **Lab 16 (Phần 2)**: Tạo ECS Cluster, Task Definitions cho Frontend/Backend, cấu hình Target Groups, ALB và khởi chạy ECS Services (Blue/Green cho Backend & Rolling Update cho Frontend) | 17/06/2026 | 17/06/2026 | [AWS ECS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html) |
| 5 | - **Lab 17 (Phần 1)**: Tích hợp CI/CD tự động sử dụng GitLab Runner (cấu hình IAM roles, variables, chạy pipeline) và GitHub Actions | 18/06/2026 | 18/06/2026 | [GitLab CI/CD Docs](https://docs.gitlab.com/ci/)<br> [GitHub Actions Docs](https://docs.github.com/en/actions)<br> [AWS CodeBuild User Guide](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) |
| 6 | - **Lab 17 (Phần 2)**: Thiết lập AWS CodeBuild cho Frontend/Backend, cấu hình Container Insights (CloudWatch) và ghi log qua AWS FireLens lên S3 | 19/06/2026 | 19/06/2026 | [AWS Firelens Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) |
| 7 - Chủ nhật | - **Lab 18**: Kích hoạt AWS Security Hub, bật các tiêu chuẩn bảo mật, phân tích Security Score và dọn dẹp tài nguyên | 20/06/2026 | 21/06/2026 | [AWS Security Hub User Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) |

## Thành tựu Tuần 9:
- **Amazon ECS (Fargate)**: Triển khai thành công kiến trúc container hóa trên ECS với các dịch vụ Frontend và Backend độc lập sử dụng tính năng Serverless compute.
- **Load Balancing & Routing**: Cấu hình Application Load Balancers (ALB) để xử lý routing dựa trên path, Blue/Green Deployment (thông qua AWS CodeDeploy) cho Backend và Rolling Update cho Frontend.
- **Multi-Platform CI/CD**: Thiết kế các luồng tự động hóa sử dụng GitLab Runner tự quản trên EC2, GitHub Actions workflow secrets và các cấu hình dự án AWS CodeBuild.
- **Monitoring & Log Routing**: Kích hoạt các metrics CloudWatch Container Insights và triển khai AWS Firelens (Fluent Bit) logs router sidecar để lưu log stdout/stderr của container trên Amazon S3.
- **Security Auditing**: Kích hoạt AWS Security Hub và đạt điểm tuân thủ bảo mật dựa trên AWS Foundational Security Best Practices và CIS AWS Foundations Benchmark.
