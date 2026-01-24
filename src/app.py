from os import sched_yield
from . import db_package
from .command_handler import MainCommandHandler

def action_list(db_conn, action):
    data = db_package.get_data(db_conn, action["target"])
    for r in data:
        print(dict(r))

def action_error(_, action):
    print(action["msg"])

def action_quit(db_conn, _):
    db_package.close(db_conn)
    raise SystemExit

class App:
    def __init__(self, DB_PATH, SCHEMA_PATH):
        self.db = db_package
        self.media = self.db.init(DB_PATH, SCHEMA_PATH)
        self.running = True
        self.commands = {
            "list": action_list,
            "quit": action_quit,
            "error": action_error,
        }


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

            handler = self.commands.get(action["type"])
            if not handler:
                continue

            if not handler:
                print("Unknown action type:", action["type"])
                continue

            try:
                handler(self.media, action)
            except SystemExit:
                break
