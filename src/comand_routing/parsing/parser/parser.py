from typing import Optional


from ..lexer.lexer import Lexer
from ..lexer.tokens.token_flow import TokenFlow
from ..lexer.tokens.tokens_scheme import TokenType
from ..models.command import Command
from ..exeptions.parser import ParserError
from .patterns.patterns import (
    identifier_token,
    long_flag_token,
    short_flag_token,
    equals_token,
    string_token,
    argument_token,
    flag_token,
    short_flag_with_arg,
    long_flag_with_arg,
    valid_flag,
)


class CommandParser:
    def __init__(
        self, 
        lexer: Lexer = Lexer(),
    ):
        self._lexer = lexer
        self._original_cmd: Optional[str] = None


    def parse_command(self, cmd: str):
        pass
