---
title: "Nhật ký công việc"
date: 2026-04-27
weight: 1
pre : " <b> 1. </b> "
---


**Thông tin sinh viên:** Phạm Quốc Nhân  
**Chuyên ngành:** Mạng máy tính  
**Team:** First Cloud Journey

---

## Worklog theo từng tuần

Danh sách bên dưới dẫn tới các page worklog riêng. Mỗi tuần đều có ảnh minh họa và nội dung mô tả đúng theo bộ tài liệu Lab 07 mà bạn gửi.

- [Week 1.1 - AWS Budgets: template, hạn mức và cảnh báo email](./Worklog_week1.1/)
- [Week 1.2 - Tạo ngân sách tùy chỉnh cho toàn bộ dịch vụ AWS](./Worklog_week1.2/)
- [Week 1.3 - Usage Budget: kiểm soát mức sử dụng theo dịch vụ](./Worklog_week1.3/)

### Tuần 1: Làm quen với AWS và các dịch vụ cơ bản
* **Nội dung:** Tìm hiểu tổng quan về AWS Console, quản lý tài khoản IAM.
* **Công việc đã làm:**
    * Cấu hình AWS CLI trên môi trường cục bộ.
    * Thiết lập cấu trúc dự án báo cáo bằng Hugo.
    * Tìm hiểu về quyền hạn (Permissions) và chính sách (Policies) trong IAM.

### Tuần 2: Quản trị hệ thống với AWS Systems Manager (SSM)
* **Nội dung:** Tối ưu hóa việc truy cập Instance an toàn.
* **Công việc đã làm:**
    * Triển khai **Session Manager** thay thế cho SSH truyền thống (bảo mật port 22).
    * Cấu hình IAM Role cho EC2 để cấp quyền cho SSM Agent.
    * Thiết lập quản lý log tập trung với CloudWatch.

### Tuần 3: Networking và Security (Dự kiến)
* **Nội dung:** Xây dựng hạ tầng mạng ảo.
* **Công việc đã làm:**
    * Thiết lập VPC, cấu hình Subnets (Public/Private).
    * Cấu hình Internet Gateway và NAT Gateway cho traffic nội bộ.

### Tuần 4: Storage Management (Dự kiến)
* **Nội dung:** Quản lý lưu trữ đối tượng với S3.
* **Công việc đã làm:**
    * Khởi tạo S3 Buckets, cấu hình Access Control Lists (ACLs).
    * Thiết lập chính sách bảo mật cho dữ liệu nhạy cảm trên S3.

---

> **Ghi chú:** Nhật ký này sẽ được cập nhật liên tục theo tiến độ thực tập thực tế của dự án.