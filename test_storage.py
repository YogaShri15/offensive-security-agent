from storage.finding_store import (
    save_findings
)

from storage.finding_loader import (
    load_findings
)

sample = [

    {
        "resource_arn":
        "test-resource",

        "severity":
        "High",

        "evidence":
        "Demo Finding",

        "business_impact":
        "Demo Impact",

        "remediation":
        "Demo Fix"
    }
]

save_findings(sample)

results = load_findings()

print(results)