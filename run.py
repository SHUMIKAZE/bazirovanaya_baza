#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.app import App
from src.config import DB_PATH, SCHEMA_PATH



app = App(DB_PATH, SCHEMA_PATH)

if __name__ == "__main__":
    app.run()
