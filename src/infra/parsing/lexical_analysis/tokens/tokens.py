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
    priority: ClassVar[int] = -1

class WhitespaceToken(_BaseToken):
    pattern: ClassVar[re.Pattern[str]] = re.compile(r'^\s+')
    priority: ClassVar[int] = 0
    should_ignore: ClassVar[bool] = True

class IdentifierToken(_BaseToken):
    pattern: ClassVar[re.Pattern[str]] = re.compile(r'^[a-zA-Z][a-zA-Z0-9._-]*')
    priority: ClassVar[int] = 1

class LongFlagToken(_BaseToken):
    pattern: ClassVar[re.Pattern[str]] = re.compile(r'^--[a-zA-Z]+(?:-[a-zA-Z]+)*')
    priority: ClassVar[int] = 2

    def _process_value(self, match):
        return match.replace('--', '')


class ShortFlagToken(_BaseToken):
    pattern: ClassVar[re.Pattern[str]] = re.compile(r'^-[a-zA-Z]+')
    priority: ClassVar[int] = 2

    def _process_value(self, match):
        return match.replace('-', '')

class EqualsToken(_BaseToken):
    pattern: ClassVar[re.Pattern[str]] = re.compile(r'^=')
    priority: ClassVar[int] = 3

class StringToken(_BaseToken):
    pattern: ClassVar[re.Pattern[str]] = re.compile(r'^"(?:[^"\\]|\\.)*"|^\'(?:[^\'\\]|\\.)*\'')
    priority: ClassVar[int] = 4

    def _process_value(self, match: str) -> str:
        return match[1:-1]
