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

## Thành tựu Tuần 6:
### Lý thuyết:
- Nắm vững kiến trúc Hybrid DNS kết nối hệ thống On-premises (giả lập Microsoft AD trên EC2) và AWS VPC sử dụng Route 53 Resolver (Inbound/Outbound Endpoints).
- Hiểu rõ cơ chế hoạt động của Amazon CloudWatch (Metrics, Logs, Alarms, Dashboards) để giám sát hiệu năng hệ thống.
- Tìm hiểu về AWS Support Plans và cách quản lý Support Cases trực tiếp trên AWS Console.

### Thực hành:
- Deploy thành công kiến trúc mạng Hybrid DNS bằng CloudFormation.
- Cấu hình chuẩn xác các quy tắc Security Groups cho phép luồng lưu lượng DNS (cổng 53 TCP/UDP) lưu thông an toàn giữa On-premises và AWS.
- Thiết lập thành công Inbound và Outbound Resolver Endpoints cùng Resolver Rules để phân giải chính xác tên miền chéo.

### Hình ảnh minh chứng:

1. **Thiết kế và triển khai mô hình Hybrid DNS (HyDrid_DNS)**
   ![Mô hình Hybrid DNS](/images/1-Worklog/Worklog_week1.6/HyDrid_DNS.png)
   *Mô tả chi tiết: Hình ảnh thể hiện sơ đồ kiến trúc và giao diện cấu hình phân giải tên miền chéo Route 53 Resolver (Hybrid DNS). Trong đó mô tả chi tiết việc cấu hình các Route 53 Inbound Endpoint (nhận yêu cầu phân giải từ mạng tại chỗ On-premises gửi lên AWS) và Outbound Endpoint cùng với các Rule tương ứng (chuyển tiếp các truy vấn tên miền nội bộ của doanh nghiệp về DNS Server On-premises). Sự tích hợp này đảm bảo hệ thống mạng lai hoạt động liền mạch, phân giải tên miền ổn định giữa môi trường cloud và local.*

2. **Cấu hình Security Group cho hệ thống DNS (security group configuration)**
   ![Cấu hình Security Group](/images/1-Worklog/Worklog_week1.6/security%20group%20configuration.png)
   *Mô tả chi tiết: Ghi lại giao diện cấu hình chi tiết của Security Group áp dụng cho các Resolver Endpoints và máy chủ Active Directory. Các quy tắc Inbound và Outbound được thiết lập chặt chẽ để chỉ cho phép các gói tin DNS truy cập qua cổng 53 (cả hai giao thức TCP và UDP) từ các dải IP được định nghĩa trước của mạng On-premises và AWS VPC. Cấu hình này giúp ngăn chặn các truy cập trái phép và giảm thiểu tối đa diện tấn công vào hạ tầng phân giải tên miền.*

3. **Triển khai Microsoft Active Directory (Directory Service)**
   ![Triển khai Directory Service](/images/1-Worklog/Worklog_week1.6/Directory_Service.png)
   *Mô tả chi tiết: Hình ảnh hiển thị trạng thái triển khai thành công Microsoft Active Directory thông qua AWS Directory Service. Hệ thống AD này đóng vai trò giả lập thư mục doanh nghiệp tại chỗ (on-premises) và là DNS server chính yếu cho tên miền nội bộ. Đây là thành phần then chốt để xác thực tích hợp Hybrid DNS, nơi các truy vấn DNS từ AWS hướng về tên miền nội bộ sẽ được chuyển tiếp đến.*

4. **Cấu hình Route 53 Inbound Endpoint (Inbound Endpoint)**
   ![Cấu hình Inbound Endpoint](/images/1-Worklog/Worklog_week1.6/Inbound_endpoint.png)
   *Mô tả chi tiết: Minh họa quá trình thiết lập Route 53 Inbound Endpoint. Endpoint này tạo ra các giao diện mạng (ENI) bên trong AWS VPC, được gán địa chỉ IP cụ thể nhằm mục đích lắng nghe và tiếp nhận các truy vấn DNS gửi tới từ mạng On-premises. Thiết lập này đóng vai trò như cổng giao tiếp cho phép các máy chủ bên ngoài phân giải liền mạch các tên miền lưu trữ trên AWS.*

5. **Kiểm tra kết quả phân giải tên miền chéo (Test Result)**
   ![Kết quả kiểm tra](/images/1-Worklog/Worklog_week1.6/Test_result.png)
   *Mô tả chi tiết: Cung cấp kết quả kiểm thử (test result) xác nhận hệ thống Hybrid DNS hoạt động chính xác. Các lệnh kiểm tra như `nslookup` hoặc `dig` cho thấy mạng tại chỗ có thể phân giải thành công tên miền nội bộ của AWS (thông qua Inbound Endpoint) và ngược lại, máy chủ trên AWS cũng truy vấn được tên miền doanh nghiệp (qua Outbound Endpoint). Điều này chứng minh các Resolver Rules và kết nối mạng hai chiều đã được cấu hình chuẩn xác.*

6. **Dọn dẹp tài nguyên - Bước 1**
   ![Dọn dẹp tài nguyên 1](/images/1-Worklog/Worklog_week1.6/clean1.png)
   *Mô tả chi tiết: Hình ảnh ghi nhận quá trình bắt đầu dọn dẹp tài nguyên để tránh phát sinh chi phí AWS không cần thiết. Bước này tập trung vào việc xóa bỏ các Route 53 Resolver Endpoints (Inbound và Outbound) cùng các Rules liên quan đã được tạo phục vụ cho mô hình Hybrid DNS.*

7. **Dọn dẹp tài nguyên - Bước 2**
   ![Dọn dẹp tài nguyên 2](/images/1-Worklog/Worklog_week1.6/clean2.png)
   *Mô tả chi tiết: Minh họa bước dọn dẹp tiếp theo, tiến hành xóa hệ thống AWS Directory Service (giả lập Microsoft AD). Việc loại bỏ dịch vụ thư mục này đảm bảo các máy chủ và tài nguyên hạ tầng nội bộ mô phỏng được thu hồi hoàn toàn.*

8. **Dọn dẹp tài nguyên - Bước cuối**
   ![Dọn dẹp tài nguyên 3](/images/1-Worklog/Worklog_week1.6/clean3.png)
   *Mô tả chi tiết: Chụp lại kết quả hoàn tất quá trình dọn dẹp, xác nhận CloudFormation stack và toàn bộ các tài nguyên đi kèm (như EC2 instances, Network Interfaces, Security Groups) đã được xóa thành công, trả môi trường AWS về trạng thái ban đầu một cách sạch sẽ.*

