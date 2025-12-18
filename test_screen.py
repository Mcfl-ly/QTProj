from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QPushButton, QVBoxLayout, QLabel


class Tela2(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.page2 = QWidget()
        layout2 = QVBoxLayout(self.page2)
        btn1 = QPushButton('SHDFAUS')
        label2 = QLabel("Página 2")
        layout2.addWidget(label2)
        layout2.addWidget(btn1)
        self.page2.setLayout(layout2)