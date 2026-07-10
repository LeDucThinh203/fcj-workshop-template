---
title: "Worklog Tuần 5"
date: 2026-05-13
weight: 5
chapter: false
pre: " <b> 1.5 </b> "
---

## Mục tiêu Tuần 5:
- Nắm vững vòng đời của AWS S3: Lazy Loading, Transient Storage, Set Policies, Crossfeed Period.
- Hiểu vai trò của Application Load Balancer (ELB) trong việc phân phối lưu lượng truy cập và tính sẵn sàng cao.
- Phân biệt Auto Scaling Group của các EC2 instances.
- Hiểu tầm quan trọng của các kỹ thuật quản lý chi phí và giám sát chi tiêu tài nguyên.

## Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học EC2 Auto Scaling (Lazy Storage, Set Policies, Crossfeed Period)<br>- Hiểu Static Website Hosting trên S3 và Route S3 làm bản sao lưu cho CloudFront<br>- Nghiên cứu về chủ đề quản lý chi phí của S3 | 18/05/2026 | 18/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | - **Thực hành:**<br>  + Tạo một S3 bucket, cấu hình static website hosting<br>  + Cấu hình Static Website Hosting cho EC2 Management UI (S3 UI)<br>  + Tạo một Auto Scaling Group | 19/05/2026 | 19/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - **Thực hành:**<br>  + Cấu hình Application Load Balancer<br>  + Cấu hình Auto Scaling Group<br>  + Cấu hình CloudFront với S3 | 20/05/2026 | 20/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | - **Thực hành:**<br>  + Kiểm tra Auto Scaling Group<br>  + Kiểm tra Application Load Balancer<br>  + Kiểm tra tích hợp CloudFront và S3<br>  + Kiểm tra ứng dụng quản lý EC2 | 21/05/2026 | 21/05/2026 | https://cloudjourney.awsstudygroup.com/ |

### Thành tựu Tuần 5:
#### Lý thuyết:
- Nắm vững vòng đời của AWS S3: Lazy Loading, Transient Storage, Set Policies, Crossfeed Period.
- Hiểu vai trò của Application Load Balancer (ELB) trong việc phân phối lưu lượng truy cập và tính sẵn sàng cao.
- Phân biệt Auto Scaling Group của các EC2 instances.
- Hiểu tầm quan trọng của các kỹ thuật quản lý chi phí và giám sát chi tiêu tài nguyên.

#### Thực hành:
Tôi có thể sử dụng các dịch vụ AWS hiệu quả:
- Thành công xây dựng ứng dụng quản lý EC2 bằng Amazon EC2 Auto-Scaling với Elastic Load Balancing để đảm bảo tính sẵn sàng cao và tính linh hoạt.
- Tất cả các dịch vụ đã sử dụng:
  - Amazon VPC: Tạo một môi trường ảo biệt lập để triển khai các tài nguyên AWS.
  - Application Load Balancer: Phân phối lưu lượng truy cập giữa các EC2 instances, cải thiện khả năng chịu lỗi của ứng dụng.
  - Auto Scaling Group: Tự động co giãn các EC2 instances theo nhu cầu thực tế, tối ưu hóa chi phí.
  - Amazon S3: Lưu trữ các tệp website tĩnh, hỗ trợ static website hosting.
  - Amazon CloudFront: Cung cấp nội dung website tĩnh một cách nhanh chóng qua mạng lưới các điểm hiện diện toàn cầu của AWS.
  - IAM: Quản lý quyền truy cập một cách an toàn cho các dịch vụ AWS.

Tạo VPC (CloudStack lab):
- Trong phòng thí nghiệm CloudFormation này, cấu hình các thông tin sau:
  - 1 VPC với CIDR: 10.10.0.0/16
  - 2 Public Subnets với CIDR: 10.10.1.0/24, 10.10.2.0/24
  - 2 Private Subnets với CIDR: 10.10.3.0/24, 10.10.4.0/24
  - 1 Internet Gateway
  - 2 NAT Gateway
  - 2 Public Route Table
  - 2 Private Route Table
  - Security Groups cho Application Load Balancer, Public EC2, Private EC2
  - IAM Role cho EC2
  - Launch Template
  - Auto Scaling Group
  - Application Load Balancer
  - Target Group
  - S3 Bucket
  - CloudFront Distribution
