import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import schedule
import time

from audit_logger import log_event
import main_level2


def run_scan():

    log_event("Security scan started")

    findings = main_level2.run()

    log_event(
        f"{len(findings)} findings detected"
    )

    log_event("Security scan completed")

    print("\n")
    print("=" * 60)
    print("RUNNING SECURITY SCAN")
    print("=" * 60)

    print(
        f"Total Findings : {len(findings)}"
    )

    print("Scan completed")


schedule.every(1).minutes.do(
    run_scan
)

print("Scheduler started...")

try:

    while True:

        schedule.run_pending()

        time.sleep(1)

except KeyboardInterrupt:

    print("\n")
    print("=" * 60)
    print("SCHEDULER STOPPED")
    print("=" * 60)

    log_event(
        "Scheduler stopped by user"
    )