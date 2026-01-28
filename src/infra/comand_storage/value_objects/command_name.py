import re
from dataclasses import dataclass

@dataclass(frozen=True)
class CommandName:
    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError("Имя команды не может быть пустым.")
        
        if " " in self.value:
            raise ValueError(f"Имя команды не должно содержать пробелов: '{self.value}'")


        pattern = r"^[a-zA-Z0-9][a-zA-Z0-9._-]*$"
        
        if not re.match(pattern, self.value):
            raise ValueError(
                f"Некорректный формат имени команды: '{self.value}'. "
                "Разрешены только буквы, цифры, '.', '_' и '-'."
            )

    def __str__(self) -> str:
        return self.value
