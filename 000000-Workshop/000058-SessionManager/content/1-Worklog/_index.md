---
title: "Worklog"
date: 2026-04-27
weight: 1
pre : " <b> 1. </b> "
---

## Week 1:
- Connect and get acquainted with members of First Cloud Journey.
- Understand basic AWS services, how to use the console & CLI.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Get acquainted with FCJ members<br>- Read and take note of the rules and regulations at the internship unit | 20/04/2026 | 20/04/2026 |  |
| 3 | - Learn about AWS and its service categories<br>  + Compute<br>  + Storage<br>  + Networking<br>  + Database<br>  + ... | [21/04/2026](./Worklog_week1.1/) | [21/04/2026](./Worklog_week1.1/) | https://cloudjourney.awsstudygroup.com/ |
| 4 | - Create an AWS Free Tier account<br>- Learn about AWS Console & AWS CLI<br>- **Practice:**<br>  + Create an AWS account<br>  + Install and configure AWS CLI<br>  + Learn how to use AWS CLI | 22/04/2026 | 22/04/2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | - Learn the basics of EC2:<br>  + Instance types<br>  + AMI<br>  + EBS<br>  + ...<br>- Explore methods for remotely connecting to EC2 via SSH<br>- Learn about Elastic IP | 23/04/2026 | 23/04/2026 | https://cloudjourney.awsstudygroup.com/ |
| 6 | - **Practice:**<br>  + Create an EC2 instance<br>  + Connect via SSH<br>  + Attach an EBS volume | 24/04/2026 | 24/04/2026 | https://cloudjourney.awsstudygroup.com/ |
| 7 - Sun | - **Advanced practice:**<br>  + Recreate the EC2 instance and configure the Security Group<br>  + Connect via SSH and install a Web Server (Apache/Nginx)<br>  + Deploy a simple website and access it through the Public IP<br>  + Learn and experiment with AWS S3 (create a bucket, upload files) | 25/04/2026 | 26/04/2026 | https://cloudjourney.awsstudygroup.com/ |

---

## Week 2:
### Week 2 Objectives:
- Understand basic networking in AWS (VPC)
- Master how to configure network components and security within a VPC
- Practice building a complete VPC

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn VPC basics:<br>  + VPC Overview<br>  + CIDR Block<br>  + Distinguish Public / Private Subnets | 27/04/2026 | 27/04/2026 | [VPC Basics](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) |
| 3 | - Learn about subnets & Route Tables:<br>  + How to divide subnets<br>  + Configure Route Tables | [28/04/2026](./Worklog_week1.2/) | [28/04/2026](./Worklog_week1.2/) | [Subnets & Route Tables](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html) |
| 4 | - Learn about Internet Gateway & NAT Gateway:<br>  + Internet Gateway for Public Subnets<br>  + NAT Gateway for Private Subnets | 29/04/2026 | 29/04/2026 | [NAT Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) |
| 5 | - Learn about security in VPC:<br>  + Security Groups<br>  + Network ACLs<br>  + Inbound / Outbound rules | 30/04/2026 | 30/04/2026 | [VPC Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) |
| 6 | - **Practice:**<br>  + Create VPC<br>  + Create Public & Private Subnets<br>  + Configure Route Tables | 01/05/2026 | 01/05/2026 | [FCJ Lab - Create VPC](https://cloudjourney.awsstudygroup.com/2-prerequisites/2.1-createvpc/) |
| 7 - Sun | - **Advanced practice:**<br>  + Attach Internet Gateway<br>  + Create NAT Gateway<br>  + Deploy EC2 in Private/Public Subnets<br>  + Verify internet connectivity | 02/05/2026 | 03/05/2026 | [FCJ Lab - Public/Private](https://cloudjourney.awsstudygroup.com/2-prerequisites/2.2-publicprivateinstance/) |

### Week 2 Achievements:
#### Theory:
- Can understand the architecture of Amazon VPC and how to manage IP address ranges via CIDR
- Know how to create and configure route tables

---

## Week 3:
### Week 3 Objectives:
- Learn about Amazon EC2 services on AWS.
- Practice initializing, configuring, and managing EC2 Instances.
- Deploy Node.js applications on Linux and Windows environments.

### Tasks to implement this week:

| Day | Tasks | Start Date | Completion Date | Reference Sources |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Overview of Amazon EC2<br>- Learn about Instance Types, AMI, Key Pair, and Snapshot<br>- Understand the mechanism of EC2 Instances | 05/04/2026 | 05/04/2026 | [Amazon EC2 Basics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 3 | - Prepare EC2 environment<br>+ Create VPC for Linux<br>+ Create VPC for Windows<br>+ Create Security Group for Linux and Windows Instances | [05/05/2026](./Worklog_week1.3/) | [05/05/2026](./Worklog_week1.3/) | [EC2 Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)<br>FCJ Lab |
| 4 | - Initialize Windows EC2 Instance<br>+ Create Windows Instance<br>+ Connect via Remote Desktop to Windows Instance | 05/06/2026 | 05/06/2026 | [EC2 Windows Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 5 | - Initialize Linux EC2 Instance<br>+ Create Linux Instance<br>+ Connect via SSH to Linux Instance<br>- Learn about changing EC2 configuration and managing EBS Snapshot | 05/07/2026 | 05/07/2026 | [EC2 Linux Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 6 | - Advanced EC2 Practice<br>+ Create Custom AMI<br>+ Create Instance from Custom AMI<br>+ Practice EC2 access when losing Key Pair | 05/08/2026 | 05/08/2026 | [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)<br>FCJ Lab |
| 7 - Sun | - Deploy Node.js application on EC2<br>+ Install LAMP/XAMPP Server<br>+ Install Node.js on Linux and Windows<br>+ Deploy Node.js application<br>- Learn about resource limits using IAM | 05/09/2026 | 05/10/2026 | [IAM for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html)<br>FCJ Lab |

---

## Week 4:
### Week 4 Objectives:
- Initialize and configure an Amazon RDS database instance.
- Connect an application running on EC2 to the RDS database.
- Understand Backup, Restore mechanisms, and advanced features (Multi-AZ, Read Replicas).

### Tasks to be implemented this week:

| Day | Task | Start Date | End Date | Resource |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Overview of Amazon RDS<br>- Compare RDS with other storage services (EC2 DB, DynamoDB, Redshift) | 11/05/2026 | 11/05/2026 | [Amazon RDS Documentation](https://docs.aws.amazon.com/rds/) |
| 3 | - Network setup for RDS:<br>  + Create VPC<br>  + Create Security Groups for EC2 and RDS<br>  + Create DB Subnet Group | [12/05/2026](./Worklog_week1.4/) | [12/05/2026](./Worklog_week1.4/) | [VPC for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) |
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

---

## Week 5:
### Week 5 Objectives:
- Mastered life cycle of AWS S3: Lazy Loading, Transient Storage, Set Policies, Crossfeed Period.
- Understood Role of Application Load Balancer (ELB) in traffic and high availability.
- Distinguished Auto Scaling Group of EC2 instances.
- Understand the importance of cost management techniques and monitor resources spending.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Study EC2 Auto Scaling (Lazy Storage, Set Policies, Crossfeed Period)<br>- Understand Static Website Hosting on S3 and Route S3 as a backup for CloudFront<br>- Research on S3 Subject of cost management | 18/05/2026 | 18/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | - **Practice:**<br>  + Create an S3 bucket, configure static website hosting<br>  + Configure Static Website Hosting for EC2 Management UI (S3 UI)<br>  + Create an Auto Scaling Group | 19/05/2026 | 19/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - **Practice:**<br>  + Configure the Application Load Balancer<br>  + Configure the Auto Scaling Group<br>  + Configure the CloudFront with S3 | 20/05/2026 | 20/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | - **Practice:**<br>  + Test the Auto Scaling Group<br>  + Test the Application Load Balancer<br>  + Test the CloudFront and S3 integration<br>  + Test the EC2 Management application | [21/05/2026](./Worklog_week1.5/) | [21/05/2026](./Worklog_week1.5/) | https://cloudjourney.awsstudygroup.com/ |

### Week 5 Achievements:
#### Theory:
- Mastered life cycle of AWS S3: Lazy Loading, Transient Storage, Set Policies, Crossfeed Period.
- Understood Role of Application Load Balancer (ELB) in traffic and high availability.
- Distinguished Auto Scaling Group of EC2 instances.
- Understand the importance of cost management techniques and monitor resources spending.

#### Practice:
I can use AWS services effectively:
- Successfully built the EC2 Management application using Amazon EC2 Auto-Scaling with Elastic Load Balancing to ensure high availability and flexibility.
- All Services used:
  - Amazon VPC: Created an isolated virtual environment for deploying AWS resources.
  - Application Load Balancer: Distributes traffic between EC2 instances, improves application fault tolerance.
  - Auto Scaling Group: Automatically scales EC2 instances according to actual demand, cost optimization.
  - Amazon S3: Stores static website files, supports static website hosting.
  - Amazon CloudFront: Delivers static website content quickly through AWS's global network of edge locations.
  - IAM: Manages access permissions securely for AWS services.

Create VPC (CloudStack lab):
- In this CloudFormation lab, configure the following:
  - 1 VPC with CIDR: 10.10.0.0/16
  - 2 Public Subnets with CIDR: 10.10.1.0/24, 10.10.2.0/24
  - 2 Private Subnets with CIDR: 10.10.3.0/24, 10.10.4.0/24
  - 1 Internet Gateway
  - 2 NAT Gateway
  - 2 Public Route Table
  - 2 Private Route Table
  - Security Groups for Application Load Balancer, Public EC2, Private EC2
  - IAM Role for EC2
  - Launch Template
  - Auto Scaling Group
  - Application Load Balancer
  - Target Group
  - S3 Bucket
  - CloudFront Distribution

---

## Week 6:
### Week 6 Objectives:
- Understand AWS Cloud Trail and managed reports here in AWS Support.
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

---

## Week 7:
### Week 7 Objectives:
- Connect and get acquainted with members of First Cloud Journey.
- Understand basic AWS services, how to use the console & CLI.

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
- Learn and practice migrating servers from On-premise to AWS using VM Import/Export.
- Containerize applications using Docker and manage containers with Docker Compose on Amazon EC2.
- Configure application containers to connect with Amazon RDS and store container images in Amazon ECR and Docker Hub.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn VM Import/Export concepts<br> - Lab 14: Prepare VM and export from On-premise environment | 08/06/2026 | 08/06/2026 | [VM Import/Export Requirements](https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html) |
| 3 | - Lab 14: Upload VM file to Amazon S3<br> - Run CLI commands to import VM as AWS AMI and launch EC2 instance | 09/06/2026 | 09/06/2026 | [Importing a VM as an Image](https://docs.aws.amazon.com/vm-import/latest/userguide/what-is-vmimport.html) |
| 4 | - Lab 14: Configure S3 Bucket ACL<br> - Export EC2 instance back to S3 as VM file and clean up resources | 10/06/2026 | 10/06/2026 | [Exporting an Instance/Image](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html) |
| 5 | - Lab 15: Deploy and test the application on Local environment<br> - AWS Preparation: Configure VPC, Security Group, IAM Roles for ECR, and log in to Docker Hub | 11/06/2026 | 11/06/2026 | [Docker Documentation](https://docs.docker.com/)<br> [Amazon ECR IAM Policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/security_iam_id-based-policy-examples.html) |
| 6 | - Lab 15: Create DB Subnet Group and launch RDS Instance<br> - Launch and configure EC2 Instance as Docker host and install dependencies | 12/06/2026 | 12/06/2026 | [Amazon RDS DB Instance Creation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html)<br> [Docker on AWS EC2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) |
| 7 - Sun | - Lab 15: Build Docker image, run container and configure Docker Compose on EC2 to connect to RDS<br> - Push Docker Image to Amazon ECR and Docker Hub<br> - Clean up resources to prevent charges | 13/06/2026 | 14/06/2026 | [Docker Compose Reference](https://docs.docker.com/compose/)<br> [ECR Push Image Commands](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html) |

### Week 8 Achievements:

---

## Week 9:
### Week 9 Objectives:
- Understand and practice deploying applications on Amazon ECS (Elastic Container Service) using Fargate, ALB, and Cloud Map.
- Learn and configure automated CI/CD pipelines using GitLab CI/CD, GitHub Actions, and AWS CodeBuild.
- Configure container monitoring with Amazon CloudWatch Container Insights and logging using AWS FireLens.
- Utilize AWS Security Hub to evaluate the overall security posture (Security Score) against AWS security standards.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn concepts of Amazon ECS, Fargate, Task Definitions, and ECS Cluster operations | 15/06/2026 | 15/06/2026 | [Amazon ECS Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) |
| 3 | - **Lab 16 (Part 1)**: Configure VPC network, Subnets, Security Groups, and push Docker images to ECR/Docker Hub | 16/06/2026 | 16/06/2026 | [AWS ECR User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) |
| 4 | - **Lab 16 (Part 2)**: Create ECS Cluster, Task Definitions for Frontend/Backend, configure Target Groups, ALB, and launch ECS Services (Blue/Green for Backend & Rolling Update for Frontend) | 17/06/2026 | 17/06/2026 | [AWS ECS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html) |
| 5 | - **Lab 17 (Part 1)**: Integrate automated CI/CD using GitLab Runner (set up IAM roles, variables, run pipeline) and GitHub Actions | 18/06/2026 | 18/06/2026 | [GitLab CI/CD Docs](https://docs.gitlab.com/ci/)<br> [GitHub Actions Docs](https://docs.github.com/en/actions)<br> [AWS CodeBuild User Guide](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) |
| 6 | - **Lab 17 (Part 2)**: Set up AWS CodeBuild for Frontend/Backend, configure Container Insights (CloudWatch) and logging via AWS FireLens to S3 | 19/06/2026 | 19/06/2026 | [AWS Firelens Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) |
| 7 - Sun | - **Lab 18**: Enable AWS Security Hub, activate security standards, analyze the Security Score, and clean up resources | 20/06/2026 | 21/06/2026 | [AWS Security Hub User Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) |

### Week 9 Achievements:
- **Amazon ECS (Fargate)**: Successfully deployed a containerized architecture on ECS with independent Frontend and Backend services using Serverless compute.
- **Load Balancing & Routing**: Configured Application Load Balancers (ALB) to handle path-based routing, Blue/Green Deployment (via AWS CodeDeploy) for Backend, and Rolling Update for Frontend.
- **Multi-Platform CI/CD**: Designed automation workflows using self-hosted GitLab Runner on EC2, GitHub Actions workflow secrets, and AWS CodeBuild project configurations.
- **Monitoring & Log Routing**: Enabled CloudWatch Container Insights metrics and deployed AWS Firelens (Fluent Bit) logs router sidecar to store container stdout/stderr logs in Amazon S3.
- **Security Auditing**: Activated AWS Security Hub and obtained the security compliance score based on AWS Foundational Security Best Practices and CIS AWS Foundations Benchmark.

---

## Week 10:
### Week 10 Objectives:
- Understand and configure VPC Peering to connect two separate VPC networks, configure routing, and set up Network ACLs (NACLs) for subnet-level stateless security control.
- Learn and deploy AWS Transit Gateway (TGW) to connect multiple VPCs in a Hub-and-Spoke model, simplifying large-scale network architecture.
- Implement serverless operations automation using AWS Lambda and Amazon EventBridge to automatically start/stop EC2 instances based on schedules and route execution logs/alerts to Slack.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn concepts of VPC Peering and Network Access Control Lists (NACLs)<br>- **Lab 19 (Part 1)**: Set up baseline network environment using Cloudformation, create Security Groups and EC2s | 22/06/2026 | 22/06/2026 | VPC Peering Guide<br>VPC ACLs |
| 3 | - **Lab 19 (Part 2)**: Configure Custom VPC Peering, create VPC Peering connection, update route tables, and verify Cross-Peer DNS resolution | 23/06/2026 | 23/06/2026 | Network Peering DNS Support |
| 4 | - Learn concepts of AWS Transit Gateway (TGW)<br>- **Lab 20 (Part 1)**: Set up 3 VPCs for demonstration, create Transit Gateway and configure VPC attachments | 24/06/2026 | 24/06/2026 | AWS Transit Gateway |
| 5 | - **Lab 20 (Part 2)**: Setup Transit Gateway Route Tables, add Routes to TGW Route Tables, and verify cross-VPC network connectivity | 25/06/2026 | 25/06/2026 | TGW Route Tables |
| 6 | - Learn AWS Lambda Serverless compute and EventBridge scheduling services<br>- **Lab 22 (Part 1)**: Set up IAM workshop, tag EC2 instances, and configure IAM Role for Lambda | 26/06/2026 | 26/06/2026 | AWS Lambda Developer Guide<br>Slack Webhooks |
| 7 - Sun | - **Lab 22 (Part 2)**: Implement Lambda Python code (boto3) to start/stop EC2s and send alerts to Slack, schedule via EventBridge, and clean up resources | 27/06/2026 | 28/06/2026 | Boto3 EC2 Client<br>EventBridge Scheduler |

### Week 10 Achievements:
- **VPC Peering & Security**: Successfully established a private network link between two isolated VPCs; applied Network ACLs to control inbound/outbound packets and gained deep knowledge of stateless NACL behavior versus stateful Security Groups.
- **Transit Gateway Deployment**: Implemented a centralized Hub-and-Spoke network interconnecting 3 VPCs using AWS Transit Gateway, eliminating the need for a complex full-mesh peering topology.
- **Serverless Automation**: Built a serverless management solution using AWS Lambda (Python boto3) that reads instance resource tags, stopping development hosts at night and starting them before business hours.
- **ChatOps Integration**: Integrated AWS Lambda alerts with Slack channel notifications using Incoming Webhooks for real-time operation status reporting.
- **Scheduled Operations**: Configured Amazon EventBridge Scheduler (cron triggers) to automatically invoke Lambda functions at specific times.

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
- Practice deploying a CI/CD pipeline using AWS CodePipeline, CodeCommit, CodeBuild, and CodeDeploy.
- Understand and configure AWS Storage Gateway to connect with on-premises environments.
- Secure applications efficiently using AWS Web Application Firewall (WAF).
- Manage AWS resources using Tags and Resource Groups.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - **Practice**: Deploy applications to EC2 with AWS CodePipeline (Part 1)<br>+ Preparation (S3, Git, IAM roles)<br>+ Launch EC2 and install CodeDeploy Agent | 29/06/2026 | 29/06/2026 | <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html" target="_blank">AWS CodeDeploy Guide</a> |
| 3 | - **Practice**: Deploy applications to EC2 with AWS CodePipeline (Part 2)<br>+ Setup AWS CodeCommit, CodeBuild, CodeDeploy<br>+ Configure CodePipeline for CI/CD automation | 30/06/2026 | 30/06/2026 | <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html" target="_blank">AWS CodePipeline Guide</a> |
| 4 | - **Practice**: AWS Storage Gateway<br>+ Create S3 Bucket for Storage Gateway<br>+ Initialize Storage Gateway and File Shares<br>+ Mount File Shares on On-premises machine | 01/07/2026 | 01/07/2026 | <a href="https://docs.aws.amazon.com/storagegateway/" target="_blank">AWS Storage Gateway</a> |
| 5 | - **Practice**: AWS Web Application Firewall (Part 1)<br>+ Deploy the sample Web App<br>+ Use AWS WAF, configure ACLs and Managed rules | 02/07/2026 | 02/07/2026 | <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html" target="_blank">AWS WAF Developer Guide</a> |
| 6 | - **Practice**: AWS Web Application Firewall (Part 2)<br>+ Create Custom rules to block IP/Countries<br>+ Enable Logging and Testing | 03/07/2026 | 03/07/2026 | <a href="https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups.html" target="_blank">AWS WAF Managed Rules</a> |
| 7 - Sun | - **Practice**: Managing Resources Using Tags and Resource Groups<br>+ Use Tags on Console and CLI<br>+ Create and manage Resource Groups | [04/07/2026](./Worklog_week1.11/) | [05/07/2026](./Worklog_week1.11/) | <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html" target="_blank">Tagging AWS resources</a><br><a href="https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html" target="_blank">AWS Resource Groups</a> |

### Week 11 Achievements:
- **Mastered CI/CD Pipeline on AWS**: Integrated services like CodeCommit, CodeBuild, CodeDeploy, and CodePipeline to fully automate application deployments.
- **AWS Storage Gateway Configuration**: Successfully understood and configured AWS File Storage Gateway to connect on-premises storage to AWS S3.
- **Web Application Security with WAF**: Deployed AWS WAF to secure web applications against attacks using Web ACLs and custom rules.
- **Resource Management with Tags & Groups**: Learned how to effectively organize and manage AWS resources using Tags and Resource Groups.
- **All Labs Completed**: Successfully completed all 4 practical labs as guided.

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
- Understand and configure IAM Tag-based Access Control for EC2 resources.
- Learn about open-source monitoring tool Grafana and how to build basic dashboards.
- Set up IAM Permissions Boundaries to delegate permissions and limit the maximum access of IAM Entities.
- Utilize AWS Systems Manager (SSM) suite to manage server infrastructure remotely, including Fleet Manager, automated OS patching via Patch Manager, and executing remote scripts via Run Command.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn IAM Tag-based Access Control<br>- Read guides and configure IAM Tags for controlling access to EC2 resources | 06/07/2026 | 06/07/2026 | <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html" target="_blank">AWS IAM Tagging</a> |
| 3 | - Learn Grafana monitoring basics<br>- Read and understand Grafana concepts and set up a basic Dashboard | 07/07/2026 | 07/07/2026 | <a href="https://grafana.com/docs/grafana/latest/" target="_blank">Grafana User Guide</a> |
| 4 | - Learn IAM Permission Boundary<br>- Configure permission boundaries to limit the maximum permissions of IAM Entities | 08/07/2026 | 08/07/2026 | <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html" target="_blank">AWS Permissions Boundaries</a> |
| 5 | - Learn AWS Systems Manager (SSM) concepts<br>- Study introduction to SSM, Fleet Manager, Patch Manager, and Run Command | 09/07/2026 | 09/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html" target="_blank">AWS Systems Manager User Guide</a> |
| 6 | - Set up network infrastructure and IAM Roles for SSM<br>- Create VPC `windows-lab-ssm`, Internet Gateway, 2 Subnets<br>- Create IAM Role/Instance Profile with `AmazonSSMManagedInstanceCore` policy<br>- Launch 2 Windows Server EC2 instances attached with the IAM Role | 10/07/2026 | 10/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html" target="_blank">SSM Agent on Windows Server</a> |
| 7 - Sun | - Execute patching and remote commands via SSM<br>- Use Patch Manager to scan vulnerabilities and auto-install OS updates<br>- Use Run Command to run PowerShell `net user` remotely and store logs in S3<br>- Perform clean-up of all AWS resources to avoid any charges | [11/07/2026](./Worklog_week1.12/) | [12/07/2026](./Worklog_week1.12/) | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html" target="_blank">SSM Patch Manager</a><br><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html" target="_blank">SSM Run Command</a> |

### Week 12 Achievements:
