# Kurdi/db_create.py

import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()
    c.execute(
        """CREATE TABLE cards(
            card_id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            meaning TEXT NOT NULL,
            type TEXT NOT NULL,
            notes TEXT,
            category TEXT NOT NULL,
            views INTEGER,
            score DECIMAL
        )"""
    )
    c.execute(
        'INSERT INTO cards (word, meaning, type, notes, category)'
        'VALUES("Hataw", "Sun", "Noun", "You can also say rozh", "Weather")'
    )
