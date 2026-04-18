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

from app.services.db import create_file, list_files
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
            create_file(
                name=payload["name"],
                case_type=payload["case_type"],
                notes=payload["notes"],
            )
            self.refresh_file_list()
            self.status_label.setText(
                f"Yeni dosya olusturuldu: {payload['name']}"
            )

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
        """Show the selected file details until the next screen is built."""
        file_record = item.data(Qt.ItemDataRole.UserRole)
        if not file_record:
            return

        message = (
            f"Secilen dosya: {file_record['name']}\n"
            f"Dava tipi: {file_record['case_type']}\n"
            f"Durum: {file_record['status']}\n\n"
            "Bir sonraki adimda bu secim bilgi giris ekranini acacak."
        )
        QMessageBox.information(self, "Dosya Ac", message)
