---
title: "Worklog Tuần 5"
date: 2026-05-13
weight: 5
chapter: false
pre: " <b> 1.5 </b> "
---

## Mục tiêu Tuần 5:
- Hiểu rõ khái niệm và kiến trúc hoạt động của AWS Systems Manager (SSM) Session Manager để quản trị máy chủ từ xa an toàn.
- Nắm vững vai trò của VPC Endpoints (Interface Endpoints) trong việc kết nối riêng tư từ mạng nội bộ tới các dịch vụ AWS mà không qua định tuyến Internet.
- Hiểu cách NAT Gateway dịch chuyển địa chỉ IP và định tuyến lưu lượng đi ra ngoài (outbound-only) cho phân khu mạng Private Subnet.

## Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học lý thuyết về AWS Systems Manager (SSM) Session Manager<br>- Tìm hiểu về VPC Endpoints (Interface Endpoints và Gateway Endpoints)<br>- Tìm hiểu về NAT Gateway và cách hoạt động của nó trong Public Subnet để cung cấp Internet cho Private Subnet | 18/05/2026 | 18/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | - **Thực hành (Phần 1):**<br>  + Tạo VPC với các phân khu mạng Public Subnet và Private Subnet<br>  + Khởi tạo NAT Gateway trong Public Subnet và cấu hình Elastic IP<br>  + Cấu hình bảng định tuyến Route Table cho Private Subnets đi qua NAT Gateway để kết nối ra ngoài Internet một cách an toàn | 19/05/2026 | 19/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - **Thực hành (Phần 2):**<br>  + Khởi tạo EC2 Instance chạy Linux trong Private Subnet (không gán Public IP)<br>  + Tạo và gán IAM Role cho EC2 Instance với các quyền cần thiết để giao tiếp với AWS Systems Manager (`AmazonSSMManagedInstanceCore`)<br>  + Cấu hình Security Group cho EC2 Instance (không mở cổng 22 SSH) | 20/05/2026 | 20/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | - **Thực hành (Phần 3):**<br>  + Tạo các VPC Endpoints (`ssm`, `ssmmessages`, `ec2messages`) trong Private Subnet<br>  + Cấu hình Security Group cho các VPC Endpoints để cho phép kết nối từ EC2 Instance<br>  + Kiểm tra kết nối từ xa vào EC2 Instance trong Private Subnet qua SSM Session Manager mà không cần cổng SSH<br>  + Dọn dẹp tài nguyên để tránh phát sinh chi phí | 21/05/2026 | 21/05/2026 | https://cloudjourney.awsstudygroup.com/ |

### Thành tựu Tuần 5:
#### Lý thuyết:
- Hiểu rõ khái niệm và kiến trúc hoạt động của AWS Systems Manager (SSM) Session Manager để quản trị máy chủ từ xa an toàn.
- Nắm vững vai trò của VPC Endpoints (Interface Endpoints) trong việc kết nối riêng tư từ mạng nội bộ tới các dịch vụ AWS mà không qua định tuyến Internet.
- Hiểu cách NAT Gateway dịch chuyển địa chỉ IP và định tuyến lưu lượng đi ra ngoài (outbound-only) cho phân khu mạng Private Subnet.

#### Thực hành:
- Xây dựng thành công VPC mạng ảo với các phân khu mạng cô lập (Private Subnets) và NAT Gateway tại Public Subnet.
- Cấu hình bảng định tuyến Route Table cho Private Subnets đi qua NAT Gateway để kết nối ra ngoài Internet một cách an toàn.
- Thiết lập hoàn chỉnh các VPC Endpoints (`ssm`, `ssmmessages`, `ec2messages`) và kết nối thành công vào EC2 Instance trong Private Subnet qua SSM Session Manager mà không cần mở cổng SSH.

### Hình ảnh minh chứng:

1. **Khởi tạo và cấu hình NAT Gateway (Nat_Gateway)**
   ![Khởi tạo NAT Gateway](/images/1-Worklog/Worklog_week1.5/Nat_Gateway.png)
   *Mô tả chi tiết: Hình ảnh ghi nhận bước tạo và cấu hình thành công dịch vụ NAT Gateway trên giao diện điều khiển AWS Console. NAT Gateway được đặt tại Public Subnet và được liên kết với một Elastic IP (EIP) tĩnh, đóng vai trò làm cầu nối dịch địa chỉ mạng để cho phép các máy chủ EC2 nằm trong Private Subnet có thể chủ động kết nối ra Internet để tải các bản cập nhật phần mềm hoặc thư viện cần thiết, trong khi chặn toàn bộ lưu lượng truy cập trái phép từ Internet đi vào Private Subnet.*

2. **Cấu hình bảng định tuyến Route Table cho NAT (NAT)**
   ![Cấu hình Route Table cho NAT](/images/1-Worklog/Worklog_week1.5/NAT.png)
   *Mô tả chi tiết: Hình ảnh hiển thị cấu hình bảng định tuyến (Route Table) của Private Subnets được cập nhật thêm một route mới chỉ định lưu lượng đi ra Internet (dải `0.0.0.0/0`) chuyển tiếp đến NAT Gateway đã tạo ở bước trước. Cấu hình định tuyến này đảm bảo luồng lưu lượng của mạng nội bộ được vận hành chính xác và an toàn.*

3. **Kiểm tra kết nối và truy cập thông qua VPC Endpoint (Connect_endpoint)**
   ![Kiểm tra kết nối qua VPC Endpoint](/images/1-Worklog/Worklog_week1.5/Connect_endpoint.png)
   *Mô tả chi tiết: Hình ảnh minh chứng việc thiết lập thành công dịch vụ VPC Endpoints (bao gồm các endpoint cho dịch vụ SSM, EC2 Messages, và SSM Messages) để cho phép kết nối, quản lý máy chủ EC2 trong phân khu mạng Private Subnet từ xa thông qua dịch vụ AWS Systems Manager (SSM) Session Manager. Điều này giúp quản trị viên có thể truy cập terminal của máy chủ một cách an toàn mà hoàn toàn không cần mở cổng 22 SSH hay gán Public IP, tăng cường tối đa mức độ an ninh cho hệ thống.*

