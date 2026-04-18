from __future__ import annotations

from pathlib import Path

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QMessageBox,
    QTextEdit,
    QVBoxLayout,
)

from app.services.export import ExportDependencyError, export_docx, export_pdf


class DraftDialog(QDialog):
    """Display the generated first-pass petition draft."""

    def __init__(self, file_record: dict, draft_text: str, parent=None) -> None:
        super().__init__(parent)
        self.file_record = file_record
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

        buttons = QDialogButtonBox()
        self.export_docx_button = buttons.addButton(
            "Word Aktar", QDialogButtonBox.ButtonRole.ActionRole
        )
        self.export_pdf_button = buttons.addButton(
            "PDF Aktar", QDialogButtonBox.ButtonRole.ActionRole
        )
        buttons.addButton(QDialogButtonBox.StandardButton.Close)

        self.export_docx_button.clicked.connect(self.handle_export_docx)
        self.export_pdf_button.clicked.connect(self.handle_export_pdf)
        close_button = buttons.button(QDialogButtonBox.StandardButton.Close)
        close_button.setText("Kapat")
        close_button.clicked.connect(self.accept)

        layout = QVBoxLayout(self)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.editor)
        layout.addWidget(buttons)

    def handle_export_docx(self) -> None:
        self._run_export("word")

    def handle_export_pdf(self) -> None:
        self._run_export("pdf")

    def _run_export(self, export_type: str) -> None:
        try:
            if export_type == "word":
                path = export_docx(
                    file_name=self.file_record["name"],
                    draft_text=self.editor.toPlainText(),
                )
            else:
                path = export_pdf(
                    file_name=self.file_record["name"],
                    draft_text=self.editor.toPlainText(),
                )
        except ExportDependencyError as exc:
            QMessageBox.warning(self, "Eksik Paket", str(exc))
            return
        except Exception as exc:  # pragma: no cover - defensive UI error path
            QMessageBox.critical(
                self,
                "Export Hatasi",
                f"Belge disa aktarilirken beklenmeyen bir hata olustu:\n{exc}",
            )
            return

        QMessageBox.information(
            self,
            "Export Tamamlandi",
            f"Belge olusturuldu:\n{Path(path)}",
        )
