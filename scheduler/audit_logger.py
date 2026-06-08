from datetime import datetime

LOG_FILE = "logs/audit.log"

def log_event(message):

    with open(
        LOG_FILE,
        "a"
    ) as file:

        file.write(
            f"[{datetime.now()}] "
            f"{message}\n"
        )