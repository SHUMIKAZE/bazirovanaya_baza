def handle(user_input):
    parts = user_input.split()
    if not parts:
        return

    cmd = parts[0]
    args = parts[1:]

    if cmd == "list":
        if not args:
            print("Specify what to list: works or genres")
            return
        what = args[0]
        if what == "works":
            return "list_works"
        elif what == "genres":
            return "list_genres"
        else:
            print("Unknown list target")
            return
    else:
        print(f"Unknown command: {cmd}")
        return

if __name__ == "__main__":
    print("fuck all of you")
