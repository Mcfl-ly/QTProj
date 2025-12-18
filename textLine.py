from PySide6.QtWidgets import  QLineEdit

class TextBox(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 35)
        self.setStyleSheet(""
                           "QLineEdit:focus {"
                           "border: 2px solid #ff1d8d;"
                           "border-radius: 0px;"
                           "border-top: none;"
                           "border-left: none;"
                           "border-right: none;"
                           "color: #ff8da1;}"
                           
                           "QLineEdit {"
                           "color: white;"
                           "font-weight: 650;"
                           "font-size: 14px;"
                           "font-family: Lucida Console;"
                           "letter-spacing: 2px;}")