import sqlite3
from pathlib import Path


DB_PATH = Path("media.db")

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row

def list_works():
    cur = conn.cursor()
    cur.execute("SELECT * FROM works")
    return cur.fetchall()

def list_genres():
    cur = conn.cursor()
    cur.execute("SELECT * FROM genres")
    return cur.fetchall()

def add_work(data):
    conn.execute("""
        INSERT INTO works (title, original_title, native_title, type, release_year)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data["title"],
        data["original"],
        data["native"],
        data["type"],
        data["year"],
    ))
    conn.commit()
