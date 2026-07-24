---
title : "AWS Core Infrastructure"
date: 2026-05-13
weight : 1
chapter : false
pre : " <b> 3.1. </b> "
---

This section presents the complete architecture and deployment of the core AWS cloud infrastructure researched, built, and operationalized to power the **Smart Parking IoT Web Platform** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)).

The cloud infrastructure is constructed entirely on the **AWS Serverless** model, leveraging the combined capabilities of **Amazon S3, Amazon DynamoDB, AWS Lambda, Amazon API Gateway, AWS IoT Core, IAM, Amazon CloudFront, AWS WAF**, and **Amazon CloudWatch**. This serverless model empowers the Web App to maintain high availability, eliminates physical server administration overhead, and scales automatically under sudden spikes in Web traffic or vehicle volume.

### 3.1.1. Strategic Objectives of Deployed Core Infrastructure
The AWS core cloud infrastructure fulfills the operational and functional requirements of the system:

* **Web App Delivery:** Serve static SPA assets via Amazon S3 Static Website Hosting backed directly by Amazon CloudFront CDN and AWS WAF security.
* **Edge IoT Integration:** Receive gate vehicle captures from ESP32-CAM via S3 Presigned URLs and parking slot occupancy telemetry via AWS IoT Core (MQTT over TLS).
* **Asynchronous Serverless Processing:** Trigger event-driven AWS Lambda functions for Automatic Number Plate Recognition (ANPR using Amazon Rekognition), parking slot state synchronization, and custom Lambda-based AI prompt handling.
* **High-Speed Data Persistence:** Store vehicle audit logs, real-time slot states, and user account metadata in Amazon DynamoDB with sub-millisecond query performance.
* **RESTful API Exposure:** Expose secured API endpoints via Amazon API Gateway protected with Amazon Cognito Authorizer for the Web App Frontend.
* **Security & Operations Governance:** Enforce strict IAM Least Privilege access permissions and monitor system logs/metrics in real-time with Amazon CloudWatch.

### 3.1.2. Infrastructure as Code (IaC) with AWS CDK
All AWS cloud resources are defined and provisioned automatically using **AWS CDK (TypeScript)**. This guarantees deployment reproducibility, maintainability, and infrastructure version control.

**Deployed CDK Project Structure:**
```text
parking-iot-cdk/
├── bin/
│   └── parking-iot.ts            # Main app entry initializing stacks
├── lib/
│   ├── storage-stack.ts          # Defines S3 Buckets & DynamoDB Tables
│   ├── api-stack.ts              # Defines API Gateway & Lambda Microservices
│   ├── iot-stack.ts              # Defines AWS IoT Core Rules & Topics
│   ├── auth-stack.ts             # Defines Cognito User Pools & Authorizers
│   ├── ai-stack.ts               # Defines AWS Lambda AI Service
│   └── monitoring-stack.ts       # Defines CloudWatch Dashboards & Alarms
├── package.json
└── cdk.json
```

**Core CDK Resource Stacks Overview:**

| CDK Stack | Provisioned AWS Services | Web Platform Role |
|---|---|---|
| **Storage Stack** | Amazon S3, DynamoDB | Stores web build assets, vehicle photos, and DynamoDB data tables |
| **API Stack** | API Gateway, AWS Lambda | Exposes backend REST APIs and business logic for the Web App |
| **IoT Stack** | AWS IoT Core, IoT Rules | Ingests MQTT telemetry from ESP32 parking slot sensors |
| **Auth Stack** | Amazon Cognito, IAM Roles | Manages Web User registration, login, and JWT API authentication |
| **AI Stack** | AWS Lambda | Powers the interactive AI Virtual Assistant service on the Web UI |
| **Monitoring Stack** | CloudWatch, AWS Budgets | Tracks application health metrics, audit logs, and cost budgets |

### 3.1.3. Amazon S3 Storage & CloudFront CDN Infrastructure
Amazon S3 is deployed in two dedicated roles:

1. **S3 Static Website Hosting (Web App Hosting):**
   - Stores production frontend compiled assets (HTML, CSS, JS, Images).
   - Distributed directly via Amazon CloudFront CDN (URL `https://d3imp0j8sdburp.cloudfront.net`) with SSL/TLS HTTPS encryption.
   - **Web Access Flow:** `User → CloudFront CDN (AWS WAF) → Amazon S3 Bucket`.

2. **S3 Vehicle Image Storage (Vehicle Photo Vault):**
   - Stores vehicle photos captured by entry/exit gate ESP32-CAM devices.
   - Utilizes S3 Presigned URLs so edge cameras upload images directly to S3 without intermediate server bottlenecks.
   - **Upload Pipeline:** `ESP32-CAM → API Gateway → Lambda Presigned URL → S3 Bucket → Triggers S3 ObjectCreated Event`.

### 3.1.4. Amazon DynamoDB Database Architecture
Amazon DynamoDB serves as the core NoSQL database, configured with On-Demand Capacity to handle real-time read/write traffic from the Web App and edge sensors.

**Primary Data Tables:**

| Table Name | Partition Key | Sort Key | Web App Functionality |
|---|---|---|---|
| `ParkingSlots` | `slot_id` (String) | - | Tracks real-time status (`available`/`occupied`) of every slot |
| `VehicleLogs` | `log_id` (String) | `timestamp` (String) | Stores entry/exit timestamps, ANPR plate text, and S3 image URLs |
| `SensorData` | `device_id` (String) | `timestamp` (String) | Stores raw sensor readings (distance cm, battery) for hardware analytics |
| `Users` | `user_id` (String) | - | Stores registered user profile information and settings |

### 3.1.5. Serverless AWS Lambda Microservices Layer
The backend logic is decoupled into event-driven AWS Lambda microservices:

| Lambda Function | Trigger Event | Business Responsibility |
|---|---|---|
| **Lambda API Backend** | Amazon API Gateway | Handles REST API requests from the Web App Frontend |
| **Lambda Presigned URL** | API Gateway (`GET /upload-url`) | Generates time-limited S3 upload presigned URLs for ESP32-CAM |
| **Lambda Image Processing** | S3 `ObjectCreated` Event | Fetches image, calls Amazon Rekognition ANPR, logs plate to DynamoDB |
| **Lambda Sensor Processing** | AWS IoT Core Rule (MQTT) | Consumes slot sensor MQTT payload and updates `ParkingSlots` table |
| **Lambda AI Service** | API Gateway (`POST /ai/chat`) | Executes custom Lambda AI logic for intelligent parking queries |

### 3.1.6. Amazon API Gateway Integration
Amazon API Gateway manages HTTPS REST requests from the Web App and ESP32-CAM edge devices, secured by an Amazon Cognito User Pool Authorizer.

**Key Deployed API Endpoints:**

| Method | Endpoint Path | Authorization | Functionality |
|---|---|---|---|
| `GET` | `/api/parking/slots` | Public / Authorized | Fetches real-time slot layout map status |
| `GET` | `/api/vehicle/logs` | Cognito Authorized | Retrieves vehicle entry/exit history logs |
| `GET` | `/api/vehicle/search` | Cognito Authorized | Searches vehicle records by license plate number |
| `POST` | `/api/camera/presigned-url` | Device Authenticated | Generates S3 Presigned URL for ESP32-CAM |
| `POST` | `/api/ai/chat` | Cognito Authorized | Routes prompt to AWS Lambda AI Service |

### 3.1.7. AWS IoT Core Device Management
AWS IoT Core maintains secure mTLS MQTT connections with ESP32 slot sensors.

* **MQTT Slot Topic:** `parking/slots/{slot_id}/status`
* **Sample Telemetry Payload:**
```json
{
  "device_id": "esp32_sensor_a01",
  "slot_id": "A01",
  "distance_cm": 25.4,
  "status": "occupied",
  "timestamp": "2026-05-13T09:15:30Z"
}
```
* **AWS IoT Rule:** Listens on topic `parking/slots/+/status` and invokes **Lambda Sensor Processing** to reflect slot occupancy updates on the Web Dashboard in real time.

### 3.1.8. Network & Security Architecture
* Managed services (S3, DynamoDB, IoT Core, Rekognition, Lambda AI, CloudWatch) operate as Regional AWS Services.
* **VPC Endpoints & Private Subnets** are configured for Lambda microservices requiring internal VPC routing.
* **AWS WAF (Web Application Firewall):** Attached directly to the CloudFront distribution to inspect incoming web traffic, block SQLi/XSS exploits, and enforce rate-limiting rules.

### 3.1.9. IAM Roles & Least Privilege Enforcement
All AWS services enforce strict IAM policies:
* **Lambda Image Processing Role:** Granted `s3:GetObject` on the photo bucket, `rekognition:DetectText`, and `dynamodb:PutItem` on `VehicleLogs`.
* **Lambda Sensor Processing Role:** Granted `dynamodb:UpdateItem` on the `ParkingSlots` table.
* **Lambda AI Service Role:** Granted DynamoDB read permissions to aggregate occupancy statistics.
* **API Gateway Role:** Granted `lambda:InvokeFunction` for designated backend Lambdas only.

### 3.1.10. Summary
The AWS Serverless core infrastructure provides a robust, scalable, and cost-efficient foundation powering the **Smart Parking IoT Web Platform**. The synthesis of CDK IaC automation, S3/DynamoDB storage, Lambda compute microservices, Rekognition ANPR, Lambda AI Service, and CloudFront CDN delivers an end-to-end smart parking web platform ready for production deployment.
