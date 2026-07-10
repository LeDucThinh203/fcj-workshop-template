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
