from pathlib import Path
from . import db_package as db
from .command_handler import MainCommandHandler

DB_PATH = Path("media.db")
SCHEMA_PATH = Path("src/db_package/schema.sql")

print("Connection...")
DB = db.init(DB_PATH, SCHEMA_PATH)

print("App started.")

def action_list(db_conn, action):
    data = db.get_data(db_conn, action["target"])
    for r in data:
        print(dict(r))

def action_error(_, action):
    print(action["msg"])

def action_quit(db_conn, _):
    db.close(db_conn)
    raise SystemExit

main_handler = MainCommandHandler()

while True:
    try:
        user_input = input(">>> ")
    except KeyboardInterrupt:
        user_input = "quit"
    except EOFError:
        user_input = "quit"

    action = main_handler.handle(user_input)


    if action is None:
        continue

    func_name = "action_" + action["type"]
    handler = globals().get(func_name)

    if not handler:
        print("Unknown action type:", action["type"])
        continue

    try:
        handler(DB, action)
    except SystemExit:
        break
