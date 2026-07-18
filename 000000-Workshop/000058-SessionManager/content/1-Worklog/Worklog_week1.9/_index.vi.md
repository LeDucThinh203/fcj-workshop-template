---
title: "Worklog Tuần 9"
date: 2026-06-15
weight: 9
chapter: false
pre: " <b> 1.9 </b> "
---

## Mục tiêu Tuần 9:
- Tìm hiểu cách tự động hóa vận hành serverless sử dụng AWS Lambda và Amazon EventBridge để khởi động và dừng EC2 instance tự động dựa trên lịch trình.
- Tìm hiểu cách gắn thẻ quản lý tài nguyên (Resource Tags), quản lý nhóm tài nguyên (Resource Groups) và lọc tài nguyên trên AWS.
- Cấu hình tích hợp thông báo vận hành (ChatOps) gửi trạng thái hoạt động của Lambda tới kênh Slack thông qua Incoming Webhooks.
- Kích hoạt và cấu hình AWS Security Hub để đánh giá posture bảo mật tài khoản (CSPM - Cloud Security Posture Management).

## Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học lý thuyết về AWS Lambda và EventBridge scheduler<br>- Tìm hiểu về thiết lập Tags, Tag Editor và Resource Groups trên AWS | 15/06/2026 | 15/06/2026 | [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/) |
| 3 | - **Thực hành (Phần 1)**: Cấu hình mạng VPC, Subnets, Security Groups và khởi chạy các EC2 Instances để thử nghiệm<br>- Tạo IAM Role cho Lambda với các quyền truy cập EC2 và CloudWatch Logs | 16/06/2026 | 16/06/2026 | [AWS Lambda IAM Permissions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) |
| 4 | - **Thực hành (Phần 2)**: Viết code Python (boto3) trong AWS Lambda để tự động hóa dừng (Stop) các máy ảo EC2 có gắn thẻ tag chỉ định | 17/06/2026 | 17/06/2026 | [Boto3 EC2 Client Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html) |
| 5 | - **Thực hành (Phần 3)**: Viết code Python (boto3) trong AWS Lambda để tự động hóa khởi động (Start) các máy ảo EC2<br>- Cấu hình Incoming Webhooks trên Slack để làm endpoint nhận tin nhắn | 18/06/2026 | 18/06/2026 | [Slack Incoming Webhooks Guide](https://api.slack.com/messaging/webhooks) |
| 6 | - **Thực hành (Phần 4)**: Tích hợp mã nguồn gửi tin nhắn thông báo tự động từ Lambda tới Slack và kiểm tra kết quả | 19/06/2026 | 19/06/2026 | [Sending Slack Messages with Lambda](https://api.slack.com/messaging/webhooks) |
| 7 - Chủ nhật | - **Thực hành (Phần 5)**: Kích hoạt AWS Security Hub CSPM, phân tích điểm số bảo mật của tài khoản và tiến hành dọn dẹp sạch sẽ tài nguyên sau thực hành | 20/06/2026 | 21/06/2026 | [AWS Security Hub User Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) |

## Thành tựu Tuần 9:
- **Tự động hóa Serverless**: Xây dựng thành công giải pháp tự động hóa bằng AWS Lambda (Python boto3) kết hợp EventBridge Scheduler để dừng các EC2 instances thử nghiệm vào buổi tối và bật lại vào ban ngày nhằm tối ưu chi phí.
- **Tích hợp ChatOps**: Cấu hình thành công Slack Incoming Webhook để Lambda gửi tin nhắn cảnh báo trạng thái chạy/dừng máy ảo theo thời gian thực trực tiếp về kênh vận hành Slack.
- **Quản trị tài nguyên**: Thành thạo việc gán thẻ (Tags) cho tài nguyên, sử dụng Tag Editor để chỉnh sửa tag hàng loạt và gom nhóm quản lý qua AWS Resource Groups.
- **Bảo mật và Tối ưu**: Kích hoạt thành công AWS Security Hub để đánh giá điểm số tuân thủ bảo mật CSPM, đồng thời dọn dẹp triệt để các tài nguyên (EC2, Lambda, Security Hub, Logs) để tránh phát sinh chi phí ngoài ý muốn.

### Hình ảnh minh chứng:

1. **Khởi tạo VPC (Create VPC)**
   ![CreateVPC](../../../images/1-Worklog/Worklog_week1.9/CreateVPC.png)
   *Mô tả chi tiết: Hình ảnh minh họa bảng điều khiển (console) của AWS khi tiến hành tạo một Virtual Private Cloud (VPC) mới. Quá trình này bao gồm việc xác định dải địa chỉ IPv4 (CIDR block), tạo các mạng con (Subnets) ở các Availability Zones khác nhau để tăng tính sẵn sàng. Đồng thời, thiết lập Internet Gateway (IGW) và Route Tables giúp định tuyến lưu lượng truy cập từ Internet vào Public Subnet một cách an toàn.*

2. **Tạo Security Group (Create Security Group)**
   ![Create Security Group](../../../images/1-Worklog/Worklog_week1.9/Create%20Security%20Group.png)
   *Mô tả chi tiết: Đây là bước thiết lập "bức tường lửa" ảo (Virtual Firewall) cấp độ instance. Hình ảnh cho thấy việc cấu hình các quy tắc Inbound (Inbound rules) để mở các cổng mạng (ports) cần thiết, ví dụ như cổng 22 (SSH) để quản trị máy chủ từ xa, hoặc cổng 80/443 (HTTP/HTTPS) cho web. Chỉ những địa chỉ IP hoặc dải mạng được chỉ định mới có thể kết nối vào tài nguyên.*

3. **Khởi chạy EC2 (Create Ec2)**
   ![Create Ec2](../../../images/1-Worklog/Worklog_week1.9/Create%20Ec2.png)
   *Mô tả chi tiết: Hình ảnh chụp lại màn hình Launch Instance thành công. Máy ảo (EC2) đã được cấp phát với thông số cấu hình cụ thể (AMI, Instance Type, Key Pair). Máy ảo này sẽ được đặt trong VPC và Subnet đã tạo trước đó, đồng thời gắn Security Group phù hợp. Đây là tài nguyên tính toán cốt lõi để chạy ứng dụng và sẽ được dùng để kiểm thử tính năng bật/tắt tự động bằng Lambda.*

4. **Tạo IAM Role cho Lambda (Create Role for lamda)**
   ![Create Role for lamda](../../../images/1-Worklog/Worklog_week1.9/Create%20Role%20for%20lamda.png)
   *Mô tả chi tiết: Hình ảnh hiển thị giao diện IAM (Identity and Access Management) nơi một Role mới đang được tạo dành riêng cho dịch vụ AWS Lambda. Role này được đính kèm các chính sách (Policies) cho phép hàm Lambda có quyền gọi các API của dịch vụ EC2 (như `ec2:StartInstances`, `ec2:StopInstances`) và quyền ghi log hoạt động (CloudWatch Logs) để thuận tiện cho việc debug sau này.*

5. **Tạo hàm Lambda Stop Instance (Function stop instance)**
   ![Function stop instance](../../../images/1-Worklog/Worklog_week1.9/Function%20stop%20instance.png)
   *Mô tả chi tiết: Giao diện chi tiết của dịch vụ AWS Lambda với hàm có chức năng tự động dừng (Stop) các máy EC2. Mã nguồn (code) của hàm, thường được viết bằng Python (Boto3), sẽ quét các EC2 có gắn thẻ (Tag) cụ thể (ví dụ: `Environment=Dev`) và thực thi lệnh dừng máy. Việc này giúp tiết kiệm chi phí tính toán đáng kể trong những khung giờ ngoài giờ hành chính hoặc ban đêm.*

6. **Tạo hàm Lambda Start Instance (Function start instance)**
   ![Function start instance](../../../images/1-Worklog/Worklog_week1.9/Function%20start%20instance.png)
   *Mô tả chi tiết: Tương tự như hàm Stop, hình ảnh này minh họa cấu hình của hàm Lambda dùng để tự động khởi động (Start) máy ảo. Được kết hợp với Amazon EventBridge để lên lịch biểu (cron job), hàm này sẽ chạy vào đầu giờ sáng làm việc (ví dụ 8h00 sáng) nhằm đảm bảo các hệ thống luôn sẵn sàng phục vụ khi nhân viên bắt đầu ngày làm việc.*

7. **Tạo máy ảo EC2 với Tags (Create EC2 Instance with tag)**
   ![Create EC2 Instance with tag](../../../images/1-Worklog/Worklog_week1.9/Create%20EC2%20Instance%20with%20tag.png)
   *Mô tả chi tiết: Minh chứng cho thấy quá trình cấu hình nâng cao khi tạo máy ảo EC2 mới. Ở mục Tags, chúng ta thiết lập các cặp Key-Value (ví dụ: `Project = FirstCloudJourney`, `Environment = Test`). Việc gắn thẻ ngay từ lúc khởi tạo giúp hệ thống tự động hóa (như hàm Lambda vừa tạo) nhận diện đúng mục tiêu để thao tác, tránh ảnh hưởng đến các máy chủ Production.*

8. **Gắn Tag cho EC2 có sẵn (EC2 add tag)**
   ![EC2 add tag](../../../images/1-Worklog/Worklog_week1.9/EC2%20add%20tag.png)
   *Mô tả chi tiết: Hình ảnh chụp tab Tags trong chi tiết của một máy EC2 đang chạy. Thông qua console, chúng ta bổ sung hoặc chỉnh sửa các thẻ (Tags) cho những máy chủ đã được tạo trước đó. Điều này rất quan trọng để đồng bộ hóa quản lý, phục vụ cho việc kiểm soát chi phí (Cost Allocation Tags) và áp dụng các chính sách phân quyền chi tiết (ABAC).*

9. **Quản lý Tags và Lọc tài nguyên (Managing Tags and Filter resources by tag)**
   ![Managing Tags and Filter resources by tag](../../../images/1-Worklog/Worklog_week1.9/Managing%20Tags%20and%20Filter%20resources%20by%20tag.png)
   *Mô tả chi tiết: Giao diện Tag Editor hoặc AWS Resource Groups được sử dụng để tìm kiếm hàng loạt tài nguyên. Thay vì phải vào từng dịch vụ, hình ảnh cho thấy cách lọc ra tất cả các tài nguyên (EC2, VPC, Lambda, v.v.) có chung một giá trị Tag nhất định. Tính năng này giúp người quản trị dễ dàng theo dõi và thống kê tổng thể kiến trúc hệ thống.*

10. **Tạo Resource Group (Create a Resource Group)**
    ![Create a Resource Group](../../../images/1-Worklog/Worklog_week1.9/Create%20a%20Resource%20Group.png)
    *Mô tả chi tiết: Hình ảnh hiển thị bảng điều khiển tạo mới một AWS Resource Group. Bằng cách sử dụng các truy vấn dựa trên Tags, hệ thống sẽ gom nhóm các tài nguyên phân tán lại thành một tập hợp logic. Từ Resource Group này, người dùng có thể thực hiện các thao tác quản trị hàng loạt (bulk actions) thông qua AWS Systems Manager một cách nhanh chóng và an toàn.*

11. **Tích hợp Incoming Web-hooks Slack (Incoming Web-hooks slack)**
    ![Incoming Web-hooks slack](../../../images/1-Worklog/Worklog_week1.9/Incoming%20Web-hooks%20slack.png)
    *Mô tả chi tiết: Giao diện cấu hình ứng dụng Slack để tạo một Incoming Webhook URL. Webhook này được sử dụng như một điểm cuối (endpoint) để nhận dữ liệu. Trong bài lab, khi các hàm Lambda thực thi việc Start/Stop máy ảo, nó sẽ gửi một payload chứa thông báo kết quả (thành công/thất bại) qua webhook này để hiển thị trực tiếp lên kênh chat (channel) của đội ngũ vận hành.*

12. **Kiểm tra kết quả (Check Result)**
    ![Check Result](../../../images/1-Worklog/Worklog_week1.9/Check%20Result.png)
    *Mô tả chi tiết: Bằng chứng cụ thể cho thấy hệ thống tự động hóa hoạt động hoàn hảo. Hình ảnh chụp lại màn hình ứng dụng Slack với các tin nhắn cảnh báo (alerts) tự động được gửi từ AWS. Người quản trị có thể ngay lập tức biết được trạng thái của các máy ảo (đã tắt hay vừa bật lên) mà không cần phải đăng nhập vào AWS Console, thực hiện đúng triết lý ChatOps.*

13. **Kích hoạt AWS Security Hub CSPM (Enable AWS Security Hub CSPM)**
    ![Enable AWS Security Hub CSPM](../../../images/1-Worklog/Worklog_week1.9/Enable%20AWS%20Security%20Hub%20CSPM.png)
    *Mô tả chi tiết: Tổng quan bảng điều khiển (Dashboard) của AWS Security Hub. Tính năng Cloud Security Posture Management (CSPM) đã được bật, tiến hành quét toàn bộ tài khoản dựa trên các tiêu chuẩn bảo mật chuẩn ngành (như AWS Foundational Security Best Practices). Giao diện hiển thị biểu đồ điểm số tuân thủ (Compliance Score) và liệt kê các lỗ hổng hoặc cấu hình sai cần khắc phục.*

14. **Dọn dẹp Security Hub (Clean Security Hub)**
    ![Clean Security Hub](../../../images/1-Worklog/Worklog_week1.9/Clean%20Security%20Hub.png)
    *Mô tả chi tiết: Hình ảnh minh chứng cho thao tác vô hiệu hóa (Disable) và xóa dữ liệu của AWS Security Hub trong phần Settings. Vì Security Hub tính phí dựa trên số lượng kiểm tra bảo mật (security checks), việc tắt dịch vụ này sau khi hoàn thành bài thực hành là rất cần thiết để đảm bảo không bị trừ tiền ngoài ý muốn trong tương lai.*

15. **Dọn dẹp Tags (Clean Tags)**
    ![Clean Tags](../../../images/1-Worklog/Worklog_week1.9/Clean%20Tags.png)
    *Mô tả chi tiết: Minh họa việc sử dụng Tag Editor để xóa hàng loạt các thẻ (Tags) đã tạo ra trên nhiều tài nguyên. Bước làm sạch này giúp môi trường AWS giữ được sự ngăn nắp, tránh việc các thẻ rác (stale tags) làm rối loạn các công cụ báo cáo chi phí hoặc làm ảnh hưởng tới các bộ quy tắc tự động hóa khác trong hệ thống.*

16. **Dọn dẹp EC2, Lambda và CloudWatch (Clean Ec2 and lamda and cloudwatch)**
    ![Clean Ec2 and lamda and cloudwatch](../../../images/1-Worklog/Worklog_week1.9/Clean%20Ec2%20and%20lamda%20and%20cloudwatch.png)
    *Mô tả chi tiết: Bước cuối cùng dọn dẹp môi trường (Terminate/Delete resources). Hình ảnh cho thấy lệnh xóa các máy ảo EC2, các hàm Lambda không còn sử dụng, và quan trọng là xóa các nhóm nhật ký (Log Groups) trong CloudWatch. Log Groups nếu để lại lâu ngày có thể phát sinh phí lưu trữ (Storage cost), do đó việc xóa triệt để đảm bảo tối ưu hóa chi phí (Cost Optimization) tối đa.*
