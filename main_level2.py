from checks import mfa_check
from checks import admin_users
from checks import security_group
from checks import cloudtrail_check
from checks import password_policy

from api_checks import security_headers
from api_checks import cors_check
from api_checks import error_disclosure
from api_checks import rate_limit_check
from api_checks import auth_check

from dependency_checks import dependency_scanner
from secret_checks import secret_scanner


def run():

    results = []

    # ==========================================
    # AWS INFRASTRUCTURE SCAN
    # ==========================================

    results.extend(mfa_check.run())
    results.extend(admin_users.run())
    results.extend(security_group.run())
    results.extend(cloudtrail_check.run())
    results.extend(password_policy.run())

    # ==========================================
    # API SCAN
    # ==========================================

    url = "https://jsonplaceholder.typicode.com/posts"

    results.extend(security_headers.run(url))
    results.extend(cors_check.run(url))
    results.extend(error_disclosure.run(url))
    results.extend(rate_limit_check.run(url))
    results.extend(auth_check.run(url))

    # ==========================================
    # DEPENDENCY SCAN
    # ==========================================

    results.extend(
        dependency_scanner.run()
    )

    # ==========================================
    # SECRET SCAN
    # ==========================================

    results.extend(
        secret_scanner.run()
    )

    # ==========================================
    # DEDUPLICATION
    # ==========================================

    unique_findings = []
    seen = set()

    for finding in results:

        key = (
            finding["resource_arn"],
            finding["evidence"]
        )

        if key not in seen:

            seen.add(key)

            unique_findings.append(
                finding
            )

    return unique_findings


if __name__ == "__main__":

    unique_findings = run()

    print("\n")
    print("=" * 70)
    print("LEVEL 2 MULTI-DOMAIN SECURITY REPORT")
    print("=" * 70)

    for i, finding in enumerate(
        unique_findings,
        start=1
    ):

        print("\n" + "=" * 70)
        print(f"Finding #{i}")
        print("=" * 70)

        for key, value in finding.items():

            print(
                f"{key}: {value}"
            )

    print("\n")
    print("=" * 70)
    print(
        f"Total Findings: "
        f"{len(unique_findings)}"
    )
    print("=" * 70)