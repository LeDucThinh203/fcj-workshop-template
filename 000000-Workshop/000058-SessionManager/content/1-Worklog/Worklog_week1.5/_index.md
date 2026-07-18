---
title: "Week 5 Worklog"
date: 2026-05-13
weight: 5
chapter: false
pre: " <b> 1.5 </b> "
---

## Week 5 Objectives:
- Understood the concept and architecture of AWS Systems Manager (SSM) Session Manager for secure instance administration.
- Understood the role of VPC Endpoints (Interface endpoints) for private connection to AWS services without internet routing.
- Understood how NAT Gateway translates private IP addresses for outbound-only internet traffic.

## Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Study the theory of AWS Systems Manager (SSM) Session Manager<br>- Learn about VPC Endpoints (Interface Endpoints and Gateway Endpoints)<br>- Learn about NAT Gateway and how it operates in a Public Subnet to provide internet access to Private Subnets | 18/05/2026 | 18/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | - **Practice (Part 1):**<br>  + Create a custom VPC with Public Subnet and Private Subnets<br>  + Initialize and configure a NAT Gateway in the Public Subnet and associate it with an Elastic IP<br>  + Configure routing rules in the Private Route Table to allow outbound internet access via the NAT Gateway | 19/05/2026 | 19/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - **Practice (Part 2):**<br>  + Launch a Linux EC2 Instance in the Private Subnet (without a Public IP)<br>  + Create and associate an IAM Role with the EC2 Instance containing the necessary permissions to communicate with AWS Systems Manager (`AmazonSSMManagedInstanceCore`)<br>  + Configure the Security Group for the EC2 Instance (no port 22 SSH open) | 20/05/2026 | 20/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | - **Practice (Part 3):**<br>  + Establish VPC Endpoints (`ssm`, `ssmmessages`, `ec2messages`) in the Private Subnet<br>  + Configure the Security Group for the VPC Endpoints to allow inbound traffic from the EC2 instance<br>  + Verify secure connection to the private EC2 instance via Systems Manager Session Manager<br>  + Clean up resources to prevent charges | 21/05/2026 | 21/05/2026 | https://cloudjourney.awsstudygroup.com/ |

### Week 5 Achievements:
#### Theory:
- Understood the concept and architecture of AWS Systems Manager (SSM) Session Manager for secure instance administration.
- Understood the role of VPC Endpoints (Interface endpoints) for private connection to AWS services without internet routing.
- Understood how NAT Gateway translates private IP addresses for outbound-only internet traffic.

#### Practice:
- Launched a custom VPC with isolated private subnets and a NAT Gateway in the public subnet.
- Configured routing rules in the Private Route Table to allow outbound internet access via the NAT Gateway.
- Established secure connections to the private EC2 instance via Systems Manager Session Manager by setting up VPC Endpoints (`ssm`, `ssmmessages`, `ec2messages`) and IAM roles.

### Evidences:

1. **NAT Gateway Initialization and Configuration (Nat_Gateway)**
   ![NAT Gateway Initialization](/images/1-Worklog/Worklog_week1.5/Nat_Gateway.png)
   *Description: Screenshot confirming the successful creation and configuration of the NAT Gateway service within the AWS Console. Deployed inside the Public Subnet and associated with a static Elastic IP (EIP), it acts as a network address translator. This allows instances in the Private Subnet to initiate outbound connections to the Internet (for software updates or packages) while blocking any incoming unauthorized traffic from the public internet.*

2. **Route Table Configuration for NAT (NAT)**
   ![Route Table for NAT](/images/1-Worklog/Worklog_week1.5/NAT.png)
   *Description: Shows the Route Table configuration associated with the Private Subnets. A new route directing default internet-bound traffic (`0.0.0.0/0`) to the newly created NAT Gateway has been added. This routing policy secures outbound flows while maintaining complete server isolation.*

3. **Connectivity Verification via VPC Endpoints (Connect_endpoint)**
   ![Connectivity via VPC Endpoints](/images/1-Worklog/Worklog_week1.5/Connect_endpoint.png)
   *Description: Verification of successfully establishing VPC Endpoints (specifically for SSM, EC2 Messages, and SSM Messages services). This configuration enables secure, agent-based remote command-line access to EC2 instances in the Private Subnet via AWS Systems Manager (SSM) Session Manager. It eliminates the need to open port 22 SSH or assign Public IPs, greatly improving the overall security posture.*

