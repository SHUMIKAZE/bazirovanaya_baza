def handle_list(args):
    if not args:
        print("Specify what to list: works or genres")
        return None

    if args[0] == "works":
        rows = args[0]
        return {"type": "table", "data": rows}

    elif args[0] == "genres":
        rows = args[0]
        return {"type": "table", "data": rows}

    print("Unknown list target") 
    return None

def handle(cmd_str):
    parts = cmd_str.split()
    if not parts:
        return None

    cmd = parts[0]
    args = parts[1:]

    if cmd == "list":
        return handle_list(args)

    if cmd.lower() in ("exit", "quit"):
        return {"type": cmd}

    print(f"Unknown command: {cmd}")
    return None

if __name__ == "__main__":
    print("fuck all of you")
