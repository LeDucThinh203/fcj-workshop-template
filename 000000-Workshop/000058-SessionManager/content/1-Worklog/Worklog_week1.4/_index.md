---
title: "Week 4 Worklog"
date: 2026-05-13
weight: 4
chapter: false
pre: " <b> 1.4 </b> "
---

## Week 4 Objectives:
- Initialize and configure network environments (VPC, Subnet Groups, Security Groups) for EC2 and RDS instances.
- Launch a Linux EC2 Instance, configure SSH Key Pair permissions, and establish secure SSH connections.
- Install Git, Node.js, and MySQL client on EC2 to deploy and connect a Node.js web application to an Amazon RDS database.
- Understand database management operations, including maintenance, monitoring logs, manual/automatic snapshots, and high-availability architecture.

## Tasks to be implemented this week:

| Day | Task | Start Date | End Date | Resource |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Overview of Amazon RDS<br>- Compare RDS with other storage services (EC2 DB, DynamoDB, Redshift, S3) | 11/05/2026 | 11/05/2026 | [Amazon RDS Documentation](https://docs.aws.amazon.com/rds/) |
| 3 | - Network setup for RDS:<br>  + Create VPC and subnets<br>  + Create Security Groups for EC2 and RDS<br>  + Create DB Subnet Group | 12/05/2026 | 12/05/2026 | [VPC for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) |
| 4 | - Practice initializing an Amazon RDS instance<br>- Configure DB engine, credentials, and database security options | 13/05/2026 | 13/05/2026 | [Creating an RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) |
| 5 | - Initialize EC2 Instance and prepare client environment:<br>  + Create Linux EC2 Instance<br>  + Configure SSH Key Pair permissions (`chmod 400`) and connect via SSH (MobaXterm)<br>  + Install Git and Node.js runtime environments on EC2 | 14/05/2026 | 14/05/2026 | [EC2 Linux Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)<br>FCJ Lab |
| 6 | - Deploy web application on EC2 and connect to RDS:<br>  + Clone repository and install dependencies<br>  + Install MySQL server client, execute SQL scripts to create databases and tables<br>  + Seed mock user data and verify connection via RDS Endpoint | 15/05/2026 | 15/05/2026 | [Connecting to RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html)<br>FCJ Lab |
| 7 - Sun | - Database administration and maintenance:<br>  + View RDS Logs & Events<br>  + Configure Maintenance & Backup options, perform manual/automatic Snapshots<br>  + Learn about Multi-AZ, Read Replicas, and clean up resources | 16/05/2026 | 17/05/2026 | [RDS Backup and Restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html)<br>FCJ Lab |

### Week 4 Results:
#### Theoretical:
- Mastered Amazon RDS knowledge: Benefits, supported DB engines, management features.
- Understood how Multi-AZ and Read Replicas work.
- Learned to differentiate when to use RDS, DynamoDB, Redshift, or S3.
- Understood security mechanisms (Security Groups, Encryption) and backups (Snapshots) on RDS.
#### Practical:
- Successfully set up a secure network environment for the Database (DB Subnet Group, Security Groups).
- Successfully initialized an Amazon RDS instance (MySQL/MariaDB).
- Successfully connected a Web application on EC2 to the RDS database via Endpoint.
- Successfully performed data backup and restoration using Snapshots.
- Efficiently managed resources and performed cleanup to avoid unnecessary costs.

### Evidences:

1. **SSH Key Pair Permissions Configuration (ec2_connection_key)**
   ![SSH Key Pair Permissions](/images/1-Worklog/Worklog_week1.4/ec2_connection_key.png)
   *Description: Demonstrates setting the appropriate permissions on the private key file (`.pem`) using the `chmod 400` command in the CLI. Restricting read/write permissions is a security requirement for SSH connections to prevent private keys from being exposed or utilized by other local users before establishing a connection.*

2. **Successful SSH Connection to Linux EC2 Public Instance (ec2_connection)**
   ![Successful SSH Connection](/images/1-Worklog/Worklog_week1.4/ec2_connection.png)
   *Description: Captures the CLI output of a successful SSH login session from the local client to the EC2 Public Instance using the configured Key Pair. The successful Amazon Linux terminal greeting confirms that the Internet Gateway routing and the Security Group's inbound rule for port 22 are operational.*

3. **Internal Routing and Connection to EC2 Private Instance (ec2_connection_Private)**
   ![Internal Connection to Private Instance](/images/1-Worklog/Worklog_week1.4/ec2_connection_Private.png)
   *Description: Practical evidence of successfully establishing an internal connection to the EC2 Private Subnet Instance from the EC2 Public Instance acting as a Bastion Host. Since the Private Instance has no public IP, this jump-host method ensures secure network containment and management.*



### 4. Create a VPC

**Creating a VPC with Subnets and Associated Resources**

{{% notice info %}}
**Information:** Amazon Virtual Private Cloud (Amazon VPC) enables you to launch AWS resources into a virtual network that you've defined. This virtual network closely resembles a traditional network in your own data center, with the benefits of using the scalable infrastructure of AWS.
{{% /notice %}}

Follow these steps to create a VPC with all necessary components for your Amazon RDS deployment:

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).
   ![Create a VPC](/images/1-Worklog/Worklog_week1.4/Create%20VPC.png)

2. On the VPC dashboard, choose **Create VPC**.

3. For **Resources to create**, select **VPC and more** to create a complete VPC environment.
   ![Create a VPC 1](/images/1-Worklog/Worklog_week1.4/Create%20VPC%201.png)

4. Configure the **Name tag auto-generation** option based on your preference. This allows AWS to automatically create consistent naming for all VPC resources.

5. Enter an **IPv4 CIDR block** range for your VPC (e.g., 10.0.0.0/16). This defines the IP address range available within your VPC.

6. (Optional) To enable IPv6 support, select **IPv6 CIDR block** and choose an Amazon-provided IPv6 range.

7. Select the appropriate **Tenancy** option:
   - **Default**: EC2 instances use the tenancy attribute specified during launch
   - **Dedicated**: All EC2 instances run on hardware dedicated to your account

   {{% notice tip %}}
   **Pro Tip:** Most workloads should use Default tenancy for cost efficiency. Only select Dedicated when you have specific compliance or licensing requirements.
   {{% /notice %}}

8. For **Number of Availability Zones (AZs)**, select at least two AZs for high availability.
   ![Create a VPC 2](/images/1-Worklog/Worklog_week1.4/Create%20VPC%202.png)

9. Configure your **Number of public subnets** and **Number of private subnets**. For Amazon RDS deployments, you'll typically need private subnets for your database instances and public subnets for resources that need internet access.

   {{% notice warning %}}
   **Security Note:** Place your RDS instances in private subnets to enhance security by preventing direct internet access to your databases.
   {{% /notice %}}

10. (Optional) If resources in private subnets need internet access, configure **NAT gateways** in each AZ where you have resources requiring outbound connectivity.

    {{% notice tip %}}
    **Pro Tip:** For production environments, deploy NAT gateways in each AZ to eliminate cross-AZ dependencies and improve fault tolerance.
    {{% /notice %}}

11. (Optional) For IPv6 outbound connectivity from private subnets, select **Yes** for **Egress-only Internet Gateway**.

12. (Optional) To enable private access to Amazon S3, select **VPC endpoints**, **S3 Gateway**. This creates a gateway endpoint that allows resources in your VPC to access S3 without using the public internet.

13. For **DNS options**, the default settings enable both DNS resolution and DNS hostnames, which are recommended for most deployments.

14. (Optional) Add tags to your VPC by expanding **Additional tags** and entering key-value pairs.

15. Review the **Preview** pane to see a visual representation of the VPC architecture you've configured.

16. Choose **Create VPC** to provision all the configured resources.
    ![Create a VPC 3](/images/1-Worklog/Worklog_week1.4/Create%20VPC%203.png)
    ![Create a VPC 4](/images/1-Worklog/Worklog_week1.4/Create%20VPC%204.png)

**Configuring Public IP Address Assignment for Subnets**

{{% notice info %}}
**Information:** The auto-assign public IPv4 address setting determines whether instances launched in a subnet automatically receive public IP addresses. For RDS deployments, your database subnets should typically have this setting disabled.
{{% /notice %}}

To modify the public IP address assignment behavior for a subnet:

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

2. In the navigation pane, choose **Subnets**.
   ![Create a VPC 5](/images/1-Worklog/Worklog_week1.4/Create%20VPC%205.png)

3. Select your subnet and choose **Actions**, then **Edit subnet settings**.
   ![Create a VPC 6](/images/1-Worklog/Worklog_week1.4/Create%20VPC%206.png)

4. Configure the **Auto-assign public IPv4 address** setting:
   - **Checked**: Instances launched in this subnet automatically receive a public IPv4 address
   - **Unchecked**: Instances launched in this subnet do not receive a public IPv4 address unless specifically requested during launch

   {{% notice warning %}}
   **Security Note:** For subnets that will host your RDS instances, ensure this setting is unchecked to prevent accidental public IP assignment.
   {{% /notice %}}

5. Choose **Save** to apply your changes.

{{% notice warning %}}
**Warning:** Default subnets have auto-assign public IPv4 addresses enabled by default. Always verify this setting when using default subnets for database deployments.
{{% /notice %}}

---

### 5. Create EC2 Security Group

**Creating a Security Group for EC2 Instances**

{{% notice info %}}
**Information:** Security groups act as virtual firewalls for your Amazon EC2 instances to control inbound and outbound traffic. For our RDS deployment, we need to create a security group for EC2 instances that will connect to our database.
{{% /notice %}}

Follow these steps to create a security group with the necessary ports:

1. Navigate to the AWS Management Console and sign in to your account.

2. In the AWS Management Console, search for and select **EC2** under services.

3. In the EC2 navigation pane, under **Network & Security**, select **Security Groups**.

4. Click the **Create security group** button.
   ![Create EC2 Security Group](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20Security%20Group.png)

5. In the **Basic details** section:
   - Enter a descriptive **Security group name** (e.g., "EC2-Web-App-SG")
   - Provide a meaningful **Description** (e.g., "Security group for EC2 instances connecting to RDS")
   - Select your **VPC** from the dropdown menu
   ![Configure Security Group Details](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20Security%20Group%201.png)

6. In the **Inbound rules** section, click **Add rule** to configure the following access:
   - **HTTP (80)**: Select "HTTP" from the Type dropdown (automatically sets port 80)
   - **HTTPS (443)**: Select "HTTPS" from the Type dropdown (automatically sets port 443)
   - **Custom TCP (5000)**: Select "Custom TCP" and enter "5000" in the Port range field
   - **SSH (22)**: Select "SSH" from the Type dropdown (automatically sets port 22)

   {{% notice warning %}}
   **Security Note:** For production environments, restrict the source IP addresses for SSH access to only trusted IP ranges rather than allowing access from anywhere (0.0.0.0/0).
   {{% /notice %}}

   ![Configure Inbound Rules](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20Security%20Group%202.png)

7. Review your settings and click **Create security group**.
   ![Create the Security Group](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20Security%20Group%203.png)

8. Once created, the new security group appears in your security groups list. Note the **Security Group ID** as you'll need it when launching EC2 instances.
   ![Security Group Created](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20Security%20Group%204.png)

{{% notice tip %}}
**Pro Tip:** You can modify security group rules at any time, and the changes take effect immediately. This allows you to adjust access controls as your application requirements evolve.
{{% /notice %}}

{{% notice warning %}}
**Warning:** Security groups are stateful — if you allow inbound traffic on a specific port, the corresponding outbound response traffic is automatically allowed, regardless of outbound rules.
{{% /notice %}}

---

### 6. Create RDS Security Group

**Creating a Security Group for Amazon RDS**

{{% notice info %}}
**Information:** Security groups act as virtual firewalls for your Amazon RDS instances, controlling inbound and outbound traffic at the instance level. Each security group contains a set of rules that filter traffic based on protocol, port, and source or destination.
{{% /notice %}}

Follow these steps to create a dedicated security group for your Amazon RDS database instance:

1. Navigate to the Amazon VPC console and select **Security Groups** from the navigation pane.

2. Click **Create Security Group** to create a new security group specifically for your RDS database instance.

3. In the **Basic details** section:
   - Enter a descriptive **Security group name** (e.g., "RDS-MySQL-SG")
   - Provide a meaningful **Description** (e.g., "Security group for RDS MySQL database instances")
   - Select your **VPC** from the dropdown menu
   ![Create a Security Group](/images/1-Worklog/Worklog_week1.4/RDS%20security%20group.png)

4. Ensure the VPC you created earlier is selected to associate the security group with your network environment.

5. Configure **Inbound rules** to control which traffic sources can access your database:
   - Select **MySQL/Aurora** from the Type dropdown (automatically sets port 3306)
   - For Source, select the security group ID of your EC2 instances that need to connect to the database

   {{% notice warning %}}
   **Security Note:** Specifying the EC2 security group as the source rather than an IP range ensures only instances with that security group can connect to your database, enhancing security.
   {{% /notice %}}

   ![Configure Inbound Rules](/images/1-Worklog/Worklog_week1.4/RDS%20security%20group%201.png)

6. Review your settings and click **Create Security Group** to complete the process.
   ![Create the Security Group](/images/1-Worklog/Worklog_week1.4/RDS%20security%20group%202.png)

{{% notice tip %}}
**Pro Tip:** You can modify security group rules at any time, and the changes take effect immediately. This allows you to adjust access controls as your application requirements evolve.
{{% /notice %}}

{{% notice warning %}}
**Warning:** It is a best practice to use separate security groups for your RDS instances and EC2 instances. This separation provides better security isolation and makes it easier to manage permissions for each resource type independently.
{{% /notice %}}

![Security Group Created](/images/1-Worklog/Worklog_week1.4/RDS%20security%20group%203.png)

---

### 7. Create DB Subnet Group

**Creating a DB Subnet Group for Amazon RDS**

{{% notice info %}}
**Information:** A DB subnet group is a collection of subnets that you designate for your Amazon RDS database instances within a VPC. DB subnet groups enable you to specify particular subnets and IP ranges where Amazon RDS can deploy database instances, ensuring proper network isolation and availability.
{{% /notice %}}

Follow these steps to create a DB subnet group:

1. Navigate to the AWS Management Console and sign in to your account.

2. Search for and select **RDS** under services.

3. In the navigation pane, select **Subnet groups**.

4. Click **Create DB Subnet Group**.
   ![Create DB Subnet Group](/images/1-Worklog/Worklog_week1.4/Create%20DB%20subnet%20group.png)

5. In the Create DB Subnet Group page, configure the basic details:
   - Enter a descriptive **Name** for your subnet group (e.g., "rds-subnet-group")
   - Provide a meaningful **Description** (e.g., "Subnet group for RDS instances")
   - Select the **VPC** you created earlier from the dropdown menu
   ![Configure DB Subnet Group Details](/images/1-Worklog/Worklog_week1.4/Create%20DB%20subnet%20group%201.png)

6. In the **Add subnets** section:
   - Select at least two different **Availability Zones** to enable Multi-AZ deployments
   - Choose the appropriate **Subnets** from each Availability Zone (typically private subnets for production databases)

   {{% notice warning %}}
   **Security Note:** For enhanced security, place your RDS instances in private subnets that don't have direct internet access.
   {{% /notice %}}

7. Click **Create** to create your DB subnet group.
   ![Add Subnets to DB Subnet Group](/images/1-Worklog/Worklog_week1.4/Create%20DB%20subnet%20group%202.png)

{{% notice warning %}}
**Warning:** A DB subnet group must include subnets in at least two different Availability Zones to support Multi-AZ deployments. Without this configuration, you won't be able to enable the Multi-AZ feature for your RDS instances.
{{% /notice %}}

{{% notice tip %}}
**Pro Tip:** If you've enabled AWS Local Zones in your account, you can also select an Availability Zone group on the Create DB Subnet Group page. In this case, select the Availability Zone group, the corresponding Availability Zones, and appropriate subnets.
{{% /notice %}}

After creation, your new DB subnet group will appear in the list of DB subnet groups in the RDS console. You can select it to view detailed information, including all associated subnets, in the details panel at the bottom of the window.

![DB Subnet Group Created](/images/1-Worklog/Worklog_week1.4/Create%20DB%20subnet%20group%203.png)

---

### 8. Create EC2 Instance

**Creating an EC2 Instance**

{{% notice info %}}
**Information:** Amazon EC2 (Elastic Compute Cloud) provides scalable computing capacity in the AWS Cloud, eliminating the need to invest in hardware upfront.
{{% /notice %}}

To create a Linux EC2 instance using the AWS Management Console, follow these instructions. This guide helps you quickly launch your first instance with essential configurations. For advanced options, refer to the Launch Instance documentation.

**Access the AWS Console**
1. Open a web browser and navigate to the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

**Launch Your Instance**
2. On the EC2 console dashboard, locate the **Launch instance** box, select **Launch instance**, then choose **Launch instance** from the dropdown menu.
   ![Launch Instance](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance.png)

**Configure Instance Details**
3. Under the **Name and tags** section, enter a descriptive name for your instance.
   ![Name and Tags](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%201.png)

4. Under **Application and OS Images (Amazon Machine Image)**, configure the following:
   - Select **Quick Start**, then choose **Amazon Linux**
   - From the Amazon Machine Image (AMI) options, select an **HVM version of Amazon Linux 2023**

   {{% notice tip %}}
   **Pro Tip:** Look for AMIs marked as Free tier eligible to avoid unexpected charges if you're using the AWS Free Tier.
   {{% /notice %}}

   ![AMI Selection](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%202.png)

5. Under **Instance type**, select **t2.micro** (pre-selected by default).

   {{% notice info %}}
   **Information:** The t2.micro instance type qualifies for the AWS Free Tier. In regions where t2.micro isn't available, you can use t3.micro under the Free Tier. For more details, see AWS Free Tier.
   {{% /notice %}}

   ![Instance Type](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%203.png)

6. Under **Key pair (login)**, select the key pair you created during your AWS setup.

   {{% notice warning %}}
   **Warning:** Do not select Proceed without a key pair (Not recommended). Without a key pair, you won't be able to connect to your instance.
   {{% /notice %}}

   ![Key Pair](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%204.png)

7. Under **Network settings**, click **Edit** and configure your security group:
   - You can use the auto-created security group, or
   - Select **Select existing security group** and choose a security group you created previously

   {{% notice warning %}}
   **Security Note:** Security groups act as virtual firewalls that control inbound and outbound traffic to your instance. Ensure your security group allows SSH access (port 22) from your IP address only.
   {{% /notice %}}

   ![Network Settings](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%205.png)

**Launch and Verify Your Instance**
8. Review the instance configuration summary in the Summary panel. When ready, click **Launch instance**.
   ![Review and Launch](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%206.png)

9. On the confirmation page, click **View all instances** to return to the EC2 console.

10. Monitor the instance status on the Instances screen:
    - Initial state: **pending**
    - Running state: **running** (with assigned public DNS name)

    {{% notice tip %}}
    **Pro Tip:** If the Public IPv4 DNS column is hidden, click the gear icon (Settings) in the upper right corner, enable Public IPv4 DNS, and click Confirm.
    {{% /notice %}}

    Wait for the instance to pass all status checks before attempting to connect.
    ![Instance Status](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%207.png)

---

### 9. Connect to Your EC2 Instance via SSH Using MobaXterm

{{% notice info %}}
**Information:** MobaXterm is an enhanced terminal for Windows with an X11 server, tabbed SSH client, and various network tools.
{{% /notice %}}

Follow these steps to connect to your EC2 instance using MobaXterm:

**Install MobaXterm**
1. Download MobaXterm from the official website: [MobaXterm Website](https://mobaxterm.mobatek.net/)
2. Install the application on your computer

**Configure SSH Connection**
3. Launch MobaXterm
4. Click the **Session** icon in the upper-left corner
5. In the configuration window, enter:
   - **Remote Host:** Your EC2 instance's public IP address or DNS name
   - **Port:** 22 (default SSH port)
   - **Username:** The default user for your AMI (typically ec2-user for Amazon Linux)
   - **Advanced SSH settings:** Browse and select your private key file (.pem)

   ![MobaXterm Configuration](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%208.png)

**Connect to Your Instance**
6. Click **OK** to save the configuration
7. Click the connect icon to establish an SSH connection

{{% notice warning %}}
**Security Note:** Ensure your private key file (.pem) has restricted permissions. On Windows, verify the file is not accessible to other users.
{{% /notice %}}

**Successful Connection**
Once connected, you'll have terminal access to your EC2 instance and can begin managing your server.
![Successful Connection](/images/1-Worklog/Worklog_week1.4/Create%20EC2%20instance%209.png)

---

### 10. Install Git on Amazon EC2 2023

Below are instructions for installing Git on an Amazon EC2 virtual machine running Amazon Linux 2023 using basic steps.

**Update System Packages**
First, update your system packages to make sure you're using the latest version:
```bash
sudo dnf update -y
```

**Find Git Packages**
Use the following command to find Git packages in the repository:
```bash
sudo dnf search git
```

**Install Git**
Once you find the Git package, you can install it with the following command:
```bash
sudo dnf install git -y
```

**Verify Git Settings**
Finally, check the Git version was successfully installed:
```bash
git --version
```
If you see the Git version appear, it means the installation is complete.

![Verify Git Installation](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance.png)

---

### 11. Install Node.js on Amazon EC2 Linux 2023

Below is a Bash script to install Node.js on Amazon EC2 Linux:

```bash
#!/bin/bash

# Color for formatting
GREEN='\033[0;32m'
NC='\033[0m' # Colorless

# Check if NVM is installed
if ! command -v nvm &> /dev/null; then
  # Step 1: Install nvm
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
  source ~/.nvm/nvm.sh
fi

# Verify nvm installation
nvm --version

# Install the LTS version of Node.js
nvm install --lts

# Use the installed LTS version
nvm use --lts

# Verify Node.js and npm installation
node -v
npm -v

# Step 4: Create package.json file (if it doesn't exist yet)
if [ ! -f package.json ]; then
  npm init -y
  echo -e "${GREEN}Created file package.json.${NC}"
fi

# Step 5: Install necessary npm packages
echo -e "Installing required npm packages..."
npm install express dotenv express-handlebars body-parser mysql

# Step 6: Install nodemon as a development dependency
echo -e "Installing nodemon as a development dependency..."
npm install --save-dev nodemon
npm install -g nodemon

# Step 7: Add npm start script to package.json
if ! grep -q '"start":' package.json; then
  npm set-script start "index.js" # Replace "your-app.js" with your entry point file
  echo -e "${GREEN}Added npm start script to package.json.${NC}"
fi

echo -e "${GREEN}Installation completed. You can now start building and running your Node.js application using 'npm start'.${NC}"
```

![Node.js Installation Output](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%201.png)

---

### 12. Creating a DB Instance on AWS

To create a DB Instance on AWS, you can use the AWS Management Console with the option of Easy create either enabled or disabled. When Easy create is enabled, you only need to specify the DB engine type, DB Instance size, and DB Instance identifier. Easy create uses default settings for other configuration options. When Easy create is disabled, you need to specify more configuration options when creating a database, including options for availability, security, backups, and maintenance.

*Note: In the procedure below, the Standard create option is enabled, and Easy create is not. This procedure uses MySQL as an example.*

To create a DB Instance:

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).
2. In the upper right corner of the Amazon RDS console, select the AWS region where you want to create the DB Instance.
3. In the navigation pane, choose **Databases**.
4. Choose **Create database**, and then select **Standard create**.
   ![Standard Create](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%202.png)

5. For **Engine type**, choose MariaDB, Microsoft SQL Server, MySQL, Oracle, or PostgreSQL. In this example, we are using Microsoft SQL Server.
6. For **Database management type**, if you are using Oracle or SQL Server, select Amazon RDS or Amazon RDS Custom.
7. For **Edition**, if you are using Oracle or SQL Server, select the version of the DB engine you want to use.
8. For **Version**, select the engine version.
   ![Select Version](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%203.png)

9. In the **Templates** section, choose a template that matches your use case. If you choose **Production**, the following options will be pre-selected in the next step:
   - Multi-AZ failover option
   - Provisioned IOPS SSD (io1) storage option
   - Protection against deletion option
   We recommend using these features for a production environment.

10. To enter your master password, follow these steps:
    - In the **Settings** section, open Credential Settings.
    - If you want to specify a password, uncheck the **Auto generate a password** box if it's already selected.
    - (Optional) Change the **Master username** value.
    - Enter the same password in both **Master password** and **Confirm password**.
    - (Optional) Set up a connection to a compute resource for this DB Instance.
    ![Setup Connection](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%204.png)

11. You can configure the connection between an Amazon EC2 instance and the new DB Instance during the DB Instance creation process. 
12. In the Connectivity section under **VPC security group (firewall)**, if you choose **Create new**, a VPC security group with a login rule allowing your local computer's IP address to access the database will be created.
    ![VPC Security Group](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%205.png)

13. For the remaining sections, specify your DB Instance settings.
14. Choose **Create database**.
    ![Create Database Button](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%206.png)

15. If you choose to use an automatically generated password, the **View credential details** button will appear on the Databases page. To view the master username and password for the DB Instance, select View credential details.
16. Under **Databases**, select the name of the new DB Instance.
    ![Select DB Instance](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%207.png)

17. On the RDS console, information about the new DB Instance will appear. The DB Instance will have a **Creating** status until it is created and ready for use. Once the status changes to **Available**, you can connect to the DB Instance.
    ![DB Instance Available](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%208.png)

---

### 13. Check RDS

In the details page of the RDS instance, you can find connection-related information such as Endpoint, Port, and Username.
The Endpoint is the URL or IP address you use to connect to the RDS database.
![Check RDS Details](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%209.png)

---

### 14. Viewing Logs and Events on AWS RDS

To monitor Logs and Events on Amazon RDS, you can follow these steps:
1. Sign in to the AWS Management Console.
2. Choose the **Amazon RDS** service from the AWS dashboard.
3. Select the RDS instance you want to view Logs and Events for.
4. In the instance details page, click on the **Logs & events** tab.

Here, you can view various logs such as:
- **Error log:** Records errors that occur on the instance.
- **General log:** Records general activities on the instance.
- **Slow query log:** Records slow queries.
- **Event log:** Displays important events related to the instance.

You can customize settings for viewing Logs and Events here, such as the time range you want to view logs or setting up email notifications for important events.
![View Logs and Events](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%2010.png)

---

### 15. Viewing Maintenance and Backups on AWS RDS

**Viewing Maintenance Information**
To view information about maintenance for a DB instance in RDS:
1. In the DB instance management page, navigate to the **Maintenance & backups** tab.
2. Here, you will see information about the maintenance schedule, including the times when the DB instance will be automatically backed up and maintenance tasks will be performed.

**Viewing Backup Information**
1. Navigate to the **Maintenance & backups** tab.
2. Here, you can view information about automatic backups and manual backups. You can also configure and manage backup settings.

![Maintenance and Backups](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%2011.png)


---

### 16. Application Deployment

**Deploy the Application**
To clone the repository from GitHub of AWS-First-Cloud-Journey, you can use the following command:
```bash
git clone https://github.com/AWS-First-Cloud-Journey/AWS-FCJ-Management
```
![Clone Repository](/images/1-Worklog/Worklog_week1.4/Application%20Deployment.png)

**Instructions for installing Node.js on Amazon Linux 2023**
Below is a Bash script to install Node.js on Amazon Linux. Please copy and execute the following steps:
```bash
#!/bin/bash

# Colors for formatting
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Check if NVM is installed
if ! command -v nvm &> /dev/null; then
  # Step 1: Install nvm
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
  source ~/.nvm/nvm.sh
fi

# Verify nvm installation
nvm --version

# Install the LTS version of Node.js
nvm install --lts

# Use the installed LTS version
nvm use --lts

# Verify Node.js and npm installation
node -v
npm -v

# Step 4: Create package.json file (if it doesn't exist yet)
if [ ! -f package.json ]; then
  npm init -y
  echo -e "${GREEN}Created file package.json.${NC}"
fi

# Step 5: Install necessary npm packages
echo -e "Installing required npm packages..."
npm install express dotenv express-handlebars body-parser mysql

# Step 6: Install nodemon as a development dependency
echo -e "Installing nodemon as a development dependency..."
npm install --save-dev nodemon
npm install -g nodemon

# Step 7: Add npm start script to package.json
if ! grep -q '"start":' package.json; then
  npm set-script start "index.js"  # Replace "your-app.js" with your entry point file
  echo -e "${GREEN}Added npm start script to package.json.${NC}"
fi

echo -e "${GREEN}Installation completed. You can now start building and running your Node.js application using 'npm start'.${NC}"
```
![Install Node.js](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%201.png)

**Install and Configure MySQL Server**
This is a Bash script used to install and configure MySQL server on a system. This script performs the following steps:
- Set variables with MySQL RPM path and database information such as RDS address, database name, username and password.
- Check if the MySQL community repository RPM already exists in the current directory. If it does not exist, it will download the RPM from the specified URL.
- Install RPM of MySQL community repository and MySQL Server.
- Start the MySQL server and configure it to automatically start with the system.
- Check the installed MySQL version.
- Secure the MySQL server with the `mysql_secure_installation` command.
- Create or update an `.env` file with database information (address, database name, username, and password).
- Connect to MySQL server with credentials and you can add specific SQL commands here.

*Note: To execute this script, you need to have sudo permissions and make sure you have provided the correct database information (RDS Endpoint, database name, username and password) before run script.*

```bash
#!/bin/bash

# Set variables for MySQL RPM and database information
MYSQL_RPM_URL="https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm"
DB_HOST="RDS Endpoint"
DB_NAME="Database name"
DB_USER="Database username"
DB_PASS="Database password"


# Check if MySQL Community repository RPM already exists
if [ ! -f mysql80-community-release-el9-1.noarch.rpm ]; then
  sudo wget $MYSQL_RPM_URL
fi

# Install MySQL Community repository
sudo dnf install -y mysql80-community-release-el9-1.noarch.rpm

# Install MySQL server
sudo dnf install -y mysql-community-server

# Start MySQL server
sudo systemctl start mysqld

# Enable MySQL to start on boot
sudo systemctl enable mysqld

# Check MySQL version
mysql -V

# Secure the MySQL server
sudo mysql_secure_installation

# Create or update the .env file with database information
echo "DB_HOST=$DB_HOST" >> .env
echo "DB_NAME=$DB_NAME" >> .env
echo "DB_USER=$DB_USER" >> .env
echo "DB_PASS=$DB_PASS" >> .env

# Connect to MySQL and create a new database (you might want to add specific SQL commands here)
mysql -h $DB_HOST -P 3306 -u $DB_USER -p$DB_PASS
```
![Install MySQL](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%202.png)

**Create Database and Table in AWS RDS**
After successfully connecting to RDS (Relational Database Service) on AWS, we can create a new database and define a table in it using the following SQL script.

**Create Database**
First, we will create a new database if it does not exist yet. Use the following command:
```sql
CREATE DATABASE IF NOT EXISTS first_cloud_users;
```
This command checks whether the database “first_cloud_users” exists or not. If it does not exist, it will create a new database named “first_cloud_users”.

**Using Database**
Next, we use the “first_cloud_users” database using the command:
```sql
USE first_cloud_users;
```
This command indicates that all SQL commands will then be executed in the “first_cloud_users” database.

**Create Table “user”**
We have created the database and used it. Now, we will define a “user” table in this database using the following SQL script:
```sql
CREATE TABLE `user`
(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `first_name` VARCHAR(45) NOT NULL,
    `last_name` VARCHAR(45) NOT NULL,
    `email` VARCHAR(100) NOT NULL UNIQUE,
    `phone` VARCHAR(15) NOT NULL,
    `comments` TEXT NOT NULL,
    `status` ENUM('active', 'inactive') NOT NULL DEFAULT 'active'
) ENGINE = InnoDB;
```
This command defines the structure of the “user” table with columns such as “id”, “first_name”, “last_name”, “email”, “phone”, “comments”, and “status”. These columns represent information about the user, and the “id” column is set as the auto-incrementing primary key.

**Add Data to Table “user”**
Finally, we can add data to the “user” table using the `INSERT INTO` command. Here is an example that adds some records to a table:
```sql
INSERT INTO `user`
(`first_name`, `last_name`, `email`, `phone`, `comments`, `status`)
VALUES
('Amanda', 'Nunes', 'anunes@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Alexander', 'Volkanovski', 'avolkanovski@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Khabib', 'Nurmagomedov', 'knurmagomedov@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Kamaru', 'Usman', 'kusman@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Israel', 'Adesanya', 'iadesanya@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Henry', 'Cejudo', 'hcejudo@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Valentina', 'Shevchenko', 'vshevchenko@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Tyron', 'Woodley', 'twoodley@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Rose', 'Namajunas', 'rnamajunas@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Tony', 'Ferguson', 'tferguson@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Jorge', 'Masvidal', 'jmasvidal@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Nate', 'Diaz', 'ndiaz@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Conor', 'McGregor', 'cmcGregor@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Cris', 'Cyborg', 'ccyborg@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Tecia', 'Torres', 'ttorres@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Ronda', 'Rousey', 'rrousey@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Holly', 'Holm', 'hholm@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Joanna', 'Jedrzejczyk', 'jjedrzejczyk@ufc.com', '012345 678910', 'I love AWS FCJ', 'active');
```
This command adds user records to the “user” table with information such as name, email, phone number, comments, and a default status of “active”.

Here are some SQL commands to check database information in a DBMS such as MySQL or PostgreSQL:

**Display a list of all databases:**
```sql
SHOW DATABASES;
```

**Choose a specific database to work with:**
```sql
USE database_name;
```

**Display tables in the current database:**
```sql
SHOW TABLES;
```

**Shows the structure of a specific table:**
```sql
DESCRIBE table_name;
```

**Display information about database size:**
```sql
SELECT table_schema "Database Name", SUM(data_length + index_length) / 1024 / 1024 "Database Size (MB)"
FROM information_schema.tables
GROUP BY table_schema;
```
Remember to replace “database_name” and “table_name” with the specific names of the database and table you want to test.
![SQL Commands](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%203.png)

**Run the Application**
Once you are in the application directory, run the following command to start the application using npm start:
```bash
npm start
```
![npm start](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%204.png)

**Test the application in the browser:**
Check EC2 Instance status: Make sure your EC2 Instance is running and functioning properly.
Open a web browser and enter the IP address or domain name of the EC2 Instance, followed by port 5000:
`http://<IP address or domain name>:5000`

Test results: The browser will display your application if everything is configured correctly and the EC2 Instance is working.
![Browser Test](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%205.png)

---

### 17. Monitoring and Restoring AWS RDS

**Monitoring AWS RDS**
On the AWS RDS interface, you can perform the following steps to monitor:
1. Select **Databases**.
2. Choose the DB instance you’ve created.
3. Select **Monitoring**.
![Monitoring RDS](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%206.png)

**Viewing Backup Information**
To view information about backups of the DB instance in AWS RDS, follow these steps:
1. Log in to the AWS Management Console.
2. Select the **Amazon RDS** service from the list of services.
3. In the RDS dashboard, choose the DB instance you want to check.
4. On the DB instance management page, navigate to the **Maintenance & backups** tab.
Here, you can view information about automatic and manual backups. You can also configure and manage backup settings.
![Backups](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%207.png)

**View Snapshot Information**
![Snapshot](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%208.png)

**Restore Snapshot**
Choose the DB snapshot you want to restore. In the Actions section, select **Restore snapshot**.
![Restore Snapshot](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%209.png)

On the Restore snapshot page, enter a name for the DB instance you want to restore in the DB instance identifier field. Select other settings such as allocated memory size.
Finally, select **Restore DB instance**.
![Restore Settings](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%2010.png)

Complete the restore snapshot process and check the restored database instance.
![Restore Complete](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%2011.png)


---

### 18. Backup and Restore

**Understanding Amazon RDS Backup and Restore**

{{% notice info %}}
**Information:** Amazon RDS provides automated backups and allows manual snapshots to ensure your database data is protected and can be recovered when needed. These capabilities are essential for disaster recovery planning and maintaining business continuity.
{{% /notice %}}

**Monitoring Backup Status in Amazon RDS**
To access backup monitoring in the Amazon RDS console:
1. Navigate to the Databases section in the AWS Management Console
2. Select your target DB instance
3. Click on the **Monitoring** tab to view performance metrics
![AWS RDS Monitoring](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore.png)

**Viewing Backup Information**
To review backup details for your Amazon RDS instance:
1. Sign in to the AWS Management Console
2. Select Amazon RDS from the services menu
3. In the RDS dashboard, select your DB instance
4. Navigate to the **Maintenance & backups** tab
Here you can view both automated and manual backup information and configure backup settings.
![AWS RDS Backup](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore%201.png)

**Managing Database Snapshots**
View your available DB snapshots in the snapshots section:
![Snapshot Information](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore%202.png)

**Restoring from a DB Snapshot**
Select the DB snapshot you want to use as your restore point:
1. Under the Actions dropdown menu, select **Restore snapshot**
![Restore Snapshot](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore%203.png)

**Configure your restored database instance:**
1. Provide a unique DB instance identifier for the new instance
2. Select appropriate instance specifications (compute, storage, etc.)
3. Configure network and security settings

{{% notice tip %}}
**Pro Tip:** When restoring a production database, consider restoring to a smaller instance class first for testing, then scale up as needed to minimize costs during validation.
{{% /notice %}}

**Initiate the restore process:**
1. Review your configuration settings
2. Click **Restore DB instance** to begin the process

{{% notice warning %}}
**Warning:** The restore process creates a completely new database instance with its own endpoint. You will need to update your application connection strings to point to this new instance if you intend to use it for production.
{{% /notice %}}

**Verifying the Restored Database**
Confirm successful restoration:
1. Check that the new DB instance appears in your RDS console
2. Verify the status shows as "Available" when the restore completes
3. Test connectivity and data integrity before directing production traffic to the restored instance

{{% notice warning %}}
**Security Note:** Remember to configure the same security groups and parameter groups as your original instance if you want identical access controls and database settings.
{{% /notice %}}


---

### 19. Clean up resources

**Resource Cleanup**

{{% notice info %}}
**Information:** After completing your lab, it's important to clean up all AWS resources to avoid ongoing charges. Follow these steps to properly remove all resources created during this workshop.
{{% /notice %}}

**Delete Database Resources**

**Delete the DB subnet group:**
1. Navigate to the Amazon RDS console
2. In the navigation pane, select **Subnet groups**
3. Select the DB subnet group related to the lab
4. Choose **Delete**, then confirm by selecting Delete in the confirmation window
![Delete DB Subnet Group](/images/1-Worklog/Worklog_week1.4/Clean.png)

**Delete DB Instance:**
1. Access the RDS Management Console
2. In the left navigation bar, select **Databases**
3. Select the DB Instance related to the lab
4. Click Actions, then **Delete**
![Delete DB Instance](/images/1-Worklog/Worklog_week1.4/Clean1.png)

5. Uncheck *Create final snapshot?* and acknowledge that automated backups will no longer be available
6. Enter `delete me` in the confirmation field
7. Click **Delete**
![Confirm Delete DB Instance](/images/1-Worklog/Worklog_week1.4/Clean2.png)

**Delete DB Snapshots:**
1. In the RDS Management Console, select **Snapshots** from the navigation bar
2. Select all snapshots related to the lab
3. Click Actions, then **Delete snapshot**
4. Confirm by clicking **Delete**
![Delete DB Snapshots](/images/1-Worklog/Worklog_week1.4/Clean3.png)

**Delete Network Resources**

**Delete security groups:**
1. Open the Amazon VPC console
2. Choose **Security Groups** from the navigation pane
3. Select the security group related to the lab
4. Choose Actions, select **Delete security groups**, then confirm
![Delete Security Groups](/images/1-Worklog/Worklog_week1.4/Clean4.png)

**Delete NAT gateway:**
1. In the VPC console, select **NAT Gateways**
2. Select the NAT Gateway related to the lab
3. Choose Actions, select **Delete NAT gateway**
4. Confirm the deletion
![Delete NAT Gateway](/images/1-Worklog/Worklog_week1.4/Clean5.png)

**Release Elastic IP addresses:**
1. Open the Amazon EC2 console
2. Select **Elastic IPs** from the navigation pane
3. Select the Elastic IP address related to the lab
4. From Actions, select **Release Elastic IP addresses**
5. Confirm by choosing **Release**
![Release Elastic IP](/images/1-Worklog/Worklog_week1.4/Clean6.png)

**Delete the VPC:**
1. In the VPC console, select **Your VPCs**
2. Select the VPC you created for this lab
3. From Actions, select **Delete VPC**
4. On the confirmation page, enter `delete` and choose **Delete**
![Delete VPC](/images/1-Worklog/Worklog_week1.4/Clean7.png)

**Delete Compute Resources**

**Terminate EC2 instances:**
1. Access the EC2 Management Console
2. Select **Instances** from the navigation pane
3. Select all EC2 Instances related to the lab
4. Click Instance state, then **Terminate instance**
5. Confirm by clicking **Terminate**
![Terminate EC2 Instances](/images/1-Worklog/Worklog_week1.4/Clean8.png)

{{% notice warning %}}
**Warning:** Terminating resources is permanent and cannot be undone. Ensure you have backed up any important data before proceeding with cleanup.
{{% /notice %}}

{{% notice tip %}}
**Pro Tip:** To verify all resources have been properly deleted, check your AWS Billing dashboard or use AWS Cost Explorer to ensure no unexpected charges appear after cleanup.
{{% /notice %}}


---

### 10. Install Git on Amazon EC2 2023

Below are instructions for installing Git on an Amazon EC2 virtual machine running Amazon Linux 2023 using basic steps.

**Update System Packages**
First, update your system packages to make sure you're using the latest version:
```bash
sudo dnf update -y
```

**Find Git Packages**
Use the following command to find Git packages in the repository:
```bash
sudo dnf search git
```

**Install Git**
Once you find the Git package, you can install it with the following command:
```bash
sudo dnf install git -y
```

**Verify Git Settings**
Finally, check the Git version was successfully installed:
```bash
git --version
```
If you see the Git version appear, it means the installation is complete.

![Verify Git Installation](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance.png)

---

### 11. Install Node.js on Amazon EC2 Linux 2023

Below is a Bash script to install Node.js on Amazon EC2 Linux:

```bash
#!/bin/bash

# Color for formatting
GREEN='\033[0;32m'
NC='\033[0m' # Colorless

# Check if NVM is installed
if ! command -v nvm &> /dev/null; then
  # Step 1: Install nvm
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
  source ~/.nvm/nvm.sh
fi

# Verify nvm installation
nvm --version

# Install the LTS version of Node.js
nvm install --lts

# Use the installed LTS version
nvm use --lts

# Verify Node.js and npm installation
node -v
npm -v

# Step 4: Create package.json file (if it doesn't exist yet)
if [ ! -f package.json ]; then
  npm init -y
  echo -e "${GREEN}Created file package.json.${NC}"
fi

# Step 5: Install necessary npm packages
echo -e "Installing required npm packages..."
npm install express dotenv express-handlebars body-parser mysql

# Step 6: Install nodemon as a development dependency
echo -e "Installing nodemon as a development dependency..."
npm install --save-dev nodemon
npm install -g nodemon

# Step 7: Add npm start script to package.json
if ! grep -q '"start":' package.json; then
  npm set-script start "index.js" # Replace "your-app.js" with your entry point file
  echo -e "${GREEN}Added npm start script to package.json.${NC}"
fi

echo -e "${GREEN}Installation completed. You can now start building and running your Node.js application using 'npm start'.${NC}"
```

![Node.js Installation Output](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%201.png)

---

### 12. Creating a DB Instance on AWS

To create a DB Instance on AWS, you can use the AWS Management Console with the option of Easy create either enabled or disabled. When Easy create is enabled, you only need to specify the DB engine type, DB Instance size, and DB Instance identifier. Easy create uses default settings for other configuration options. When Easy create is disabled, you need to specify more configuration options when creating a database, including options for availability, security, backups, and maintenance.

*Note: In the procedure below, the Standard create option is enabled, and Easy create is not. This procedure uses MySQL as an example.*

To create a DB Instance:

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).
2. In the upper right corner of the Amazon RDS console, select the AWS region where you want to create the DB Instance.
3. In the navigation pane, choose **Databases**.
4. Choose **Create database**, and then select **Standard create**.
   ![Standard Create](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%202.png)

5. For **Engine type**, choose MariaDB, Microsoft SQL Server, MySQL, Oracle, or PostgreSQL. In this example, we are using Microsoft SQL Server.
6. For **Database management type**, if you are using Oracle or SQL Server, select Amazon RDS or Amazon RDS Custom.
7. For **Edition**, if you are using Oracle or SQL Server, select the version of the DB engine you want to use.
8. For **Version**, select the engine version.
   ![Select Version](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%203.png)

9. In the **Templates** section, choose a template that matches your use case. If you choose **Production**, the following options will be pre-selected in the next step:
   - Multi-AZ failover option
   - Provisioned IOPS SSD (io1) storage option
   - Protection against deletion option
   We recommend using these features for a production environment.

10. To enter your master password, follow these steps:
    - In the **Settings** section, open Credential Settings.
    - If you want to specify a password, uncheck the **Auto generate a password** box if it's already selected.
    - (Optional) Change the **Master username** value.
    - Enter the same password in both **Master password** and **Confirm password**.
    - (Optional) Set up a connection to a compute resource for this DB Instance.
    ![Setup Connection](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%204.png)

11. You can configure the connection between an Amazon EC2 instance and the new DB Instance during the DB Instance creation process. 
12. In the Connectivity section under **VPC security group (firewall)**, if you choose **Create new**, a VPC security group with a login rule allowing your local computer's IP address to access the database will be created.
    ![VPC Security Group](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%205.png)

13. For the remaining sections, specify your DB Instance settings.
14. Choose **Create database**.
    ![Create Database Button](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%206.png)

15. If you choose to use an automatically generated password, the **View credential details** button will appear on the Databases page. To view the master username and password for the DB Instance, select View credential details.
16. Under **Databases**, select the name of the new DB Instance.
    ![Select DB Instance](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%207.png)

17. On the RDS console, information about the new DB Instance will appear. The DB Instance will have a **Creating** status until it is created and ready for use. Once the status changes to **Available**, you can connect to the DB Instance.
    ![DB Instance Available](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%208.png)

---

### 13. Check RDS

In the details page of the RDS instance, you can find connection-related information such as Endpoint, Port, and Username.
The Endpoint is the URL or IP address you use to connect to the RDS database.
![Check RDS Details](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%209.png)

---

### 14. Viewing Logs and Events on AWS RDS

To monitor Logs and Events on Amazon RDS, you can follow these steps:
1. Sign in to the AWS Management Console.
2. Choose the **Amazon RDS** service from the AWS dashboard.
3. Select the RDS instance you want to view Logs and Events for.
4. In the instance details page, click on the **Logs & events** tab.

Here, you can view various logs such as:
- **Error log:** Records errors that occur on the instance.
- **General log:** Records general activities on the instance.
- **Slow query log:** Records slow queries.
- **Event log:** Displays important events related to the instance.

You can customize settings for viewing Logs and Events here, such as the time range you want to view logs or setting up email notifications for important events.
![View Logs and Events](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%2010.png)

---

### 15. Viewing Maintenance and Backups on AWS RDS

**Viewing Maintenance Information**
To view information about maintenance for a DB instance in RDS:
1. In the DB instance management page, navigate to the **Maintenance & backups** tab.
2. Here, you will see information about the maintenance schedule, including the times when the DB instance will be automatically backed up and maintenance tasks will be performed.

**Viewing Backup Information**
1. Navigate to the **Maintenance & backups** tab.
2. Here, you can view information about automatic backups and manual backups. You can also configure and manage backup settings.

![Maintenance and Backups](/images/1-Worklog/Worklog_week1.4/Create%20RDS%20database%20instance%2011.png)


---

### 16. Application Deployment

**Deploy the Application**
To clone the repository from GitHub of AWS-First-Cloud-Journey, you can use the following command:
```bash
git clone https://github.com/AWS-First-Cloud-Journey/AWS-FCJ-Management
```
![Clone Repository](/images/1-Worklog/Worklog_week1.4/Application%20Deployment.png)

**Instructions for installing Node.js on Amazon Linux 2023**
Below is a Bash script to install Node.js on Amazon Linux. Please copy and execute the following steps:
```bash
#!/bin/bash

# Colors for formatting
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Check if NVM is installed
if ! command -v nvm &> /dev/null; then
  # Step 1: Install nvm
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
  source ~/.nvm/nvm.sh
fi

# Verify nvm installation
nvm --version

# Install the LTS version of Node.js
nvm install --lts

# Use the installed LTS version
nvm use --lts

# Verify Node.js and npm installation
node -v
npm -v

# Step 4: Create package.json file (if it doesn't exist yet)
if [ ! -f package.json ]; then
  npm init -y
  echo -e "${GREEN}Created file package.json.${NC}"
fi

# Step 5: Install necessary npm packages
echo -e "Installing required npm packages..."
npm install express dotenv express-handlebars body-parser mysql

# Step 6: Install nodemon as a development dependency
echo -e "Installing nodemon as a development dependency..."
npm install --save-dev nodemon
npm install -g nodemon

# Step 7: Add npm start script to package.json
if ! grep -q '"start":' package.json; then
  npm set-script start "index.js"  # Replace "your-app.js" with your entry point file
  echo -e "${GREEN}Added npm start script to package.json.${NC}"
fi

echo -e "${GREEN}Installation completed. You can now start building and running your Node.js application using 'npm start'.${NC}"
```
![Install Node.js](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%201.png)

**Install and Configure MySQL Server**
This is a Bash script used to install and configure MySQL server on a system. This script performs the following steps:
- Set variables with MySQL RPM path and database information such as RDS address, database name, username and password.
- Check if the MySQL community repository RPM already exists in the current directory. If it does not exist, it will download the RPM from the specified URL.
- Install RPM of MySQL community repository and MySQL Server.
- Start the MySQL server and configure it to automatically start with the system.
- Check the installed MySQL version.
- Secure the MySQL server with the `mysql_secure_installation` command.
- Create or update an `.env` file with database information (address, database name, username, and password).
- Connect to MySQL server with credentials and you can add specific SQL commands here.

*Note: To execute this script, you need to have sudo permissions and make sure you have provided the correct database information (RDS Endpoint, database name, username and password) before run script.*

```bash
#!/bin/bash

# Set variables for MySQL RPM and database information
MYSQL_RPM_URL="https://dev.mysql.com/get/mysql80-community-release-el9-1.noarch.rpm"
DB_HOST="RDS Endpoint"
DB_NAME="Database name"
DB_USER="Database username"
DB_PASS="Database password"


# Check if MySQL Community repository RPM already exists
if [ ! -f mysql80-community-release-el9-1.noarch.rpm ]; then
  sudo wget $MYSQL_RPM_URL
fi

# Install MySQL Community repository
sudo dnf install -y mysql80-community-release-el9-1.noarch.rpm

# Install MySQL server
sudo dnf install -y mysql-community-server

# Start MySQL server
sudo systemctl start mysqld

# Enable MySQL to start on boot
sudo systemctl enable mysqld

# Check MySQL version
mysql -V

# Secure the MySQL server
sudo mysql_secure_installation

# Create or update the .env file with database information
echo "DB_HOST=$DB_HOST" >> .env
echo "DB_NAME=$DB_NAME" >> .env
echo "DB_USER=$DB_USER" >> .env
echo "DB_PASS=$DB_PASS" >> .env

# Connect to MySQL and create a new database (you might want to add specific SQL commands here)
mysql -h $DB_HOST -P 3306 -u $DB_USER -p$DB_PASS
```
![Install MySQL](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%202.png)

**Create Database and Table in AWS RDS**
After successfully connecting to RDS (Relational Database Service) on AWS, we can create a new database and define a table in it using the following SQL script.

**Create Database**
First, we will create a new database if it does not exist yet. Use the following command:
```sql
CREATE DATABASE IF NOT EXISTS first_cloud_users;
```
This command checks whether the database “first_cloud_users” exists or not. If it does not exist, it will create a new database named “first_cloud_users”.

**Using Database**
Next, we use the “first_cloud_users” database using the command:
```sql
USE first_cloud_users;
```
This command indicates that all SQL commands will then be executed in the “first_cloud_users” database.

**Create Table “user”**
We have created the database and used it. Now, we will define a “user” table in this database using the following SQL script:
```sql
CREATE TABLE `user`
(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `first_name` VARCHAR(45) NOT NULL,
    `last_name` VARCHAR(45) NOT NULL,
    `email` VARCHAR(100) NOT NULL UNIQUE,
    `phone` VARCHAR(15) NOT NULL,
    `comments` TEXT NOT NULL,
    `status` ENUM('active', 'inactive') NOT NULL DEFAULT 'active'
) ENGINE = InnoDB;
```
This command defines the structure of the “user” table with columns such as “id”, “first_name”, “last_name”, “email”, “phone”, “comments”, and “status”. These columns represent information about the user, and the “id” column is set as the auto-incrementing primary key.

**Add Data to Table “user”**
Finally, we can add data to the “user” table using the `INSERT INTO` command. Here is an example that adds some records to a table:
```sql
INSERT INTO `user`
(`first_name`, `last_name`, `email`, `phone`, `comments`, `status`)
VALUES
('Amanda', 'Nunes', 'anunes@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Alexander', 'Volkanovski', 'avolkanovski@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Khabib', 'Nurmagomedov', 'knurmagomedov@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Kamaru', 'Usman', 'kusman@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Israel', 'Adesanya', 'iadesanya@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Henry', 'Cejudo', 'hcejudo@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Valentina', 'Shevchenko', 'vshevchenko@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Tyron', 'Woodley', 'twoodley@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Rose', 'Namajunas', 'rnamajunas@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Tony', 'Ferguson', 'tferguson@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Jorge', 'Masvidal', 'jmasvidal@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Nate', 'Diaz', 'ndiaz@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Conor', 'McGregor', 'cmcGregor@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Cris', 'Cyborg', 'ccyborg@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Tecia', 'Torres', 'ttorres@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Ronda', 'Rousey', 'rrousey@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Holly', 'Holm', 'hholm@ufc.com', '012345 678910', 'I love AWS FCJ', 'active'),
('Joanna', 'Jedrzejczyk', 'jjedrzejczyk@ufc.com', '012345 678910', 'I love AWS FCJ', 'active');
```
This command adds user records to the “user” table with information such as name, email, phone number, comments, and a default status of “active”.

Here are some SQL commands to check database information in a DBMS such as MySQL or PostgreSQL:

**Display a list of all databases:**
```sql
SHOW DATABASES;
```

**Choose a specific database to work with:**
```sql
USE database_name;
```

**Display tables in the current database:**
```sql
SHOW TABLES;
```

**Shows the structure of a specific table:**
```sql
DESCRIBE table_name;
```

**Display information about database size:**
```sql
SELECT table_schema "Database Name", SUM(data_length + index_length) / 1024 / 1024 "Database Size (MB)"
FROM information_schema.tables
GROUP BY table_schema;
```
Remember to replace “database_name” and “table_name” with the specific names of the database and table you want to test.
![SQL Commands](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%203.png)

**Run the Application**
Once you are in the application directory, run the following command to start the application using npm start:
```bash
npm start
```
![npm start](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%204.png)

**Test the application in the browser:**
Check EC2 Instance status: Make sure your EC2 Instance is running and functioning properly.
Open a web browser and enter the IP address or domain name of the EC2 Instance, followed by port 5000:
`http://<IP address or domain name>:5000`

Test results: The browser will display your application if everything is configured correctly and the EC2 Instance is working.
![Browser Test](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%205.png)

---

### 17. Monitoring and Restoring AWS RDS

**Monitoring AWS RDS**
On the AWS RDS interface, you can perform the following steps to monitor:
1. Select **Databases**.
2. Choose the DB instance you’ve created.
3. Select **Monitoring**.
![Monitoring RDS](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%206.png)

**Viewing Backup Information**
To view information about backups of the DB instance in AWS RDS, follow these steps:
1. Log in to the AWS Management Console.
2. Select the **Amazon RDS** service from the list of services.
3. In the RDS dashboard, choose the DB instance you want to check.
4. On the DB instance management page, navigate to the **Maintenance & backups** tab.
Here, you can view information about automatic and manual backups. You can also configure and manage backup settings.
![Backups](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%207.png)

**View Snapshot Information**
![Snapshot](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%208.png)

**Restore Snapshot**
Choose the DB snapshot you want to restore. In the Actions section, select **Restore snapshot**.
![Restore Snapshot](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%209.png)

On the Restore snapshot page, enter a name for the DB instance you want to restore in the DB instance identifier field. Select other settings such as allocated memory size.
Finally, select **Restore DB instance**.
![Restore Settings](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%2010.png)

Complete the restore snapshot process and check the restored database instance.
![Restore Complete](/images/1-Worklog/Worklog_week1.4/Application%20Deployment%2011.png)


---

### 18. Backup and Restore

**Understanding Amazon RDS Backup and Restore**

{{% notice info %}}
**Information:** Amazon RDS provides automated backups and allows manual snapshots to ensure your database data is protected and can be recovered when needed. These capabilities are essential for disaster recovery planning and maintaining business continuity.
{{% /notice %}}

**Monitoring Backup Status in Amazon RDS**
To access backup monitoring in the Amazon RDS console:
1. Navigate to the Databases section in the AWS Management Console
2. Select your target DB instance
3. Click on the **Monitoring** tab to view performance metrics
![AWS RDS Monitoring](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore.png)

**Viewing Backup Information**
To review backup details for your Amazon RDS instance:
1. Sign in to the AWS Management Console
2. Select Amazon RDS from the services menu
3. In the RDS dashboard, select your DB instance
4. Navigate to the **Maintenance & backups** tab
Here you can view both automated and manual backup information and configure backup settings.
![AWS RDS Backup](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore%201.png)

**Managing Database Snapshots**
View your available DB snapshots in the snapshots section:
![Snapshot Information](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore%202.png)

**Restoring from a DB Snapshot**
Select the DB snapshot you want to use as your restore point:
1. Under the Actions dropdown menu, select **Restore snapshot**
![Restore Snapshot](/images/1-Worklog/Worklog_week1.4/Backup%20and%20restore%203.png)

**Configure your restored database instance:**
1. Provide a unique DB instance identifier for the new instance
2. Select appropriate instance specifications (compute, storage, etc.)
3. Configure network and security settings

{{% notice tip %}}
**Pro Tip:** When restoring a production database, consider restoring to a smaller instance class first for testing, then scale up as needed to minimize costs during validation.
{{% /notice %}}

**Initiate the restore process:**
1. Review your configuration settings
2. Click **Restore DB instance** to begin the process

{{% notice warning %}}
**Warning:** The restore process creates a completely new database instance with its own endpoint. You will need to update your application connection strings to point to this new instance if you intend to use it for production.
{{% /notice %}}

**Verifying the Restored Database**
Confirm successful restoration:
1. Check that the new DB instance appears in your RDS console
2. Verify the status shows as "Available" when the restore completes
3. Test connectivity and data integrity before directing production traffic to the restored instance

{{% notice warning %}}
**Security Note:** Remember to configure the same security groups and parameter groups as your original instance if you want identical access controls and database settings.
{{% /notice %}}


---

### 19. Clean up resources

**Resource Cleanup**

{{% notice info %}}
**Information:** After completing your lab, it's important to clean up all AWS resources to avoid ongoing charges. Follow these steps to properly remove all resources created during this workshop.
{{% /notice %}}

**Delete Database Resources**

**Delete the DB subnet group:**
1. Navigate to the Amazon RDS console
2. In the navigation pane, select **Subnet groups**
3. Select the DB subnet group related to the lab
4. Choose **Delete**, then confirm by selecting Delete in the confirmation window
![Delete DB Subnet Group](/images/1-Worklog/Worklog_week1.4/Clean.png)

**Delete DB Instance:**
1. Access the RDS Management Console
2. In the left navigation bar, select **Databases**
3. Select the DB Instance related to the lab
4. Click Actions, then **Delete**
![Delete DB Instance](/images/1-Worklog/Worklog_week1.4/Clean1.png)

5. Uncheck *Create final snapshot?* and acknowledge that automated backups will no longer be available
6. Enter `delete me` in the confirmation field
7. Click **Delete**
![Confirm Delete DB Instance](/images/1-Worklog/Worklog_week1.4/Clean2.png)

**Delete DB Snapshots:**
1. In the RDS Management Console, select **Snapshots** from the navigation bar
2. Select all snapshots related to the lab
3. Click Actions, then **Delete snapshot**
4. Confirm by clicking **Delete**
![Delete DB Snapshots](/images/1-Worklog/Worklog_week1.4/Clean3.png)

**Delete Network Resources**

**Delete security groups:**
1. Open the Amazon VPC console
2. Choose **Security Groups** from the navigation pane
3. Select the security group related to the lab
4. Choose Actions, select **Delete security groups**, then confirm
![Delete Security Groups](/images/1-Worklog/Worklog_week1.4/Clean4.png)

**Delete NAT gateway:**
1. In the VPC console, select **NAT Gateways**
2. Select the NAT Gateway related to the lab
3. Choose Actions, select **Delete NAT gateway**
4. Confirm the deletion
![Delete NAT Gateway](/images/1-Worklog/Worklog_week1.4/Clean5.png)

**Release Elastic IP addresses:**
1. Open the Amazon EC2 console
2. Select **Elastic IPs** from the navigation pane
3. Select the Elastic IP address related to the lab
4. From Actions, select **Release Elastic IP addresses**
5. Confirm by choosing **Release**
![Release Elastic IP](/images/1-Worklog/Worklog_week1.4/Clean6.png)

**Delete the VPC:**
1. In the VPC console, select **Your VPCs**
2. Select the VPC you created for this lab
3. From Actions, select **Delete VPC**
4. On the confirmation page, enter `delete` and choose **Delete**
![Delete VPC](/images/1-Worklog/Worklog_week1.4/Clean7.png)

**Delete Compute Resources**

**Terminate EC2 instances:**
1. Access the EC2 Management Console
2. Select **Instances** from the navigation pane
3. Select all EC2 Instances related to the lab
4. Click Instance state, then **Terminate instance**
5. Confirm by clicking **Terminate**
![Terminate EC2 Instances](/images/1-Worklog/Worklog_week1.4/Clean8.png)

{{% notice warning %}}
**Warning:** Terminating resources is permanent and cannot be undone. Ensure you have backed up any important data before proceeding with cleanup.
{{% /notice %}}

{{% notice tip %}}
**Pro Tip:** To verify all resources have been properly deleted, check your AWS Billing dashboard or use AWS Cost Explorer to ensure no unexpected charges appear after cleanup.
{{% /notice %}}

