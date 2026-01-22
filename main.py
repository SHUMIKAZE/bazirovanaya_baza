from pathlib import Path
import db_package as db
from command_handler import handle


DB_PATH = Path("media.db")
SCHEMA_PATH = Path("db_package/schema.sql")

print("Connection...")
DB = db.init(DB_PATH, SCHEMA_PATH)

print("App started.")

while True:
    try:
        user_input = input(">>> ")
    except KeyboardInterrupt:
        user_input = "quit"
    except EOFError:
        user_input = "quit"

    action = handle(user_input)

    if action is None:
        continue

    if action["type"] == "list":
        data = db.get_data(DB, action["target"])
        print(dict(data[0]))

    if action["type"] == "error":
        print(action["msg"])

    if action["type"] == "quit":
        db.close(DB)
        break
