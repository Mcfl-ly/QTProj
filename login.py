from PySide6.QtWidgets import   QVBoxLayout, QGridLayout, QWidget, QPushButton, QMessageBox
from PySide6.QtCore import Qt
from textLine import TextBox
from button import Button
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

class LoginScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.create_db(login, password)
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
        self.button = Button('ENTRAR')
        self.password_textbox.returnPressed.connect(self.button.click)
        self.login_textbox.returnPressed.connect(self.button.click)

        self.button.clicked.connect(self.authenticate)

        #adicionando as caixas de texto a tela de login
        screen_layout.addWidget(self.login_textbox, alignment=Qt.AlignmentFlag.AlignCenter)
        screen_layout.addWidget(self.password_textbox, alignment=Qt.AlignmentFlag.AlignCenter)
        screen_layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)

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

    def go_to_page2(self):
        self.stacked_widget.setCurrentIndex(1)

    def create_db(self, login, password):
        db = sqlite3.connect('banco.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (ID INTEGER PRIMARY KEY AUTOINCREMENT, login VARCHAR(30), password VARCHAR(30), UNIQUE(login, password))")

        cursor.execute("CREATE TABLE IF NOT EXISTS filial ()")

        cursor.execute(f"INSERT OR IGNORE INTO users (login, password) VALUES ('{login}','{password}')")
        db.commit()

    def authenticate(self):
        login_input = self.login_textbox.text()
        password_input = self.password_textbox.text()

        db = sqlite3.connect('banco.db')
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM users WHERE login = '{login_input}' AND password = '{password_input}'")
        row = cursor.fetchone()
        if row:
            self.go_to_page2()
        else:
            msg_error = QMessageBox()
            msg_error.information(self, "Login Incorreto", "Login ou senha incorretos.")

