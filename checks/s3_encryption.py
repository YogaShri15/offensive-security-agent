import boto3
from logger import log_error

def run():

    findings = []

    s3 = boto3.client("s3")

    buckets = s3.list_buckets()["Buckets"]

    for bucket in buckets:

        bucket_name = bucket["Name"]

        try:

            s3.get_bucket_encryption(
                Bucket=bucket_name
            )

        except Exception as e:

            log_error(
                "s3_encryption",
                e
            )

            findings.append({
                "resource_arn": f"arn:aws:s3:::{bucket_name}",
                "severity": "High",
                "evidence": "Bucket encryption not enabled",
                "business_impact": "Sensitive data exposure",
                "remediation": "Enable default encryption"
            })

    return findings