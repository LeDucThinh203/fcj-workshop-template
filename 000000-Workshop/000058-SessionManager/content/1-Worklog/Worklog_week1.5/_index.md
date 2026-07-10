---
title: "Week 5 Worklog"
date: 2026-05-13
weight: 5
chapter: false
pre: " <b> 1.5 </b> "
---

## Week 5 Objectives:
- Mastered life cycle of AWS S3: Lazy Loading, Transient Storage, Set Policies, Crossfeed Period.
- Understood Role of Application Load Balancer (ELB) in traffic and high availability.
- Distinguished Auto Scaling Group of EC2 instances.
- Understand the importance of cost management techniques and monitor resources spending.

## Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Study EC2 Auto Scaling (Lazy Storage, Set Policies, Crossfeed Period)<br>- Understand Static Website Hosting on S3 and Route S3 as a backup for CloudFront<br>- Research on S3 Subject of cost management | 18/05/2026 | 18/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | - **Practice:**<br>  + Create an S3 bucket, configure static website hosting<br>  + Configure Static Website Hosting for EC2 Management UI (S3 UI)<br>  + Create an Auto Scaling Group | 19/05/2026 | 19/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - **Practice:**<br>  + Configure the Application Load Balancer<br>  + Configure the Auto Scaling Group<br>  + Configure the CloudFront with S3 | 20/05/2026 | 20/05/2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | - **Practice:**<br>  + Test the Auto Scaling Group<br>  + Test the Application Load Balancer<br>  + Test the CloudFront and S3 integration<br>  + Test the EC2 Management application | 21/05/2026 | 21/05/2026 | https://cloudjourney.awsstudygroup.com/ |

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
