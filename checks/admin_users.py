import boto3

def run():

    findings = []

    iam = boto3.client("iam")

    users = iam.list_users()["Users"]

    for user in users:

        attached = iam.list_attached_user_policies(
            UserName=user["UserName"]
        )

        for policy in attached["AttachedPolicies"]:

            if policy["PolicyName"] == "AdministratorAccess":

                findings.append({
                    "resource_arn": user["Arn"],
                    "severity": "Critical",
                    "evidence": "AdministratorAccess policy attached",
                    "business_impact": "Full account compromise possible",
                    "remediation": "Apply least privilege principle"
                })

    return findings