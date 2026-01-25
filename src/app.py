from .database import Database
from .command_handler import MainCommandHandler
from .command_executor import COMMANDS
from .config import DB_PATH, SCHEMA_PATH


class App:
    def __init__(self):
        self.db = Database(DB_PATH, SCHEMA_PATH)
        self.db.media.connect()
        self.running = True
        self.commands = {c.name: c for c in COMMANDS}


    def run(self):
        print("App started.")


        main_handler = MainCommandHandler()

        while self.running:
            try:
                user_input = input(">>> ")
            except KeyboardInterrupt:
                user_input = "quit"
            except EOFError:
                user_input = "quit"

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
                handler.execute(self, action)
            except SystemExit:
                break
