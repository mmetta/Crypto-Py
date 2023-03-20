from py_Core import *


class Py_Page_4(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.wid_central = QWidget()
        self.lay_wid_central = QVBoxLayout(self.wid_central)
        self.lay_wid_central.setAlignment(Qt.AlignCenter)

        self.label_title = QLabel('Carteira')
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setStyleSheet('font: 700 16pt "Segoe UI"; color: #c3ccdf')
        self.label_title.setContentsMargins(0, 0, 0, 40)

        self.lay_wid_central.addWidget(self.label_title)

        self.verticalLayout_3.addWidget(self.wid_central)
