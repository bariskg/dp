from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.services.db import (
    create_file,
    get_file,
    get_intake_form,
    list_files,
    save_intake_form,
)
from app.ui.file_intake_dialog import FileIntakeDialog
from app.ui.intake_summary_dialog import IntakeSummaryDialog
from app.ui.new_file_dialog import NewFileDialog


class MainWindow(QMainWindow):
    """Initial working window for the divorce-law MVP."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("dp - Bosanma MVP")
        self.resize(960, 640)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(32, 32, 32, 32)
        layout.setSpacing(16)

        title = QLabel("Bosanma Dosyasi Yardimcisi")
        title.setStyleSheet("font-size: 24px; font-weight: 600;")

        subtitle = QLabel(
            "Bosanma dosyalarinizi buradan olusturabilir ve kayitli dosyalari "
            "yeniden acabilirsiniz."
        )
        subtitle.setWordWrap(True)

        self.new_file_button = QPushButton("Yeni Bosanma Dosyasi")
        self.new_file_button.clicked.connect(self.open_new_file_dialog)

        self.open_file_button = QPushButton("Kayitli Dosyayi Ac")
        self.open_file_button.clicked.connect(self.show_open_file_message)

        self.status_label = QLabel("Heniz dosya olusturulmadi.")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.file_list = QListWidget()
        self.file_list.itemDoubleClicked.connect(self.open_selected_file)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.new_file_button)
        layout.addWidget(self.open_file_button)
        layout.addWidget(self.status_label)
        layout.addWidget(self.file_list, 1)

        self.setCentralWidget(container)
        self.refresh_file_list()

    def refresh_file_list(self) -> None:
        """Reload the recent file list from the local database."""
        self.file_list.clear()
        files = list_files()

        if not files:
            self.status_label.setText("Henuz kayitli bosanma dosyasi yok.")
            self.open_file_button.setEnabled(False)
            placeholder = QListWidgetItem(
                "Kayitli dosya bulunamadi. Yeni Bosanma Dosyasi ile baslayin."
            )
            placeholder.setFlags(Qt.ItemFlag.NoItemFlags)
            self.file_list.addItem(placeholder)
            return

        self.status_label.setText(f"{len(files)} kayitli bosanma dosyasi bulundu.")
        self.open_file_button.setEnabled(True)

        for file_record in files:
            item = QListWidgetItem(
                f"{file_record['name']} | {file_record['case_type']} | "
                f"Durum: {file_record['status']}"
            )
            item.setData(Qt.ItemDataRole.UserRole, file_record)
            self.file_list.addItem(item)

    def open_new_file_dialog(self) -> None:
        """Open the dialog used to create a new divorce case file."""
        dialog = NewFileDialog(self)
        if dialog.exec():
            payload = dialog.get_payload()
            file_id = create_file(
                name=payload["name"],
                case_type=payload["case_type"],
                notes=payload["notes"],
            )
            self.refresh_file_list()
            self.status_label.setText(
                f"Yeni dosya olusturuldu: {payload['name']}"
            )
            self.open_file_by_id(file_id)

    def show_open_file_message(self) -> None:
        """Explain that the detail screen is the next implementation step."""
        current_item = self.file_list.currentItem()
        if current_item is None:
            QMessageBox.information(
                self,
                "Dosya Secin",
                "Devam etmek icin once listeden bir dosya secin.",
            )
            return
        self.open_selected_file(current_item)

    def open_selected_file(self, item: QListWidgetItem) -> None:
        """Open the first-pass intake form for the selected file."""
        file_record = item.data(Qt.ItemDataRole.UserRole)
        if not file_record:
            return
        self.open_file_by_id(int(file_record["id"]))

    def open_file_by_id(self, file_id: int) -> None:
        """Load the selected file and open its intake form dialog."""
        file_record = get_file(file_id)
        if not file_record:
            QMessageBox.warning(
                self,
                "Dosya Bulunamadi",
                "Secilen dosya bulunamadi. Liste yenilenip tekrar deneyin.",
            )
            self.refresh_file_list()
            return

        intake_data = get_intake_form(file_id)
        dialog = FileIntakeDialog(file_record=file_record, intake_data=intake_data, parent=self)
        if dialog.exec():
            payload = dialog.get_payload()
            save_intake_form(file_id, payload)
            self.refresh_file_list()
            summary_dialog = IntakeSummaryDialog(
                file_record=file_record,
                intake_data=payload,
                parent=self,
            )
            if summary_dialog.exec():
                self.status_label.setText(
                    f"Ozet onaylandi: {file_record['name']}"
                )
                QMessageBox.information(
                    self,
                    "Siradaki Adim",
                    "Bir sonraki adimda bu ozet ekranindan kaynak onerileri acilacak.",
                )
            else:
                self.status_label.setText(
                    f"Dosya guncellendi: {file_record['name']}"
                )
