#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from src.app import App
from src import commands


COMMANDS = {
    commands.ListCommand(),
    commands.QuitCommand(),
}

DB_PATH = Path("media.db")
SCHEMA_PATH = Path("src/db_package/schema.sql")

app = App(DB_PATH, SCHEMA_PATH, COMMANDS)

if __name__ == "__main__":
    app.run()
