import requests

def run(url):

    findings = []

    try:

        response = requests.get(
            url,
            timeout=10
        )

        cors = response.headers.get(
            "Access-Control-Allow-Origin"
        )

        if cors == "*":

            findings.append({
                "resource_arn": url,
                "severity": "High",
                "evidence": "CORS allows all origins (*)",
                "business_impact": "Cross-origin data exposure",
                "remediation": "Restrict allowed origins"
            })

    except Exception as e:

        print(e)

    return findings