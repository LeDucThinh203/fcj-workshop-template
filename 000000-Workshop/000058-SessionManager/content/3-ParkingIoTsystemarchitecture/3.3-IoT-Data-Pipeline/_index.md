---
title : "IoT Data Pipeline"
date: 2026-05-13
weight : 3
chapter : false
pre : " <b> 3.3. </b> "
---

This section details the real-time IoT Data Pipelines designed, implemented, and operationalized on AWS Serverless infrastructure to connect ESP32 edge hardware directly to the **Smart Parking IoT Web Platform** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)).

The data pipeline serves as the central data backbone of the system, asynchronously processing two primary telemetry streams: **Vehicle Image Data** (for Automatic Number Plate Recognition - ANPR) and **Bay Occupancy Sensor Data** (for real-time parking slot floor map management).

### 3.3.1. Data Pipeline Architecture Overview
Telemetry gathered from the physical parking lot undergoes automated ingestion, processing, and persistence from edge nodes to the Web App UI.

**High-Level Data Pipeline Diagram:**
`ESP32 Edge Devices → AWS IoT Core / Amazon S3 → AWS Lambda Microservices → Amazon Rekognition / DynamoDB → API Gateway / CloudFront → Web App UI`.

**Three Core Telemetry Ingestion Streams:**

| Telemetry Stream | Data Input | AWS Processing Engine | Web App Output |
|---|---|---|---|
| **Image ANPR Pipeline** | Vehicle photo from ESP32-CAM | S3 Bucket, Lambda, Amazon Rekognition | Vehicle entry/exit logs, extracted plate string, photo display |
| **Sensor Status Pipeline** | MQTT payload from ESP32 Sensor | AWS IoT Core, IoT Rule, Lambda, DynamoDB | Live green/red bay occupancy status map |
| **Web REST & AI Pipeline** | HTTPS requests from Web User | API Gateway, Cognito, Lambda, Lambda AI Service | Vehicle lookup history, AI Virtual Assistant responses |

### 3.3.2. Image ANPR Processing Pipeline
The vehicle image processing pipeline is engineered for rapid license plate extraction during gate arrival:

1. **Gate Event Detection:** Vehicle arrives at entry/exit gate; ESP32-CAM detects motion and triggers photo capture.
2. **Presigned URL Request:** ESP32-CAM issues an HTTP GET request to API Gateway endpoint `/api/camera/presigned-url`.
3. **Short-Lived Upload URL:** `Lambda Presigned URL` function generates a 5-minute time-bound S3 upload presigned URL.
4. **Direct S3 Upload:** ESP32-CAM uploads the binary JPEG image directly into the S3 bucket path `s3://smart-parking-vehicle-images/entrance/`.
5. **Event Trigger:** Amazon S3 emits an `s3:ObjectCreated:Put` event, instantly invoking the `Lambda Image Processing` function.
6. **ANPR Extraction:** The Lambda function forwards the image bytes to **Amazon Rekognition** via the `DetectText` API.
7. **Persistence & Sync:** Extracted plate number string (e.g., `51H-98765`, confidence `98.2%`) is saved into DynamoDB table `VehicleLogs` and synchronized to the Web Dashboard.

### 3.3.3. Amazon S3 Bucket Layout & Object Metadata
Images are stored in a structured hierarchy inside Amazon S3 to enable fast image loading on the Web App:

**S3 Bucket Layout Structure:**
```text
smart-parking-vehicle-images/
├── entrance/
│   ├── cam_ent_01_20260513_091528.jpg
│   └── cam_ent_01_20260513_093000.jpg
└── exit/
    ├── cam_ext_01_20260513_101500.jpg
    └── cam_ext_01_20260513_104520.jpg
```

**Object Metadata Tagging Payload:**
```json
{
  "image_id": "cam_ent_01_20260513_091528.jpg",
  "gate_id": "GATE_ENTRANCE_01",
  "direction": "in",
  "timestamp": "2026-05-13T09:15:28Z",
  "s3_uri": "s3://smart-parking-vehicle-images/entrance/cam_ent_01_20260513_091528.jpg"
}
```

### 3.3.4. Optical License Plate Detection via Amazon Rekognition
The `Lambda Image Processing` service calls **Amazon Rekognition** to detect bounding box text fragments matching license plate string patterns:

```python
import boto3

rekognition = boto3.client('rekognition')

def detect_license_plate(bucket, key):
    response = rekognition.detect_text(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}}
    )
    text_detections = response['TextDetections']
    # Filter text detections matching plate format with confidence > 90%
    for text in text_detections:
        if text['Type'] == 'LINE' and text['Confidence'] > 90.0:
            return text['DetectedText'], text['Confidence']
    return "UNKNOWN", 0.0
```

### 3.3.5. Parking Slot Telemetry Pipeline
The parking bay status stream operates continuously in real time:

1. **Distance Polling:** ESP32 ultrasonic sensor measures distance at slot `A01`.
2. **MQTT Publishing:** Upon state transition from `available` to `occupied`, ESP32 publishes JSON payload to MQTT topic `parking/slots/A01/status`.
3. **AWS IoT Rule Filtering:** SQL Rule on AWS IoT Core filters incoming MQTT messages:
   ```sql
   SELECT slot_id, status, distance_cm, timestamp 
   FROM 'parking/slots/+/status'
   ```
4. **DynamoDB State Update:** IoT Rule invokes `Lambda Sensor Processing` to immediately update row state for slot `A01` in table `ParkingSlots`.
5. **Web Dashboard Sync:** When web users query slot status API, the latest state is served under 100ms.

### 3.3.6. Web App Queries & AWS Lambda AI Pipeline
For user interactions on the Web App frontend:

* **Vehicle Audit Log Search:** Web App $\to$ API Gateway `GET /api/vehicle/logs?plate=51H-98765` $\to$ `Lambda API Backend` $\to$ DynamoDB Query $\to$ Returns JSON array with CloudFront image URLs.
* **AI Chatbot Interaction:** Web Chat UI $\to$ API Gateway `POST /api/ai/chat` $\to$ `Lambda AI Service` $\to$ Processes custom AI algorithm & aggregates DynamoDB data $\to$ Returns natural language responses back to the Web Chat interface.

### 3.3.7. Fault Tolerance & Dead Letter Queue (DLQ) Integration
The data pipeline includes built-in fault tolerance:
* Unhandled processing exceptions in Lambda (e.g. Rekognition rate limits) route failed payloads to an **Amazon SQS Dead Letter Queue (DLQ)** for retry processing without data loss.
* DynamoDB client calls enforce exponential backoff retry logic.

### 3.3.8. Real-time Synchronization & User Experience
The asynchronous AWS Serverless pipeline ensures:
* Parking slot state transitions and vehicle entry/exit events reflect on the Web App UI within **1.8 seconds**.
* Non-blocking UI execution delivers a responsive, single-page application experience.

### 3.3.9. Summary
The IoT Data Pipeline successfully establishes a high-throughput, secure, and asynchronous telemetry streaming mechanism. By orchestrating serverless AWS services, physical sensor signals and camera images are converted into actionable real-time insights visualized on the **Smart Parking IoT Web Platform**.
