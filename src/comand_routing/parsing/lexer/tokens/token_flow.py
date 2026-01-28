from typing import List, Union
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
    
    def pop_token(self, count: int = 1) -> Union[Token, List[Token]]:
        if count == 1:
            return self.popleft()
        return self.popleft() if count == 1 else [self.popleft() for _ in range(count)]
    
    @property
    def has_next(self) -> bool:
        return bool(self)
    
