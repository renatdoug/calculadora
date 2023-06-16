import sys
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs ) -> None:
        super().__init__(parent, *args, **kwargs)

        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)

        self.label1 = QLabel('Renato Douglas')
        self.v_layout.addWidget(self.label1)

        self.setCentralWidget(self.cw)