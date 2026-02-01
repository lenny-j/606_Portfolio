# Compute Services Lab: EC2 vs Lambda Comparison

> **Author:** [Your Name]
> **Date:** [Date Completed]
> **Course:** Cloud Infrastructure Workshop - Lesson 1

---

## Objective

In this lab, I deployed the same simple web response using two different AWS compute services to understand their differences, trade-offs, and appropriate use cases.

**Business Scenario:** TechStart Inc. needs to serve a simple web page to customers. I evaluated two compute options to determine the best fit.

---

## Architecture Overview

<!-- Replace this section with your own diagram or description -->
<!-- You can use ASCII art, a screenshot from draw.io, or describe the architecture -->

```
┌─────────────────────────────────────────────────────────────────┐
│                        AWS Cloud                                │
│                                                                 │
│   ┌─────────────────────┐       ┌─────────────────────┐        │
│   │     EC2 Instance    │       │   Lambda Function   │        │
│   │    (t3.micro)       │       │   (Python 3.12)     │        │
│   │                     │       │                     │        │
│   │  ┌───────────────┐  │       │  ┌───────────────┐  │        │
│   │  │ Amazon Linux  │  │       │  │   Handler     │  │        │
│   │  │    + httpd    │  │       │  │   Function    │  │        │
│   │  └───────────────┘  │       │  └───────────────┘  │        │
│   │                     │       │                     │        │
│   │  Public IP: X.X.X.X │       │  No static IP       │        │
│   └─────────────────────┘       └─────────────────────┘        │
│            │                              │                     │
│            ▼                              ▼                     │
│     HTTP Response                  Test Invocation              │
│     (Always On)                    (On-Demand)                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Deployment Evidence

### EC2 Instance

**Instance Details:**
| Attribute | Value |
|-----------|-------|
| Instance ID | `i-xxxxxxxxxx` |
| Instance Type | t3.micro |
| vCPUs | [Fill in] |
| Memory | [Fill in] |
| Storage | [Fill in] |
| Public IP | [Fill in] |
| AMI | Amazon Linux 2023 |

**Screenshot: EC2 Instance Running**

<!-- Add your screenshot here -->
![EC2 Instance Details](evidence/ec2-instance-details.png)

**Screenshot: Web Page Response**

<!-- Add your screenshot here -->
![EC2 Web Response](evidence/ec2-webpage.png)

---

### Lambda Function

**Function Details:**
| Attribute | Value |
|-----------|-------|
| Function Name | `TechStart-HelloWorld` |
| Runtime | Python 3.12 |
| Memory Allocated | 128 MB |
| Timeout | 3 seconds |
| Architecture | x86_64 |

**Execution Metrics (from test):**
| Metric | Value |
|--------|-------|
| Duration | [Fill in] ms |
| Billed Duration | [Fill in] ms |
| Memory Used | [Fill in] MB |

**Screenshot: Lambda Test Results**

<!-- Add your screenshot here -->
![Lambda Execution Results](evidence/lambda-test-result.png)

---

## Comparison Analysis

### Side-by-Side Comparison

| Attribute | EC2 (t3.micro) | Lambda |
|-----------|----------------|--------|
| **Compute Model** | Virtual Machine | Serverless Function |
| **Startup Time** | [What I observed] | [What I observed] |
| **vCPU** | [Fill in] | Auto-allocated |
| **Memory** | [Fill in] | 128 MB (configurable) |
| **Storage** | [Fill in] | 512 MB ephemeral |
| **Billing Model** | Per hour while running | Per request + duration |
| **OS Access** | Full (SSH available) | None |
| **Scaling** | Manual or Auto Scaling Groups | Automatic |
| **Management Overhead** | High (patches, updates, security) | Low (AWS managed) |

### Cost Estimate

**Assumptions:** TechStart expects approximately 100,000 requests per month.

**EC2 Costs:**
| Item | Calculation | Monthly Cost |
|------|-------------|--------------|
| Instance (t3.micro) | $0.0104/hr × 730 hrs | $7.59 |
| Storage (20 GB gp3) | $0.08/GB × 20 GB | $1.60 |
| **Total** | | **$9.19** |

**Lambda Costs:**
| Item | Calculation | Monthly Cost |
|------|-------------|--------------|
| Requests | 100,000 × $0.0000002 | $0.02 |
| Duration | 100,000 × 100ms × $0.0000166667/GB-s | [Calculate] |
| **Total** | | **[Fill in]** |

<!--
Lambda pricing reference:
- $0.20 per 1 million requests
- $0.0000166667 per GB-second
- 128 MB = 0.125 GB
- If each request takes 100ms: 100,000 × 0.1s × 0.125 GB × $0.0000166667 = $0.02
-->

---

## Recommendations

### Scenario 1: TechStart's Main Website (24/7 traffic)

**My Recommendation:** [EC2 or Lambda?]

**Reasoning:**
[Explain why - consider consistent traffic patterns, need for customization, team familiarity, etc.]

---

### Scenario 2: Nightly Report Generator (runs once daily for 5 minutes)

**My Recommendation:** [EC2 or Lambda?]

**Reasoning:**
[Explain why - consider sporadic usage, cost efficiency, no idle time, etc.]

---

### Scenario 3: Image Processing API (unpredictable spikes, 0-10,000 requests/hour)

**My Recommendation:** [EC2 or Lambda?]

**Reasoning:**
[Explain why - consider scaling needs, cost during low traffic, burst capacity, etc.]

---

## Code Deployed

### EC2 User Data Script

The following bash script was executed on instance launch to configure the web server:

```bash
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>TechStart Inc. - Web Server</h1><p>Instance: $(hostname)</p>" > /var/www/html/index.html
```

**What this script does:**
1. [Explain line by line what each command does]
2. ...
3. ...

---

### Lambda Function Code

```python
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': '<h1>TechStart Inc. - Serverless Response</h1><p>Powered by AWS Lambda</p>'
    }
```

**What this code does:**
- [Explain the function structure and return format]

---

## Key Takeaways

1. **[First takeaway]:** [What did you learn about compute services?]

2. **[Second takeaway]:** [What surprised you about EC2 vs Lambda?]

3. **[Third takeaway]:** [How will this knowledge apply to real-world scenarios?]

---

## Resources Used

- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)
- [Lambda Pricing](https://aws.amazon.com/lambda/pricing/)

---

## Cleanup Confirmation

- [x] EC2 instance terminated
- [x] Lambda function deleted
- [x] Security group deleted

**I confirm that all AWS resources created during this lab have been terminated to avoid ongoing charges.**

---

> **Portfolio Note:** This lab demonstrates my ability to deploy and compare cloud compute services, analyze trade-offs, and make informed architectural recommendations.
