from sqlite3 import Connection
from typing import Any, Dict
from .base import DBBase





class DBGetList(DBBase):
    QUERY_MAP = {
        'works': "SELECT * FROM works",
        'genres': "SELECT * FROM genres",
    }

    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def execute(self, table: Dict[str,str]) -> list[Any]:
        table_key = table["target"]

        if table_key not in DBGetList.QUERY_MAP:
            raise ValueError(f"Key {table_key} is not found.")

        sql = DBGetList.QUERY_MAP[table_key]
        cursor = self.conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        return data
