from __future__ import annotations

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QTextEdit,
    QVBoxLayout,
)


class DraftDialog(QDialog):
    """Display the generated first-pass petition draft."""

    def __init__(self, file_record: dict, draft_text: str, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle(f"Dilekce Taslagi - {file_record['name']}")
        self.resize(820, 760)

        title = QLabel("Dilekce Taslagi")
        title.setStyleSheet("font-size: 18px; font-weight: 600;")

        subtitle = QLabel(
            "Bu ilk surumde taslak, girilen bilgilere ve secilen kaynak onerilerine "
            "gore sabit bir iskelet uzerinden olusturuluyor."
        )
        subtitle.setWordWrap(True)

        self.editor = QTextEdit()
        self.editor.setPlainText(draft_text)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        close_button = buttons.button(QDialogButtonBox.StandardButton.Close)
        close_button.setText("Kapat")
        close_button.clicked.connect(self.accept)

        layout = QVBoxLayout(self)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.editor)
        layout.addWidget(buttons)
