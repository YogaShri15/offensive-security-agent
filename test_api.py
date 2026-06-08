from api_checks import security_headers
from api_checks import cors_check
from api_checks import error_disclosure
from api_checks import rate_limit_check
from api_checks import auth_check

results = []

url = "https://jsonplaceholder.typicode.com/posts"

results.extend(
    security_headers.run(url)
)

results.extend(
    cors_check.run(url)
)

results.extend(
    error_disclosure.run(url)
)

results.extend(
    rate_limit_check.run(url)
)

results.extend(
    auth_check.run(url)
)

print("\n")
print("=" * 60)
print("API SECURITY SCAN REPORT")
print("=" * 60)

if len(results) == 0:
    print("\nNo API security findings detected.\n")

for i, finding in enumerate(results, start=1):

    print("\n" + "=" * 60)
    print(f"Finding #{i}")
    print("=" * 60)

    print(f"Resource ARN    : {finding['resource_arn']}")
    print(f"Severity        : {finding['severity']}")
    print(f"Evidence        : {finding['evidence']}")
    print(f"Business Impact : {finding['business_impact']}")
    print(f"Remediation     : {finding['remediation']}")

print("\n" + "=" * 60)
print(f"Total Findings : {len(results)}")
print("=" * 60)