import json
import os

DATABASE_FILE = "storage/findings_db.json"

def load_findings():

    if not os.path.exists(
        DATABASE_FILE
    ):
        return []

    with open(
        DATABASE_FILE,
        "r"
    ) as file:

        return json.load(file)