---
title: "Week 2 Worklog"
date: 2026-05-13
weight: 2
chapter: false
pre: " <b> 1.2 </b> "
---

## Week 2 Objectives:
- Understand AWS Billing and Cost Management tools.
- Master the role and configuration of AWS Budgets to monitor cloud spending.
- Practice setting budget limits and configuring automated threshold-based email alerts.

## Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn about AWS Billing & Cost Management tools:<br>  + AWS Billing Tools<br>  + Calculate basic service costs | 27/04/2026 | 27/04/2026 | [AWS Billing Overview](https://docs.aws.amazon.com/billing/latest/userguide/billing-whatis.html) |
| 3 | - Understand AWS Budgets mechanisms:<br>  + Cost budget vs. Usage budget concepts<br>  + Actual and forecasted cost alert thresholds | 28/04/2026 | 28/04/2026 | [AWS Budgets Guide](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) |
| 4 | - Plan monthly budget limits for an AWS Free Tier account to avoid unexpected charges. | 29/04/2026 | 29/04/2026 | [AWS Free Tier Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) |
| 5 | - Learn how to configure budget alerts via email and automated notification channels (Amazon SNS). | 30/04/2026 | 30/04/2026 | [AWS Budgets Alerts](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-alerts.html) |
| 6 | - **Practice (Part 1):** Initialize a monthly cost budget (`My Monthly Cost Budget`) with a $100 limit. | 01/05/2026 | 01/05/2026 | [Creating a Cost Budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create-cost.html) |
| 7 - Sun | - **Practice (Part 2):** Create a backup cost budget (`My-200$-budget`) and resource usage budget (`Cost budget`). Verify health status and alert triggers. | 02/05/2026 | 03/05/2026 | [Monitoring Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-viewing.html) |

## Week 2 Achievements:
### Theory:
- Gained a solid understanding of AWS pricing models, billing drivers, and how to use AWS Budgets as a financial safety net.
- Distinguished between Cost Budgets (financial monitoring) and Usage Budgets (resource utilization monitoring).

### Practice:
- Successfully initialized three separate budgets to monitor spending from multiple dimensions on the AWS Console.
- Configured automated email alerts when actual costs reach 80% of the limit or forecasted charges exceed the threshold.

### Evidences:

1. **AWS Budgets - Initial Budget Creation (Create budget)**
   ![Lab07 Configuration - Step 1](/images/1-Worklog/Worklog_week1.2/Module%2001-Lab07-01.png)
   *Description: Shows the Budgets Overview dashboard with two active, healthy budgets: `My Monthly Cost Budget` ($100 monthly cost tracker) and `My-200$-budget` ($200 cost tracker), indicating healthy status with no alerts triggered.*

2. **AWS Budgets - Successful Creation of Cost Budget (Add cost budget)**
   ![Lab07 Configuration - Step 2](/images/1-Worklog/Worklog_week1.2/Module%2001-Lab07-02.png)
   *Description: Banner confirming that a third budget named `Cost budget` has been successfully provisioned with a limit of $200, raising the total monitored budgets to three for detailed categorizations.*

3. **AWS Budgets - Budget Details Verification (Budget details)**
   ![Lab07 Configuration - Step 3](/images/1-Worklog/Worklog_week1.2/Module%2001-Lab07-03.png)
   *Description: Displays detailed metrics for the newly created `Cost budget`, confirming a Healthy status, usage amount of 1.440 Hrs, monthly tracking period, and a configuration start date of 2026-05-01.*
