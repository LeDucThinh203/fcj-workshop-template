---
title : "Project: Smart Parking IoT"
date: 2026-05-13
weight : 3
chapter : false
pre : " <b> 3. </b> "
---

# Smart Parking IoT Web Platform on AWS Serverless

The **Smart Parking IoT System** is an end-to-end solution designed for automated parking lot monitoring, Automatic Number Plate Recognition (ANPR), and AWS Lambda-powered AI Virtual Assistant integration. The entire system has been successfully researched and deployed by the team on **AWS Serverless** production environment.

{{% notice tip "Live Access & Online Demo" %}}
🌐 **Website CloudFront (Live Deploy):** [https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)  
🔑 **Admin Account:** `leducthinh203` | **Password:** `Admin123@`  
👤 **User Account:** Free registration directly on the Web App platform.  
🎬 **Frontend Demo (FE):** Watch video clips and view screenshots of the live Web Dashboard at [Google Drive Demo FE Folder](https://drive.google.com/drive/folders/1RLwMvlmJNH05ot-FZzCE_2U7c10_8zqz?usp=sharing).
{{% /notice %}}

## Overview of the Deployed System

This chapter details the overall architecture, cloud infrastructure, real-time IoT data processing pipelines, Web App control interface, as well as the security and operations management mechanisms deployed by the team.

### Core Modules:

* **3.1. [AWS Core Infrastructure](3.1-aws-core-infrastructure/):** Core serverless infrastructure including S3, DynamoDB, Lambda, API Gateway, AWS IoT Core, CloudFront, and WAF managed via AWS CDK (Infrastructure as Code).
* **3.2. [ESP32 Edge Devices](3.2-esp32-edge-devices/):** Hardware edge devices (ESP32 Camera for gate entry/exit and ESP32 sensors for slot status) connected directly to AWS.
* **3.3. [IoT Data Pipeline](3.3-iot-data-pipeline/):** Real-time data streaming and processing pipelines connecting edge devices, AWS Lambda, Amazon Rekognition (ANPR), and DynamoDB storage.
* **3.4. [User Interface and Security](3.4-user-interface-and-security/):** Modern Web Dashboard (Admin & User Portals), integrated AWS Lambda AI Assistant, and multi-layered security with Amazon Cognito, CloudFront HTTPS, and AWS WAF.
* **3.5. [Monitoring and Management](3.5-monitoring-and-management/):** Operations monitoring, log analytics, alarm rules via Amazon CloudWatch, CloudTrail audit logs, and AWS Budgets cost control.
* **3.6. [System Testing and Optimization](3.6-system-testing-and-optimization/):** Empirical test results on latency (<2s), plate recognition accuracy (>95%), and cost/performance optimizations achieved.