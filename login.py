from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout, QLabel, QSizePolicy, \
    QWidget, QLineEdit
from PySide6.QtCore import Qt
from textLine import TextBox



class LoginScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setFixedSize(540,360)
        self.setStyleSheet("background-color: transparent;")

        layout = QVBoxLayout()


        self.login_textbox = TextBox()
        self.login_textbox.setPlaceholderText("Login")

        self.password_textbox = TextBox()
        self.password_textbox.setPlaceholderText("Password")
        self.password_textbox.setEchoMode(TextBox.EchoMode.Password)



        layout.addWidget(self.login_textbox, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.password_textbox, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

