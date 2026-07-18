---
title: "Worklog Tuần 8"
date: 2026-05-13
weight: 8
chapter: false
pre: " <b> 1.8 </b> "
---

## Mục tiêu Tuần 8:
- Tìm hiểu cách quản lý danh tính và phân quyền truy cập nâng cao sử dụng IAM Groups, Users, Policies và Roles.
- Học và cấu hình mã hóa dữ liệu trên Amazon S3 sử dụng AWS Key Management Service (KMS), cấu hình chia sẻ dữ liệu được mã hóa an toàn giữa các tài khoản AWS.
- Cấu hình theo dõi và ghi nhật ký hoạt động hệ thống bằng AWS CloudTrail để phục vụ giám sát và kiểm toán bảo mật.
- Sử dụng Amazon Athena để thực hiện truy vấn phân tích log CloudTrail được lưu trữ trên S3 bucket bằng ngôn ngữ SQL.

## Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học lý thuyết về IAM Groups, Users, Policies, Roles nâng cao và nguyên tắc đặc quyền tối thiểu<br>- **Thực hành (Phần 1)**: Khởi tạo IAM Groups và Users phục vụ việc kiểm soát truy cập phân quyền | 08/06/2026 | 08/06/2026 | [IAM Policies Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) |
| 3 | - Học lý thuyết về mã hóa dữ liệu AWS KMS (KMS Keys, Key Policies)<br>- **Thực hành (Phần 2)**: Khởi tạo AWS Key Management Service (KMS) và cấu hình Key Policy | 09/06/2026 | 09/06/2026 | [AWS KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) |
| 4 | - **Thực hành (Phần 3)**: Tạo IAM Policy và IAM Role cho phép sử dụng khóa KMS<br>- Khởi tạo S3 bucket và tải tệp tin dữ liệu thử nghiệm lên, cấu hình mã hóa SSE-KMS | 10/06/2026 | 10/06/2026 | [Amazon S3 KMS Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) |
| 5 | - **Thực hành (Phần 4)**: Kiểm tra cấu hình và thực hiện chia sẻ dữ liệu đã mã hóa trên S3 bucket với tài khoản AWS khác thông qua khóa KMS | 11/06/2026 | 11/06/2026 | [S3 Cross-Account Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html) |
| 6 | - Học lý thuyết về theo dõi hệ thống với AWS CloudTrail<br>- **Thực hành (Phần 5)**: Khởi tạo CloudTrail trail, cấu hình lưu trữ log hoạt động hệ thống vào S3 bucket | 12/06/2026 | 12/06/2026 | [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) |
| 7 - Chủ nhật | - **Thực hành (Phần 6)**: Cấu hình Amazon Athena, kết nối nguồn dữ liệu log CloudTrail trên S3 và thực hiện các câu lệnh SQL để truy vấn log<br>- Tiến hành dọn dẹp sạch sẽ tài nguyên để tránh phát sinh chi phí | 13/06/2026 | 14/06/2026 | [Querying CloudTrail Logs with Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-cloudtrail-logs.html) |

## Thành tựu Tuần 8:
- **Quản trị truy cập (IAM)**: Thiết lập thành công phân quyền an toàn qua IAM Groups, Users, Policies và Roles đảm bảo tuân thủ nguyên tắc đặc quyền tối thiểu.
- **Mã hóa & Chia sẻ dữ liệu**: Cấu hình thành công AWS KMS để mã hóa S3 bucket, thiết lập Key Policy cho phép chia sẻ dữ liệu mã hóa an toàn với tài khoản AWS bên ngoài.
- **Giám sát & Kiểm toán (CloudTrail)**: Triển khai thành công AWS CloudTrail ghi nhận toàn bộ hoạt động API của tài khoản vào lưu trữ S3.
- **Phân tích log (Amazon Athena)**: Thành thạo việc sử dụng Amazon Athena viết truy vấn SQL trực tiếp trên S3 để phân tích log hoạt động CloudTrail phục vụ điều tra sự cố bảo mật.
- **Tối ưu chi phí**: Thực hiện dọn dẹp sạch sẽ tài nguyên thực hành để tránh phát sinh chi phí ngoài ý muốn.

### Hình ảnh minh chứng:

1. **Tạo IAM Group và User (Create Group and User)**
   ![Tạo IAM Group và User](/images/1-Worklog/Worklog_week1.8/Create%20Group%20and%20User.png)
   *Mô tả chi tiết: Ảnh ghi lại giao diện quản trị IAM sau khi tạo thành công IAM Group và IAM User. Việc phân chia người dùng vào các nhóm giúp quản trị viên dễ dàng quản lý quyền truy cập tập trung theo vai trò công việc.*

2. **Khởi tạo AWS Key Management Service (Create Key Management Service)**
   ![Tạo khóa KMS](/images/1-Worklog/Worklog_week1.8/Create%20Key%20Management%20Service.png)
   *Mô tả chi tiết: Giao diện tạo khóa mã hóa tùy chỉnh (Customer Managed Key) trong dịch vụ AWS KMS. Khóa này được sử dụng để mã hóa dữ liệu trên S3 và kiểm soát quyền giải mã thông qua Key Policy.*

3. **Cấu hình Policy và Role trong IAM (Create policy and role)**
   ![Cấu hình Policy và Role](/images/1-Worklog/Worklog_week1.8/Create%20policy%20and%20role.png)
   *Mô tả chi tiết: Thiết lập các IAM Policy chi tiết định nghĩa quyền sử dụng khóa KMS và IAM Role được gán các quyền này để cho phép các thực thể hoặc tài khoản khác thực hiện thao tác mã hóa/giải mã.*

4. **Tạo S3 Bucket và tải dữ liệu lên (Create and upload data bucket)**
   ![Tạo S3 Bucket và Upload](/images/1-Worklog/Worklog_week1.8/Create%20and%20upload%20data%20bucket.png)
   *Mô tả chi tiết: Tạo S3 bucket mới dùng để lưu trữ dữ liệu cần bảo vệ và thực hiện tải lên các tệp tin dữ liệu mẫu, chuẩn bị cho việc thử nghiệm cấu hình mã hóa.*

5. **Kiểm tra và chia sẻ dữ liệu mã hóa trên S3 (Test and share encrypted data on S3)**
   ![Chia sẻ dữ liệu mã hóa](/images/1-Worklog/Worklog_week1.8/Test%20and%20share%20encrypted%20data%20on%20S3.png)
   *Mô tả chi tiết: Xác minh việc mã hóa dữ liệu phía máy chủ (SSE-KMS) hoạt động chính xác trên S3 bucket và cấu hình chính sách chia sẻ chéo tài khoản, cho phép tài khoản AWS bên ngoài có thể đọc được dữ liệu này thông qua quyền hạn khóa KMS.*

6. **Khởi tạo AWS CloudTrail (Create CloudTrail)**
   ![Tạo CloudTrail](/images/1-Worklog/Worklog_week1.8/Create%20CloudTrail.png)
   *Mô tả chi tiết: Khởi tạo dịch vụ AWS CloudTrail để ghi lại nhật ký (logs) các cuộc gọi API và hoạt động diễn ra trong tài khoản AWS, hướng luồng log này lưu trữ vào một S3 bucket chuyên dụng.*

7. **Ghi log hoạt động vào CloudTrail (Logging to CloudTrail)**
   ![Ghi log CloudTrail](/images/1-Worklog/Worklog_week1.8/Logging%20to%20CloudTrail.png)
   *Mô tả chi tiết: Minh chứng các sự kiện hoạt động (events) đang được ghi nhận liên tục và xuất bản đầy đủ vào S3 bucket dưới dạng các tệp nén log CloudTrail.*

8. **Cấu hình Amazon Athena (Create Amazon Athena)**
   ![Cấu hình Amazon Athena](/images/1-Worklog/Worklog_week1.8/Create%20Amazon%20Athena.png)
   *Mô tả chi tiết: Thiết lập Amazon Athena bao gồm cấu hình thư mục lưu kết quả truy vấn (Query result location) trên S3 và khởi tạo cơ sở dữ liệu/bảng ánh xạ tới tệp tin log CloudTrail.*

9. **Truy vấn log bằng Athena SQL (Retrieve data with athena)**
   ![Truy vấn dữ liệu bằng Athena](/images/1-Worklog/Worklog_week1.8/Retrieve%20data%20with%20athena.png)
   *Mô tả chi tiết: Thực thi câu lệnh SQL SELECT trên giao diện Amazon Athena để truy vấn và trích xuất thông tin chi tiết từ log CloudTrail, ví dụ như tìm kiếm ai đã thực hiện thao tác gì trên tài nguyên tại thời điểm nào.*

10. **Dọn dẹp sạch tài nguyên thực hành (Clean)**
    ![Dọn dẹp tài nguyên](/images/1-Worklog/Worklog_week1.8/Clean.png)
    *Mô tả chi tiết: Tiến hành xóa bỏ tất cả tài nguyên đã tạo trong bài thực hành (KMS Keys, CloudTrail Trails, Athena tables, S3 Buckets, IAM Roles/Policies/Users/Groups) để đảm bảo không phát sinh chi phí duy trì dịch vụ sau khi kết thúc lab.*
