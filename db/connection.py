import sqlite3

_conn = None

def connect(DB_PATH):
    global _conn
    if _conn is None:
        _conn = sqlite3.connect(DB_PATH)
        _conn.row_factory = sqlite3.Row
    return _conn

def close():
    global _conn
    if _conn is not None:
        _conn.close()
        _conn = None
