from __future__ import annotations

import sys

from app.services.db import initialize_database
from app.services.storage import ensure_data_directories


def main() -> int:
    ensure_data_directories()
    initialize_database()

    try:
        from PySide6.QtWidgets import QApplication
    except ImportError:
        print(
            "PySide6 is not installed. Run `pip install -r requirements.txt` first.",
            file=sys.stderr,
        )
        return 1

    from app.ui.main_window import MainWindow

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
