import json

from datetime import datetime

from storage.finding_loader import (
    load_findings
)

DATABASE_FILE = "storage/findings_db.json"

def save_findings(findings):

    existing = load_findings()

    for finding in findings:

        duplicate = False

        for record in existing:

            if (
                record["resource_arn"]
                ==
                finding["resource_arn"]

                and

                record["evidence"]
                ==
                finding["evidence"]
            ):

                record[
                    "last_seen"
                ] = datetime.now().isoformat()

                duplicate = True

                break

        if not duplicate:

            existing.append({

                "status": "OPEN",

                "created_at":
                datetime.now().isoformat(),

                "last_seen":
                datetime.now().isoformat(),

                **finding
            })

    with open(
        DATABASE_FILE,
        "w"
    ) as file:

        json.dump(
            existing,
            file,
            indent=4
        )