import sqlite3

def init(db_path, schema_path):
    conn= sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    with open(schema_path, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    return conn

def close(conn):
    conn.close()
    conn = None
