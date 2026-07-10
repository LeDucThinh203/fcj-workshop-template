---
title: "Week 9 Worklog"
date: 2026-06-15
weight: 9
chapter: false
pre: " <b> 1.9 </b> "
---

## Week 9 Objectives:
- Understand and practice deploying applications on Amazon ECS (Elastic Container Service) using Fargate, ALB, and Cloud Map.
- Learn and configure automated CI/CD pipelines using GitLab CI/CD, GitHub Actions, and AWS CodeBuild.
- Configure container monitoring with Amazon CloudWatch Container Insights and logging using AWS FireLens.
- Utilize AWS Security Hub to evaluate the overall security posture (Security Score) against AWS security standards.

## Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn concepts of Amazon ECS, Fargate, Task Definitions, and ECS Cluster operations | 15/06/2026 | 15/06/2026 | [Amazon ECS Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) |
| 3 | - **Lab 16 (Part 1)**: Configure VPC network, Subnets, Security Groups, and push Docker images to ECR/Docker Hub | 16/06/2026 | 16/06/2026 | [AWS ECR User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) |
| 4 | - **Lab 16 (Part 2)**: Create ECS Cluster, Task Definitions for Frontend/Backend, configure Target Groups, ALB, and launch ECS Services (Blue/Green for Backend & Rolling Update for Frontend) | 17/06/2026 | 17/06/2026 | [AWS ECS Blue/Green Deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html) |
| 5 | - **Lab 17 (Part 1)**: Integrate automated CI/CD using GitLab Runner (set up IAM roles, variables, run pipeline) and GitHub Actions | 18/06/2026 | 18/06/2026 | [GitLab CI/CD Docs](https://docs.gitlab.com/ci/)<br> [GitHub Actions Docs](https://docs.github.com/en/actions)<br> [AWS CodeBuild User Guide](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) |
| 6 | - **Lab 17 (Part 2)**: Set up AWS CodeBuild for Frontend/Backend, configure Container Insights (CloudWatch) and logging via AWS FireLens to S3 | 19/06/2026 | 19/06/2026 | [AWS Firelens Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) |
| 7 - Sun | - **Lab 18**: Enable AWS Security Hub, activate security standards, analyze the Security Score, and clean up resources | 20/06/2026 | 21/06/2026 | [AWS Security Hub User Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) |

## Week 9 Achievements:
- **Amazon ECS (Fargate)**: Successfully deployed a containerized architecture on ECS with independent Frontend and Backend services using Serverless compute.
- **Load Balancing & Routing**: Configured Application Load Balancers (ALB) to handle path-based routing, Blue/Green Deployment (via AWS CodeDeploy) for Backend, and Rolling Update for Frontend.
- **Multi-Platform CI/CD**: Designed automation workflows using self-hosted GitLab Runner on EC2, GitHub Actions workflow secrets, and AWS CodeBuild project configurations.
- **Monitoring & Log Routing**: Enabled CloudWatch Container Insights metrics and deployed AWS Firelens (Fluent Bit) logs router sidecar to store container stdout/stderr logs in Amazon S3.
- **Security Auditing**: Activated AWS Security Hub and obtained the security compliance score based on AWS Foundational Security Best Practices and CIS AWS Foundations Benchmark.
