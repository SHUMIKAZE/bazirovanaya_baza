from typing import List
from collections import deque

from .tokens import Token

class TokenFlow(deque):
    def __init__(self) -> None:
        super().__init__()

    @property
    def tokens(self):
        return self

    def insert_tokens(self, *tokens: Token) -> None:
        self.extend(tokens)

    def peek(self) -> Token:
        return self[0]
    
    def pop_token(self) -> Token:
        return super().popleft()
    
    def has_next(self) -> bool:
        return bool(self)
    
