from ._base import _BaseToken
from typing import ClassVar
import re

__all__ = [
    'WhitespaceToken',
    'IdentifierToken',
    'LongFlagToken',
    'ShortFlagToken',
    'EqualsToken',
    'StringToken',
    'Token'
]
Token = _BaseToken

class EOFToken(_BaseToken):
    pattern: ClassVar[re.Pattern[str]] = re.compile(r'(?!)')

class WhitespaceToken(_BaseToken):
    pattern: ClassVar[re.Pattern[str]] = re.compile(r'^\s+')

class IdentifierToken(_BaseToken):
    pattern: ClassVar[re.Pattern[str]] = re.compile(r'^[a-zA-Z][a-zA-Z0-9._-]*')

class LongFlagToken(_BaseToken):
    pattern: ClassVar[re.Pattern[str]] = re.compile(r'^--[a-zA-Z]+(?:-[a-zA-Z]+)*')

    def _process_value(self, match):
        return match.replace('--', '')


class ShortFlagToken(_BaseToken):
    pattern: ClassVar[re.Pattern[str]] = re.compile(r'^-[a-zA-Z]+')

    def _process_value(self, match):
        return match.replace('-', '')

class EqualsToken(_BaseToken):
    pattern: ClassVar[re.Pattern[str]] = re.compile(r'^=')

class StringToken(_BaseToken):
    pattern: ClassVar[re.Pattern[str]] = re.compile(r'^"(?:[^"\\]|\\.)*"|^\'(?:[^\'\\]|\\.)*\'')

    def _process_value(self, match: str) -> str:
        return match[1:-1]
