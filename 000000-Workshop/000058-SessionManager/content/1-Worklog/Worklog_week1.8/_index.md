---
title: "Week 8 Worklog"
date: 2026-05-13
weight: 8
chapter: false
pre: " <b> 1.8 </b> "
---

## Week 8 Objectives:
- Learn advanced identity and access management using IAM Groups, Users, Policies, and Roles.
- Understand data encryption on Amazon S3 using AWS Key Management Service (KMS), and configure secure cross-account encrypted data sharing.
- Configure system activity tracking and auditing using AWS CloudTrail.
- Use Amazon Athena to query and analyze CloudTrail logs stored in Amazon S3 using standard SQL.

## Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn advanced concepts of IAM Groups, Users, Policies, and Roles under the principle of least privilege<br>- **Practice (Part 1)**: Create IAM Groups and Users to control access boundaries | 08/06/2026 | 08/06/2026 | [IAM Policies Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) |
| 3 | - Study AWS KMS encryption principles (SSE-KMS, Customer Managed Keys, Key Policies)<br>- **Practice (Part 2)**: Create a Customer Managed Key in AWS Key Management Service (KMS) and set up its Key Policy | 09/06/2026 | 09/06/2026 | [AWS KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) |
| 4 | - **Practice (Part 3)**: Author IAM Policies and Roles to delegate usage permissions for the KMS Key<br>- Create a new S3 bucket and upload test files, setting up server-side encryption via KMS (SSE-KMS) | 10/06/2026 | 10/06/2026 | [Amazon S3 KMS Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) |
| 5 | - **Practice (Part 4)**: Verify encryption and share the encrypted S3 objects with an external AWS account | 11/06/2026 | 11/06/2026 | [S3 Cross-Account Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html) |
| 6 | - Study system auditing with AWS CloudTrail<br>- **Practice (Part 5)**: Deploy an AWS CloudTrail trail to deliver API activity logs to a secure S3 bucket | 12/06/2026 | 12/06/2026 | [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) |
| 7 - Sun | - **Practice (Part 6)**: Configure Amazon Athena, define query result locations on S3, and run SQL queries against CloudTrail log tables<br>- Clean up all provisioned resources for Cost Optimization | 13/06/2026 | 14/06/2026 | [Querying CloudTrail Logs with Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-cloudtrail-logs.html) |

## Week 8 Achievements:
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
