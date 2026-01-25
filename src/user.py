from pathlib import Path
from .database import Database





class User:
    def __init__(self, db_path: Path, schema_path: Path) -> None:
        self.db = Database(db_path, schema_path)
        self.db.media.connect()
