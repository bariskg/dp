from __future__ import annotations

import sqlite3

from app.services.storage import DATABASE_PATH


SCHEMA_STATEMENTS = (
    """
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        case_type TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'draft',
        notes TEXT,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """,
)


def initialize_database() -> None:
    """Initialize the local SQLite database for the MVP."""
    with sqlite3.connect(DATABASE_PATH) as connection:
        # OneDrive-backed folders can be sensitive to temporary journal files.
        connection.execute("PRAGMA journal_mode=MEMORY")
        connection.execute("PRAGMA temp_store=MEMORY")
        for statement in SCHEMA_STATEMENTS:
            connection.execute(statement)
        connection.commit()
