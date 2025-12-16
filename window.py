import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QGridLayout
from PySide6.QtCore import Qt
from login import LoginScreen


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1080, 720)
        self.showMaximized()
        self.setWindowTitle("QTProj")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login = LoginScreen(self.stacked_widget)
        # self.login.setFixedSize(540, 170)

        container = QWidget()
        container.setObjectName("container")

        layout = QVBoxLayout(container)

        layout.addStretch()
        layout.addWidget(self.login, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()

        #adiciona o login a lista de paginas e define como a primeira
        self.stacked_widget.addWidget(container)
        self.stacked_widget.setCurrentIndex(0)
        self.show()






