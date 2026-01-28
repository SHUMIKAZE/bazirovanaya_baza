from dataclasses import dataclass
from typing import Optional

@dataclass
class Flag:
    name: str
    arg: Optional[str]

    def set_arg(self, arg: str):
        if self.has_arg:
            raise ValueError("Флаг уже имеет аргумент.")
        self.arg = arg

    @property
    def has_arg(self) -> bool:
        return self.arg is not None