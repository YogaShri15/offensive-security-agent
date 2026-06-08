import requests

def run(url):

    findings = []

    success_count = 0

    try:

        for _ in range(20):

            response = requests.get(
                url,
                timeout=5
            )

            if response.status_code == 200:
                success_count += 1

        if success_count == 20:

            findings.append({
                "resource_arn": url,
                "severity": "Medium",
                "evidence": "No rate limiting detected",
                "business_impact": "Potential abuse and DoS risk",
                "remediation": "Implement rate limiting"
            })

    except Exception as e:
        print(e)

    return findings