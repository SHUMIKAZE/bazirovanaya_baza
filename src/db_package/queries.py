def get_data(conn, table_key):
    QUERY_MAP = {
        'works': "SELECT * FROM works",
        'genres': "SELECT * FROM genres"
    }

    if table_key not in QUERY_MAP:
        raise ValueError(f"Key {table_key} is not found.")

    sql = QUERY_MAP[table_key]
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    return data
