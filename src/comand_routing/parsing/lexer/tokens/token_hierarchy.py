from typing import List, Type

from .tokens import (
    EqualsToken,
    IdentifierToken,
    LongFlagToken,
    ShortFlagToken,
    StringToken,
    WhitespaceToken,
    EOFToken,
    Token,
)

class TokenConflictResolver:
    """
    Resolves conflicts when multiple token patterns match the same input text.
    It uses a predefined hierarchy to select the most specific token type.
    """

    # Priority order: The token type at index 0 has the highest priority.
    # Specific matches (literals, complex structures) should generally be higher than generic ones.
    _PRIORITY: List[Type[Token]] = [
        StringToken,      # High priority: Specific complex structure
        EqualsToken,      # High priority: Exact literal match
        LongFlagToken,    # Medium priority: Specific flag syntax
        ShortFlagToken,   # Medium priority: Specific flag syntax
        IdentifierToken,  # Low priority: Generic alphanumeric pattern (catch-all for words)
        WhitespaceToken,  # Lowest priority: Separator
        EOFToken,         # Lowest priority: End of input
    ]

    @classmethod
    def _get_sort_key(cls, token: Token) -> tuple[int, float]:
        length_key = -len(token)

        try:
            priority_key = float(cls._PRIORITY.index(type(token)))
        except ValueError:
            priority_key = float('inf')

        return length_key, priority_key

    @classmethod
    def resolve(cls, candidates: List[Token]) -> Token:
        if not candidates:
            raise ValueError("Cannot resolve conflict: candidate list is empty.")

        return min(candidates, key=cls._get_sort_key)
