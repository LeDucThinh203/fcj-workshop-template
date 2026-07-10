---
title: "Worklog Tuần 6"
date: 2026-05-13
weight: 6
chapter: false
pre: " <b> 1.6 </b> "
---

## Mục tiêu Tuần 6:
- Hiểu AWS Cloud Trail và các báo cáo được quản lý tại đây trong AWS Support.
- Triển khai tích hợp Hybrid DNS trên các máy chủ tại chỗ với AWS bằng Route 53 Resolver và Microsoft AD.

## Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học Amazon CloudWatch & chuẩn bị môi trường<br> - CloudWatch Metrics:<br>  + Xem Metrics<br>  + Thực hiện các hoạt động tìm kiếm<br>  + Thực hiện các phép toán toán học<br>  + Tạo dynamic labels | 25/05/2026 | 25/05/2026 | [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)<br> [Using Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) |
| 3 | - CloudWatch Logs:<br>  + Xem CloudWatch Logs<br>  + CloudWatch Logs Insights<br>  + CloudWatch Metric Filter<br>  + Tạo CloudWatch Alarms<br>  + Tạo CloudWatch Dashboards<br>  + Dọn dẹp tài nguyên | 26/05/2026 | 26/05/2026 | [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)<br> [Creating CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html)<br> [CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) |
| 4 | - Học về các AWS Support Plans: Basic, Developer, Business, Enterprise On-Ramp, Enterprise<br> - Truy cập AWS Support Console<br> - Học về các loại Support Request (Account & billing, Technical)<br> - Thay đổi support plan | 27/05/2026 | 27/05/2026 | [AWS Support Plans](https://aws.amazon.com/vi/premiumsupport/plans/)<br> [Getting started with AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html) |
| 5 | - Tạo một Support Request (Support Case)<br> - Chọn mức Severity<br> - Quản lý và theo dõi trạng thái yêu cầu support | 28/05/2026 | 28/05/2026 | [Creating a support case](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) |
| 6 | - Đọc tổng quan bài lab hybrid DNS<br> - Tạo Key Pair<br> - Khởi tạo CloudFormation Template<br> - Cấu hình Security Group<br> - Kết nối với RDGW (Remote Desktop Gateway)<br> - Triển khai Microsoft Active Directory | 29/05/2026 | 29/05/2026 | [What is AWS Directory Service?](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html)<br> [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) |
| 7 - Chủ nhật | - Thiết lập DNS với Route 53:<br>  + Tạo Route 53 Outbound Endpoint<br>  + Tạo Route 53 Resolver Rules<br>  + Tạo Route 53 Inbound Endpoints<br>  + Kiểm tra kết quả<br>  + Dọn dẹp tài nguyên | 30/05/2026 | 31/05/2026 | [Forwarding outbound DNS queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html)<br> [Forwarding inbound DNS queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html) |
