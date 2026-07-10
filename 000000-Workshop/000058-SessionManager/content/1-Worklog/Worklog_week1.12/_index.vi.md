
---
title: "Nhật ký công việc Tuần 12"
date: 2026-07-06
weight: 12
chapter: false
pre: " <b> 1.12 </b> "
---

## Mục tiêu Tuần 12:
- Hiểu và cấu hình IAM Tag-based Access Control cho tài nguyên EC2.
- Tìm hiểu về công cụ giám sát mã nguồn mở Grafana và cách tạo dashboard cơ bản.
- Thiết lập IAM Permissions Boundaries để ủy quyền và giới hạn truy cập tối đa của IAM Entities.
- Sử dụng bộ công cụ AWS Systems Manager (SSM) để quản lý cơ sở hạ tầng máy chủ từ xa, bao gồm Fleet Manager, cập nhật OS tự động qua Patch Manager và thực thi script từ xa qua Run Command.

## Công việc cần thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học IAM Tag-based Access Control<br>- Đọc hướng dẫn và cấu hình IAM Tags để kiểm soát truy cập vào tài nguyên EC2 | 06/07/2026 | 06/07/2026 | <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html" target="_blank">AWS IAM Tagging</a> |
| 3 | - Học cơ bản về giám sát Grafana<br>- Đọc và hiểu các khái niệm Grafana và tạo Dashboard cơ bản | 07/07/2026 | 07/07/2026 | <a href="https://grafana.com/docs/grafana/latest/" target="_blank">Grafana User Guide</a> |
| 4 | - Học IAM Permission Boundary<br>- Cấu hình permission boundaries để giới hạn quyền tối đa của IAM Entities | 08/07/2026 | 08/07/2026 | <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html" target="_blank">AWS Permissions Boundaries</a> |
| 5 | - Học các khái niệm AWS Systems Manager (SSM)<br>- Đọc giới thiệu về SSM, Fleet Manager, Patch Manager và Run Command | 09/07/2026 | 09/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html" target="_blank">AWS Systems Manager User Guide</a> |
| 6 | - Thiết lập cơ sở hạ tầng mạng và IAM Roles cho SSM<br>- Tạo VPC `windows-lab-ssm`, Internet Gateway, 2 Subnets<br>- Tạo IAM Role/Instance Profile với chính sách `AmazonSSMManagedInstanceCore`<br>- Khởi chạy 2 máy ảo EC2 Windows Server gắn với IAM Role | 10/07/2026 | 10/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html" target="_blank">SSM Agent on Windows Server</a> |
| 7 - Chủ nhật | - Thực hiện cập nhật patch và chạy lệnh từ xa qua SSM<br>- Sử dụng Patch Manager để quét lỗ hổng và cài đặt cập nhật OS tự động<br>- Sử dụng Run Command để chạy PowerShell `net user` từ xa và lưu log vào S3<br>- Thực hiện dọn dẹp tất cả tài nguyên AWS để tránh các chi phí không mong muốn | 11/07/2026 | 12/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html" target="_blank">SSM Patch Manager</a><br><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html" target="_blank">SSM Run Command</a> |

## Thành tựu Tuần 12:
