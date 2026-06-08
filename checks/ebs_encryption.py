import boto3

def run():

    findings = []

    ec2 = boto3.client("ec2")

    volumes = ec2.describe_volumes()["Volumes"]

    for volume in volumes:

        if not volume["Encrypted"]:

            findings.append({
                "resource_arn": volume["VolumeId"],
                "severity": "High",
                "evidence": "EBS volume not encrypted",
                "business_impact": "Data exposure risk",
                "remediation": "Enable EBS encryption"
            })

    return findings