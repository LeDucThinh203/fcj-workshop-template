---
title: "Week 9 Worklog"
date: 2026-06-15
weight: 9
chapter: false
pre: " <b> 1.9 </b> "
---

## Week 9 Objectives:
- Learn and implement serverless operations automation using AWS Lambda and Amazon EventBridge to automatically start/stop EC2 instances based on schedules.
- Understand resource tagging strategies, AWS Resource Groups, and resource filtering.
- Configure ChatOps integration to route Lambda execution logs and operational alerts to Slack using Incoming Webhooks.
- Activate and configure AWS Security Hub to evaluate account security posture (CSPM - Cloud Security Posture Management).

## Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn basic concepts of AWS Lambda serverless computing and EventBridge scheduling triggers (cron jobs)<br>- Understand resource tagging, bulk tag editing via Tag Editor, and creating AWS Resource Groups | 15/06/2026 | 15/06/2026 | [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/) |
| 3 | - **Practice (Part 1)**: Create a VPC, subnets, security groups, and launch EC2 instances to prepare the environment<br>- Create an IAM Role for Lambda with permissions to invoke EC2 actions and write logs to CloudWatch | 16/06/2026 | 16/06/2026 | [AWS Lambda IAM Permissions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) |
| 4 | - **Practice (Part 2)**: Implement Python Lambda code (boto3) to stop EC2 instances containing specific resource tags (e.g. `Environment=Dev`) | 17/06/2026 | 17/06/2026 | [Boto3 EC2 Client Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html) |
| 5 | - **Practice (Part 3)**: Implement Python Lambda code (boto3) to start EC2 instances<br>- Configure Incoming Webhooks on Slack to generate a webhook URL endpoint | 18/06/2026 | 18/06/2026 | [Slack Incoming Webhooks Guide](https://api.slack.com/messaging/webhooks) |
| 6 | - **Practice (Part 4)**: Integrate the Slack webhook payload notification within the Lambda functions and verify manually | 19/06/2026 | 19/06/2026 | [Sending Slack Messages with Lambda](https://api.slack.com/messaging/webhooks) |
| 7 - Sun | - **Practice (Part 5)**: Enable AWS Security Hub and standard security posture management (CSPM) compliance benchmarks, check score, and clean up resources | 20/06/2026 | 21/06/2026 | [AWS Security Hub User Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) |

## Week 9 Achievements:
- **Serverless Automation**: Successfully built a serverless scheduling solution using AWS Lambda (Python boto3) combined with EventBridge Scheduler rules to stop EC2 hosts at night and start them in the morning for cost optimization.
- **ChatOps Integration**: Integrated AWS Lambda alerts with Slack channel notifications using Slack Incoming Webhooks to report VM operations in real-time.
- **Resource Management**: Mastered bulk resource tagging using Tag Editor and logical grouping via AWS Resource Groups.
- **Security & Optimization**: Activated AWS Security Hub to evaluate compliance posture (CSPM) and performed thorough cleanup of all lab resources to optimize costs.

### Evidences:

1. **Create VPC (CreateVPC)**
   ![CreateVPC](../../images/1-Worklog/Worklog_week1.9/CreateVPC.png)
   *Description: This image illustrates the AWS Management Console during the creation of a new Virtual Private Cloud (VPC). The process involves defining the IPv4 CIDR block, setting up Subnets across different Availability Zones for high availability, and configuring an Internet Gateway (IGW) along with Route Tables to route internet traffic to Public Subnets securely.*

2. **Create Security Group (Create Security Group)**
   ![Create Security Group](../../images/1-Worklog/Worklog_week1.9/Create%20Security%20Group.png)
   *Description: This step involves setting up a virtual firewall at the instance level. The image displays the configuration of Inbound rules to open necessary network ports, such as port 22 for SSH remote management or port 80/443 for web traffic. This ensures that only specified IP addresses or network ranges can access the resources.*

3. **Launch EC2 Instance (Create Ec2)**
   ![Create Ec2](../../images/1-Worklog/Worklog_week1.9/Create%20Ec2.png)
   *Description: The image captures a successful EC2 instance launch screen. The virtual machine has been provisioned with specific configurations (AMI, Instance Type, Key Pair). It resides in the previously created VPC and Subnet and is attached to the proper Security Group. This core compute resource will be used to test the automated Start/Stop Lambda functions.*

4. **Create IAM Role for Lambda (Create Role for lamda)**
   ![Create Role for lamda](../../images/1-Worklog/Worklog_week1.9/Create%20Role%20for%20lamda.png)
   *Description: Displays the IAM (Identity and Access Management) console where a new Role is created specifically for the AWS Lambda service. This Role is attached with Policies that grant the Lambda function permissions to invoke EC2 API actions (like `ec2:StartInstances`, `ec2:StopInstances`) and write execution logs to CloudWatch Logs for debugging purposes.*

5. **Create Lambda Function to Stop Instance (Function stop instance)**
   ![Function stop instance](../../images/1-Worklog/Worklog_week1.9/Function%20stop%20instance.png)
   *Description: Detailed view of the AWS Lambda service showing a function designed to automatically stop EC2 instances. The function's code (typically written in Python using Boto3) scans for EC2 instances with specific Tags (e.g., `Environment=Dev`) and executes the stop command. This significantly saves compute costs during non-working hours or at night.*

6. **Create Lambda Function to Start Instance (Function start instance)**
   ![Function start instance](../../images/1-Worklog/Worklog_week1.9/Function%20start%20instance.png)
   *Description: Similar to the Stop function, this image illustrates the configuration of the Lambda function used to automatically start virtual machines. Triggered by an Amazon EventBridge cron schedule, this function runs at the beginning of the workday (e.g., 8:00 AM) to ensure systems are ready for use when employees start working.*

7. **Create EC2 Instance with Tags (Create EC2 Instance with tag)**
   ![Create EC2 Instance with tag](../../images/1-Worklog/Worklog_week1.9/Create%20EC2%20Instance%20with%20tag.png)
   *Description: Evidence of advanced configuration when launching a new EC2 instance. In the Tags section, Key-Value pairs (e.g., `Project = FirstCloudJourney`, `Environment = Test`) are defined. Tagging at launch helps automated systems (like our Lambda functions) correctly identify target instances without affecting Production servers.*

8. **Add Tag to Existing EC2 (EC2 add tag)**
   ![EC2 add tag](../../images/1-Worklog/Worklog_week1.9/EC2%20add%20tag.png)
   *Description: A screenshot of the Tags tab within a running EC2 instance's details. Through the console, additional metadata Tags are appended or modified for pre-existing servers. This is crucial for unified management, Cost Allocation tracking, and implementing Attribute-Based Access Control (ABAC) policies.*

9. **Manage Tags and Filter Resources (Managing Tags and Filter resources by tag)**
   ![Managing Tags and Filter resources by tag](../../images/1-Worklog/Worklog_week1.9/Managing%20Tags%20and%20Filter%20resources%20by%20tag.png)
   *Description: Using the AWS Tag Editor or Resource Groups console to search across resources in bulk. Instead of checking individual services, the image shows how to filter all resources (EC2, VPC, Lambda, etc.) that share a specific Tag value. This feature provides administrators with a holistic view of the system architecture.*

10. **Create a Resource Group (Create a Resource Group)**
    ![Create a Resource Group](../../images/1-Worklog/Worklog_week1.9/Create%20a%20Resource%20Group.png)
    *Description: The console view for creating a new AWS Resource Group. By utilizing Tag-based queries, the system groups scattered resources into a single logical collection. From this Resource Group, users can safely and quickly perform bulk administrative actions via AWS Systems Manager.*

11. **Configure Slack Incoming Web-hooks (Incoming Web-hooks slack)**
    ![Incoming Web-hooks slack](../../images/1-Worklog/Worklog_week1.9/Incoming%20Web-hooks%20slack.png)
    *Description: The configuration interface of the Slack application to generate an Incoming Webhook URL. This webhook acts as an endpoint to receive data payloads. In this lab, whenever the Lambda functions execute the Start/Stop actions, they send a payload containing the result notification (success/failure) through this webhook directly to the operations team's chat channel (ChatOps).*

12. **Check Result (Check Result)**
    ![Check Result](../../images/1-Worklog/Worklog_week1.9/Check%20Result.png)
    *Description: Concrete proof that the automation system operates flawlessly. The image captures the Slack application screen showing automated alert messages sent from AWS in real-time. Administrators can instantly know the status of virtual machines (stopped or started) without logging into the AWS Console, embodying the ChatOps philosophy.*

13. **Enable AWS Security Hub CSPM (Enable AWS Security Hub CSPM)**
    ![Enable AWS Security Hub CSPM](../../images/1-Worklog/Worklog_week1.9/Enable%20AWS%20Security%20Hub%20CSPM.png)
    *Description: The central dashboard of AWS Security Hub. The Cloud Security Posture Management (CSPM) feature has been activated to scan the entire account based on industry-standard security frameworks (like AWS Foundational Security Best Practices). The interface displays the compliance score chart and lists misconfigurations or vulnerabilities that need remediation.*

14. **Clean Up Security Hub (Clean Security Hub)**
    ![Clean Security Hub](../../images/1-Worklog/Worklog_week1.9/Clean%20Security%20Hub.png)
    *Description: Evidence of disabling and deleting data from AWS Security Hub within its Settings. Since Security Hub incurs charges based on the number of security checks performed, turning off this service after completing the lab is essential to prevent unexpected ongoing monthly fees.*

15. **Clean Up Tags (Clean Tags)**
    ![Clean Tags](../../images/1-Worklog/Worklog_week1.9/Clean%20Tags.png)
    *Description: Illustrates the use of Tag Editor to mass-delete the Tags created across multiple resources. This cleanup step keeps the AWS environment organized, preventing stale tags from cluttering cost reporting tools or disrupting other automated rule sets in the system.*

16. **Clean Up EC2, Lambda, and CloudWatch (Clean Ec2 and lamda and cloudwatch)**
    ![Clean Ec2 and lamda and cloudwatch](../../images/1-Worklog/Worklog_week1.9/Clean%20Ec2%20and%20lamda%20and%20cloudwatch.png)
    *Description: The final environment cleanup step (Terminate/Delete resources). The image shows the deletion of EC2 virtual machines, unused Lambda functions, and importantly, the removal of CloudWatch Log Groups. If left indefinitely, Log Groups can accumulate storage costs, so deleting them thoroughly ensures maximum Cost Optimization.*
