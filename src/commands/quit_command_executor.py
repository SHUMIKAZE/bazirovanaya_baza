from typing import Dict
from src.user import User
from .base import CommandExecutor





class QuitCommand(CommandExecutor):
    name = "quit"

    def execute(self, user: User, args: Dict[str, str]) -> None:
        if user.db.media.conn is None:
            raise ValueError("DB is not connected.")

        user.db.media.conn.close()
        print(args["msg"])
        raise SystemExit
