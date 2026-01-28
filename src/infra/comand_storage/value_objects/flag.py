import re
from dataclasses import dataclass
from typing import Optional

from .argument import Argument

@dataclass(frozen=True)
class Flag:
    value: str
    argument: Optional[Argument] = None

    def __post_init__(self):
        if not self.value:
            raise ValueError("Флаг не может быть пустым.")

        if not self.value.startswith("-"):
            raise ValueError(f"Флаг должен начинаться с '-' или '--': '{self.value}'")

        if " " in self.value:
            raise ValueError(f"Флаг не должен содержать пробелов: '{self.value}'")

        pattern = r"^-{1,2}[a-zA-Z0-9][a-zA-Z0-9._-]*$"

        if not re.match(pattern, self.value):
            raise ValueError(
                f"Некорректный формат флага: '{self.value}'. "
                "Ожидается формат типа '-v' или '--verbose'."
            )

    def __str__(self) -> str:
        return self.value
