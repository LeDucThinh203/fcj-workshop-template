---
title : "User Interface and Security"
date: 2026-05-13
weight : 4
chapter : false
pre : " <b> 3.4. </b> "
---

This section details the **Smart Parking IoT Web Application Platform** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)) interface features and **Multi-Layered Cloud Security Architecture** deployed on AWS Serverless.

The Web App serves as a real-time Operational Control Center for parking managers and a Self-Service Portal for parking customers, featuring an integrated **AWS Lambda AI Chatbot Assistant**, **AWS Lambda AI 7-Day Vehicle Traffic Forecasting Chart**, **AWS AppSync WebSockets Chatbox**, and cloud security safeguards.

### 3.4.1. Deployed Web App Platform Overview
The Web App frontend is built using modern HTML5/CSS3/JavaScript standards, fully responsive across Desktop browsers and Mobile devices.

**Core Web App Features:**
* 🔑 **User Authentication System:** Secure signup, sign-in, and session management via Amazon Cognito User Pool.
* 📊 **Real-time Parking Slot Map:** Visual interactive representation of parking bays rendered in Green (Available) vs Red (Occupied), updated via **AWS AppSync Subscriptions**.
* 🚗 **Vehicle Entry/Exit ANPR Audit Logs:** Historical feed of gate entries/exits displaying ESP32-CAM photos and extracted license plate metadata.
* 🔍 **License Plate Search Engine:** Instant lookup for vehicle history and photo records by plate number query string.
* 📈 **AI 7-Day Vehicle Traffic Forecast Chart:** Interactive trend chart computed by the **AWS Lambda AI Forecast Model**, visualizing predicted traffic density over Day +1 to Day +7.
* 💬 **Real-time WebSockets Chatbox Widget (AWS AppSync):** Low-latency bidirectional Socket communication via GraphQL Subscriptions & WebSockets connection.
* 🤖 **AI Virtual Assistant Chatbot (AWS Lambda AI Chatbot):** Embedded AI chat widget providing natural language Q&A and automated user assistance.
* 📊 **Occupancy & Density Analytics:** Graphical charts illustrating peak parking hours and turnover rates.

{{% notice tip "Live Access Credentials" %}}
🌐 **Web CloudFront Live Deploy:** [https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)  
🔑 **Admin Demo Account:** `leducthinh203` | **Password:** `Admin123@`  
🎬 Watch UI walkthrough video and view screenshots in the [Google Drive FE Demo Folder](https://drive.google.com/drive/folders/1RLwMvlmJNH05ot-FZzCE_2U7c10_8zqz?usp=sharing).
{{% /notice %}}

### 3.4.2. High-Speed Web Delivery via Amazon S3 & CloudFront CDN
Static web assets are hosted on Amazon S3 Static Website Hosting and globally accelerated directly via **Amazon CloudFront CDN** (`https://d3imp0j8sdburp.cloudfront.net`).

### 3.4.3. Direct Routing & Delivery via Amazon CloudFront CDN
The platform utilizes direct CloudFront CDN domain distribution without requiring Route 53 DNS setup:
`Web User → CloudFront Distribution Domain (https://d3imp0j8sdburp.cloudfront.net) → Amazon S3 Bucket`.

### 3.4.4. Web Platform Protection via AWS WAF
Protected by AWS WAF rate limiting and exploit rulesets.

### 3.4.5. User Authentication via Amazon Cognito User Pool
Secured with JWT Tokens (`ID Token`, `Access Token`, `Refresh Token`).

### 3.4.6. Role-Based Access Control (RBAC)

| Access Role | Target Users | Web App Accessible Features |
|---|---|---|
| **Role: User (Customer)** | Registered parking users | Pre-arrival slot lookup, vehicle binding, AI assistant chat via WebSockets Chatbox |
| **Role: Admin (Manager)** | Account `leducthinh203` | Real-time floor map monitoring, ANPR plate search, **AI 7-Day Vehicle Traffic Forecast Chart** |

### 3.4.7. Integration of AI Chatbot, AI 7-Day Forecast & AWS AppSync WebSockets Chatbox
1. **WebSockets Chatbox (AWS AppSync):** Web dispatches `sendMessage` GraphQL Mutation over WebSockets ➔ `Lambda AI Chatbot` processes response ➔ AppSync broadcasts `onNewChatMessage` Subscription.
2. **AI Virtual Assistant Chatbot (AWS Lambda AI Chatbot):** Answers user parking questions automatically.
3. **AI 7-Day Traffic Forecast Chart (AWS Lambda AI Forecast):** Embedded on the Admin Dashboard, rendering time-series predictions for the upcoming 7 days to optimize site operations.

### 3.4.8. Security Compliance & IAM Least Privilege
Passwords hashed with Salted SHA-256; Least Privilege IAM roles assigned across microservices.

### 3.4.9. Summary
The Web Application frontend combined with AWS multi-layered cloud security, **AI 7-Day Traffic Forecasting**, **AI Chatbot Assistant**, and **AWS AppSync WebSockets Chatbox** delivers a state-of-the-art smart parking web platform.
