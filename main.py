import sys

from py_Core import *
from gui.ui_main_window import UiMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Crypto PY')

        self.ui = UiMainWindow()
        self.ui.setup_ui(self)

        self.tmp = QTimer()

        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # Btn home
        self.ui.btn_1.clicked.connect(self.show_page_1)

        # Btn edit list
        self.ui.btn_2.clicked.connect(self.show_page_2)

        # Btn reload
        self.ui.btn_3.clicked.connect(self.list_reload)

        # Btn wallet
        self.ui.btn_4.clicked.connect(self.show_page_4)

        # Btn settings
        self.ui.btn_settings.clicked.connect(self.show_page_3)

        self.show()

    # Reset BTN Selection
    def reset_selection(self):
        for btn in self.ui.left_frame.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    # Atualizar a lista
    def list_reload(self):
        self.ui.ui_pages.page_1.atual()
        self.ui.ui_pages.page_4.update_values()
        self.ui.ui_pages.page_4.search_pars()

    # Btn home function
    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.right_top_label.setText('|| PÁGINA PRINCIPAL')
        self.ui.btn_1.set_active(True)

    # Btn widgets function
    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.right_top_label.setText('|| EDITAR LISTA')
        self.ui.btn_2.set_active(True)

    # Btn widgets function
    def show_page_4(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_4)
        self.ui.right_top_label.setText('|| CARTEIRA')
        self.ui.btn_4.set_active(True)

    # Btn pase gettings
    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.right_top_label.setText('|| SOBRE')
        self.ui.btn_settings.set_active(True)

    # Toggle button
    def toggle_button(self):
        menu_width = self.ui.left_frame.width()
        width = 50

        if menu_width == 50:
            width = 240

        self.animation = QPropertyAnimation(self.ui.left_frame, b'minimumWidth')
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("assets/favicon.ico"))
    pixmap = QPixmap('assets/splash.png')
    splash = QSplashScreen(pixmap)
    splash.show()

    timer = QTimer()
    timer.timeout.connect(print('start'))
    timer.start(6000)

    window = MainWindow()
    window.show()
    splash.finish(window)
    # app.exec()
    sys.exit(app.exec())
