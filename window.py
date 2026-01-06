import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QGridLayout
from PySide6.QtCore import Qt
from login import LoginScreen
from add_src_screen import AddSrc


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1080, 720)
        self.showMaximized()
        self.setWindowTitle("QTProj")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login = LoginScreen(self.stacked_widget)
        self.addSrc = AddSrc(self.stacked_widget)
        # self.login.setFixedSize(540, 170))

        #tela1
        container = QWidget()
        container.setObjectName("container")

        layout = QVBoxLayout(container)

        layout.addStretch()
        layout.addWidget(self.login, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()

        #tela2
        container2 = QWidget()
        container2.setObjectName("container")

        layout = QVBoxLayout(container2)

        layout.addStretch()
        layout.addWidget(self.addSrc, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()

        #adiciona o login a lista de paginas e define como a primeira
        self.stacked_widget.addWidget(container)
        self.stacked_widget.addWidget(container2)
        self.stacked_widget.setCurrentIndex(0)

        self.show()






