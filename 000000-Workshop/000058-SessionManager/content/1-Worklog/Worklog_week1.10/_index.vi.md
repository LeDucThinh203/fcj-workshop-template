---
title: "Worklog Tuần 10"
date: 2026-06-22
weight: 10
chapter: false
pre: " <b> 1.10 </b> "
---

## Mục tiêu Tuần 10:
- Hiểu và cấu hình VPC Peering để kết nối hai mạng VPC riêng biệt, cấu hình định tuyến (routing) và kiểm tra phân giải DNS chéo (Cross-Peer DNS resolution).
- Thiết lập và kiểm chứng Network Access Control Lists (NACLs) để kiểm soát bảo mật không trạng thái (stateless firewall) ở mức subnet trong VPC.
- Tìm hiểu và triển khai AWS Transit Gateway (TGW) làm bộ định tuyến trung tâm để kết nối nhiều VPC theo mô hình Hub-and-Spoke, đơn giản hóa kiến trúc mạng quy mô lớn.

## Công việc thực hiện trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Học các khái niệm VPC Peering và Network Access Control Lists (NACLs)<br>- **Lab 19 (Phần 1)**: Thiết lập môi trường mạng cơ sở sử dụng CloudFormation, tạo Security Groups và EC2s | 22/06/2026 | 22/06/2026 | [VPC Peering Guide](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html)<br>[Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) |
| 3 | - **Lab 19 (Phần 2)**: Cấu hình Custom VPC Peering, tạo kết nối VPC Peering, cập nhật route tables và xác minh Cross-Peer DNS resolution | 23/06/2026 | 23/06/2026 | [VPC Peering DNS Support](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) |
| 4 | - **Lab 19 (Phần 3)**: Cấu hình Network ACLs (NACLs) ở mức subnet để chặn/cho phép lưu lượng ICMP/SSH, kiểm tra tính chất không trạng thái (stateless) và so sánh với Security Groups | 24/06/2026 | 24/06/2026 | [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) |
| 5 | - Học các khái niệm AWS Transit Gateway (TGW) và mô hình Hub-and-Spoke<br>- **Lab 20 (Phần 1)**: Thiết lập 3 VPC để minh họa sử dụng CloudFormation | 25/06/2026 | 25/06/2026 | [AWS Transit Gateway Guide](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) |
| 6 | - **Lab 20 (Phần 2)**: Tạo Transit Gateway và cấu hình gắn kết (attachments) cho các VPC | 26/06/2026 | 26/06/2026 | [Transit Gateway Attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html) |
| 7 - Chủ nhật | - **Lab 20 (Phần 3)**: Thiết lập Transit Gateway Route Tables, thêm Routes vào TGW Route Tables và xác minh kết nối mạng cross-VPC<br>- Tiến hành dọn dẹp sạch sẽ tài nguyên để tránh phát sinh chi phí | 27/06/2026 | 28/06/2026 | [TGW Route Tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html) |

## Thành tựu Tuần 10:
- **VPC Peering & Bảo mật**: Đã thiết lập thành công kết nối mạng riêng giữa hai VPC cô lập; áp dụng Network ACLs để kiểm soát các gói tin vào/ra và hiểu rõ hơn về hoạt động không giữ trạng thái (stateless) của NACL so với Security Groups giữ trạng thái (stateful).
- **Triển khai Transit Gateway**: Đã xây dựng mạng Hub-and-Spoke trung tâm kết nối 3 VPC bằng AWS Transit Gateway, loại bỏ nhu cầu cấu hình peering dạng full-mesh phức tạp, giúp quản trị và mở rộng hạ tầng mạng quy mô lớn dễ dàng hơn.
- **Tối ưu hóa chi phí**: Thực hiện dọn dẹp triệt để toàn bộ các tài nguyên (TGW, EC2, CloudFormation stacks) sau khi hoàn tất các bài lab để tránh phát sinh chi phí không mong muốn.

### Hình ảnh minh chứng:

1. **Khởi tạo ngăn xếp CloudFormation cho VPC Peering (Create_Stack)**
   ![Khởi tạo Stack](../../../images/1-Worklog/Worklog_week1.10/Create_Stack.png)
   *Mô tả chi tiết: Hình ảnh này ghi lại quá trình khởi tạo và triển khai thành công ngăn xếp (stack) AWS CloudFormation nhằm tự động hóa việc xây dựng môi trường mạng cơ sở cho bài thực hành VPC Peering. Việc sử dụng Cơ sở hạ tầng dưới dạng mã (IaC) giúp đảm bảo toàn bộ VPC, subnet, bảng định tuyến và máy chủ được tạo ra một cách đồng nhất và chính xác. Stack này tạo ra nền tảng mạng ban đầu gồm 'My VPC' và 'HG VPC', giúp tiết kiệm thời gian thiết lập thủ công và giảm thiểu sai sót.*

2. **Cấu hình Security Group cho My VPC (Create_MY VPC SG)**
   ![Cấu hình Security Group My VPC](../../../images/1-Worklog/Worklog_week1.10/Create_MY%20VPC%20SG.png)
   *Mô tả chi tiết: Cung cấp góc nhìn chi tiết về các quy tắc Security Group được áp dụng cho 'My VPC'. Security Group đóng vai trò là tường lửa ảo có trạng thái (stateful) bảo vệ ở cấp độ instance. Trong thiết lập này, các quy tắc inbound được tinh chỉnh cẩn thận để chỉ cho phép lưu lượng SSH (cổng 22) và ICMP (ping) từ các địa chỉ IP đáng tin cậy hoặc cụ thể là từ dải CIDR của VPC được kết nối (peered VPC). Điều này thể hiện nguyên tắc đặc quyền tối thiểu, đảm bảo an toàn tối đa cho máy chủ.*

3. **Cấu hình Security Group cho HG VPC (Create_HG VPC SG)**
   ![Cấu hình Security Group HG VPC](../../../images/1-Worklog/Worklog_week1.10/Create_HG%20VPC%20SG.png)
   *Mô tả chi tiết: Thể hiện cấu hình Security Group tương ứng cho các máy chủ đặt tại 'HG VPC' (mạng được kết nối). Tương tự như 'My VPC', tường lửa này được thiết lập để tiếp nhận lưu lượng truy cập đi vào một cách nghiêm ngặt, chỉ cho phép xuất phát từ dải mạng của 'My VPC'. Việc cấu hình các quy tắc đối xứng giữa hai VPC tạo ra một kênh giao tiếp hai chiều an toàn, là điều kiện tiên quyết để thực hiện các bài kiểm tra kết nối mạng (như lệnh ping) sau khi thiết lập peering.*

4. **Triển khai máy chủ EC2 (Create EC2)**
   ![Khởi tạo máy chủ EC2](../../../images/1-Worklog/Worklog_week1.10/Create%20EC2.png)
   *Mô tả chi tiết: Minh họa trạng thái hoạt động ổn định của các máy chủ ảo EC2 đã được khởi tạo thành công trên các VPC khác nhau (một máy chủ thuộc 'My VPC' và một thuộc 'HG VPC'). Những máy chủ này đóng vai trò là các điểm đầu cuối (endpoint) để tiến hành kiểm thử kết nối mạng. Việc xác nhận máy chủ đang chạy và được cấp phát đúng địa chỉ IP private trong subnet là bước chuẩn bị quan trọng nhất trước khi kiểm tra tính hợp lệ của đường truyền.*

5. **Thiết lập kết nối VPC Peering (MyVPC peering to HG VPC)**
   ![Kết nối VPC Peering](../../../images/1-Worklog/Worklog_week1.10/MyVPC%20peering%20to%20HG%20VPC.png)
   *Mô tả chi tiết: Làm nổi bật mục tiêu cốt lõi của bài lab — kết nối VPC Peering đang trong trạng thái hoạt động (Active) liên kết 'My VPC' với 'HG VPC'. VPC Peering cho phép định tuyến lưu lượng giữa hai mạng thông qua địa chỉ IP private IPv4 hoặc IPv6. Hình ảnh xác nhận yêu cầu kết nối đã được chấp thuận, qua đó hợp nhất ảo hai phân đoạn mạng tách biệt thành một không gian mạng riêng tư liên tục mà không cần dữ liệu phải đi qua môi trường internet công cộng.*

6. **Cập nhật bảng định tuyến cho Peering (route_table)**
   ![Cập nhật Route Table](../../../images/1-Worklog/Worklog_week1.10/route_table.png)
   *Mô tả chi tiết: Hiển thị những sửa đổi mang tính quyết định trên các bảng định tuyến (Route Tables) của VPC. Để máy chủ ở hai VPC có thể giao tiếp với nhau, bảng định tuyến của các subnet liên quan bắt buộc phải được cập nhật. Ảnh chụp màn hình cho thấy việc thêm một route cụ thể, trong đó đích đến (Destination) là dải CIDR của VPC đối diện, và mục tiêu (Target) là ID của kết nối VPC Peering (bắt đầu bằng pcx-...). Nếu thiếu bước này, gói tin sẽ bị rớt.*

7. **Kiểm chứng Network Access Control List - NACL (ALI)**
   ![Cấu hình NACL](../../../images/1-Worklog/Worklog_week1.10/ALI.png)
   *Mô tả chi tiết: Trình bày quá trình cấu hình và kiểm thử Network ACLs (NACLs). Khác với Security Group, NACL là tường lửa không trạng thái (stateless) hoạt động ở cấp độ subnet, yêu cầu phải định nghĩa rõ ràng cả quy tắc inbound và outbound. Hình ảnh minh chứng việc thay đổi một quy tắc NACL để chặn hoặc cho phép lưu lượng cụ thể (như ICMP hay SSH) sẽ ngay lập tức tác động đến toàn bộ subnet, cung cấp một lớp phòng thủ an ninh mạng bao quát và mạnh mẽ hơn.*

8. **Khởi tạo CloudFormation Template (Initialize CloudFormation Template)**
   ![Khởi tạo CloudFormation Template](../../../images/1-Worklog/Worklog_week1.10/Initialize%20CloudFormation%20Template.png)
   *Mô tả chi tiết: Hình ảnh này thể hiện bước đầu tiên trong việc thiết lập môi trường bằng cách sử dụng AWS CloudFormation. Việc chạy template sẽ tự động hóa quá trình tạo ra các VPC, Subnet, Route Table và các tài nguyên mạng cơ bản cần thiết cho bài thực hành Transit Gateway. Đây là phương pháp hiệu quả để xây dựng hạ tầng nhanh chóng và đồng nhất thay vì phải tạo từng tài nguyên thủ công qua console.*

9. **Tạo Key Pair bảo mật (Create_key_pair)**
   ![Tạo Key Pair](../../../images/1-Worklog/Worklog_week1.10/Create_key_pair.png)
   *Mô tả chi tiết: Quá trình tạo mới Amazon EC2 Key Pair được hiển thị trong ảnh này. Key Pair đóng vai trò xác thực quan trọng, cho phép quản trị viên truy cập an toàn (SSH) vào các máy chủ EC2 sẽ được khởi tạo trong các mạng VPC. Việc quản lý khóa bảo mật cẩn thận là nguyên tắc cơ bản trong bảo mật đám mây.*

10. **Tạo AWS Transit Gateway (Create Transit gateways)**
   ![Tạo Transit Gateway](../../../images/1-Worklog/Worklog_week1.10/Create%20Transit%20gateways.png)
   *Mô tả chi tiết: Hình ảnh ghi nhận việc khởi tạo thành công tài nguyên AWS Transit Gateway (TGW). TGW đóng vai trò là một hub trung tâm để kết nối nhiều mạng VPC và hệ thống mạng on-premises, giúp thay thế kiến trúc kết nối VPC Peering dạng lưới (full-mesh) phức tạp bằng mô hình hub-and-spoke đơn giản, dễ mở rộng và dễ quản lý tập trung.*

11. **Gắn kết VPC vào Transit Gateway (Create Transit gateway attachments)**
   ![Gắn kết Transit Gateway](../../../images/1-Worklog/Worklog_week1.10/Create%20Transit%20gateway%20attachments.png)
   *Mô tả chi tiết: Bước tiếp theo sau khi tạo TGW là gắn kết (attach) các mạng VPC cụ thể vào hub trung tâm này. Ảnh chụp màn hình minh họa quá trình tạo TGW Attachments, qua đó các VPC được liên kết vào Transit Gateway. Điều này cho phép lưu lượng mạng từ các subnet bên trong VPC có thể được định tuyến tới TGW để đi tới các mạng đích khác.*

12. **Cấu hình bảng định tuyến cho Transit Gateway (Create Transit gateway route tables)**
   ![Cấu hình Route Tables cho TGW](../../../images/1-Worklog/Worklog_week1.10/Create%20Transit%20gateway%20route%20tables.png)
   *Mô tả chi tiết: Hình ảnh này hiển thị việc tạo và cấu hình Transit Gateway Route Tables. Khác với Route Table của VPC, TGW Route Table kiểm soát cách thức gói tin được định tuyến sau khi đến Transit Gateway. Bằng cách sử dụng nhiều route table, người quản trị có thể thiết lập các chính sách định tuyến phức tạp (ví dụ: cách ly các VPC, hoặc cho phép một số VPC giao tiếp với nhau).*

13. **Cập nhật quy tắc định tuyến TGW (Create Transit gateway route tables 1)**
   ![Cập nhật Route Tables cho TGW](../../../images/1-Worklog/Worklog_week1.10/Create%20Transit%20gateway%20route%20tables%201.png)
   *Mô tả chi tiết: Chi tiết quá trình cập nhật các bản ghi định tuyến (routes) bên trong TGW Route Table. Việc khai báo đích đến (destination CIDR) và đính kèm (attachment target) tương ứng đảm bảo các gói tin biết chính xác đường đi để tới được VPC đích. Đây là bước quyết định để thiết lập khả năng giao tiếp xuyên mạng (cross-VPC).*

14. **Kiểm tra kết quả định tuyến mạng qua TGW (Transit Gateway Route result & result 1)**
   ![Kết quả định tuyến TGW](../../../images/1-Worklog/Worklog_week1.10/Transit%20Gateway%20Route%20result.png)
   ![Kết quả kết nối TGW](../../../images/1-Worklog/Worklog_week1.10/Transit%20Gateway%20Route%20result%201.png)
   *Mô tả chi tiết: Các hình ảnh này là bằng chứng xác nhận việc định tuyến thông qua Transit Gateway đã hoạt động chính xác. Kết quả ping hoặc trace route từ máy chủ ở VPC này tới máy chủ ở VPC khác thành công chứng minh rằng mạng lưới hub-and-spoke đã được thông suốt. Toàn bộ kiến trúc mạng từ Route Table của subnet tới Route Table của TGW đều đã được cấu hình đồng bộ.*

15. **Dọn dẹp tài nguyên để tối ưu chi phí (Clean)**
   ![Clean 1](../../../images/1-Worklog/Worklog_week1.10/clean%201.png)
   ![Clean 2](../../../images/1-Worklog/Worklog_week1.10/clean%202.png)
   ![Clean](../../../images/1-Worklog/Worklog_week1.10/Clean.png)
   *Mô tả chi tiết: Chuỗi hình ảnh cuối cùng này ghi nhận quá trình "dọn dẹp" (tear down) các tài nguyên thực hành bao gồm xóa Transit Gateway Attachments, xóa Transit Gateway, terminate EC2 instances và xóa CloudFormation stacks. Việc chủ động xóa các tài nguyên sau khi hoàn thành bài lab là thực hành cực kỳ quan trọng trên AWS để ngăn chặn các khoản phí phát sinh không mong muốn (cost optimization).*
