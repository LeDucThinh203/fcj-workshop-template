---
title: "Nhật ký công việc"
date: 2026-04-27
weight: 1
pre : " <b> 1. </b> "
---

## Tuần 1:
- Kết nối và làm quen với các thành viên của First Cloud Journey.
- Nghiên cứu lý thuyết về các dịch vụ AWS cơ bản và tìm hiểu tài liệu hướng dẫn sử dụng AWS Management Console & AWS CLI.

### Công việc cần thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Làm quen với các thành viên FCJ<br>- Đọc và ghi nhớ các quy định, quy tắc tại đơn vị thực tập | 20/04/2026 | 20/04/2026 |  |
| 3 | - Tìm hiểu lý thuyết về điện toán đám mây và các dịch vụ cơ bản của AWS:<br>  + Compute (EC2, Lambda)<br>  + Storage (S3, EBS)<br>  + Networking (VPC, Route 53)<br>  + Database (RDS, DynamoDB) | [21/04/2026](./Worklog_week1.1/) | [21/04/2026](./Worklog_week1.1/) | [AWS Cloud Concepts](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html) |
| 4 | - Tìm hiểu về chính sách tài khoản AWS Free Tier<br>- Nghiên cứu tài liệu giới thiệu về AWS Management Console & AWS CLI:<br>  + Quy trình đăng ký tài khoản AWS<br>  + Hướng dẫn cài đặt và cấu hình AWS CLI trên các hệ điều hành | 22/04/2026 | 22/04/2026 | [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) |
| 5 | - Nghiên cứu lý thuyết cơ bản về dịch vụ Amazon EC2:<br>  + Khái niệm Instance Types, AMI, Key Pair và EBS Volumes/Snapshots<br>  + Tìm hiểu các phương thức kết nối an toàn từ xa tới EC2 qua giao thức SSH<br>  + Tìm hiểu vai trò của Elastic IP | 23/04/2026 | 23/04/2026 | [Amazon EC2 Overview](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) |
| 6 | - Đọc tài liệu hướng dẫn quy trình:<br>  + Khởi tạo EC2 instance qua Console và CLI<br>  + Cách sử dụng SSH key pair để kết nối máy chủ<br>  + Cách gắn và quản lý EBS volume | 24/04/2026 | 24/04/2026 | [Amazon EC2 Instance Lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html) |
| 7 - Chủ nhật | - Nghiên cứu lý thuyết nâng cao:<br>  + Cách thiết lập Security Groups để phân quyền cổng truy cập mạng<br>  + Cách cài đặt và vận hành các Web Server (Apache/Nginx) trên hệ điều hành Linux<br>  + Tìm hiểu về kiến trúc lưu trữ đối tượng của AWS S3 (Buckets, Objects, Permissions) | 25/04/2026 | 26/04/2026 | [Amazon S3 Basics](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) |

---

## Tuần 2:
### Mục tiêu Tuần 2:
- Tìm hiểu về các công cụ quản lý chi phí và lập hóa đơn trên AWS (AWS Billing & Cost Management).
- Nắm vững vai trò và cách cấu hình AWS Budgets để kiểm soát chi tiêu đám mây.
- Thực hành thiết lập hạn mức ngân sách và cấu hình cảnh báo ngưỡng chi phí tự động.

### Công việc cần thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học tổng quan về quản lý chi phí trên AWS:<br>  + Các công cụ AWS Billing<br>  + Cách tính toán chi phí dịch vụ cơ bản | 27/04/2026 | 27/04/2026 | [AWS Billing Overview](https://docs.aws.amazon.com/billing/latest/userguide/billing-whatis.html) |
| 3 | - Tìm hiểu cơ chế hoạt động của AWS Budgets:<br>  + Khái niệm Cost budget và Usage budget<br>  + Ngưỡng cảnh báo chi phí thực tế và dự báo | [28/04/2026](./Worklog_week1.2/) | [28/04/2026](./Worklog_week1.2/) | [AWS Budgets Guide](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) |
| 4 | - Nghiên cứu thiết lập kế hoạch ngân sách cho tài khoản Free Tier để tránh phát sinh chi phí ngoài ý muốn. | 29/04/2026 | 29/04/2026 | [AWS Free Tier Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) |
| 5 | - Học cách cấu hình nhận cảnh báo ngân sách qua email và các kênh thông báo tự động (Amazon SNS). | 30/04/2026 | 30/04/2026 | [AWS Budgets Alerts](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-alerts.html) |
| 6 | - **Thực hành (Phần 1):** Khởi tạo ngân sách chi phí hàng tháng (My Monthly Cost Budget) với hạn mức cảnh báo $100. | 01/05/2026 | 01/05/2026 | [Creating a Cost Budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create-cost.html) |
| 7 - Chủ nhật | - **Thực hành (Phần 2):** Khởi tạo thêm ngân sách dự phòng $200 (My-200$-budget) và ngân sách mức độ sử dụng tài nguyên (Cost budget). Xác minh trạng thái và hoạt động cảnh báo. | 02/05/2026 | 03/05/2026 | [Monitoring Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-viewing.html) |

### Thành tựu Tuần 2:
#### Lý thuyết:
- Hiểu rõ mô hình tính phí của AWS, các yếu tố ảnh hưởng trực tiếp đến hóa đơn và cách sử dụng AWS Budgets làm chốt chặn bảo mật tài chính.
- Nắm vững sự khác nhau giữa Cost Budgets (ngân sách chi phí) và Usage Budgets (ngân sách lượng tài nguyên tiêu thụ).

#### Thực hành:
- Khởi tạo thành công 3 ngân sách khác nhau phục vụ theo dõi chi tiêu đa chiều trên AWS Console.
- Cấu hình hoàn chỉnh ngưỡng cảnh báo tự động gửi email khi chi phí thực tế đạt 80% hoặc chi phí dự báo vượt hạn mức định trước.

---

## Tuần 3:
### Mục tiêu Tuần 3:
- Tìm hiểu về dịch vụ Amazon EC2 trên AWS.
- Thực hành khởi tạo, cấu hình và quản lý EC2 Instances trong Public Subnet và Private Subnet.
- Hiểu dịch vụ AWS IAM và thiết lập phân quyền bảo mật, bao gồm các cấu hình giới hạn chuyển đổi Role theo IP và thời gian.

### Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Tổng quan về Amazon EC2<br>- Tìm hiểu về Instance Types, AMI, Key Pair và Snapshot<br>- Hiểu cơ chế hoạt động của EC2 Instances | 05/04/2026 | 05/04/2026 | [Amazon EC2 Basics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 3 | - Chuẩn bị môi trường EC2<br>+ Tạo VPC với Public Subnet và Private Subnet<br>+ Tạo Security Group mở các cổng thích hợp (cổng 22 cho SSH, cổng 80/443 cho Web Server) | [05/05/2026](./Worklog_week1.3/) | [05/05/2026](./Worklog_week1.3/) | [EC2 Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)<br>FCJ Lab |
| 4 | - Khởi tạo EC2 Instance trong Public Subnet (EC2_Public)<br>+ Tạo Public EC2 Instance chạy Linux<br>+ Kiểm tra và kết nối SSH tới máy chủ Public | 05/06/2026 | 05/06/2026 | [EC2 Public Instance Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 5 | - Khởi tạo EC2 Instance trong Private Subnet (EC2_Private)<br>+ Tạo Private EC2 Instance chạy Linux<br>+ Cấu hình kết nối và bảo mật cho máy chủ Private | 05/07/2026 | 05/07/2026 | [EC2 Private Instance Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 6 | - Tìm hiểu và cấu hình bảo mật IAM<br>+ Tạo IAM User và User Groups<br>+ Gán chính sách phân quyền và kiểm tra quyền hạn | 05/08/2026 | 05/08/2026 | [AWS IAM Basics](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)<br>FCJ Lab |
| 7 - Chủ nhật | - Triển khai các chính sách bảo mật nâng cao cho IAM Roles<br>+ Giới hạn chuyển đổi Role theo địa chỉ IP nguồn (SourceIp)<br>+ Giới hạn chuyển đổi Role theo khung giờ làm việc cố định (CurrentTime) | 05/09/2026 | 05/10/2026 | [IAM Policies & Switch Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html)<br>FCJ Lab |

---

## Tuần 4:
### Mục tiêu Tuần 4:
- Khởi tạo và cấu hình môi trường mạng (VPC, Subnet Groups, Security Groups) cho các EC2 Instance và RDS DB Instance.
- Triển khai EC2 Instance chạy Linux, cấu hình quyền hạn file khóa SSH và thực hiện kết nối SSH an toàn qua MobaXterm.
- Cài đặt Git, Node.js và MySQL client trên máy chủ EC2 để chuẩn bị và chạy ứng dụng Web Node.js kết nối tới RDS database.
- Hiểu rõ các thao tác quản trị cơ sở dữ liệu trên RDS bao gồm xem Logs & Events, thiết lập Maintenance & Backup, thực hiện Snapshots và tìm hiểu kiến trúc sẵn sàng cao (Multi-AZ, Read Replicas).

### Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày kết thúc | Nguồn tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Tổng quan về Amazon RDS<br>- So sánh RDS với các dịch vụ lưu trữ khác (EC2 DB, DynamoDB, Redshift, S3) | 11/05/2026 | 11/05/2026 | [Amazon RDS Documentation](https://docs.aws.amazon.com/rds/) |
| 3 | - Cấu hình mạng cho RDS:<br>  + Tạo VPC và các subnet liên quan<br>  + Tạo Security Groups cho EC2 và RDS<br>  + Tạo DB Subnet Group | [12/05/2026](./Worklog_week1.4/) | [12/05/2026](./Worklog_week1.4/) | [VPC for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) |
| 4 | - Thực hành khởi tạo một Amazon RDS instance<br>- Cấu hình các tham số, thông tin tài khoản và cấu hình bảo mật cho Database | 13/05/2026 | 13/05/2026 | [Creating an RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) |
| 5 | - Khởi tạo EC2 Instance và chuẩn bị môi trường kết nối:<br>  + Tạo Linux EC2 Instance<br>  + Cấu hình quyền truy cập SSH Key Pair (`chmod 400`) và kết nối bằng MobaXterm<br>  + Cài đặt môi trường runtime Git và Node.js trên EC2 | 14/05/2026 | 14/05/2026 | [EC2 Linux Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 6 | - Triển khai ứng dụng Web trên EC2 và kết nối đến RDS:<br>  + Clone repository dự án từ Github và cài đặt các package phụ thuộc<br>  + Cài đặt MySQL client, chạy các script SQL khởi tạo cơ sở dữ liệu và các bảng<br>  + Thêm dữ liệu mẫu (mock user data) và kiểm tra kết nối ứng dụng qua RDS Endpoint | 15/05/2026 | 15/05/2026 | [Connecting to RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html)<br>FCJ Lab |
| 7 - Chủ nhật | - Quản trị và bảo trì cơ sở dữ liệu:<br>  + Xem và theo dõi Logs & Events của RDS<br>  + Cấu hình các tùy chọn bảo trì, thực hành tạo Snapshot thủ công và tự động<br>  + Tìm hiểu kiến trúc Multi-AZ, Read Replicas và dọn dẹp tài nguyên tối ưu chi phí | 16/05/2026 | 17/05/2026 | [RDS Backup and Restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html)<br>FCJ Lab |

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
- Hiểu rõ khái niệm và kiến trúc hoạt động của AWS Systems Manager (SSM) Session Manager để quản trị máy chủ từ xa an toàn.
- Nắm vững vai trò của VPC Endpoints (Interface Endpoints) trong việc kết nối riêng tư từ mạng nội bộ tới các dịch vụ AWS mà không qua định tuyến Internet.
- Hiểu cách NAT Gateway dịch chuyển địa chỉ IP và định tuyến lưu lượng đi ra ngoài (outbound-only) cho phân khu mạng Private Subnet.

### Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học lý thuyết về AWS Systems Manager (SSM) Session Manager<br>- Tìm hiểu về VPC Endpoints (Interface Endpoints và Gateway Endpoints)<br>- Tìm hiểu về NAT Gateway và cách hoạt động của nó trong Public Subnet để cung cấp Internet cho Private Subnet | 18/05/2026 | 18/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | - **Thực hành (Phần 1):**<br>  + Tạo VPC với các phân khu mạng Public Subnet và Private Subnet<br>  + Khởi tạo NAT Gateway trong Public Subnet và cấu hình Elastic IP<br>  + Cấu hình bảng định tuyến Route Table cho Private Subnets đi qua NAT Gateway để kết nối ra ngoài Internet một cách an toàn | 19/05/2026 | 19/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - **Thực hành (Phần 2):**<br>  + Khởi tạo EC2 Instance chạy Linux trong Private Subnet (không gán Public IP)<br>  + Tạo và gán IAM Role cho EC2 Instance với các quyền cần thiết để giao tiếp với AWS Systems Manager (`AmazonSSMManagedInstanceCore`)<br>  + Cấu hình Security Group cho EC2 Instance (không mở cổng 22 SSH) | 20/05/2026 | 20/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | - **Thực hành (Phần 3):**<br>  + Tạo các VPC Endpoints (`ssm`, `ssmmessages`, `ec2messages`) trong Private Subnet<br>  + Cấu hình Security Group cho các VPC Endpoints để cho phép kết nối từ EC2 Instance<br>  + Kiểm tra kết nối từ xa vào EC2 Instance trong Private Subnet qua SSM Session Manager mà không cần cổng SSH<br>  + Dọn dẹp tài nguyên để tránh phát sinh chi phí | [21/05/2026](./Worklog_week1.5/) | [21/05/2026](./Worklog_week1.5/) | https://cloudjourney.awsstudygroup.com/ |

### Thành tựu Tuần 5:
#### Lý thuyết:
- Hiểu rõ khái niệm và kiến trúc hoạt động của AWS Systems Manager (SSM) Session Manager để quản trị máy chủ từ xa an toàn.
- Nắm vững vai trò của VPC Endpoints (Interface Endpoints) trong việc kết nối riêng tư từ mạng nội bộ tới các dịch vụ AWS mà không qua định tuyến Internet.
- Hiểu cách NAT Gateway dịch chuyển địa chỉ IP và định tuyến lưu lượng đi ra ngoài (outbound-only) cho phân khu mạng Private Subnet.

#### Thực hành:
- Xây dựng thành công VPC mạng ảo với các phân khu mạng cô lập (Private Subnets) và NAT Gateway tại Public Subnet.
- Cấu hình bảng định tuyến Route Table cho Private Subnets đi qua NAT Gateway để kết nối ra ngoài Internet một cách an toàn.
- Thiết lập hoàn chỉnh các VPC Endpoints (`ssm`, `ssmmessages`, `ec2messages`) và kết nối thành công vào EC2 Instance trong Private Subnet qua SSM Session Manager mà không cần mở cổng SSH.

---

## Tuần 6:
### Mục tiêu Tuần 6:
- Hiểu rõ cơ chế hoạt động của Amazon CloudWatch (Metrics, Logs, Alarms, Dashboards) để giám sát hiệu năng hệ thống.
- Tìm hiểu về AWS Support Plans và cách quản lý Support Cases trực tiếp trên AWS Console.
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

### Thành tựu Tuần 6:
#### Lý thuyết:
- Nắm vững kiến trúc Hybrid DNS kết nối hệ thống On-premises (giả lập Microsoft AD trên EC2) và AWS VPC sử dụng Route 53 Resolver (Inbound/Outbound Endpoints).
- Hiểu rõ cơ chế hoạt động của Amazon CloudWatch (Metrics, Logs, Alarms, Dashboards) để giám sát hiệu năng hệ thống.
- Tìm hiểu về AWS Support Plans và cách quản lý Support Cases trực tiếp trên AWS Console.

#### Thực hành:
- Deploy thành công kiến trúc mạng Hybrid DNS bằng CloudFormation.
- Cấu hình chuẩn xác các quy tắc Security Groups cho phép luồng lưu lượng DNS (cổng 53 TCP/UDP) lưu thông an toàn giữa On-premises và AWS.
- Thiết lập thành công Inbound và Outbound Resolver Endpoints cùng Resolver Rules để phân giải chính xác tên miền chéo.

---

## Tuần 7:
### Mục tiêu Tuần 7:
- Làm quen và thực hành sử dụng AWS CLI để xem, cấu hình và quản trị các tài nguyên AWS (S3, SNS, IAM, VPC, EC2).
- Hiểu kiến trúc quản lý đa tài khoản bằng AWS Organizations, cấu hình đơn vị tổ chức (OU) và IAM Identity Center.
- Nắm vững giải pháp sao lưu tập trung bằng AWS Backup để bảo vệ an toàn dữ liệu trên AWS.

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
#### Lý thuyết:
- Hiểu cách cấu hình và gọi các API dịch vụ AWS qua AWS CLI.
- Nắm vững mô hình quản trị tài khoản quy mô doanh nghiệp với AWS Organizations và IAM Identity Center, phân quyền theo thời gian và chính sách khách hàng tự quản (Customer Managed Policies).
- Hiểu nguyên lý hoạt động của AWS Backup: Backup Vaults, Backup Plans, Retention rules và khôi phục dữ liệu (Restore).

#### Thực hành:
- Thực hành thành thạo các câu lệnh CLI cơ bản và nâng cao để tạo/quản lý EC2, S3, IAM và VPC.
- Xây dựng thành công hệ thống sao lưu tự động (AWS Backup Plan) cho hạ tầng máy chủ EC2 và lưu trữ S3.
- Thực hiện thành công quy trình kiểm thử khôi phục dữ liệu (Test Restore) từ bản sao lưu và dọn dẹp tài nguyên (Cost Optimization).

### Hình ảnh minh chứng:

1. **Khởi tạo hạ tầng (Deploy infrastructure)**
   ![Deploy infrastructure](../../images/1-Worklog/Worklog_week1.7/Deloy%20infrastructure.png)
   *Mô tả chi tiết: Quá trình triển khai hạ tầng cơ sở cho bài thực hành sử dụng AWS CloudFormation. Các tài nguyên cần thiết như EC2 instance, EBS volume, hoặc các thiết lập mạng cơ bản được tự động hóa khởi tạo. Đây là bước chuẩn bị quan trọng để có tài nguyên thực tế nhằm kiểm thử tính năng sao lưu (backup) và phục hồi (restore).*

2. **Tạo thư mục S3 (Create s3 folder)**
   ![Create S3 Folder](../../images/1-Worklog/Worklog_week1.7/Create%20s3%20folder.png)
   *Mô tả chi tiết: Khởi tạo thư mục hoặc bucket trên Amazon S3. S3 thường được sử dụng làm nơi lưu trữ an toàn, bền bỉ và tiết kiệm chi phí cho các bản sao lưu (backup vault/storage) từ AWS Backup hoặc các dịch vụ khác. Việc thiết lập cấu trúc lưu trữ chuẩn xác đảm bảo dữ liệu backup được tổ chức tốt và dễ dàng truy xuất khi cần.*

3. **Cấu hình kế hoạch sao lưu (Create Backup plans)**
   ![Create Backup plans](../../images/1-Worklog/Worklog_week1.7/Create%20Backup%20plans.png)
   *Mô tả chi tiết: Cấu hình AWS Backup plan. Bước này thiết lập các quy tắc tự động hóa quá trình sao lưu, bao gồm tần suất sao lưu (ví dụ: hàng ngày, hàng tuần), thời gian lưu trữ (retention period) và cửa sổ sao lưu (backup window). Quản lý sao lưu tự động giúp doanh nghiệp tuân thủ các quy định về an toàn dữ liệu mà không tốn công sức vận hành thủ công.*

4. **Kiểm tra phục hồi dữ liệu (Test Restore)**
   ![Test Restore](../../images/1-Worklog/Worklog_week1.7/Test%20Restore.png)
   *Mô tả chi tiết: Thực hiện quy trình phục hồi (restore) dữ liệu từ một bản sao lưu (recovery point) đã tạo trước đó. Đây là bước kiểm chứng quan trọng nhất trong bất kỳ chiến lược sao lưu nào, đảm bảo rằng trong trường hợp xảy ra sự cố mất mát dữ liệu hoặc hỏng hóc hệ thống, dữ liệu có thể được khôi phục nguyên vẹn và hệ thống có thể hoạt động trở lại bình thường.*

5. **Dọn dẹp tài nguyên (Clean up resources)**
   ![Clean up resources](../../images/1-Worklog/Worklog_week1.7/Clean%20up%20resources.png)
   *Mô tả chi tiết: Xóa bỏ các tài nguyên AWS đã được tạo ra trong suốt quá trình thực hành (như EC2, S3, Backup plans, CloudFormation stack). Việc dọn dẹp cẩn thận sau khi hoàn thành lab là thao tác bắt buộc để tối ưu hóa chi phí (Cost Optimization), đảm bảo tài khoản không phải chịu các khoản phí duy trì cho những tài nguyên không còn sử dụng.*

---

## Tuần 8:
### Mục tiêu Tuần 8:
- Tìm hiểu cách quản lý danh tính và phân quyền truy cập nâng cao sử dụng IAM Groups, Users, Policies và Roles.
- Học và cấu hình mã hóa dữ liệu trên Amazon S3 sử dụng AWS Key Management Service (KMS), cấu hình chia sẻ dữ liệu được mã hóa an toàn giữa các tài khoản AWS.
- Cấu hình theo dõi và ghi nhật ký hoạt động hệ thống bằng AWS CloudTrail để phục vụ giám sát và kiểm toán bảo mật.
- Sử dụng Amazon Athena để thực hiện truy vấn phân tích log CloudTrail được lưu trữ trên S3 bucket bằng ngôn ngữ SQL.

### Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học lý thuyết về IAM Groups, Users, Policies, Roles nâng cao và nguyên tắc đặc quyền tối thiểu<br>- **Thực hành (Phần 1)**: Khởi tạo IAM Groups và Users phục vụ việc kiểm soát truy cập phân quyền | 08/06/2026 | 08/06/2026 | [IAM Policies Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) |
| 3 | - Học lý thuyết về mã hóa dữ liệu AWS KMS (KMS Keys, Key Policies)<br>- **Thực hành (Phần 2)**: Khởi tạo AWS Key Management Service (KMS) và cấu hình Key Policy | 09/06/2026 | 09/06/2026 | [AWS KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) |
| 4 | - **Thực hành (Phần 3)**: Tạo IAM Policy và IAM Role cho phép sử dụng khóa KMS<br>- Khởi tạo S3 bucket và tải tệp tin dữ liệu thử nghiệm lên, cấu hình mã hóa SSE-KMS | 10/06/2026 | 10/06/2026 | [Amazon S3 KMS Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) |
| 5 | - **Thực hành (Phần 4)**: Kiểm tra cấu hình và thực hiện chia sẻ dữ liệu đã mã hóa trên S3 bucket với tài khoản AWS khác thông qua khóa KMS | 11/06/2026 | 11/06/2026 | [S3 Cross-Account Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html) |
| 6 | - Học lý thuyết về theo dõi hệ thống với AWS CloudTrail<br>- **Thực hành (Phần 5)**: Khởi tạo CloudTrail trail, cấu hình lưu trữ log hoạt động hệ thống vào S3 bucket | 12/06/2026 | 12/06/2026 | [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) |
| 7 - Chủ nhật | - **Thực hành (Phần 6)**: Cấu hình Amazon Athena, kết nối nguồn dữ liệu log CloudTrail trên S3 và thực hiện các câu lệnh SQL để truy vấn log<br>- Tiến hành dọn dẹp sạch sẽ tài nguyên để tránh phát sinh chi phí | [13/06/2026](./Worklog_week1.8/) | [14/06/2026](./Worklog_week1.8/) | [Querying CloudTrail Logs with Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-cloudtrail-logs.html) |

### Thành tựu Tuần 8:
- **Quản trị truy cập (IAM)**: Thiết lập thành công phân quyền an toàn qua IAM Groups, Users, Policies và Roles đảm bảo tuân thủ nguyên tắc đặc quyền tối thiểu.
- **Mã hóa & Chia sẻ dữ liệu**: Cấu hình thành công AWS KMS để mã hóa S3 bucket, thiết lập Key Policy cho phép chia sẻ dữ liệu mã hóa an toàn với tài khoản AWS bên ngoài.
- **Giám sát & Kiểm toán (CloudTrail)**: Triển khai thành công AWS CloudTrail ghi nhận toàn bộ hoạt động API của tài khoản vào lưu trữ S3.
- **Phân tích log (Amazon Athena)**: Thành thạo việc sử dụng Amazon Athena viết truy vấn SQL trực tiếp trên S3 để phân tích log hoạt động CloudTrail phục vụ điều tra sự cố bảo mật.
- **Tối ưu chi phí**: Thực hiện dọn dẹp sạch sẽ tài nguyên thực hành để tránh phát sinh chi phí ngoài ý muốn.

### Hình ảnh minh chứng:

1. **Tạo IAM Group và User (Create Group and User)**
   ![Tạo IAM Group và User](/images/1-Worklog/Worklog_week1.8/Create%20Group%20and%20User.png)
   *Mô tả chi tiết: Ảnh ghi lại giao diện quản trị IAM sau khi tạo thành công IAM Group và IAM User. Việc phân chia người dùng vào các nhóm giúp quản trị viên dễ dàng quản lý quyền truy cập tập trung theo vai trò công việc.*

2. **Khởi tạo AWS Key Management Service (Create Key Management Service)**
   ![Tạo khóa KMS](/images/1-Worklog/Worklog_week1.8/Create%20Key%20Management%20Service.png)
   *Mô tả chi tiết: Giao diện tạo khóa mã hóa tùy chỉnh (Customer Managed Key) trong dịch vụ AWS KMS. Khóa này được sử dụng để mã hóa dữ liệu trên S3 và kiểm soát quyền giải mã thông qua Key Policy.*

3. **Cấu hình Policy và Role trong IAM (Create policy and role)**
   ![Cấu hình Policy và Role](/images/1-Worklog/Worklog_week1.8/Create%20policy%20and%20role.png)
   *Mô tả chi tiết: Thiết lập các IAM Policy chi tiết định nghĩa quyền sử dụng khóa KMS và IAM Role được gán các quyền này để cho phép các thực thể hoặc tài khoản khác thực hiện thao tác mã hóa/giải mã.*

4. **Tạo S3 Bucket và tải dữ liệu lên (Create and upload data bucket)**
   ![Tạo S3 Bucket và Upload](/images/1-Worklog/Worklog_week1.8/Create%20and%20upload%20data%20bucket.png)
   *Mô tả chi tiết: Tạo S3 bucket mới dùng để lưu trữ dữ liệu cần bảo vệ và thực hiện tải lên các tệp tin dữ liệu mẫu, chuẩn bị cho việc thử nghiệm cấu hình mã hóa.*

5. **Kiểm tra và chia sẻ dữ liệu mã hóa trên S3 (Test and share encrypted data on S3)**
   ![Chia sẻ dữ liệu mã hóa](/images/1-Worklog/Worklog_week1.8/Test%20and%20share%20encrypted%20data%20on%20S3.png)
   *Mô tả chi tiết: Xác minh việc mã hóa dữ liệu phía máy chủ (SSE-KMS) hoạt động chính xác trên S3 bucket và cấu hình chính sách chia sẻ chéo tài khoản, cho phép tài khoản AWS bên ngoài có thể đọc được dữ liệu này thông qua quyền hạn khóa KMS.*

6. **Khởi tạo AWS CloudTrail (Create CloudTrail)**
   ![Tạo CloudTrail](/images/1-Worklog/Worklog_week1.8/Create%20CloudTrail.png)
   *Mô tả chi tiết: Khởi tạo dịch vụ AWS CloudTrail để ghi lại nhật ký (logs) các cuộc gọi API và hoạt động diễn ra trong tài khoản AWS, hướng luồng log này lưu trữ vào một S3 bucket chuyên dụng.*

7. **Ghi log hoạt động vào CloudTrail (Logging to CloudTrail)**
   ![Ghi log CloudTrail](/images/1-Worklog/Worklog_week1.8/Logging%20to%20CloudTrail.png)
   *Mô tả chi tiết: Minh chứng các sự kiện hoạt động (events) đang được ghi nhận liên tục và xuất bản đầy đủ vào S3 bucket dưới dạng các tệp nén log CloudTrail.*

8. **Cấu hình Amazon Athena (Create Amazon Athena)**
   ![Cấu hình Amazon Athena](/images/1-Worklog/Worklog_week1.8/Create%20Amazon%20Athena.png)
   *Mô tả chi tiết: Thiết lập Amazon Athena bao gồm cấu hình thư mục lưu kết quả truy vấn (Query result location) trên S3 và khởi tạo cơ sở dữ liệu/bảng ánh xạ tới tệp tin log CloudTrail.*

9. **Truy vấn log bằng Athena SQL (Retrieve data with athena)**
   ![Truy vấn dữ liệu bằng Athena](/images/1-Worklog/Worklog_week1.8/Retrieve%20data%20with%20athena.png)
   *Mô tả chi tiết: Thực thi câu lệnh SQL SELECT trên giao diện Amazon Athena để truy vấn và trích xuất thông tin chi tiết từ log CloudTrail, ví dụ như tìm kiếm ai đã thực hiện thao tác gì trên tài nguyên tại thời điểm nào.*

10. **Dọn dẹp sạch tài nguyên thực hành (Clean)**
    ![Dọn dẹp tài nguyên](/images/1-Worklog/Worklog_week1.8/Clean.png)
    *Mô tả chi tiết: Tiến hành xóa bỏ tất cả tài nguyên đã tạo trong bài thực hành (KMS Keys, CloudTrail Trails, Athena tables, S3 Buckets, IAM Roles/Policies/Users/Groups) để đảm bảo không phát sinh chi phí duy trì dịch vụ sau khi kết thúc lab.*

---

## Tuần 9:
### Mục tiêu Tuần 9:
- Tìm hiểu cách tự động hóa vận hành serverless sử dụng AWS Lambda và Amazon EventBridge để khởi động và dừng EC2 instance tự động dựa trên lịch trình.
- Tìm hiểu cách gắn thẻ quản lý tài nguyên (Resource Tags), quản lý nhóm tài nguyên (Resource Groups) và lọc tài nguyên trên AWS.
- Cấu hình tích hợp thông báo vận hành (ChatOps) gửi trạng thái hoạt động của Lambda tới kênh Slack thông qua Incoming Webhooks.
- Kích hoạt và cấu hình AWS Security Hub để đánh giá posture bảo mật tài khoản (CSPM - Cloud Security Posture Management).

### Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học lý thuyết về AWS Lambda và EventBridge scheduler<br>- Tìm hiểu về thiết lập Tags, Tag Editor và Resource Groups trên AWS | 15/06/2026 | 15/06/2026 | [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/) |
| 3 | - **Thực hành (Phần 1)**: Cấu hình mạng VPC, Subnets, Security Groups và khởi chạy các EC2 Instances để thử nghiệm<br>- Tạo IAM Role cho Lambda với các quyền truy cập EC2 và CloudWatch Logs | 16/06/2026 | 16/06/2026 | [AWS Lambda IAM Permissions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) |
| 4 | - **Thực hành (Phần 2)**: Viết code Python (boto3) trong AWS Lambda để tự động hóa dừng (Stop) các máy ảo EC2 có gắn thẻ tag chỉ định | 17/06/2026 | 17/06/2026 | [Boto3 EC2 Client Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html) |
| 5 | - **Thực hành (Phần 3)**: Viết code Python (boto3) trong AWS Lambda để tự động hóa khởi động (Start) các máy ảo EC2<br>- Cấu hình Incoming Webhooks trên Slack để làm endpoint nhận tin nhắn | 18/06/2026 | 18/06/2026 | [Slack Incoming Webhooks Guide](https://api.slack.com/messaging/webhooks) |
| 6 | - **Thực hành (Phần 4)**: Tích hợp mã nguồn gửi tin nhắn thông báo tự động từ Lambda tới Slack và kiểm tra kết quả | 19/06/2026 | 19/06/2026 | [Sending Slack Messages with Lambda](https://api.slack.com/messaging/webhooks) |
| 7 - Chủ nhật | - **Thực hành (Phần 5)**: Kích hoạt AWS Security Hub CSPM, phân tích điểm số bảo mật của tài khoản và tiến hành dọn dẹp sạch sẽ tài nguyên sau thực hành | [20/06/2026](./Worklog_week1.9/) | [21/06/2026](./Worklog_week1.9/) | [AWS Security Hub User Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) |

### Thành tựu Tuần 9:
- **Tự động hóa Serverless**: Xây dựng thành công giải pháp tự động hóa bằng AWS Lambda (Python boto3) kết hợp EventBridge Scheduler để dừng các EC2 instances thử nghiệm vào buổi tối và bật lại vào ban ngày nhằm tối ưu chi phí.
- **Tích hợp ChatOps**: Cấu hình thành công Slack Incoming Webhook để Lambda gửi tin nhắn cảnh báo trạng thái chạy/dừng máy ảo theo thời gian thực trực tiếp về kênh vận hành Slack.
- **Quản trị tài nguyên**: Thành thạo việc gán thẻ (Tags) cho tài nguyên, sử dụng Tag Editor để chỉnh sửa tag hàng loạt và gom nhóm quản lý qua AWS Resource Groups.
- **Bảo mật và Tối ưu**: Kích hoạt thành công AWS Security Hub để đánh giá điểm số tuân thủ bảo mật CSPM, đồng thời dọn dẹp triệt để các tài nguyên (EC2, Lambda, Security Hub, Logs) để tránh phát sinh chi phí ngoài ý muốn.

### Hình ảnh minh chứng:

1. **Khởi tạo VPC (Create VPC)**
   ![CreateVPC](../images/1-Worklog/Worklog_week1.9/CreateVPC.png)
   *Mô tả chi tiết: Hình ảnh minh họa bảng điều khiển (console) của AWS khi tiến hành tạo một Virtual Private Cloud (VPC) mới. Quá trình này bao gồm việc xác định dải địa chỉ IPv4 (CIDR block), tạo các mạng con (Subnets) ở các Availability Zones khác nhau để tăng tính sẵn sàng. Đồng thời, thiết lập Internet Gateway (IGW) và Route Tables giúp định tuyến lưu lượng truy cập từ Internet vào Public Subnet một cách an toàn.*

2. **Tạo Security Group (Create Security Group)**
   ![Create Security Group](../images/1-Worklog/Worklog_week1.9/Create%20Security%20Group.png)
   *Mô tả chi tiết: Đây là bước thiết lập "bức tường lửa" ảo (Virtual Firewall) cấp độ instance. Hình ảnh cho thấy việc cấu hình các quy tắc Inbound (Inbound rules) để mở các cổng mạng (ports) cần thiết, ví dụ như cổng 22 (SSH) để quản trị máy chủ từ xa, hoặc cổng 80/443 (HTTP/HTTPS) cho web. Chỉ những địa chỉ IP hoặc dải mạng được chỉ định mới có thể kết nối vào tài nguyên.*

3. **Khởi chạy EC2 (Create Ec2)**
   ![Create Ec2](../images/1-Worklog/Worklog_week1.9/Create%20Ec2.png)
   *Mô tả chi tiết: Hình ảnh chụp lại màn hình Launch Instance thành công. Máy ảo (EC2) đã được cấp phát với thông số cấu hình cụ thể (AMI, Instance Type, Key Pair). Máy ảo này sẽ được đặt trong VPC và Subnet đã tạo trước đó, đồng thời gắn Security Group phù hợp. Đây là tài nguyên tính toán cốt lõi để chạy ứng dụng và sẽ được dùng để kiểm thử tính năng bật/tắt tự động bằng Lambda.*

4. **Tạo IAM Role cho Lambda (Create Role for lamda)**
   ![Create Role for lamda](../images/1-Worklog/Worklog_week1.9/Create%20Role%20for%20lamda.png)
   *Mô tả chi tiết: Hình ảnh hiển thị giao diện IAM (Identity and Access Management) nơi một Role mới đang được tạo dành riêng cho dịch vụ AWS Lambda. Role này được đính kèm các chính sách (Policies) cho phép hàm Lambda có quyền gọi các API của dịch vụ EC2 (như `ec2:StartInstances`, `ec2:StopInstances`) và quyền ghi log hoạt động (CloudWatch Logs) để thuận tiện cho việc debug sau này.*

5. **Tạo hàm Lambda Stop Instance (Function stop instance)**
   ![Function stop instance](../images/1-Worklog/Worklog_week1.9/Function%20stop%20instance.png)
   *Mô tả chi tiết: Giao diện chi tiết của dịch vụ AWS Lambda với hàm có chức năng tự động dừng (Stop) các máy EC2. Mã nguồn (code) của hàm, thường được viết bằng Python (Boto3), sẽ quét các EC2 có gắn thẻ (Tag) cụ thể (ví dụ: `Environment=Dev`) và thực thi lệnh dừng máy. Việc này giúp tiết kiệm chi phí tính toán đáng kể trong những khung giờ ngoài giờ hành chính hoặc ban đêm.*

6. **Tạo hàm Lambda Start Instance (Function start instance)**
   ![Function start instance](../images/1-Worklog/Worklog_week1.9/Function%20start%20instance.png)
   *Mô tả chi tiết: Tương tự như hàm Stop, hình ảnh này minh họa cấu hình của hàm Lambda dùng để tự động khởi động (Start) máy ảo. Được kết hợp với Amazon EventBridge để lên lịch biểu (cron job), hàm này sẽ chạy vào đầu giờ sáng làm việc (ví dụ 8h00 sáng) nhằm đảm bảo các hệ thống luôn sẵn sàng phục vụ khi nhân viên bắt đầu ngày làm việc.*

7. **Tạo máy ảo EC2 với Tags (Create EC2 Instance with tag)**
   ![Create EC2 Instance with tag](../images/1-Worklog/Worklog_week1.9/Create%20EC2%20Instance%20with%20tag.png)
   *Mô tả chi tiết: Minh chứng cho thấy quá trình cấu hình nâng cao khi tạo máy ảo EC2 mới. Ở mục Tags, chúng ta thiết lập các cặp Key-Value (ví dụ: `Project = FirstCloudJourney`, `Environment = Test`). Việc gắn thẻ ngay từ lúc khởi tạo giúp hệ thống tự động hóa (như hàm Lambda vừa tạo) nhận diện đúng mục tiêu để thao tác, tránh ảnh hưởng đến các máy chủ Production.*

8. **Gắn Tag cho EC2 có sẵn (EC2 add tag)**
   ![EC2 add tag](../images/1-Worklog/Worklog_week1.9/EC2%20add%20tag.png)
   *Mô tả chi tiết: Hình ảnh chụp tab Tags trong chi tiết của một máy EC2 đang chạy. Thông qua console, chúng ta bổ sung hoặc chỉnh sửa các thẻ (Tags) cho những máy chủ đã được tạo trước đó. Điều này rất quan trọng để đồng bộ hóa quản lý, phục vụ cho việc kiểm soát chi phí (Cost Allocation Tags) và áp dụng các chính sách phân quyền chi tiết (ABAC).*

9. **Quản lý Tags và Lọc tài nguyên (Managing Tags and Filter resources by tag)**
   ![Managing Tags and Filter resources by tag](../images/1-Worklog/Worklog_week1.9/Managing%20Tags%20and%20Filter%20resources%20by%20tag.png)
   *Mô tả chi tiết: Giao diện Tag Editor hoặc AWS Resource Groups được sử dụng để tìm kiếm hàng loạt tài nguyên. Thay vì phải vào từng dịch vụ, hình ảnh cho thấy cách lọc ra tất cả các tài nguyên (EC2, VPC, Lambda, v.v.) có chung một giá trị Tag nhất định. Tính năng này giúp người quản trị dễ dàng theo dõi và thống kê tổng thể kiến trúc hệ thống.*

10. **Tạo Resource Group (Create a Resource Group)**
    ![Create a Resource Group](../images/1-Worklog/Worklog_week1.9/Create%20a%20Resource%20Group.png)
    *Mô tả chi tiết: Hình ảnh hiển thị bảng điều khiển tạo mới một AWS Resource Group. Bằng cách sử dụng các truy vấn dựa trên Tags, hệ thống sẽ gom nhóm các tài nguyên phân tán lại thành một tập hợp logic. Từ Resource Group này, người dùng có thể thực hiện các thao tác quản trị hàng loạt (bulk actions) thông qua AWS Systems Manager một cách nhanh chóng và an toàn.*

11. **Tích hợp Incoming Web-hooks Slack (Incoming Web-hooks slack)**
    ![Incoming Web-hooks slack](../images/1-Worklog/Worklog_week1.9/Incoming%20Web-hooks%20slack.png)
    *Mô tả chi tiết: Giao diện cấu hình ứng dụng Slack để tạo một Incoming Webhook URL. Webhook này được sử dụng như một điểm cuối (endpoint) để nhận dữ liệu. Trong bài lab, khi các hàm Lambda thực thi việc Start/Stop máy ảo, nó sẽ gửi một payload chứa thông báo kết quả (thành công/thất bại) qua webhook này để hiển thị trực tiếp lên kênh chat (channel) của đội ngũ vận hành.*

12. **Kiểm tra kết quả (Check Result)**
    ![Check Result](../images/1-Worklog/Worklog_week1.9/Check%20Result.png)
    *Mô tả chi tiết: Bằng chứng cụ thể cho thấy hệ thống tự động hóa hoạt động hoàn hảo. Hình ảnh chụp lại màn hình ứng dụng Slack với các tin nhắn cảnh báo (alerts) tự động được gửi từ AWS. Người quản trị có thể ngay lập tức biết được trạng thái của các máy ảo (đã tắt hay vừa bật lên) mà không cần phải đăng nhập vào AWS Console, thực hiện đúng triết lý ChatOps.*

13. **Kích hoạt AWS Security Hub CSPM (Enable AWS Security Hub CSPM)**
    ![Enable AWS Security Hub CSPM](../images/1-Worklog/Worklog_week1.9/Enable%20AWS%20Security%20Hub%20CSPM.png)
    *Mô tả chi tiết: Tổng quan bảng điều khiển (Dashboard) của AWS Security Hub. Tính năng Cloud Security Posture Management (CSPM) đã được bật, tiến hành quét toàn bộ tài khoản dựa trên các tiêu chuẩn bảo mật chuẩn ngành (như AWS Foundational Security Best Practices). Giao diện hiển thị biểu đồ điểm số tuân thủ (Compliance Score) và liệt kê các lỗ hổng hoặc cấu hình sai cần khắc phục.*

14. **Dọn dẹp Security Hub (Clean Security Hub)**
    ![Clean Security Hub](../images/1-Worklog/Worklog_week1.9/Clean%20Security%20Hub.png)
    *Mô tả chi tiết: Hình ảnh minh chứng cho thao tác vô hiệu hóa (Disable) và xóa dữ liệu của AWS Security Hub trong phần Settings. Vì Security Hub tính phí dựa trên số lượng kiểm tra bảo mật (security checks), việc tắt dịch vụ này sau khi hoàn thành bài thực hành là rất cần thiết để đảm bảo không bị trừ tiền ngoài ý muốn trong tương lai.*

15. **Dọn dẹp Tags (Clean Tags)**
    ![Clean Tags](../images/1-Worklog/Worklog_week1.9/Clean%20Tags.png)
    *Mô tả chi tiết: Minh họa việc sử dụng Tag Editor để xóa hàng loạt các thẻ (Tags) đã tạo ra trên nhiều tài nguyên. Bước làm sạch này giúp môi trường AWS giữ được sự ngăn nắp, tránh việc các thẻ rác (stale tags) làm rối loạn các công cụ báo cáo chi phí hoặc làm ảnh hưởng tới các bộ quy tắc tự động hóa khác trong hệ thống.*

16. **Dọn dẹp EC2, Lambda và CloudWatch (Clean Ec2 and lamda and cloudwatch)**
    ![Clean Ec2 and lamda and cloudwatch](../images/1-Worklog/Worklog_week1.9/Clean%20Ec2%20and%20lamda%20and%20cloudwatch.png)
    *Mô tả chi tiết: Bước cuối cùng dọn dẹp môi trường (Terminate/Delete resources). Hình ảnh cho thấy lệnh xóa các máy ảo EC2, các hàm Lambda không còn sử dụng, và quan trọng là xóa các nhóm nhật ký (Log Groups) trong CloudWatch. Log Groups nếu để lại lâu ngày có thể phát sinh phí lưu trữ (Storage cost), do đó việc xóa triệt để đảm bảo tối ưu hóa chi phí (Cost Optimization) tối đa.*

---

## Tuần 10:
### Mục tiêu Tuần 10:
- Hiểu và cấu hình VPC Peering để kết nối hai mạng VPC riêng biệt, cấu hình định tuyến (routing) và kiểm tra phân giải DNS chéo (Cross-Peer DNS resolution).
- Thiết lập và kiểm chứng Network Access Control Lists (NACLs) để kiểm soát bảo mật không trạng thái (stateless firewall) ở mức subnet trong VPC.
- Tìm hiểu và triển khai AWS Transit Gateway (TGW) làm bộ định tuyến trung tâm để kết nối nhiều VPC theo mô hình Hub-and-Spoke, đơn giản hóa kiến trúc mạng quy mô lớn.

### Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học các khái niệm VPC Peering và Network Access Control Lists (NACLs)<br>- **Lab 19 (Phần 1)**: Thiết lập môi trường mạng cơ sở sử dụng CloudFormation, tạo Security Groups và EC2s | 22/06/2026 | 22/06/2026 | [VPC Peering Guide](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html)<br>[Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) |
| 3 | - **Lab 19 (Phần 2)**: Cấu hình Custom VPC Peering, tạo kết nối VPC Peering, cập nhật route tables và xác minh Cross-Peer DNS resolution | 23/06/2026 | 23/06/2026 | [VPC Peering DNS Support](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) |
| 4 | - **Lab 19 (Phần 3)**: Cấu hình Network ACLs (NACLs) ở mức subnet để chặn/cho phép lưu lượng ICMP/SSH, kiểm tra tính chất không trạng thái (stateless) và so sánh với Security Groups | 24/06/2026 | 24/06/2026 | [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) |
| 5 | - Học các khái niệm AWS Transit Gateway (TGW) và mô hình Hub-and-Spoke<br>- **Lab 20 (Phần 1)**: Thiết lập 3 VPC để minh họa sử dụng CloudFormation | 25/06/2026 | 25/06/2026 | [AWS Transit Gateway Guide](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) |
| 6 | - **Lab 20 (Phần 2)**: Tạo Transit Gateway và cấu hình gắn kết (attachments) cho các VPC | 26/06/2026 | 26/06/2026 | [Transit Gateway Attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html) |
| 7 - Chủ nhật | - **Lab 20 (Phần 3)**: Thiết lập Transit Gateway Route Tables, thêm Routes vào TGW Route Tables và xác minh kết nối mạng cross-VPC<br>- Tiến hành dọn dẹp sạch sẽ tài nguyên để tránh phát sinh chi phí | [27/06/2026](./Worklog_week1.10/) | [28/06/2026](./Worklog_week1.10/) | [TGW Route Tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html) |

### Thành tựu Tuần 10:
- **VPC Peering & Bảo mật**: Đã thiết lập thành công kết nối mạng riêng giữa hai VPC cô lập; áp dụng Network ACLs để kiểm soát các gói tin vào/ra và hiểu rõ hơn về hoạt động không giữ trạng thái (stateless) của NACL so với Security Groups giữ trạng thái (stateful).
- **Triển khai Transit Gateway**: Đã xây dựng mạng Hub-and-Spoke trung tâm kết nối 3 VPC bằng AWS Transit Gateway, loại bỏ nhu cầu cấu hình peering dạng full-mesh phức tạp, giúp quản trị và mở rộng hạ tầng mạng quy mô lớn dễ dàng hơn.
- **Tối ưu hóa chi phí**: Thực hiện dọn dẹp triệt để toàn bộ các tài nguyên (TGW, EC2, CloudFormation stacks) sau khi hoàn tất các bài lab để tránh phát sinh chi phí không mong muốn.

### Hình ảnh minh chứng:

1. **Khởi tạo ngăn xếp CloudFormation cho VPC Peering (Create_Stack)**
   ![Khởi tạo Stack](../../images/1-Worklog/Worklog_week1.10/Create_Stack.png)
   *Mô tả chi tiết: Hình ảnh này ghi lại quá trình khởi tạo và triển khai thành công ngăn xếp (stack) AWS CloudFormation nhằm tự động hóa việc xây dựng môi trường mạng cơ sở cho bài thực hành VPC Peering. Việc sử dụng Cơ sở hạ tầng dưới dạng mã (IaC) giúp đảm bảo toàn bộ VPC, subnet, bảng định tuyến và máy chủ được tạo ra một cách đồng nhất và chính xác. Stack này tạo ra nền tảng mạng ban đầu gồm 'My VPC' và 'HG VPC', giúp tiết kiệm thời gian thiết lập thủ công và giảm thiểu sai sót.*

2. **Cấu hình Security Group cho My VPC (Create_MY VPC SG)**
   ![Cấu hình Security Group My VPC](../../images/1-Worklog/Worklog_week1.10/Create_MY%20VPC%20SG.png)
   *Mô tả chi tiết: Cung cấp góc nhìn chi tiết về các quy tắc Security Group được áp dụng cho 'My VPC'. Security Group đóng vai trò là tường lửa ảo có trạng thái (stateful) bảo vệ ở cấp độ instance. Trong thiết lập này, các quy tắc inbound được tinh chỉnh cẩn thận để chỉ cho phép lưu lượng SSH (cổng 22) và ICMP (ping) từ các địa chỉ IP đáng tin cậy hoặc cụ thể là từ dải CIDR của VPC được kết nối (peered VPC). Điều này thể hiện nguyên tắc đặc quyền tối thiểu, đảm bảo an toàn tối đa cho máy chủ.*

3. **Cấu hình Security Group cho HG VPC (Create_HG VPC SG)**
   ![Cấu hình Security Group HG VPC](../../images/1-Worklog/Worklog_week1.10/Create_HG%20VPC%20SG.png)
   *Mô tả chi tiết: Thể hiện cấu hình Security Group tương ứng cho các máy chủ đặt tại 'HG VPC' (mạng được kết nối). Tương tự như 'My VPC', tường lửa này được thiết lập để tiếp nhận lưu lượng truy cập đi vào một cách nghiêm ngặt, chỉ cho phép xuất phát từ dải mạng của 'My VPC'. Việc cấu hình các quy tắc đối xứng giữa hai VPC tạo ra một kênh giao tiếp hai chiều an toàn, là điều kiện tiên quyết để thực hiện các bài kiểm tra kết nối mạng (như lệnh ping) sau khi thiết lập peering.*

4. **Triển khai máy chủ EC2 (Create EC2)**
   ![Khởi tạo máy chủ EC2](../../images/1-Worklog/Worklog_week1.10/Create%20EC2.png)
   *Mô tả chi tiết: Minh họa trạng thái hoạt động ổn định của các máy chủ ảo EC2 đã được khởi tạo thành công trên các VPC khác nhau (một máy chủ thuộc 'My VPC' và một thuộc 'HG VPC'). Những máy chủ này đóng vai trò là các điểm đầu cuối (endpoint) để tiến hành kiểm thử kết nối mạng. Việc xác nhận máy chủ đang chạy và được cấp phát đúng địa chỉ IP private trong subnet là bước chuẩn bị quan trọng nhất trước khi kiểm tra tính hợp lệ của đường truyền.*

5. **Thiết lập kết nối VPC Peering (MyVPC peering to HG VPC)**
   ![Kết nối VPC Peering](../../images/1-Worklog/Worklog_week1.10/MyVPC%20peering%20to%20HG%20VPC.png)
   *Mô tả chi tiết: Làm nổi bật mục tiêu cốt lõi của bài lab — kết nối VPC Peering đang trong trạng thái hoạt động (Active) liên kết 'My VPC' với 'HG VPC'. VPC Peering cho phép định tuyến lưu lượng giữa hai mạng thông qua địa chỉ IP private IPv4 hoặc IPv6. Hình ảnh xác nhận yêu cầu kết nối đã được chấp thuận, qua đó hợp nhất ảo hai phân đoạn mạng tách biệt thành một không gian mạng riêng tư liên tục mà không cần dữ liệu phải đi qua môi trường internet công cộng.*

6. **Cập nhật bảng định tuyến cho Peering (route_table)**
   ![Cập nhật Route Table](../../images/1-Worklog/Worklog_week1.10/route_table.png)
   *Mô tả chi tiết: Hiển thị những sửa đổi mang tính quyết định trên các bảng định tuyến (Route Tables) của VPC. Để máy chủ ở hai VPC có thể giao tiếp với nhau, bảng định tuyến của các subnet liên quan bắt buộc phải được cập nhật. Ảnh chụp màn hình cho thấy việc thêm một route cụ thể, trong đó đích đến (Destination) là dải CIDR của VPC đối diện, và mục tiêu (Target) là ID của kết nối VPC Peering (bắt đầu bằng pcx-...). Nếu thiếu bước này, gói tin sẽ bị rớt.*

7. **Kiểm chứng Network Access Control List - NACL (ALI)**
   ![Cấu hình NACL](../../images/1-Worklog/Worklog_week1.10/ALI.png)
   *Mô tả chi tiết: Trình bày quá trình cấu hình và kiểm thử Network ACLs (NACLs). Khác với Security Group, NACL là tường lửa không trạng thái (stateless) hoạt động ở cấp độ subnet, yêu cầu phải định nghĩa rõ ràng cả quy tắc inbound và outbound. Hình ảnh minh chứng việc thay đổi một quy tắc NACL để chặn hoặc cho phép lưu lượng cụ thể (như ICMP hay SSH) sẽ ngay lập tức tác động đến toàn bộ subnet, cung cấp một lớp phòng thủ an ninh mạng bao quát và mạnh mẽ hơn.*

8. **Khởi tạo CloudFormation Template (Initialize CloudFormation Template)**
   ![Khởi tạo CloudFormation Template](../../images/1-Worklog/Worklog_week1.10/Initialize%20CloudFormation%20Template.png)
   *Mô tả chi tiết: Hình ảnh này thể hiện bước đầu tiên trong việc thiết lập môi trường bằng cách sử dụng AWS CloudFormation. Việc chạy template sẽ tự động hóa quá trình tạo ra các VPC, Subnet, Route Table và các tài nguyên mạng cơ bản cần thiết cho bài thực hành Transit Gateway. Đây là phương pháp hiệu quả để xây dựng hạ tầng nhanh chóng và đồng nhất thay vì phải tạo từng tài nguyên thủ công qua console.*

9. **Tạo Key Pair bảo mật (Create_key_pair)**
   ![Tạo Key Pair](../../images/1-Worklog/Worklog_week1.10/Create_key_pair.png)
   *Mô tả chi tiết: Quá trình tạo mới Amazon EC2 Key Pair được hiển thị trong ảnh này. Key Pair đóng vai trò xác thực quan trọng, cho phép quản trị viên truy cập an toàn (SSH) vào các máy chủ EC2 sẽ được khởi tạo trong các mạng VPC. Việc quản lý khóa bảo mật cẩn thận là nguyên tắc cơ bản trong bảo mật đám mây.*

10. **Tạo AWS Transit Gateway (Create Transit gateways)**
   ![Tạo Transit Gateway](../../images/1-Worklog/Worklog_week1.10/Create%20Transit%20gateways.png)
   *Mô tả chi tiết: Hình ảnh ghi nhận việc khởi tạo thành công tài nguyên AWS Transit Gateway (TGW). TGW đóng vai trò là một hub trung tâm để kết nối nhiều mạng VPC và hệ thống mạng on-premises, giúp thay thế kiến trúc kết nối VPC Peering dạng lưới (full-mesh) phức tạp bằng mô hình hub-and-spoke đơn giản, dễ mở rộng và dễ quản lý tập trung.*

11. **Gắn kết VPC vào Transit Gateway (Create Transit gateway attachments)**
   ![Gắn kết Transit Gateway](../../images/1-Worklog/Worklog_week1.10/Create%20Transit%20gateway%20attachments.png)
   *Mô tả chi tiết: Bước tiếp theo sau khi tạo TGW là gắn kết (attach) các mạng VPC cụ thể vào hub trung tâm này. Ảnh chụp màn hình minh họa quá trình tạo TGW Attachments, qua đó các VPC được liên kết vào Transit Gateway. Điều này cho phép lưu lượng mạng từ các subnet bên trong VPC có thể được định tuyến tới TGW để đi tới các mạng đích khác.*

12. **Cấu hình bảng định tuyến cho Transit Gateway (Create Transit gateway route tables)**
   ![Cấu hình Route Tables cho TGW](../../images/1-Worklog/Worklog_week1.10/Create%20Transit%20gateway%20route%20tables.png)
   *Mô tả chi tiết: Hình ảnh này hiển thị việc tạo và cấu hình Transit Gateway Route Tables. Khác với Route Table của VPC, TGW Route Table kiểm soát cách thức gói tin được định tuyến sau khi đến Transit Gateway. Bằng cách sử dụng nhiều route table, người quản trị có thể thiết lập các chính sách định tuyến phức tạp (ví dụ: cách ly các VPC, hoặc cho phép một số VPC giao tiếp với nhau).*

13. **Cập nhật quy tắc định tuyến TGW (Create Transit gateway route tables 1)**
   ![Cập nhật Route Tables cho TGW](../../images/1-Worklog/Worklog_week1.10/Create%20Transit%20gateway%20route%20tables%201.png)
   *Mô tả chi tiết: Chi tiết quá trình cập nhật các bản ghi định tuyến (routes) bên trong TGW Route Table. Việc khai báo đích đến (destination CIDR) và đính kèm (attachment target) tương ứng đảm bảo các gói tin biết chính xác đường đi để tới được VPC đích. Đây là bước quyết định để thiết lập khả năng giao tiếp xuyên mạng (cross-VPC).*

14. **Kiểm tra kết quả định tuyến mạng qua TGW (Transit Gateway Route result & result 1)**
   ![Kết quả định tuyến TGW](../../images/1-Worklog/Worklog_week1.10/Transit%20Gateway%20Route%20result.png)
   ![Kết quả kết nối TGW](../../images/1-Worklog/Worklog_week1.10/Transit%20Gateway%20Route%20result%201.png)
   *Mô tả chi tiết: Các hình ảnh này là bằng chứng xác nhận việc định tuyến thông qua Transit Gateway đã hoạt động chính xác. Kết quả ping hoặc trace route từ máy chủ ở VPC này tới máy chủ ở VPC khác thành công chứng minh rằng mạng lưới hub-and-spoke đã được thông suốt. Toàn bộ kiến trúc mạng từ Route Table của subnet tới Route Table của TGW đều đã được cấu hình đồng bộ.*

15. **Dọn dẹp tài nguyên để tối ưu chi phí (Clean)**
   ![Clean 1](../../images/1-Worklog/Worklog_week1.10/clean%201.png)
   ![Clean 2](../../images/1-Worklog/Worklog_week1.10/clean%202.png)
   ![Clean](../../images/1-Worklog/Worklog_week1.10/Clean.png)
   *Mô tả chi tiết: Chuỗi hình ảnh cuối cùng này ghi nhận quá trình "dọn dẹp" (tear down) các tài nguyên thực hành bao gồm xóa Transit Gateway Attachments, xóa Transit Gateway, terminate EC2 instances và xóa CloudFormation stacks. Việc chủ động xóa các tài nguyên sau khi hoàn thành bài lab là thực hành cực kỳ quan trọng trên AWS để ngăn chặn các khoản phí phát sinh không mong muốn (cost optimization).*

---

## Tuần 11:
### Mục tiêu Tuần 11:
- Tìm hiểu các khái niệm về dịch vụ AWS Storage Gateway và mô hình lưu trữ lai (Hybrid Cloud Storage).
- Thực hành triển khai và cấu hình AWS File Storage Gateway để kết nối hạ tầng lưu trữ tại chỗ (On-premises) với dịch vụ lưu trữ đám mây Amazon S3.
- Thực hành kết nối (mount) File Share (NFS/SMB) từ Storage Gateway lên hệ điều hành Linux (giả lập máy chủ On-premises).

### Công việc cần thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học lý thuyết về AWS Storage Gateway, phân loại các dòng Gateway và mô hình Hybrid Cloud Storage | 29/06/2026 | 29/06/2026 | [AWS Storage Gateway Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/WhatIsStorageGateway.html) |
| 3 | - **Thực hành (Phần 1)**: Khởi tạo S3 bucket trên AWS để đóng vai trò làm backend storage cho Storage Gateway | 30/06/2026 | 30/06/2026 | [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/) |
| 4 | - **Thực hành (Phần 2)**: Khởi chạy một EC2 instance chạy Linux để giả lập môi trường máy chủ nội bộ (On-premises machine) | 01/07/2026 | 01/07/2026 | [Amazon EC2 User Guide](https://docs.aws.amazon.com/ec2/) |
| 5 | - **Thực hành (Phần 3)**: Tạo và cấu hình AWS File Storage Gateway thông qua giao diện quản trị AWS Console | 02/07/2026 | 02/07/2026 | [Creating a File Gateway](https://docs.aws.amazon.com/storagegateway/latest/userguide/CreatingAnAppliance.html) |
| 6 | - **Thực hành (Phần 4)**: Tạo File Share trên Storage Gateway và liên kết trực tiếp với S3 bucket đã chuẩn bị ở bước trước | 03/07/2026 | 03/07/2026 | [Creating a File Share](https://docs.aws.amazon.com/storagegateway/latest/userguide/CreatingAFileShare.html) |
| 7 - Chủ nhật | - **Thực hành (Phần 5)**: Thực hiện kết nối (mount) File Share NFS lên máy chủ EC2 giả lập, kiểm tra đồng bộ ghi dữ liệu chéo lên S3<br>- Tiến hành dọn dẹp sạch sẽ tài nguyên để tránh phát sinh chi phí | [04/07/2026](./Worklog_week1.11/) | [05/07/2026](./Worklog_week1.11/) | [Mounting a File Share](https://docs.aws.amazon.com/storagegateway/latest/userguide/mounting-file-share.html) |

### Thành tựu Tuần 11:
- **Cấu hình AWS Storage Gateway**: Hiểu rõ nguyên lý hoạt động của kiến trúc lưu trữ lai (Hybrid Cloud Storage) và cấu hình thành công AWS File Storage Gateway để kết nối bộ nhớ on-premises với AWS S3 thông qua các giao thức chia sẻ tệp tiêu chuẩn.
- **Tích hợp hạ tầng lai**: Thực hành thành công quy trình mount File Share NFS và xác minh khả năng đồng bộ hóa tệp dữ liệu tự động giữa môi trường tại chỗ và cloud.
- **Tối ưu hóa chi phí**: Chủ động dọn dẹp hoàn toàn các tài nguyên thực hành (Storage Gateway, File Share, S3 Bucket, EC2 Instance) để tránh phát sinh chi phí duy trì dịch vụ Storage Gateway.

### Hình ảnh minh chứng:

1. **Khởi tạo S3 Bucket (Create s3 bucket)**
   ![Create s3 bucket](../images/1-Worklog/Worklog_week1.11/Create%20s3%20bucket.png)
   *Mô tả chi tiết: Quá trình tạo Amazon S3 Bucket để làm nơi lưu trữ dữ liệu cho Storage Gateway. S3 cung cấp kho lưu trữ đối tượng an toàn, bền bỉ và có khả năng mở rộng, đóng vai trò là điểm đến (backend storage) cho các file được chia sẻ qua File Gateway.*

2. **Khởi chạy EC2 (Create EC2)**
   ![Create EC2](../images/1-Worklog/Worklog_week1.11/Create%20EC2.png)
   *Mô tả chi tiết: Triển khai một máy ảo (EC2 instance) đóng vai trò như một máy chủ on-premises mô phỏng. Máy ảo này sẽ được cấu hình để mount (kết nối) vào File Share mà Storage Gateway cung cấp, nhằm kiểm tra khả năng lưu trữ file lên S3 từ môi trường mạng nội bộ.*

3. **Tạo Storage Gateway (Create Storage GateWay)**
   ![Create Storage GateWay](../images/1-Worklog/Worklog_week1.11/Create%20Storage%20GateWay.png)
   *Mô tả chi tiết: Giao diện cấu hình và khởi tạo AWS File Storage Gateway. Storage Gateway đóng vai trò làm cầu nối (bridge) giữa ứng dụng on-premises và hệ sinh thái lưu trữ đám mây của AWS. Nó cung cấp giao thức SMB/NFS tiêu chuẩn để các ứng dụng cũ có thể dễ dàng lưu file lên S3 mà không cần thay đổi kiến trúc.*

4. **Tạo File Share (Create File Share)**
   ![Create File Share](../images/1-Worklog/Worklog_week1.11/Create%20File%20Share.png)
   *Mô tả chi tiết: Quá trình thiết lập một File Share trên Storage Gateway vừa tạo. File share này được liên kết trực tiếp với S3 bucket. Bất kỳ file nào được ghi vào file share này thông qua NFS/SMB sẽ được Gateway tự động đẩy lên S3 dưới dạng các object.*

5. **Kết nối File Share vào máy On-premises (Mount File shares on On-premises machine)**
   ![Mount File shares on On-premises machine](../images/1-Worklog/Worklog_week1.11/Mount%20File%20shares%20on%20On-premises%20machine.png)
   *Mô tả chi tiết: Thực hiện lệnh mount thư mục được chia sẻ từ Storage Gateway lên máy ảo EC2 (mô phỏng máy chủ on-premises). Hình ảnh cho thấy việc kết nối thành công, cho phép người dùng hoặc ứng dụng có thể đọc/ghi dữ liệu vào S3 thông qua một thư mục mạng cục bộ một cách hoàn toàn trong suốt.*

6. **Dọn dẹp tài nguyên (Clean)**
   ![Clean](../images/1-Worklog/Worklog_week1.11/Clean.png)
   *Mô tả chi tiết: Thao tác xóa bỏ các tài nguyên đã tạo (Storage Gateway, File Share, S3 Bucket, EC2 Instance) sau khi hoàn thành bài thực hành. Đây là nguyên tắc quan trọng nhằm tối ưu hóa chi phí (Cost Optimization) và đảm bảo không có tài nguyên dư thừa bị bỏ quên.*

---

## Tuần 12:
### Mục tiêu Tuần 12:
- **Tổng kết & Đánh giá:** Tổng hợp, đánh giá và kiểm tra lại toàn bộ quá trình nghiên cứu và thực hành trong suốt chặng đường 12 tuần của chương trình First Cloud Journey.
- **Quản trị hệ thống từ xa:** Sử dụng bộ công cụ AWS Systems Manager (SSM) bao gồm Fleet Manager, Patch Manager và Run Command để quản lý và vận hành hệ thống máy chủ Windows Server.
- **Kiểm soát truy cập nâng cao:** Cấu hình IAM Tag-based Access Control cho EC2 và thiết lập IAM Permissions Boundaries để giới hạn quyền truy cập tối đa của IAM Entities.
- **Giám sát nâng cao:** Tìm hiểu công cụ giám sát mã nguồn mở Grafana để xây dựng dashboard theo dõi tài nguyên trực quan.
- **Xác minh chuyên cần:** Đối soát và hoàn thiện lịch sử chấm công chuyên cần của toàn bộ khóa học 12 tuần.

### Công việc cần thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học IAM Tag-based Access Control<br>- Đọc hướng dẫn và cấu hình IAM Tags để kiểm soát truy cập vào tài nguyên EC2 | 06/07/2026 | 06/07/2026 | <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html" target="_blank">AWS IAM Tagging</a> |
| 3 | - Học cơ bản về giám sát Grafana<br>- Đọc và hiểu các khái niệm Grafana và tạo Dashboard cơ bản | 07/07/2026 | 07/07/2026 | <a href="https://grafana.com/docs/grafana/latest/" target="_blank">Grafana User Guide</a> |
| 4 | - Học IAM Permission Boundary<br>- Cấu hình permission boundaries để giới hạn quyền tối đa của IAM Entities | 08/07/2026 | 08/07/2026 | <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html" target="_blank">AWS Permissions Boundaries</a> |
| 5 | - Học các khái niệm AWS Systems Manager (SSM)<br>- Đọc giới thiệu về SSM, Fleet Manager, Patch Manager và Run Command | 09/07/2026 | 09/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html" target="_blank">AWS Systems Manager User Guide</a> |
| 6 | - Thiết lập cơ sở hạ tầng mạng và IAM Roles cho SSM<br>- Tạo VPC `windows-lab-ssm`, Internet Gateway, 2 Subnets<br>- Tạo IAM Role/Instance Profile với chính sách `AmazonSSMManagedInstanceCore`<br>- Khởi chạy 2 máy ảo EC2 Windows Server gắn với IAM Role | 10/07/2026 | 10/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html" target="_blank">SSM Agent on Windows Server</a> |
| 7 - Chủ nhật | - Thực hiện cập nhật patch và chạy lệnh từ xa qua SSM<br>- Sử dụng Patch Manager để quét lỗ hổng và cài đặt cập nhật OS tự động<br>- Sử dụng Run Command để chạy PowerShell `net user` từ xa và lưu log vào S3<br>- Tổng kết toàn bộ lộ trình học tập 12 tuần và thực hiện dọn dẹp sạch tài nguyên | [11/07/2026](./Worklog_week1.12/) | [12/07/2026](./Worklog_week1.12/) | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html" target="_blank">SSM Patch Manager</a><br><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html" target="_blank">SSM Run Command</a> |

### Thành tựu Tuần 12:

#### 1. Tổng hợp lộ trình nghiên cứu và thực hành của 12 tuần:
Trải qua 12 tuần của chương trình **First Cloud Journey**, lộ trình tích lũy kiến thức đã được hoàn thành xuất sắc với các cột mốc quan trọng:
* **Tuần 1 - 2 (Làm quen & Kiểm soát chi phí):** Làm quen hệ thống AWS, nghiên cứu lý thuyết S3/EC2 và thiết lập chốt chặn tài chính an toàn bằng **AWS Budgets**.
* **Tuần 3 - 4 (Hạ tầng & Cơ sở dữ liệu):** Triển khai máy chủ ảo EC2 (Public/Private Subnets), phân quyền chi tiết IAM và kết nối ứng dụng Node.js đến cơ sở dữ liệu **Amazon RDS** (cấu hình Multi-AZ, Backups và Snapshots).
* **Tuần 5 - 6 (Tính sẵn sàng cao & Giám sát):** Cấu hình hạ tầng quy mô với **Auto Scaling Groups**, **Load Balancers**, tối ưu phân phối qua **CloudFront** và **Route 53**. Đồng thời xây dựng hệ thống cảnh báo qua **Amazon CloudWatch** (Metrics, Alarms, Logs Insights).
* **Tuần 7 - 8 (Tự động hóa & Kiểm toán bảo mật):** Tự động hóa hạ tầng qua **AWS CLI**, cấu hình **AWS Backup** lập lịch sao lưu tự động. Nâng cao bảo mật dữ liệu với **AWS S3 SSE-KMS**, kiểm toán hoạt động qua **AWS CloudTrail** và phân tích logs bằng **Amazon Athena**.
* **Tuần 9 - 11 (Vận hành Serverless & Mạng doanh nghiệp):** Tự động hóa bật/tắt EC2 bằng **AWS Lambda** & **EventBridge** tích hợp thông báo về Slack (ChatOps). Thiết lập mạng kết nối đa VPC qua **VPC Peering**, **Transit Gateway** và kết nối hybrid on-premises qua **AWS Storage Gateway (NFS)**.
* **Tuần 12 (Hạ tầng quản trị tập trung & Kết thúc):** Quản trị an toàn thông qua **IAM Permissions Boundaries** và **Tag-based Access Control**. Sử dụng **AWS Systems Manager (SSM)** để quản lý, vá lỗi bảo mật (Patch Manager) và chạy lệnh (Run Command) từ xa trên máy chủ mà không cần mở cổng SSH/RDP truyền thống.

#### 2. Kết quả thực hiện trong Tuần 12:
* Tuần 12 tập trung hoàn toàn vào nghiên cứu tài liệu, tổng kết lý thuyết hệ thống và tổng hợp báo cáo. Không thực hiện thao tác khởi tạo hay thay đổi cấu hình tài nguyên trực tiếp trên cloud.
* Hoàn thiện đối soát lịch sử chuyên cần và check-in thực tế của toàn bộ khóa học.

### Hình ảnh minh chứng tổng kết chuyên cần:

1. **Lịch sử chuyên cần khóa học - Phần 1 (Attendance History 1)**
   ![Lịch sử chuyên cần 1](/images/1-Worklog/Worklog_week1.12/Attendance%20history%201.png)
   *Mô tả chi tiết: Hình ảnh ghi lại nhật ký chuyên cần của giai đoạn đầu khóa học trên cổng thông tin đào tạo, xác minh sự tham gia học tập lý thuyết, sync nhóm và hoàn thành đầy đủ nhiệm vụ theo lịch trình đề ra.*

2. **Lịch sử chuyên cần khóa học - Phần 2 (Attendance History 2)**
   ![Lịch sử chuyên cần 2](/images/1-Worklog/Worklog_week1.12/Attendance%20history%202.png)
   *Mô tả chi tiết: Minh chứng tiếp tục quá trình ghi nhận chuyên cần giai đoạn tiếp theo, phản ánh tính kỷ luật cao và nỗ lực học tập không ngừng của học viên trong suốt quá trình đào tạo.*

3. **Lịch sử chuyên cần tổng thể toàn khóa (Attendance History)**
   ![Lịch sử chuyên cần tổng thể](/images/1-Worklog/Worklog_week1.12/Attendance%20history.png)
   *Mô tả chi tiết: Bảng thống kê tổng hợp lịch sử chuyên cần cuối kỳ của học viên, ghi nhận việc hoàn thành 100% thời lượng đào tạo và tham gia đầy đủ các buổi thảo luận, hướng dẫn trực tiếp.*

4. **Hình ảnh check-in thực tế tại văn phòng đào tạo (Attendance history picture checkin)**
   ![Checkin thực tế](/images/1-Worklog/Worklog_week1.12/Attendance%20history%20picture%20checkin.png)
   *Mô tả chi tiết: Ảnh chụp check-in trực tiếp của học viên trong buổi học tập và làm việc nhóm tại văn phòng thực tập, minh chứng cho việc thực hiện đúng giờ giấc làm việc thực tế, giao lưu và phối hợp chặt chẽ cùng các thành viên trong đội ngũ First Cloud Journey.*
