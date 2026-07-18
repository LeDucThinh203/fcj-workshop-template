---
title: "Worklog Tuần 4"
date: 2026-05-13
weight: 4
chapter: false
pre: " <b> 1.4 </b> "
---

## Mục tiêu Tuần 4:
- Khởi tạo và cấu hình môi trường mạng (VPC, Subnet Groups, Security Groups) cho các EC2 Instance và RDS DB Instance.
- Triển khai EC2 Instance chạy Linux, cấu hình quyền hạn file khóa SSH và thực hiện kết nối SSH an toàn qua MobaXterm.
- Cài đặt Git, Node.js và MySQL client trên máy chủ EC2 để chuẩn bị và chạy ứng dụng Web Node.js kết nối tới RDS database.
- Hiểu rõ các thao tác quản trị cơ sở dữ liệu trên RDS bao gồm xem Logs & Events, thiết lập Maintenance & Backup, thực hiện Snapshots và tìm hiểu kiến trúc sẵn sàng cao (Multi-AZ, Read Replicas).

## Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày kết thúc | Nguồn tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Tổng quan về Amazon RDS<br>- So sánh RDS với các dịch vụ lưu trữ khác (EC2 DB, DynamoDB, Redshift, S3) | 11/05/2026 | 11/05/2026 | [Amazon RDS Documentation](https://docs.aws.amazon.com/rds/) |
| 3 | - Cấu hình mạng cho RDS:<br>  + Tạo VPC và các subnet liên quan<br>  + Tạo Security Groups cho EC2 và RDS<br>  + Tạo DB Subnet Group | 12/05/2026 | 12/05/2026 | [VPC for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) |
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


### 4. Khởi tạo một VPC

**Khởi tạo VPC với Subnets và các tài nguyên liên quan**

{{% notice info %}}
**Thông tin:** Amazon Virtual Private Cloud (Amazon VPC) cho phép bạn khởi chạy các tài nguyên AWS vào một mạng ảo mà bạn đã định nghĩa. Mạng ảo này gần giống với một mạng truyền thống trong trung tâm dữ liệu của riêng bạn, với các lợi ích của việc sử dụng cơ sở hạ tầng có thể mở rộng của AWS.
{{% /notice %}}

Thực hiện theo các bước sau để tạo VPC với tất cả các thành phần cần thiết cho việc triển khai Amazon RDS của bạn:

1. Mở bảng điều khiển Amazon VPC tại [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).
   ![Create a VPC](/images/1-Worklog/Worklog_week1.4/Create%20VPC.png)

2. Trên bảng điều khiển VPC, chọn **Create VPC**.

3. Đối với **Resources to create**, chọn **VPC and more** để tạo một môi trường VPC hoàn chỉnh.
   ![Create a VPC 1](/images/1-Worklog/Worklog_week1.4/Create%20VPC%201.png)

4. Cấu hình tùy chọn **Name tag auto-generation** dựa trên sở thích của bạn. Điều này cho phép AWS tự động tạo tên nhất quán cho tất cả các tài nguyên VPC.

5. Nhập dải **IPv4 CIDR block** cho VPC của bạn (ví dụ: 10.0.0.0/16). Điều này định nghĩa dải địa chỉ IP có sẵn trong VPC của bạn.

6. (Tùy chọn) Để bật hỗ trợ IPv6, chọn **IPv6 CIDR block** và chọn dải IPv6 do Amazon cung cấp.

7. Chọn tùy chọn **Tenancy** thích hợp:
   - **Default**: Các EC2 instance sử dụng thuộc tính tenancy được chỉ định trong quá trình khởi chạy
   - **Dedicated**: Tất cả các EC2 instance chạy trên phần cứng dành riêng cho tài khoản của bạn

   {{% notice tip %}}
   **Mẹo hay:** Hầu hết các khối lượng công việc nên sử dụng Default tenancy để tối ưu hóa chi phí. Chỉ chọn Dedicated khi bạn có các yêu cầu tuân thủ hoặc cấp phép cụ thể.
   {{% /notice %}}

8. Đối với **Number of Availability Zones (AZs)**, chọn ít nhất hai AZ để đảm bảo tính sẵn sàng cao.
   ![Create a VPC 2](/images/1-Worklog/Worklog_week1.4/Create%20VPC%202.png)

9. Cấu hình **Number of public subnets** và **Number of private subnets** của bạn. Đối với việc triển khai Amazon RDS, bạn thường sẽ cần private subnets cho các database instance của mình và public subnets cho các tài nguyên cần truy cập internet.

   {{% notice warning %}}
   **Lưu ý bảo mật:** Đặt các RDS instance của bạn trong private subnets để tăng cường bảo mật bằng cách ngăn chặn truy cập internet trực tiếp vào cơ sở dữ liệu của bạn.
   {{% /notice %}}

10. (Tùy chọn) Nếu các tài nguyên trong private subnets cần truy cập internet, hãy cấu hình **NAT gateways** trong mỗi AZ nơi bạn có các tài nguyên yêu cầu kết nối ra ngoài.

    {{% notice tip %}}
    **Mẹo hay:** Đối với môi trường sản xuất, hãy triển khai NAT gateways trong mỗi AZ để loại bỏ sự phụ thuộc chéo AZ và cải thiện khả năng chịu lỗi.
    {{% /notice %}}

11. (Tùy chọn) Đối với kết nối IPv6 ra ngoài từ private subnets, chọn **Yes** cho **Egress-only Internet Gateway**.

12. (Tùy chọn) Để cho phép truy cập riêng vào Amazon S3, chọn **VPC endpoints**, **S3 Gateway**. Điều này tạo một gateway endpoint cho phép các tài nguyên trong VPC của bạn truy cập S3 mà không cần sử dụng internet công cộng.

13. Đối với **DNS options**, các cài đặt mặc định bật cả phân giải DNS và hostnames DNS, được khuyến nghị cho hầu hết các triển khai.

14. (Tùy chọn) Thêm tags cho VPC của bạn bằng cách mở rộng **Additional tags** và nhập các cặp key-value.

15. Xem lại ngăn **Preview** để thấy bản mô tả trực quan về kiến trúc VPC bạn đã cấu hình.

16. Chọn **Create VPC** để cấp phát tất cả các tài nguyên đã cấu hình.
    ![Create a VPC 3](/images/1-Worklog/Worklog_week1.4/Create%20VPC%203.png)
    ![Create a VPC 4](/images/1-Worklog/Worklog_week1.4/Create%20VPC%204.png)

**Cấu hình gán địa chỉ IP công cộng cho Subnets**

{{% notice info %}}
**Thông tin:** Cài đặt tự động gán địa chỉ IPv4 công cộng (auto-assign public IPv4 address) xác định xem các instance được khởi chạy trong một subnet có tự động nhận địa chỉ IP công cộng hay không. Đối với các triển khai RDS, database subnets của bạn thường nên tắt cài đặt này.
{{% /notice %}}

Để sửa đổi hành vi gán địa chỉ IP công cộng cho một subnet:

1. Mở bảng điều khiển Amazon VPC tại [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

2. Trong ngăn điều hướng, chọn **Subnets**.
   ![Create a VPC 5](/images/1-Worklog/Worklog_week1.4/Create%20VPC%205.png)

3. Chọn subnet của bạn và chọn **Actions**, sau đó chọn **Edit subnet settings**.
   ![Create a VPC 6](/images/1-Worklog/Worklog_week1.4/Create%20VPC%206.png)

4. Cấu hình cài đặt **Auto-assign public IPv4 address**:
   - **Đã kiểm tra (Checked)**: Các instance khởi chạy trong subnet này tự động nhận địa chỉ IPv4 công cộng
   - **Bỏ chọn (Unchecked)**: Các instance khởi chạy trong subnet này không nhận địa chỉ IPv4 công cộng trừ khi được yêu cầu cụ thể trong quá trình khởi chạy

   {{% notice warning %}}
   **Lưu ý bảo mật:** Đối với các subnets sẽ chứa RDS instance của bạn, hãy đảm bảo cài đặt này được bỏ chọn để ngăn việc vô tình gán IP công cộng.
   {{% /notice %}}

5. Chọn **Save** để áp dụng các thay đổi của bạn.

{{% notice warning %}}
**Cảnh báo:** Các default subnets được bật sẵn auto-assign public IPv4 addresses theo mặc định. Luôn xác minh cài đặt này khi sử dụng default subnets cho việc triển khai cơ sở dữ liệu.
{{% /notice %}}

---

### 5. Tạo EC2 Security Group

**Tạo Security Group cho EC2 Instances**

{{% notice info %}}
**Thông tin:** Security groups hoạt động như tường lửa ảo cho các Amazon EC2 instance của bạn để kiểm soát lưu lượng truy cập vào và ra. Đối với việc triển khai RDS của chúng ta, cần phải tạo một security group cho các EC2 instance sẽ kết nối với cơ sở dữ liệu.
{{% /notice %}}

Làm theo các bước sau để tạo một security group với các cổng cần thiết:

1. Điều hướng đến AWS Management Console và đăng nhập vào tài khoản của bạn.

2. Trong AWS Management Console, tìm kiếm và chọn **EC2** trong phần services.

3. Trong ngăn điều hướng EC2, bên dưới **Network & Security**, chọn **Security Groups**.

4. Nhấp vào nút **Create security group**.
   ![Tạo EC2 Security Group](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20Security%20Group.png)

5. Trong phần **Basic details**:
   - Nhập một tên mô tả cho **Security group name** (ví dụ: "EC2-Web-App-SG")
   - Cung cấp một **Description** (mô tả) có ý nghĩa (ví dụ: "Security group cho EC2 instances kết nối tới RDS")
   - Chọn **VPC** của bạn từ menu thả xuống
   ![Cấu hình chi tiết Security Group](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20Security%20Group%201.png)

6. Trong phần **Inbound rules**, nhấp vào **Add rule** để cấu hình quyền truy cập sau:
   - **HTTP (80)**: Chọn "HTTP" từ menu Type (tự động thiết lập cổng 80)
   - **HTTPS (443)**: Chọn "HTTPS" từ menu Type (tự động thiết lập cổng 443)
   - **Custom TCP (5000)**: Chọn "Custom TCP" và nhập "5000" vào trường Port range
   - **SSH (22)**: Chọn "SSH" từ menu Type (tự động thiết lập cổng 22)

   {{% notice warning %}}
   **Lưu ý bảo mật:** Đối với môi trường sản xuất, hãy hạn chế các địa chỉ IP nguồn cho truy cập SSH chỉ từ các dải IP đáng tin cậy thay vì cho phép truy cập từ bất kỳ đâu (0.0.0.0/0).
   {{% /notice %}}

   ![Cấu hình Inbound Rules](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20Security%20Group%202.png)

7. Xem lại các cài đặt của bạn và nhấp vào **Create security group**.
   ![Hoàn tất tạo Security Group](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20Security%20Group%203.png)

8. Sau khi được tạo, security group mới sẽ xuất hiện trong danh sách security groups của bạn. Ghi lại **Security Group ID** vì bạn sẽ cần nó khi khởi chạy các EC2 instance.
   ![Security Group đã được tạo](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20Security%20Group%204.png)

{{% notice tip %}}
**Mẹo hay:** Bạn có thể sửa đổi các quy tắc security group bất kỳ lúc nào và các thay đổi sẽ có hiệu lực ngay lập tức. Điều này cho phép bạn điều chỉnh kiểm soát truy cập khi yêu cầu ứng dụng của bạn thay đổi.
{{% /notice %}}

{{% notice warning %}}
**Cảnh báo:** Security groups có tính trạng thái (stateful) — nếu bạn cho phép lưu lượng truy cập vào trên một cổng cụ thể, lưu lượng phản hồi đi ra tương ứng sẽ tự động được cho phép, bất kể các quy tắc outbound.
{{% /notice %}}

---

### 6. Tạo RDS Security Group

**Tạo Security Group cho Amazon RDS**

{{% notice info %}}
**Thông tin:** Security groups hoạt động như tường lửa ảo cho các Amazon RDS instance của bạn, kiểm soát lưu lượng truy cập vào và ra ở cấp độ instance. Mỗi security group chứa một tập hợp các quy tắc lọc lưu lượng dựa trên giao thức, cổng, và nguồn hoặc đích.
{{% /notice %}}

Thực hiện theo các bước sau để tạo một security group dành riêng cho Amazon RDS database instance của bạn:

1. Điều hướng đến Amazon VPC console và chọn **Security Groups** từ ngăn điều hướng.

2. Nhấp vào **Create Security Group** để tạo một security group mới dành riêng cho RDS database instance của bạn.

3. Trong phần **Basic details**:
   - Nhập một tên mô tả cho **Security group name** (ví dụ: "RDS-MySQL-SG")
   - Cung cấp một **Description** (mô tả) có ý nghĩa (ví dụ: "Security group cho các RDS MySQL database instances")
   - Chọn **VPC** của bạn từ menu thả xuống
   ![Tạo Security Group](/images/1-Worklog/Worklog_week1.4/RDS%20security%20group.png)

4. Đảm bảo VPC mà bạn đã tạo trước đó được chọn để liên kết security group với môi trường mạng của bạn.

5. Cấu hình **Inbound rules** để kiểm soát những nguồn lưu lượng nào có thể truy cập vào cơ sở dữ liệu của bạn:
   - Chọn **MySQL/Aurora** từ menu Type (tự động thiết lập cổng 3306)
   - Đối với Source (Nguồn), chọn ID security group của các EC2 instance cần kết nối với cơ sở dữ liệu

   {{% notice warning %}}
   **Lưu ý bảo mật:** Việc chỉ định EC2 security group làm nguồn thay vì một dải IP đảm bảo chỉ các instance có security group đó mới có thể kết nối với cơ sở dữ liệu của bạn, giúp tăng cường bảo mật.
   {{% /notice %}}

   ![Cấu hình Inbound Rules](/images/1-Worklog/Worklog_week1.4/RDS%20security%20group%201.png)

6. Xem lại các cài đặt của bạn và nhấp vào **Create Security Group** để hoàn tất quá trình.
   ![Hoàn tất tạo Security Group](/images/1-Worklog/Worklog_week1.4/RDS%20security%20group%202.png)

{{% notice tip %}}
**Mẹo hay:** Bạn có thể sửa đổi các quy tắc security group bất kỳ lúc nào và các thay đổi sẽ có hiệu lực ngay lập tức. Điều này cho phép bạn điều chỉnh kiểm soát truy cập khi yêu cầu ứng dụng của bạn thay đổi.
{{% /notice %}}

{{% notice warning %}}
**Cảnh báo:** Phương pháp tốt nhất (best practice) là sử dụng các security groups riêng biệt cho các RDS instance và EC2 instance của bạn. Sự tách biệt này cung cấp khả năng cách ly bảo mật tốt hơn và giúp việc quản lý quyền cho từng loại tài nguyên một cách độc lập dễ dàng hơn.
{{% /notice %}}

![Security Group đã được tạo](/images/1-Worklog/Worklog_week1.4/RDS%20security%20group%203.png)

---

### 7. Tạo DB Subnet Group

**Tạo DB Subnet Group cho Amazon RDS**

{{% notice info %}}
**Thông tin:** DB subnet group là một tập hợp các subnets mà bạn chỉ định cho các Amazon RDS database instances của mình trong một VPC. DB subnet groups cho phép bạn chỉ định các subnets và dải IP cụ thể nơi Amazon RDS có thể triển khai các database instances, đảm bảo sự cách ly mạng và tính khả dụng phù hợp.
{{% /notice %}}

Thực hiện theo các bước sau để tạo DB subnet group:

1. Điều hướng đến AWS Management Console và đăng nhập vào tài khoản của bạn.

2. Tìm kiếm và chọn **RDS** trong phần services.

3. Trong ngăn điều hướng, chọn **Subnet groups**.

4. Nhấp vào **Create DB Subnet Group**.
   ![Tạo DB Subnet Group](/images/1-Worklog/Worklog_week1.4/Create%20DB%20subnet%20group.png)

5. Trên trang Create DB Subnet Group, cấu hình các chi tiết cơ bản:
   - Nhập một **Name** (Tên) mô tả cho subnet group của bạn (ví dụ: "rds-subnet-group")
   - Cung cấp một **Description** (Mô tả) có ý nghĩa (ví dụ: "Subnet group cho các RDS instances")
   - Chọn **VPC** mà bạn đã tạo trước đó từ menu thả xuống
   ![Cấu hình chi tiết DB Subnet Group](/images/1-Worklog/Worklog_week1.4/Create%20DB%20subnet%20group%201.png)

6. Trong phần **Add subnets**:
   - Chọn ít nhất hai **Availability Zones** khác nhau để cho phép triển khai Multi-AZ
   - Chọn các **Subnets** thích hợp từ mỗi Availability Zone (thường là private subnets cho cơ sở dữ liệu sản xuất)

   {{% notice warning %}}
   **Lưu ý bảo mật:** Để tăng cường bảo mật, hãy đặt các RDS instances của bạn trong private subnets không có kết nối internet trực tiếp.
   {{% /notice %}}

7. Nhấp vào **Create** để tạo DB subnet group của bạn.
   ![Thêm Subnets vào DB Subnet Group](/images/1-Worklog/Worklog_week1.4/Create%20DB%20subnet%20group%202.png)

{{% notice warning %}}
**Cảnh báo:** DB subnet group phải bao gồm các subnets ở ít nhất hai Availability Zones khác nhau để hỗ trợ triển khai Multi-AZ. Không có cấu hình này, bạn sẽ không thể bật tính năng Multi-AZ cho các RDS instances của mình.
{{% /notice %}}

{{% notice tip %}}
**Mẹo hay:** Nếu bạn đã bật AWS Local Zones trong tài khoản của mình, bạn cũng có thể chọn một Availability Zone group trên trang Create DB Subnet Group. Trong trường hợp này, hãy chọn Availability Zone group, các Availability Zones tương ứng và các subnets thích hợp.
{{% /notice %}}

Sau khi được tạo, DB subnet group mới của bạn sẽ xuất hiện trong danh sách các DB subnet groups trong bảng điều khiển RDS. Bạn có thể chọn nó để xem thông tin chi tiết, bao gồm tất cả các subnets được liên kết, trong bảng thông tin chi tiết ở phía dưới cùng của cửa sổ.

![DB Subnet Group đã được tạo](/images/1-Worklog/Worklog_week1.4/Create%20DB%20subnet%20group%203.png)

---

### 8. Tạo EC2 Instance

**Khởi tạo EC2 Instance**

{{% notice info %}}
**Thông tin:** Amazon EC2 (Elastic Compute Cloud) cung cấp khả năng tính toán có thể mở rộng trên AWS Cloud, loại bỏ nhu cầu phải đầu tư vào phần cứng trả trước.
{{% /notice %}}

Để tạo một Linux EC2 instance sử dụng AWS Management Console, hãy làm theo các hướng dẫn sau. Hướng dẫn này giúp bạn nhanh chóng khởi chạy instance đầu tiên của mình với các cấu hình thiết yếu. Để biết các tùy chọn nâng cao, hãy tham khảo tài liệu Launch Instance.

**Truy cập AWS Console**
1. Mở trình duyệt web và điều hướng đến Amazon EC2 console tại [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

**Khởi chạy Instance của bạn**
2. Trên trang tổng quan (dashboard) của bảng điều khiển EC2, tìm hộp **Launch instance**, chọn **Launch instance**, sau đó chọn **Launch instance** từ menu thả xuống.
   ![Khởi chạy Instance](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance.png)

**Cấu hình Chi tiết Instance**
3. Trong phần **Name and tags**, nhập tên mô tả cho instance của bạn.
   ![Name and Tags](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%201.png)

4. Trong phần **Application and OS Images (Amazon Machine Image)**, cấu hình như sau:
   - Chọn **Quick Start**, sau đó chọn **Amazon Linux**
   - Từ các tùy chọn Amazon Machine Image (AMI), chọn phiên bản **HVM của Amazon Linux 2023**

   {{% notice tip %}}
   **Mẹo hay:** Tìm kiếm các AMI được đánh dấu là Free tier eligible (đủ điều kiện cấp miễn phí) để tránh các khoản phí ngoài dự kiến nếu bạn đang sử dụng AWS Free Tier.
   {{% /notice %}}

   ![Lựa chọn AMI](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%202.png)

5. Dưới **Instance type**, chọn **t2.micro** (được chọn sẵn theo mặc định).

   {{% notice info %}}
   **Thông tin:** Loại instance t2.micro đủ điều kiện cho AWS Free Tier. Ở những khu vực không có t2.micro, bạn có thể sử dụng t3.micro trong Free Tier. Để biết thêm chi tiết, xem phần AWS Free Tier.
   {{% /notice %}}

   ![Loại Instance](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%203.png)

6. Dưới **Key pair (login)**, chọn cặp khóa (key pair) bạn đã tạo trong quá trình thiết lập AWS.

   {{% notice warning %}}
   **Cảnh báo:** Không chọn Proceed without a key pair (Không khuyến nghị). Nếu không có cặp khóa, bạn sẽ không thể kết nối với instance của mình.
   {{% /notice %}}

   ![Key Pair](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%204.png)

7. Dưới **Network settings**, nhấp vào **Edit** và cấu hình security group của bạn:
   - Bạn có thể sử dụng security group được tạo tự động, hoặc
   - Chọn **Select existing security group** và chọn một security group bạn đã tạo trước đó

   {{% notice warning %}}
   **Lưu ý bảo mật:** Security groups hoạt động như tường lửa ảo kiểm soát lưu lượng vào và ra instance của bạn. Đảm bảo security group của bạn cho phép truy cập SSH (cổng 22) chỉ từ địa chỉ IP của bạn.
   {{% /notice %}}

   ![Cấu hình Mạng](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%205.png)

**Khởi chạy và Xác minh Instance của bạn**
8. Xem lại tóm tắt cấu hình instance trong bảng Summary. Khi đã sẵn sàng, nhấp vào **Launch instance**.
   ![Xem lại và Khởi chạy](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%206.png)

9. Trên trang xác nhận, nhấp vào **View all instances** để trở lại bảng điều khiển EC2.

10. Theo dõi trạng thái của instance trên màn hình Instances:
    - Trạng thái ban đầu: **pending** (đang chờ xử lý)
    - Trạng thái hoạt động: **running** (đang chạy, kèm theo tên miền DNS công cộng được gán)

    {{% notice tip %}}
    **Mẹo hay:** Nếu cột Public IPv4 DNS bị ẩn, hãy nhấp vào biểu tượng bánh răng (Settings) ở góc trên bên phải, bật Public IPv4 DNS và nhấp vào Confirm.
    {{% /notice %}}

    Đợi instance vượt qua tất cả các kiểm tra trạng thái (status checks) trước khi thử kết nối.
    ![Trạng thái Instance](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%207.png)

---

### 9. Kết nối tới EC2 Instance qua SSH bằng MobaXterm

{{% notice info %}}
**Thông tin:** MobaXterm là một terminal nâng cao cho Windows với một X11 server, trình khách SSH có hỗ trợ tab và nhiều công cụ mạng khác.
{{% /notice %}}

Thực hiện theo các bước sau để kết nối với EC2 instance của bạn bằng MobaXterm:

**Cài đặt MobaXterm**
1. Tải xuống MobaXterm từ trang web chính thức: [MobaXterm Website](https://mobaxterm.mobatek.net/)
2. Cài đặt ứng dụng trên máy tính của bạn

**Cấu hình Kết nối SSH**
3. Khởi chạy MobaXterm
4. Nhấp vào biểu tượng **Session** ở góc trên bên trái
5. Trong cửa sổ cấu hình, nhập:
   - **Remote Host:** Địa chỉ IP công cộng (public IP) hoặc tên DNS của EC2 instance
   - **Port:** 22 (cổng SSH mặc định)
   - **Username:** Người dùng mặc định cho AMI của bạn (thường là ec2-user đối với Amazon Linux)
   - **Advanced SSH settings:** Duyệt và chọn file khóa bảo mật cá nhân (private key - .pem)

   ![Cấu hình MobaXterm](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%208.png)

**Kết nối với Instance của bạn**
6. Nhấp vào **OK** để lưu cấu hình
7. Nhấp vào biểu tượng connect để thiết lập kết nối SSH

{{% notice warning %}}
**Lưu ý bảo mật:** Đảm bảo file private key (.pem) của bạn có quyền hạn chế (restricted permissions). Trên Windows, hãy kiểm tra để chắc chắn rằng file không thể bị truy cập bởi người dùng khác.
{{% /notice %}}

**Kết nối Thành công**
Sau khi kết nối thành công, bạn sẽ có quyền truy cập terminal vào EC2 instance và có thể bắt đầu quản trị server của mình.
![Kết nối Thành công](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%209.png)

---

### 10. Cài đặt Git trên Amazon EC2 2023

Dưới đây là hướng dẫn cài đặt Git trên máy ảo Amazon EC2 chạy hệ điều hành Amazon Linux 2023 bằng các bước cơ bản.

**Cập nhật các gói hệ thống**
Đầu tiên, hãy cập nhật các gói hệ thống của bạn để đảm bảo bạn đang sử dụng phiên bản mới nhất:
```bash
sudo dnf update -y
```

**Tìm gói Git**
Sử dụng lệnh sau để tìm gói Git trong repository:
```bash
sudo dnf search git
```

**Cài đặt Git**
Khi bạn đã tìm thấy gói Git, bạn có thể cài đặt nó bằng lệnh sau:
```bash
sudo dnf install git -y
```

**Xác minh cài đặt Git**
Cuối cùng, hãy kiểm tra xem phiên bản Git đã được cài đặt thành công chưa:
```bash
git --version
```
Nếu bạn thấy phiên bản Git hiển thị, điều đó có nghĩa là quá trình cài đặt đã hoàn tất.

![Xác minh cài đặt Git](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance.png)

---

### 11. Cài đặt Node.js trên Amazon EC2 Linux 2023

Dưới đây là Bash script để cài đặt Node.js trên Amazon EC2 Linux:

```bash
#!/bin/bash

# Color for formatting
GREEN='\033[0;32m'
NC='\033[0m' # Colorless

# Check if NVM is installed
if ! command -v nvm &> /dev/null; then
  # Step 1: Install nvm
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
  source ~/.nvm/nvm.sh
fi

# Verify nvm installation
nvm --version

# Install the LTS version of Node.js
nvm install --lts

# Use the installed LTS version
nvm use --lts

# Verify Node.js and npm installation
node -v
npm -v

# Step 4: Create package.json file (if it doesn't exist yet)
if [ ! -f package.json ]; then
  npm init -y
  echo -e "${GREEN}Created file package.json.${NC}"
fi

# Step 5: Install necessary npm packages
echo -e "Installing required npm packages..."
npm install express dotenv express-handlebars body-parser mysql

# Step 6: Install nodemon as a development dependency
echo -e "Installing nodemon as a development dependency..."
npm install --save-dev nodemon
npm install -g nodemon

# Step 7: Add npm start script to package.json
if ! grep -q '"start":' package.json; then
  npm set-script start "index.js" # Replace "your-app.js" with your entry point file
  echo -e "${GREEN}Added npm start script to package.json.${NC}"
fi

echo -e "${GREEN}Installation completed. You can now start building and running your Node.js application using 'npm start'.${NC}"
```

![Kết quả cài đặt Node.js](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%201.png)

---

### 12. Tạo DB Instance trên AWS

Để tạo một DB Instance trên AWS, bạn có thể sử dụng AWS Management Console với tùy chọn Easy create được bật hoặc tắt. Khi Easy create được bật, bạn chỉ cần chỉ định loại DB engine, kích thước DB Instance và định danh DB Instance identifier. Easy create sử dụng các cài đặt mặc định cho các tùy chọn cấu hình khác. Khi Easy create bị tắt, bạn cần chỉ định nhiều tùy chọn cấu hình hơn khi tạo database, bao gồm các tùy chọn về tính khả dụng, bảo mật, sao lưu và bảo trì.

*Lưu ý: Trong quy trình dưới đây, tùy chọn Standard create được bật, và Easy create bị tắt. Quy trình này sử dụng MySQL làm ví dụ.*

Để tạo một DB Instance:

1. Đăng nhập vào AWS Management Console và mở Amazon RDS console tại [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).
2. Ở góc trên bên phải của Amazon RDS console, chọn khu vực (AWS region) nơi bạn muốn tạo DB Instance.
3. Trong ngăn điều hướng, chọn **Databases**.
4. Chọn **Create database**, và sau đó chọn **Standard create**.
   ![Tạo tiêu chuẩn](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%202.png)

5. Đối với **Engine type**, chọn MariaDB, Microsoft SQL Server, MySQL, Oracle, hoặc PostgreSQL. Trong ví dụ này, chúng ta sử dụng Microsoft SQL Server.
6. Đối với **Database management type**, nếu bạn đang sử dụng Oracle hoặc SQL Server, hãy chọn Amazon RDS hoặc Amazon RDS Custom.
7. Đối với **Edition**, nếu bạn đang sử dụng Oracle hoặc SQL Server, hãy chọn phiên bản DB engine mà bạn muốn sử dụng.
8. Đối với **Version**, chọn phiên bản engine.
   ![Chọn phiên bản](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%203.png)

9. Trong phần **Templates**, chọn một mẫu phù hợp với trường hợp sử dụng của bạn. Nếu bạn chọn **Production**, các tùy chọn sau sẽ được chọn sẵn ở bước tiếp theo:
   - Tùy chọn Multi-AZ failover
   - Tùy chọn lưu trữ Provisioned IOPS SSD (io1)
   - Tùy chọn Protection against deletion (bảo vệ chống xóa)
   Chúng tôi khuyến nghị sử dụng các tính năng này cho môi trường sản xuất.

10. Để nhập mật khẩu quản trị viên (master password), hãy làm theo các bước sau:
    - Trong phần **Settings**, mở Credential Settings.
    - Nếu bạn muốn chỉ định một mật khẩu, bỏ chọn hộp **Auto generate a password** nếu nó đã được chọn.
    - (Tùy chọn) Thay đổi giá trị **Master username**.
    - Nhập cùng một mật khẩu vào cả hai ô **Master password** và **Confirm password**.
    - (Tùy chọn) Thiết lập kết nối tới một tài nguyên tính toán (compute resource) cho DB Instance này.
    ![Thiết lập kết nối](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%204.png)

11. Bạn có thể cấu hình kết nối giữa một Amazon EC2 instance và DB Instance mới trong quá trình tạo DB Instance. 
12. Trong phần Connectivity dưới mục **VPC security group (firewall)**, nếu bạn chọn **Create new**, một VPC security group mới với quy tắc đăng nhập cho phép địa chỉ IP máy tính cục bộ của bạn truy cập vào cơ sở dữ liệu sẽ được tạo ra.
    ![VPC Security Group](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%205.png)

13. Đối với các phần còn lại, chỉ định các cài đặt DB Instance của bạn.
14. Chọn **Create database**.
    ![Nút Create Database](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%206.png)

15. Nếu bạn chọn sử dụng mật khẩu được tạo tự động, nút **View credential details** sẽ xuất hiện trên trang Databases. Để xem username và password cho DB Instance, hãy chọn View credential details.
16. Bên dưới mục **Databases**, chọn tên của DB Instance mới.
    ![Chọn DB Instance](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%207.png)

17. Trên RDS console, thông tin về DB Instance mới sẽ xuất hiện. DB Instance sẽ có trạng thái là **Creating** cho đến khi nó được tạo xong và sẵn sàng sử dụng. Khi trạng thái chuyển sang **Available**, bạn có thể kết nối với DB Instance.
    ![DB Instance khả dụng](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%208.png)

---

### 13. Kiểm tra RDS

Trên trang thông tin chi tiết của RDS instance, bạn có thể tìm thấy các thông tin liên quan đến kết nối như Endpoint, Port (Cổng), và Username.
Endpoint là địa chỉ URL hoặc IP mà bạn dùng để kết nối với cơ sở dữ liệu RDS.
![Chi tiết cấu hình RDS](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%209.png)

---

### 14. Xem Log và Event trên AWS RDS

Để theo dõi Log và Event trên Amazon RDS, bạn có thể thực hiện theo các bước sau:
1. Đăng nhập vào AWS Management Console.
2. Chọn dịch vụ **Amazon RDS** từ bảng điều khiển chính AWS.
3. Chọn RDS instance mà bạn muốn xem Log và Event.
4. Trong trang chi tiết instance, nhấp vào tab **Logs & events**.

Tại đây, bạn có thể xem các loại log khác nhau như:
- **Error log:** Ghi lại các lỗi xảy ra trên instance.
- **General log:** Ghi lại các hoạt động chung trên instance.
- **Slow query log:** Ghi lại các truy vấn bị chậm.
- **Event log:** Hiển thị các sự kiện quan trọng liên quan đến instance.

Bạn cũng có thể tùy chỉnh các cài đặt khi xem Log và Event tại đây, ví dụ như khoảng thời gian bạn muốn xem log hoặc thiết lập thông báo qua email cho các sự kiện quan trọng.
![Xem Log và Event](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%2010.png)

---

### 15. Xem thông tin Bảo trì và Sao lưu trên AWS RDS

**Xem thông tin bảo trì**
Để xem thông tin về bảo trì cho một DB instance trong RDS:
1. Trên trang quản lý DB instance, chuyển qua tab **Maintenance & backups**.
2. Tại đây, bạn sẽ thấy thông tin về lịch trình bảo trì, bao gồm thời gian tự động sao lưu và các tác vụ bảo trì định kỳ.

**Xem thông tin sao lưu**
1. Cũng tại tab **Maintenance & backups**.
2. Ở đây, bạn có thể xem thông tin chi tiết về các bản sao lưu tự động và sao lưu thủ công. Bạn cũng có thể tiến hành cấu hình và quản lý các thiết lập sao lưu.

![Bảo trì và Sao lưu](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%2011.png)


---

### 16. Triển khai Ứng dụng (Application Deployment)

**Triển khai Ứng dụng**
Để sao chép repository AWS-First-Cloud-Journey từ GitHub, bạn có thể sử dụng lệnh sau:
```bash
git clone https://github.com/AWS-First-Cloud-Journey/AWS-FCJ-Management
```
![Clone Repository](/images/1-Worklog/Worklog_week1.4/Application%20Deployment.png)

**Hướng dẫn cài đặt Node.js trên Amazon Linux 2023**
Dưới đây là một Bash script để cài đặt Node.js trên Amazon Linux. Vui lòng sao chép và thực thi các bước sau:
```bash
#!/bin/bash

# Các màu cho định dạng
GREEN='\033[0;32m'
NC='\033[0m' # Không màu

# Kiểm tra xem NVM đã được cài đặt chưa
if ! command -v nvm &> /dev/null; then
  # Bước 1: Cài đặt nvm
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
  source ~/.nvm/nvm.sh
fi

# Xác minh việc cài đặt nvm
nvm --version

# Cài đặt phiên bản LTS của Node.js
nvm install --lts

# Sử dụng phiên bản LTS đã cài đặt
nvm use --lts

# Xác minh cài đặt Node.js và npm
node -v
npm -v

# Bước 4: Tạo tệp package.json (nếu nó chưa tồn tại)
if [ ! -f package.json ]; then
  npm init -y
  echo -e "${GREEN}Đã tạo tệp package.json.${NC}"
fi

# Bước 5: Cài đặt các gói npm cần thiết
echo -e "Đang cài đặt các gói npm cần thiết..."
npm install express dotenv express-handlebars body-parser mysql

# Bước 6: Cài đặt nodemon như một phần phát triển
echo -e "Đang cài đặt nodemon như một phần phát triển..."
npm install --save-dev nodemon
npm install -g nodemon

# Bước 7: Thêm script npm start vào package.json
if ! grep -q '"start":' package.json; then
  npm set-script start "index.js"  # Thay thế "your-app.js" bằng tệp điểm nhập của bạn
  echo -e "${GREEN}Đã thêm script npm start vào package.json.${NC}"
fi

echo -e "${GREEN}Cài đặt hoàn tất. Bây giờ bạn có thể bắt đầu xây dựng và chạy ứng dụng Node.js của mình bằng 'npm start'.${NC}"
```
![Install Node.js](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%201.png)

**Cài đặt và Cấu hình MySQL Server**
Đây là một Bash script dùng để cài đặt và cấu hình máy chủ MySQL trên hệ thống. Script này thực hiện các bước sau:
- Thiết lập các biến với đường dẫn RPM của MySQL và thông tin cơ sở dữ liệu như địa chỉ RDS, tên cơ sở dữ liệu, tên người dùng và mật khẩu.
- Kiểm tra xem tệp RPM của kho lưu trữ cộng đồng MySQL đã tồn tại trong thư mục hiện tại chưa. Nếu chưa tồn tại, nó sẽ tải xuống RPM từ URL đã chỉ định.
- Cài đặt RPM của kho lưu trữ cộng đồng MySQL và MySQL Server.
- Khởi động MySQL server và cấu hình để tự động khởi động cùng hệ thống.
- Kiểm tra phiên bản MySQL đã cài đặt.
- Bảo mật máy chủ MySQL bằng lệnh `mysql_secure_installation`.
- Tạo hoặc cập nhật tệp `.env` với thông tin cơ sở dữ liệu (địa chỉ, tên cơ sở dữ liệu, tên người dùng và mật khẩu).
- Kết nối tới máy chủ MySQL bằng thông tin xác thực và bạn có thể thêm các lệnh SQL cụ thể tại đây.

*Lưu ý: Để thực thi đoạn mã này, bạn cần có quyền sudo và phải chắc chắn rằng bạn đã cung cấp đúng thông tin cơ sở dữ liệu (RDS Endpoint, tên cơ sở dữ liệu, tên người dùng và mật khẩu) trước khi chạy.*

```bash
#!/bin/bash

# Thiết lập các biến cho MySQL RPM và thông tin cơ sở dữ liệu
MYSQL_RPM_URL="https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm"
DB_HOST="RDS Endpoint"
DB_NAME="Tên cơ sở dữ liệu"
DB_USER="Tên người dùng cơ sở dữ liệu"
DB_PASS="Mật khẩu cơ sở dữ liệu"


# Kiểm tra xem MySQL Community repository RPM đã tồn tại chưa
if [ ! -f mysql80-community-release-el9-1.noarch.rpm ]; then
  sudo wget $MYSQL_RPM_URL
fi

# Cài đặt MySQL Community repository
sudo dnf install -y mysql80-community-release-el9-1.noarch.rpm

# Cài đặt MySQL server
sudo dnf install -y mysql-community-server

# Khởi động MySQL server
sudo systemctl start mysqld

# Bật MySQL để tự động khởi chạy
sudo systemctl enable mysqld

# Kiểm tra phiên bản MySQL
mysql -V

# Bảo mật máy chủ MySQL
sudo mysql_secure_installation

# Tạo hoặc cập nhật tệp .env với thông tin cơ sở dữ liệu
echo "DB_HOST=$DB_HOST" >> .env
echo "DB_NAME=$DB_NAME" >> .env
echo "DB_USER=$DB_USER" >> .env
echo "DB_PASS=$DB_PASS" >> .env

# Kết nối đến MySQL và tạo một CSDL mới (bạn có thể thêm các lệnh SQL cụ thể ở đây)
mysql -h $DB_HOST -P 3306 -u $DB_USER -p$DB_PASS
```
![Install MySQL](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%202.png)

**Tạo Cơ sở dữ liệu và Bảng trong AWS RDS**
Sau khi kết nối thành công với RDS (Relational Database Service) trên AWS, chúng ta có thể tạo một cơ sở dữ liệu mới và định nghĩa một bảng trong đó bằng cách sử dụng tập lệnh SQL sau.

**Tạo Cơ sở dữ liệu (Create Database)**
Đầu tiên, chúng ta sẽ tạo một cơ sở dữ liệu mới nếu nó chưa tồn tại. Sử dụng lệnh sau:
```sql
CREATE DATABASE IF NOT EXISTS first_cloud_users;
```
Lệnh này kiểm tra xem cơ sở dữ liệu “first_cloud_users” đã tồn tại hay chưa. Nếu chưa, nó sẽ tạo một cơ sở dữ liệu mới với tên “first_cloud_users”.

**Sử dụng Cơ sở dữ liệu (Using Database)**
Tiếp theo, chúng ta sử dụng cơ sở dữ liệu “first_cloud_users” bằng lệnh:
```sql
USE first_cloud_users;
```
Lệnh này cho biết rằng tất cả các lệnh SQL tiếp theo sẽ được thực thi trên cơ sở dữ liệu “first_cloud_users”.

**Tạo Bảng "user"**
Chúng ta đã tạo và sử dụng cơ sở dữ liệu. Bây giờ, chúng ta sẽ định nghĩa bảng “user” trong cơ sở dữ liệu này bằng tập lệnh SQL sau:
```sql
CREATE TABLE `user`
(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `first_name` VARCHAR(45) NOT NULL,
    `last_name` VARCHAR(45) NOT NULL,
    `email` VARCHAR(100) NOT NULL UNIQUE,
    `phone` VARCHAR(15) NOT NULL,
    `comments` TEXT NOT NULL,
    `status` ENUM('active', 'inactive') NOT NULL DEFAULT 'active'
) ENGINE = InnoDB;
```
Lệnh này định nghĩa cấu trúc của bảng “user” với các cột như “id”, “first_name”, “last_name”, “email”, “phone”, “comments”, và “status”. Các cột này đại diện cho thông tin của người dùng, trong đó cột “id” được đặt làm khóa chính (primary key) và tự động tăng.

**Thêm dữ liệu vào bảng "user"**
Cuối cùng, chúng ta có thể thêm dữ liệu vào bảng “user” bằng cách sử dụng lệnh `INSERT INTO`. Dưới đây là ví dụ thêm một số bản ghi vào bảng:
```sql
INSERT INTO `user`
(`first_name`, `last_name`, `email`, `phone`, `comments`, `status`)
VALUES
('Amanda', 'Nunes', 'anunes@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Alexander', 'Volkanovski', 'avolkanovski@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Khabib', 'Nurmagomedov', 'knurmagomedov@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Kamaru', 'Usman', 'kusman@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Israel', 'Adesanya', 'iadesanya@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Henry', 'Cejudo', 'hcejudo@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Valentina', 'Shevchenko', 'vshevchenko@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Tyron', 'Woodley', 'twoodley@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Rose', 'Namajunas', 'rnamajunas@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Tony', 'Ferguson', 'tferguson@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Jorge', 'Masvidal', 'jmasvidal@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Nate', 'Diaz', 'ndiaz@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Conor', 'McGregor', 'cmcGregor@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Cris', 'Cyborg', 'ccyborg@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Tecia', 'Torres', 'ttorres@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Ronda', 'Rousey', 'rrousey@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Holly', 'Holm', 'hholm@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Joanna', 'Jedrzejczyk', 'jjedrzejczyk@ufc.com', '012345 678910', 'I love AWS FCJ', 'active');
```
Lệnh này thêm các bản ghi người dùng vào bảng “user” với các thông tin như tên, email, số điện thoại, ghi chú và trạng thái mặc định là “active”.

Dưới đây là một số lệnh SQL để kiểm tra thông tin cơ sở dữ liệu trong một Hệ Quản Trị CSDL (DBMS) như MySQL hoặc PostgreSQL:

**Hiển thị danh sách tất cả các cơ sở dữ liệu:**
```sql
SHOW DATABASES;
```
Lệnh này sẽ liệt kê tất cả các cơ sở dữ liệu hiện có trong hệ thống.

**Chọn một cơ sở dữ liệu cụ thể để làm việc:**
```sql
USE database_name;
```
Lệnh này sẽ di chuyển bạn từ CSDL hiện tại sang một CSDL có tên là “database_name”. Sau khi sử dụng lệnh này, tất cả các lệnh SQL tiếp theo sẽ được áp dụng cho CSDL này.

**Hiển thị các bảng trong cơ sở dữ liệu hiện tại:**
```sql
SHOW TABLES;
```
Lệnh này sẽ liệt kê tất cả các bảng có trong CSDL hiện tại.

**Hiển thị cấu trúc của một bảng cụ thể:**
```sql
DESCRIBE table_name;
```
Lệnh này sẽ cung cấp cấu trúc của bảng có tên là “table_name”, bao gồm tên cột, kiểu dữ liệu và các thuộc tính khác của cột.

**Hiển thị thông tin về dung lượng cơ sở dữ liệu:**
```sql
SELECT table_schema "Tên CSDL", SUM(data_length + index_length) / 1024 / 1024 "Kích thước (MB)"
FROM information_schema.tables
GROUP BY table_schema;
```
Lệnh này sẽ hiển thị thông tin về dung lượng của các CSDL trong hệ thống, được tính bằng Megabytes (MB).
Hãy nhớ thay thế “database_name” và “table_name” bằng những tên cụ thể của CSDL và bảng mà bạn muốn kiểm tra.
![Các Lệnh SQL](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%203.png)

**Chạy Ứng dụng**
Sau khi bạn đã ở trong thư mục ứng dụng, hãy chạy lệnh sau để khởi động ứng dụng bằng `npm start`:
```bash
npm start
```
![npm start](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%204.png)

**Kiểm tra ứng dụng trên trình duyệt:**
Kiểm tra trạng thái của EC2 Instance: Đảm bảo EC2 Instance của bạn đang chạy và hoạt động bình thường.
Mở một trình duyệt web và nhập địa chỉ IP hoặc tên miền của EC2 Instance, theo sau là cổng 5000:
`http://<IP address or domain name>:5000`

Kết quả kiểm tra: Trình duyệt sẽ hiển thị ứng dụng của bạn nếu mọi thứ được cấu hình đúng đắn và EC2 Instance đang hoạt động.
![Kiểm tra Trình duyệt](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%205.png)

---

### 17. Giám sát và Khôi phục AWS RDS

**Giám sát AWS RDS**
Trên giao diện AWS RDS, bạn có thể thực hiện các bước sau để giám sát:
1. Chọn **Databases**.
2. Chọn DB instance mà bạn đã tạo.
3. Chọn **Monitoring**.
![Giám sát RDS](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%206.png)

**Xem Thông tin Sao lưu**
Để xem thông tin về các bản sao lưu của DB instance trong AWS RDS, hãy làm theo các bước sau:
1. Đăng nhập vào AWS Management Console.
2. Chọn dịch vụ **Amazon RDS** từ danh sách dịch vụ.
3. Trong bảng điều khiển RDS, chọn DB instance mà bạn muốn kiểm tra.
4. Trên trang quản lý DB instance, chuyển qua tab **Maintenance & backups**.
Tại đây, bạn có thể xem thông tin về các bản sao lưu tự động và thủ công. Bạn cũng có thể cấu hình và quản lý các thiết lập sao lưu.
![Sao lưu (Backups)](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%207.png)

**Xem thông tin Snapshot**
![Snapshot](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%208.png)

**Khôi phục Snapshot (Restore Snapshot)**
Chọn DB snapshot mà bạn muốn khôi phục. Trong phần Actions, chọn **Restore snapshot**.
![Khôi phục Snapshot](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%209.png)

Trên trang Restore snapshot, nhập tên cho DB instance mà bạn muốn khôi phục vào trường DB instance identifier. Chọn các cài đặt khác như kích thước bộ nhớ được cấp phát.
Cuối cùng, chọn **Restore DB instance**.
![Thiết lập Khôi phục](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%2010.png)

Hoàn tất quy trình khôi phục snapshot và kiểm tra lại cơ sở dữ liệu đã được khôi phục.
![Khôi phục Hoàn tất](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%2011.png)


---

### 18. Sao lưu và Khôi phục (Backup and Restore)

**Hiểu về Sao lưu và Khôi phục trên Amazon RDS**

{{% notice info %}}
**Thông tin:** Amazon RDS cung cấp tính năng sao lưu tự động và cho phép tạo snapshot thủ công để đảm bảo dữ liệu cơ sở dữ liệu của bạn được bảo vệ và có thể được khôi phục khi cần thiết. Những khả năng này rất cần thiết cho việc lập kế hoạch khắc phục thảm họa (disaster recovery) và duy trì tính liên tục của doanh nghiệp.
{{% /notice %}}

**Theo dõi trạng thái sao lưu trên Amazon RDS**
Để truy cập phần theo dõi sao lưu trong bảng điều khiển Amazon RDS:
1. Điều hướng đến phần **Databases** trong AWS Management Console.
2. Chọn DB instance đích của bạn.
3. Nhấp vào tab **Monitoring** để xem các số liệu hiệu suất.
![Giám sát AWS RDS](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore.png)

**Xem thông tin sao lưu**
Để xem chi tiết sao lưu cho Amazon RDS instance của bạn:
1. Đăng nhập vào AWS Management Console.
2. Chọn Amazon RDS từ menu dịch vụ.
3. Trong bảng điều khiển RDS, chọn DB instance của bạn.
4. Điều hướng đến tab **Maintenance & backups**.
Tại đây bạn có thể xem thông tin sao lưu tự động và thủ công cũng như cấu hình các cài đặt sao lưu.
![Sao lưu AWS RDS](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore%201.png)

**Quản lý Database Snapshots**
Xem các DB snapshot hiện có của bạn trong phần snapshots:
![Thông tin Snapshot](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore%202.png)

**Khôi phục từ một DB Snapshot**
Chọn DB snapshot bạn muốn sử dụng làm điểm khôi phục của mình:
1. Dưới menu thả xuống Actions, chọn **Restore snapshot**.
![Khôi phục Snapshot](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore%203.png)

**Cấu hình cho cơ sở dữ liệu đã được khôi phục:**
1. Cung cấp một định danh DB instance duy nhất (DB instance identifier) cho instance mới.
2. Chọn thông số kỹ thuật (instance specifications) phù hợp cho instance (compute, storage, v.v.).
3. Cấu hình mạng và cài đặt bảo mật.

{{% notice tip %}}
**Mẹo hay:** Khi khôi phục một cơ sở dữ liệu sản xuất, hãy cân nhắc việc khôi phục sang một instance class nhỏ hơn trước để thử nghiệm, sau đó mới mở rộng (scale up) khi cần thiết nhằm giảm thiểu chi phí trong quá trình xác thực.
{{% /notice %}}

**Bắt đầu quá trình khôi phục:**
1. Xem lại các cài đặt cấu hình của bạn.
2. Nhấp vào **Restore DB instance** để bắt đầu quá trình.

{{% notice warning %}}
**Cảnh báo:** Quá trình khôi phục tạo ra một database instance hoàn toàn mới với endpoint riêng. Bạn sẽ cần cập nhật các chuỗi kết nối của ứng dụng (connection strings) để trỏ đến instance mới này nếu định sử dụng nó cho môi trường sản xuất.
{{% /notice %}}

**Xác minh Cơ sở dữ liệu đã khôi phục**
Xác nhận khôi phục thành công:
1. Kiểm tra xem DB instance mới có xuất hiện trong bảng điều khiển RDS của bạn không.
2. Xác minh trạng thái hiển thị là "Available" khi quá trình khôi phục hoàn tất.
3. Kiểm tra kết nối và tính toàn vẹn của dữ liệu trước khi điều hướng lưu lượng truy cập sản xuất (production traffic) đến instance đã khôi phục.

{{% notice warning %}}
**Lưu ý bảo mật:** Hãy nhớ cấu hình các nhóm bảo mật (security groups) và các nhóm tham số (parameter groups) giống với instance ban đầu nếu bạn muốn giữ nguyên các kiểm soát truy cập và cấu hình của cơ sở dữ liệu.
{{% /notice %}}


---

### 19. Dọn dẹp tài nguyên (Clean up resources)

**Dọn dẹp Tài nguyên**

{{% notice info %}}
**Thông tin:** Sau khi hoàn thành bài thực hành, việc dọn dẹp tất cả các tài nguyên AWS là rất quan trọng để tránh các khoản phí phát sinh. Hãy làm theo các bước sau để xóa đúng cách tất cả các tài nguyên đã tạo trong buổi workshop này.
{{% /notice %}}

**Xóa Tài nguyên Cơ sở dữ liệu (Database Resources)**

**Xóa nhóm mạng con CSDL (DB subnet group):**
1. Điều hướng đến bảng điều khiển Amazon RDS.
2. Trong ngăn điều hướng, chọn **Subnet groups**.
3. Chọn DB subnet group liên quan đến bài lab.
4. Chọn **Delete**, sau đó xác nhận bằng cách chọn Delete trong cửa sổ xác nhận.
![Xóa DB Subnet Group](/images/1-Worklog/Worklog_week1.4/Clean.png)

**Xóa DB Instance:**
1. Truy cập RDS Management Console.
2. Ở thanh điều hướng bên trái, chọn **Databases**.
3. Chọn DB Instance liên quan đến bài lab.
4. Nhấp vào Actions, sau đó chọn **Delete**.
![Xóa DB Instance](/images/1-Worklog/Worklog_week1.4/Clean1.png)

5. Bỏ chọn mục *Create final snapshot?* và xác nhận rằng các bản sao lưu tự động sẽ không còn khả dụng nữa.
6. Nhập `delete me` vào trường xác nhận.
7. Nhấp vào **Delete**.
![Xác nhận xóa DB Instance](/images/1-Worklog/Worklog_week1.4/Clean2.png)

**Xóa DB Snapshots:**
1. Trong RDS Management Console, chọn **Snapshots** từ thanh điều hướng.
2. Chọn tất cả các snapshot liên quan đến bài lab.
3. Nhấp vào Actions, sau đó chọn **Delete snapshot**.
4. Xác nhận bằng cách nhấp vào **Delete**.
![Xóa DB Snapshots](/images/1-Worklog/Worklog_week1.4/Clean3.png)

**Xóa Tài nguyên Mạng (Network Resources)**

**Xóa các nhóm bảo mật (security groups):**
1. Mở bảng điều khiển Amazon VPC.
2. Chọn **Security Groups** từ ngăn điều hướng.
3. Chọn security group liên quan đến bài lab.
4. Chọn Actions, chọn **Delete security groups**, sau đó xác nhận.
![Xóa Security Groups](/images/1-Worklog/Worklog_week1.4/Clean4.png)

**Xóa NAT gateway:**
1. Trong bảng điều khiển VPC, chọn **NAT Gateways**.
2. Chọn NAT Gateway liên quan đến bài lab.
3. Chọn Actions, chọn **Delete NAT gateway**.
4. Xác nhận xóa.
![Xóa NAT Gateway](/images/1-Worklog/Worklog_week1.4/Clean5.png)

**Giải phóng địa chỉ Elastic IP:**
1. Mở bảng điều khiển Amazon EC2.
2. Chọn **Elastic IPs** từ ngăn điều hướng.
3. Chọn địa chỉ Elastic IP liên quan đến bài lab.
4. Từ menu Actions, chọn **Release Elastic IP addresses**.
5. Xác nhận bằng cách chọn **Release**.
![Giải phóng Elastic IP](/images/1-Worklog/Worklog_week1.4/Clean6.png)

**Xóa VPC:**
1. Trong bảng điều khiển VPC, chọn **Your VPCs**.
2. Chọn VPC mà bạn đã tạo cho bài lab này.
3. Từ menu Actions, chọn **Delete VPC**.
4. Trên trang xác nhận, nhập `delete` và chọn **Delete**.
![Xóa VPC](/images/1-Worklog/Worklog_week1.4/Clean7.png)

**Xóa Tài nguyên Tính toán (Compute Resources)**

**Chấm dứt (Terminate) các EC2 instances:**
1. Truy cập EC2 Management Console.
2. Chọn **Instances** từ ngăn điều hướng.
3. Chọn tất cả các EC2 Instances liên quan đến bài lab.
4. Nhấp vào trạng thái Instance (Instance state), sau đó chọn **Terminate instance**.
5. Xác nhận bằng cách nhấp vào **Terminate**.
![Chấm dứt EC2 Instances](/images/1-Worklog/Worklog_week1.4/Clean8.png)

{{% notice warning %}}
**Cảnh báo:** Việc chấm dứt tài nguyên là vĩnh viễn và không thể hoàn tác. Đảm bảo rằng bạn đã sao lưu mọi dữ liệu quan trọng trước khi tiến hành dọn dẹp.
{{% /notice %}}

{{% notice tip %}}
**Mẹo hay:** Để xác minh rằng tất cả các tài nguyên đã được xóa đúng cách, hãy kiểm tra bảng điều khiển Thanh toán AWS (AWS Billing dashboard) hoặc sử dụng AWS Cost Explorer để đảm bảo không có chi phí ngoài ý muốn nào xuất hiện sau khi dọn dẹp.
{{% /notice %}}


---

### 10. Cài đặt Git trên Amazon EC2 2023

Dưới đây là hướng dẫn cài đặt Git trên máy ảo Amazon EC2 chạy hệ điều hành Amazon Linux 2023 bằng các bước cơ bản.

**Cập nhật các gói hệ thống**
Đầu tiên, hãy cập nhật các gói hệ thống của bạn để đảm bảo bạn đang sử dụng phiên bản mới nhất:
```bash
sudo dnf update -y
```

**Tìm gói Git**
Sử dụng lệnh sau để tìm gói Git trong repository:
```bash
sudo dnf search git
```

**Cài đặt Git**
Khi bạn đã tìm thấy gói Git, bạn có thể cài đặt nó bằng lệnh sau:
```bash
sudo dnf install git -y
```

**Xác minh cài đặt Git**
Cuối cùng, hãy kiểm tra xem phiên bản Git đã được cài đặt thành công chưa:
```bash
git --version
```
Nếu bạn thấy phiên bản Git hiển thị, điều đó có nghĩa là quá trình cài đặt đã hoàn tất.

![Xác minh cài đặt Git](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance.png)

---

### 11. Cài đặt Node.js trên Amazon EC2 Linux 2023

Dưới đây là Bash script để cài đặt Node.js trên Amazon EC2 Linux:

```bash
#!/bin/bash

# Color for formatting
GREEN='\033[0;32m'
NC='\033[0m' # Colorless

# Check if NVM is installed
if ! command -v nvm &> /dev/null; then
  # Step 1: Install nvm
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
  source ~/.nvm/nvm.sh
fi

# Verify nvm installation
nvm --version

# Install the LTS version of Node.js
nvm install --lts

# Use the installed LTS version
nvm use --lts

# Verify Node.js and npm installation
node -v
npm -v

# Step 4: Create package.json file (if it doesn't exist yet)
if [ ! -f package.json ]; then
  npm init -y
  echo -e "${GREEN}Created file package.json.${NC}"
fi

# Step 5: Install necessary npm packages
echo -e "Installing required npm packages..."
npm install express dotenv express-handlebars body-parser mysql

# Step 6: Install nodemon as a development dependency
echo -e "Installing nodemon as a development dependency..."
npm install --save-dev nodemon
npm install -g nodemon

# Step 7: Add npm start script to package.json
if ! grep -q '"start":' package.json; then
  npm set-script start "index.js" # Replace "your-app.js" with your entry point file
  echo -e "${GREEN}Added npm start script to package.json.${NC}"
fi

echo -e "${GREEN}Installation completed. You can now start building and running your Node.js application using 'npm start'.${NC}"
```

![Kết quả cài đặt Node.js](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%201.png)

---

### 12. Tạo DB Instance trên AWS

Để tạo một DB Instance trên AWS, bạn có thể sử dụng AWS Management Console với tùy chọn Easy create được bật hoặc tắt. Khi Easy create được bật, bạn chỉ cần chỉ định loại DB engine, kích thước DB Instance và định danh DB Instance identifier. Easy create sử dụng các cài đặt mặc định cho các tùy chọn cấu hình khác. Khi Easy create bị tắt, bạn cần chỉ định nhiều tùy chọn cấu hình hơn khi tạo database, bao gồm các tùy chọn về tính khả dụng, bảo mật, sao lưu và bảo trì.

*Lưu ý: Trong quy trình dưới đây, tùy chọn Standard create được bật, và Easy create bị tắt. Quy trình này sử dụng MySQL làm ví dụ.*

Để tạo một DB Instance:

1. Đăng nhập vào AWS Management Console và mở Amazon RDS console tại [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).
2. Ở góc trên bên phải của Amazon RDS console, chọn khu vực (AWS region) nơi bạn muốn tạo DB Instance.
3. Trong ngăn điều hướng, chọn **Databases**.
4. Chọn **Create database**, và sau đó chọn **Standard create**.
   ![Tạo tiêu chuẩn](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%202.png)

5. Đối với **Engine type**, chọn MariaDB, Microsoft SQL Server, MySQL, Oracle, hoặc PostgreSQL. Trong ví dụ này, chúng ta sử dụng Microsoft SQL Server.
6. Đối với **Database management type**, nếu bạn đang sử dụng Oracle hoặc SQL Server, hãy chọn Amazon RDS hoặc Amazon RDS Custom.
7. Đối với **Edition**, nếu bạn đang sử dụng Oracle hoặc SQL Server, hãy chọn phiên bản DB engine mà bạn muốn sử dụng.
8. Đối với **Version**, chọn phiên bản engine.
   ![Chọn phiên bản](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%203.png)

9. Trong phần **Templates**, chọn một mẫu phù hợp với trường hợp sử dụng của bạn. Nếu bạn chọn **Production**, các tùy chọn sau sẽ được chọn sẵn ở bước tiếp theo:
   - Tùy chọn Multi-AZ failover
   - Tùy chọn lưu trữ Provisioned IOPS SSD (io1)
   - Tùy chọn Protection against deletion (bảo vệ chống xóa)
   Chúng tôi khuyến nghị sử dụng các tính năng này cho môi trường sản xuất.

10. Để nhập mật khẩu quản trị viên (master password), hãy làm theo các bước sau:
    - Trong phần **Settings**, mở Credential Settings.
    - Nếu bạn muốn chỉ định một mật khẩu, bỏ chọn hộp **Auto generate a password** nếu nó đã được chọn.
    - (Tùy chọn) Thay đổi giá trị **Master username**.
    - Nhập cùng một mật khẩu vào cả hai ô **Master password** và **Confirm password**.
    - (Tùy chọn) Thiết lập kết nối tới một tài nguyên tính toán (compute resource) cho DB Instance này.
    ![Thiết lập kết nối](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%204.png)

11. Bạn có thể cấu hình kết nối giữa một Amazon EC2 instance và DB Instance mới trong quá trình tạo DB Instance. 
12. Trong phần Connectivity dưới mục **VPC security group (firewall)**, nếu bạn chọn **Create new**, một VPC security group mới với quy tắc đăng nhập cho phép địa chỉ IP máy tính cục bộ của bạn truy cập vào cơ sở dữ liệu sẽ được tạo ra.
    ![VPC Security Group](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%205.png)

13. Đối với các phần còn lại, chỉ định các cài đặt DB Instance của bạn.
14. Chọn **Create database**.
    ![Nút Create Database](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%206.png)

15. Nếu bạn chọn sử dụng mật khẩu được tạo tự động, nút **View credential details** sẽ xuất hiện trên trang Databases. Để xem username và password cho DB Instance, hãy chọn View credential details.
16. Bên dưới mục **Databases**, chọn tên của DB Instance mới.
    ![Chọn DB Instance](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%207.png)

17. Trên RDS console, thông tin về DB Instance mới sẽ xuất hiện. DB Instance sẽ có trạng thái là **Creating** cho đến khi nó được tạo xong và sẵn sàng sử dụng. Khi trạng thái chuyển sang **Available**, bạn có thể kết nối với DB Instance.
    ![DB Instance khả dụng](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%208.png)

---

### 13. Kiểm tra RDS

Trên trang thông tin chi tiết của RDS instance, bạn có thể tìm thấy các thông tin liên quan đến kết nối như Endpoint, Port (Cổng), và Username.
Endpoint là địa chỉ URL hoặc IP mà bạn dùng để kết nối với cơ sở dữ liệu RDS.
![Chi tiết cấu hình RDS](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%209.png)

---

### 14. Xem Log và Event trên AWS RDS

Để theo dõi Log và Event trên Amazon RDS, bạn có thể thực hiện theo các bước sau:
1. Đăng nhập vào AWS Management Console.
2. Chọn dịch vụ **Amazon RDS** từ bảng điều khiển chính AWS.
3. Chọn RDS instance mà bạn muốn xem Log và Event.
4. Trong trang chi tiết instance, nhấp vào tab **Logs & events**.

Tại đây, bạn có thể xem các loại log khác nhau như:
- **Error log:** Ghi lại các lỗi xảy ra trên instance.
- **General log:** Ghi lại các hoạt động chung trên instance.
- **Slow query log:** Ghi lại các truy vấn bị chậm.
- **Event log:** Hiển thị các sự kiện quan trọng liên quan đến instance.

Bạn cũng có thể tùy chỉnh các cài đặt khi xem Log và Event tại đây, ví dụ như khoảng thời gian bạn muốn xem log hoặc thiết lập thông báo qua email cho các sự kiện quan trọng.
![Xem Log và Event](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%2010.png)

---

### 15. Xem thông tin Bảo trì và Sao lưu trên AWS RDS

**Xem thông tin bảo trì**
Để xem thông tin về bảo trì cho một DB instance trong RDS:
1. Trên trang quản lý DB instance, chuyển qua tab **Maintenance & backups**.
2. Tại đây, bạn sẽ thấy thông tin về lịch trình bảo trì, bao gồm thời gian tự động sao lưu và các tác vụ bảo trì định kỳ.

**Xem thông tin sao lưu**
1. Cũng tại tab **Maintenance & backups**.
2. Ở đây, bạn có thể xem thông tin chi tiết về các bản sao lưu tự động và sao lưu thủ công. Bạn cũng có thể tiến hành cấu hình và quản lý các thiết lập sao lưu.

![Bảo trì và Sao lưu](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%2011.png)


---

### 16. Triển khai Ứng dụng (Application Deployment)

**Triển khai Ứng dụng**
Để sao chép repository AWS-First-Cloud-Journey từ GitHub, bạn có thể sử dụng lệnh sau:
```bash
git clone https://github.com/AWS-First-Cloud-Journey/AWS-FCJ-Management
```
![Clone Repository](/images/1-Worklog/Worklog_week1.4/Application%20Deployment.png)

**Hướng dẫn cài đặt Node.js trên Amazon Linux 2023**
Dưới đây là một Bash script để cài đặt Node.js trên Amazon Linux. Vui lòng sao chép và thực thi các bước sau:
```bash
#!/bin/bash

# Các màu cho định dạng
GREEN='\033[0;32m'
NC='\033[0m' # Không màu

# Kiểm tra xem NVM đã được cài đặt chưa
if ! command -v nvm &> /dev/null; then
  # Bước 1: Cài đặt nvm
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
  source ~/.nvm/nvm.sh
fi

# Xác minh việc cài đặt nvm
nvm --version

# Cài đặt phiên bản LTS của Node.js
nvm install --lts

# Sử dụng phiên bản LTS đã cài đặt
nvm use --lts

# Xác minh cài đặt Node.js và npm
node -v
npm -v

# Bước 4: Tạo tệp package.json (nếu nó chưa tồn tại)
if [ ! -f package.json ]; then
  npm init -y
  echo -e "${GREEN}Đã tạo tệp package.json.${NC}"
fi

# Bước 5: Cài đặt các gói npm cần thiết
echo -e "Đang cài đặt các gói npm cần thiết..."
npm install express dotenv express-handlebars body-parser mysql

# Bước 6: Cài đặt nodemon như một phần phát triển
echo -e "Đang cài đặt nodemon như một phần phát triển..."
npm install --save-dev nodemon
npm install -g nodemon

# Bước 7: Thêm script npm start vào package.json
if ! grep -q '"start":' package.json; then
  npm set-script start "index.js"  # Thay thế "your-app.js" bằng tệp điểm nhập của bạn
  echo -e "${GREEN}Đã thêm script npm start vào package.json.${NC}"
fi

echo -e "${GREEN}Cài đặt hoàn tất. Bây giờ bạn có thể bắt đầu xây dựng và chạy ứng dụng Node.js của mình bằng 'npm start'.${NC}"
```
![Install Node.js](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%201.png)

**Cài đặt và Cấu hình MySQL Server**
Đây là một Bash script dùng để cài đặt và cấu hình máy chủ MySQL trên hệ thống. Script này thực hiện các bước sau:
- Thiết lập các biến với đường dẫn RPM của MySQL và thông tin cơ sở dữ liệu như địa chỉ RDS, tên cơ sở dữ liệu, tên người dùng và mật khẩu.
- Kiểm tra xem tệp RPM của kho lưu trữ cộng đồng MySQL đã tồn tại trong thư mục hiện tại chưa. Nếu chưa tồn tại, nó sẽ tải xuống RPM từ URL đã chỉ định.
- Cài đặt RPM của kho lưu trữ cộng đồng MySQL và MySQL Server.
- Khởi động MySQL server và cấu hình để tự động khởi động cùng hệ thống.
- Kiểm tra phiên bản MySQL đã cài đặt.
- Bảo mật máy chủ MySQL bằng lệnh `mysql_secure_installation`.
- Tạo hoặc cập nhật tệp `.env` với thông tin cơ sở dữ liệu (địa chỉ, tên cơ sở dữ liệu, tên người dùng và mật khẩu).
- Kết nối tới máy chủ MySQL bằng thông tin xác thực và bạn có thể thêm các lệnh SQL cụ thể tại đây.

*Lưu ý: Để thực thi đoạn mã này, bạn cần có quyền sudo và phải chắc chắn rằng bạn đã cung cấp đúng thông tin cơ sở dữ liệu (RDS Endpoint, tên cơ sở dữ liệu, tên người dùng và mật khẩu) trước khi chạy.*

```bash
#!/bin/bash

# Thiết lập các biến cho MySQL RPM và thông tin cơ sở dữ liệu
MYSQL_RPM_URL="https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm"
DB_HOST="RDS Endpoint"
DB_NAME="Tên cơ sở dữ liệu"
DB_USER="Tên người dùng cơ sở dữ liệu"
DB_PASS="Mật khẩu cơ sở dữ liệu"


# Kiểm tra xem MySQL Community repository RPM đã tồn tại chưa
if [ ! -f mysql80-community-release-el9-1.noarch.rpm ]; then
  sudo wget $MYSQL_RPM_URL
fi

# Cài đặt MySQL Community repository
sudo dnf install -y mysql80-community-release-el9-1.noarch.rpm

# Cài đặt MySQL server
sudo dnf install -y mysql-community-server

# Khởi động MySQL server
sudo systemctl start mysqld

# Bật MySQL để tự động khởi chạy
sudo systemctl enable mysqld

# Kiểm tra phiên bản MySQL
mysql -V

# Bảo mật máy chủ MySQL
sudo mysql_secure_installation

# Tạo hoặc cập nhật tệp .env với thông tin cơ sở dữ liệu
echo "DB_HOST=$DB_HOST" >> .env
echo "DB_NAME=$DB_NAME" >> .env
echo "DB_USER=$DB_USER" >> .env
echo "DB_PASS=$DB_PASS" >> .env

# Kết nối đến MySQL và tạo một CSDL mới (bạn có thể thêm các lệnh SQL cụ thể ở đây)
mysql -h $DB_HOST -P 3306 -u $DB_USER -p$DB_PASS
```
![Install MySQL](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%202.png)

**Tạo Cơ sở dữ liệu và Bảng trong AWS RDS**
Sau khi kết nối thành công với RDS (Relational Database Service) trên AWS, chúng ta có thể tạo một cơ sở dữ liệu mới và định nghĩa một bảng trong đó bằng cách sử dụng tập lệnh SQL sau.

**Tạo Cơ sở dữ liệu (Create Database)**
Đầu tiên, chúng ta sẽ tạo một cơ sở dữ liệu mới nếu nó chưa tồn tại. Sử dụng lệnh sau:
```sql
CREATE DATABASE IF NOT EXISTS first_cloud_users;
```
Lệnh này kiểm tra xem cơ sở dữ liệu “first_cloud_users” đã tồn tại hay chưa. Nếu chưa, nó sẽ tạo một cơ sở dữ liệu mới với tên “first_cloud_users”.

**Sử dụng Cơ sở dữ liệu (Using Database)**
Tiếp theo, chúng ta sử dụng cơ sở dữ liệu “first_cloud_users” bằng lệnh:
```sql
USE first_cloud_users;
```
Lệnh này cho biết rằng tất cả các lệnh SQL tiếp theo sẽ được thực thi trên cơ sở dữ liệu “first_cloud_users”.

**Tạo Bảng "user"**
Chúng ta đã tạo và sử dụng cơ sở dữ liệu. Bây giờ, chúng ta sẽ định nghĩa bảng “user” trong cơ sở dữ liệu này bằng tập lệnh SQL sau:
```sql
CREATE TABLE `user`
(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `first_name` VARCHAR(45) NOT NULL,
    `last_name` VARCHAR(45) NOT NULL,
    `email` VARCHAR(100) NOT NULL UNIQUE,
    `phone` VARCHAR(15) NOT NULL,
    `comments` TEXT NOT NULL,
    `status` ENUM('active', 'inactive') NOT NULL DEFAULT 'active'
) ENGINE = InnoDB;
```
Lệnh này định nghĩa cấu trúc của bảng “user” với các cột như “id”, “first_name”, “last_name”, “email”, “phone”, “comments”, và “status”. Các cột này đại diện cho thông tin của người dùng, trong đó cột “id” được đặt làm khóa chính (primary key) và tự động tăng.

**Thêm dữ liệu vào bảng "user"**
Cuối cùng, chúng ta có thể thêm dữ liệu vào bảng “user” bằng cách sử dụng lệnh `INSERT INTO`. Dưới đây là ví dụ thêm một số bản ghi vào bảng:
```sql
INSERT INTO `user`
(`first_name`, `last_name`, `email`, `phone`, `comments`, `status`)
VALUES
('Amanda', 'Nunes', 'anunes@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Alexander', 'Volkanovski', 'avolkanovski@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Khabib', 'Nurmagomedov', 'knurmagomedov@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Kamaru', 'Usman', 'kusman@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Israel', 'Adesanya', 'iadesanya@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Henry', 'Cejudo', 'hcejudo@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Valentina', 'Shevchenko', 'vshevchenko@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Tyron', 'Woodley', 'twoodley@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Rose', 'Namajunas', 'rnamajunas@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Tony', 'Ferguson', 'tferguson@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Jorge', 'Masvidal', 'jmasvidal@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Nate', 'Diaz', 'ndiaz@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Conor', 'McGregor', 'cmcGregor@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Cris', 'Cyborg', 'ccyborg@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Tecia', 'Torres', 'ttorres@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Ronda', 'Rousey', 'rrousey@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Holly', 'Holm', 'hholm@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Joanna', 'Jedrzejczyk', 'jjedrzejczyk@ufc.com', '012345 678910', 'I love AWS FCJ', 'active');
```
Lệnh này thêm các bản ghi người dùng vào bảng “user” với các thông tin như tên, email, số điện thoại, ghi chú và trạng thái mặc định là “active”.

Dưới đây là một số lệnh SQL để kiểm tra thông tin cơ sở dữ liệu trong một Hệ Quản Trị CSDL (DBMS) như MySQL hoặc PostgreSQL:

**Hiển thị danh sách tất cả các cơ sở dữ liệu:**
```sql
SHOW DATABASES;
```
Lệnh này sẽ liệt kê tất cả các cơ sở dữ liệu hiện có trong hệ thống.

**Chọn một cơ sở dữ liệu cụ thể để làm việc:**
```sql
USE database_name;
```
Lệnh này sẽ di chuyển bạn từ CSDL hiện tại sang một CSDL có tên là “database_name”. Sau khi sử dụng lệnh này, tất cả các lệnh SQL tiếp theo sẽ được áp dụng cho CSDL này.

**Hiển thị các bảng trong cơ sở dữ liệu hiện tại:**
```sql
SHOW TABLES;
```
Lệnh này sẽ liệt kê tất cả các bảng có trong CSDL hiện tại.

**Hiển thị cấu trúc của một bảng cụ thể:**
```sql
DESCRIBE table_name;
```
Lệnh này sẽ cung cấp cấu trúc của bảng có tên là “table_name”, bao gồm tên cột, kiểu dữ liệu và các thuộc tính khác của cột.

**Hiển thị thông tin về dung lượng cơ sở dữ liệu:**
```sql
SELECT table_schema "Tên CSDL", SUM(data_length + index_length) / 1024 / 1024 "Kích thước (MB)"
FROM information_schema.tables
GROUP BY table_schema;
```
Lệnh này sẽ hiển thị thông tin về dung lượng của các CSDL trong hệ thống, được tính bằng Megabytes (MB).
Hãy nhớ thay thế “database_name” và “table_name” bằng những tên cụ thể của CSDL và bảng mà bạn muốn kiểm tra.
![Các Lệnh SQL](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%203.png)

**Chạy Ứng dụng**
Sau khi bạn đã ở trong thư mục ứng dụng, hãy chạy lệnh sau để khởi động ứng dụng bằng `npm start`:
```bash
npm start
```
![npm start](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%204.png)

**Kiểm tra ứng dụng trên trình duyệt:**
Kiểm tra trạng thái của EC2 Instance: Đảm bảo EC2 Instance của bạn đang chạy và hoạt động bình thường.
Mở một trình duyệt web và nhập địa chỉ IP hoặc tên miền của EC2 Instance, theo sau là cổng 5000:
`http://<IP address or domain name>:5000`

Kết quả kiểm tra: Trình duyệt sẽ hiển thị ứng dụng của bạn nếu mọi thứ được cấu hình đúng đắn và EC2 Instance đang hoạt động.
![Kiểm tra Trình duyệt](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%205.png)

---

### 17. Giám sát và Khôi phục AWS RDS

**Giám sát AWS RDS**
Trên giao diện AWS RDS, bạn có thể thực hiện các bước sau để giám sát:
1. Chọn **Databases**.
2. Chọn DB instance mà bạn đã tạo.
3. Chọn **Monitoring**.
![Giám sát RDS](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%206.png)

**Xem Thông tin Sao lưu**
Để xem thông tin về các bản sao lưu của DB instance trong AWS RDS, hãy làm theo các bước sau:
1. Đăng nhập vào AWS Management Console.
2. Chọn dịch vụ **Amazon RDS** từ danh sách dịch vụ.
3. Trong bảng điều khiển RDS, chọn DB instance mà bạn muốn kiểm tra.
4. Trên trang quản lý DB instance, chuyển qua tab **Maintenance & backups**.
Tại đây, bạn có thể xem thông tin về các bản sao lưu tự động và thủ công. Bạn cũng có thể cấu hình và quản lý các thiết lập sao lưu.
![Sao lưu (Backups)](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%207.png)

**Xem thông tin Snapshot**
![Snapshot](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%208.png)

**Khôi phục Snapshot (Restore Snapshot)**
Chọn DB snapshot mà bạn muốn khôi phục. Trong phần Actions, chọn **Restore snapshot**.
![Khôi phục Snapshot](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%209.png)

Trên trang Restore snapshot, nhập tên cho DB instance mà bạn muốn khôi phục vào trường DB instance identifier. Chọn các cài đặt khác như kích thước bộ nhớ được cấp phát.
Cuối cùng, chọn **Restore DB instance**.
![Thiết lập Khôi phục](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%2010.png)

Hoàn tất quy trình khôi phục snapshot và kiểm tra lại cơ sở dữ liệu đã được khôi phục.
![Khôi phục Hoàn tất](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%2011.png)


---

### 18. Sao lưu và Khôi phục (Backup and Restore)

**Hiểu về Sao lưu và Khôi phục trên Amazon RDS**

{{% notice info %}}
**Thông tin:** Amazon RDS cung cấp tính năng sao lưu tự động và cho phép tạo snapshot thủ công để đảm bảo dữ liệu cơ sở dữ liệu của bạn được bảo vệ và có thể được khôi phục khi cần thiết. Những khả năng này rất cần thiết cho việc lập kế hoạch khắc phục thảm họa (disaster recovery) và duy trì tính liên tục của doanh nghiệp.
{{% /notice %}}

**Theo dõi trạng thái sao lưu trên Amazon RDS**
Để truy cập phần theo dõi sao lưu trong bảng điều khiển Amazon RDS:
1. Điều hướng đến phần **Databases** trong AWS Management Console.
2. Chọn DB instance đích của bạn.
3. Nhấp vào tab **Monitoring** để xem các số liệu hiệu suất.
![Giám sát AWS RDS](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore.png)

**Xem thông tin sao lưu**
Để xem chi tiết sao lưu cho Amazon RDS instance của bạn:
1. Đăng nhập vào AWS Management Console.
2. Chọn Amazon RDS từ menu dịch vụ.
3. Trong bảng điều khiển RDS, chọn DB instance của bạn.
4. Điều hướng đến tab **Maintenance & backups**.
Tại đây bạn có thể xem thông tin sao lưu tự động và thủ công cũng như cấu hình các cài đặt sao lưu.
![Sao lưu AWS RDS](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore%201.png)

**Quản lý Database Snapshots**
Xem các DB snapshot hiện có của bạn trong phần snapshots:
![Thông tin Snapshot](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore%202.png)

**Khôi phục từ một DB Snapshot**
Chọn DB snapshot bạn muốn sử dụng làm điểm khôi phục của mình:
1. Dưới menu thả xuống Actions, chọn **Restore snapshot**.
![Khôi phục Snapshot](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore%203.png)

**Cấu hình cho cơ sở dữ liệu đã được khôi phục:**
1. Cung cấp một định danh DB instance duy nhất (DB instance identifier) cho instance mới.
2. Chọn thông số kỹ thuật (instance specifications) phù hợp cho instance (compute, storage, v.v.).
3. Cấu hình mạng và cài đặt bảo mật.

{{% notice tip %}}
**Mẹo hay:** Khi khôi phục một cơ sở dữ liệu sản xuất, hãy cân nhắc việc khôi phục sang một instance class nhỏ hơn trước để thử nghiệm, sau đó mới mở rộng (scale up) khi cần thiết nhằm giảm thiểu chi phí trong quá trình xác thực.
{{% /notice %}}

**Bắt đầu quá trình khôi phục:**
1. Xem lại các cài đặt cấu hình của bạn.
2. Nhấp vào **Restore DB instance** để bắt đầu quá trình.

{{% notice warning %}}
**Cảnh báo:** Quá trình khôi phục tạo ra một database instance hoàn toàn mới với endpoint riêng. Bạn sẽ cần cập nhật các chuỗi kết nối của ứng dụng (connection strings) để trỏ đến instance mới này nếu định sử dụng nó cho môi trường sản xuất.
{{% /notice %}}

**Xác minh Cơ sở dữ liệu đã khôi phục**
Xác nhận khôi phục thành công:
1. Kiểm tra xem DB instance mới có xuất hiện trong bảng điều khiển RDS của bạn không.
2. Xác minh trạng thái hiển thị là "Available" khi quá trình khôi phục hoàn tất.
3. Kiểm tra kết nối và tính toàn vẹn của dữ liệu trước khi điều hướng lưu lượng truy cập sản xuất (production traffic) đến instance đã khôi phục.

{{% notice warning %}}
**Lưu ý bảo mật:** Hãy nhớ cấu hình các nhóm bảo mật (security groups) và các nhóm tham số (parameter groups) giống với instance ban đầu nếu bạn muốn giữ nguyên các kiểm soát truy cập và cấu hình của cơ sở dữ liệu.
{{% /notice %}}


---

### 19. Dọn dẹp tài nguyên (Clean up resources)

**Dọn dẹp Tài nguyên**

{{% notice info %}}
**Thông tin:** Sau khi hoàn thành bài thực hành, việc dọn dẹp tất cả các tài nguyên AWS là rất quan trọng để tránh các khoản phí phát sinh. Hãy làm theo các bước sau để xóa đúng cách tất cả các tài nguyên đã tạo trong buổi workshop này.
{{% /notice %}}

**Xóa Tài nguyên Cơ sở dữ liệu (Database Resources)**

**Xóa nhóm mạng con CSDL (DB subnet group):**
1. Điều hướng đến bảng điều khiển Amazon RDS.
2. Trong ngăn điều hướng, chọn **Subnet groups**.
3. Chọn DB subnet group liên quan đến bài lab.
4. Chọn **Delete**, sau đó xác nhận bằng cách chọn Delete trong cửa sổ xác nhận.
![Xóa DB Subnet Group](/images/1-Worklog/Worklog_week1.4/Clean.png)

**Xóa DB Instance:**
1. Truy cập RDS Management Console.
2. Ở thanh điều hướng bên trái, chọn **Databases**.
3. Chọn DB Instance liên quan đến bài lab.
4. Nhấp vào Actions, sau đó chọn **Delete**.
![Xóa DB Instance](/images/1-Worklog/Worklog_week1.4/Clean1.png)

5. Bỏ chọn mục *Create final snapshot?* và xác nhận rằng các bản sao lưu tự động sẽ không còn khả dụng nữa.
6. Nhập `delete me` vào trường xác nhận.
7. Nhấp vào **Delete**.
![Xác nhận xóa DB Instance](/images/1-Worklog/Worklog_week1.4/Clean2.png)

**Xóa DB Snapshots:**
1. Trong RDS Management Console, chọn **Snapshots** từ thanh điều hướng.
2. Chọn tất cả các snapshot liên quan đến bài lab.
3. Nhấp vào Actions, sau đó chọn **Delete snapshot**.
4. Xác nhận bằng cách nhấp vào **Delete**.
![Xóa DB Snapshots](/images/1-Worklog/Worklog_week1.4/Clean3.png)

**Xóa Tài nguyên Mạng (Network Resources)**

**Xóa các nhóm bảo mật (security groups):**
1. Mở bảng điều khiển Amazon VPC.
2. Chọn **Security Groups** từ ngăn điều hướng.
3. Chọn security group liên quan đến bài lab.
4. Chọn Actions, chọn **Delete security groups**, sau đó xác nhận.
![Xóa Security Groups](/images/1-Worklog/Worklog_week1.4/Clean4.png)

**Xóa NAT gateway:**
1. Trong bảng điều khiển VPC, chọn **NAT Gateways**.
2. Chọn NAT Gateway liên quan đến bài lab.
3. Chọn Actions, chọn **Delete NAT gateway**.
4. Xác nhận xóa.
![Xóa NAT Gateway](/images/1-Worklog/Worklog_week1.4/Clean5.png)

**Giải phóng địa chỉ Elastic IP:**
1. Mở bảng điều khiển Amazon EC2.
2. Chọn **Elastic IPs** từ ngăn điều hướng.
3. Chọn địa chỉ Elastic IP liên quan đến bài lab.
4. Từ menu Actions, chọn **Release Elastic IP addresses**.
5. Xác nhận bằng cách chọn **Release**.
![Giải phóng Elastic IP](/images/1-Worklog/Worklog_week1.4/Clean6.png)

**Xóa VPC:**
1. Trong bảng điều khiển VPC, chọn **Your VPCs**.
2. Chọn VPC mà bạn đã tạo cho bài lab này.
3. Từ menu Actions, chọn **Delete VPC**.
4. Trên trang xác nhận, nhập `delete` và chọn **Delete**.
![Xóa VPC](/images/1-Worklog/Worklog_week1.4/Clean7.png)

**Xóa Tài nguyên Tính toán (Compute Resources)**

**Chấm dứt (Terminate) các EC2 instances:**
1. Truy cập EC2 Management Console.
2. Chọn **Instances** từ ngăn điều hướng.
3. Chọn tất cả các EC2 Instances liên quan đến bài lab.
4. Nhấp vào trạng thái Instance (Instance state), sau đó chọn **Terminate instance**.
5. Xác nhận bằng cách nhấp vào **Terminate**.
![Chấm dứt EC2 Instances](/images/1-Worklog/Worklog_week1.4/Clean8.png)

{{% notice warning %}}
**Cảnh báo:** Việc chấm dứt tài nguyên là vĩnh viễn và không thể hoàn tác. Đảm bảo rằng bạn đã sao lưu mọi dữ liệu quan trọng trước khi tiến hành dọn dẹp.
{{% /notice %}}

{{% notice tip %}}
**Mẹo hay:** Để xác minh rằng tất cả các tài nguyên đã được xóa đúng cách, hãy kiểm tra bảng điều khiển Thanh toán AWS (AWS Billing dashboard) hoặc sử dụng AWS Cost Explorer để đảm bảo không có chi phí ngoài ý muốn nào xuất hiện sau khi dọn dẹp.
{{% /notice %}}

