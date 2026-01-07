from pathlib import Path
import subprocess

if not Path("media.db").exists():
    print("Database not found, initializing...")
    subprocess.run(["python", "db/init_db.py"])

print("App started.")
