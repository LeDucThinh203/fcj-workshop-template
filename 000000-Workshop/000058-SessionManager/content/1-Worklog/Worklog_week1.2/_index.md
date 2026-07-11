---
title: "Week 2 Worklog"
date: 2026-05-13
weight: 2
chapter: false
pre: " <b> 1.2 </b> "
---

## Week 2 Objectives:
- Understand basic networking in AWS (VPC)
- Master how to configure network components and security within a VPC
- Practice building a complete VPC

## Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn VPC basics:<br>  + VPC Overview<br>  + CIDR Block<br>  + Distinguish Public / Private Subnets | 27/04/2026 | 27/04/2026 | [VPC Basics](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) |
| 3 | - Learn about subnets & Route Tables:<br>  + How to divide subnets<br>  + Configure Route Tables | 28/04/2026 | 28/04/2026 | [Subnets & Route Tables](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html) |
| 4 | - Learn about Internet Gateway & NAT Gateway:<br>  + Internet Gateway for Public Subnets<br>  + NAT Gateway for Private Subnets | 29/04/2026 | 29/04/2026 | [NAT Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) |
| 5 | - Learn about security in VPC:<br>  + Security Groups<br>  + Network ACLs<br>  + Inbound / Outbound rules | 30/04/2026 | 30/04/2026 | [VPC Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) |
| 6 | - **Practice:**<br>  + Create VPC<br>  + Create Public & Private Subnets<br>  + Configure Route Tables | 01/05/2026 | 01/05/2026 | [FCJ Lab - Create VPC](https://cloudjourney.awsstudygroup.com/2-prerequisites/2.1-createvpc/) |
| 7 - Sun | - **Advanced practice:**<br>  + Attach Internet Gateway<br>  + Create NAT Gateway<br>  + Deploy EC2 in Private/Public Subnets<br>  + Verify internet connectivity | 02/05/2026 | 03/05/2026 | [FCJ Lab - Public/Private](https://cloudjourney.awsstudygroup.com/2-prerequisites/2.2-publicprivateinstance/) |

## Week 2 Achievements:
### Theory:
- Can understand the architecture of Amazon VPC and how to manage IP address ranges via CIDR
- Know how to create and configure route tables

### Practice:
- Completed the configuration of a complete VPC including public and private subnets.
- Successfully set up Internet Gateway and NAT Gateway to route network traffic.
- Deployed EC2 Instances and configured security using Security Groups/Network ACLs.

### Evidences:

1. **Attendance History - Week 2**
   ![Attendance History](/images/1-Worklog/Worklog_week1.2/attendance_history_2.png)
   *Description: Screenshot confirming the attendance log and full participation in all learning, mentoring, and team sync sessions during Week 2. This serves as verification of schedule compliance, self-discipline, and completing the required training hours under the First Cloud Journey program.*

2. **Lab07 Network Configuration - Step 1: VPC Initialization & DNS Setup**
   ![Lab07 Configuration - Step 1](/images/1-Worklog/Worklog_week1.2/Module%2001-Lab07-01.png)
   *Description: Hands-on evidence of the initial step in the Lab07 exercise - setting up the Virtual Private Cloud (VPC) environment. This image details the configuration of the primary IPv4 CIDR Block and enabling crucial attributes such as DNS Resolution and DNS Hostnames, laying a solid foundation for subnet deployment.*

3. **Lab07 Network Configuration - Step 2: Subnet Partitioning & Route Tables**
   ![Lab07 Configuration - Step 2](/images/1-Worklog/Worklog_week1.2/Module%2001-Lab07-02.png)
   *Description: Architectural configuration demonstrating the subdivision of the CIDR block into isolated Public and Private Subnets across multiple Availability Zones for high availability. It also displays the customization of Route Tables and subnet associations to ensure proper and secure routing control.*

4. **Lab07 Network Configuration - Step 3: Gateway Attachment & Connectivity Verification**
   ![Lab07 Configuration - Step 3](/images/1-Worklog/Worklog_week1.2/Module%2001-Lab07-03.png)
   *Description: Verification screenshot of the final network design phase. This shows the setup of an Internet Gateway (IGW) to handle external traffic for Public Subnets, and a NAT Gateway to securely connect instances in Private Subnets to the Internet for updates. All routing controls are successfully verified and tested.*



