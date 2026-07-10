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
