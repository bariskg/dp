from __future__ import annotations

from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QMessageBox,
    QTextEdit,
    QVBoxLayout,
)


class NewFileDialog(QDialog):
    """Collect the minimum information required to create a new case file."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Yeni Bosanma Dosyasi")
        self.resize(480, 320)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Ornek: A.Y. Bosanma Dosyasi")

        self.case_type_input = QComboBox()
        self.case_type_input.addItems(["Anlasmali Bosanma", "Cekismeli Bosanma"])

        self.notes_input = QTextEdit()
        self.notes_input.setPlaceholderText("Kisa not veya aciklama ekleyebilirsiniz.")
        self.notes_input.setMaximumHeight(120)

        form = QFormLayout()
        form.addRow("Dosya Adi", self.name_input)
        form.addRow("Dava Tipi", self.case_type_input)
        form.addRow("Kisa Not", self.notes_input)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self._validate_and_accept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(buttons)

    def get_payload(self) -> dict[str, str]:
        """Return the sanitized dialog values."""
        return {
            "name": self.name_input.text().strip(),
            "case_type": self.case_type_input.currentText().strip(),
            "notes": self.notes_input.toPlainText().strip(),
        }

    def _validate_and_accept(self) -> None:
        if not self.name_input.text().strip():
            QMessageBox.warning(
                self,
                "Eksik Bilgi",
                "Devam etmek icin once dosya adini girmeniz gerekiyor.",
            )
            return
        self.accept()
