from __future__ import annotations

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QTextEdit,
    QVBoxLayout,
)


class SourceSuggestionsDialog(QDialog):
    """Display first-pass statute and decision suggestions."""

    def __init__(
        self,
        file_record: dict,
        intake_data: dict,
        suggestions: dict[str, list[dict[str, str]]],
        parent=None,
    ) -> None:
        super().__init__(parent)
        self.setWindowTitle(f"Kaynak Onerileri - {file_record['name']}")
        self.resize(760, 680)

        title = QLabel("Kaynak Onerileri")
        title.setStyleSheet("font-size: 18px; font-weight: 600;")

        subtitle = QLabel(
            "Bu ilk surumde oneriler test verileri ve temel kurallarla olusturuluyor. "
            "Bir sonraki adimda bunlari secilebilir hale getirip gercek veriyle besleyecegiz."
        )
        subtitle.setWordWrap(True)

        info = QLabel(
            f"Dosya: {file_record.get('name', '-')} | Bosanma tipi: "
            f"{intake_data.get('divorce_type') or file_record.get('case_type', '-')}"
        )
        info.setWordWrap(True)

        text = QTextEdit()
        text.setReadOnly(True)
        text.setPlainText(self._build_text(suggestions))

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        buttons.rejected.connect(self.reject)
        close_button = buttons.button(QDialogButtonBox.StandardButton.Close)
        close_button.setText("Kapat")
        close_button.clicked.connect(self.accept)

        layout = QVBoxLayout(self)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(info)
        layout.addWidget(text)
        layout.addWidget(buttons)

    @staticmethod
    def _build_text(suggestions: dict[str, list[dict[str, str]]]) -> str:
        lines: list[str] = ["Mevzuat Onerileri"]
        for item in suggestions.get("statutes", []):
            lines.extend(
                [
                    f"- {item['title']}",
                    f"  Dayanak: {item['reference']}",
                    f"  Neden secildi: {item['reason']}",
                    "",
                ]
            )

        lines.append("Karar Onerileri")
        for item in suggestions.get("decisions", []):
            lines.extend(
                [
                    f"- {item['title']}",
                    f"  Dayanak: {item['reference']}",
                    f"  Neden secildi: {item['reason']}",
                    "",
                ]
            )

        return "\n".join(lines).strip()
