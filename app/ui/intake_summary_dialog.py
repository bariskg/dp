from __future__ import annotations

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QTextEdit,
    QVBoxLayout,
)


class IntakeSummaryDialog(QDialog):
    """Show a compact summary of intake data before the next workflow step."""

    def __init__(self, file_record: dict, intake_data: dict, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle(f"Ozet ve Kontrol - {file_record['name']}")
        self.resize(720, 640)

        title = QLabel("Ozet ve Kontrol")
        title.setStyleSheet("font-size: 18px; font-weight: 600;")

        subtitle = QLabel(
            "Kaynak onerilerine gecmeden once girilen bilgileri burada toplu halde "
            "inceleyebilirsiniz."
        )
        subtitle.setWordWrap(True)

        summary_text = QTextEdit()
        summary_text.setReadOnly(True)
        summary_text.setPlainText(self._build_summary(file_record, intake_data))

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel
        )
        ok_button = buttons.button(QDialogButtonBox.StandardButton.Ok)
        ok_button.setText("Onayla")
        cancel_button = buttons.button(QDialogButtonBox.StandardButton.Cancel)
        cancel_button.setText("Geri Don")

        buttons.accepted.connect(self._accept_if_valid)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(summary_text)
        layout.addWidget(buttons)

    def _accept_if_valid(self) -> None:
        self.accept()

    @staticmethod
    def _build_summary(file_record: dict, intake_data: dict) -> str:
        sections = [
            f"Dosya Adi: {file_record.get('name', '-')}",
            f"Dava Tipi: {intake_data.get('divorce_type') or file_record.get('case_type', '-')}",
            "",
            "Taraf Bilgileri",
            f"- Davaci etiketi: {intake_data.get('plaintiff_label') or '-'}",
            f"- Davali etiketi: {intake_data.get('defendant_label') or '-'}",
            "",
            "Aile Bilgileri",
            f"- Evlilik tarihi: {intake_data.get('marriage_date') or '-'}",
            f"- Fiili ayrilik: {intake_data.get('separation_status') or '-'}",
            f"- Ortak cocuk: {intake_data.get('has_children') or '-'}",
            "",
            "Talepler",
            f"- Velayet talebi: {intake_data.get('custody_request') or '-'}",
            f"- Nafaka talebi: {intake_data.get('alimony_request') or '-'}",
            f"- Tazminat talebi: {intake_data.get('compensation_request') or '-'}",
            "",
            "Olay Ozeti",
            intake_data.get("event_summary") or "-",
            "",
            "Delil Notlari",
            intake_data.get("evidence_notes") or "-",
        ]
        return "\n".join(sections)
