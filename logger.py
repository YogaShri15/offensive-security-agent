from datetime import datetime

def log_error(check_name, error):

    with open("reports/error.log", "a") as file:

        file.write(
            f"[{datetime.now()}] "
            f"[ERROR] "
            f"[{check_name}] "
            f"{str(error)}\n"
        )