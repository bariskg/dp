from __future__ import annotations

from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QTextEdit,
    QVBoxLayout,
)


class FileIntakeDialog(QDialog):
    """Edit the first-pass intake information for a divorce file."""

    def __init__(self, file_record: dict, intake_data: dict, parent=None) -> None:
        super().__init__(parent)
        self.file_record = file_record
        self.setWindowTitle(f"Bilgi Girisi - {file_record['name']}")
        self.resize(680, 620)

        header = QLabel(
            f"Dosya: {file_record['name']} | Dava tipi: {file_record['case_type']}"
        )
        header.setWordWrap(True)
        header.setStyleSheet("font-size: 16px; font-weight: 600;")

        self.divorce_type_input = QComboBox()
        self.divorce_type_input.addItems(["Anlasmali Bosanma", "Cekismeli Bosanma"])
        self._set_combo_value(
            self.divorce_type_input,
            intake_data.get("divorce_type") or file_record["case_type"],
        )

        self.plaintiff_input = QLineEdit(
            intake_data.get("plaintiff_label") or "Davaci"
        )
        self.defendant_input = QLineEdit(
            intake_data.get("defendant_label") or "Davali"
        )
        self.marriage_date_input = QLineEdit(intake_data.get("marriage_date") or "")
        self.marriage_date_input.setPlaceholderText("Ornek: 14.06.2019")

        self.separation_status_input = QComboBox()
        self.separation_status_input.addItems(
            ["Belirtilmedi", "Birlikte Yasiyorlar", "Fiilen Ayrilar"]
        )
        self._set_combo_value(
            self.separation_status_input,
            intake_data.get("separation_status") or "Belirtilmedi",
        )

        self.has_children_input = QComboBox()
        self.has_children_input.addItems(["Belirtilmedi", "Evet", "Hayir"])
        self._set_combo_value(
            self.has_children_input,
            intake_data.get("has_children") or "Belirtilmedi",
        )

        self.custody_request_input = QComboBox()
        self.custody_request_input.addItems(["Belirtilmedi", "Evet", "Hayir"])
        self._set_combo_value(
            self.custody_request_input,
            intake_data.get("custody_request") or "Belirtilmedi",
        )

        self.alimony_request_input = QComboBox()
        self.alimony_request_input.addItems(["Belirtilmedi", "Evet", "Hayir"])
        self._set_combo_value(
            self.alimony_request_input,
            intake_data.get("alimony_request") or "Belirtilmedi",
        )

        self.compensation_request_input = QComboBox()
        self.compensation_request_input.addItems(["Belirtilmedi", "Evet", "Hayir"])
        self._set_combo_value(
            self.compensation_request_input,
            intake_data.get("compensation_request") or "Belirtilmedi",
        )

        self.event_summary_input = QTextEdit(intake_data.get("event_summary") or "")
        self.event_summary_input.setPlaceholderText(
            "Bosanma gerekcesini ve olaylarin kisaca nasil gelistigini yazin."
        )

        self.evidence_notes_input = QTextEdit(intake_data.get("evidence_notes") or "")
        self.evidence_notes_input.setPlaceholderText(
            "Varsa tanik, mesaj, belge veya diger delil notlarini yazin."
        )

        form = QFormLayout()
        form.addRow("Bosanma Tipi", self.divorce_type_input)
        form.addRow("Davaci Etiketi", self.plaintiff_input)
        form.addRow("Davali Etiketi", self.defendant_input)
        form.addRow("Evlilik Tarihi", self.marriage_date_input)
        form.addRow("Fiili Ayrilik", self.separation_status_input)
        form.addRow("Ortak Cocuk", self.has_children_input)
        form.addRow("Velayet Talebi", self.custody_request_input)
        form.addRow("Nafaka Talebi", self.alimony_request_input)
        form.addRow("Tazminat Talebi", self.compensation_request_input)
        form.addRow("Olay Ozeti", self.event_summary_input)
        form.addRow("Delil Notlari", self.evidence_notes_input)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self._validate_and_accept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addWidget(header)
        layout.addLayout(form)
        layout.addWidget(buttons)

    def get_payload(self) -> dict[str, str]:
        """Return sanitized intake form values."""
        return {
            "divorce_type": self.divorce_type_input.currentText().strip(),
            "plaintiff_label": self.plaintiff_input.text().strip(),
            "defendant_label": self.defendant_input.text().strip(),
            "marriage_date": self.marriage_date_input.text().strip(),
            "separation_status": self.separation_status_input.currentText().strip(),
            "has_children": self.has_children_input.currentText().strip(),
            "custody_request": self.custody_request_input.currentText().strip(),
            "alimony_request": self.alimony_request_input.currentText().strip(),
            "compensation_request": self.compensation_request_input.currentText().strip(),
            "event_summary": self.event_summary_input.toPlainText().strip(),
            "evidence_notes": self.evidence_notes_input.toPlainText().strip(),
        }

    def _validate_and_accept(self) -> None:
        if not self.event_summary_input.toPlainText().strip():
            QMessageBox.warning(
                self,
                "Eksik Bilgi",
                "Devam etmek icin olay ozetini girmeniz gerekiyor.",
            )
            return
        self.accept()

    @staticmethod
    def _set_combo_value(combo: QComboBox, value: str) -> None:
        index = combo.findText(value)
        if index >= 0:
            combo.setCurrentIndex(index)
