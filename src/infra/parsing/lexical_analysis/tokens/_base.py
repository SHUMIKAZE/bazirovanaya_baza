from typing import ClassVar, TYPE_CHECKING
import re

if TYPE_CHECKING:
    from .tokens_scheme import TokenType


class _BaseToken:
    pattern: ClassVar[re.Pattern[str]]

    def __init__(self, match: str = '', *, token_type: 'TokenType') -> None:
        self.matched_string: str = match
        self.value: str = self._process_value(match)
        self.token_type: 'TokenType' = token_type

    def _process_value(self, match: str) -> str:
        """Метод для постобработки найденной строки. По умолчанию возвращает как есть."""
        return match

    def __len__(self) -> int:
        return len(self.matched_string)
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.value}', matched_string='{self.matched_string}')"

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} '{self.value}'>"
    
