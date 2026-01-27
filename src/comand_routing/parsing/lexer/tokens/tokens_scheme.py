from enum import Enum

from .tokens import (
    WhitespaceToken,
    IdentifierToken,
    LongFlagToken,
    ShortFlagToken,
    EqualsToken,
    StringToken
)

__all__ = [
    'TokenType'
]

class TokenType(Enum):
    WHITESPACE = WhitespaceToken
    IDENTIFIER = IdentifierToken
    LONG_FLAG = LongFlagToken
    SHORT_FLAG = ShortFlagToken
    EQUALS = EqualsToken
    STRING = StringToken



