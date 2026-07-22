import sys

path_vi = r'e:\NamHoc_2023-2024\AWS\fcj-workshop-template\000000-Workshop\000058-SessionManager\content\1-Worklog\Worklog_week1.4\_index.vi.md'
path_en = r'e:\NamHoc_2023-2024\AWS\fcj-workshop-template\000000-Workshop\000058-SessionManager\content\1-Worklog\Worklog_week1.4\_index.md'

good_header = """---
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

### Hình ảnh minh chứng:

#### Cấu hình SSH Key Pair bảo mật kết nối (ec2_connection_key)
![Cấu hình SSH Key Pair](/images/1-Worklog/Worklog_week1.4/ec2_connection_key.png)
*Mô tả chi tiết: Hình ảnh thể hiện việc phân quyền truy cập cho tệp khóa bảo mật Private Key (.pem) bằng lệnh `chmod 400` trên môi trường dòng lệnh Linux. Việc hạn chế quyền đọc/ghi cho tệp khóa là yêu cầu bảo mật bắt buộc của giao thức SSH để đảm bảo khóa không bị lộ hoặc bị sử dụng bởi người dùng khác trên cùng hệ thống trước khi bắt đầu phiên kết nối.*

#### Kết nối SSH thành công vào Linux EC2 Public Instance (ec2_connection)
![Kết nối SSH thành công](/images/1-Worklog/Worklog_week1.4/ec2_connection.png)
*Mô tả chi tiết: Ghi lại kết quả thực tế khi kết nối thành công từ máy khách cục bộ vào máy chủ EC2 Public Instance thông qua CLI sử dụng giao thức SSH và Key Pair đã cấu hình. Giao diện dòng lệnh hiển thị shell đăng nhập thành công của Amazon Linux, xác nhận cấu hình định tuyến Internet Gateway và Security Group inbound port 22 hoạt động hoàn hảo.*

#### Định tuyến và kết nối nội bộ vào EC2 Private Instance (ec2_connection_Private)
![Kết nối nội bộ EC2 Private](/images/1-Worklog/Worklog_week1.4/ec2_connection_Private.png)
*Mô tả chi tiết: Minh chứng thực hành kết nối nội bộ thành công vào EC2 Instance trong Private Subnet từ máy chủ EC2 Public (đóng vai trò là Bastion Host). Do Private Instance không thể truy cập trực tiếp từ Internet, việc cấu hình định tuyến bắc cầu này đảm bảo kiểm soát truy cập nghiêm ngặt và quản trị an toàn các máy chủ trong dải mạng nội bộ.*
"""

with open(path_vi, 'r', encoding='utf-8', errors='ignore') as f:
    text_vi = f.read()

idx = text_vi.find('### 4.')
if idx == -1:
    idx = text_vi.find('4. Kh')
if idx == -1:
    print('Could not find start of section 4')
    sys.exit(1)

new_text = good_header + '\n\n' + text_vi[idx:]

with open(path_vi, 'w', encoding='utf-8', newline='') as f:
    f.write(new_text)

print('Fixed _index.vi.md successfully!')
