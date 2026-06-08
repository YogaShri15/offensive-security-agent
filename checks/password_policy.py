import boto3
from botocore.exceptions import ClientError
from logger import log_error

def run():

    findings = []

    iam = boto3.client("iam")

    try:

        policy = iam.get_account_password_policy()

        minimum_length = policy["PasswordPolicy"]["MinimumPasswordLength"]

        if minimum_length < 12:

            findings.append({
                "resource_arn": "Account Password Policy",
                "severity": "Medium",
                "evidence": "Password length less than 12",
                "business_impact": "Weak passwords possible",
                "remediation": "Set minimum password length to 12+"
            })

    except ClientError as e:

        if e.response["Error"]["Code"] == "NoSuchEntity":

            findings.append({
                "resource_arn": "Account Password Policy",
                "severity": "High",
                "evidence": "No password policy configured",
                "business_impact": "Weak account security",
                "remediation": "Configure strong password policy"
            })

        else:

            log_error(
                "password_policy",
                e
            )

    return findings