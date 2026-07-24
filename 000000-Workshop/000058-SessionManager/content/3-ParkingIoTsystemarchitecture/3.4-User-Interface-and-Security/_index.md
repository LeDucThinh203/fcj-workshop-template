---
title : "User Interface and Security"
date: 2026-05-13
weight : 4
chapter : false
pre : " <b> 3.4. </b> "
---

This section details the **Smart Parking IoT Web Application Platform** ([https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)) interface features and **Multi-Layered Cloud Security Architecture** deployed on AWS Serverless.

The Web App serves as a real-time Operational Control Center for parking managers and a Self-Service Portal for parking customers, featuring integrated AWS Lambda AI capabilities and cloud security safeguards.

### 3.4.1. Deployed Web App Platform Overview
The Web App frontend is built using modern HTML5/CSS3/JavaScript standards, fully responsive across Desktop browsers and Mobile devices.

**Core Web App Features:**
* 🔑 **User Authentication System:** Secure signup, sign-in, and session management via Amazon Cognito User Pool.
* 📊 **Real-time Parking Slot Map:** Visual interactive representation of parking bays rendered in Green (Available) vs Red (Occupied).
* 🚗 **Vehicle Entry/Exit ANPR Audit Logs:** Historical feed of gate entries/exits displaying ESP32-CAM photos and extracted license plate metadata.
* 🔍 **License Plate Search Engine:** Instant lookup for vehicle history and photo records by plate number query string.
* 🤖 **AI Virtual Assistant (AWS Lambda AI Service):** Embedded AI chat widget providing natural language Q&A and operational analytics.
* 📈 **Occupancy & Density Analytics:** Graphical charts illustrating peak parking hours and turnover rates.

{{% notice tip "Live Access Credentials" %}}
🌐 **Web CloudFront Live Deploy:** [https://d3imp0j8sdburp.cloudfront.net](https://d3imp0j8sdburp.cloudfront.net)  
🔑 **Admin Demo Account:** `leducthinh203` | **Password:** `Admin123@`  
🎬 Watch UI walkthrough video and view screenshots in the [Google Drive FE Demo Folder](https://drive.google.com/drive/folders/1RLwMvlmJNH05ot-FZzCE_2U7c10_8zqz?usp=sharing).
{{% /notice %}}

### 3.4.2. High-Speed Web Delivery via Amazon S3 & CloudFront CDN
Static web assets are hosted on Amazon S3 Static Website Hosting and globally accelerated directly via **Amazon CloudFront CDN** (`https://d3imp0j8sdburp.cloudfront.net`).

**Benefits of CloudFront + S3 Hosting Architecture:**
* **Sub-Second Page Load:** Static assets cached at CloudFront edge locations deliver latency under 100ms globally.
* **Automated HTTPS Encryption:** ACM SSL/TLS certificates enforce encrypted HTTPS communication between web browsers and AWS edge endpoints.
* **S3 Offloading:** CloudFront caches handle up to 95% of static requests without incurring S3 read operation charges.

### 3.4.3. Direct Routing & Delivery via Amazon CloudFront CDN
The platform utilizes direct CloudFront CDN domain distribution to serve frontend assets to end-users without requiring complex Route 53 DNS setup:
`Web User → CloudFront Distribution Domain (https://d3imp0j8sdburp.cloudfront.net) → Amazon S3 Bucket`.

### 3.4.4. Web Platform Protection via AWS WAF (Web Application Firewall)
AWS WAF is deployed at the outer edge in front of CloudFront to mitigate web security threats:
* **Exploit Mitigation:** Filters malicious payloads attempting SQL Injection (SQLi) or Cross-Site Scripting (XSS).
* **Rate Limiting Rules:** Automatically blocks client IP addresses exceeding 100 requests per minute to prevent DDoS and Brute Force attacks.
* **IP Reputation Lists:** Enforces AWS Managed Rulesets to block known bad IP addresses.

### 3.4.5. User Authentication via Amazon Cognito User Pool
Identity and access management is powered by **Amazon Cognito User Pool**:

**Authentication & API Authorization Workflow:**
1. User submits credentials on the Web App login form.
2. Web App sends authentication request to the Cognito User Pool Endpoint.
3. Cognito authenticates credentials and returns **JSON Web Tokens (JWT)**: `ID Token`, `Access Token`, and `Refresh Token`.
4. Web App attaches the token in HTTP headers `Authorization: Bearer <JWT_Token>` for subsequent API Gateway calls.
5. API Gateway Cognito Authorizer validates token signature and claims before executing backend Lambda functions.

### 3.4.6. Role-Based Access Control (RBAC)
The Web App enforces explicit role permissions:

| Access Role | Target Users | Web App Accessible Features |
|---|---|---|
| **Role: User (Customer)** | Registered parking users | Pre-arrival slot availability lookup, vehicle binding, AI assistant chat |
| **Role: Admin (Manager)** | Account `leducthinh203` | Real-time floor map monitoring, full vehicle audit logs, ANPR plate search, analytics dashboards |

### 3.4.7. AI Virtual Assistant (AWS Lambda AI Service)
An intelligent chat widget is embedded directly into the Web App interface:
* **Underlying Technology:** Powered by **AWS Lambda AI Service** connecting directly to DynamoDB tables and natural language processing logic.
* **Capabilities:**
  - Answers user queries: *"Are there available slots in Zone A right now?"*, *"What are the parking fee rules?"*.
  - Assists admins with natural language analytics queries: *"Summarize vehicle entries between 8 AM and 10 AM today"*.

### 3.4.8. Security Compliance & IAM Least Privilege
* User passwords stored in Cognito are encrypted using Salted SHA-256 hash algorithms.
* Backend Lambda execution roles enforce IAM Least Privilege policies, preventing an image processing function from accessing sensitive user tables.

### 3.4.9. Summary
The Web Application frontend combined with AWS multi-layered cloud security delivers a state-of-the-art, secure, and intuitive smart parking platform ready for production scale.
