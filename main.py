import db
import command_handler
import table_renderer

import subprocess

subprocess.run(["python", "db/init_db.py"])

print("App started.")

while True:
    try:
        user_input = input(">>> ")
    except KeyboardInterrupt:
        user_input = "quit"
    except EOFError:
        user_input = "exit"

    action = command_handler.handle(user_input)

    if action is None:
        continue

    if action["type"].lower() in ("exit", "quit"):
        break

    if action["type"] == "table":
        table_renderer.render(action["data"])

    if action["type"] == "add_work":
        db.add_work(action["data"])
