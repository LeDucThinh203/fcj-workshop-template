---
title: "Nhật ký công việc"
date: 2026-04-27
weight: 1
pre : " <b> 1. </b> "
---

## Tuần 1:
- Kết nối và làm quen với các thành viên của First Cloud Journey.
- Hiểu các dịch vụ AWS cơ bản, cách sử dụng console và CLI.

### Công việc cần thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Làm quen với các thành viên FCJ<br>- Đọc và ghi nhớ các quy định, quy tắc tại đơn vị thực tập | 20/04/2026 | 20/04/2026 |  |
| 3 | - Tìm hiểu về AWS và các loại dịch vụ của nó<br>  + Compute<br>  + Storage<br>  + Networking<br>  + Database<br>  + ... | [21/04/2026](./Worklog_week1.1/) | [21/04/2026](./Worklog_week1.1/) | https://cloudjourney.awsstudygroup.com/ |
| 4 | - Tạo tài khoản AWS Free Tier<br>- Tìm hiểu về AWS Console và AWS CLI<br>- **Thực hành:**<br>  + Tạo tài khoản AWS<br>  + Cài đặt và cấu hình AWS CLI<br>  + Học cách sử dụng AWS CLI | 22/04/2026 | 22/04/2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | - Tìm hiểu cơ bản về EC2:<br>  + Loại instance<br>  + AMI<br>  + EBS<br>  + ...<br>- Khám phá các phương pháp kết nối từ xa tới EC2 qua SSH<br>- Tìm hiểu về Elastic IP | 23/04/2026 | 23/04/2026 | https://cloudjourney.awsstudygroup.com/ |
| 6 | - **Thực hành:**<br>  + Tạo EC2 instance<br>  + Kết nối qua SSH<br>  + Gắn EBS volume | 24/04/2026 | 24/04/2026 | https://cloudjourney.awsstudygroup.com/ |
| 7 - Chủ nhật | - **Thực hành nâng cao:**<br>  + Tạo lại EC2 instance và cấu hình Security Group<br>  + Kết nối qua SSH và cài đặt Web Server (Apache/Nginx)<br>  + Triển khai website đơn giản và truy cập qua Public IP<br>  + Tìm hiểu và thử nghiệm với AWS S3 (tạo bucket, upload file) | 25/04/2026 | 26/04/2026 | https://cloudjourney.awsstudygroup.com/ |

---

## Tuần 2:
### Mục tiêu Tuần 2:
- Hiểu mạng cơ bản trong AWS (VPC)
- Thành thạo cách cấu hình các thành phần mạng và bảo mật trong VPC
- Thực hành xây dựng một VPC hoàn chỉnh

### Công việc cần thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học cơ bản VPC:<br>  + Tổng quan VPC<br>  + CIDR Block<br>  + Phân biệt Subnet Công cộng / Riêng | 27/04/2026 | 27/04/2026 | [VPC Basics](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) |
| 3 | - Học về Subnet & Route Tables:<br>  + Cách chia Subnet<br>  + Cấu hình Route Tables | [28/04/2026](./Worklog_week1.2/) | [28/04/2026](./Worklog_week1.2/) | [Subnets & Route Tables](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html) |
| 4 | - Học về Internet Gateway & NAT Gateway:<br>  + Internet Gateway cho Subnet Công cộng<br>  + NAT Gateway cho Subnet Riêng | 29/04/2026 | 29/04/2026 | [NAT Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) |
| 5 | - Học về bảo mật trong VPC:<br>  + Security Groups<br>  + Network ACLs<br>  + Quy tắc Inbound / Outbound | 30/04/2026 | 30/04/2026 | [VPC Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) |
| 6 | - **Thực hành:**<br>  + Tạo VPC<br>  + Tạo Subnet Công cộng & Riêng<br>  + Cấu hình Route Tables | 01/05/2026 | 01/05/2026 | [FCJ Lab - Create VPC](https://cloudjourney.awsstudygroup.com/2-prerequisites/2.1-createvpc/) |
| 7 - Chủ nhật | - **Thực hành nâng cao:**<br>  + Gắn Internet Gateway<br>  + Tạo NAT Gateway<br>  + Triển khai EC2 trong Subnet Riêng/Công cộng<br>  + Xác minh kết nối internet | 02/05/2026 | 03/05/2026 | [FCJ Lab - Public/Private](https://cloudjourney.awsstudygroup.com/2-prerequisites/2.2-publicprivateinstance/) |

### Thành tựu Tuần 2:
#### Lý thuyết:
- Có thể hiểu kiến trúc của Amazon VPC và cách quản lý dải địa chỉ IP qua CIDR
- Biết cách tạo và cấu hình route tables

---

## Tuần 3:
### Mục tiêu Tuần 3:
- Tìm hiểu về dịch vụ Amazon EC2 trên AWS.
- Thực hành khởi tạo, cấu hình và quản lý EC2 Instances.
- Triển khai ứng dụng Node.js trên môi trường Linux và Windows.

### Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Tổng quan về Amazon EC2<br>- Tìm hiểu về Instance Types, AMI, Key Pair và Snapshot<br>- Hiểu cơ chế hoạt động của EC2 Instances | 05/04/2026 | 05/04/2026 | [Amazon EC2 Basics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 3 | - Chuẩn bị môi trường EC2<br>+ Tạo VPC cho Linux<br>+ Tạo VPC cho Windows<br>+ Tạo Security Group cho các Instance Linux và Windows | [05/05/2026](./Worklog_week1.3/) | [05/05/2026](./Worklog_week1.3/) | [EC2 Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)<br>FCJ Lab |
| 4 | - Khởi tạo EC2 Instance Windows<br>+ Tạo Windows Instance<br>+ Kết nối Remote Desktop vào Windows Instance | 05/06/2026 | 05/06/2026 | [EC2 Windows Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 5 | - Khởi tạo EC2 Instance Linux<br>+ Tạo Linux Instance<br>+ Kết nối SSH vào Linux Instance<br>- Tìm hiểu thay đổi cấu hình EC2 và quản lý EBS Snapshot | 05/07/2026 | 05/07/2026 | [EC2 Linux Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 6 | - Thực hành nâng cao EC2<br>+ Tạo Custom AMI<br>+ Tạo Instance từ Custom AMI<br>+ Thực hành truy cập EC2 khi mất Key Pair | 05/08/2026 | 05/08/2026 | [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)<br>FCJ Lab |
| 7 - Chủ nhật | - Triển khai ứng dụng Node.js lên EC2<br>+ Cài đặt Server LAMP/XAMPP<br>+ Cài đặt Node.js trên Linux và Windows<br>+ Triển khai ứng dụng Node.js<br>- Tìm hiểu giới hạn tài nguyên sử dụng IAM | 05/09/2026 | 05/10/2026 | [IAM for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html)<br>FCJ Lab |

---

## Tuần 4:
### Mục tiêu Tuần 4:
- Khởi tạo và cấu hình một Amazon RDS database instance.
- Kết nối ứng dụng chạy trên EC2 đến RDS database.
- Hiểu các cơ chế Backup, Restore và các tính năng nâng cao (Multi-AZ, Read Replicas).

### Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày kết thúc | Nguồn tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Tổng quan về Amazon RDS<br>- So sánh RDS với các dịch vụ lưu trữ khác (EC2 DB, DynamoDB, Redshift) | 11/05/2026 | 11/05/2026 | [Amazon RDS Documentation](https://docs.aws.amazon.com/rds/) |
| 3 | - Cấu hình mạng cho RDS:<br>  + Tạo VPC<br>  + Tạo Security Groups cho EC2 và RDS<br>  + Tạo DB Subnet Group | [12/05/2026](./Worklog_week1.4/) | [12/05/2026](./Worklog_week1.4/) | [VPC for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) |
| 4 | - Thực hành khởi tạo một Amazon RDS instance<br>- Cấu hình các tham số và các tùy chọn bảo mật cho Database | 13/05/2026 | 13/05/2026 | [Creating an RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) |
| 5 | - Triển khai ứng dụng trên EC2 và kết nối đến RDS<br>- Xác minh truy cập và quản lý dữ liệu qua Endpoint | 14/05/2026 | 14/05/2026 | [Connecting to RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html) |
| 6 | - Học và thực hành Backup & Restore<br>- Thực hành Snapshot thủ công và tự động | 15/05/2026 | 15/05/2026 | [RDS Backup and Restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html) |
| 7 - Chủ nhật | - Học về Multi-AZ và Read Replicas<br>- Dọn dẹp tài nguyên để tối ưu chi phí | 16/05/2026 | 17/05/2026 | [High Availability (Multi-AZ)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) |

### Kết quả Tuần 4:
#### Lý thuyết:
- Nắm vững kiến thức về Amazon RDS: Lợi ích, các engine DB được hỗ trợ, các tính năng quản lý.
- Hiểu cách hoạt động của Multi-AZ và Read Replicas.
- Học cách phân biệt khi nào sử dụng RDS, DynamoDB, Redshift hoặc S3.
- Hiểu các cơ chế bảo mật (Security Groups, Encryption) và sao lưu (Snapshots) trên RDS.
#### Thực hành:
- Thiết lập thành công môi trường mạng an toàn cho Database (DB Subnet Group, Security Groups).
- Khởi tạo thành công một Amazon RDS instance (MySQL/MariaDB).
- Kết nối thành công ứng dụng Web trên EC2 với RDS database qua Endpoint.
- Thực hiện thành công sao lưu và khôi phục dữ liệu bằng Snapshots.
- Quản lý tài nguyên hiệu quả và dọn dẹp để tránh chi phí không cần thiết.

---

## Tuần 5:
### Mục tiêu Tuần 5:
- Nắm vững vòng đời của AWS S3: Lazy Loading, Transient Storage, Set Policies, Crossfeed Period.
- Hiểu vai trò của Application Load Balancer (ELB) trong việc phân phối lưu lượng truy cập và tính sẵn sàng cao.
- Phân biệt Auto Scaling Group của các EC2 instances.
- Hiểu tầm quan trọng của các kỹ thuật quản lý chi phí và giám sát chi tiêu tài nguyên.

### Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học EC2 Auto Scaling (Lazy Storage, Set Policies, Crossfeed Period)<br>- Hiểu Static Website Hosting trên S3 và Route S3 làm bản sao lưu cho CloudFront<br>- Nghiên cứu về chủ đề quản lý chi phí của S3 | 18/05/2026 | 18/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | - **Thực hành:**<br>  + Tạo một S3 bucket, cấu hình static website hosting<br>  + Cấu hình Static Website Hosting cho EC2 Management UI (S3 UI)<br>  + Tạo một Auto Scaling Group | 19/05/2026 | 19/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - **Thực hành:**<br>  + Cấu hình Application Load Balancer<br>  + Cấu hình Auto Scaling Group<br>  + Cấu hình CloudFront với S3 | 20/05/2026 | 20/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | - **Thực hành:**<br>  + Kiểm tra Auto Scaling Group<br>  + Kiểm tra Application Load Balancer<br>  + Kiểm tra tích hợp CloudFront và S3<br>  + Kiểm tra ứng dụng quản lý EC2 | [21/05/2026](./Worklog_week1.5/) | [21/05/2026](./Worklog_week1.5/) | https://cloudjourney.awsstudygroup.com/ |

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

---

## Tuần 6:
### Mục tiêu Tuần 6:
- Hiểu AWS Cloud Trail và các báo cáo được quản lý tại đây trong AWS Support.
- Triển khai tích hợp Hybrid DNS trên các máy chủ tại chỗ với AWS bằng Route 53 Resolver và Microsoft AD.

### Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học Amazon CloudWatch & chuẩn bị môi trường<br> - CloudWatch Metrics:<br>  + Xem Metrics<br>  + Thực hiện các hoạt động tìm kiếm<br>  + Thực hiện các phép toán toán học<br>  + Tạo dynamic labels | 25/05/2026 | 25/05/2026 | [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)<br> [Using Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) |
| 3 | - CloudWatch Logs:<br>  + Xem CloudWatch Logs<br>  + CloudWatch Logs Insights<br>  + CloudWatch Metric Filter<br>  + Tạo CloudWatch Alarms<br>  + Tạo CloudWatch Dashboards<br>  + Dọn dẹp tài nguyên | 26/05/2026 | 26/05/2026 | [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)<br> [Creating CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html)<br> [CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) |
| 4 | - Học về các AWS Support Plans: Basic, Developer, Business, Enterprise On-Ramp, Enterprise<br> - Truy cập AWS Support Console<br> - Học về các loại Support Request (Account & billing, Technical)<br> - Thay đổi support plan | 27/05/2026 | 27/05/2026 | [AWS Support Plans](https://aws.amazon.com/vi/premiumsupport/plans/)<br> [Getting started with AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html) |
| 5 | - Tạo một Support Request (Support Case)<br> - Chọn mức Severity<br> - Quản lý và theo dõi trạng thái yêu cầu support | 28/05/2026 | 28/05/2026 | [Creating a support case](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) |
| 6 | - Đọc tổng quan bài lab hybrid DNS<br> - Tạo Key Pair<br> - Khởi tạo CloudFormation Template<br> - Cấu hình Security Group<br> - Kết nối với RDGW (Remote Desktop Gateway)<br> - Triển khai Microsoft Active Directory | [29/05/2026](./Worklog_week1.6/) | [29/05/2026](./Worklog_week1.6/) | [What is AWS Directory Service?](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html)<br> [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) |
| 7 - Chủ nhật | - Thiết lập DNS với Route 53:<br>  + Tạo Route 53 Outbound Endpoint<br>  + Tạo Route 53 Resolver Rules<br>  + Tạo Route 53 Inbound Endpoints<br>  + Kiểm tra kết quả<br>  + Dọn dẹp tài nguyên | 30/05/2026 | 31/05/2026 | [Forwarding outbound DNS queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html)<br> [Forwarding inbound DNS queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html) |

---

## Tuần 7:
### Mục tiêu Tuần 7:
- Kết nối và làm quen với các thành viên của First Cloud Journey.
- Hiểu các dịch vụ AWS cơ bản, cách sử dụng console & CLI.

### Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học AWS CLI & Cài đặt<br> - Xem tài nguyên qua CLI<br> - AWS CLI với Amazon S3 và Amazon SNS | 01/06/2026 | 01/06/2026 | [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)<br> [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/) |
| 3 | - AWS CLI với IAM và VPC (VPC, Internet Gateway)<br> - Thực hành tạo EC2 qua AWS CLI | 02/06/2026 | 02/06/2026 | [AWS CLI for EC2 & VPC](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2.html)<br> [AWS CLI for IAM](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-iam.html) |
| 4 | - Học AWS Organizations<br> - Tạo các tài khoản thành viên, cấu hình Organizational Unit (OU) và mời các Tài khoản AWS | 03/06/2026 | 03/06/2026 | [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)<br> [Creating account in Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) |
| 5 | - Cấu hình truy cập Tài khoản Thành viên qua CLI<br> - Cấu hình kiểm soát truy cập theo thời gian & Customer Managed Policies<br> - Hiểu IAM Identity Center Identity Store APIs | 04/06/2026 | 04/06/2026 | [AWS IAM Identity Center Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)<br> [Identity Store APIs](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/Welcome.html) |
| 6 | - Học dịch vụ AWS Backup<br> - Chuẩn bị môi trường: Tạo S3 Bucket & Triển khai cơ sở hạ tầng sao lưu | 05/06/2026 | 05/06/2026 | [What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)<br> [Backup S3 with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html) |
| 7 - Chủ nhật | - Thiết lập Backup plan & cấu hình thông báo<br> - Thực hiện các hoạt động Khôi phục kiểm tra<br> - Dọn dẹp tài nguyên để tránh chi phí | [06/06/2026](./Worklog_week1.7/) | [07/06/2026](./Worklog_week1.7/) | [Creating backup plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)<br> [Restoring a backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) |

### Thành tựu Tuần 7:

---

## Tuần 8:
### Mục tiêu Tuần 8:
- Học và thực hành di chuyển máy chủ từ On-premise lên AWS bằng VM Import/Export.
- Tạo container cho ứng dụng bằng Docker và quản lý container với Docker Compose trên Amazon EC2.
- Cấu hình các container ứng dụng kết nối với Amazon RDS và lưu trữ ảnh container trong Amazon ECR và Docker Hub.

### Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học các khái niệm VM Import/Export<br> - Lab 14: Chuẩn bị VM và xuất từ môi trường On-premise | 08/06/2026 | 08/06/2026 | [VM Import/Export Requirements](https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html) |
| 3 | - Lab 14: Tải tệp VM lên Amazon S3<br> - Chạy lệnh CLI để nhập VM làm AWS AMI và khởi chạy EC2 instance | 09/06/2026 | 09/06/2026 | [Importing a VM as an Image](https://docs.aws.amazon.com/vm-import/latest/userguide/what-is-vmimport.html) |
| 4 | - Lab 14: Cấu hình S3 Bucket ACL<br> - Xuất EC2 instance trở lại S3 dưới dạng tệp VM và dọn dẹp tài nguyên | 10/06/2026 | 10/06/2026 | [Exporting an Instance/Image](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html) |
| 5 | - Lab 15: Triển khai và kiểm tra ứng dụng trên môi trường Local<br> - Chuẩn bị AWS: Cấu hình VPC, Security Group, IAM Roles cho ECR và đăng nhập vào Docker Hub | 11/06/2026 | 11/06/2026 | [Docker Documentation](https://docs.docker.com/)<br> [Amazon ECR IAM Policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/security_iam_id-based-policy-examples.html) |
| 6 | - Lab 15: Tạo DB Subnet Group và khởi chạy RDS Instance<br> - Khởi chạy và cấu hình EC2 Instance làm máy chủ Docker và cài đặt các phụ thuộc | 12/06/2026 | 12/06/2026 | [Amazon RDS DB Instance Creation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html)<br> [Docker on AWS EC2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) |
| 7 - Chủ nhật | - Lab 15: Tạo ảnh Docker, chạy container và cấu hình Docker Compose trên EC2 để kết nối với RDS<br> - Đẩy ảnh Docker lên Amazon ECR và Docker Hub<br> - Dọn dẹp tài nguyên để tránh chi phí | 13/06/2026 | 14/06/2026 | [Docker Compose Reference](https://docs.docker.com/compose/)<br> [ECR Push Image Commands](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html) |

### Thành tựu Tuần 8:

---

## Tuần 9:
### Mục tiêu Tuần 9:
- Hiểu và thực hành triển khai ứng dụng trên Amazon ECS (Elastic Container Service) sử dụng Fargate, ALB và Cloud Map.
- Học và cấu hình CI/CD pipeline tự động sử dụng GitLab CI/CD, GitHub Actions và AWS CodeBuild.
- Cấu hình giám sát container bằng Amazon CloudWatch Container Insights và ghi log sử dụng AWS FireLens.
- Sử dụng AWS Security Hub để đánh giá posture bảo mật tổng thể (Security Score) theo các tiêu chuẩn bảo mật AWS.

### Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học các khái niệm Amazon ECS, Fargate, Task Definitions và các hoạt động ECS Cluster | 15/06/2026 | 15/06/2026 | [Amazon ECS Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) |
| 3 | - **Lab 16 (Phần 1)**: Cấu hình mạng VPC, Subnets, Security Groups và đẩy Docker images lên ECR/Docker Hub | 16/06/2026 | 16/06/2026 | [AWS ECR User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) |
| 4 | - **Lab 16 (Phần 2)**: Tạo ECS Cluster, Task Definitions cho Frontend/Backend, cấu hình Target Groups, ALB và khởi chạy ECS Services (Blue/Green cho Backend & Rolling Update cho Frontend) | 17/06/2026 | 17/06/2026 | [AWS ECS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html) |
| 5 | - **Lab 17 (Phần 1)**: Tích hợp CI/CD tự động sử dụng GitLab Runner (cấu hình IAM roles, variables, chạy pipeline) và GitHub Actions | 18/06/2026 | 18/06/2026 | [GitLab CI/CD Docs](https://docs.gitlab.com/ci/)<br> [GitHub Actions Docs](https://docs.github.com/en/actions)<br> [AWS CodeBuild User Guide](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) |
| 6 | - **Lab 17 (Phần 2)**: Thiết lập AWS CodeBuild cho Frontend/Backend, cấu hình Container Insights (CloudWatch) và ghi log qua AWS FireLens lên S3 | 19/06/2026 | 19/06/2026 | [AWS Firelens Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) |
| 7 - Chủ nhật | - **Lab 18**: Kích hoạt AWS Security Hub, bật các tiêu chuẩn bảo mật, phân tích Security Score và dọn dẹp tài nguyên | 20/06/2026 | 21/06/2026 | [AWS Security Hub User Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) |

### Thành tựu Tuần 9:
- **Amazon ECS (Fargate)**: Triển khai thành công kiến trúc container hóa trên ECS với các dịch vụ Frontend và Backend độc lập sử dụng tính năng Serverless compute.
- **Load Balancing & Routing**: Cấu hình Application Load Balancers (ALB) để xử lý routing dựa trên path, Blue/Green Deployment (thông qua AWS CodeDeploy) cho Backend và Rolling Update cho Frontend.
- **Multi-Platform CI/CD**: Thiết kế các luồng tự động hóa sử dụng GitLab Runner tự quản trên EC2, GitHub Actions workflow secrets và các cấu hình dự án AWS CodeBuild.
- **Monitoring & Log Routing**: Kích hoạt các metrics CloudWatch Container Insights và triển khai AWS Firelens (Fluent Bit) logs router sidecar để lưu log stdout/stderr của container trên Amazon S3.
- **Security Auditing**: Kích hoạt AWS Security Hub và đạt điểm tuân thủ bảo mật dựa trên AWS Foundational Security Best Practices và CIS AWS Foundations Benchmark.

---

## Tuần 10:
### Mục tiêu Tuần 10:
- Hiểu và cấu hình VPC Peering để kết nối hai mạng VPC riêng biệt, cấu hình routing và thiết lập Network ACLs (NACLs) để kiểm soát bảo mật stateless ở mức subnet.
- Học và triển khai AWS Transit Gateway (TGW) để kết nối nhiều VPC theo mô hình Hub-and-Spoke, đơn giản hóa kiến trúc mạng quy mô lớn.
- Thực hiện tự động hóa hoạt động serverless sử dụng AWS Lambda và Amazon EventBridge để tự động start/stop EC2 instances dựa trên lịch trình và chuyển hướng log/alarm thực thi đến Slack.

### Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học các khái niệm VPC Peering và Network Access Control Lists (NACLs)<br>- **Lab 19 (Part 1)**: Thiết lập môi trường mạng cơ sở sử dụng Cloudformation, tạo Security Groups và EC2s | 22/06/2026 | 22/06/2026 | VPC Peering Guide<br>VPC ACLs |
| 3 | - **Lab 19 (Part 2)**: Cấu hình Custom VPC Peering, tạo kết nối VPC Peering, cập nhật route tables và xác minh Cross-Peer DNS resolution | 23/06/2026 | 23/06/2026 | Network Peering DNS Support |
| 4 | - Học các khái niệm AWS Transit Gateway (TGW)<br>- **Lab 20 (Part 1)**: Thiết lập 3 VPC để minh họa, tạo Transit Gateway và cấu hình VPC attachments | 24/06/2026 | 24/06/2026 | AWS Transit Gateway |
| 5 | - **Lab 20 (Part 2)**: Thiết lập Transit Gateway Route Tables, thêm Routes vào TGW Route Tables và xác minh kết nối mạng cross-VPC | 25/06/2026 | 25/06/2026 | TGW Route Tables |
| 6 | - Học dịch vụ tính toán serverless AWS Lambda và EventBridge scheduling<br>- **Lab 22 (Part 1)**: Thiết lập IAM workshop, gán thẻ cho EC2 instances và cấu hình IAM Role cho Lambda | 26/06/2026 | 26/06/2026 | AWS Lambda Developer Guide<br>Slack Webhooks |
| 7 - Chủ nhật | - **Lab 22 (Part 2)**: Triển khai mã Python Lambda (boto3) để start/stop EC2s và gửi cảnh báo đến Slack, lên lịch thông qua EventBridge và dọn dẹp tài nguyên | 27/06/2026 | 28/06/2026 | Boto3 EC2 Client<br>EventBridge Scheduler |

### Thành tựu Tuần 10:
- **VPC Peering & Bảo mật**: Đã thiết lập thành công kết nối mạng riêng giữa hai VPC cô lập; áp dụng Network ACLs để kiểm soát các gói tin vào/ra và hiểu rõ hơn về hoạt động không giữ trạng thái (stateless) của NACL so với Security Groups giữ trạng thái (stateful).
- **Triển khai Transit Gateway**: Đã xây dựng mạng Hub-and-Spoke trung tâm kết nối 3 VPC bằng AWS Transit Gateway, loại bỏ nhu cầu cấu hình peering dạng full-mesh phức tạp.
- **Tự động hóa Serverless**: Đã xây dựng giải pháp quản lý serverless bằng AWS Lambda (Python boto3) đọc các tag tài nguyên của instance, dừng các máy chủ phát triển vào ban đêm và khởi động trước giờ làm việc.
- **Tích hợp ChatOps**: Đã tích hợp cảnh báo AWS Lambda với thông báo trên kênh Slack bằng Incoming Webhooks để báo cáo trạng thái hoạt động theo thời gian thực.
- **Hoạt động theo lịch trình**: Đã cấu hình Amazon EventBridge Scheduler (các trình kích hoạt cron) để tự động gọi các hàm Lambda vào các thời điểm cụ thể.

---

## Tuần 11:
### Mục tiêu Tuần 11:
- Thực hành triển khai CI/CD pipeline bằng AWS CodePipeline, CodeCommit, CodeBuild và CodeDeploy.
- Hiểu và cấu hình AWS Storage Gateway để kết nối với môi trường on-premises.
- Bảo vệ ứng dụng hiệu quả bằng AWS Web Application Firewall (WAF).
- Quản lý tài nguyên AWS bằng Tags và Resource Groups.

### Công việc cần thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - **Thực hành**: Triển khai ứng dụng lên EC2 với AWS CodePipeline (Phần 1)<br>+ Chuẩn bị (S3, Git, IAM roles)<br>+ Khởi chạy EC2 và cài đặt CodeDeploy Agent | 29/06/2026 | 29/06/2026 | <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html" target="_blank">AWS CodeDeploy Guide</a> |
| 3 | - **Thực hành**: Triển khai ứng dụng lên EC2 với AWS CodePipeline (Phần 2)<br>+ Thiết lập AWS CodeCommit, CodeBuild, CodeDeploy<br>+ Cấu hình CodePipeline cho tự động hóa CI/CD | 30/06/2026 | 30/06/2026 | <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html" target="_blank">AWS CodePipeline Guide</a> |
| 4 | - **Thực hành**: AWS Storage Gateway<br>+ Tạo S3 Bucket cho Storage Gateway<br>+ Khởi tạo Storage Gateway và File Shares<br>+ Gắn File Shares lên máy On-premises | 01/07/2026 | 01/07/2026 | <a href="https://docs.aws.amazon.com/storagegateway/" target="_blank">AWS Storage Gateway</a> |
| 5 | - **Thực hành**: AWS Web Application Firewall (Phần 1)<br>+ Triển khai Web App mẫu<br>+ Sử dụng AWS WAF, cấu hình ACLs và Managed rules | 02/07/2026 | 02/07/2026 | <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html" target="_blank">AWS WAF Developer Guide</a> |
| 6 | - **Thực hành**: AWS Web Application Firewall (Phần 2)<br>+ Tạo Custom rules để chặn IP/Quốc gia<br>+ Bật Logging và Kiểm tra | 03/07/2026 | 03/07/2026 | <a href="https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups.html" target="_blank">AWS WAF Managed Rules</a> |
| 7 - Chủ nhật | - **Thực hành**: Quản lý tài nguyên bằng Tags và Resource Groups<br>+ Sử dụng Tags trên Console và CLI<br>+ Tạo và quản lý Resource Groups | [04/07/2026](./Worklog_week1.11/) | [05/07/2026](./Worklog_week1.11/) | <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html" target="_blank">Tagging AWS resources</a><br><a href="https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html" target="_blank">AWS Resource Groups</a> |

### Thành tựu Tuần 11:
- **Thành thạo CI/CD Pipeline trên AWS**: Đã tích hợp các dịch vụ như CodeCommit, CodeBuild, CodeDeploy và CodePipeline để tự động hóa hoàn toàn việc triển khai ứng dụng.
- **Cấu hình AWS Storage Gateway**: Đã hiểu và cấu hình thành công AWS File Storage Gateway để kết nối bộ nhớ on-premises với AWS S3.
- **Bảo vệ ứng dụng web với WAF**: Đã triển khai AWS WAF để bảo vệ các ứng dụng web khỏi các cuộc tấn công bằng Web ACLs và các quy tắc tuỳ chỉnh.
- **Quản lý tài nguyên với Tags & Resource Groups**: Đã học cách tổ chức và quản lý các tài nguyên AWS một cách hiệu quả bằng Tags và Resource Groups.
- **Hoàn thành tất cả bài lab**: Đã hoàn thành thành công tất cả 4 bài lab thực hành như hướng dẫn.

---

## Tuần 12:
### Mục tiêu Tuần 12:
- Hiểu và cấu hình IAM Tag-based Access Control cho tài nguyên EC2.
- Tìm hiểu về công cụ giám sát mã nguồn mở Grafana và cách tạo dashboard cơ bản.
- Thiết lập IAM Permissions Boundaries để ủy quyền và giới hạn truy cập tối đa của IAM Entities.
- Sử dụng bộ công cụ AWS Systems Manager (SSM) để quản lý cơ sở hạ tầng máy chủ từ xa, bao gồm Fleet Manager, cập nhật OS tự động qua Patch Manager và thực thi script từ xa qua Run Command.

### Công việc cần thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học IAM Tag-based Access Control<br>- Đọc hướng dẫn và cấu hình IAM Tags để kiểm soát truy cập vào tài nguyên EC2 | 06/07/2026 | 06/07/2026 | <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html" target="_blank">AWS IAM Tagging</a> |
| 3 | - Học cơ bản về giám sát Grafana<br>- Đọc và hiểu các khái niệm Grafana và tạo Dashboard cơ bản | 07/07/2026 | 07/07/2026 | <a href="https://grafana.com/docs/grafana/latest/" target="_blank">Grafana User Guide</a> |
| 4 | - Học IAM Permission Boundary<br>- Cấu hình permission boundaries để giới hạn quyền tối đa của IAM Entities | 08/07/2026 | 08/07/2026 | <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html" target="_blank">AWS Permissions Boundaries</a> |
| 5 | - Học các khái niệm AWS Systems Manager (SSM)<br>- Đọc giới thiệu về SSM, Fleet Manager, Patch Manager và Run Command | 09/07/2026 | 09/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html" target="_blank">AWS Systems Manager User Guide</a> |
| 6 | - Thiết lập cơ sở hạ tầng mạng và IAM Roles cho SSM<br>- Tạo VPC `windows-lab-ssm`, Internet Gateway, 2 Subnets<br>- Tạo IAM Role/Instance Profile với chính sách `AmazonSSMManagedInstanceCore`<br>- Khởi chạy 2 máy ảo EC2 Windows Server gắn với IAM Role | 10/07/2026 | 10/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html" target="_blank">SSM Agent on Windows Server</a> |
| 7 - Chủ nhật | - Thực hiện cập nhật patch và chạy lệnh từ xa qua SSM<br>- Sử dụng Patch Manager để quét lỗ hổng và cài đặt cập nhật OS tự động<br>- Sử dụng Run Command để chạy PowerShell `net user` từ xa và lưu log vào S3<br>- Thực hiện dọn dẹp tất cả tài nguyên AWS để tránh các chi phí không mong muốn | [11/07/2026](./Worklog_week1.12/) | [12/07/2026](./Worklog_week1.12/) | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html" target="_blank">SSM Patch Manager</a><br><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html" target="_blank">SSM Run Command</a> |

### Thành tựu Tuần 12:
