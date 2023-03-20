from py_Core import *
from gui.pages.ui_pages import Ui_StackedWidget
from gui.ui_pushbutton import PyPushButton


class UiMainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName('MainWindow')

        parent.resize(680, 620)
        parent.setMinimumSize(560, 500)

        self.central_frame = QFrame()

        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.left_frame = QFrame()
        self.left_frame.setStyleSheet('background-color: #44475A')
        self.left_frame.setMaximumWidth(50)
        self.left_frame.setMinimumWidth(50)

        self.left_menu_layout = QVBoxLayout(self.left_frame)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(40)
        self.left_menu_top_frame.setObjectName('left_menu_top_frame')
        # self.left_menu_top_frame.setStyleSheet('#left_menu_top_frame { background-color: blue; }')

        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)

        self.toggle_button = PyPushButton(
            text='Ocultar menu',
            icon_path='menu.svg'
        )
        self.btn_1 = PyPushButton(
            text='Página inicial',
            icon_path='home.svg',
            is_active=True
        )
        self.btn_2 = PyPushButton(
            text='Editar lista',
            icon_path='list_edit.svg'
        )
        self.btn_4 = PyPushButton(
            text='Carteira',
            icon_path='wallet.svg'
        )
        self.btn_3 = PyPushButton(
            text='Atualizar',
            icon_path='reload.svg'
        )

        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)
        self.left_menu_top_layout.addWidget(self.btn_4)
        self.left_menu_top_layout.addWidget(self.btn_3)

        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(40)
        self.left_menu_bottom_frame.setObjectName('left_menu_bottom_frame')
        # self.left_menu_bottom_frame.setStyleSheet('#left_menu_bottom_frame { background-color: red; }')

        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        self.btn_settings = PyPushButton(
            text='Sobre',
            icon_path='settings.svg'
        )

        self.left_menu_bottom_layout.addWidget(self.btn_settings)

        self.left_menu_label_version = QLabel('v 0.0.3')
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet('color: #C3CCDF; background-color: #4f5368')

        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.bottom_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)

        self.content = QFrame()
        self.content.setStyleSheet('background-color: #282A36')

        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet('background-color: #21232D; color: #6272A4')

        self.left_top_label = QLabel('Preço atual das suas Cryptomoedas na Binance')
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.right_top_label = QLabel('|| PAGINA INICIAL')
        self.right_top_label.setStyleSheet('font: 700 9pt "Segoe UI"')

        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)
        self.top_bar_layout.addWidget(self.left_top_label)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.right_top_label)

        self.pages = QStackedWidget()
        self.pages.setStyleSheet('font_size: 12pt; color: #F8F8F2')
        self.ui_pages = Ui_StackedWidget()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_1)

        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet('background-color: #21232D; color: #6272A4')

        self.left_bottom_babel = QLabel('Mario F. Metta')
        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.right_bottom_Label = QLabel('fev 2023')
        self.right_bottom_Label.setStyleSheet('font: 700 9pt "Segoe UI"')

        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)
        self.bottom_bar_layout.addWidget(self.left_bottom_babel)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.right_bottom_Label)

        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        self.main_layout.addWidget(self.left_frame)
        self.main_layout.addWidget(self.content)

        parent.setCentralWidget(self.central_frame)
