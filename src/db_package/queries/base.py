from abc import ABC
from typing import Any, List

class DBBase(ABC):
    def __init__(self, conn) -> None:
        ...

    def execute(self, table) -> List[Any]:
        ...
