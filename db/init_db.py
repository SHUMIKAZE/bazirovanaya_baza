import sqlite3
from pathlib import Path

DB_PATH = Path("media.db")
SCHEMA_PATH = Path("db/schema.sql")

REWRITTING_PASSWORD = "REWRITE"

def init_db():
    if DB_PATH.exists():
        print("DB already exists. Openning...")
    else:
        print("Creating database...")

    conn = sqlite3.connect(DB_PATH)
    print("Creating tables...")

    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        conn.executescript(f.read())

    conn.close()

if __name__ == "__main__":
    init_db()
    print("DB ready.")
    while input(f"If you want to rewrite DB type '{REWRITTING_PASSWORD}': ") == REWRITTING_PASSWORD:
        print("Deleting...")
        DB_PATH.unlink()
        init_db()
        print("DB succesfully rewritten.")
