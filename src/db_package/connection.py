from typing import Optional
from pathlib import Path
import sqlite3

from ..config import DB_PATH, SCHEMA_PATH

class DBConnection:
    def __init__(
        self,
        db_path: Path = DB_PATH,
        schema_path: Path = SCHEMA_PATH
    ) -> None:

        self.db_path = db_path
        self.schema_path = schema_path
        self.conn: Optional[sqlite3.Connection] = None
    
    def connect(self) -> None:
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

    def close(self) -> None:
        if self.conn:
            self.conn.close()
        self.conn = None


def init(db_path, schema_path):
    conn= sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    with open(schema_path, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    return conn

def close(conn):
    conn.close()
    conn = None
