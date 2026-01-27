from typing import List, Optional

from ...lexer.tokens.token_flow import TokenFlow
from ...lexer.tokens.tokens import Token
from .base import TokenPatternBase


class SequencePattern(TokenPatternBase):
    """Паттерн последовательности: ожидает паттерны один за другим (AND)."""

    def __init__(self, *patterns: TokenPatternBase):
        self.patterns = patterns

    def match(self, flow: TokenFlow) -> Optional[List[Token]]:
        matched_total = []

        current_tokens = list(flow)
        
        for pattern in self.patterns:

            temp_flow = TokenFlow()
            temp_flow.extend(current_tokens)
            
            matched = pattern.match(temp_flow)
            if matched is None:
                return None
            
            matched_total.extend(matched)

            current_tokens = current_tokens[len(matched):]
            
        return matched_total
    
    def __add__(self, other: TokenPatternBase) -> 'SequencePattern':

        if isinstance(other, SequencePattern):
            return SequencePattern(*self.patterns, *other.patterns)
        return SequencePattern(*self.patterns, other)


class AlternativePattern(TokenPatternBase):
    """Паттерн выбора: пробует варианты и возвращает самое длинное совпадение (OR + Longest Match)."""

    def __init__(self, *patterns: TokenPatternBase):
        self.patterns = patterns

    def match(self, flow: TokenFlow) -> Optional[List[Token]]:
        best_match: Optional[List[Token]] = None

        for pattern in self.patterns:
            matched = pattern.match(flow)
            if matched is not None:
                if best_match is None or len(matched) > len(best_match):
                    best_match = matched
        return best_match

    def __or__(self, other: TokenPatternBase) -> 'AlternativePattern':
        if isinstance(other, AlternativePattern):
            return AlternativePattern(*self.patterns, *other.patterns)
        return AlternativePattern(*self.patterns, other)


class OptionalPattern(TokenPatternBase):
    """Необязательный паттерн (0 или 1). Всегда успешен (возвращает [] если не совпал)."""

    def __init__(self, pattern: TokenPatternBase):
        self.pattern = pattern

    def match(self, flow: TokenFlow) -> Optional[List[Token]]:
        matched = self.pattern.match(flow)
        if matched is not None:
            return matched
        return [] 


class NotPattern(TokenPatternBase):
    """
    Паттерн отрицания (Negative Lookahead).
    Успешен, если вложенный паттерн НЕ совпадает с текущей позицией.
    Не потребляет токены (возвращает пустой список при успехе).
    """

    def __init__(self, pattern: TokenPatternBase):
        self.pattern = pattern

    def match(self, flow: TokenFlow) -> Optional[List[Token]]:
        if self.pattern.match(flow) is None:
            return []  
        return None  


class AndPattern(TokenPatternBase):
    """
    Паттерн логического И (Intersection).
    Успешен, если ВСЕ вложенные паттерны совпадают с текущей позицией.
    Возвращает самое длинное совпадение из всех вложенных паттернов.
    """

    def __init__(self, *patterns: TokenPatternBase):
        self.patterns = patterns

    def match(self, flow: TokenFlow) -> Optional[List[Token]]:
        if not self.patterns:
            return []

        longest_match: Optional[List[Token]] = None

        for pattern in self.patterns:
            matched = pattern.match(flow)
            if matched is None:
                return None
            
            if longest_match is None or len(matched) > len(longest_match):
                longest_match = matched

        return longest_match

    def __and__(self, other: TokenPatternBase) -> 'AndPattern':
        if isinstance(other, AndPattern):
            return AndPattern(*self.patterns, *other.patterns)
        return AndPattern(*self.patterns, other)
    
