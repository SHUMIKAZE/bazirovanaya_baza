from typing import Dict
from src.user import User
from .base import CommandExecutor





class ListCommand(CommandExecutor):
    name = "list"

    def execute(self, user: User, args: Dict[str, str]) -> None:
        data = user.db.get_list.execute(args)
        for r in data:
            print(dict(r))
