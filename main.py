import yaml

from checks import s3_public
from checks import mfa_check
from checks import admin_users
from checks import security_group
from checks import s3_encryption
from checks import cloudtrail_check
from checks import root_mfa
from checks import password_policy
from checks import unused_keys
from checks import ebs_encryption

from report_generator import (
    generate_json_report,
    generate_markdown_report
)

results = []

with open("config/checks.yaml", "r") as file:
    config = yaml.safe_load(file)

if "public_s3" in config["checks"]:
    results.extend(s3_public.run())

if "mfa_disabled" in config["checks"]:
    results.extend(mfa_check.run())

if "admin_users" in config["checks"]:
    results.extend(admin_users.run())

if "open_security_groups" in config["checks"]:
    results.extend(security_group.run())

if "s3_encryption" in config["checks"]:
    results.extend(s3_encryption.run())

if "cloudtrail" in config["checks"]:
    results.extend(cloudtrail_check.run())

if "root_mfa" in config["checks"]:
    results.extend(root_mfa.run())

if "password_policy" in config["checks"]:
    results.extend(password_policy.run())

if "unused_access_keys" in config["checks"]:
    results.extend(unused_keys.run())

if "ebs_encryption" in config["checks"]:
    results.extend(ebs_encryption.run())

generate_json_report(results)
generate_markdown_report(results)

print("\n")
print("=" * 60)
print("AWS SECURITY SCAN REPORT")
print("=" * 60)

if len(results) == 0:
    print("\nNo security findings detected.\n")

for i, finding in enumerate(results, start=1):

    print("\n" + "=" * 60)
    print(f"Finding #{i}")
    print("=" * 60)

    print(f"Resource ARN    : {finding['resource_arn']}")
    print(f"Severity        : {finding['severity']}")
    print(f"Evidence        : {finding['evidence']}")
    print(f"Business Impact : {finding['business_impact']}")
    print(f"Remediation     : {finding['remediation']}")

print("\n" + "=" * 60)
print("JSON report generated -> reports/findings.json")
print("Markdown report generated -> reports/report.md")
print("=" * 60)