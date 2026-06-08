import boto3
from logger import log_error 

def run():
    findings = []

    s3 = boto3.client("s3")

    buckets = s3.list_buckets()["Buckets"]

    for bucket in buckets:
        bucket_name = bucket["Name"]

        try:
            status = s3.get_bucket_policy_status(
                Bucket=bucket_name
            )

            if status["PolicyStatus"]["IsPublic"]:

                findings.append({
                    "resource_arn": f"arn:aws:s3:::{bucket_name}",
                    "severity": "Critical",
                    "evidence": "Bucket is publicly accessible",
                    "business_impact": "Sensitive data exposure",
                    "remediation": "Enable Block Public Access"
                })

        except Exception as e:

            log_error(
                "public_s3",
                e
            )

    return findings