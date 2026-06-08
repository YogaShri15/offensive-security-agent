import boto3

def run():

    findings = []
    processed = set()

    ec2 = boto3.client("ec2")

    groups = ec2.describe_security_groups()

    for sg in groups["SecurityGroups"]:

        for permission in sg.get("IpPermissions", []):

            for ip in permission.get("IpRanges", []):

                if ip.get("CidrIp") == "0.0.0.0/0":

                    if sg["GroupId"] not in processed:

                        findings.append({
                            "resource_arn": sg["GroupId"],
                            "severity": "Critical",
                            "evidence": "Security Group open to 0.0.0.0/0",
                            "business_impact": "Unauthorized internet access",
                            "remediation": "Restrict inbound rules"
                        })

                        processed.add(sg["GroupId"])

    return findings