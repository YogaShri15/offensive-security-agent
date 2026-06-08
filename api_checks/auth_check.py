import requests

def run(url):

    findings = []

    try:

        response = requests.get(
            url,
            timeout=10
        )

        if response.status_code == 200:

            findings.append({
                "resource_arn": url,
                "severity": "Medium",
                "evidence": "Endpoint accessible without authentication",
                "business_impact": "Unauthorized access possible",
                "remediation": "Require authentication for sensitive endpoints"
            })

    except Exception as e:
        print(e)

    return findings