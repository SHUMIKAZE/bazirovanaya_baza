from typing import overload, Iterable

class Command:
    __slots__ = ("parts",)

    @overload
    def __init__(self, parts: str) -> None: ...

    @overload
    def __init__(self, parts: Iterable[str]) -> None: ...

    def __init__(self, parts: str | Iterable[str]) -> None:
        if isinstance(parts, str):
            self.parts = (parts.strip(),)
        else:
            self.parts = tuple(part.strip() for part in parts)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Command):
            return NotImplemented
        return self.parts == other.parts

    def __hash__(self) -> int:
        return hash(self.parts)
    
    def __repr__(self) -> str:
        return f"Command({self.parts})"

    def __str__(self) -> str:
        return " ".join(self.parts)