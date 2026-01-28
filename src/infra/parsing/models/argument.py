from dataclasses import dataclass

@dataclass(frozen=True)
class Argument:
    value: str