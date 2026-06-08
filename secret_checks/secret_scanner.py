import re
import os

def run():

    findings = []

    patterns = {
        "AWS Access Key":
        r"AKIA[0-9A-Z]{16}",

        "Password":
        r"password\s*=\s*[\"'].*?[\"']",

        "API Token":
        r"token\s*=\s*[\"'].*?[\"']"
    }

    for root, dirs, files in os.walk("."):

        for file in files:

            if file.endswith(
                (
                    ".py",
                    ".txt",
                    ".yaml",
                    ".yml",
                    ".env"
                )
            ):

                path = os.path.join(
                    root,
                    file
                )

                try:

                    with open(
                        path,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        content = f.read()

                        for name, pattern in patterns.items():

                            matches = re.findall(
                                pattern,
                                content,
                                re.IGNORECASE
                            )

                            if matches:

                                findings.append({
                                    "resource_arn": path,
                                    "severity": "Critical",
                                    "evidence": f"{name} detected",
                                    "business_impact": "Credential exposure",
                                    "remediation": "Remove hardcoded secret"
                                })

                except Exception:
                    pass

    return findings