import shlex

def handle_list(args):
    if args[0] == "works":
        return {
            "type": "list",
            "target": "works"
        }
    if args[0] == "genres":
        return {
            "type": "list",
            "target": "genres"
        }
        
    return {
        "type": "error",
        "msg": f"Unknown argument {args[0]}"
    }


def handle(cmd_str):
    try:
        parts = shlex.split(cmd_str)
    except ValueError:
        return {
            "type": "error",
            "msg": "Parse error"
        }

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

    if cmd == "list":
        if args:
            return handle_list(args)
        else:
            return {
                "type": "error",
                "msg": "What to list, works or genres?"
            }

    return {
        "type": "error",
        "msg": f"Unknown command: {cmd}"
    }
