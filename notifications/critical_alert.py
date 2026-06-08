def send_alert(findings):
    
    critical_findings = []

    for finding in findings:

        if finding["severity"] == "Critical":

            critical_findings.append(
                finding
            )

    if len(critical_findings) > 0:

        print("\n")
        print("=" * 60)
        print("CRITICAL SECURITY ALERT")
        print("=" * 60)

        for finding in critical_findings:

            print(
                f"Resource : "
                f"{finding['resource_arn']}"
            )

            print(
                f"Evidence : "
                f"{finding['evidence']}"
            )

            print("-" * 60)

    else:

        print(
            "No critical findings."
        )