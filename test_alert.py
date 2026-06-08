from notifications.critical_alert import (
    send_alert
)

sample = [

    {
        "resource_arn":
        "sg-123456",

        "severity":
        "Critical",

        "evidence":
        "Security Group open to 0.0.0.0/0"
    },

    {
        "resource_arn":
        "IAM User",

        "severity":
        "High",

        "evidence":
        "MFA not enabled"
    }
]

send_alert(sample)