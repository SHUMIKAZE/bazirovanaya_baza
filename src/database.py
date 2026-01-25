from pathlib import Path
from .db_package import (
    DBConnection,
    DBGetList
)





class Database:
    def __init__(self, db_path: Path, schema_path: Path) -> None:
        self.media = DBConnection(db_path, schema_path)
        self.media.connect()

        if self.media.conn is None:
            raise ValueError("DB is not connected.")

        self.get_list = DBGetList(self.media.conn)
