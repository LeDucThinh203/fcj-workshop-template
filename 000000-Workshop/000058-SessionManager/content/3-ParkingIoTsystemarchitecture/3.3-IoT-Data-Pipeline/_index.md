---
title : "IoT Data Pipeline"
date: 2026-05-13
weight : 3
chapter : false
pre : " <b> 3.3. </b> "
---

This section details the real-time IoT Data Pipelines designed, implemented, and operationalized on AWS Serverless infrastructure to connect ESP32 edge hardware directly to the **Smart Parking IoT Web Platform** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)).

The data pipeline serves as the central data backbone of the system, asynchronously processing multiple telemetry streams: **Vehicle Image Data** (ANPR), **Bay Occupancy Sensor Data**, **Real-time WebSockets Chatbox Stream (AWS AppSync)**, **AWS Lambda AI Chatbot**, and the **AWS Lambda AI 7-Day Vehicle Traffic Forecasting Model**.

### 3.3.1. Data Pipeline Architecture Overview
Telemetry gathered from the physical parking lot undergoes automated ingestion, processing, and persistence from edge nodes to the Web App UI.

**High-Level Data Pipeline Diagram:**
`ESP32 Edge Devices → AWS IoT Core / Amazon S3 → AWS Lambda Microservices (ANPR, AI Chatbot, AI Forecast) → Amazon Rekognition / DynamoDB → AWS AppSync (WebSockets) / API Gateway → Web App UI`.

**Core Telemetry & Analytics Ingestion Streams:**

| Telemetry Stream | Data Input | AWS Processing Engine | Web App Output |
|---|---|---|---|
| **Image ANPR Pipeline** | Vehicle photo from ESP32-CAM | S3 Bucket, Lambda, Amazon Rekognition | Vehicle entry/exit logs, extracted plate string, photo display |
| **Sensor Status Pipeline** | MQTT payload from ESP32 Sensor | AWS IoT Core, IoT Rule, Lambda, DynamoDB, AppSync Subscription | Live green/red bay occupancy status map updated via WebSockets |
| **AppSync WebSockets Chatbox** | Socket messages from Web Chatbox | AWS AppSync WebSockets, Lambda AI Chatbot, DynamoDB | Real-time chat responses streamed to the Web Chatbox UI |
| **AI 7-Day Traffic Forecast** | Vehicle log history from `VehicleLogs` | EventBridge Cron, Lambda AI Forecast, DynamoDB | 7-day predicted vehicle traffic density line chart on Admin Dashboard |

### 3.3.2. Image ANPR Processing Pipeline
The vehicle image processing pipeline is engineered for rapid license plate extraction during gate arrival.

### 3.3.3. Amazon S3 Bucket Layout & Object Metadata
Images are stored in a structured hierarchy inside Amazon S3.

### 3.3.4. Optical License Plate Detection via Amazon Rekognition
The `Lambda Image Processing` service calls **Amazon Rekognition** to detect bounding box text fragments matching license plate string patterns.

### 3.3.5. Parking Slot Telemetry Pipeline & AWS AppSync Subscriptions
The parking bay status stream operates continuously in real time: ESP32 sensor MQTT payload ➔ AWS IoT Core ➔ `Lambda Sensor Processing` ➔ DynamoDB update ➔ **AWS AppSync Mutation** ➔ Broadcast **GraphQL Subscription** (`onUpdateParkingSlot`) over WebSockets.

### 3.3.6. WebSockets Chatbox Pipeline via AWS AppSync & Lambda AI Chatbot
Client browser sends GraphQL Mutation `sendMessage` over **AWS AppSync WebSockets** ➔ `Lambda AI Chatbot` processes query ➔ Logs conversation in DynamoDB `ChatMessages` ➔ AppSync broadcasts `onNewChatMessage` Subscription back to Web UI.

### 3.3.7. AWS Lambda AI 7-Day Vehicle Traffic Forecasting Data Pipeline
The predictive traffic analytics pipeline operates as follows:

1. **Historical Data Aggregation:** `Lambda AI 7-Day Forecast` queries past 30-day vehicle entry/exit history from DynamoDB table `VehicleLogs`.
2. **Time-Series Predictive Modeling:** Machine learning forecasting algorithm computes expected hourly vehicle volume for the next 7 days (Day +1 to Day +7).
3. **Forecast Persistence:** Results are persisted into DynamoDB table `TrafficForecasts`.
4. **Admin Dashboard Visualization:** Web Frontend calls API Gateway `GET /api/ai/forecast-7days` to render an interactive 7-day traffic density trend line chart for parking managers.

### 3.3.8. Fault Tolerance & Dead Letter Queue (DLQ) Integration
The data pipeline includes built-in fault tolerance with SQS DLQ queues and exponential backoff retry.

### 3.3.9. Summary
The IoT Data Pipeline combined with **AWS AppSync WebSockets Chatbox**, **AWS Lambda AI Chatbot**, and **AWS Lambda AI 7-Day Vehicle Traffic Forecasting** provides a cutting-edge real-time and predictive analytics data infrastructure.
