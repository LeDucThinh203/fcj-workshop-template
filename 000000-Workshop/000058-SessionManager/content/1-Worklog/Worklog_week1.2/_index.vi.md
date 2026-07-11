---
title: "Nhật ký Tuần 2"
date: 2026-05-13
weight: 2
chapter: false
pre: " <b> 1.2 </b> "
---

## Mục tiêu Tuần 2:
- Hiểu mạng cơ bản trong AWS (VPC)
- Thành thạo cách cấu hình các thành phần mạng và bảo mật trong VPC
- Thực hành xây dựng một VPC hoàn chỉnh

## Công việc cần thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học cơ bản VPC:<br>  + Tổng quan VPC<br>  + CIDR Block<br>  + Phân biệt Subnet Công cộng / Riêng | 27/04/2026 | 27/04/2026 | [VPC Basics](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) |
| 3 | - Học về Subnet & Route Tables:<br>  + Cách chia Subnet<br>  + Cấu hình Route Tables | 28/04/2026 | 28/04/2026 | [Subnets & Route Tables](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html) |
| 4 | - Học về Internet Gateway & NAT Gateway:<br>  + Internet Gateway cho Subnet Công cộng<br>  + NAT Gateway cho Subnet Riêng | 29/04/2026 | 29/04/2026 | [NAT Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) |
| 5 | - Học về bảo mật trong VPC:<br>  + Security Groups<br>  + Network ACLs<br>  + Quy tắc Inbound / Outbound | 30/04/2026 | 30/04/2026 | [VPC Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) |
| 6 | - **Thực hành:**<br>  + Tạo VPC<br>  + Tạo Subnet Công cộng & Riêng<br>  + Cấu hình Route Tables | 01/05/2026 | 01/05/2026 | [FCJ Lab - Create VPC](https://cloudjourney.awsstudygroup.com/2-prerequisites/2.1-createvpc/) |
| 7 - Chủ nhật | - **Thực hành nâng cao:**<br>  + Gắn Internet Gateway<br>  + Tạo NAT Gateway<br>  + Triển khai EC2 trong Subnet Riêng/Công cộng<br>  + Xác minh kết nối internet | 02/05/2026 | 03/05/2026 | [FCJ Lab - Public/Private](https://cloudjourney.awsstudygroup.com/2-prerequisites/2.2-publicprivateinstance/) |

## Thành tựu Tuần 2:
### Lý thuyết:
- Có thể hiểu kiến trúc của Amazon VPC và cách quản lý dải địa chỉ IP qua CIDR
- Biết cách tạo và cấu hình route tables

### Thực hành:
- Đã thực hiện cấu hình VPC hoàn chỉnh bao gồm các Subnet công cộng và riêng tư.
- Thiết lập thành công Internet Gateway và NAT Gateway để định tuyến lưu lượng mạng.
- Triển khai EC2 Instance và cấu hình bảo mật thông qua Security Groups/Network ACLs.

### Hình ảnh minh chứng:

1. **Lịch sử chuyên cần (Attendance History - Tuần 2)**
   ![Lịch sử chuyên cần](/images/1-Worklog/Worklog_week1.2/attendance_history_2.png)
   *Mô tả chi tiết: Hình ảnh ghi nhận lịch sử chấm công và tham gia đầy đủ các buổi học tập, thảo luận nhóm trong Tuần 2. Đây là bằng chứng xác thực cho việc tuân thủ giờ giấc làm việc, tinh thần tự giác và hoàn thành đầy đủ thời lượng đào tạo theo yêu cầu của chương trình First Cloud Journey.*

2. **Cấu hình sơ đồ mạng Lab07 - Bước 1: Khởi tạo VPC & Thiết lập thông số cơ bản**
   ![Cấu hình Lab07 - Bước 1](/images/1-Worklog/Worklog_week1.2/Module%2001-Lab07-01.png)
   *Mô tả chi tiết: Minh chứng cho bước đầu tiên trong chuỗi thực hành Lab07 - tạo dựng môi trường mạng ảo Amazon VPC (Virtual Private Cloud). Hình ảnh hiển thị quá trình định nghĩa dải IPv4 CIDR Block chính cho hệ thống mạng nội bộ, kích hoạt các tính năng phân giải tên miền quan trọng như DNS Resolution và DNS Hostnames, tạo nền tảng vững chắc để xây dựng các phân khu mạng con (Subnets) ở các bước tiếp theo.*

3. **Cấu hình sơ đồ mạng Lab07 - Bước 2: Tạo Subnets & Thiết lập Route Tables**
   ![Cấu hình Lab07 - Bước 2](/images/1-Worklog/Worklog_week1.2/Module%2001-Lab07-02.png)
   *Mô tả chi tiết: Minh chứng quá trình phân chia dải mạng lớn thành các Subnets độc lập bao gồm Public Subnets (mạng công cộng) và Private Subnets (mạng riêng tư) trên các Availability Zones (Vùng khả dụng) khác nhau để đảm bảo tính sẵn sàng cao. Đồng thời, cấu hình bảng định tuyến (Route Tables), liên kết chính xác từng subnet với bảng định tuyến tương ứng nhằm kiểm soát và phân luồng dữ liệu truy cập một cách bảo mật.*

4. **Cấu hình sơ đồ mạng Lab07 - Bước 3: Thiết lập Gateways & Kiểm tra kết nối Internet**
   ![Cấu hình Lab07 - Bước 3](/images/1-Worklog/Worklog_week1.2/Module%2001-Lab07-03.png)
   *Mô tả chi tiết: Hình ảnh ghi nhận bước hoàn thiện sơ đồ mạng bằng cách cấu hình Internet Gateway (IGW) cho phép lưu lượng truy cập từ ngoài Internet vào Public Subnet, và thiết lập NAT Gateway để hỗ trợ các máy chủ EC2 ở Private Subnet tải cập nhật và kết nối Internet một chiều một cách an toàn. Đây là bước xác minh quan trọng chứng minh toàn bộ hệ thống định tuyến hoạt động ổn định và đúng thiết kế kiến trúc.*
