from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt

class Button(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setFixedSize(100,50)
        self.setStyleSheet("QPushButton {background-color: none;"
                           "border-radius: 15;"
                           "font-weight: 650;"
                           "font-size: 13px;"
                           "font-family: Lucida Console;"
                           "letter-spacing: 2px;"
                           "border: 1px solid #ff1d8d;}"
                           
                           "QPushButton:hover{"
                           "background-color: #ff8da1;}"
                           
                           "QPushButton:pressed{"
                           "background-color: #ff1d8d;"
                           "}"
                           )