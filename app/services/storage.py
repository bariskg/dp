from __future__ import annotations

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
EXPORTS_DIR = DATA_DIR / "exports"
DATABASE_PATH = DATA_DIR / "dp.sqlite3"


def ensure_data_directories() -> None:
    """Create the local data directories used by the desktop app."""
    for path in (DATA_DIR, RAW_DIR, EXPORTS_DIR):
        path.mkdir(parents=True, exist_ok=True)
