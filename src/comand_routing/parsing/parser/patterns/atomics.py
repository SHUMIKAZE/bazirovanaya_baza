from typing import List, Optional

from ...lexer.tokens.token_flow import TokenFlow
from ...lexer.tokens.tokens import Token
from ...lexer.tokens.tokens_scheme import TokenType
from .base import TokenPatternBase


class TokenMatch(TokenPatternBase):
    """Паттерн, ожидающий один конкретный тип токена."""
    
    def __init__(self, token_type: TokenType):
        self.token_type = token_type

    def match(self, flow: TokenFlow) -> Optional[List[Token]]:
        if not flow:
            return None
        
        token = flow.peek()
        if token.token_type == self.token_type:
            return [token]
        return None