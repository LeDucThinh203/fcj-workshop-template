---
title: "Worklog Tuần 4"
date: 2026-05-13
weight: 4
chapter: false
pre: " <b> 1.4 </b> "
---

## Mục tiêu Tuần 4:
- Khởi tạo và cấu hình một Amazon RDS database instance.
- Kết nối ứng dụng chạy trên EC2 đến RDS database.
- Hiểu các cơ chế Backup, Restore và các tính năng nâng cao (Multi-AZ, Read Replicas).

## Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày kết thúc | Nguồn tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Tổng quan về Amazon RDS<br>- So sánh RDS với các dịch vụ lưu trữ khác (EC2 DB, DynamoDB, Redshift) | 11/05/2026 | 11/05/2026 | [Amazon RDS Documentation](https://docs.aws.amazon.com/rds/) |
| 3 | - Cấu hình mạng cho RDS:<br>  + Tạo VPC<br>  + Tạo Security Groups cho EC2 và RDS<br>  + Tạo DB Subnet Group | 12/05/2026 | 12/05/2026 | [VPC for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) |
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
