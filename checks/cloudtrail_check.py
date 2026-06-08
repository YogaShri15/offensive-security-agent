import boto3

def run():

    findings = []

    cloudtrail = boto3.client("cloudtrail")

    trails = cloudtrail.describe_trails()

    if len(trails["trailList"]) == 0:

        findings.append({
            "resource_arn": "AWS Account",
            "severity": "High",
            "evidence": "No CloudTrail trail configured",
            "business_impact": "No audit logging available",
            "remediation": "Enable CloudTrail"
        })

    return findings