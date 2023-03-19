from py_Core import *
from settings.dialog_pars import ler_json, ler_json_all, delete_json, inserir_json
from settings.estilos import scroll_bar_style, edit_line_style, cbx_style, btn_edit_style, list_style_extra
from settings.req_binance import consult_price, lista_nova


class Py_Page_2(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.fazer = []
        self.allpar = ler_json_all()
        self.pares = ler_json()
        self.font12 = QFont('Arial', 12)

        self.edit_widget = QWidget()
        self.edit_widget.setMaximumSize(400, 440)
        self.edit_widget.setMinimumSize(400, 360)
        self.edit_layout = QVBoxLayout(self.edit_widget)

        self.label_all = QLabel()
        self.label_all.setText(f'Lista geral com {len(self.allpar)} pares de Cryptomoedas')
        self.label_all.setAlignment(Qt.AlignCenter)
        self.label_all.setStyleSheet('font: 11pt "Segoe UI"; color: #c3ccdf')
        self.label_despised = QLabel()
        self.label_despised.setAlignment(Qt.AlignCenter)
        self.label_despised.setStyleSheet('font: 10pt "Segoe UI"; color: #c3ccdf')

        self.icon_bx = QPixmap('assets/icons/baixar.svg')
        self.btn_all = QPushButton()
        self.btn_all.setIcon(self.icon_bx)
        self.btn_all.setStyleSheet(btn_edit_style())
        self.btn_all.setMinimumSize(30, 30)
        self.btn_all.setMaximumSize(30, 30)
        self.btn_all.clicked.connect(self.nova_lista_all)

        self.Hlay_all = QHBoxLayout()
        self.Hlay_all.setContentsMargins(0, 20, 0, 0)
        self.Hlay_all.addWidget(self.label_all)
        self.Hlay_all.addWidget(self.btn_all)

        self.list_all = QListView()
        self.list_all.setMaximumHeight(120)
        self.model = QStandardItemModel()
        self.list_all.setSelectionMode(QAbstractItemView.SingleSelection)
        self.pop_model(self.allpar)
        self.list_all.setModel(self.model)
        self.list_all.clicked.connect(self.text_changed)
        # self.list_all.selectionModel().selectionChanged.connect(self.text_changed)
        self.list_all.setStyleSheet(scroll_bar_style() + list_style_extra())

        self.lbl2 = QLabel()

        self.cbx2 = QComboBox()
        self.cbx2.setMaximumHeight(30)
        self.cbx2.setStyleSheet(cbx_style())
        self.cbx2.setPlaceholderText('Sua lista')
        self.cbx2.view().verticalScrollBar().setStyleSheet(scroll_bar_style())
        self.cbx2.view().setStyleSheet('padding: 15px;')

        self.lay_btn = QHBoxLayout()

        self.btn0 = QPushButton()
        self.btn0.setMinimumHeight(30)
        self.btn0.setStyleSheet(btn_edit_style())
        self.btn0.clicked.connect(self.salvar)

        self.btn1 = QPushButton('Limpar tudo')
        self.btn1.setMinimumHeight(30)
        self.btn1.setStyleSheet(btn_edit_style())
        self.btn1.clicked.connect(self.limpar_tudo)

        self.lbl3 = QLabel()
        self.lbl3.setFont(self.font12)
        self.lbl3.setAlignment(Qt.AlignCenter)
        self.lbl4 = QLabel()
        self.lbl4.setFont(self.font12)
        self.lbl4.setAlignment(Qt.AlignCenter)
        self.lbl5 = QLabel()
        self.lbl5.setFont(self.font12)
        self.lbl5.setAlignment(Qt.AlignCenter)
        self.lay_price = QHBoxLayout()
        self.lay_price.addWidget(self.lbl3)
        self.lay_price.addWidget(self.lbl4)
        self.lay_price.addWidget(self.lbl5)

        self.lay_edit = QHBoxLayout()
        self.items = self.allpar

        self.ledt = QLineEdit()
        self.ledt.setPlaceholderText('Pesquisar')
        self.ledt.setMinimumHeight(30)
        self.ledt.setMaximumHeight(30)
        self.ledt.textChanged.connect(self.busca)
        self.lay_edit.addWidget(self.ledt)

        self.setStyleSheet(edit_line_style())

        self.bcls = QPushButton('X')
        self.bcls.setStyleSheet(btn_edit_style())
        self.bcls.setMinimumSize(30, 30)
        self.bcls.setMaximumSize(30, 30)
        self.bcls.clicked.connect(self.limpar)
        self.lay_edit.addWidget(self.bcls)

        self.cbx2.addItems(self.pares)
        self.cbx2.setCurrentIndex(-1)
        self.cbx2.activated.connect(self.current_text_via_index)

        self.edit_layout.addLayout(self.lay_edit)
        self.edit_layout.addWidget(self.list_all)
        self.edit_layout.addWidget(self.lbl2)
        self.edit_layout.addWidget(self.cbx2)
        self.edit_layout.addLayout(self.lay_price)

        self.lay_btn.addWidget(self.btn1)
        self.lay_btn.addWidget(self.btn0)
        self.edit_layout.addLayout(self.lay_btn)
        self.edit_layout.addLayout(self.Hlay_all)
        self.edit_layout.addWidget(self.label_despised)

        self.verticalLayout_2.addWidget(self.edit_widget)
        self.verticalLayout_2.setAlignment(Qt.AlignCenter)

    def nova_lista_all(self):
        desp = lista_nova()
        self.allpar = ler_json_all()
        self.label_all.setText(f'Lista geral com {len(self.allpar)} pares de Cryptomoedas')
        self.label_despised.setText(f'{desp} pares com valor 0 absoluto foram despresados.')

    def pop_model(self, items):
        for i in items:
            item = QStandardItem(i)
            self.model.appendRow(item)

    def limpar(self):
        if self.btn0.text() == 'Inserir' and self.ledt.text() != '':
            self.btn0.setText('')
            self.fazer = []
            self.lbl3.setText('')
            self.lbl4.setText('')
            self.lbl5.setText('')
        if self.ledt.text() != '':
            self.ledt.clear()

    def limpar_tudo(self):
        if self.ledt.text() != '':
            self.ledt.clear()
        self.list_all.clearSelection()
        self.cbx2.setCurrentIndex(-1)
        self.lbl3.setText('')
        self.lbl4.setText('')
        self.lbl5.setText('')
        self.btn0.setText('')

    def busca(self, t):
        if t:
            txt = t.upper()
            list_new = []
            for item in self.allpar:
                if txt in item:
                    list_new.append(item)
            self.items = list_new
        else:
            self.items = self.allpar
        self.model.clear()
        self.pop_model(self.items)

    def text_changed(self):
        self.cbx2.setCurrentIndex(-1)
        item = ''
        for index in self.list_all.selectedIndexes():
            item = self.list_all.model().itemFromIndex(index)
        if item != '':
            text = item.text()
            self.fazer = ['Inserir', text]
            pesq = consult_price(text)
            self.btn0.setText('Inserir')
            self.lbl3.setText(f'Inserir: {text}')
            self.lbl4.setText(f'{pesq[1]}')
            self.lbl4.setStyleSheet(f'color: {pesq[3]};')
            self.lbl5.setText(f'{pesq[2]}')
            self.lbl5.setStyleSheet(f'color: {pesq[3]};')

    def current_text_via_index(self, index):
        if index >= 0:
            # tirar seleção do list_all
            self.list_all.clearSelection()
            self.lbl4.setText('')
            self.lbl5.setText('')
            ctext = self.cbx2.itemText(index)
            self.btn0.setText('Deletar')
            self.lbl3.setText(f'Deletar: {ctext}')
            self.fazer = ['Deletar', index]
            self.ledt.setText('')

    def atualiza_pares(self):
        self.pares = ler_json()
        self.cbx2.clear()
        self.cbx2.addItems(self.pares)

    def salvar(self):
        if self.fazer:
            print(self.fazer[0], self.fazer[1])
            if self.fazer[0] == 'Deletar':
                delete_json(self.fazer[1])
            else:
                inserir_json(self.fazer[1])
            self.atualiza_pares()
            self.limpar_tudo()
