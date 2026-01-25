from abc import ABC, abstractmethod
from typing import Dict
from src.user import User





class CommandExecutor(ABC):
    name = ""
    
    @abstractmethod
    def execute(self, user: User, args: Dict[str, str]):
        ...
