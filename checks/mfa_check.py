import boto3

def run():

    findings = []

    iam = boto3.client("iam")

    users = iam.list_users()["Users"]

    for user in users:

        devices = iam.list_mfa_devices(
            UserName=user["UserName"]
        )["MFADevices"]

        if len(devices) == 0:

            findings.append({
                "resource_arn": user["Arn"],
                "severity": "High",
                "evidence": "MFA not enabled",
                "business_impact": "Account compromise risk",
                "remediation": "Enable MFA"
            })

    return findings