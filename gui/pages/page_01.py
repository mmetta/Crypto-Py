from gui.pages.list_crypto import Cryptos
from py_Core import *
from settings.req_binance import data_e_hora


class Py_Page_1(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.verticalLayout = QVBoxLayout()

        self.list_crypto = Cryptos()

        self.statusLayout = QHBoxLayout()
        self.statusLabel = QLabel()
        self.statusLabel.setText('Atualizado ' + data_e_hora())
        self.statusLabel.setAlignment(Qt.AlignCenter)
        self.statusLayout.addWidget(self.statusLabel)

        self.verticalLayout.addWidget(self.list_crypto)
        self.verticalLayout.addLayout(self.statusLayout)
        self.setLayout(self.verticalLayout)
