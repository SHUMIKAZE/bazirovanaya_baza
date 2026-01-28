from typing import List, Optional, Union, Type
from enum import Enum

from ..exeptions.lexer import LexerError
from ._base import _LexerBase
from .tokens.tokens import Token, EOFToken
from .tokens.tokens_scheme import TokenType
from .tokens.token_hierarchy import TokenConflictResolver
from .tokens.token_flow import TokenFlow





class Lexer(_LexerBase):

    def __init__(
        self,
        tokens: Optional[List[Union[TokenType, Type[Token]]]] = None,
        additional_tokens: Optional[List[Union[TokenType, Type[Token]]]] = None,
        conflict_resolver: type[TokenConflictResolver] = TokenConflictResolver,
        eof_token: Type[Token] = EOFToken,
    ) -> None:
        if tokens is None:
            tokens = list(TokenType)
        
        combined_tokens = tokens + (additional_tokens or [])
        self._tokens = [t.value if isinstance(t, Enum) else t for t in combined_tokens]
        self._conflict_resolver = conflict_resolver
        self._eof_token = eof_token
        self._original_cmd: Optional[str] = None


    def tokenize(self, cmd: str) -> TokenFlow:
        flow = TokenFlow()
        self._original_cmd = cmd

        while cmd:

            matched_tokens = self._get_matched_tokens(cmd)
            true_token = self._conflict_resolver.resolve(matched_tokens)

            if not true_token.should_ignore:
                flow.insert_tokens(true_token)

            cmd = cmd[len(true_token):]

        else:
            flow.insert_tokens(self._eof_token())

        self._original_cmd = None
        return flow

    def _get_matched_tokens(self, cmd: str) -> List[Token]:
        matched_tokens = []

        assert self._original_cmd is not None

        if not cmd:
            return []

        for token_cls in self._tokens:
            match = token_cls.pattern.match(cmd)
            if match:
                matched_tokens.append(token_cls(match.group(0)))

        if not matched_tokens:
            error_position = len(self._original_cmd) - len(cmd)
            raise LexerError(
                message="Lexical analysis failed: No matching token found",
                source=self._original_cmd,
                position=error_position,
                unparsed_suffix=cmd
            )

        return matched_tokens