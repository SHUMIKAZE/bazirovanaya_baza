from enum import Enum

from .tokens import (
    WhitespaceToken,
    IdentifierToken,
    LongFlagToken,
    ShortFlagToken,
    EqualsToken,
    StringToken,
    EOFToken,
    Token,
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
    EOF = EOFToken

# Inject token_type into token classes automatically
for token_enum in TokenType:
    token_enum.value.token_type = token_enum
