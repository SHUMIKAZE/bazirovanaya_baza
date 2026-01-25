from typing import Optional
from pathlib import Path
from sqlite3 import Connection, Row, connect


class DBConnection:
    def __init__(self, db_path: Path, schema_path: Path) -> None:
        self.db_path = db_path
        self.schema_path = schema_path
        self.conn: Optional[Connection] = None
    
    def connect(self) -> None:
        self.conn = connect(self.db_path)
        self.conn.row_factory = Row

        with open(self.schema_path, "r", encoding="utf-8") as f:
            self.conn.executescript(f.read())

    def close(self) -> None:
        if self.conn:
            self.conn.close()
        self.conn = None
