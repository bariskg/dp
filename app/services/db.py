from __future__ import annotations

import sqlite3
from typing import Any

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


def _connect() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA journal_mode=MEMORY")
    connection.execute("PRAGMA temp_store=MEMORY")
    return connection


def initialize_database() -> None:
    """Initialize the local SQLite database for the MVP."""
    with _connect() as connection:
        for statement in SCHEMA_STATEMENTS:
            connection.execute(statement)
        connection.commit()


def create_file(name: str, case_type: str, notes: str = "") -> int:
    """Create a new case file and return its database id."""
    with _connect() as connection:
        cursor = connection.execute(
            """
            INSERT INTO files (name, case_type, notes)
            VALUES (?, ?, ?)
            """,
            (name.strip(), case_type.strip(), notes.strip()),
        )
        connection.commit()
        return int(cursor.lastrowid)


def list_files() -> list[dict[str, Any]]:
    """Return files ordered by most recent update."""
    with _connect() as connection:
        rows = connection.execute(
            """
            SELECT id, name, case_type, status, notes, created_at, updated_at
            FROM files
            ORDER BY datetime(updated_at) DESC, id DESC
            """
        ).fetchall()
    return [dict(row) for row in rows]
