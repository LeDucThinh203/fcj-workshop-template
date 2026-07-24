---
title : "AWS Core Infrastructure"
date: 2026-05-13
weight : 1
chapter : false
pre : " <b> 3.1. </b> "
---

This section presents the complete architecture and deployment of the core AWS cloud infrastructure researched, built, and operationalized to power the **Smart Parking IoT Web Platform** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)).

The cloud infrastructure is constructed entirely on the **AWS Serverless** model, leveraging the combined capabilities of **Amazon S3, Amazon DynamoDB, AWS Lambda, Amazon API Gateway, AWS AppSync (GraphQL & WebSockets Chatbox), AWS IoT Core, IAM, Amazon CloudFront, AWS WAF**, and **Amazon CloudWatch**. This serverless model empowers the Web App to maintain high availability, eliminates physical server administration overhead, and scales automatically under sudden spikes in Web traffic or vehicle volume.

### 3.1.1. Strategic Objectives of Deployed Core Infrastructure
The AWS core cloud infrastructure fulfills the operational and functional requirements of the system:

* **Web App Delivery:** Serve static SPA assets via Amazon S3 Static Website Hosting backed directly by Amazon CloudFront CDN and AWS WAF security.
* **Edge IoT Integration:** Receive gate vehicle captures from ESP32-CAM via S3 Presigned URLs and parking slot occupancy telemetry via AWS IoT Core (MQTT over TLS).
* **Real-time WebSockets Communication (AWS AppSync):** Establish bidirectional WebSockets channels managed by AWS AppSync GraphQL API to power the interactive real-time Chatbox widget and push live floor map updates.
* **Serverless Compute & AI Microservices (AWS Lambda):**
  - **Lambda ANPR:** Automated license plate recognition via Amazon Rekognition.
  - **Lambda AI Chatbot:** Virtual Assistant Chatbot for automated user guidance and parking Q&A.
  - **Lambda AI 7-Day Traffic Forecasting Model:** Time-series machine learning model forecasting vehicle traffic volume over the next 7 days, powering predictive charts on the Admin Dashboard.
* **High-Speed Data Persistence:** Store vehicle audit logs, real-time slot states, 7-day traffic forecasts, chat histories, and user account metadata in Amazon DynamoDB with sub-millisecond query performance.
* **API Exposure:** Expose secured RESTful APIs via Amazon API Gateway and real-time GraphQL APIs via AWS AppSync protected with Amazon Cognito Authorizer.
* **Security & Operations Governance:** Enforce strict IAM Least Privilege access permissions and monitor system logs/metrics in real-time with Amazon CloudWatch.

### 3.1.2. Infrastructure as Code (IaC) with AWS CDK
All AWS cloud resources are defined and provisioned automatically using **AWS CDK (TypeScript)**.

**Deployed CDK Project Structure:**
```text
parking-iot-cdk/
├── bin/
│   └── parking-iot.ts            # Main app entry initializing stacks
├── lib/
│   ├── storage-stack.ts          # Defines S3 Buckets & DynamoDB Tables
│   ├── api-stack.ts              # Defines API Gateway & Lambda Microservices
│   ├── appsync-stack.ts          # Defines AWS AppSync GraphQL Schema & WebSockets Chatbox
│   ├── iot-stack.ts              # Defines AWS IoT Core Rules & Topics
│   ├── auth-stack.ts             # Defines Cognito User Pools & Authorizers
│   ├── ai-chatbot-stack.ts       # Defines AWS Lambda AI Chatbot Assistant
│   ├── ai-forecast-stack.ts      # Defines AWS Lambda AI 7-Day Traffic Forecasting Model
│   └── monitoring-stack.ts       # Defines CloudWatch Dashboards & Alarms
├── package.json
└── cdk.json
```

**Core CDK Resource Stacks Overview:**

| CDK Stack | Provisioned AWS Services | Web Platform Role |
|---|---|---|
| **Storage Stack** | Amazon S3, DynamoDB | Stores web build assets, vehicle photos, forecast models, and DynamoDB tables |
| **API Stack** | API Gateway, AWS Lambda | Exposes backend REST APIs and business logic for the Web App |
| **AppSync Stack** | AWS AppSync (GraphQL & WebSockets) | Provides real-time Socket connectivity for Chatbox and Subscriptions |
| **IoT Stack** | AWS IoT Core, IoT Rules | Ingests MQTT telemetry from ESP32 parking slot sensors |
| **Auth Stack** | Amazon Cognito, IAM Roles | Manages Web User registration, login, and JWT API authentication |
| **AI Chatbot Stack** | AWS Lambda | Powers the interactive AI Virtual Assistant Chatbot on the Web UI |
| **AI Forecast Stack** | AWS Lambda, DynamoDB | Computes 7-day vehicle traffic volume forecasts for the Admin Dashboard |
| **Monitoring Stack** | CloudWatch, AWS Budgets | Tracks application health metrics, audit logs, and cost budgets |

### 3.1.3. AWS AppSync & Real-time WebSockets Chatbox Infrastructure
AWS AppSync manages GraphQL API infrastructure and bidirectional WebSockets connections for the Web App Chatbox widget and live GraphQL Subscriptions (`onUpdateParkingSlot`, `onNewChatMessage`).

### 3.1.4. Amazon S3 Storage & CloudFront CDN Infrastructure
* **S3 Static Website Hosting:** Hosts static compiled Web assets distributed directly via Amazon CloudFront CDN (`https://d3imp0j8sdburp.cloudfront.net`).
* **S3 Vehicle Image Storage:** Receives gate captures from ESP32-CAM via S3 Presigned URLs.

### 3.1.5. Amazon DynamoDB Database Architecture
Amazon DynamoDB serves as the core NoSQL database, configured with On-Demand Capacity for real-time read/write traffic.

**Primary Data Tables:**

| Table Name | Partition Key | Sort Key | Web App Functionality |
|---|---|---|---|
| `ParkingSlots` | `slot_id` (String) | - | Tracks real-time status (`available`/`occupied`) of every slot |
| `VehicleLogs` | `log_id` (String) | `timestamp` (String) | Stores entry/exit timestamps, ANPR plate text, and S3 image URLs |
| `TrafficForecasts` | `forecast_date` (String) | `slot_zone` (String) | Stores 7-day vehicle traffic forecasting model predictions |
| `ChatMessages` | `chat_id` (String) | `timestamp` (String) | Stores Chatbox conversation history between user and AI Chatbot |
| `Users` | `user_id` (String) | - | Stores registered user profile information and settings |

### 3.1.6. Serverless AWS Lambda Microservices Layer
The backend logic is decoupled into event-driven AWS Lambda microservices:

| Lambda Function | Trigger Event | Business Responsibility |
|---|---|---|
| **Lambda API Backend** | API Gateway / AppSync Resolver | Handles REST/GraphQL API requests from the Web App Frontend |
| **Lambda Presigned URL** | API Gateway (`GET /upload-url`) | Generates time-limited S3 upload presigned URLs for ESP32-CAM |
| **Lambda Image Processing** | S3 `ObjectCreated` Event | Fetches image, calls Amazon Rekognition ANPR, logs plate to DynamoDB |
| **Lambda Sensor Processing** | AWS IoT Core Rule (MQTT) | Consumes slot sensor MQTT payload, updates DynamoDB, triggers AppSync |
| **Lambda AI Chatbot** | AWS AppSync / API Gateway (`POST /chat`) | Virtual Assistant Chatbot executing NLP & user query responses |
| **Lambda AI 7-Day Forecast** | EventBridge Cron / API Gateway (`GET /forecast-7days`) | Computes time-series traffic predictions over the next 7 days |

### 3.1.7. API Gateway & AWS AppSync Integration
The system integrates API Gateway (for REST APIs, Presigned URLs & 7-Day Forecast endpoint) and **AWS AppSync** (for GraphQL Queries, Mutations & WebSockets Chatbox).

### 3.1.8. Network & Security Architecture
CloudFront CDN, API Gateway, and AppSync WebSockets traffic are encrypted via TLS 1.3/HTTPS, backed by AWS WAF rate limiting and Cognito authorization.

### 3.1.9. Summary
The AWS Serverless core infrastructure integrated with **AWS AppSync WebSockets Chatbox**, **AWS Lambda AI Chatbot**, and **AWS Lambda AI 7-Day Vehicle Traffic Forecasting** delivers an advanced, predictive smart parking web platform ready for production scale.
