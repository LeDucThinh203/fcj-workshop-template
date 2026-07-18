
---
title: "Week 11 Worklog"
date: 2026-06-29
weight: 11
chapter: false
pre: " <b> 1.11 </b> "
---

## Week 11 Objectives:
- Understand the core concepts of AWS Storage Gateway and hybrid cloud storage models.
- Practice deploying and configuring AWS File Storage Gateway to connect on-premises storage infrastructure with Amazon S3 cloud storage.
- Mount NFS/SMB File Shares from the Storage Gateway onto a Linux client (simulating an on-premises host).

## Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Study the theoretical concepts of AWS Storage Gateway, its types, and hybrid cloud storage architectures | 29/06/2026 | 29/06/2026 | <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/WhatIsStorageGateway.html" target="_blank">AWS Storage Gateway Guide</a> |
| 3 | - **Practice (Part 1)**: Create an Amazon S3 Bucket to act as the backend storage for the Storage Gateway | 30/06/2026 | 30/06/2026 | <a href="https://docs.aws.amazon.com/s3/" target="_blank">Amazon S3 Documentation</a> |
| 4 | - **Practice (Part 2)**: Launch a Linux EC2 instance to simulate an on-premises client host | 01/07/2026 | 01/07/2026 | <a href="https://docs.aws.amazon.com/ec2/" target="_blank">Amazon EC2 User Guide</a> |
| 5 | - **Practice (Part 3)**: Deploy and configure the AWS File Storage Gateway via the AWS Console | 02/07/2026 | 02/07/2026 | <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/CreatingAnAppliance.html" target="_blank">Creating a File Gateway</a> |
| 6 | - **Practice (Part 4)**: Create a File Share on the Storage Gateway and associate it directly with the S3 bucket | 03/07/2026 | 03/07/2026 | <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/CreatingAFileShare.html" target="_blank">Creating a File Share</a> |
| 7 - Sun | - **Practice (Part 5)**: Mount the NFS File Share onto the simulated Linux host (EC2 instance), verify data synchronization from the host to the S3 bucket<br>- Perform resource cleanup to prevent ongoing AWS charges | 04/07/2026 | 05/07/2026 | <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/mounting-file-share.html" target="_blank">Mounting a File Share</a> |

## Week 11 Achievements:
- **AWS Storage Gateway Configuration**: Mastered hybrid cloud storage mechanisms and successfully configured AWS File Storage Gateway to link simulated on-premises file storage with AWS S3 using standard file sharing protocols.
- **Hybrid Infrastructure Integration**: Successfully mounted NFS File Shares and verified seamless automated file synchronization between local and cloud environments.
- **Cost Optimization**: Cleaned up all provisioned Storage Gateway resources, virtual hosts, and storage buckets to prevent ongoing monthly charges.

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
