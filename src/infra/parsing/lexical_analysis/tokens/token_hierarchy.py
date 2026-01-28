from typing import List

from .tokens import Token

class TokenConflictResolver:
    """
    Resolves conflicts when multiple token patterns match the same input text.
    It uses a predefined hierarchy to select the most specific token type.
    """

    @classmethod
    def _get_sort_key(cls, token: Token) -> tuple[int, float]:
        # Primary sort key: Length (descending) -> represented as negative number
        length_key = -len(token)
        
        # Secondary sort key: Priority (descending) -> represented as negative number
        # Higher priority value means "more important", so we negate it for min() function or reverse logic
        priority_key = -float(getattr(token, 'priority', 0))

        return length_key, priority_key

    @classmethod
    def resolve(cls, candidates: List[Token]) -> Token:
        if not candidates:
            raise ValueError("Cannot resolve conflict: candidate list is empty.")

        return min(candidates, key=cls._get_sort_key)
