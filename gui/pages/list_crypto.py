from py_Core import *
from settings.req_binance import consulta


class CustomWidget(QWidget):
    def __init__(self, par, parent=None):
        super().__init__(parent)
        self.label1 = QLabel(par[0])
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFont(QFont('Arial', 14, 700))
        self.label1.setStyleSheet('background: transparent;')
        self.label2 = QLabel(par[1])
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet('background: transparent; color: #ffffff; font-size: 14pt;')
        self.label3 = QLabel(f'{par[2]}%')
        cor = '#55ff00' if float(par[2]) > 0 else '#ff5500'
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setStyleSheet(f'background: transparent; color: {cor}; font-size: 14pt;')

        layout = QHBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)

        self.setLayout(layout)


class Cryptos(QListWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setObjectName(u"page_1")

        self.atual()

        self.setStyleSheet("""
            QListWidget::item:selected { background-color: #24344a; }
        """)

    def atual(self):
        list_par = consulta()
        self.clear()
        for par in list_par:
            item = QListWidgetItem()
            custom_widget = CustomWidget(par)
            item.setSizeHint(custom_widget.sizeHint())
            self.addItem(item)
            self.setItemWidget(item, custom_widget)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.clearSelection()
        else:
            super().keyPressEvent(event)
