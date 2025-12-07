# AWS Cloud Mastery for Automation Engineers

## 1. S3 (Simple Storage Service)
The "Hard Drive" of the cloud.
*   **Buckets**: Like folders. Unique names globally.
*   **Objects**: Files inside buckets.
*   **Lifecycle Rules**: Auto-delete files after 30 days (Save money!).

### Python Example (Boto3)
```python
import boto3
s3 = boto3.client('s3')
s3.upload_file("report.html", "my-test-bucket", "daily_report.html")
```

## 2. EC2 (Elastic Compute Cloud)
The "Virtual Computer".
*   You choose OS (Linux/Windows) and Size (t2.micro).
*   **Security Groups**: The Firewall. (Allow Port 22 for SSH, 80 for Web).

## 3. Lambda (Serverless)
The "Function as a Service".
*   You don't rent a server. You just upload Python code.
*   Trigger: "Run this function whenever a file is uploaded to S3".
*   Use Case: Auto-validating data files when they arrive.

---

## [HANDS ON TASK]
1.  Log into AWS Console (Free Tier).
2.  Create an S3 Bucket.
3.  Manually upload a file.
4.  Try to read it using the `portfolio/python-frameworks/utils/aws_handler.py` script.
