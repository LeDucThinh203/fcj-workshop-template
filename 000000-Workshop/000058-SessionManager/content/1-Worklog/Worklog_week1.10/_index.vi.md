---
title: "Worklog Tuần 10"
date: 2026-06-22
weight: 10
chapter: false
pre: " <b> 1.10 </b> "
---

## Mục tiêu Tuần 10:
- Hiểu và cấu hình VPC Peering để kết nối hai mạng VPC riêng biệt, cấu hình routing và thiết lập Network ACLs (NACLs) để kiểm soát bảo mật stateless ở mức subnet.
- Học và triển khai AWS Transit Gateway (TGW) để kết nối nhiều VPC theo mô hình Hub-and-Spoke, đơn giản hóa kiến trúc mạng quy mô lớn.
- Thực hiện tự động hóa hoạt động serverless sử dụng AWS Lambda và Amazon EventBridge để tự động start/stop EC2 instances dựa trên lịch trình và chuyển hướng log/alarm thực thi đến Slack.

## Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học các khái niệm VPC Peering và Network Access Control Lists (NACLs)<br>- **Lab 19 (Part 1)**: Thiết lập môi trường mạng cơ sở sử dụng Cloudformation, tạo Security Groups và EC2s | 22/06/2026 | 22/06/2026 | <a href="https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html" target="_blank">VPC Peering Guide</a><br><a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html" target="_blank">Network ACLs</a> |
| 3 | - **Lab 19 (Part 2)**: Cấu hình Custom VPC Peering, tạo kết nối VPC Peering, cập nhật route tables và xác minh Cross-Peer DNS resolution | 23/06/2026 | 23/06/2026 | <a href="https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html" target="_blank">VPC Peering DNS Support</a> |
| 4 | - Học các khái niệm AWS Transit Gateway (TGW)<br>- **Lab 20 (Part 1)**: Thiết lập 3 VPC để minh họa, tạo Transit Gateway và cấu hình VPC attachments | 24/06/2026 | 24/06/2026 | <a href="https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html" target="_blank">AWS Transit Gateway Guide</a> |
| 5 | - **Lab 20 (Part 2)**: Thiết lập Transit Gateway Route Tables, thêm Routes vào TGW Route Tables và xác minh kết nối mạng cross-VPC | 25/06/2026 | 25/06/2026 | <a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html" target="_blank">TGW Route Tables</a> |
| 6 | - Học dịch vụ tính toán serverless AWS Lambda và EventBridge scheduling<br>- **Lab 22 (Part 1)**: Thiết lập IAM workshop, gán thẻ cho EC2 instances và cấu hình IAM Role cho Lambda | 26/06/2026 | 26/06/2026 | <a href="https://docs.aws.amazon.com/lambda/latest/dg/welcome.html" target="_blank">AWS Lambda Developer Guide</a><br><a href="https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/" target="_blank">Slack Webhooks</a> |
| 7 - Chủ nhật | - **Lab 22 (Part 2)**: Triển khai mã Python Lambda (boto3) để start/stop EC2s và gửi cảnh báo đến Slack, lên lịch thông qua EventBridge và dọn dẹp tài nguyên | 27/06/2026 | 28/06/2026 | <a href="https://docs.aws.amazon.com/boto3/latest/reference/services/ec2.html" target="_blank">Boto3 EC2 Client</a><br><a href="https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html" target="_blank">EventBridge Scheduler</a> |

## Thành tựu Tuần 10:
- **VPC Peering & Bảo mật**: Đã thiết lập thành công kết nối mạng riêng giữa hai VPC cô lập; áp dụng Network ACLs để kiểm soát các gói tin vào/ra và hiểu rõ hơn về hoạt động không giữ trạng thái (stateless) của NACL so với Security Groups giữ trạng thái (stateful).
- **Triển khai Transit Gateway**: Đã xây dựng mạng Hub-and-Spoke trung tâm kết nối 3 VPC bằng AWS Transit Gateway, loại bỏ nhu cầu cấu hình peering dạng full-mesh phức tạp.
- **Tự động hóa Serverless**: Đã xây dựng giải pháp quản lý serverless bằng AWS Lambda (Python boto3) đọc các tag tài nguyên của instance, dừng các máy chủ phát triển vào ban đêm và khởi động trước giờ làm việc.
- **Tích hợp ChatOps**: Đã tích hợp cảnh báo AWS Lambda với thông báo trên kênh Slack bằng Incoming Webhooks để báo cáo trạng thái hoạt động theo thời gian thực.
- **Hoạt động theo lịch trình**: Đã cấu hình Amazon EventBridge Scheduler (các trình kích hoạt cron) để tự động gọi các hàm Lambda vào các thời điểm cụ thể.

### Hình ảnh minh chứng:

1. **Khởi tạo ngăn xếp CloudFormation cho VPC Peering (Create_Stack)**
   ![Khởi tạo Stack](/images/1-Worklog/Worklog_week1.10/Create_Stack.png)
   *Mô tả chi tiết: Hình ảnh này ghi lại quá trình khởi tạo và triển khai thành công ngăn xếp (stack) AWS CloudFormation nhằm tự động hóa việc xây dựng môi trường mạng cơ sở cho bài thực hành VPC Peering. Việc sử dụng Cơ sở hạ tầng dưới dạng mã (IaC) giúp đảm bảo toàn bộ VPC, subnet, bảng định tuyến và máy chủ được tạo ra một cách đồng nhất và chính xác. Stack này tạo ra nền tảng mạng ban đầu gồm 'My VPC' và 'HG VPC', giúp tiết kiệm thời gian thiết lập thủ công và giảm thiểu sai sót.*

2. **Cấu hình Security Group cho My VPC (Create_MY VPC SG)**
   ![Cấu hình Security Group My VPC](/images/1-Worklog/Worklog_week1.10/Create_MY%20VPC%20SG.png)
   *Mô tả chi tiết: Cung cấp góc nhìn chi tiết về các quy tắc Security Group được áp dụng cho 'My VPC'. Security Group đóng vai trò là tường lửa ảo có trạng thái (stateful) bảo vệ ở cấp độ instance. Trong thiết lập này, các quy tắc inbound được tinh chỉnh cẩn thận để chỉ cho phép lưu lượng SSH (cổng 22) và ICMP (ping) từ các địa chỉ IP đáng tin cậy hoặc cụ thể là từ dải CIDR của VPC được kết nối (peered VPC). Điều này thể hiện nguyên tắc đặc quyền tối thiểu, đảm bảo an toàn tối đa cho máy chủ.*

3. **Cấu hình Security Group cho HG VPC (Create_HG VPC SG)**
   ![Cấu hình Security Group HG VPC](/images/1-Worklog/Worklog_week1.10/Create_HG%20VPC%20SG.png)
   *Mô tả chi tiết: Thể hiện cấu hình Security Group tương ứng cho các máy chủ đặt tại 'HG VPC' (mạng được kết nối). Tương tự như 'My VPC', tường lửa này được thiết lập để tiếp nhận lưu lượng truy cập đi vào một cách nghiêm ngặt, chỉ cho phép xuất phát từ dải mạng của 'My VPC'. Việc cấu hình các quy tắc đối xứng giữa hai VPC tạo ra một kênh giao tiếp hai chiều an toàn, là điều kiện tiên quyết để thực hiện các bài kiểm tra kết nối mạng (như lệnh ping) sau khi thiết lập peering.*

4. **Triển khai máy chủ EC2 (Create EC2)**
   ![Khởi tạo máy chủ EC2](/images/1-Worklog/Worklog_week1.10/Create%20EC2.png)
   *Mô tả chi tiết: Minh họa trạng thái hoạt động ổn định của các máy chủ ảo EC2 đã được khởi tạo thành công trên các VPC khác nhau (một máy chủ thuộc 'My VPC' và một thuộc 'HG VPC'). Những máy chủ này đóng vai trò là các điểm đầu cuối (endpoint) để tiến hành kiểm thử kết nối mạng. Việc xác nhận máy chủ đang chạy và được cấp phát đúng địa chỉ IP private trong subnet là bước chuẩn bị quan trọng nhất trước khi kiểm tra tính hợp lệ của đường truyền.*

5. **Thiết lập kết nối VPC Peering (MyVPC peering to HG VPC)**
   ![Kết nối VPC Peering](/images/1-Worklog/Worklog_week1.10/MyVPC%20peering%20to%20HG%20VPC.png)
   *Mô tả chi tiết: Làm nổi bật mục tiêu cốt lõi của bài lab — kết nối VPC Peering đang trong trạng thái hoạt động (Active) liên kết 'My VPC' với 'HG VPC'. VPC Peering cho phép định tuyến lưu lượng giữa hai mạng thông qua địa chỉ IP private IPv4 hoặc IPv6. Hình ảnh xác nhận yêu cầu kết nối đã được chấp thuận, qua đó hợp nhất ảo hai phân đoạn mạng tách biệt thành một không gian mạng riêng tư liên tục mà không cần dữ liệu phải đi qua môi trường internet công cộng.*

6. **Cập nhật bảng định tuyến cho Peering (route_table)**
   ![Cập nhật Route Table](/images/1-Worklog/Worklog_week1.10/route_table.png)
   *Mô tả chi tiết: Hiển thị những sửa đổi mang tính quyết định trên các bảng định tuyến (Route Tables) của VPC. Để máy chủ ở hai VPC có thể giao tiếp với nhau, bảng định tuyến của các subnet liên quan bắt buộc phải được cập nhật. Ảnh chụp màn hình cho thấy việc thêm một route cụ thể, trong đó đích đến (Destination) là dải CIDR của VPC đối diện, và mục tiêu (Target) là ID của kết nối VPC Peering (bắt đầu bằng pcx-...). Nếu thiếu bước này, gói tin sẽ bị rớt.*

7. **Kiểm chứng Network Access Control List - NACL (ALI)**
   ![Cấu hình NACL](/images/1-Worklog/Worklog_week1.10/ALI.png)
   *Mô tả chi tiết: Trình bày quá trình cấu hình và kiểm thử Network ACLs (NACLs). Khác với Security Group, NACL là tường lửa không trạng thái (stateless) hoạt động ở cấp độ subnet, yêu cầu phải định nghĩa rõ ràng cả quy tắc inbound và outbound. Hình ảnh minh chứng việc thay đổi một quy tắc NACL để chặn hoặc cho phép lưu lượng cụ thể (như ICMP hay SSH) sẽ ngay lập tức tác động đến toàn bộ subnet, cung cấp một lớp phòng thủ an ninh mạng bao quát và mạnh mẽ hơn.*
