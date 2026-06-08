import boto3
from datetime import datetime, timezone

def run():

    findings = []

    iam = boto3.client("iam")

    users = iam.list_users()["Users"]

    for user in users:

        keys = iam.list_access_keys(
            UserName=user["UserName"]
        )["AccessKeyMetadata"]

        for key in keys:

            age = (
                datetime.now(timezone.utc)
                - key["CreateDate"]
            ).days

            if age > 90:

                findings.append({
                    "resource_arn": key["AccessKeyId"],
                    "severity": "Medium",
                    "evidence": f"Access key age {age} days",
                    "business_impact": "Credential exposure risk",
                    "remediation": "Rotate access keys"
                })

    return findings