---
title : "ESP32 Edge Devices"
date: 2026-05-13
weight : 2
chapter : false
pre : " <b> 3.2. </b> "
---

This section details the hardware edge device integration (ESP32 Edge Devices) deployed at the parking site to continuously feed real-time telemetry into the **Smart Parking IoT Web Platform** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)).

Edge hardware serves as the primary visual sensors and physical detection nodes feeding data into the Web App platform, utilizing two specialized ESP32 device categories:
* **ESP32-CAM (Entry / Exit Gates):** Automatically triggers high-resolution image capture upon vehicle arrival, requests S3 Presigned URLs, and uploads image payloads directly to Amazon S3 to initiate Automatic Number Plate Recognition (ANPR).
* **ESP32 Sensor Devices (Ultrasonic / IR Sensors):** Installed at individual parking bays to measure distance, determine slot availability (`available` vs `occupied`), and publish MQTT status messages to AWS IoT Core.

All telemetry stream data from ESP32 edge nodes is automatically processed by AWS Serverless services and synchronized directly to the **Web Dashboard**, allowing site administrators and users to view real-time parking floor maps seamlessly without latency.

### 3.2.1. Role of Edge Devices in the Web App Ecosystem
The deployed ESP32 edge devices act as an automated telemetry acquisition layer, interacting directly with physical parking infrastructure and transmitting structured data payload streams to the AWS Cloud.

**Core Edge Device Responsibilities:**
* **Gate Entry/Exit Monitoring:** Detect incoming/outgoing vehicles, capture photos, and upload image payloads to Amazon S3 via Presigned URLs.
* **Slot Occupancy Detection:** Measure distance at individual parking bays and publish MQTT status updates to AWS IoT Core.
* **Real-Time Data Synchronization:** Maintain end-to-end data delivery latency from edge hardware to Web Dashboard under 1.5 seconds.
* **Automated Parking Operations:** Eliminate manual vehicle logging by security personnel.

### 3.2.2. ESP32-CAM Subsystem (Gate Capture & ANPR Trigger)
ESP32-CAM hardware modules are mounted at the entrance gate and exit gate, calibrated for lighting and camera angles to capture clear vehicle front/rear plates.

**Hardware Specs & Workflow Pipeline:**
* **Hardware Module:** ESP32-CAM board with OV2640 camera sensor, onboard LED flash, and 2.4GHz Wi-Fi connectivity.
* **Image Transmission Flow:**
  `Vehicle Arrival → Sensor Detect → ESP32-CAM Capture → API Gateway Presigned URL Request → Direct S3 JPEG Upload`.

**Sample Image Payload Metadata from ESP32-CAM:**
```json
{
  "device_id": "esp32_cam_entrance_01",
  "gate_type": "entrance",
  "image_name": "cam01_20260513_091528.jpg",
  "timestamp": "2026-05-13T09:15:28Z",
  "upload_status": "success"
}
```

### 3.2.3. ESP32 Sensor Subsystem (Bay Occupancy Detection)
Each parking bay is equipped with an ESP32 micro-controller interfaced with ultrasonic sensors (HC-SR04) or infrared sensors.

**Distance Thresholds & State Decisions:**
* Distance `< 50 cm`: Bay status classified as `occupied`.
* Distance `>= 50 cm`: Bay status classified as `available`.

**Parking Slot State Representation on Web Dashboard:**

| Bay Status | Payload State | Web Dashboard Visualization |
|---|---|---|
| Available Slot | `available` | Green Indicator - Open for user parking |
| Occupied Slot | `occupied` | Red Indicator - Displays current parked vehicle plate |

**Sensor Telemetry Pipeline:**
`ESP32 Sensor → AWS IoT Core (MQTT over mTLS) → AWS IoT Rule → Lambda Sensor Processing → DynamoDB → Web App UI`.

### 3.2.4. ESP32 Firmware Source Code & AWS IoT Core Connectivity
Firmware running on ESP32 is built using C++/Arduino Framework, utilizing `PubSubClient` and `WiFiClientSecure` libraries to establish encrypted mTLS connections to AWS IoT Core endpoints.

**Deployed Firmware Characteristics:**
- **Security Certificates:** Embedded AWS Root CA, Device Certificate, and Private Key in ESP32 encrypted flash memory.
- **Sensor Polling Routine:** Polls distance sensor every 2 seconds; upon state transition, constructs JSON payload and publishes to MQTT topic `parking/slots/{slot_id}/status`.

### 3.2.5. Presigned URL Upload Mechanism for ESP32-CAM
To prevent API Gateway and Lambda compute bottlenecks during large binary image transfers, ESP32-CAM employs S3 Presigned URLs:
1. ESP32-CAM sends an HTTP GET request to API Gateway endpoint `/api/camera/presigned-url`.
2. API Gateway triggers `Lambda Presigned URL` to generate a 5-minute time-bound S3 Upload URL.
3. ESP32-CAM receives the URL and issues an HTTP PUT request uploading the JPEG image directly into the Amazon S3 Bucket.

### 3.2.6. Edge Device Health Synchronization on Web Dashboard
The Web App features an Edge Device Health Monitoring table displaying real-time hardware status:
* **Heartbeat Ping:** ESP32 nodes emit a heartbeat ping every 60 seconds to MQTT topic `parking/devices/heartbeat`.
* **Connection Status:** Web Dashboard displays Green (Online) or Gray (Offline) badges, allowing site managers to spot hardware power outages or Wi-Fi disconnects.

### 3.2.7. Noise Filtering & Hardware Reliability
* **Sensor Debouncing:** Takes 5 consecutive distance measurements before triggering a state change, filtering out transient interference from walking pedestrians.
* **Auto-Reconnect Handler:** Automatic Wi-Fi and MQTT reconnection routine using exponential backoff strategy to ensure unattended hardware resilience.

### 3.2.8. Summary
The ESP32-CAM and ESP32 Sensor edge devices provide reliable frontline data acquisition. By connecting securely via mTLS to AWS IoT Core and S3, the edge layer feeds continuous real-time telemetry to the **Smart Parking IoT Web Platform**, powering the real-time floor map display and ANPR license plate recognition workflows.
