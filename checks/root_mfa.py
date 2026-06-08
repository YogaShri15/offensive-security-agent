import boto3

def run():

    findings = []

    iam = boto3.client("iam")

    summary = iam.get_account_summary()["SummaryMap"]

    if summary.get("AccountMFAEnabled", 0) == 0:

        findings.append({
            "resource_arn": "Root User",
            "severity": "Critical",
            "evidence": "Root user MFA not enabled",
            "business_impact": "Root account compromise",
            "remediation": "Enable MFA on root account"
        })

    return findings