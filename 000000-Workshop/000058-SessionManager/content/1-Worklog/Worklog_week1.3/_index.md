---
title: "Week 3 Worklog"
date: 2026-05-13
weight: 3
chapter: false
pre: " <b> 1.3 </b> "
---

## Week 3 Objectives:
- Learn about Amazon EC2 services on AWS.
- Practice initializing, configuring, and managing EC2 Instances.
- Deploy Node.js applications on Linux and Windows environments.

## Tasks to implement this week:

| Day | Tasks | Start Date | Completion Date | Reference Sources |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Overview of Amazon EC2<br>- Learn about Instance Types, AMI, Key Pair, and Snapshot<br>- Understand the mechanism of EC2 Instances | 05/04/2026 | 05/04/2026 | [Amazon EC2 Basics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 3 | - Prepare EC2 environment<br>+ Create VPC for Linux<br>+ Create VPC for Windows<br>+ Create Security Group for Linux and Windows Instances | 05/05/2026 | 05/05/2026 | [EC2 Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)<br>FCJ Lab |
| 4 | - Initialize Windows EC2 Instance<br>+ Create Windows Instance<br>+ Connect via Remote Desktop to Windows Instance | 05/06/2026 | 05/06/2026 | [EC2 Windows Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 5 | - Initialize Linux EC2 Instance<br>+ Create Linux Instance<br>+ Connect via SSH to Linux Instance<br>- Learn about changing EC2 configuration and managing EBS Snapshot | 05/07/2026 | 05/07/2026 | [EC2 Linux Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 6 | - Advanced EC2 Practice<br>+ Create Custom AMI<br>+ Create Instance from Custom AMI<br>+ Practice EC2 access when losing Key Pair | 05/08/2026 | 05/08/2026 | [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)<br>FCJ Lab |
| 7 - Sun | - Deploy Node.js application on EC2<br>+ Install LAMP/XAMPP Server<br>+ Install Node.js on Linux and Windows<br>+ Deploy Node.js application<br>- Learn about resource limits using IAM | 05/09/2026 | 05/10/2026 | [IAM for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html)<br>FCJ Lab |

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

