import sqlite3

def connect(DB_PATH):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def close(conn):
    conn.close()
    conn = None
