---
title: "Week 7 Worklog"
date: 2026-05-13
weight: 7
chapter: false
pre: " <b> 1.7 </b> "
---

## Week 7 Objectives:
- Get familiar with and practice using the AWS Command Line Interface (CLI) to view, configure, and manage AWS resources (S3, SNS, IAM, VPC, EC2).
- Understand multi-account management using AWS Organizations, configuring Organizational Units (OUs), and IAM Identity Center.
- Master centralized backup solutions using AWS Backup to protect data safety on AWS.

## Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn AWS CLI & Installation<br> - View resources via CLI<br> - AWS CLI with Amazon S3 and Amazon SNS | 01/06/2026 | 01/06/2026 | [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)<br> [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/) |
| 3 | - AWS CLI with IAM and VPC (VPC, Internet Gateway)<br> - Practice creating EC2 via AWS CLI | 02/06/2026 | 02/06/2026 | [AWS CLI for EC2 & VPC](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2.html)<br> [AWS CLI for IAM](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-iam.html) |
| 4 | - Learn AWS Organizations<br> - Create member accounts, configure Organizational Unit (OU) and invite AWS Accounts | 03/06/2026 | 03/06/2026 | [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)<br> [Creating account in Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) |
| 5 | - Configure Member Account access via CLI<br> - Configure Time-based access control & Customer Managed Policies<br> - Understand IAM Identity Center Identity Store APIs | 04/06/2026 | 04/06/2026 | [AWS IAM Identity Center Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)<br> [Identity Store APIs](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/Welcome.html) |
| 6 | - Learn AWS Backup service<br> - Prepare environment: Create S3 Bucket & Deploy backup infrastructure | 05/06/2026 | 05/06/2026 | [What is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)<br> [Backup S3 with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html) |
| 7 - Sun | - Setup Backup plan & configure notifications<br> - Test Restore operations<br> - Clean up resources to prevent charges | 06/06/2026 | 07/06/2026 | [Creating backup plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)<br> [Restoring a backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) |

## Week 7 Achievements:
### Theory:
- Understood how to configure and invoke AWS service APIs via the AWS CLI.
- Mastered enterprise-scale account management with AWS Organizations and IAM Identity Center, including time-based access controls and Customer Managed Policies.
- Understood the core mechanism of AWS Backup: Backup Vaults, Backup Plans, Retention rules, and data restoration (Restore).

### Practice:
- Proficiently used CLI commands to query and manage EC2, S3, IAM, and VPC resources.
- Successfully built an automated backup system (AWS Backup Plan) for EC2 server infrastructure and S3 storage.
- Successfully performed recovery testing (Test Restore) from backup points and executed cleanups for Cost Optimization.

### Evidences:

1. **Deploy Infrastructure (Deploy infrastructure)**
   ![Deploy infrastructure](../../images/1-Worklog/Worklog_week1.7/Deloy%20infrastructure.png)
   *Description: The process of deploying the foundational infrastructure for the lab using AWS CloudFormation. Necessary resources such as EC2 instances, EBS volumes, or basic network configurations are automatically provisioned. This is a crucial preparation step to have actual resources for testing backup and restore capabilities.*

2. **Create S3 Folder (Create s3 folder)**
   ![Create S3 Folder](../../images/1-Worklog/Worklog_week1.7/Create%20s3%20folder.png)
   *Description: Initializing a directory or bucket on Amazon S3. S3 is commonly used as a secure, durable, and cost-effective storage location for backups (backup vault/storage) from AWS Backup or other services. Setting up a proper storage structure ensures that backup data is well-organized and easily retrievable when needed.*

3. **Configure Backup Plans (Create Backup plans)**
   ![Create Backup plans](../../images/1-Worklog/Worklog_week1.7/Create%20Backup%20plans.png)
   *Description: Configuring an AWS Backup plan. This step establishes rules for automating the backup process, including backup frequency (e.g., daily, weekly), retention period, and backup window. Automated backup management helps organizations comply with data security regulations without manual operational overhead.*

4. **Test Data Restoration (Test Restore)**
   ![Test Restore](../../images/1-Worklog/Worklog_week1.7/Test%20Restore.png)
   *Description: Executing the data restoration process from a previously created backup (recovery point). This is the most critical validation step in any backup strategy, ensuring that in the event of data loss or system failure, data can be restored intact and systems can return to normal operation.*

5. **Clean Up Resources (Clean up resources)**
   ![Clean up resources](../../images/1-Worklog/Worklog_week1.7/Clean%20up%20resources.png)
   *Description: Deleting the AWS resources created during the hands-on lab (such as EC2, S3, Backup plans, CloudFormation stacks). Careful cleanup after completing the lab is a mandatory best practice for Cost Optimization, ensuring the account does not incur ongoing charges for unused resources.*
