import json

def generate_json_report(results):

    with open("reports/findings.json", "w") as file:
        json.dump(results, file, indent=4)

def generate_markdown_report(results):

    with open("reports/report.md", "w") as file:

        file.write("# Security Scan Report\n\n")

        for i, finding in enumerate(results, start=1):

            file.write(f"## Finding {i}\n\n")
            file.write(f"**Resource ARN:** {finding['resource_arn']}\n\n")
            file.write(f"**Severity:** {finding['severity']}\n\n")
            file.write(f"**Evidence:** {finding['evidence']}\n\n")
            file.write(f"**Business Impact:** {finding['business_impact']}\n\n")
            file.write(f"**Remediation:** {finding['remediation']}\n\n")
            file.write("---\n\n")