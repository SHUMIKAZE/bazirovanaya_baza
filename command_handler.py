import shlex
#import db

def handle_list(args):
    if not args:
        print("Specify what to list: works or genres")
        return None

    if args[0] == "works":
        rows = "data"#db.list_works()
        return {"type": "table", "data": rows}

    if args[0] == "genres":
        rows = "data"#db.list_genres()
        return {"type": "table", "data": rows}

    print("Unknown list target") 
    return None

def handle_add(args):
    if not args:
        print("Specify what to add: work or genre")
        return None

    if args[0] == "work":
        title, original, native, wtype, year = args[1:]
        return {
                "type": "add_work",
                "data": {
                    "title": title,
                    "original": original,
                    "native": native,
                    "type": wtype,
                    "year": year,
                },
        }
    if args[0] == "genre":
        return {
            "type": "add_genre",
            "data": args[0],
        }

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

    if cmd == "list" and 0:
        return handle_list(args)

    if cmd == "add" and 0:
        return handle_add(args)

    if cmd.lower() in ("exit", "quit"):
        return {"type": cmd}

    print(f"Unknown command: {cmd}")
    return None
