from .atomics import TokenMatch
from .combinators import (
    SequencePattern, 
    AlternativePattern, 
    AndPattern,
    OptionalPattern,
    NotPattern,
)
from ...lexer.tokens.tokens_scheme import TokenType

__all__ = [
    'identifier_token',
    'long_flag_token',
    'short_flag_token',
    'equals_token',
    'string_token',
    'argument_token',
    'flag_token',
    'short_flag_with_arg',
    'long_flag_with_arg',
    'valid_flag',
]

identifier_token = TokenMatch(TokenType.IDENTIFIER)
long_flag_token = TokenMatch(TokenType.LONG_FLAG)
short_flag_token = TokenMatch(TokenType.SHORT_FLAG)
equals_token = TokenMatch(TokenType.EQUALS)
string_token = TokenMatch(TokenType.STRING)

argument_token = AlternativePattern(identifier_token, string_token)
flag_token = AlternativePattern(long_flag_token, short_flag_token)
short_flag_with_arg = SequencePattern(short_flag_token, equals_token, argument_token)
long_flag_with_arg = SequencePattern(long_flag_token, equals_token, argument_token)

valid_flag = AndPattern(
    NotPattern(short_flag_with_arg),
    AlternativePattern(flag_token, long_flag_with_arg),
)