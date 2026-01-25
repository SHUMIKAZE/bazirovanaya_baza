from abc import ABC, abstractmethod
from sqlite3 import Connection
from typing import Any, Dict, List





class DBBase(ABC):
    @abstractmethod
    def __init__(self, conn: Connection) -> None:
        ...

    @abstractmethod
    def execute(self, table: Dict[str, str]) -> List[Any]:
        ...
