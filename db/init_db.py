import sqlite3
from pathlib import Path

DB_PATH = Path("media.db")
SCHEMA_PATH = Path("db/schema.sql")

def init_db():
    if DB_PATH.exists():
        print("DB already exists.")
        return

    print("Creating database...")

    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        conn.executescript(f.read())

    conn.close()
    print("Done.")

if __name__ == "__main__":
    init_db()
