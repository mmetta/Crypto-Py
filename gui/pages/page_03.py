from py_Core import *


class Py_Page_3(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.wid_central = QWidget()
        self.lay_wid_central = QVBoxLayout(self.wid_central)
        self.lay_wid_central.setAlignment(Qt.AlignCenter)

        self.label_img = QLabel()
        self.logo_img = QPixmap('assets/favicon.png')
        self.label_img.setPixmap(self.logo_img)
        self.label_img.setAlignment(Qt.AlignCenter)

        self.label_title = QLabel('Crypto PY')
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setStyleSheet('font: 700 16pt "Segoe UI"; color: #c3ccdf')
        self.label_title.setContentsMargins(0, 0, 0, 40)

        self.label_3 = QLabel()
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumWidth(500)
        self.label_3.setText('Aplicativo desenvolvido em Python3 - PySide6 para\n' +
                             'acompanhar cotações de pares de Cryptomoedas.\n\n' +
                             'As consultas são feitas na API2 Binance e trazem\n' +
                             'informações de preço e % de oscilação.\n\n' +
                             'Você pode atualizar as informações e adicionar ou\n' +
                             'remover pares da sua lista de acompanhamento.\n\n' +
                             'Na aba Carteira você pode anotar suas quantidades\n' +
                             'de cada ativo e manter atualizado seu saldo sem a\n' +
                             'necessidade de conectar-se a exchange, evitando assim\n'+
                             'riscos desnecessários.')
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setStyleSheet('font: 12pt "Segoe UI"; color: #c3ccdf')
        self.label_3.setContentsMargins(0, 0, 0, 40)

        self.label_ass = QLabel('Mario F Metta\n2023')
        self.label_ass.setStyleSheet('font: 700 9pt "Segoe UI"; color: #c3ccdf')
        self.label_ass.setAlignment(Qt.AlignCenter)

        self.lay_wid_central.addWidget(self.label_img)
        self.lay_wid_central.addWidget(self.label_title)
        self.lay_wid_central.addWidget(self.label_3)
        self.lay_wid_central.addWidget(self.label_ass)

        self.verticalLayout_3.addWidget(self.wid_central)
