---
title: "Nhật ký Tuần 2"
date: 2026-05-13
weight: 2
chapter: false
pre: " <b> 1.2 </b> "
---

## Mục tiêu Tuần 2:
- Tìm hiểu về các công cụ quản lý chi phí và lập hóa đơn trên AWS (AWS Billing & Cost Management).
- Nắm vững vai trò và cách cấu hình AWS Budgets để kiểm soát chi tiêu đám mây.
- Thực hành thiết lập hạn mức ngân sách và cấu hình cảnh báo ngưỡng chi phí tự động.

## Công việc cần thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học tổng quan về quản lý chi phí trên AWS:<br>  + Các công cụ AWS Billing<br>  + Cách tính toán chi phí dịch vụ cơ bản | 27/04/2026 | 27/04/2026 | [AWS Billing Overview](https://docs.aws.amazon.com/billing/latest/userguide/billing-whatis.html) |
| 3 | - Tìm hiểu cơ chế hoạt động của AWS Budgets:<br>  + Khái niệm Cost budget và Usage budget<br>  + Ngưỡng cảnh báo chi phí thực tế và dự báo | 28/04/2026 | 28/04/2026 | [AWS Budgets Guide](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) |
| 4 | - Nghiên cứu thiết lập kế hoạch ngân sách cho tài khoản Free Tier để tránh phát sinh chi phí ngoài ý muốn. | 29/04/2026 | 29/04/2026 | [AWS Free Tier Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) |
| 5 | - Học cách cấu hình nhận cảnh báo ngân sách qua email và các kênh thông báo tự động (Amazon SNS). | 30/04/2026 | 30/04/2026 | [AWS Budgets Alerts](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-alerts.html) |
| 6 | - **Thực hành (Phần 1):** Khởi tạo ngân sách chi phí hàng tháng (My Monthly Cost Budget) với hạn mức cảnh báo $100. | 01/05/2026 | 01/05/2026 | [Creating a Cost Budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create-cost.html) |
| 7 - Chủ nhật | - **Thực hành (Phần 2):** Khởi tạo thêm ngân sách dự phòng $200 (My-200$-budget) và ngân sách mức độ sử dụng tài nguyên (Cost budget). Xác minh trạng thái và hoạt động cảnh báo. | 02/05/2026 | 03/05/2026 | [Monitoring Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-viewing.html) |

## Thành tựu Tuần 2:
### Lý thuyết:
- Hiểu rõ mô hình tính phí của AWS, các yếu tố ảnh hưởng trực tiếp đến hóa đơn và cách sử dụng AWS Budgets làm chốt chặn bảo mật tài chính.
- Nắm vững sự khác nhau giữa Cost Budgets (ngân sách chi phí) và Usage Budgets (ngân sách lượng tài nguyên tiêu thụ).

### Thực hành:
- Khởi tạo thành công 3 ngân sách khác nhau phục vụ theo dõi chi tiêu đa chiều trên AWS Console.
- Cấu hình hoàn chỉnh ngưỡng cảnh báo tự động gửi email khi chi phí thực tế đạt 80% hoặc chi phí dự báo vượt hạn mức định trước.

### Hình ảnh minh chứng:

1. **Cấu hình AWS Budgets - Khởi tạo ngân sách (Create budget)**
   ![Cấu hình Lab07 - Bước 1](/images/1-Worklog/Worklog_week1.2/Module%2001-Lab07-01.png)
   *Mô tả chi tiết: Màn hình quản lý Budgets Overview hiển thị hai ngân sách đầu tiên đã được tạo thành công: `My Monthly Cost Budget` (ngân sách theo dõi chi tiêu hàng tháng hạn mức $100) và `My-200$-budget` (ngân sách hạn mức $200), tất cả đều ở trạng thái hoạt động bình thường (Healthy) và chưa vượt ngưỡng cảnh báo.*

2. **Cấu hình AWS Budgets - Thêm ngân sách chi phí (Add cost budget)**
   ![Cấu hình Lab07 - Bước 2](/images/1-Worklog/Worklog_week1.2/Module%2001-Lab07-02.png)
   *Mô tả chi tiết: Minh chứng hệ thống thông báo tạo thành công ngân sách thứ ba mang tên `Cost budget` với hạn mức $200, nâng tổng số ngân sách giám sát lên 3 nhằm phân loại và kiểm soát chi tiêu chi tiết theo các mục tiêu sử dụng khác nhau.*

3. **Cấu hình AWS Budgets - Xem chi tiết thông số ngân sách (Budget details)**
   ![Cấu hình Lab07 - Bước 3](/images/1-Worklog/Worklog_week1.2/Module%2001-Lab07-03.png)
   *Mô tả chi tiết: Giao diện hiển thị chi tiết thông số của ngân sách `Cost budget` vừa tạo, bao gồm trạng thái sức khỏe ổn định (Healthy), lượng tài nguyên đã sử dụng (Usage amount 1.440 Hrs), chu kỳ giám sát hàng tháng (Monthly) và ngày bắt đầu áp dụng cấu hình (2026-05-01).*
