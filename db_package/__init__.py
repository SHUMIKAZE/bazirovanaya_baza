from .connection import connect, close

_connection = None

def init(db_path, schema_path):
    global _connection

    _connection = connect(db_path)
    with open(schema_path, "r", encoding="utf-8") as f:
        _connection.executescript(f.read())
    close(_connection)
    return _connection
