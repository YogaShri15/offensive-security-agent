import requests

def run(url):

    findings = []

    response = requests.get(url, timeout=10)

    headers = response.headers

    required_headers = [
        "X-Frame-Options",
        "Content-Security-Policy",
        "X-Content-Type-Options"
    ]

    for header in required_headers:

        if header not in headers:

            findings.append({
                "resource_arn": url,
                "severity": "Medium",
                "evidence": f"{header} missing",
                "business_impact": "Reduced browser security",
                "remediation": f"Add {header} header"
            })

    return findings