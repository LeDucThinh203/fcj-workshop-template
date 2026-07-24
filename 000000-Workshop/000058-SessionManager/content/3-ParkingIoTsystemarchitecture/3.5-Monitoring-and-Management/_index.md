---
title : "Monitoring and Management"
date: 2026-05-13
weight : 5
chapter : false
pre : " <b> 3.5. </b> "
---

This section outlines the operational monitoring, performance auditing, and cost governance strategy deployed for the **Smart Parking IoT Web Platform** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)) running on AWS Serverless infrastructure.

The monitoring suite leverages native AWS observability tools (Lambda ANPR, Lambda AI Chatbot, Lambda AI 7-Day Forecast, AppSync WebSockets, API Gateway, IoT Core, S3, DynamoDB, Rekognition) to maintain continuous high availability (99.9% Uptime SLA), low API latency for the Web App, and predictable cloud spending:
* **Amazon CloudWatch:** Centralized management of CloudWatch Dashboards, API Gateway/Lambda/AppSync Log Groups, and automated CloudWatch Alarms for error thresholds.
* **AWS Budgets & Cost Explorer:** Real-time tracking of daily AWS service expenditures with automated Email notifications when costs breach 80% of defined budget thresholds.
* **AWS CloudTrail:** Complete security audit logging of API calls and configuration changes across all AWS infrastructure resources.
* **IAM Security Governance:** Periodic audit and enforcement of Least Privilege policies for Lambda execution roles and API Gateway authorizers.

### 3.5.1. Operational Monitoring Objectives
The operations framework guarantees seamless 24/7 Web App execution and enables rapid root-cause diagnosis for site engineers.

**Primary Monitoring Objectives:**
* **Lambda Microservices SLA:** Maintain execution duration under 500ms and keep function error rate below 0.1% across ANPR, AI Chatbot, and AI 7-Day Forecast Lambdas.
* **AWS AppSync WebSockets Tracking:** Monitor concurrent Chatbox Socket connections and GraphQL Subscription broadcast latency.
* **API Gateway Traffic Ingestion:** Monitor HTTPS query volume from the Web App, tracking 4xx/5xx HTTP response codes.
* **IoT Core Connection Tracking:** Monitor ESP32 sensor MQTT message delivery rates and device online status.
* **ANPR Pipeline Auditing:** Detect failures during image feature extraction or Rekognition plate parsing.
* **Cloud Budget Governance:** Ensure monthly AWS infrastructure costs remain within projected budget caps.

### 3.5.2. Centralized Operations via Amazon CloudWatch Dashboards
The engineering team created an **AWS CloudWatch Operational Dashboard** consolidating key real-time metrics:
1. **API Gateway & AppSync Invocations:** Real-time chart tracking Web App request volume, WebSockets Chatbox message rates, and latency.
2. **Lambda Microservices Duration & Error Rates:** Execution duration histograms and exception counters for Lambda Backend, ANPR, AI Chatbot, and AI 7-Day Forecast Lambdas.
3. **DynamoDB Consumed Capacity Units:** Read/Write capacity metrics for `ParkingSlots`, `VehicleLogs`, `TrafficForecasts`, and `ChatMessages` tables.
4. **AWS IoT Core Telemetry Message Rate:** Ingested MQTT payload volume received from ESP32 bay sensors.

### 3.5.3. CloudWatch Log Groups & Log Insights
Logs from API Gateway, AppSync, Lambda microservices, and IoT Rules stream to CloudWatch Logs with a 30-day retention policy.

### 3.5.4. Automated Alerting via CloudWatch Alarms & Amazon SNS
Automated SNS alerts dispatches email notifications upon Lambda errors or API 5xx spikes.

### 3.5.5. Cloud Cost Management via AWS Budgets & Cost Explorer
Enforces $20.00 USD monthly budget cap with automated email alerts at 80% and 100%.

### 3.5.6. Security Audit Trail Logging via AWS CloudTrail
CloudTrail records administrative API calls and IAM configuration changes.

### 3.5.7. Summary
The CloudWatch operational monitoring suite and AWS Budgets cost governance framework provide comprehensive management oversight for the **Smart Parking IoT Web Platform**.
