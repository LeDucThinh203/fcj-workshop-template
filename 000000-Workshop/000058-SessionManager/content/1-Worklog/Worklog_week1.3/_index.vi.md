---
title: "Worklog Tuần 3"
date: 2026-05-13
weight: 3
chapter: false
pre: " <b> 1.3 </b> "
---

## Mục tiêu Tuần 3:
- Tìm hiểu về dịch vụ Amazon EC2 trên AWS.
- Thực hành khởi tạo, cấu hình và quản lý EC2 Instances.
- Triển khai ứng dụng Node.js trên môi trường Linux và Windows.

## Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Tổng quan về Amazon EC2<br>- Tìm hiểu về Instance Types, AMI, Key Pair và Snapshot<br>- Hiểu cơ chế hoạt động của EC2 Instances | 05/04/2026 | 05/04/2026 | [Amazon EC2 Basics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 3 | - Chuẩn bị môi trường EC2<br>+ Tạo VPC cho Linux<br>+ Tạo VPC cho Windows<br>+ Tạo Security Group cho các Instance Linux và Windows | 05/05/2026 | 05/05/2026 | [EC2 Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)<br>FCJ Lab |
| 4 | - Khởi tạo EC2 Instance Windows<br>+ Tạo Windows Instance<br>+ Kết nối Remote Desktop vào Windows Instance | 05/06/2026 | 05/06/2026 | [EC2 Windows Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 5 | - Khởi tạo EC2 Instance Linux<br>+ Tạo Linux Instance<br>+ Kết nối SSH vào Linux Instance<br>- Tìm hiểu thay đổi cấu hình EC2 và quản lý EBS Snapshot | 05/07/2026 | 05/07/2026 | [EC2 Linux Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 6 | - Thực hành nâng cao EC2<br>+ Tạo Custom AMI<br>+ Tạo Instance từ Custom AMI<br>+ Thực hành truy cập EC2 khi mất Key Pair | 05/08/2026 | 05/08/2026 | [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)<br>FCJ Lab |
| 7 - Chủ nhật | - Triển khai ứng dụng Node.js lên EC2<br>+ Cài đặt Server LAMP/XAMPP<br>+ Cài đặt Node.js trên Linux và Windows<br>+ Triển khai ứng dụng Node.js<br>- Tìm hiểu giới hạn tài nguyên sử dụng IAM | 05/09/2026 | 05/10/2026 | [IAM for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html)<br>FCJ Lab |

## Thành tựu Tuần 3:
### Lý thuyết:
- Nắm vững kiến trúc và cơ chế hoạt động của dịch vụ Amazon EC2 (Elastic Compute Cloud).
- Hiểu rõ các thành phần cốt lõi: Instance Types (tối ưu hóa tài nguyên), Amazon Machine Image (AMI - đóng gói hệ điều hành), Key Pair (bảo mật khóa công khai/khóa bí mật) và EBS Volume/Snapshot (lưu trữ và sao lưu dữ liệu).
- Tìm hiểu về phân quyền IAM Role cho EC2 để cấp quyền truy cập tài nguyên AWS khác một cách an toàn mà không cần lưu trữ Access Key trên máy chủ.

### Thực hành:
- Thiết lập hoàn chỉnh môi trường mạng bảo mật và khởi tạo thành công 2 EC2 Instances (1 Linux Instance nằm trong Public Subnet và 1 Linux Instance nằm trong Private Subnet).
- Cấu hình Security Group mở cổng thích hợp (cổng 22 cho SSH, cổng 80/443 cho Web Server) đảm bảo kiểm soát chặt chẽ lưu lượng inbound/outbound.
- Thực hành kết nối thành công tới các máy chủ và chạy thử nghiệm các dịch vụ cơ bản.

### Hình ảnh minh chứng:

1. **Khởi tạo và kiểm tra kết nối EC2 Instance trong Public Subnet (EC2_Public)**
   ![EC2 Public Instance](/images/1-Worklog/Worklog_week1.3/EC2_Public.png)
   *Mô tả chi tiết: Hình ảnh minh chứng quá trình khởi tạo thành công EC2 Instance trong phân khu mạng Public Subnet. Hệ thống máy chủ được gán Public IP và liên kết với Security Group cho phép truy cập từ xa. Kết quả hiển thị trạng thái instance đang chạy (Running) cùng các thông số cấu hình mạng cần thiết, sẵn sàng cho việc kết nối trực tiếp qua giao thức SSH.*

2. **Khởi tạo và cấu hình bảo mật cho EC2 Instance trong Private Subnet (EC2_Private)**
   ![EC2 Private Instance](/images/1-Worklog/Worklog_week1.3/EC2_Private.png)
   *Mô tả chi tiết: Hình ảnh ghi nhận cấu hình của EC2 Instance được triển khai hoàn toàn trong Private Subnet (phân khu mạng nội bộ bảo mật cao). Máy chủ này không được cấp phát Public IP nhằm cô lập hoàn toàn khỏi môi trường Internet công cộng, đảm bảo an toàn tuyệt đối cho cơ sở dữ liệu hoặc các ứng dụng backend bên trong. Mọi kết nối đến instance này đều phải đi qua máy chủ trung chuyển (Bastion Host / NAT Gateway) hoặc thông qua VPC Endpoints.*

3. **Tạo Người dùng IAM (Create IAM User)**
   ![Create IAM User](/images/1-Worklog/Worklog_week1.3/Create%20IAM%20User.png)
   *Mô tả chi tiết: Quá trình tạo mới một IAM User trong AWS Management Console. Bước này bao gồm việc thiết lập thông tin người dùng, lựa chọn loại truy cập (truy cập qua CLI hoặc qua Console), và cấp phát các thông tin đăng nhập ban đầu một cách an toàn.*

4. **Tạo Nhóm Người dùng (Create User Groups)**
   ![Create user groups](/images/1-Worklog/Worklog_week1.3/Create%20user%20groups.png)
   *Mô tả chi tiết: Nhóm các người dùng IAM lại với nhau. Việc tạo nhóm giúp quản lý phân quyền dễ dàng hơn bằng cách gán các chính sách (IAM policies) cho toàn bộ nhóm thay vì gán lẻ tẻ cho từng người dùng, tuân thủ nguyên tắc đặc quyền tối thiểu.*

5. **Kiểm tra Quyền hạn (Check Permission)**
   ![Check permission](/images/1-Worklog/Worklog_week1.3/Check%20permission.png)
   *Mô tả chi tiết: Xác minh các chính sách đã đính kèm và quyền hạn được giao cho người dùng hoặc nhóm IAM. Bước này nhằm đảm bảo các thực thể được cấu hình có chính xác các quyền cần thiết để thực hiện thao tác trên AWS mà không vượt quá giới hạn cho phép.*

6. **Kiểm tra Tổng thể (General Check)**
   ![Check](/images/1-Worklog/Worklog_week1.3/Check.png)
   *Mô tả chi tiết: Bước kiểm tra và xác nhận tổng thể để đảm bảo rằng tất cả các cấu hình IAM, bao gồm việc tạo người dùng và gán nhóm, đã được áp dụng thành công và đang hoạt động đúng như mong đợi.*

7. **Giới hạn chuyển đổi Role theo IP (Limit Switch Role by IP)**
   ![Limit switch by IP](/images/1-Worklog/Worklog_week1.3/limit%20switch%20by%20IP.png)
   *Mô tả chi tiết: Triển khai các chính sách bảo mật nâng cao sử dụng điều kiện IAM. Hình ảnh này minh họa việc hạn chế hành động sts:AssumeRole (Switch Role) sao cho nó chỉ có thể được thực hiện từ các địa chỉ IP đáng tin cậy cụ thể (ws:SourceIp), giúp tăng cường đáng kể bảo mật mạng.*

8. **Giới hạn chuyển đổi Role theo thời gian (Limit Switch Role by Time)**
   ![Limit switch role by time](/images/1-Worklog/Worklog_week1.3/limit%20switch%20role%20by%20time.png)
   *Mô tả chi tiết: Áp dụng các hạn chế về thời gian cho IAM roles. Cấu hình này sử dụng các điều kiện như ws:CurrentTime để đảm bảo rằng người dùng chỉ có thể đảm nhận các role cụ thể trong khoảng thời gian làm việc được chỉ định, giảm thiểu rủi ro truy cập trái phép ngoài giờ hoạt động.*
