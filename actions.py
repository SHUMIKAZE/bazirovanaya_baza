import db_package as db

def action_list(db_conn, action):
    data = db.get_data(db_conn, action["target"])
    for r in data:
        print(dict(r))

def action_error(_, action):
    print(action["msg"])

def action_quit(db_conn, _):
    db.close(db_conn)
    raise SystemExit
