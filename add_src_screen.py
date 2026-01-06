from PySide6.QtWidgets import   QVBoxLayout, QGridLayout, QWidget, QPushButton
from PySide6.QtCore import Qt
from textLine import TextBox
from button import Button



class AddSrc(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        #cria o layout geral do widget de login
        tela_layout = QGridLayout(self)
        tela_layout.setContentsMargins(0, 0, 0, 0)
        tela_layout.setSpacing(0)


        self.screen = QWidget()
        self.screen.setObjectName("screen")
        self.screen.setFixedSize(540,360)


        screen_layout = QVBoxLayout(self.screen)
        screen_layout.setContentsMargins(24,24,24,24)
        screen_layout.setSpacing(16)

        #textos das caixas
        self.addButton = Button("Adicionar Item")
        self.srcButton = Button("Pesquisar Item")
        #adicionando as caixas de texto a tela
        screen_layout.addWidget(self.addButton)
        screen_layout.addWidget(self.srcButton)


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