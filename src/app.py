from . import db_package
from .command_handler import MainCommandHandler
from .command_executor import COMMANDS

class App:
    def __init__(self, DB_PATH, SCHEMA_PATH):
        self.db = db_package
        self.media = self.db.init(DB_PATH, SCHEMA_PATH)
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
