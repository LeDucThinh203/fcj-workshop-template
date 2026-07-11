---
title: "Week 10 Worklog"
date: 2026-06-22
weight: 10
chapter: false
pre: " <b> 1.10 </b> "
---

## Week 10 Objectives:
- Understand and configure VPC Peering to connect two separate VPC networks, configure routing, and set up Network ACLs (NACLs) for subnet-level stateless security control.
- Learn and deploy AWS Transit Gateway (TGW) to connect multiple VPCs in a Hub-and-Spoke model, simplifying large-scale network architecture.
- Implement serverless operations automation using AWS Lambda and Amazon EventBridge to automatically start/stop EC2 instances based on schedules and route execution logs/alerts to Slack.

## Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn concepts of VPC Peering and Network Access Control Lists (NACLs)<br>- **Lab 19 (Part 1)**: Set up baseline network environment using Cloudformation, create Security Groups and EC2s | 22/06/2026 | 22/06/2026 | <a href="https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html" target="_blank">VPC Peering Guide</a><br><a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html" target="_blank">Network ACLs</a> |
| 3 | - **Lab 19 (Part 2)**: Configure Custom VPC Peering, create VPC Peering connection, update route tables, and verify Cross-Peer DNS resolution | 23/06/2026 | 23/06/2026 | <a href="https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html" target="_blank">VPC Peering DNS Support</a> |
| 4 | - Learn concepts of AWS Transit Gateway (TGW)<br>- **Lab 20 (Part 1)**: Set up 3 VPCs for demonstration, create Transit Gateway and configure VPC attachments | 24/06/2026 | 24/06/2026 | <a href="https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html" target="_blank">AWS Transit Gateway Guide</a> |
| 5 | - **Lab 20 (Part 2)**: Setup Transit Gateway Route Tables, add Routes to TGW Route Tables, and verify cross-VPC network connectivity | 25/06/2026 | 25/06/2026 | <a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html" target="_blank">TGW Route Tables</a> |
| 6 | - Learn AWS Lambda Serverless compute and EventBridge scheduling services<br>- **Lab 22 (Part 1)**: Set up IAM workshop, tag EC2 instances, and configure IAM Role for Lambda | 26/06/2026 | 26/06/2026 | <a href="https://docs.aws.amazon.com/lambda/latest/dg/welcome.html" target="_blank">AWS Lambda Developer Guide</a><br><a href="https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/" target="_blank">Slack Webhooks</a> |
| 7 - Sun | - **Lab 22 (Part 2)**: Implement Lambda Python code (boto3) to start/stop EC2s and send alerts to Slack, schedule via EventBridge, and clean up resources | 27/06/2026 | 28/06/2026 | <a href="https://docs.aws.amazon.com/boto3/latest/reference/services/ec2.html" target="_blank">Boto3 EC2 Client</a><br><a href="https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html" target="_blank">EventBridge Scheduler</a> |

## Week 10 Achievements:
- **VPC Peering & Security**: Successfully established a private network link between two isolated VPCs; applied Network ACLs to control inbound/outbound packets and gained deep knowledge of stateless NACL behavior versus stateful Security Groups.
- **Transit Gateway Deployment**: Implemented a centralized Hub-and-Spoke network interconnecting 3 VPCs using AWS Transit Gateway, eliminating the need for a complex full-mesh peering topology.
- **Serverless Automation**: Built a serverless management solution using AWS Lambda (Python boto3) that reads instance resource tags, stopping development hosts at night and starting them before business hours.
- **ChatOps Integration**: Integrated AWS Lambda alerts with Slack channel notifications using Incoming Webhooks for real-time operation status reporting.
- **Scheduled Operations**: Configured Amazon EventBridge Scheduler (cron triggers) to automatically invoke Lambda functions at specific times.

### Evidences:

1. **VPC Peering CloudFormation Stack Creation (Create_Stack)**
   ![VPC Peering Stack](/images/1-Worklog/Worklog_week1.10/Create_Stack.png)
   *Description: This image captures the successful initiation and creation of the AWS CloudFormation stack used to rapidly provision the baseline network environment for the VPC Peering lab. Utilizing Infrastructure as Code (IaC) ensures that all necessary VPCs, subnets, route tables, and instances are deployed consistently and accurately. The stack creates the foundational 'My VPC' and 'HG VPC' which will subsequently be peered, allowing for a structured and repeatable learning experience without manual setup overhead.*

2. **Security Group Configuration for My VPC (Create_MY VPC SG)**
   ![My VPC Security Group](/images/1-Worklog/Worklog_week1.10/Create_MY%20VPC%20SG.png)
   *Description: Depicts the specific Security Group rules configured for 'My VPC'. Security groups act as stateful virtual firewalls at the instance level. In this configuration, inbound rules are carefully defined to permit SSH (port 22) and ICMP (ping) traffic originating only from trusted IP addresses or specifically from the peered VPC CIDR block. This demonstrates the principle of least privilege, ensuring that even when VPCs are connected, instances remain protected against unauthorized access attempts from the broader network.*

3. **Security Group Configuration for HG VPC (Create_HG VPC SG)**
   ![HG VPC Security Group](/images/1-Worklog/Worklog_week1.10/Create_HG%20VPC%20SG.png)
   *Description: Shows the corresponding Security Group configuration for instances located within the 'HG VPC' (the peered network). Similar to the previous setup, this firewall rule is tailored to accept incoming traffic strictly from the 'My VPC' CIDR range. By configuring these rules symmetrically across both VPCs, we establish a secure bidirectional communication channel, which is essential for verifying connectivity testing (like pinging instances) after the peering connection is actively established.*

4. **EC2 Instances Provisioning (Create EC2)**
   ![Create EC2 Instances](/images/1-Worklog/Worklog_week1.10/Create%20EC2.png)
   *Description: Illustrates the successful launch and running state of the EC2 instances deployed across the different VPCs (e.g., one instance in 'My VPC' and another in 'HG VPC'). These virtual servers act as the primary endpoints for our network connectivity tests. Verifying that these instances are running and possess the correct private IP addresses within their respective subnets is a critical prerequisite before attempting to validate the VPC peering routes and security group rules.*

5. **Establishing VPC Peering Connection (MyVPC peering to HG VPC)**
   ![VPC Peering Connection](/images/1-Worklog/Worklog_week1.10/MyVPC%20peering%20to%20HG%20VPC.png)
   *Description: Highlights the core objective of the lab—the active and functioning VPC Peering connection linking 'My VPC' to 'HG VPC'. A peering connection is a networking connection between two VPCs that enables the routing of traffic between them using private IPv4 or IPV6 addresses. This image confirms that the connection request was accepted, changing the status to 'Active', thereby virtually merging the two separate network segments into a continuous private network space without traversing the public internet.*

6. **Route Table Updates for Peering (route_table)**
   ![Route Table Configuration](/images/1-Worklog/Worklog_week1.10/route_table.png)
   *Description: Displays the crucial modifications made to the VPC route tables. For instances in one VPC to communicate with instances in the peered VPC, the route tables associated with their subnets must be updated. This screenshot shows the addition of a specific route where the destination is the CIDR block of the peered VPC, and the target is the newly created VPC Peering Connection ID (pcx-...). Without this exact routing configuration, the peering connection remains unutilized, and packets would simply be dropped.*

7. **Network Access Control List (NACL) Verification (ALI)**
   ![Network ACL Configuration](/images/1-Worklog/Worklog_week1.10/ALI.png)
   *Description: Presents the configuration and testing of Network ACLs (NACLs). Unlike Security Groups, NACLs act as stateless firewalls at the subnet level, meaning both inbound and outbound rules must be explicitly defined. This part of the lab emphasizes the difference between stateful and stateless filtering. The image demonstrates how modifying a NACL to block or allow specific traffic (like ICMP or SSH) immediately impacts the entire subnet, providing an additional, broader layer of network security defense beyond individual instance firewalls.*
