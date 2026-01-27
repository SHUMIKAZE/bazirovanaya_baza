from dataclasses import dataclass
from abc import ABC, abstractmethod


class _LexerBase(ABC):

    @abstractmethod
    def tockenize(self, cmd: str): ...