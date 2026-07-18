---
title: "Week 3 Worklog"
date: 2026-05-13
weight: 3
chapter: false
pre: " <b> 1.3 </b> "
---

## Week 3 Objectives:
- Learn about Amazon EC2 services on AWS.
- Practice initializing, configuring, and managing EC2 Instances in Public and Private Subnets.
- Understand AWS IAM service and implement security permissions, including advanced restrictions on switching roles by IP and time.

## Tasks to implement this week:

| Day | Tasks | Start Date | Completion Date | Reference Sources |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Overview of Amazon EC2<br>- Learn about Instance Types, AMI, Key Pair, and Snapshot<br>- Understand the mechanism of EC2 Instances | 05/04/2026 | 05/04/2026 | [Amazon EC2 Basics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 3 | - Prepare EC2 environment<br>+ Create a VPC with Public and Private Subnets<br>+ Create Security Groups with appropriate ports (22 for SSH, 80/443 for HTTP/HTTPS) | 05/05/2026 | 05/05/2026 | [EC2 Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)<br>FCJ Lab |
| 4 | - Initialize Public Subnet EC2 Instance (EC2_Public)<br>+ Launch a Linux EC2 Instance in the Public Subnet<br>+ Test connection and accessibility to the Public EC2 Instance | 05/06/2026 | 05/06/2026 | [EC2 Public Instance Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 5 | - Initialize Private Subnet EC2 Instance (EC2_Private)<br>+ Launch a Linux EC2 Instance in the Private Subnet<br>+ Test remote connectivity and configurations for the Private EC2 Instance | 05/07/2026 | 05/07/2026 | [EC2 Private Instance Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 6 | - Learn about AWS IAM security management<br>+ Create IAM Users and User Groups<br>+ Assign IAM policies and check permissions | 05/08/2026 | 05/08/2026 | [AWS IAM Basics](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)<br>FCJ Lab |
| 7 - Sun | - Learn about advanced security policies for IAM roles<br>+ Restrict Switch Role action by specific IP addresses (SourceIp)<br>+ Restrict Switch Role action by specific working hours (CurrentTime) | 05/09/2026 | 05/10/2026 | [IAM Policies & Switch Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html)<br>FCJ Lab |

## Week 3 Achievements:
### Theory:
- Gained a solid understanding of the architecture and mechanisms of Amazon EC2 (Elastic Compute Cloud).
- Understood core components: Instance Types (resource optimization), Amazon Machine Image (AMI - OS packaging), Key Pairs (public/private key security), and EBS Volumes/Snapshots (data storage and backups).
- Explored IAM Roles for EC2 to securely grant AWS resource permissions without embedding Access Keys on the servers.

### Practice:
- Established a secure network environment and successfully launched 2 EC2 Instances (1 Linux Instance in the Public Subnet and 1 Linux Instance in the Private Subnet).
- Configured Security Groups with appropriate ports (port 22 for SSH, port 80/443 for Web Server) ensuring strict inbound/outbound traffic control.
- Successfully established remote connections to the instances and verified basic service deployments.

### Evidences:

1. **Initialization and Connectivity Check for Public Subnet EC2 Instance (EC2_Public)**
   ![EC2 Public Instance](/images/1-Worklog/Worklog_week1.3/EC2_Public.png)
   *Description: Verification of successfully launching an EC2 Instance inside the Public Subnet. The host is assigned a Public IP and associated with a Security Group that permits remote connections. The screenshot shows the instance state as 'Running' along with its networking details, fully prepared for SSH access.*

2. **Security Setup and Configuration for Private Subnet EC2 Instance (EC2_Private)**
   ![EC2 Private Instance](/images/1-Worklog/Worklog_week1.3/EC2_Private.png)
   *Description: Screenshot showing the configurations of the EC2 Instance deployed entirely in the Private Subnet (highly secure internal network partition). This host does not have a Public IP assigned, effectively isolating it from the public internet to protect backend databases or application code. Connections to this instance are routed through a Bastion Host, NAT Gateway, or VPC Endpoints.*



3. **Create IAM User**
   ![Create IAM User](/images/1-Worklog/Worklog_week1.3/Create%20IAM%20User.png)
   *Description: The process of creating a new IAM User in the AWS Management Console. This involves setting up user details, selecting AWS access type (programmatic access or AWS Management Console access), and securely generating initial credentials.*

4. **Create User Groups**
   ![Create user groups](/images/1-Worklog/Worklog_week1.3/Create%20user%20groups.png)
   *Description: Organizing IAM users into groups. Creating user groups allows for easier permission management by applying IAM policies to the group rather than individually to each user, adhering to the principle of least privilege.*

5. **Check Permissions**
   ![Check permission](/images/1-Worklog/Worklog_week1.3/Check%20permission.png)
   *Description: Verifying the attached policies and assigned permissions for the IAM user or group. This step ensures that the configured entities have exactly the required access rights to perform necessary AWS operations without exceeding their authorized scope.*

6. **General Check**
   ![Check](/images/1-Worklog/Worklog_week1.3/Check.png)
   *Description: A comprehensive review and validation step to ensure all IAM configurations, including user creation and group assignments, have been successfully applied and are functioning as intended.*

7. **Limit Switch Role by IP**
   ![Limit switch by IP](/images/1-Worklog/Worklog_week1.3/limit%20switch%20by%20IP.png)
   *Description: Implementing advanced security policies using IAM conditions. This screenshot demonstrates restricting the sts:AssumeRole action (Switch Role) so that it can only be performed from specific trusted IP addresses (ws:SourceIp), greatly enhancing network security.*

8. **Limit Switch Role by Time**
   ![Limit switch role by time](/images/1-Worklog/Worklog_week1.3/limit%20switch%20role%20by%20time.png)
   *Description: Applying time-based restrictions to IAM roles. This configuration uses conditions such as ws:CurrentTime to ensure that users can only assume specific roles during designated working hours, reducing the risk of unauthorized access outside of regular operational windows.*
