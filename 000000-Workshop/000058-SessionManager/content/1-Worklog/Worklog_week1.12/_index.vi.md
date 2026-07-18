---
title: "Nhật ký công việc Tuần 12"
date: 2026-07-06
weight: 12
chapter: false
pre: " <b> 1.12 </b> "
---

## Mục tiêu Tuần 12:
- **Tổng kết & Đánh giá:** Tổng hợp, đánh giá và kiểm tra lại toàn bộ quá trình nghiên cứu lý thuyết trong suốt chặng đường 12 tuần của chương trình First Cloud Journey.
- **Nghiên cứu quản trị hệ thống:** Tìm hiểu lý thuyết về bộ công cụ AWS Systems Manager (SSM) bao gồm Fleet Manager, Patch Manager và Run Command để quản lý máy chủ Windows Server từ xa.
- **Nghiên cứu bảo mật nâng cao:** Tìm hiểu lý thuyết về IAM Tag-based Access Control cho EC2 và cách thiết lập IAM Permissions Boundaries để giới hạn quyền tối đa của IAM Entities.
- **Nghiên cứu giám sát hệ thống:** Tìm hiểu kiến trúc của công cụ giám sát mã nguồn mở Grafana và cách xây dựng dashboard theo dõi tài nguyên trực quan.
- **Xác minh chuyên cần:** Đối soát và hoàn thiện lịch sử chấm công chuyên cần của toàn bộ khóa học 12 tuần.

## Công việc cần thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Nghiên cứu lý thuyết về IAM Tag-based Access Control đối với tài nguyên EC2 | 06/07/2026 | 06/07/2026 | <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html" target="_blank">AWS IAM Tagging</a> |
| 3 | - Tìm hiểu lý thuyết về hệ thống giám sát mã nguồn mở Grafana và dashboard theo dõi trực quan | 07/07/2026 | 07/07/2026 | <a href="https://grafana.com/docs/grafana/latest/" target="_blank">Grafana User Guide</a> |
| 4 | - Nghiên cứu lý thuyết về IAM Permissions Boundaries và cách giới hạn quyền tối đa của IAM Entities | 08/07/2026 | 08/07/2026 | <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html" target="_blank">AWS Permissions Boundaries</a> |
| 5 | - Nghiên cứu tài liệu giới thiệu về bộ dịch vụ AWS Systems Manager (SSM) bao gồm Fleet Manager, Patch Manager và Run Command | 09/07/2026 | 09/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html" target="_blank">AWS Systems Manager User Guide</a> |
| 6 | - Tìm hiểu kiến trúc quản lý máy chủ Windows Server trên AWS và quy trình tích hợp quản trị qua SSM Agent | 10/07/2026 | 10/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html" target="_blank">SSM Agent on Windows Server</a> |
| 7 - Chủ nhật | - Đánh giá và tổng kết lại toàn bộ chặng đường nghiên cứu lý thuyết 12 tuần, đối soát nhật ký chuyên cần và hoàn thiện báo cáo tổng hợp | 11/07/2026 | 12/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html" target="_blank">SSM Patch Manager</a><br><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html" target="_blank">SSM Run Command</a> |

## Thành tựu Tuần 12:

### 1. Tổng hợp lộ trình nghiên cứu của 12 tuần:
Trải qua 12 tuần của chương trình **First Cloud Journey**, lộ trình tích lũy kiến thức đã được hoàn thành xuất sắc với các cột mốc quan trọng:
* **Tuần 1 - 2 (Làm quen & Kiểm soát chi phí):** Làm quen hệ thống AWS, nghiên cứu lý thuyết S3/EC2 và thiết lập chốt chặn tài chính an toàn bằng **AWS Budgets**.
* **Tuần 3 - 4 (Hạ tầng & Cơ sở dữ liệu):** Nghiên cứu máy chủ ảo EC2 (Public/Private Subnets), phân quyền chi tiết IAM và kết nối ứng dụng Node.js đến cơ sở dữ liệu **Amazon RDS** (cấu hình Multi-AZ, Backups và Snapshots).
* **Tuần 5 - 6 (Tính sẵn sàng cao & Giám sát):** Tìm hiểu Auto Scaling Groups, Load Balancers, tối ưu phân phối qua **CloudFront** và **Route 53**. Đồng thời nghiên cứu hệ thống cảnh báo qua **Amazon CloudWatch** (Metrics, Alarms, Logs Insights).
* **Tuần 7 - 8 (Tự động hóa & Kiểm toán bảo mật):** Tự động hóa hạ tầng qua **AWS CLI**, cấu hình **AWS Backup** lập lịch sao lưu tự động. Nâng cao bảo mật dữ liệu với **AWS S3 SSE-KMS**, kiểm toán hoạt động qua **AWS CloudTrail** và phân tích logs bằng **Amazon Athena**.
* **Tuần 9 - 11 (Vận hành Serverless & Mạng doanh nghiệp):** Tự động hóa bật/tắt EC2 bằng **AWS Lambda** & **EventBridge** tích hợp thông báo về Slack (ChatOps). Thiết lập mạng kết nối đa VPC qua **VPC Peering**, **Transit Gateway** và kết nối hybrid on-premises qua **AWS Storage Gateway (NFS)**.
* **Tuần 12 (Tổng kết & Quản trị hệ thống):** Nghiên cứu lý thuyết quản trị hệ thống qua **AWS Systems Manager (SSM)** (Patch Manager, Run Command) và bảo mật nâng cao qua **Permissions Boundaries**, **Tag-based Access Control** kết hợp hệ thống giám sát **Grafana**.

### 2. Kết quả thực hiện trong Tuần 12:
* Tuần 12 tập trung hoàn toàn vào nghiên cứu tài liệu, tổng kết lý thuyết hệ thống và tổng hợp báo cáo. Không thực hiện thao tác khởi tạo hay thay đổi cấu hình tài nguyên trực tiếp trên cloud.
* Hoàn thiện đối soát lịch sử chuyên cần và check-in thực tế của toàn bộ khóa học.

---

### Hình ảnh minh chứng tổng kết chuyên cần:

1. **Lịch sử chuyên cần khóa học - Phần 1 (Attendance History 1)**
   ![Lịch sử chuyên cần 1](/images/1-Worklog/Worklog_week1.12/Attendance%20history%201.png)
   *Mô tả chi tiết: Hình ảnh ghi lại nhật ký chuyên cần của giai đoạn đầu khóa học trên cổng thông tin đào tạo, xác minh sự tham gia học tập lý thuyết, sync nhóm và hoàn thành đầy đủ nhiệm vụ theo lịch trình đề ra.*

2. **Lịch sử chuyên cần khóa học - Phần 2 (Attendance History 2)**
   ![Lịch sử chuyên cần 2](/images/1-Worklog/Worklog_week1.12/Attendance%20history%202.png)
   *Mô tả chi tiết: Minh chứng tiếp tục quá trình ghi nhận chuyên cần giai đoạn tiếp theo, phản ánh tính kỷ luật cao và nỗ lực học tập không ngừng của học viên trong suốt quá trình đào tạo.*

3. **Lịch sử chuyên cần tổng thể toàn khóa (Attendance History)**
   ![Lịch sử chuyên cần tổng thể](/images/1-Worklog/Worklog_week1.12/Attendance%20history.png)
   *Mô tả chi tiết: Bảng thống kê tổng hợp lịch sử chuyên cần cuối kỳ của học viên, ghi nhận việc hoàn thành 100% thời lượng đào tạo và tham gia đầy đủ các buổi thảo luận, hướng dẫn trực tiếp.*

4. **Hình ảnh check-in thực tế tại văn phòng đào tạo (Attendance history picture checkin)**
   ![Checkin thực tế](/images/1-Worklog/Worklog_week1.12/Attendance%20history%20picture%20checkin.png)
   *Mô tả chi tiết: Ảnh chụp check-in trực tiếp của học viên trong buổi học tập và làm việc nhóm tại văn phòng thực tập, minh chứng cho việc thực hiện đúng giờ giấc làm việc thực tế, giao lưu và phối hợp chặt chẽ cùng các thành viên trong đội ngũ First Cloud Journey.*
