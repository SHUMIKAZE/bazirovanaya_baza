import sqlite3
from pathlib import Path

SCHEMA_PATH = Path("db/schema.sql")

REWRITTING_PASSWORD = "REWRITE"

def init(DB_PATH):
    if DB_PATH.exists():
        print("DB already exists. Openning...")
    else:
        print("Creating database...")

    conn = sqlite3.connect(DB_PATH)
    print("Creating tables...")

    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        conn.executescript(f.read())

    conn.close()
    print("DB ready.")


if __name__ == "__main__":
    #init()
    print("DB ready.")
    while input(f"If you want to rewrite DB type '{REWRITTING_PASSWORD}': ") == REWRITTING_PASSWORD:
        print("Deleting...")
        #DB_PATH.unlink()
        #init()
        print("DB succesfully rewritten.")
