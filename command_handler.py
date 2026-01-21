import shlex

def handle(cmd_str):
    try:
        parts = shlex.split(cmd_str)
    except ValueError:
        print("Parse error")
        return None

    if not parts:
        return None

    cmd = parts[0]
    args = parts[1:]


    if cmd == "quit":
        if args:
            return {
                "type": "error",
                "msg": f"Unknown argument {args[0]}"
            }
        else:
            return {"type": "quit"}

    return {
        "type": "error",
        "msg": f"Unknown command: {cmd}"
    }
