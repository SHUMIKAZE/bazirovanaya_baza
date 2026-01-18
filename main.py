import command_handler
import table_renderer

import subprocess

subprocess.run(["python", "db/init_db.py"])

print("App started.")

while True:
    user_input = input(">>> ")
    if user_input.lower() in ("exit", "quit"):
        break

    result = command_handler.handle(user_input)

    if result is not None:
        table_renderer.render(result)
