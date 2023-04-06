def scroll_bar_style():
    st = """
     QScrollBar:vertical {
         border: 0;
         border-radius: 6px;
         background: #21232D;
         width: 12px;
         margin: 22px 0 22px 0;
     }
     QScrollBar::handle:vertical {
         border-radius: 6px;
         background: #44475A;
         min-height: 20px;
     }
     QScrollBar::add-line:vertical {
         border: 0;
         border-radius: 6px;
         background: #21232D;
         height: 12px;
         subcontrol-position: bottom;
         subcontrol-origin: margin;
     }

     QScrollBar::sub-line:vertical {
         border: 0;
         border-radius: 6px;
         background: #21232D;
         height: 12px;
         subcontrol-position: top;
         subcontrol-origin: margin;
     }
     QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
         border: 0;
         width: 3px;
         height: 3px;
         background: #0F0;
     }
     QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
         background: none;
     }
    """
    return st


def table_widget():
    tw = """
        QTableWidget {
            selection-background-color: #24344a;
            selection-border: 2px outset #24344a;
            selection-color: #fff;
        }
        QTableWidget QTableCornerButton::section {
            background: #24344a;
            border: 2px outset #24344a;
        }
    """
    return tw


def radio_button():
    rb = """
        QRadioButton::indicator:checked {
            border-radius: 6px;
            border: 3px solid #0f0;
        }
    """
    return rb


def edit_line_style():
    els = f"""
                QLineEdit {{
                    border: 1px solid #44475A;
                    border-radius: 15px;
                    padding-left: 15px;
                }}
                QLineEdit:hover {{
                    border: 1px solid #c3ccdf;
                }}
                QLineEdit:focus {{
                    border: 1px solid #0f0;
                }}"""
    return els


def btn_edit_style():
    bes = f'''
            QPushButton {{
              border-radius: 15px;
              border: 1 solid #44475A;
              color: #c3ccdf;
            }}
            QPushButton:hover {{
                border: 1px solid #c3ccdf;
            }}
            QPushButton:pressed {{
                border: 1px solid #0f0;
            }}
          '''
    return bes


def list_style_extra():
    lse = f'''
              QListView {{
                  padding-left: 15px;
                  border: 1 solid #44475A;
                  border-radius: 15px;
              }}
          '''
    return lse


def cbx_style():
    cbs = '''
            border: 1 solid #44475A;
            border-radius: 15px;
            selection-background-color: #44475A;
            padding-left: 15px;
          '''
    return cbs


def cbx_scroll_style():
    css = '''
            border: 1 solid #44475A;
            border-radius: 6px;
            background-color: #44475A;
            width: 12px;
          '''
    return css
