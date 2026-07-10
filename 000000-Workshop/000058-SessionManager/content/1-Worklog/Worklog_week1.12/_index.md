
---
title: "Week 12 Worklog"
date: 2026-07-06
weight: 12
chapter: false
pre: " <b> 1.12 </b> "
---

## Week 12 Objectives:
- Understand and configure IAM Tag-based Access Control for EC2 resources.
- Learn about open-source monitoring tool Grafana and how to build basic dashboards.
- Set up IAM Permissions Boundaries to delegate permissions and limit the maximum access of IAM Entities.
- Utilize AWS Systems Manager (SSM) suite to manage server infrastructure remotely, including Fleet Manager, automated OS patching via Patch Manager, and executing remote scripts via Run Command.

## Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| 2 | - Learn IAM Tag-based Access Control<br>- Read guides and configure IAM Tags for controlling access to EC2 resources | 06/07/2026 | 06/07/2026 | <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html" target="_blank">AWS IAM Tagging</a> |
| 3 | - Learn Grafana monitoring basics<br>- Read and understand Grafana concepts and set up a basic Dashboard | 07/07/2026 | 07/07/2026 | <a href="https://grafana.com/docs/grafana/latest/" target="_blank">Grafana User Guide</a> |
| 4 | - Learn IAM Permission Boundary<br>- Configure permission boundaries to limit the maximum permissions of IAM Entities | 08/07/2026 | 08/07/2026 | <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html" target="_blank">AWS Permissions Boundaries</a> |
| 5 | - Learn AWS Systems Manager (SSM) concepts<br>- Study introduction to SSM, Fleet Manager, Patch Manager, and Run Command | 09/07/2026 | 09/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html" target="_blank">AWS Systems Manager User Guide</a> |
| 6 | - Set up network infrastructure and IAM Roles for SSM<br>- Create VPC `windows-lab-ssm`, Internet Gateway, 2 Subnets<br>- Create IAM Role/Instance Profile with `AmazonSSMManagedInstanceCore` policy<br>- Launch 2 Windows Server EC2 instances attached with the IAM Role | 10/07/2026 | 10/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html" target="_blank">SSM Agent on Windows Server</a> |
| 7 - Sun | - Execute patching and remote commands via SSM<br>- Use Patch Manager to scan vulnerabilities and auto-install OS updates<br>- Use Run Command to run PowerShell `net user` remotely and store logs in S3<br>- Perform clean-up of all AWS resources to avoid any charges | 11/07/2026 | 12/07/2026 | <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html" target="_blank">SSM Patch Manager</a><br><a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html" target="_blank">SSM Run Command</a> |

## Week 12 Achievements:
