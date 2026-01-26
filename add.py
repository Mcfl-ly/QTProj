from PySide6.QtWidgets import QVBoxLayout, QGridLayout, QWidget, QComboBox, QMenu
from PySide6.QtCore import Qt, Slot
from textLine import TextBox
from button import Button
from datetime import datetime
import sqlite3

class AddItem(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        # cria o layout geral do widget de login
        tela_layout = QGridLayout(self)
        tela_layout.setContentsMargins(0, 0, 0, 0)
        tela_layout.setSpacing(0)

        self.screen = QWidget()
        self.screen.setObjectName("screen")
        self.screen.setFixedSize(720, 480)

        screen_layout = QVBoxLayout(self.screen)
        screen_layout.setContentsMargins(24, 24, 24, 24)
        screen_layout.setSpacing(16)

        # textos das caixas
        self.item_name = TextBox()
        self.item_name.setPlaceholderText("Nome do item")

        self.categoria = TextBox()
        self.categoria.setPlaceholderText("Categoria do item")
        self.combo = QComboBox()
        self.combo.setStyleSheet("QComboBox{"
                           "color: white;"
                           "font-weight: 650;"
                           "font-size: 14px;"
                           "font-family: Lucida Console;"
                           "letter-spacing: 2px;"
                            "padding: 15px 60px;}")
        self.combo.setEditable(False)
        self.combo.addItem("Categoria")
        self.combo.model().item(0).setEnabled(False)
        self.combo.addItems(["opção 1", "opção 2", "opção 3"])

        self.combo2 = QComboBox()
        self.combo2.setStyleSheet("QComboBox{"
                            "color: white;"
                            "font-weight: 650;"
                            "font-size: 14px;"
                            "font-family: Lucida Console;"
                            "letter-spacing: 2px;"
                            "padding: 15px 60px;}")
        self.combo2.setEditable(False)
        self.combo2.addItem("Filial")
        self.combo2.model().item(0).setEnabled(False)
        self.combo2.addItems(["filial 1", "filial 2", "filial 3"])



        # menu = QMenu()
        # menu.addAction("option 1", lambda: self.categoria.setText("Opção 1"))
        # menu.addAction("option 2", lambda: self.categoria.setText("Opção 2"))
        # menu.addAction("option 3", lambda: self.categoria.setText("Opção 3"))
        # self.categoria.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.categoria.customContextMenuRequested.connect(lambda pos: menu.exec(self.categoria.mapToGlobal(pos)))


        self.preco = TextBox()
        self.preco.setPlaceholderText("Valor do item")
        self.quantidade = TextBox()
        self.quantidade.setPlaceholderText("Quantidade")

        self.addButton = Button("Adicionar")
        self.addButton.setFixedWidth(200)
        self.addButton.clicked.connect(self.adicionar)
        self.back_button = Button("< Voltar")
        self.back_button.clicked.connect(self.go_back)


        #PEGANDO OS DADOS INSERIDOS










        # adicionando as caixas de texto a tela
        screen_layout.addWidget(self.item_name, alignment=Qt.AlignmentFlag.AlignCenter)

        screen_layout.addWidget(self.preco, alignment=Qt.AlignmentFlag.AlignCenter)
        screen_layout.addWidget(self.quantidade, alignment=Qt.AlignmentFlag.AlignCenter)
        screen_layout.addWidget(self.combo, alignment=Qt.AlignmentFlag.AlignCenter)
        screen_layout.addWidget(self.combo2, alignment=Qt.AlignmentFlag.AlignCenter)
        screen_layout.addWidget(self.addButton, alignment=Qt.AlignmentFlag.AlignCenter)
        screen_layout.addWidget(self.back_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # adicionando a telinha de login ao widget inteiro e alinhando ao centro
        tela_layout.addWidget(self.screen, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        tela_layout.setRowStretch(0, 1)
        tela_layout.setRowStretch(2, 1)
        tela_layout.setColumnStretch(0, 1)
        tela_layout.setColumnStretch(2, 1)

    def adicionar(self):
        banco = sqlite3.connect('banco.db')
        cursor = banco.cursor()

        data = datetime.now().strftime('%Y-%m-%d')
        prod_name = self.item_name.text()
        prod_value = self.preco.text()
        prod_categoria = self.combo.currentText()
        filial = self.combo2.currentText()
        quantidade = int(self.quantidade.text())

        print(prod_name, prod_value, prod_categoria, filial)

    def go_back(self):
        self.stacked_widget.setCurrentIndex(1)