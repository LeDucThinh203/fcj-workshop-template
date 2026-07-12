
---
title: "Week 11 Worklog"
date: 2026-06-29
weight: 11
chapter: false
pre: " <b> 1.11 </b> "
---

## Week 11 Objectives:
- Practice deploying a CI/CD pipeline using AWS CodePipeline, CodeCommit, CodeBuild, and CodeDeploy.
- Understand and configure AWS Storage Gateway to connect with on-premises environments.
- Secure applications efficiently using AWS Web Application Firewall (WAF).
- Manage AWS resources using Tags and Resource Groups.

## Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - **Practice**: Deploy applications to EC2 with AWS CodePipeline (Part 1)<br>+ Preparation (S3, Git, IAM roles)<br>+ Launch EC2 and install CodeDeploy Agent | 29/06/2026 | 29/06/2026 | <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html" target="_blank">AWS CodeDeploy Guide</a> |
| 3 | - **Practice**: Deploy applications to EC2 with AWS CodePipeline (Part 2)<br>+ Setup AWS CodeCommit, CodeBuild, CodeDeploy<br>+ Configure CodePipeline for CI/CD automation | 30/06/2026 | 30/06/2026 | <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html" target="_blank">AWS CodePipeline Guide</a> |
| 4 | - **Practice**: AWS Storage Gateway<br>+ Create S3 Bucket for Storage Gateway<br>+ Initialize Storage Gateway and File Shares<br>+ Mount File Shares on On-premises machine | 01/07/2026 | 01/07/2026 | <a href="https://docs.aws.amazon.com/storagegateway/" target="_blank">AWS Storage Gateway</a> |
| 5 | - **Practice**: AWS Web Application Firewall (Part 1)<br>+ Deploy the sample Web App<br>+ Use AWS WAF, configure ACLs and Managed rules | 02/07/2026 | 02/07/2026 | <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html" target="_blank">AWS WAF Developer Guide</a> |
| 6 | - **Practice**: AWS Web Application Firewall (Part 2)<br>+ Create Custom rules to block IP/Countries<br>+ Enable Logging and Testing | 03/07/2026 | 03/07/2026 | <a href="https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups.html" target="_blank">AWS WAF Managed Rules</a> |
| 7 - Sun | - **Practice**: Managing Resources Using Tags and Resource Groups<br>+ Use Tags on Console and CLI<br>+ Create and manage Resource Groups | 04/07/2026 | 05/07/2026 | <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html" target="_blank">Tagging AWS resources</a><br><a href="https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html" target="_blank">AWS Resource Groups</a> |

## Week 11 Achievements:
- **Mastered CI/CD Pipeline on AWS**: Integrated services like CodeCommit, CodeBuild, CodeDeploy, and CodePipeline to fully automate application deployments.
- **AWS Storage Gateway Configuration**: Successfully understood and configured AWS File Storage Gateway to connect on-premises storage to AWS S3.
- **Web Application Security with WAF**: Deployed AWS WAF to secure web applications against attacks using Web ACLs and custom rules.
- **Resource Management with Tags & Groups**: Learned how to effectively organize and manage AWS resources using Tags and Resource Groups.
- **All Labs Completed**: Successfully completed all 4 practical labs as guided.

### Evidences:

1. **Create S3 Bucket (Create s3 bucket)**
   ![Create s3 bucket](../../images/1-Worklog/Worklog_week1.11/Create%20s3%20bucket.png)
   *Description: The process of creating an Amazon S3 Bucket to serve as the data storage backend for the Storage Gateway. S3 provides secure, durable, and highly scalable object storage, acting as the final destination for files shared via the File Gateway.*

2. **Launch EC2 Instance (Create EC2)**
   ![Create EC2](../../images/1-Worklog/Worklog_week1.11/Create%20EC2.png)
   *Description: Deploying a new virtual machine (EC2 instance) to act as a simulated on-premises server. This instance will be configured to mount the File Share provided by the Storage Gateway to test file storage capabilities to S3 from a local network environment.*

3. **Initialize Storage Gateway (Create Storage GateWay)**
   ![Create Storage GateWay](../../images/1-Worklog/Worklog_week1.11/Create%20Storage%20GateWay.png)
   *Description: The configuration and initialization interface of the AWS File Storage Gateway. The Storage Gateway acts as a bridge between on-premises applications and the AWS cloud storage ecosystem. It provides standard SMB/NFS protocols so legacy applications can seamlessly save files to S3 without code refactoring.*

4. **Set Up File Share (Create File Share)**
   ![Create File Share](../../images/1-Worklog/Worklog_week1.11/Create%20File%20Share.png)
   *Description: The process of setting up a File Share on the newly created Storage Gateway. This file share is directly linked to the S3 bucket. Any file written to this file share via NFS/SMB is automatically uploaded to S3 as an object by the Gateway.*

5. **Mount File Share to On-premises Machine (Mount File shares on On-premises machine)**
   ![Mount File shares on On-premises machine](../../images/1-Worklog/Worklog_week1.11/Mount%20File%20shares%20on%20On-premises%20machine.png)
   *Description: Executing the command to mount the shared directory from the Storage Gateway onto the EC2 instance (simulated on-premises server). The image demonstrates a successful connection, allowing users or applications to transparently read/write data to S3 through a local network directory.*

6. **Clean Up Resources (Clean)**
   ![Clean](../../images/1-Worklog/Worklog_week1.11/Clean.png)
   *Description: The operation of deleting the created resources (Storage Gateway, File Share, S3 Bucket, EC2 Instance) after completing the hands-on lab. This is a crucial principle for Cost Optimization, ensuring no redundant resources are left running unintentionally.*
