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
