# Offensive Security Agent

AI/ML Hiring Challenge - Agent 2: Offensive Security Agent

## Overview

This project is an autonomous security scanning agent that continuously evaluates AWS infrastructure, API endpoints, application dependencies, and source code secrets.

The agent generates actionable findings with severity ratings, business impact, and remediation guidance.

---

## Features

### Level 1 - Infrastructure Security Scanning

* IAM MFA Check
* Administrator Access Detection
* Security Group Exposure Detection
* CloudTrail Verification
* Password Policy Validation
* JSON Report Generation
* Markdown Report Generation

### Level 2 - Multi-Domain Security Scanning

#### AWS Infrastructure

* MFA Validation
* Admin Policy Detection
* Security Group Review
* CloudTrail Validation
* Password Policy Checks

#### API Security

* Security Headers Validation
* CORS Misconfiguration Detection
* Error Disclosure Detection
* Rate Limiting Checks
* Authentication Validation

#### Dependency Security

* Vulnerable Package Detection
* CVE Identification
* CVSS Severity Scoring

#### Secret Scanning

* AWS Access Key Detection
* Hardcoded Password Detection

### Level 3 - Autonomous Continuous Scanning

* Scheduled Security Scans
* Audit Logging
* Critical Alerting
* Finding Persistence
* Deduplication Across Runs

---

## Project Structure

offensive-security-system/

├── checks/

├── api_checks/

├── dependency_checks/

├── secret_checks/

├── scheduler/

├── storage/

├── notifications/

├── reports/

├── logs/

├── main.py

├── main_level2.py

└── requirements.txt

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run Level 1

```bash
python main.py
```

---

## Run Level 2

```bash
python main_level2.py
```

---

## Run Continuous Scanning

```bash
python scheduler/run_scheduler.py
```

---

## Output

The agent generates:

* Console Reports
* JSON Findings
* Markdown Reports
* Audit Logs
* Critical Security Alerts

---

## Sample Findings

* MFA Not Enabled
* Administrator Access Assigned
* Public Security Groups
* Missing CloudTrail
* Weak Password Policies
* Missing Security Headers
* Vulnerable Dependencies
* Hardcoded Secrets

---

## Author

Yoga Shri P K
