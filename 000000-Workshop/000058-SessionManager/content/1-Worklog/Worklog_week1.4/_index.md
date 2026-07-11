---
title: "Week 4 Worklog"
date: 2026-05-13
weight: 4
chapter: false
pre: " <b> 1.4 </b> "
---

## Week 4 Objectives:
- Initialize and configure an Amazon RDS database instance.
- Connect an application running on EC2 to the RDS database.
- Understand Backup, Restore mechanisms, and advanced features (Multi-AZ, Read Replicas).

## Tasks to be implemented this week:

| Day | Task | Start Date | End Date | Resource |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Overview of Amazon RDS<br>- Compare RDS with other storage services (EC2 DB, DynamoDB, Redshift) | 11/05/2026 | 11/05/2026 | [Amazon RDS Documentation](https://docs.aws.amazon.com/rds/) |
| 3 | - Network setup for RDS:<br>  + Create VPC<br>  + Create Security Groups for EC2 and RDS<br>  + Create DB Subnet Group | 12/05/2026 | 12/05/2026 | [VPC for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) |
| 4 | - Practice initializing an Amazon RDS instance<br>- Configure parameters and security options for the Database | 13/05/2026 | 13/05/2026 | [Creating an RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) |
| 5 | - Deploy application on EC2 and connect to RDS<br>- Verify access and data management via Endpoint | 14/05/2026 | 14/05/2026 | [Connecting to RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html) |
| 6 | - Learn and practice Backup & Restore<br>- Practice manual and automatic Snapshots | 15/05/2026 | 15/05/2026 | [RDS Backup and Restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html) |
| 7 - Sun | - Learn about Multi-AZ and Read Replicas<br>- Resource cleanup to optimize costs | 16/05/2026 | 17/05/2026 | [High Availability (Multi-AZ)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) |

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

### Evidences:

1. **SSH Key Pair Permissions Configuration (ec2_connection_key)**
   ![SSH Key Pair Permissions](/images/1-Worklog/Worklog_week1.4/ec2_connection_key.png)
   *Description: Demonstrates setting the appropriate permissions on the private key file (`.pem`) using the `chmod 400` command in the CLI. Restricting read/write permissions is a security requirement for SSH connections to prevent private keys from being exposed or utilized by other local users before establishing a connection.*

2. **Successful SSH Connection to Linux EC2 Public Instance (ec2_connection)**
   ![Successful SSH Connection](/images/1-Worklog/Worklog_week1.4/ec2_connection.png)
   *Description: Captures the CLI output of a successful SSH login session from the local client to the EC2 Public Instance using the configured Key Pair. The successful Amazon Linux terminal greeting confirms that the Internet Gateway routing and the Security Group's inbound rule for port 22 are operational.*

3. **Internal Routing and Connection to EC2 Private Instance (ec2_connection_Private)**
   ![Internal Connection to Private Instance](/images/1-Worklog/Worklog_week1.4/ec2_connection_Private.png)
   *Description: Practical evidence of successfully establishing an internal connection to the EC2 Private Subnet Instance from the EC2 Public Instance acting as a Bastion Host. Since the Private Instance has no public IP, this jump-host method ensures secure network containment and management.*

