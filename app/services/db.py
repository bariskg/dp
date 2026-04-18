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
    """
    CREATE TABLE IF NOT EXISTS intake_forms (
        file_id INTEGER PRIMARY KEY,
        divorce_type TEXT,
        plaintiff_label TEXT,
        defendant_label TEXT,
        marriage_date TEXT,
        separation_status TEXT,
        has_children TEXT,
        custody_request TEXT,
        alimony_request TEXT,
        compensation_request TEXT,
        event_summary TEXT,
        evidence_notes TEXT,
        updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (file_id) REFERENCES files (id) ON DELETE CASCADE
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
        file_id = int(cursor.lastrowid)
        connection.execute(
            """
            INSERT INTO intake_forms (
                file_id, divorce_type, plaintiff_label, defendant_label,
                separation_status, has_children, custody_request,
                alimony_request, compensation_request
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                file_id,
                case_type.strip(),
                "Davaci",
                "Davali",
                "Belirtilmedi",
                "Belirtilmedi",
                "Belirtilmedi",
                "Belirtilmedi",
                "Belirtilmedi",
            ),
        )
        connection.commit()
        return file_id


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


def get_file(file_id: int) -> dict[str, Any] | None:
    """Return a single file record by id."""
    with _connect() as connection:
        row = connection.execute(
            """
            SELECT id, name, case_type, status, notes, created_at, updated_at
            FROM files
            WHERE id = ?
            """,
            (file_id,),
        ).fetchone()
    return dict(row) if row else None


def get_intake_form(file_id: int) -> dict[str, Any]:
    """Return the saved intake form data for a file."""
    with _connect() as connection:
        row = connection.execute(
            """
            SELECT file_id, divorce_type, plaintiff_label, defendant_label,
                   marriage_date, separation_status, has_children,
                   custody_request, alimony_request, compensation_request,
                   event_summary, evidence_notes, updated_at
            FROM intake_forms
            WHERE file_id = ?
            """,
            (file_id,),
        ).fetchone()
    return dict(row) if row else {}


def save_intake_form(file_id: int, payload: dict[str, str]) -> None:
    """Persist the first-pass intake form for a file."""
    with _connect() as connection:
        connection.execute(
            """
            INSERT INTO intake_forms (
                file_id, divorce_type, plaintiff_label, defendant_label,
                marriage_date, separation_status, has_children,
                custody_request, alimony_request, compensation_request,
                event_summary, evidence_notes, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(file_id) DO UPDATE SET
                divorce_type = excluded.divorce_type,
                plaintiff_label = excluded.plaintiff_label,
                defendant_label = excluded.defendant_label,
                marriage_date = excluded.marriage_date,
                separation_status = excluded.separation_status,
                has_children = excluded.has_children,
                custody_request = excluded.custody_request,
                alimony_request = excluded.alimony_request,
                compensation_request = excluded.compensation_request,
                event_summary = excluded.event_summary,
                evidence_notes = excluded.evidence_notes,
                updated_at = CURRENT_TIMESTAMP
            """,
            (
                file_id,
                payload.get("divorce_type", "").strip(),
                payload.get("plaintiff_label", "").strip(),
                payload.get("defendant_label", "").strip(),
                payload.get("marriage_date", "").strip(),
                payload.get("separation_status", "").strip(),
                payload.get("has_children", "").strip(),
                payload.get("custody_request", "").strip(),
                payload.get("alimony_request", "").strip(),
                payload.get("compensation_request", "").strip(),
                payload.get("event_summary", "").strip(),
                payload.get("evidence_notes", "").strip(),
            ),
        )
        connection.execute(
            """
            UPDATE files
            SET updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (file_id,),
        )
        connection.commit()
