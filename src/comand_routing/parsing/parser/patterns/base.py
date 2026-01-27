from abc import ABC, abstractmethod
from typing import List, Optional, TYPE_CHECKING

from ...lexer.tokens.token_flow import TokenFlow
from ...lexer.tokens.tokens import Token

if TYPE_CHECKING:
    from .combinators import SequencePattern, AlternativePattern, NotPattern, AndPattern


class TokenPatternBase(ABC):
    """
    Базовый класс для паттернов токенов.
    Позволяет описывать структуру команды как комбинацию типов токенов.
    """

    @abstractmethod
    def match(self, flow: TokenFlow) -> Optional[List[Token]]:
        """
        Проверяет, соответствует ли начало потока токенов этому паттерну.
        Не изменяет переданный поток (lookahead).
        
        :return: Список совпавших токенов или None, если совпадения нет.
        """
        pass

    def __add__(self, other: 'TokenPatternBase') -> 'SequencePattern':
        """Оператор + для создания последовательности (Sequence)."""
        # Локальный импорт для предотвращения циклической зависимости
        from .combinators import SequencePattern
        return SequencePattern(self, other)

    def __or__(self, other: 'TokenPatternBase') -> 'AlternativePattern':
        """Оператор | для создания выбора (Alternative)."""
        # Локальный импорт для предотвращения циклической зависимости
        from .combinators import AlternativePattern
        return AlternativePattern(self, other)

    def __invert__(self) -> 'NotPattern':
        """Оператор ~ для создания отрицания (NotPattern)."""
        # Локальный импорт для предотвращения циклической зависимости
        from .combinators import NotPattern
        return NotPattern(self)

    def __and__(self, other: 'TokenPatternBase') -> 'AndPattern':
        """Оператор & для создания пересечения (AndPattern)."""
        # Локальный импорт для предотвращения циклической зависимости
        from .combinators import AndPattern
        return AndPattern(self, other)