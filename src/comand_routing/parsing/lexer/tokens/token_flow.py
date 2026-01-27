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
    
    def next(self) -> Token:
        return self.popleft()

    def peek(self) -> Token:
        return self[0]