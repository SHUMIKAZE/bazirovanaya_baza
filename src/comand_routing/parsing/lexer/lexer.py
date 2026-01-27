from typing import List, Optional

from ..exeptions.lexer import LexerError
from ._base import _LexerBase
from .tokens.tokens import Token
from .tokens.tokens_scheme import TokenType
from .tokens.token_hierarchy import TokenConflictResolver
from .tokens.token_flow import TokenFlow





class Lexer(_LexerBase):

    def __init__(
        self,
        tokens: List[TokenType] = list(TokenType),
        conflict_resolver: type[TokenConflictResolver] = TokenConflictResolver,
    ):
        self._tokens = tokens
        self._conflict_resolver = conflict_resolver
        self._original_cmd: Optional[str] = None


    def tockenize(self, cmd: str) -> TokenFlow:
        flow = TokenFlow()
        self._original_cmd = cmd

        while cmd:

            matched_tokens = self._get_matched_tokens(cmd)
            true_token = self._conflict_resolver.resolve(matched_tokens)

            flow.insert_tokens(true_token)
            cmd = cmd[len(true_token):]


        self._original_cmd = None
        return flow
        

    def _get_matched_tokens(self, cmd: str) -> List[Token]:
        matched_tokens = []

        if not cmd:
            return []

        for token_type in self._tokens:
            token_cls = token_type.value
            match = token_cls.pattern.match(cmd)
            if match:
                matched_tokens.append(token_cls(match.group(0)))

        if not matched_tokens:
            error_position = len(self._original_cmd) - len(cmd)               # type: ignore
            raise LexerError(
                message="Lexical analysis failed: No matching token found",
                source=self._original_cmd,                                    # type: ignore
                position=error_position,
                unparsed_suffix=cmd
            )

        return matched_tokens