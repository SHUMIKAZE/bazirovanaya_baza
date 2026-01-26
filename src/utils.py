def get_user_input():

    try:
        user_input: str = input(">>> ")
    except KeyboardInterrupt:
        close_app()
    except EOFError:
        close_app()
    
    
    return user_input


def close_app():
    print("\nApp closed.")
    raise SystemExit