# import timeit

from py_Core import *
from settings.estilos import scroll_bar_style
from settings.req_binance import consulta, data_e_hora


class Py_Page_1(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName(u"page_1")

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 10, 20, 10)

        self.statusLayout = QHBoxLayout()
        self.statusLabel = QLabel()
        self.statusLabel.setAlignment(Qt.AlignCenter)
        self.statusLayout.addWidget(self.statusLabel)

        self.verticalLayout.addLayout(self.statusLayout)

        self.scroll = QScrollArea()
        self.scrollbar = self.scroll.verticalScrollBar()
        self.scrollbar.setStyleSheet(scroll_bar_style())

        self.listWidget = QWidget()
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumWidth(590)
        self.listWidget.setContentsMargins(0, 0, 0, 0)

        self.vbox = QVBoxLayout(self.listWidget)
        self.atual()

    def retranslateUi(self, val, cor):
        wid = QWidget()
        wid.setMinimumHeight(30)
        wid.setMaximumHeight(30)
        wid.setContentsMargins(20, 0, 0, 0)

        horizontalLayout = QHBoxLayout(wid)
        horizontalLayout.setObjectName(u"horizontalLayout")
        horizontalLayout.setContentsMargins(0, 0, 0, 0)

        label = QLabel(val[0])
        label.setStyleSheet('font: 700 12pt "Segoe UI"; color: #FFF')
        label_2 = QLabel(val[1])
        label_2.setAlignment(Qt.AlignCenter)
        label_2.setStyleSheet(f'font: 12pt "Segoe UI"; color:{cor}')
        label_3 = QLabel(f'{val[2]}%')
        label_3.setAlignment(Qt.AlignCenter)
        label_3.setStyleSheet(f'font: 12pt "Segoe UI"; color:{cor}')
        horizontalLayout.addWidget(label)
        horizontalLayout.addWidget(label_2)
        horizontalLayout.addWidget(label_3)
        self.vbox.addWidget(wid)

    def atual(self):
        # inicio = timeit.default_timer()
        # Limpa o vbox caso já tenha widgets nele
        while self.vbox.count():
            child = self.vbox.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        vals = consulta()
        for row, val in enumerate(vals):
            if float(val[2]) > 0:
                cor = '#00FF00'
            else:
                cor = '#FF0000'
            self.retranslateUi(val, cor)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setStyleSheet('border: 0')
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.listWidget)

        self.verticalLayout.addWidget(self.scroll)

        dh = data_e_hora()
        self.statusLabel.setText(f'Atualizado: {dh}')
        # fim = timeit.default_timer()
        # print(fim - inicio)
