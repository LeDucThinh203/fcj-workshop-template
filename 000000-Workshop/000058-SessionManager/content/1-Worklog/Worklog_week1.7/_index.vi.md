---
title: "Worklog Tuần 7"
date: 2026-05-13
weight: 7
chapter: false
pre: " <b> 1.7 </b> "
---

## Mục tiêu Tuần 7:
- Kết nối và làm quen với các thành viên của First Cloud Journey.
- Hiểu các dịch vụ AWS cơ bản, cách sử dụng console & CLI.

## Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học AWS CLI & Cài đặt<br> - Xem tài nguyên qua CLI<br> - AWS CLI với Amazon S3 và Amazon SNS | 01/06/2026 | 01/06/2026 | [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)<br> [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/) |
| 3 | - AWS CLI với IAM và VPC (VPC, Internet Gateway)<br> - Thực hành tạo EC2 qua AWS CLI | 02/06/2026 | 02/06/2026 | [AWS CLI for EC2 & VPC](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2.html)<br> [AWS CLI for IAM](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-iam.html) |
| 4 | - Học AWS Organizations<br> - Tạo các tài khoản thành viên, cấu hình Organizational Unit (OU) và mời các Tài khoản AWS | 03/06/2026 | 03/06/2026 | [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)<br> [Creating account in Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) |
| 5 | - Cấu hình truy cập Tài khoản Thành viên qua CLI<br> - Cấu hình kiểm soát truy cập theo thời gian & Customer Managed Policies<br> - Hiểu IAM Identity Center Identity Store APIs | 04/06/2026 | 04/06/2026 | [AWS IAM Identity Center Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)<br> [Identity Store APIs](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/Welcome.html) |
| 6 | - Học dịch vụ AWS Backup<br> - Chuẩn bị môi trường: Tạo S3 Bucket & Triển khai cơ sở hạ tầng sao lưu | 05/06/2026 | 05/06/2026 | [What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)<br> [Backup S3 with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html) |
| 7 - Chủ nhật | - Thiết lập Backup plan & cấu hình thông báo<br> - Thực hiện các hoạt động Khôi phục kiểm tra<br> - Dọn dẹp tài nguyên để tránh chi phí | 06/06/2026 | 07/06/2026 | [Creating backup plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)<br> [Restoring a backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) |

## Thành tựu Tuần 7:

### Hình ảnh minh chứng:

1. **Khởi tạo hạ tầng (Deploy infrastructure)**
   ![Deploy infrastructure](../../../images/1-Worklog/Worklog_week1.7/Deloy%20infrastructure.png)
   *Mô tả chi tiết: Quá trình triển khai hạ tầng cơ sở cho bài thực hành sử dụng AWS CloudFormation. Các tài nguyên cần thiết như EC2 instance, EBS volume, hoặc các thiết lập mạng cơ bản được tự động hóa khởi tạo. Đây là bước chuẩn bị quan trọng để có tài nguyên thực tế nhằm kiểm thử tính năng sao lưu (backup) và phục hồi (restore).*

2. **Tạo thư mục S3 (Create s3 folder)**
   ![Create S3 Folder](../../../images/1-Worklog/Worklog_week1.7/Create%20s3%20folder.png)
   *Mô tả chi tiết: Khởi tạo thư mục hoặc bucket trên Amazon S3. S3 thường được sử dụng làm nơi lưu trữ an toàn, bền bỉ và tiết kiệm chi phí cho các bản sao lưu (backup vault/storage) từ AWS Backup hoặc các dịch vụ khác. Việc thiết lập cấu trúc lưu trữ chuẩn xác đảm bảo dữ liệu backup được tổ chức tốt và dễ dàng truy xuất khi cần.*

3. **Cấu hình kế hoạch sao lưu (Create Backup plans)**
   ![Create Backup plans](../../../images/1-Worklog/Worklog_week1.7/Create%20Backup%20plans.png)
   *Mô tả chi tiết: Cấu hình AWS Backup plan. Bước này thiết lập các quy tắc tự động hóa quá trình sao lưu, bao gồm tần suất sao lưu (ví dụ: hàng ngày, hàng tuần), thời gian lưu trữ (retention period) và cửa sổ sao lưu (backup window). Quản lý sao lưu tự động giúp doanh nghiệp tuân thủ các quy định về an toàn dữ liệu mà không tốn công sức vận hành thủ công.*

4. **Kiểm tra phục hồi dữ liệu (Test Restore)**
   ![Test Restore](../../../images/1-Worklog/Worklog_week1.7/Test%20Restore.png)
   *Mô tả chi tiết: Thực hiện quy trình phục hồi (restore) dữ liệu từ một bản sao lưu (recovery point) đã tạo trước đó. Đây là bước kiểm chứng quan trọng nhất trong bất kỳ chiến lược sao lưu nào, đảm bảo rằng trong trường hợp xảy ra sự cố mất mát dữ liệu hoặc hỏng hóc hệ thống, dữ liệu có thể được khôi phục nguyên vẹn và hệ thống có thể hoạt động trở lại bình thường.*

5. **Dọn dẹp tài nguyên (Clean up resources)**
   ![Clean up resources](../../../images/1-Worklog/Worklog_week1.7/Clean%20up%20resources.png)
   *Mô tả chi tiết: Xóa bỏ các tài nguyên AWS đã được tạo ra trong suốt quá trình thực hành (như EC2, S3, Backup plans, CloudFormation stack). Việc dọn dẹp cẩn thận sau khi hoàn thành lab là thao tác bắt buộc để tối ưu hóa chi phí (Cost Optimization), đảm bảo tài khoản không phải chịu các khoản phí duy trì cho những tài nguyên không còn sử dụng.*
