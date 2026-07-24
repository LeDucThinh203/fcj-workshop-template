---
title : "Monitoring and Management"
date: 2026-05-13
weight : 5
chapter : false
pre : " <b> 3.5. </b> "
---

This section outlines the operational monitoring, performance auditing, and cost governance strategy deployed for the **Smart Parking IoT Web Platform** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)) running on AWS Serverless infrastructure.

The monitoring suite leverages native AWS observability tools (Lambda, API Gateway, IoT Core, S3, DynamoDB, Rekognition, Lambda AI Service) to maintain continuous high availability (99.9% Uptime SLA), low API latency for the Web App, and predictable cloud spending:
* **Amazon CloudWatch:** Centralized management of CloudWatch Dashboards, API Gateway/Lambda Log Groups, and automated CloudWatch Alarms for error thresholds.
* **AWS Budgets & Cost Explorer:** Real-time tracking of daily AWS service expenditures with automated Email notifications when costs breach 80% of defined budget thresholds.
* **AWS CloudTrail:** Complete security audit logging of API calls and configuration changes across all AWS infrastructure resources.
* **IAM Security Governance:** Periodic audit and enforcement of Least Privilege policies for Lambda execution roles and API Gateway authorizers.

### 3.5.1. Operational Monitoring Objectives
The operations framework guarantees seamless 24/7 Web App execution and enables rapid root-cause diagnosis for site engineers.

**Primary Monitoring Objectives:**
* **Lambda Backend Latency & Error SLA:** Maintain execution duration under 500ms and keep function error rate below 0.1%.
* **API Gateway Traffic Ingestion:** Monitor HTTPS query volume from the Web App, tracking 4xx/5xx HTTP response codes.
* **IoT Core Connection Tracking:** Monitor ESP32 sensor MQTT message delivery rates and device online status.
* **ANPR Pipeline Auditing:** Detect failures during image feature extraction or Rekognition plate parsing.
* **Cloud Budget Governance:** Ensure monthly AWS infrastructure costs remain within projected budget caps.

### 3.5.2. Centralized Operations via Amazon CloudWatch Dashboards
The engineering team created an **AWS CloudWatch Operational Dashboard** consolidating key real-time metrics:

**Core Dashboard Widgets:**
1. **API Gateway Invocations & Latency:** Real-time chart tracking Web App request volume per minute and endpoint latency.
2. **Lambda Duration & Error Rates:** Execution duration histograms and exception counters for backend Lambda microservices (including Lambda Backend, Image Processing, and Lambda AI Service).
3. **DynamoDB Capacity Consumption:** Consumed Read/Write Capacity Units for `ParkingSlots` and `VehicleLogs` tables.
4. **AWS IoT Core Telemetry Message Rate:** Ingested MQTT payload volume received from ESP32 bay sensors.

### 3.5.3. CloudWatch Log Groups & Log Insights
Operational logs from API Gateway, Lambda Functions, and IoT Core Rules stream automatically into **CloudWatch Logs Groups**:

* **Retention Policy:** Log groups configure a 30-day retention policy to optimize cloud log storage costs.
* **CloudWatch Logs Insights Queries:** Proactive log searching for system exceptions using CloudWatch query syntax:
  ```sql
  fields @timestamp, @message
  | filter @message like /ERROR/ or @message like /Exception/
  | sort @timestamp desc
  | limit 20
  ```

### 3.5.4. Automated Alerting via CloudWatch Alarms & Amazon SNS
Automated alarm rules trigger instant Email notifications to site reliability engineers via **Amazon SNS (Simple Notification Service)**:

| Alarm Rule Name | Trigger Condition | Automated Action |
|---|---|---|
| `High-Lambda-Error-Alarm` | Lambda function error count > 5 within 5 minutes | Dispatches urgent alert email to DevSecOps team |
| `API-Gateway-5xx-Alarm` | 5xx HTTP error rate on API Gateway exceeds 1% | Alerts engineers to potential backend service outages |
| `ESP32-Offline-Alarm` | Sensor node heartbeat missing for over 3 minutes | Flags potential Wi-Fi connection loss at physical bay |

### 3.5.5. Cloud Cost Management via AWS Budgets & Cost Explorer
The project enforces financial governance using **AWS Budgets**:
* **Monthly Budget Threshold:** Configured a $20.00 USD monthly budget cap covering staging and production environments.
* **Automated Cost Alerts:** Dispatches email notifications when actual spending reaches **80% ($16.00)** and **100% ($20.00)** of the budget threshold.
* **Cost Breakdown Analytics:** Monitors daily itemized charges per service (DynamoDB, Lambda, Rekognition, CloudFront).

### 3.5.6. Security Audit Trail Logging via AWS CloudTrail
AWS CloudTrail records all administrative API calls and infrastructure configuration changes:
* Auditing IAM policy modifications, AWS WAF rule updates, and Cognito User Pool setting changes.
* Ensures security compliance and provides audit trails during security incident retrospectives.

### 3.5.7. Incident Management & Support Workflow
1. **Detection:** CloudWatch Alarm triggers an SNS notification alerting the operations team.
2. **Root Cause Analysis:** SRE team runs CloudWatch Logs Insights filtering by Lambda `RequestId`.
3. **Remediation & Redeployment:** Fixes are deployed using AWS CDK CLI, verifying metric recovery on CloudWatch Dashboards.

### 3.5.8. Summary
The CloudWatch operational monitoring suite and AWS Budgets cost governance framework provide comprehensive management oversight for the **Smart Parking IoT Web Platform**, maintaining high availability, low latency, and strict cloud cost controls.
