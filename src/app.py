from typing import Dict
from .command_handler import MainCommandHandler
from .command_executor import COMMANDS, CommandExecutor
from .config import DB_PATH, SCHEMA_PATH
from .user import User





class App:
    def __init__(self) -> None:
        self.user = User(DB_PATH, SCHEMA_PATH)
        self.running: bool = True
        self.commands: Dict[str, CommandExecutor] = {c.name: c for c in COMMANDS}

    def run(self) -> None:
        print("App started.")

        main_handler = MainCommandHandler()

        while self.running:
            try:
                user_input: str = input(">>> ")
            except KeyboardInterrupt:
                user_input: str = "quit"
            except EOFError:
                user_input: str = "quit"

            action = main_handler.handle(user_input)


            if action is None:
                continue

            if action["type"] == "error":
                print(action["msg"])
                continue

            handler = self.commands.get(action["type"])

            if not handler:
                print("Unknown action type:", action["type"])
                continue

            try:
                handler.execute(self.user, action)
            except SystemExit:
                break
