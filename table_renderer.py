def render(rows):
    if not rows:
        print("(empty)")
        return

    headers = rows[0].keys()
    print(" | ".join(headers))
    print("-" * 80)

    for r in rows:
        print(" | ".join([str(r[h]) for h in headers]))
