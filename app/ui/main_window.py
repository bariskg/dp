from __future__ import annotations

from PySide6.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    """Initial shell window for the divorce-law MVP."""

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
            "Bu ilk iskelet surumudur. Siradaki adimda ana ekran, dosya olusturma "
            "ve bilgi giris akislarini ekleyecegiz."
        )
        subtitle.setWordWrap(True)

        new_file_button = QPushButton("Yeni Bosanma Dosyasi")
        new_file_button.setEnabled(False)

        open_file_button = QPushButton("Kayitli Dosyayi Ac")
        open_file_button.setEnabled(False)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(new_file_button)
        layout.addWidget(open_file_button)
        layout.addStretch()

        self.setCentralWidget(container)
