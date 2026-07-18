---
title: "Worklog"
date: 2026-04-27
weight: 1
pre : " <b> 1. </b> "
---

## Week 1:
- Connect and get acquainted with members of First Cloud Journey.
- Study basic AWS service concepts and read documentation on the AWS Management Console & AWS CLI.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Get acquainted with FCJ members<br>- Read and take note of the rules and regulations at the internship unit | 20/04/2026 | 20/04/2026 |  |
| 3 | - Learn about cloud computing theory and AWS service categories:<br>  + Compute (EC2, Lambda)<br>  + Storage (S3, EBS)<br>  + Networking (VPC, Route 53)<br>  + Database (RDS, DynamoDB) | [21/04/2026](./Worklog_week1.1/) | [21/04/2026](./Worklog_week1.1/) | [AWS Cloud Concepts](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html) |
| 4 | - Study AWS Free Tier account policies<br>- Research AWS Management Console and AWS CLI documentation:<br>  + Read guides on AWS account registration procedures<br>  + Study AWS CLI installation and configuration workflows for different OS | 22/04/2026 | 22/04/2026 | [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) |
| 5 | - Learn the theoretical basics of Amazon EC2:<br>  + Understand Instance types, AMI, Key Pair, and EBS Volumes/Snapshots<br>  + Study methods for remotely connecting to EC2 via SSH<br>  + Learn about Elastic IP functions | 23/04/2026 | 23/04/2026 | [Amazon EC2 Overview](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) |
| 6 | - Read documentation on:<br>  + Launching EC2 instances via Console and CLI<br>  + Connecting to instances via SSH using private keys<br>  + Mounting and configuring EBS volumes | 24/04/2026 | 24/04/2026 | [Amazon EC2 Instance Lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html) |
| 7 - Sun | - Conduct advanced theoretical research:<br>  + Study Security Group configurations and port management best practices<br>  + Learn the setup logic for Web Servers (Apache/Nginx) on Linux<br>  + Understand Amazon S3 storage architecture (buckets, objects, and permissions) | 25/04/2026 | 26/04/2026 | [Amazon S3 Basics](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) |

---

## Week 2:
### Week 2 Objectives:
- Understand AWS Billing and Cost Management tools.
- Master the role and configuration of AWS Budgets to monitor cloud spending.
- Practice setting budget limits and configuring automated threshold-based email alerts.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn about AWS Billing & Cost Management tools:<br>  + AWS Billing Tools<br>  + Calculate basic service costs | 27/04/2026 | 27/04/2026 | [AWS Billing Overview](https://docs.aws.amazon.com/billing/latest/userguide/billing-whatis.html) |
| 3 | - Understand AWS Budgets mechanisms:<br>  + Cost budget vs. Usage budget concepts<br>  + Actual and forecasted cost alert thresholds | [28/04/2026](./Worklog_week1.2/) | [28/04/2026](./Worklog_week1.2/) | [AWS Budgets Guide](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) |
| 4 | - Plan monthly budget limits for an AWS Free Tier account to avoid unexpected charges. | 29/04/2026 | 29/04/2026 | [AWS Free Tier Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) |
| 5 | - Learn how to configure budget alerts via email and automated notification channels (Amazon SNS). | 30/04/2026 | 30/04/2026 | [AWS Budgets Alerts](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-alerts.html) |
| 6 | - **Practice (Part 1):** Initialize a monthly cost budget (`My Monthly Cost Budget`) with a $100 limit. | 01/05/2026 | 01/05/2026 | [Creating a Cost Budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create-cost.html) |
| 7 - Sun | - **Practice (Part 2):** Create a backup cost budget (`My-200$-budget`) and resource usage budget (`Cost budget`). Verify health status and alert triggers. | 02/05/2026 | 03/05/2026 | [Monitoring Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-viewing.html) |

### Week 2 Achievements:
#### Theory:
- Gained a solid understanding of AWS pricing models, billing drivers, and how to use AWS Budgets as a financial safety net.
- Distinguished between Cost Budgets (financial monitoring) and Usage Budgets (resource utilization monitoring).

#### Practice:
- Successfully initialized three separate budgets to monitor spending from multiple dimensions on the AWS Console.
- Configured automated email alerts when actual costs reach 80% of the limit or forecasted charges exceed the threshold.

---

## Week 3:
### Week 3 Objectives:
- Learn about Amazon EC2 services on AWS.
- Practice initializing, configuring, and managing EC2 Instances in Public and Private Subnets.
- Understand AWS IAM service and implement security permissions, including advanced restrictions on switching roles by IP and time.

### Tasks to implement this week:

| Day | Tasks | Start Date | Completion Date | Reference Sources |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Overview of Amazon EC2<br>- Learn about Instance Types, AMI, Key Pair, and Snapshot<br>- Understand the mechanism of EC2 Instances | 05/04/2026 | 05/04/2026 | [Amazon EC2 Basics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 3 | - Prepare EC2 environment<br>+ Create a VPC with Public and Private Subnets<br>+ Create Security Groups with appropriate ports (22 for SSH, 80/443 for HTTP/HTTPS) | [05/05/2026](./Worklog_week1.3/) | [05/05/2026](./Worklog_week1.3/) | [EC2 Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)<br>FCJ Lab |
| 4 | - Initialize Public Subnet EC2 Instance (EC2_Public)<br>+ Launch a Linux EC2 Instance in the Public Subnet<br>+ Test connection and accessibility to the Public EC2 Instance | 05/06/2026 | 05/06/2026 | [EC2 Public Instance Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 5 | - Initialize Private Subnet EC2 Instance (EC2_Private)<br>+ Launch a Linux EC2 Instance in the Private Subnet<br>+ Test remote connectivity and configurations for the Private EC2 Instance | 05/07/2026 | 05/07/2026 | [EC2 Private Instance Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 6 | - Learn about AWS IAM security management<br>+ Create IAM Users and User Groups<br>+ Assign IAM policies and check permissions | 05/08/2026 | 05/08/2026 | [AWS IAM Basics](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)<br>FCJ Lab |
| 7 - Sun | - Learn about advanced security policies for IAM roles<br>+ Restrict Switch Role action by specific IP addresses (SourceIp)<br>+ Restrict Switch Role action by specific working hours (CurrentTime) | 05/09/2026 | 05/10/2026 | [IAM Policies & Switch Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html)<br>FCJ Lab |

---

## Week 4:
### Week 4 Objectives:
- Initialize and configure network environments (VPC, Subnet Groups, Security Groups) for EC2 and RDS instances.
- Launch a Linux EC2 Instance, configure SSH Key Pair permissions, and establish secure SSH connections.
- Install Git, Node.js, and MySQL client on EC2 to deploy and connect a Node.js web application to an Amazon RDS database.
- Understand database management operations, including maintenance, monitoring logs, manual/automatic snapshots, and high-availability architecture.

### Tasks to be implemented this week:

| Day | Task | Start Date | End Date | Resource |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Overview of Amazon RDS<br>- Compare RDS with other storage services (EC2 DB, DynamoDB, Redshift, S3) | 11/05/2026 | 11/05/2026 | [Amazon RDS Documentation](https://docs.aws.amazon.com/rds/) |
| 3 | - Network setup for RDS:<br>  + Create VPC and subnets<br>  + Create Security Groups for EC2 and RDS<br>  + Create DB Subnet Group | [12/05/2026](./Worklog_week1.4/) | [12/05/2026](./Worklog_week1.4/) | [VPC for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) |
| 4 | - Practice initializing an Amazon RDS instance<br>- Configure DB engine, credentials, and database security options | 13/05/2026 | 13/05/2026 | [Creating an RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) |
| 5 | - Initialize EC2 Instance and prepare client environment:<br>  + Create Linux EC2 Instance<br>  + Configure SSH Key Pair permissions (`chmod 400`) and connect via SSH (MobaXterm)<br>  + Install Git and Node.js runtime environments on EC2 | 14/05/2026 | 14/05/2026 | [EC2 Linux Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 6 | - Deploy web application on EC2 and connect to RDS:<br>  + Clone repository and install dependencies<br>  + Install MySQL server client, execute SQL scripts to create databases and tables<br>  + Seed mock user data and verify connection via RDS Endpoint | 15/05/2026 | 15/05/2026 | [Connecting to RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html)<br>FCJ Lab |
| 7 - Sun | - Database administration and maintenance:<br>  + View RDS Logs & Events<br>  + Configure Maintenance & Backup options, perform manual/automatic Snapshots<br>  + Learn about Multi-AZ, Read Replicas, and clean up resources | 16/05/2026 | 17/05/2026 | [RDS Backup and Restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html)<br>FCJ Lab |

### Week 4 Results:
#### Theoretical:
- Mastered Amazon RDS knowledge: Benefits, supported DB engines, management features.
- Understood how Multi-AZ and Read Replicas work.
- Learned to differentiate when to use RDS, DynamoDB, Redshift, or S3.
- Understood security mechanisms (Security Groups, Encryption) and backups (Snapshots) on RDS.
#### Practical:
- Successfully set up a secure network environment for the Database (DB Subnet Group, Security Groups).
- Successfully initialized an Amazon RDS instance (MySQL/MariaDB).
- Successfully connected a Web application on EC2 to the RDS database via Endpoint.
- Successfully performed data backup and restoration using Snapshots.
- Efficiently managed resources and performed cleanup to avoid unnecessary costs.

---

## Week 5:
### Week 5 Objectives:
- Understood the concept and architecture of AWS Systems Manager (SSM) Session Manager for secure instance administration.
- Understood the role of VPC Endpoints (Interface endpoints) for private connection to AWS services without internet routing.
- Understood how NAT Gateway translates private IP addresses for outbound-only internet traffic.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Study the theory of AWS Systems Manager (SSM) Session Manager<br>- Learn about VPC Endpoints (Interface Endpoints and Gateway Endpoints)<br>- Learn about NAT Gateway and how it operates in a Public Subnet to provide internet access to Private Subnets | 18/05/2026 | 18/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | - **Practice (Part 1):**<br>  + Create a custom VPC with Public Subnet and Private Subnets<br>  + Initialize and configure a NAT Gateway in the Public Subnet and associate it with an Elastic IP<br>  + Configure routing rules in the Private Route Table to allow outbound internet access via the NAT Gateway | 19/05/2026 | 19/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - **Practice (Part 2):**<br>  + Launch a Linux EC2 Instance in the Private Subnet (without a Public IP)<br>  + Create and associate an IAM Role with the EC2 Instance containing the necessary permissions to communicate with AWS Systems Manager (`AmazonSSMManagedInstanceCore`)<br>  + Configure the Security Group for the EC2 Instance (no port 22 SSH open) | 20/05/2026 | 20/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | - **Practice (Part 3):**<br>  + Establish VPC Endpoints (`ssm`, `ssmmessages`, `ec2messages`) in the Private Subnet<br>  + Configure the Security Group for the VPC Endpoints to allow inbound traffic from the EC2 instance<br>  + Verify secure connection to the private EC2 instance via Systems Manager Session Manager<br>  + Clean up resources to prevent charges | [21/05/2026](./Worklog_week1.5/) | [21/05/2026](./Worklog_week1.5/) | https://cloudjourney.awsstudygroup.com/ |

### Week 5 Achievements:
#### Theory:
- Understood the concept and architecture of AWS Systems Manager (SSM) Session Manager for secure instance administration.
- Understood the role of VPC Endpoints (Interface endpoints) for private connection to AWS services without internet routing.
- Understood how NAT Gateway translates private IP addresses for outbound-only internet traffic.

#### Practice:
- Launched a custom VPC with isolated private subnets and a NAT Gateway in the public subnet.
- Configured routing rules in the Private Route Table to allow outbound internet access via the NAT Gateway.
- Established secure connections to the private EC2 instance via Systems Manager Session Manager by setting up VPC Endpoints (ssm, ssmmessages, ec2messages) and IAM roles.

---

## Week 6:
### Week 6 Objectives:
- Understood the core operations of Amazon CloudWatch (Metrics, Logs, Alarms, Dashboards) to monitor infrastructure performance.
- Explored AWS Support Plans and how to handle technical or billing support cases in the AWS Console.
- Deploy a Hybrid DNS integration on premises with AWS using Route 53 Resolver and Microsoft AD.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn Amazon CloudWatch & prepare environment<br> - CloudWatch Metrics:<br>  + View Metrics<br>  + Perform search operations<br>  + Perform math operations<br>  + Create dynamic labels | 25/05/2026 | 25/05/2026 | [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)<br> [Using Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) |
| 3 | - CloudWatch Logs:<br>  + View CloudWatch Logs<br>  + CloudWatch Logs Insights<br>  + CloudWatch Metric Filter<br>  + Create CloudWatch Alarms<br>  + Create CloudWatch Dashboards<br>  + Clean up resources | 26/05/2026 | 26/05/2026 | [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)<br> [Creating CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html)<br> [CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) |
| 4 | - Learn about AWS Support Plans: Basic, Developer, Business, Enterprise On-Ramp, Enterprise<br> - Access AWS Support Console<br> - Learn about Support Request types (Account & billing, Technical)<br> - Change support plan | 27/05/2026 | 27/05/2026 | [AWS Support Plans](https://aws.amazon.com/vi/premiumsupport/plans/)<br> [Getting started with AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html) |
| 5 | - Create a Support Request (Support Case)<br> - Select Severity level<br> - Manage and track support request status | 28/05/2026 | 28/05/2026 | [Creating a support case](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) |
| 6 | - Read hybrid DNS lab overview<br> - Generate Key Pair<br> - Initialize CloudFormation Template<br> - Configure Security Group<br> - Connect to RDGW (Remote Desktop Gateway)<br> - Deploy Microsoft Active Directory | [29/05/2026](./Worklog_week1.6/) | [29/05/2026](./Worklog_week1.6/) | [What is AWS Directory Service?](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html)<br> [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) |
| 7 - Sun | - Set up DNS with Route 53:<br>  + Create Route 53 Outbound Endpoint<br>  + Create Route 53 Resolver Rules<br>  + Create Route 53 Inbound Endpoints<br>  + Test results<br>  + Clean up resources | 30/05/2026 | 31/05/2026 | [Forwarding outbound DNS queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html)<br> [Forwarding inbound DNS queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html) |

### Week 6 Achievements:
#### Theory:
- Mastered Hybrid DNS architecture connecting On-premises systems (simulated via Microsoft AD on EC2) and AWS VPCs using Route 53 Resolver (Inbound/Outbound Endpoints).
- Understood the core operations of Amazon CloudWatch (Metrics, Logs, Alarms, Dashboards) to monitor infrastructure performance.
- Explored AWS Support Plans and how to handle technical or billing support cases in the AWS Console.

#### Practice:
- Successfully deployed a Hybrid DNS architecture using AWS CloudFormation.
- Configured precise Security Group rules to safely allow DNS traffic (port 53 TCP/UDP) between On-premises and AWS networks.
- Set up Inbound/Outbound Resolver Endpoints and custom Route 53 Resolver Rules to achieve cross-environment domain resolution.

---

## Week 7:
### Week 7 Objectives:
- Get familiar with and practice using the AWS Command Line Interface (CLI) to view, configure, and manage AWS resources (S3, SNS, IAM, VPC, EC2).
- Understand multi-account management using AWS Organizations, configuring Organizational Units (OUs), and IAM Identity Center.
- Master centralized backup solutions using AWS Backup to protect data safety on AWS.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn AWS CLI & Installation<br> - View resources via CLI<br> - AWS CLI with Amazon S3 and Amazon SNS | 01/06/2026 | 01/06/2026 | [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)<br> [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/) |
| 3 | - AWS CLI with IAM and VPC (VPC, Internet Gateway)<br> - Practice creating EC2 via AWS CLI | 02/06/2026 | 02/06/2026 | [AWS CLI for EC2 & VPC](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2.html)<br> [AWS CLI for IAM](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-iam.html) |
| 4 | - Learn AWS Organizations<br> - Create member accounts, configure Organizational Unit (OU) and invite AWS Accounts | 03/06/2026 | 03/06/2026 | [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)<br> [Creating account in Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) |
| 5 | - Configure Member Account access via CLI<br> - Configure Time-based access control & Customer Managed Policies<br> - Understand IAM Identity Center Identity Store APIs | 04/06/2026 | 04/06/2026 | [AWS IAM Identity Center Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)<br> [Identity Store APIs](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/Welcome.html) |
| 6 | - Learn AWS Backup service<br> - Prepare environment: Create S3 Bucket & Deploy backup infrastructure | 05/06/2026 | 05/06/2026 | [What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)<br> [Backup S3 with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html) |
| 7 - Sun | - Setup Backup plan & configure notifications<br> - Test Restore operations<br> - Clean up resources to prevent charges | [06/06/2026](./Worklog_week1.7/) | [07/06/2026](./Worklog_week1.7/) | [Creating backup plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)<br> [Restoring a backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) |

### Week 7 Achievements:
#### Theory:
- Understood how to configure and invoke AWS service APIs via the AWS CLI.
- Mastered enterprise-scale account management with AWS Organizations and IAM Identity Center, including time-based access controls and Customer Managed Policies.
- Understood the core mechanism of AWS Backup: Backup Vaults, Backup Plans, Retention rules, and data restoration (Restore).

#### Practice:
- Proficiently used CLI commands to query and manage EC2, S3, IAM, and VPC resources.
- Successfully built an automated backup system (AWS Backup Plan) for EC2 server infrastructure and S3 storage.
- Successfully performed recovery testing (Test Restore) from backup points and executed cleanups for Cost Optimization.

### Evidences:

1. **Deploy Infrastructure (Deploy infrastructure)**
   ![Deploy infrastructure](../images/1-Worklog/Worklog_week1.7/Deloy%20infrastructure.png)
   *Description: The process of deploying the foundational infrastructure for the lab using AWS CloudFormation. Necessary resources such as EC2 instances, EBS volumes, or basic network configurations are automatically provisioned. This is a crucial preparation step to have actual resources for testing backup and restore capabilities.*

2. **Create S3 Folder (Create s3 folder)**
   ![Create S3 Folder](../images/1-Worklog/Worklog_week1.7/Create%20s3%20folder.png)
   *Description: Initializing a directory or bucket on Amazon S3. S3 is commonly used as a secure, durable, and cost-effective storage location for backups (backup vault/storage) from AWS Backup or other services. Setting up a proper storage structure ensures that backup data is well-organized and easily retrievable when needed.*

3. **Configure Backup Plans (Create Backup plans)**
   ![Create Backup plans](../images/1-Worklog/Worklog_week1.7/Create%20Backup%20plans.png)
   *Description: Configuring an AWS Backup plan. This step establishes rules for automating the backup process, including backup frequency (e.g., daily, weekly), retention period, and backup window. Automated backup management helps organizations comply with data security regulations without manual operational overhead.*

4. **Test Data Restoration (Test Restore)**
   ![Test Restore](../images/1-Worklog/Worklog_week1.7/Test%20Restore.png)
   *Description: Executing the data restoration process from a previously created backup (recovery point). This is the most critical validation step in any backup strategy, ensuring that in the event of data loss or system failure, data can be restored intact and systems can return to normal operation.*

5. **Clean Up Resources (Clean up resources)**
   ![Clean up resources](../images/1-Worklog/Worklog_week1.7/Clean%20up%20resources.png)
   *Description: Deleting the AWS resources created during the hands-on lab (such as EC2, S3, Backup plans, CloudFormation stacks). Careful cleanup after completing the lab is a mandatory best practice for Cost Optimization, ensuring the account does not incur ongoing charges for unused resources.*

---

## Week 8:
### Week 8 Objectives:
- Learn advanced identity and access management using IAM Groups, Users, Policies, and Roles.
- Understand data encryption on Amazon S3 using AWS Key Management Service (KMS), and configure secure cross-account encrypted data sharing.
- Configure system activity tracking and auditing using AWS CloudTrail.
- Use Amazon Athena to query and analyze CloudTrail logs stored in Amazon S3 using standard SQL.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn advanced concepts of IAM Groups, Users, Policies, and Roles under the principle of least privilege<br>- **Practice (Part 1)**: Create IAM Groups and Users to control access boundaries | 08/06/2026 | 08/06/2026 | [IAM Policies Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) |
| 3 | - Study AWS KMS encryption principles (SSE-KMS, Customer Managed Keys, Key Policies)<br>- **Practice (Part 2)**: Create a Customer Managed Key in AWS Key Management Service (KMS) and set up its Key Policy | 09/06/2026 | 09/06/2026 | [AWS KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) |
| 4 | - **Practice (Part 3)**: Author IAM Policies and Roles to delegate usage permissions for the KMS Key<br>- Create a new S3 bucket and upload test files, setting up server-side encryption via KMS (SSE-KMS) | 10/06/2026 | 10/06/2026 | [Amazon S3 KMS Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) |
| 5 | - **Practice (Part 4)**: Verify encryption and share the encrypted S3 objects with an external AWS account | 11/06/2026 | 11/06/2026 | [S3 Cross-Account Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html) |
| 6 | - Study system auditing with AWS CloudTrail<br>- **Practice (Part 5)**: Deploy an AWS CloudTrail trail to deliver API activity logs to a secure S3 bucket | 12/06/2026 | 12/06/2026 | [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) |
| 7 - Sun | - **Practice (Part 6)**: Configure Amazon Athena, define query result locations on S3, and run SQL queries against CloudTrail log tables<br>- Clean up all provisioned resources for Cost Optimization | [13/06/2026](./Worklog_week1.8/) | [14/06/2026](./Worklog_week1.8/) | [Querying CloudTrail Logs with Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-cloudtrail-logs.html) |

### Week 8 Achievements:
- **Access Management (IAM)**: Successfully configured granular access controls using IAM Groups, Users, Policies, and Roles to enforce least privilege.
- **Data Encryption & Sharing**: Implemented AWS KMS server-side encryption on Amazon S3 and securely shared encrypted datasets across separate AWS accounts.
- **Monitoring & Auditing**: Deployed AWS CloudTrail to log and deliver API activity histories to durable S3 storage.
- **Log Analytics (Athena)**: Mastered Amazon Athena to run SQL queries directly on S3 to inspect CloudTrail operational logs for security audits.
- **Cost Optimization**: Cleaned up all temporary lab resources to prevent ongoing charges.

### Evidences:

1. **Create IAM Group and User (Create Group and User)**
   ![Create IAM Group and User](/images/1-Worklog/Worklog_week1.8/Create%20Group%20and%20User.png)
   *Description: Shows the IAM console after successfully creating a new group and user. Placing users into groups simplifies permission management and adheres to best practices.*

2. **Initialize AWS Key Management Service (Create Key Management Service)**
   ![Create KMS Key](/images/1-Worklog/Worklog_week1.8/Create%20Key%20Management%20Service.png)
   *Description: Displays the creation of a Customer Managed Key in AWS KMS, which will be utilized to encrypt data on S3 and regulate access via Key Policies.*

3. **Configure Policy and Role in IAM (Create policy and role)**
   ![Create IAM Policy and Role](/images/1-Worklog/Worklog_week1.8/Create%20policy%20and%20role.png)
   *Description: Shows custom IAM Policies and Roles designed to delegate KMS encryption/decryption rights to specific services or external users.*

4. **Create S3 Bucket and Upload Data (Create and upload data bucket)**
   ![Create S3 Bucket and Upload](/images/1-Worklog/Worklog_week1.8/Create%20and%20upload%20data%20bucket.png)
   *Description: Demonstrates creating a new Amazon S3 bucket and uploading sample datasets to prepare for server-side encryption testing.*

5. **Test and Share Encrypted S3 Data (Test and share encrypted data on S3)**
   ![Share Encrypted Data](/images/1-Worklog/Worklog_week1.8/Test%20and%20share%20encrypted%20data%20on%20S3.png)
   *Description: Confirms SSE-KMS encryption is active on the S3 bucket and verifies cross-account sharing permissions, allowing authorized external accounts to read the encrypted files.*

6. **Initialize AWS CloudTrail (Create CloudTrail)**
   ![Create CloudTrail](/images/1-Worklog/Worklog_week1.8/Create%20CloudTrail.png)
   *Description: Shows the configuration of a new AWS CloudTrail trail logging all API calls and delivery of those logs to a centralized S3 bucket.*

7. **Log System Activity to CloudTrail (Logging to CloudTrail)**
   ![CloudTrail Logging](/images/1-Worklog/Worklog_week1.8/Logging%20to%20CloudTrail.png)
   *Description: Verifies that account events are actively captured and written as compressed log files in the specified S3 storage path.*

8. **Configure Amazon Athena (Create Amazon Athena)**
   ![Configure Amazon Athena](/images/1-Worklog/Worklog_week1.8/Create%20Amazon%20Athena.png)
   *Description: Illustrates configuring Amazon Athena's query output folder on S3 and setting up database tables linked to the CloudTrail log datasets.*

9. **Query Logs with Athena SQL (Retrieve data with athena)**
   ![Query Logs with Athena](/images/1-Worklog/Worklog_week1.8/Retrieve%20data%20with%20athena.png)
   *Description: Demonstrates running SQL SELECT queries in Athena to parse, filter, and audit specific API operations recorded by CloudTrail.*

10. **Clean Up Lab Resources (Clean)**
    ![Clean Up Resources](/images/1-Worklog/Worklog_week1.8/Clean.png)
    *Description: Shows the systematic deletion of all trial resources (KMS keys, S3 buckets, CloudTrail trails, Athena tables, IAM roles/policies/users/groups) to maintain a clean environment and avoid unwanted costs.*

---

## Week 9:
### Week 9 Objectives:
- Learn and implement serverless operations automation using AWS Lambda and Amazon EventBridge to automatically start/stop EC2 instances based on schedules.
- Understand resource tagging strategies, AWS Resource Groups, and resource filtering.
- Configure ChatOps integration to route Lambda execution logs and operational alerts to Slack using Incoming Webhooks.
- Activate and configure AWS Security Hub to evaluate account security posture (CSPM - Cloud Security Posture Management).

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn basic concepts of AWS Lambda serverless computing and EventBridge scheduling triggers (cron jobs)<br>- Understand resource tagging, bulk tag editing via Tag Editor, and creating AWS Resource Groups | 15/06/2026 | 15/06/2026 | [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/) |
| 3 | - **Practice (Part 1)**: Create a VPC, subnets, security groups, and launch EC2 instances to prepare the environment<br>- Create an IAM Role for Lambda with permissions to invoke EC2 actions and write logs to CloudWatch | 16/06/2026 | 16/06/2026 | [AWS Lambda IAM Permissions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) |
| 4 | - **Practice (Part 2)**: Implement Python Lambda code (boto3) to stop EC2 instances containing specific resource tags (e.g. `Environment=Dev`) | 17/06/2026 | 17/06/2026 | [Boto3 EC2 Client Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html) |
| 5 | - **Practice (Part 3)**: Implement Python Lambda code (boto3) to start EC2 instances<br>- Configure Incoming Webhooks on Slack to generate a webhook URL endpoint | 18/06/2026 | 18/06/2026 | [Slack Incoming Webhooks Guide](https://api.slack.com/messaging/webhooks) |
| 6 | - **Practice (Part 4)**: Integrate the Slack webhook payload notification within the Lambda functions and verify manually | 19/06/2026 | 19/06/2026 | [Sending Slack Messages with Lambda](https://api.slack.com/messaging/webhooks) |
| 7 - Sun | - **Practice (Part 5)**: Enable AWS Security Hub and standard security posture management (CSPM) compliance benchmarks, check score, and clean up resources | [20/06/2026](./Worklog_week1.9/) | [21/06/2026](./Worklog_week1.9/) | [AWS Security Hub User Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) |

### Week 9 Achievements:
- **Serverless Automation**: Successfully built a serverless scheduling solution using AWS Lambda (Python boto3) combined with EventBridge Scheduler rules to stop EC2 hosts at night and start them in the morning for cost optimization.
- **ChatOps Integration**: Integrated AWS Lambda alerts with Slack channel notifications using Slack Incoming Webhooks to report VM operations in real-time.
- **Resource Management**: Mastered bulk resource tagging using Tag Editor and logical grouping via AWS Resource Groups.
- **Security & Optimization**: Activated AWS Security Hub to evaluate compliance posture (CSPM) and performed thorough cleanup of all lab resources to optimize costs.

### Evidences:

1. **Create VPC (CreateVPC)**
   ![CreateVPC](../images/1-Worklog/Worklog_week1.9/CreateVPC.png)
   *Description: This image illustrates the AWS Management Console during the creation of a new Virtual Private Cloud (VPC). The process involves defining the IPv4 CIDR block, setting up Subnets across different Availability Zones for high availability, and configuring an Internet Gateway (IGW) along with Route Tables to route internet traffic to Public Subnets securely.*

2. **Create Security Group (Create Security Group)**
   ![Create Security Group](../images/1-Worklog/Worklog_week1.9/Create%20Security%20Group.png)
   *Description: This step involves setting up a virtual firewall at the instance level. The image displays the configuration of Inbound rules to open necessary network ports, such as port 22 for SSH remote management or port 80/443 for web traffic. This ensures that only specified IP addresses or network ranges can access the resources.*

3. **Launch EC2 Instance (Create Ec2)**
   ![Create Ec2](../images/1-Worklog/Worklog_week1.9/Create%20Ec2.png)
   *Description: The image captures a successful EC2 instance launch screen. The virtual machine has been provisioned with specific configurations (AMI, Instance Type, Key Pair). It resides in the previously created VPC and Subnet and is attached to the proper Security Group. This core compute resource will be used to test the automated Start/Stop Lambda functions.*

4. **Create IAM Role for Lambda (Create Role for lamda)**
   ![Create Role for lamda](../images/1-Worklog/Worklog_week1.9/Create%20Role%20for%20lamda.png)
   *Description: Displays the IAM (Identity and Access Management) console where a new Role is created specifically for the AWS Lambda service. This Role is attached with Policies that grant the Lambda function permissions to invoke EC2 API actions (like `ec2:StartInstances`, `ec2:StopInstances`) and write execution logs to CloudWatch Logs for debugging purposes.*

5. **Create Lambda Function to Stop Instance (Function stop instance)**
   ![Function stop instance](../images/1-Worklog/Worklog_week1.9/Function%20stop%20instance.png)
   *Description: Detailed view of the AWS Lambda service showing a function designed to automatically stop EC2 instances. The function's code (typically written in Python using Boto3) scans for EC2 instances with specific Tags (e.g., `Environment=Dev`) and executes the stop command. This significantly saves compute costs during non-working hours or at night.*

6. **Create Lambda Function to Start Instance (Function start instance)**
   ![Function start instance](../images/1-Worklog/Worklog_week1.9/Function%20start%20instance.png)
   *Description: Similar to the Stop function, this image illustrates the configuration of the Lambda function used to automatically start virtual machines. Triggered by an Amazon EventBridge cron schedule, this function runs at the beginning of the workday (e.g., 8:00 AM) to ensure systems are ready for use when employees start working.*

7. **Create EC2 Instance with Tags (Create EC2 Instance with tag)**
   ![Create EC2 Instance with tag](../images/1-Worklog/Worklog_week1.9/Create%20EC2%20Instance%20with%20tag.png)
   *Description: Evidence of advanced configuration when launching a new EC2 instance. In the Tags section, Key-Value pairs (e.g., `Project = FirstCloudJourney`, `Environment = Test`) are defined. Tagging at launch helps automated systems (like our Lambda functions) correctly identify target instances without affecting Production servers.*

8. **Add Tag to Existing EC2 (EC2 add tag)**
   ![EC2 add tag](../images/1-Worklog/Worklog_week1.9/EC2%20add%20tag.png)
   *Description: A screenshot of the Tags tab within a running EC2 instance's details. Through the console, additional metadata Tags are appended or modified for pre-existing servers. This is crucial for unified management, Cost Allocation tracking, and implementing Attribute-Based Access Control (ABAC) policies.*

9. **Manage Tags and Filter Resources (Managing Tags and Filter resources by tag)**
   ![Managing Tags and Filter resources by tag](../images/1-Worklog/Worklog_week1.9/Managing%20Tags%20and%20Filter%20resources%20by%20tag.png)
   *Description: Using the AWS Tag Editor or Resource Groups console to search across resources in bulk. Instead of checking individual services, the image shows how to filter all resources (EC2, VPC, Lambda, etc.) that share a specific Tag value. This feature provides administrators with a holistic view of the system architecture.*

10. **Create a Resource Group (Create a Resource Group)**
    ![Create a Resource Group](../images/1-Worklog/Worklog_week1.9/Create%20a%20Resource%20Group.png)
    *Description: The console view for creating a new AWS Resource Group. By utilizing Tag-based queries, the system groups scattered resources into a single logical collection. From this Resource Group, users can safely and quickly perform bulk administrative actions via AWS Systems Manager.*

11. **Configure Slack Incoming Web-hooks (Incoming Web-hooks slack)**
    ![Incoming Web-hooks slack](../images/1-Worklog/Worklog_week1.9/Incoming%20Web-hooks%20slack.png)
    *Description: The configuration interface of the Slack application to generate an Incoming Webhook URL. This webhook acts as an endpoint to receive data payloads. In this lab, whenever the Lambda functions execute the Start/Stop actions, they send a payload containing the result notification (success/failure) through this webhook directly to the operations team's chat channel (ChatOps).*

12. **Check Result (Check Result)**
    ![Check Result](../images/1-Worklog/Worklog_week1.9/Check%20Result.png)
    *Description: Concrete proof that the automation system operates flawlessly. The image captures the Slack application screen showing automated alert messages sent from AWS in real-time. Administrators can instantly know the status of virtual machines (stopped or started) without logging into the AWS Console, embodying the ChatOps philosophy.*

13. **Enable AWS Security Hub CSPM (Enable AWS Security Hub CSPM)**
    ![Enable AWS Security Hub CSPM](../images/1-Worklog/Worklog_week1.9/Enable%20AWS%20Security%20Hub%20CSPM.png)
    *Description: The central dashboard of AWS Security Hub. The Cloud Security Posture Management (CSPM) feature has been activated to scan the entire account based on industry-standard security frameworks (like AWS Foundational Security Best Practices). The interface displays the compliance score chart and lists misconfigurations or vulnerabilities that need remediation.*

14. **Clean Up Security Hub (Clean Security Hub)**
    ![Clean Security Hub](../images/1-Worklog/Worklog_week1.9/Clean%20Security%20Hub.png)
    *Description: Evidence of disabling and deleting data from AWS Security Hub within its Settings. Since Security Hub incurs charges based on the number of security checks performed, turning off this service after completing the lab is essential to prevent unexpected ongoing monthly fees.*

15. **Clean Up Tags (Clean Tags)**
    ![Clean Tags](../images/1-Worklog/Worklog_week1.9/Clean%20Tags.png)
    *Description: Illustrates the use of Tag Editor to mass-delete the Tags created across multiple resources. This cleanup step keeps the AWS environment organized, preventing stale tags from cluttering cost reporting tools or disrupting other automated rule sets in the system.*

16. **Clean Up EC2, Lambda, and CloudWatch (Clean Ec2 and lamda and cloudwatch)**
    ![Clean Ec2 and lamda and cloudwatch](../images/1-Worklog/Worklog_week1.9/Clean%20Ec2%20and%20lamda%20and%20cloudwatch.png)
    *Description: The final environment cleanup step (Terminate/Delete resources). The image shows the deletion of EC2 virtual machines, unused Lambda functions, and importantly, the removal of CloudWatch Log Groups. If left indefinitely, Log Groups can accumulate storage costs, so deleting them thoroughly ensures maximum Cost Optimization.*

---

## Week 10:
### Week 10 Objectives:
- Understand and configure VPC Peering to connect two separate VPC networks, configure routing rules, and verify Cross-Peer DNS resolution.
- Set up and verify Network Access Control Lists (NACLs) for subnet-level stateless security filtering within VPCs.
- Learn and deploy AWS Transit Gateway (TGW) as a central cloud router to connect multiple VPCs in a Hub-and-Spoke model, simplifying large-scale network architecture.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn concepts of VPC Peering and Network Access Control Lists (NACLs)<br>- **Lab 19 (Part 1)**: Set up baseline network environment using CloudFormation, create Security Groups and EC2s | 22/06/2026 | 22/06/2026 | [VPC Peering Guide](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html)<br>[VPC ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) |
| 3 | - **Lab 19 (Part 2)**: Configure Custom VPC Peering, create VPC Peering connection, update route tables, and verify Cross-Peer DNS resolution | 23/06/2026 | 23/06/2026 | [Network Peering DNS Support](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) |
| 4 | - **Lab 19 (Part 3)**: Configure Network ACLs (NACLs) at the subnet level to filter ICMP and SSH traffic, verify stateless filtering behavior, and compare it with stateful Security Groups | 24/06/2026 | 24/06/2026 | [VPC ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) |
| 5 | - Learn AWS Transit Gateway (TGW) concepts and the advantages of a Hub-and-Spoke model<br>- **Lab 20 (Part 1)**: Set up 3 VPCs for demonstration using CloudFormation | 25/06/2026 | 25/06/2026 | [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) |
| 6 | - **Lab 20 (Part 2)**: Create Transit Gateway and configure VPC attachments | 26/06/2026 | 26/06/2026 | [Transit Gateway Attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html) |
| 7 - Sun | - **Lab 20 (Part 3)**: Setup Transit Gateway Route Tables, add Routes to TGW Route Tables, and verify cross-VPC network connectivity<br>- Perform resource cleanup to prevent ongoing AWS charges | [27/06/2026](./Worklog_week1.10/) | [28/06/2026](./Worklog_week1.10/) | [TGW Route Tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html) |

### Week 10 Achievements:
- **VPC Peering & Security**: Successfully established a private network link between two isolated VPCs; applied Network ACLs to control inbound/outbound packets and gained deep knowledge of stateless NACL behavior versus stateful Security Groups.
- **Transit Gateway Deployment**: Implemented a centralized Hub-and-Spoke network interconnecting 3 VPCs using AWS Transit Gateway, eliminating the need for a complex full-mesh peering topology and allowing scalable network expansion.
- **Cost Optimization**: Performed a thorough cleanup of all networking and compute resources to prevent unexpected charges.

### Evidences:

1. **VPC Peering CloudFormation Stack Creation (Create_Stack)**
   ![VPC Peering Stack](../images/1-Worklog/Worklog_week1.10/Create_Stack.png)
   *Description: This image captures the successful initiation and creation of the AWS CloudFormation stack used to rapidly provision the baseline network environment for the VPC Peering lab. Utilizing Infrastructure as Code (IaC) ensures that all necessary VPCs, subnets, route tables, and instances are deployed consistently and accurately. The stack creates the foundational 'My VPC' and 'HG VPC' which will subsequently be peered, allowing for a structured and repeatable learning experience without manual setup overhead.*

2. **Security Group Configuration for My VPC (Create_MY VPC SG)**
   ![My VPC Security Group](../images/1-Worklog/Worklog_week1.10/Create_MY%20VPC%20SG.png)
   *Description: Depicts the specific Security Group rules configured for 'My VPC'. Security groups act as stateful virtual firewalls at the instance level. In this configuration, inbound rules are carefully defined to permit SSH (port 22) and ICMP (ping) traffic originating only from trusted IP addresses or specifically from the peered VPC CIDR block. This demonstrates the principle of least privilege, ensuring that even when VPCs are connected, instances remain protected against unauthorized access attempts from the broader network.*

3. **Security Group Configuration for HG VPC (Create_HG VPC SG)**
   ![HG VPC Security Group](../images/1-Worklog/Worklog_week1.10/Create_HG%20VPC%20SG.png)
   *Description: Shows the corresponding Security Group configuration for instances located within the 'HG VPC' (the peered network). Similar to the previous setup, this firewall rule is tailored to accept incoming traffic strictly from the 'My VPC' CIDR range. By configuring these rules symmetrically across both VPCs, we establish a secure bidirectional communication channel, which is essential for verifying connectivity testing (like pinging instances) after the peering connection is actively established.*

4. **EC2 Instances Provisioning (Create EC2)**
   ![Create EC2 Instances](../images/1-Worklog/Worklog_week1.10/Create%20EC2.png)
   *Description: Illustrates the successful launch and running state of the EC2 instances deployed across the different VPCs (e.g., one instance in 'My VPC' and another in 'HG VPC'). These virtual servers act as the primary endpoints for our network connectivity tests. Verifying that these instances are running and possess the correct private IP addresses within their respective subnets is a critical prerequisite before attempting to validate the VPC peering routes and security group rules.*

5. **Establishing VPC Peering Connection (MyVPC peering to HG VPC)**
   ![VPC Peering Connection](../images/1-Worklog/Worklog_week1.10/MyVPC%20peering%20to%20HG%20VPC.png)
   *Description: Highlights the core objective of the lab—the active and functioning VPC Peering connection linking 'My VPC' to 'HG VPC'. A peering connection is a networking connection between two VPCs that enables the routing of traffic between them using private IPv4 or IPV6 addresses. This image confirms that the connection request was accepted, changing the status to 'Active', thereby virtually merging the two separate network segments into a continuous private network space without traversing the public internet.*

6. **Route Table Updates for Peering (route_table)**
   ![Route Table Configuration](../images/1-Worklog/Worklog_week1.10/route_table.png)
   *Description: Displays the crucial modifications made to the VPC route tables. For instances in one VPC to communicate with instances in the peered VPC, the route tables associated with their subnets must be updated. This screenshot shows the addition of a specific route where the destination is the CIDR block of the peered VPC, and the target is the newly created VPC Peering Connection ID (pcx-...). Without this exact routing configuration, the peering connection remains unutilized, and packets would simply be dropped.*

7. **Network Access Control List (NACL) Verification (ALI)**
   ![Network ACL Configuration](../images/1-Worklog/Worklog_week1.10/ALI.png)
   *Description: Presents the configuration and testing of Network ACLs (NACLs). Unlike Security Groups, NACLs act as stateless firewalls at the subnet level, meaning both inbound and outbound rules must be explicitly defined. This part of the lab emphasizes the difference between stateful and stateless filtering. The image demonstrates how modifying a NACL to block or allow specific traffic (like ICMP or SSH) immediately impacts the entire subnet, providing an additional, broader layer of network security defense beyond individual instance firewalls.*

8. **Initialize CloudFormation Template (Initialize CloudFormation Template)**
   ![Initialize CloudFormation Template](../images/1-Worklog/Worklog_week1.10/Initialize%20CloudFormation%20Template.png)
   *Description: This image shows the first step in setting up the environment using AWS CloudFormation. Running the template automates the creation of VPCs, Subnets, Route Tables, and basic network resources required for the Transit Gateway lab. This is an efficient method to build infrastructure quickly and consistently rather than creating resources manually via the console.*

9. **Create Security Key Pair (Create_key_pair)**
   ![Create Key Pair](../images/1-Worklog/Worklog_week1.10/Create_key_pair.png)
   *Description: The process of creating a new Amazon EC2 Key Pair is displayed here. The Key Pair (public key stored on AWS and private key downloaded by the user) acts as a crucial authentication mechanism, allowing administrators secure SSH access to the EC2 instances that will be launched in the VPCs. Careful management of security keys is a fundamental principle in cloud security.*

10. **Create AWS Transit Gateway (Create Transit gateways)**
   ![Create Transit Gateway](../images/1-Worklog/Worklog_week1.10/Create%20Transit%20gateways.png)
   *Description: This image captures the successful initialization of the AWS Transit Gateway (TGW) resource. TGW acts as a central hub (cloud router) to connect multiple VPCs and on-premises networks, helping to replace complex full-mesh VPC Peering architectures with a simple, scalable, and centrally managed hub-and-spoke model.*

11. **Attach VPCs to Transit Gateway (Create Transit gateway attachments)**
   ![Create Transit Gateway Attachments](../images/1-Worklog/Worklog_week1.10/Create%20Transit%20gateway%20attachments.png)
   *Description: The next step after creating the TGW is attaching specific VPC networks to this central hub. The screenshot illustrates the TGW Attachments creation process, linking the VPCs to the Transit Gateway. This allows network traffic from subnets within a VPC to be routed to the TGW and onward to other destination networks.*

12. **Configure Transit Gateway Route Tables (Create Transit gateway route tables)**
   ![Create Transit Gateway Route Tables](../images/1-Worklog/Worklog_week1.10/Create%20Transit%20gateway%20route%20tables.png)
   *Description: This image displays the creation and configuration of Transit Gateway Route Tables. Unlike VPC Route Tables, TGW Route Tables control how packets are routed after they reach the Transit Gateway. By using multiple route tables, administrators can establish complex routing policies (e.g., isolating VPCs, or allowing specific VPCs to communicate with each other).*

13. **Update TGW Routing Rules (Create Transit gateway route tables 1)**
   ![Create Transit Gateway Route Tables 1](../images/1-Worklog/Worklog_week1.10/Create%20Transit%20gateway%20route%20tables%201.png)
   *Description: Details the process of updating routing records (routes) inside the TGW Route Table. Specifying the destination CIDR and the corresponding attachment target ensures that packets know the exact path to reach the destination VPC. This is a critical step to establish cross-network (cross-VPC) communication capabilities.*

14. **Verify Network Routing via TGW (Transit Gateway Route result & result 1)**
   ![Transit Gateway Route result](../images/1-Worklog/Worklog_week1.10/Transit%20Gateway%20Route%20result.png)
   ![Transit Gateway Route result 1](../images/1-Worklog/Worklog_week1.10/Transit%20Gateway%20Route%20result%201.png)
   *Description: These images serve as evidence that routing through the Transit Gateway is functioning correctly. Successful ping or trace route results from a server in one VPC to a server in another VPC prove that the hub-and-spoke network is operational. The entire network architecture, from the subnet Route Tables to the TGW Route Tables, has been synchronized successfully.*

15. **Resource Cleanup for Cost Optimization (Clean)**
   ![Clean 1](../images/1-Worklog/Worklog_week1.10/clean%201.png)
   ![Clean 2](../images/1-Worklog/Worklog_week1.10/clean%202.png)
   ![Clean](../images/1-Worklog/Worklog_week1.10/Clean.png)
   *Description: This final sequence of images records the "tear down" process of lab resources, including deleting Transit Gateway Attachments, deleting the Transit Gateway, terminating EC2 instances, and deleting CloudFormation stacks. Proactively deleting resources after completing a lab is an extremely important practice on AWS to prevent unexpected charges (cost optimization).*

---

## Week 11:
### Week 11 Objectives:
- Understand the core concepts of AWS Storage Gateway and hybrid cloud storage models.
- Practice deploying and configuring AWS File Storage Gateway to connect on-premises storage infrastructure with Amazon S3 cloud storage.
- Mount NFS/SMB File Shares from the Storage Gateway onto a Linux client (simulating an on-premises host).

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Study the theoretical concepts of AWS Storage Gateway, its types, and hybrid cloud storage architectures | 29/06/2026 | 29/06/2026 | [AWS Storage Gateway Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/WhatIsStorageGateway.html) |
| 3 | - **Practice (Part 1)**: Create an Amazon S3 Bucket to act as the backend storage for the Storage Gateway | 30/06/2026 | 30/06/2026 | [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/) |
| 4 | - **Practice (Part 2)**: Launch a Linux EC2 instance to simulate an on-premises client host | 01/07/2026 | 01/07/2026 | [Amazon EC2 User Guide](https://docs.aws.amazon.com/ec2/) |
| 5 | - **Practice (Part 3)**: Deploy and configure the AWS File Storage Gateway via the AWS Console | 02/07/2026 | 02/07/2026 | [Creating a File Gateway](https://docs.aws.amazon.com/storagegateway/latest/userguide/CreatingAnAppliance.html) |
| 6 | - **Practice (Part 4)**: Create a File Share on the Storage Gateway and associate it directly with the S3 bucket | 03/07/2026 | 03/07/2026 | [Creating a File Share](https://docs.aws.amazon.com/storagegateway/latest/userguide/CreatingAFileShare.html) |
| 7 - Sun | - **Practice (Part 5)**: Mount the NFS File Share onto the simulated Linux host (EC2 instance), verify data synchronization from the host to the S3 bucket<br>- Tear down and clean up all lab resources to prevent ongoing charges | [04/07/2026](./Worklog_week1.11/) | [05/07/2026](./Worklog_week1.11/) | [Mounting a File Share](https://docs.aws.amazon.com/storagegateway/latest/userguide/mounting-file-share.html) |

### Week 11 Achievements:
- **AWS Storage Gateway Configuration**: Mastered hybrid cloud storage mechanisms and successfully configured AWS File Storage Gateway to link simulated on-premises file storage with AWS S3 using standard file sharing protocols.
- **Hybrid Infrastructure Integration**: Successfully mounted NFS File Shares and verified seamless automated file synchronization between local and cloud environments.
- **Cost Optimization**: Cleaned up all provisioned Storage Gateway resources, virtual hosts, and storage buckets to prevent ongoing monthly charges.

### Evidences:

1. **Create S3 Bucket (Create s3 bucket)**
   ![Create s3 bucket](../images/1-Worklog/Worklog_week1.11/Create%20s3%20bucket.png)
   *Description: The process of creating an Amazon S3 Bucket to serve as the data storage backend for the Storage Gateway. S3 provides secure, durable, and highly scalable object storage, acting as the final destination for files shared via the File Gateway.*

2. **Launch EC2 Instance (Create EC2)**
   ![Create EC2](../images/1-Worklog/Worklog_week1.11/Create%20EC2.png)
   *Description: Deploying a new virtual machine (EC2 instance) to act as a simulated on-premises server. This instance will be configured to mount the File Share provided by the Storage Gateway to test file storage capabilities to S3 from a local network environment.*

3. **Initialize Storage Gateway (Create Storage GateWay)**
   ![Create Storage GateWay](../images/1-Worklog/Worklog_week1.11/Create%20Storage%20GateWay.png)
   *Description: The configuration and initialization interface of the AWS File Storage Gateway. The Storage Gateway acts as a bridge between on-premises applications and the AWS cloud storage ecosystem. It provides standard SMB/NFS protocols so legacy applications can seamlessly save files to S3 without code refactoring.*

4. **Set Up File Share (Create File Share)**
   ![Create File Share](../images/1-Worklog/Worklog_week1.11/Create%20File%20Share.png)
   *Description: The process of setting up a File Share on the newly created Storage Gateway. This file share is directly linked to the S3 bucket. Any file written to this file share via NFS/SMB is automatically uploaded to S3 as an object by the Gateway.*

5. **Mount File Share to On-premises Machine (Mount File shares on On-premises machine)**
   ![Mount File shares on On-premises machine](../images/1-Worklog/Worklog_week1.11/Mount%20File%20shares%20on%20On-premises%20machine.png)
   *Description: Executing the command to mount the shared directory from the Storage Gateway onto the EC2 instance (simulated on-premises server). The image demonstrates a successful connection, allowing users or applications to transparently read/write data to S3 through a local network directory.*

6. **Clean Up Resources (Clean)**
   ![Clean](../images/1-Worklog/Worklog_week1.11/Clean.png)
   *Description: The operation of deleting the created resources (Storage Gateway, File Share, S3 Bucket, EC2 Instance) after completing the hands-on lab. This is a crucial principle for Cost Optimization, ensuring no redundant resources are left running unintentionally.*

---

## Week 12:
### Week 12 Objectives:
- **Synthesis & Review:** Summarize, evaluate, and check the entire 12-week study, research, and hands-on practice journey of the First Cloud Journey program.
- **Systems Administration:** Utilize AWS Systems Manager (SSM) suite, including Fleet Manager, Patch Manager, and Run Command, to manage and operate Windows Server fleets.
- **Advanced Access Controls:** Configure IAM Tag-based Access Control for EC2 resources and set up IAM Permissions Boundaries to restrict maximum delegated permissions of IAM Entities.
- **Advanced Monitoring:** Explore the open-source monitoring tool Grafana to design intuitive resource observation dashboards.
- **Attendance Auditing:** Review and verify complete attendance logs and check-in history across the 12-week timeline.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn IAM Tag-based Access Control<br>- Read guides and configure IAM Tags for controlling access to EC2 resources | 06/07/2026 | 06/07/2026 | <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html" target="_blank">AWS IAM Tagging</a> |
| 3 | - Learn Grafana monitoring basics<br>- Read and understand Grafana concepts and set up a basic Dashboard | 07/07/2026 | 07/07/2026 | <a href="https://grafana.com/docs/grafana/latest/" target="_blank">Grafana User Guide</a> |
| 4 | - Learn IAM Permission Boundary<br>- Configure permission boundaries to limit the maximum permissions of IAM Entities | 08/07/2026 | 08/07/2026 | <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html" target="_blank">AWS Permissions Boundaries</a> |
| 5 | - Learn AWS Systems Manager (SSM) concepts<br>- Study introduction to SSM, Fleet Manager, Patch Manager, and Run Command | 09/07/2026 | 09/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html" target="_blank">AWS Systems Manager User Guide</a> |
| 6 | - Set up network infrastructure and IAM Roles for SSM<br>- Create VPC `windows-lab-ssm`, Internet Gateway, 2 Subnets<br>- Create IAM Role/Instance Profile with `AmazonSSMManagedInstanceCore` policy<br>- Launch 2 Windows Server EC2 instances attached with the IAM Role | 10/07/2026 | 10/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html" target="_blank">SSM Agent on Windows Server</a> |
| 7 - Sun | - Execute patching and remote commands via SSM<br>- Use Patch Manager to scan vulnerabilities and auto-install OS updates<br>- Use Run Command to run PowerShell `net user` remotely and store logs in S3<br>- Review the entire 12-week learning path and perform final cleanup of resources | [11/07/2026](./Worklog_week1.12/) | [12/07/2026](./Worklog_week1.12/) | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html" target="_blank">SSM Patch Manager</a><br><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html" target="_blank">SSM Run Command</a> |

### Week 12 Achievements:

#### 1. Synthesis of the 12-Week Study & Research Path:
Over the 12-week timeline of the **First Cloud Journey** program, all knowledge milestones have been successfully completed:
* **Weeks 1 - 2 (Onboarding & Cost Guardrails):** Onboarded with the team, studied fundamental S3/EC2 concepts, and set up financial safety checks using **AWS Budgets**.
* **Weeks 3 - 4 (Compute & Database Infrastructures):** Deployed EC2 instances (Public/Private Subnets), customized IAM policies, and connected application code to **Amazon RDS** databases (configuring Multi-AZ, Backups, and Snapshots).
* **Weeks 5 - 6 (High Availability & Monitoring):** Designed scalable structures with **Auto Scaling Groups**, **Load Balancers**, **CloudFront**, and **Route 53** fallback. Built alerting networks using **Amazon CloudWatch** (Metrics, Alarms, Logs Insights).
* **Weeks 7 - 8 (Automation & Audit Security):** Automated setups via **AWS CLI** and scheduled automated backup plans using **AWS Backup**. Enhanced security with **AWS S3 SSE-KMS**, audited API calls with **AWS CloudTrail**, and queried logs via **Amazon Athena**.
* **Weeks 9 - 11 (Serverless Operations & Enterprise Networking):** Automated EC2 states using **AWS Lambda** & **EventBridge** rules with Slack messaging (ChatOps). Designed multi-VPC networks via **VPC Peering**, **Transit Gateway**, and hybrid storage connectivity with **AWS Storage Gateway (NFS)**.
* **Weeks 12 (Centralized Systems Management & Completion):** Enforced safety via **IAM Permissions Boundaries** and **Tag-based Access Control**. Deployed **AWS Systems Manager (SSM)** to manage hosts, patch OS vulnerabilities (Patch Manager), and run remote scripts (Run Command) without opening management ports (SSH/RDP).

#### 2. Results in Week 12:
* Week 12 was dedicated entirely to literature review, conceptual studies, and compiling the final report. No cloud resources were provisioned or modified on the AWS platform.
* Audited and verified full attendance history and check-ins for the entire course.

### Evidences & Attendance History:

1. **Attendance History - Part 1**
   ![Attendance History 1](/images/1-Worklog/Worklog_week1.12/Attendance%20history%201.png)
   *Description: Captures the attendance log from the initial phase of the training program on the student portal, confirming attendance in all theoretical lectures, syncs, and tasks.*

2. **Attendance History - Part 2**
   ![Attendance History 2](/images/1-Worklog/Worklog_week1.12/Attendance%20history%202.png)
   *Description: Shows the attendance history for the subsequent phase, reflecting high discipline, persistence, and continuous learning achievements.*

3. **General Attendance History**
   ![General Attendance History](/images/1-Worklog/Worklog_week1.12/Attendance%20history.png)
   *Description: The summary attendance report indicating 100% attendance rate throughout the 12-week First Cloud Journey program, documenting completion of all training obligations.*

4. **Selfie Check-in at the Internship Office (Attendance history picture checkin)**
   ![Selfie Check-in](/images/1-Worklog/Worklog_week1.12/Attendance%20history%20picture%20checkin.png)
   *Description: Selfie of the student during a collaborative working and sync session at the internship office, showing active physical attendance, engagement, and team coordination.*
