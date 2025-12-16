from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout, QLabel, QSizePolicy, \
    QWidget, QLineEdit
from PySide6.QtCore import Qt
from textLine import TextBox



class LoginScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        #cria o layout geral do widget de login
        tela_layout = QGridLayout(self)
        tela_layout.setContentsMargins(0, 0, 0, 0)
        tela_layout.setSpacing(0)

        #aqui cria a telinha de login, a parte importante
        self.screen = QWidget()
        self.screen.setObjectName("screen")
        self.screen.setFixedSize(540,360)

        #cria o layout da telinha de login, colocando ele na vertical
        screen_layout = QVBoxLayout(self.screen)
        screen_layout.setContentsMargins(24,24,24,24)
        screen_layout.setSpacing(16)

        #textos das caixas
        self.login_textbox = TextBox()
        self.login_textbox.setPlaceholderText("Login")
        self.password_textbox = TextBox()
        self.password_textbox.setPlaceholderText("Password")
        self.password_textbox.setEchoMode(TextBox.EchoMode.Password)

        #adicionando as caixas de texto a tela de login
        screen_layout.addWidget(self.login_textbox)
        screen_layout.addWidget(self.password_textbox)

        #adicionando a telinha de login ao widget inteiro e alinhando ao centro
        tela_layout.addWidget(self.screen,1,1,alignment=Qt.AlignmentFlag.AlignCenter)
        tela_layout.setRowStretch(0, 1)
        tela_layout.setRowStretch(2, 1)
        tela_layout.setColumnStretch(0, 1)
        tela_layout.setColumnStretch(2, 1)

        self.setStyleSheet("background-color: yellow;")

        self.setStyleSheet("""
                   QWidget { background-color: #1e1e1e; }
                   #screen {
                       background-color: transparent;
                       border-radius: 12px;
                       border: 2px solid #ff1d8d;
                   }
               """)
