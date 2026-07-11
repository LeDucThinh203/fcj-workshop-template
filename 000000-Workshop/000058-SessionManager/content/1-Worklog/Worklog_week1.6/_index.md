---
title: "Week 6 Worklog"
date: 2026-05-13
weight: 6
chapter: false
pre: " <b> 1.6 </b> "
---

## Week 6 Objectives:
- Understand AWS Cloud Trail and managed reports here in AWS Support.
- Deploy a Hybrid DNS integration on premises with AWS using Route 53 Resolver and Microsoft AD.

## Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn Amazon CloudWatch & prepare environment<br> - CloudWatch Metrics:<br>  + View Metrics<br>  + Perform search operations<br>  + Perform math operations<br>  + Create dynamic labels | 25/05/2026 | 25/05/2026 | [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)<br> [Using Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) |
| 3 | - CloudWatch Logs:<br>  + View CloudWatch Logs<br>  + CloudWatch Logs Insights<br>  + CloudWatch Metric Filter<br>  + Create CloudWatch Alarms<br>  + Create CloudWatch Dashboards<br>  + Clean up resources | 26/05/2026 | 26/05/2026 | [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)<br> [Creating CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html)<br> [CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) |
| 4 | - Learn about AWS Support Plans: Basic, Developer, Business, Enterprise On-Ramp, Enterprise<br> - Access AWS Support Console<br> - Learn about Support Request types (Account & billing, Technical)<br> - Change support plan | 27/05/2026 | 27/05/2026 | [AWS Support Plans](https://aws.amazon.com/vi/premiumsupport/plans/)<br> [Getting started with AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html) |
| 5 | - Create a Support Request (Support Case)<br> - Select Severity level<br> - Manage and track support request status | 28/05/2026 | 28/05/2026 | [Creating a support case](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) |
| 6 | - Read hybrid DNS lab overview<br> - Generate Key Pair<br> - Initialize CloudFormation Template<br> - Configure Security Group<br> - Connect to RDGW (Remote Desktop Gateway)<br> - Deploy Microsoft Active Directory | 29/05/2026 | 29/05/2026 | [What is AWS Directory Service?](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html)<br> [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) |
| 7 - Sun | - Set up DNS with Route 53:<br>  + Create Route 53 Outbound Endpoint<br>  + Create Route 53 Resolver Rules<br>  + Create Route 53 Inbound Endpoints<br>  + Test results<br>  + Clean up resources | 30/05/2026 | 31/05/2026 | [Forwarding outbound DNS queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html)<br> [Forwarding inbound DNS queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html) |

## Week 6 Achievements:
### Theory:
- Mastered Hybrid DNS architecture connecting On-premises systems (simulated via Microsoft AD on EC2) and AWS VPCs using Route 53 Resolver (Inbound/Outbound Endpoints).
- Understood the core operations of Amazon CloudWatch (Metrics, Logs, Alarms, Dashboards) to monitor infrastructure performance.
- Explored AWS Support Plans and how to handle technical or billing support cases in the AWS Console.

### Practice:
- Successfully deployed a Hybrid DNS architecture using AWS CloudFormation.
- Configured precise Security Group rules to safely allow DNS traffic (port 53 TCP/UDP) between On-premises and AWS networks.
- Set up Inbound/Outbound Resolver Endpoints and custom Route 53 Resolver Rules to achieve cross-environment domain resolution.

### Evidences:

1. **Hybrid DNS Architecture and Resolver Setup (HyDrid_DNS)**
   ![Hybrid DNS Architecture](/images/1-Worklog/Worklog_week1.6/HyDrid_DNS.png)
   *Description: Captures the architectural layout and settings for the cross-environment resolution via Route 53 Resolvers. It details the configuration of Inbound Endpoints (accepting DNS queries from the local on-premises network onto AWS) and Outbound Endpoints with forwarding rules (routing queries for corporate internal domains back to the local AD server). This setup ensures seamless, low-latency name resolution between cloud and local networks.*

2. **DNS Infrastructure Security Group Configuration (security group configuration)**
   ![Security Group Configuration](/images/1-Worklog/Worklog_week1.6/security%20group%20configuration.png)
   *Description: Shows the security group configurations protecting the Route 53 Resolver endpoints and Active Directory servers. The inbound/outbound rules are strictly restricted to only allow DNS queries via port 53 (both TCP and UDP protocols) originating from specified local and VPC IP CIDR blocks. This setup prevents unauthorized access and minimizes the attack surface on the DNS infrastructure.*

3. **Microsoft Active Directory Deployment (Directory Service)**
   ![Directory Service Deployment](/images/1-Worklog/Worklog_week1.6/Directory_Service.png)
   *Description: Displays the successful deployment of Microsoft Active Directory using AWS Directory Service. This AD setup simulates the on-premises corporate directory, acting as the primary DNS server for the corporate domain. It plays a crucial role in validating the hybrid DNS integration, as all outbound DNS queries for the internal domain from the AWS environment will be forwarded to this directory service.*

4. **Route 53 Inbound Endpoint Configuration (Inbound Endpoint)**
   ![Inbound Endpoint Configuration](/images/1-Worklog/Worklog_week1.6/Inbound_endpoint.png)
   *Description: Illustrates the creation and configuration of a Route 53 Inbound Endpoint. This endpoint provisions specific ENIs (Elastic Network Interfaces) within the AWS VPC, assigning them IP addresses that listen for DNS queries originating from the on-premises network. This setup is the gateway that allows external resources to seamlessly resolve AWS-hosted domains.*

5. **Cross-Environment DNS Resolution Validation (Test Result)**
   ![DNS Resolution Test Result](/images/1-Worklog/Worklog_week1.6/Test_result.png)
   *Description: Presents the final test results verifying the hybrid DNS setup. It shows successful `nslookup` or `dig` queries originating from the local environment resolving AWS internal domain names (via the Inbound Endpoint) and queries from the AWS environment successfully resolving corporate AD domains (via the Outbound Endpoint). This confirms the correct functioning of the Route 53 Resolver rules and bidirectional network connectivity.*

