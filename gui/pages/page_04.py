from py_Core import *
from settings.estilos import scroll_bar_style, btn_edit_style, edit_line_style, cbx_style, table_widget, radio_button
from settings.lists_pars import ler_json, save_wallet, ler_settings, save_settings
from settings.req_binance import update_val, par


class Py_Page_4(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName(u"page_4")
        self.verticalLayout_4 = QVBoxLayout(self)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.wid_central = QWidget()
        self.lay_wid_central = QVBoxLayout(self.wid_central)
        self.lay_wid_central.setAlignment(Qt.AlignCenter)

        self.obj_settings = ler_settings()
        self.fiat = self.obj_settings['fiat']
        self.list_wallet = update_val(self.fiat)

        # QTableWidget - crypto list in wallet
        self.wallet_table = QTableWidget()
        self.wallet_table.setRowCount(len(self.list_wallet))
        self.wallet_table.setColumnCount(4)
        self.wallet_table.setMaximumWidth(560)
        self.wallet_table.setColumnWidth(0, 200)
        self.wallet_table.setColumnWidth(1, 100)
        self.wallet_table.setColumnWidth(2, 110)
        self.wallet_table.setColumnWidth(3, 120)
        self.wallet_table.setStyleSheet(table_widget())
        self.wallet_table.horizontalHeader().setStyleSheet('::section {background: #44475A;}')
        self.wallet_table.verticalHeader().setStyleSheet('::section {background: #777A8D;}')
        self.wallet_table.verticalHeader().sectionClicked.connect(self.edit_par)

        self.lay_total = QHBoxLayout()
        pref_total = 'R$' if self.fiat == 'BRL' else 'US$'
        self.lbl_total = QLabel(pref_total)
        self.lbl_total.setAlignment(Qt.AlignRight)
        self.lbl_total.setFont(QFont('Arial', 11, 700))
        self.val_total = QLabel()
        self.val_total.setFont(QFont('Arial', 11, 400))
        self.lay_total.addWidget(self.lbl_total)
        self.lay_total.addWidget(self.val_total)

        self.popular_table()

        self.lay_H_sel = QHBoxLayout()
        self.lay_H_sel.setContentsMargins(10, 5, 10, 5)

        self.group_fiat = QButtonGroup()
        self.lay_radio = QHBoxLayout()
        self.btn_brl = QRadioButton('BRL')
        self.btn_brl.setStyleSheet(radio_button())
        self.btn_brl.setChecked(True if self.fiat == 'BRL' else False)
        self.btn_usdt = QRadioButton('USDT')
        self.btn_usdt.setStyleSheet(radio_button())
        self.btn_usdt.setChecked(True if self.fiat == 'USDT' else False)
        self.btn_busd = QRadioButton('BUSD')
        self.btn_busd.setStyleSheet(radio_button())
        self.btn_busd.setChecked(True if self.fiat == 'BUSD' else False)
        self.group_fiat.addButton(self.btn_brl)
        self.group_fiat.addButton(self.btn_usdt)
        self.group_fiat.addButton(self.btn_busd)
        self.lay_radio.addWidget(self.btn_brl)
        self.lay_radio.addWidget(self.btn_usdt)
        self.lay_radio.addWidget(self.btn_busd)
        self.group_fiat.buttonClicked.connect(self.on_fiat_clicked)

        self.sel_par = QComboBox()
        self.sel_par.setFixedSize(QSize(200, 30))
        self.sel_par.setStyleSheet(cbx_style())
        self.search_pars()
        self.sel_par.setPlaceholderText('Escolha um par da sua lista')
        self.sel_par.setCurrentIndex(-1)
        self.sel_par.view().verticalScrollBar().setStyleSheet(scroll_bar_style())
        self.sel_par.view().setStyleSheet('padding: 15px;')

        self.btn_add = QPushButton('Selecionar')
        self.btn_add.setFixedSize(QSize(75, 30))
        self.btn_add.setStyleSheet(btn_edit_style())
        self.btn_add.clicked.connect(self.add_par)

        self.lay_H_sel.addLayout(self.lay_radio)
        self.lay_H_sel.addWidget(self.sel_par)
        self.lay_H_sel.addWidget(self.btn_add)

        self.painel_wid = QWidget()
        self.painel_lay = QVBoxLayout(self.painel_wid)
        self.painel_wid.setMaximumWidth(560)

        self.lay_H_edit = QHBoxLayout()
        self.lay_H_edit.setContentsMargins(10, 5, 10, 10)

        self.par_edit = QLineEdit()
        self.par_edit.setMinimumHeight(30)
        self.setStyleSheet(edit_line_style())
        self.par_edit.setReadOnly(True)
        self.par_edit.setPlaceholderText('Par escolhido')

        self.qtd_edit = QLineEdit()
        self.qtd_edit.setMinimumHeight(30)
        self.qtd_edit.setPlaceholderText('Quant. em carteira')
        self.qtd_edit.setValidator(QDoubleValidator())
        self.qtd_edit.setAlignment(Qt.AlignCenter)

        self.btn_cls = QPushButton('Limpar')
        self.btn_cls.setFixedSize(QSize(75, 30))
        self.btn_cls.setStyleSheet(btn_edit_style())
        self.btn_cls.clicked.connect(self.clear_all)
        self.btn_del = QPushButton('Deletar')
        self.btn_del.setFixedSize(QSize(75, 30))
        self.btn_del.setStyleSheet(btn_edit_style())
        self.btn_del.clicked.connect(self.delete_par)
        self.btn_edit = QPushButton(' Salvar ')
        self.btn_edit.setFixedSize(QSize(75, 30))
        self.btn_edit.setStyleSheet(btn_edit_style())
        self.btn_edit.clicked.connect(self.save_edit)

        self.lay_H_edit.addWidget(self.par_edit)
        self.lay_H_edit.addWidget(self.qtd_edit)
        self.lay_H_edit.addWidget(self.btn_cls)
        self.lay_H_edit.addWidget(self.btn_del)
        self.lay_H_edit.addWidget(self.btn_edit)

        self.painel_lay.addLayout(self.lay_H_sel)
        self.painel_lay.addLayout(self.lay_H_edit)

        self.lay_wid_central.addWidget(self.wallet_table)
        self.lay_wid_central.addLayout(self.lay_total)
        self.lay_wid_central.addWidget(self.painel_wid)

        self.verticalLayout_4.addWidget(self.wid_central)

    def search_pars(self):
        self.sel_par.clear()
        pref = ler_json()
        n = len(self.fiat)
        n = n * -1
        monitored = []
        for par in pref:
            if par[n:] == self.fiat:
                add = True
                for item in self.list_wallet:
                    if par in item:
                        add = False
                if add:
                    monitored.append(par)
        self.sel_par.addItems(monitored)

    def update_values(self):
        self.list_wallet = update_val(self.fiat)
        self.popular_table()

    def on_fiat_clicked(self, button):
        self.fiat = button.text()
        obj = self.obj_settings
        obj['fiat'] = self.fiat
        save_settings(obj)
        pref_total = 'R$' if self.fiat == 'BRL' else 'US$'
        self.lbl_total.setText(pref_total)
        self.update_values()
        self.search_pars()
        self.clear_all()

    def clear_all(self):
        self.qtd_edit.setText('')
        self.par_edit.setText('')
        self.sel_par.setCurrentIndex(-1)

    def popular_table(self):
        self.wallet_table.clear()
        total = 0
        self.wallet_table.setRowCount(len(self.list_wallet))
        for i, row in enumerate(self.list_wallet):
            self.wallet_table.setHorizontalHeaderItem(0, QTableWidgetItem('PAR DE MOEDAS'))
            self.wallet_table.setHorizontalHeaderItem(1, QTableWidgetItem('VALOR ATUAL'))
            self.wallet_table.setHorizontalHeaderItem(2, QTableWidgetItem('QUANT'))
            self.wallet_table.setHorizontalHeaderItem(3, QTableWidgetItem('SUBTOTAL'))
            item0 = QTableWidgetItem(row[0])
            item1 = QTableWidgetItem(row[1])
            item2 = QTableWidgetItem(row[2])
            item3 = QTableWidgetItem(row[3])
            total = total + float(row[3])
            item0.setTextAlignment(Qt.AlignCenter | Qt.AlignCenter)
            item1.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item2.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            item3.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.wallet_table.setItem(i, 0, item0)
            self.wallet_table.setItem(i, 1, item1)
            self.wallet_table.setItem(i, 2, item2)
            self.wallet_table.setItem(i, 3, item3)
        self.val_total.setText(f'{float(total):.2f}')

    def add_par(self):
        txt = self.sel_par.currentText()
        if txt != '':
            self.par_edit.setText(txt)
            self.qtd_edit.setText('')
            self.qtd_edit.setFocus()
            self.btn_edit.setText('INSERIR')
            self.btn_del.setEnabled(False)

    def delete_par(self):
        d = self.wallet_table.currentRow()
        items = []
        for i, item in enumerate(self.list_wallet):
            if i != d:
                items.append(item)
        save_wallet(items, self.fiat)
        self.update_values()
        self.search_pars()
        self.clear_all()

    def edit_par(self):
        i = self.wallet_table.currentRow()
        item = self.list_wallet[i]
        self.par_edit.setText(item[0])
        self.qtd_edit.setText(item[2])
        self.btn_edit.setText('ALTERAR')
        self.btn_del.setEnabled(True)
        self.sel_par.setCurrentIndex(-1)

    def save_edit(self):
        if self.par_edit.text() != '' and self.qtd_edit.text() != '':
            items = self.list_wallet
            val = par(0, self.par_edit.text())
            qtd = self.qtd_edit.text().replace(',', '.')
            sub = float(val[2]) * float(qtd)
            item = [self.par_edit.text(), val[2], qtd, str(sub)]
            if self.btn_edit.text() == 'INSERIR':
                items.append(item)
            else:
                i = self.wallet_table.currentRow()
                items[i] = item
            save_wallet(items, self.fiat)
            self.update_values()
            self.search_pars()
            self.clear_all()
