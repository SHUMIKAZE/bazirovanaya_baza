from dataclasses import dataclass

@dataclass(frozen=True)
class Argument:
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise ValueError("Значение аргумента должно быть строкой.")
        
        if not self.value:
            raise ValueError("Аргумент флага не может быть пустым.")

    def __str__(self) -> str:
        return self.value