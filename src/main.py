from pathlib import Path
from . import db_package as db
from .command_handler import MainCommandHandler

DB_PATH = Path("media.db")
SCHEMA_PATH = Path("src/db_package/schema.sql")

print("Connection...")
DB = db.init(DB_PATH, SCHEMA_PATH)

print("App started.")

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

    if action["type"] == "list":
        print(action["target"])

    if action["type"] == "error":
        print(action["msg"])

    if action["type"] == "quit":
        db.close(DB)
        break
