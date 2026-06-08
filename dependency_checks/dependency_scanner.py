import pkg_resources

def run():

    findings = []

    vulnerable_packages = {
        "urllib3": {
            "cve": "CVE-2023-43804",
            "cvss": "7.5",
            "fixed_version": "2.0.7"
        }
    }

    installed_packages = pkg_resources.working_set

    for package in installed_packages:

        package_name = package.project_name.lower()

        if package_name in vulnerable_packages:

            vuln = vulnerable_packages[package_name]

            findings.append({
                "resource_arn": package_name,
                "severity": "High",
                "evidence": f"{package_name} {package.version}",
                "business_impact": f"Known vulnerability {vuln['cve']}",
                "remediation": (
                    f"Upgrade to "
                    f"{vuln['fixed_version']}"
                ),
                "cve": vuln["cve"],
                "cvss": vuln["cvss"]
            })

    return findings