import requests

def run(url):

    findings = []

    try:

        test_url = url + "/nonexistentendpoint123"

        response = requests.get(
            test_url,
            timeout=10
        )

        body = response.text.lower()

        keywords = [
            "stack trace",
            "exception",
            "traceback",
            "sql syntax",
            "internal server error"
        ]

        for keyword in keywords:

            if keyword in body:

                findings.append({
                    "resource_arn": url,
                    "severity": "Medium",
                    "evidence": f"Error disclosure: {keyword}",
                    "business_impact": "Information leakage",
                    "remediation": "Hide internal errors"
                })

                break

    except Exception as e:

        print(e)

    return findings